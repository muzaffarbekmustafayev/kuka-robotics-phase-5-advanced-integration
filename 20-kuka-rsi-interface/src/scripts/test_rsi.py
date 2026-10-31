"""Unit tests for KUKA RSI protocol parsing and packet synthesis."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from rsi_socket_server import RsiProtocolHandler, RsiPacket


def test_rsi_xml_parsing_exact():
    handler = RsiProtocolHandler()
    xml_data = (
        b'<Rob Type="KUKA">'
        b'<RIst X="520.12" Y="-10.50" Z="380.00" A="5.0" B="85.0" C="-2.0"/>'
        b'<AIPos A1="12.0" A2="-80.0" A3="75.0" A4="0.0" A5="30.0" A6="-5.0"/>'
        b'<IPOC>50000</IPOC>'
        b'</Rob>'
    )
    pkt = handler.parse_robot_xml(xml_data)

    assert pkt.ipoc == 50000
    assert np.isclose(pkt.cartesian_act[0], 520.12)
    assert np.isclose(pkt.cartesian_act[1], -10.50)
    assert np.isclose(pkt.axis_act[0], 12.0)
    assert np.isclose(pkt.axis_act[1], -80.0)


def test_ipoc_continuity_and_drop_tracking():
    handler = RsiProtocolHandler()

    pkt1 = b'<Rob><IPOC>100</IPOC></Rob>'
    pkt2 = b'<Rob><IPOC>101</IPOC></Rob>'
    pkt3 = b'<Rob><IPOC>103</IPOC></Rob>'  # 1 packet dropped (102 missing)

    handler.parse_robot_xml(pkt1)
    handler.parse_robot_xml(pkt2)
    assert handler.packet_drops == 0

    handler.parse_robot_xml(pkt3)
    assert handler.packet_drops == 1


def test_create_correction_xml_structure():
    handler = RsiProtocolHandler()
    corr = np.array([1.5, -0.5, 0.25, 0.0, 0.1, 0.0])
    xml_reply = handler.create_correction_xml(ipoc=2024, cartesian_corr=corr)

    text = xml_reply.decode("utf-8")
    assert "<Sen Type=\"ImFree\">" in text
    assert '<IPOC>2024</IPOC>' in text
    assert 'X="1.5000"' in text
    assert 'Z="0.2500"' in text
