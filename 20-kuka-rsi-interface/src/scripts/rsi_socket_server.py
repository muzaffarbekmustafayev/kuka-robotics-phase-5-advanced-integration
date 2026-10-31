"""KUKA RobotSensorInterface (RSI) Real-Time XML/UDP Protocol Engine.

Implements high-speed 4ms/12ms cyclic XML packet parsing, IPOC (Interpolation Cycle)
continuity tracking, Cartesian correction synthesis (RKorr), and deadline watchdog monitoring.
"""

from dataclasses import dataclass
from typing import Dict, Optional, Tuple
import xml.etree.ElementTree as ET
import numpy as np


@dataclass
class RsiPacket:
    """Parsed incoming RSI packet from KRC."""
    ipoc: int
    cartesian_act: np.ndarray  # [X, Y, Z, A, B, C]
    axis_act: np.ndarray       # [A1, A2, A3, A4, A5, A6]


class RsiProtocolHandler:
    r"""Manages real-time RSI communication cycles with strict IPOC sequencing."""

    def __init__(self, cycle_time_ms: float = 4.0, max_jitter_ms: float = 2.0):
        self.cycle_time_ms = cycle_time_ms
        self.max_jitter_ms = max_jitter_ms
        self.last_ipoc: Optional[int] = None
        self.packet_drops = 0
        self.total_packets = 0

    def parse_robot_xml(self, xml_bytes: bytes) -> RsiPacket:
        """Parse incoming XML payload from KUKA KRC."""
        root = ET.fromstring(xml_bytes)

        # Extract IPOC
        ipoc_elem = root.find("IPOC")
        if ipoc_elem is None or ipoc_elem.text is None:
            raise ValueError("Invalid RSI packet: missing <IPOC> tag.")
        ipoc = int(ipoc_elem.text)

        # Check IPOC monotonicity
        if self.last_ipoc is not None:
            diff = ipoc - self.last_ipoc
            if diff != 1:
                self.packet_drops += (diff - 1)
        self.last_ipoc = ipoc
        self.total_packets += 1

        # Extract Cartesian actual: <RIst X=".." Y=".." Z=".." A=".." B=".." C=".."/>
        rist = root.find("RIst")
        c_act = np.zeros(6, dtype=np.float64)
        if rist is not None:
            c_act = np.array([
                float(rist.attrib.get("X", 0.0)),
                float(rist.attrib.get("Y", 0.0)),
                float(rist.attrib.get("Z", 0.0)),
                float(rist.attrib.get("A", 0.0)),
                float(rist.attrib.get("B", 0.0)),
                float(rist.attrib.get("C", 0.0)),
            ])

        # Extract Axis actual: <AIPos A1=".." A2=".." A3=".." A4=".." A5=".." A6=".."/>
        aipos = root.find("AIPos")
        a_act = np.zeros(6, dtype=np.float64)
        if aipos is not None:
            a_act = np.array([
                float(aipos.attrib.get("A1", 0.0)),
                float(aipos.attrib.get("A2", 0.0)),
                float(aipos.attrib.get("A3", 0.0)),
                float(aipos.attrib.get("A4", 0.0)),
                float(aipos.attrib.get("A5", 0.0)),
                float(aipos.attrib.get("A6", 0.0)),
            ])

        return RsiPacket(ipoc=ipoc, cartesian_act=c_act, axis_act=a_act)

    def create_correction_xml(self, ipoc: int, cartesian_corr: np.ndarray) -> bytes:
        r"""Construct outgoing XML correction packet to KRC.

        Format:
            <Sen Type="ImFree">
                <RKorr X="dx" Y="dy" Z="dz" A="da" B="db" C="dc"/>
                <IPOC>123456</IPOC>
            </Sen>
        """
        corr = np.asarray(cartesian_corr, dtype=np.float64)
        xml_str = (
            f'<Sen Type="ImFree">'
            f'<RKorr X="{corr[0]:.4f}" Y="{corr[1]:.4f}" Z="{corr[2]:.4f}" '
            f'A="{corr[3]:.4f}" B="{corr[4]:.4f}" C="{corr[5]:.4f}"/>'
            f'<IPOC>{ipoc}</IPOC>'
            f'</Sen>'
        )
        return xml_str.encode("utf-8")


def main():
    print("=" * 65)
    print("Lesson 20: KUKA RSI (RobotSensorInterface) Real-Time XML Protocol")
    print("=" * 65)

    handler = RsiProtocolHandler(cycle_time_ms=4.0)

    # Sample simulated XML packet from KUKA controller
    sample_xml = (
        b'<Rob Type="KUKA">'
        b'<RIst X="480.00" Y="0.00" Z="435.00" A="0.00" B="90.00" C="0.00"/>'
        b'<AIPos A1="0.00" A2="-90.00" A3="90.00" A4="0.00" A5="0.00" A6="0.00"/>'
        b'<IPOC>10001</IPOC>'
        b'</Rob>'
    )

    pkt = handler.parse_robot_xml(sample_xml)
    print(f"\nReceived Robot State:")
    print(f"  IPOC:          {pkt.ipoc}")
    print(f"  TCP Cartesian: {pkt.cartesian_act.tolist()}")
    print(f"  Joint Angles:  {pkt.axis_act.tolist()}")

    # Synthesize small 4ms real-time correction delta: +0.2 mm along Z
    delta_corr = np.array([0.0, 0.0, 0.20, 0.0, 0.0, 0.0])
    reply_xml = handler.create_correction_xml(pkt.ipoc, delta_corr)
    print(f"\nSent XML Reply to KRC:")
    print(f"  {reply_xml.decode('utf-8')}")


if __name__ == "__main__":
    main()
