import rclpy
from rclpy.node import Node
from unitree_hg.msg import (MotorCmd,LowCmd)
from dataclasses import dataclass, field
from typing import List

@dataclass
class MotorCmdRaw:
    mode: int        
    q: float         
    dq: float       
    tau: float     
    Kp: float    
    Kd: float     
    reserve: int = 0 

@dataclass
class LowCmdRaw:
    modePr: int                           
    modeMachine: int                      
    motorCmd: List[MotorCmdRaw] = field(default_factory=lambda: [MotorCmdRaw(0,0,0,0,0,0) for _ in range(35)])
    reserve: List[int] = field(default_factory=lambda: [0]*4)  
    crc: int = 0    

import struct
from typing import List

def get_crc(msg) -> None:
    """
    Compute CRC32 for LowCmd-like object and update msg.crc
    Assumes msg has same fields as LowCmd dataclass.
    """
    # Build a raw LowCmd copy
    raw = LowCmdRaw(
        modePr=msg.mode_pr,
        modeMachine=msg.mode_machine,
        motorCmd=[
            MotorCmdRaw(
                mode=m.mode,
                q=m.q,
                dq=m.dq,
                tau=m.tau,
                Kp=m.kp,
                Kd=m.kd,
                reserve=m.reserve
            )
            for m in msg.motor_cmd
        ],
        reserve=list(msg.reserve),
        crc=0
    )

    # Serialize raw into bytes (mimicking C memory layout: little-endian, 32-bit words)
    packed = bytearray()
    packed += struct.pack("<B", raw.modePr)
    packed += struct.pack("<B", raw.modeMachine)

    for mc in raw.motorCmd:
        packed += struct.pack("<B", mc.mode)
        packed += struct.pack("<f", mc.q)
        packed += struct.pack("<f", mc.dq)
        packed += struct.pack("<f", mc.tau)
        packed += struct.pack("<f", mc.Kp)
        packed += struct.pack("<f", mc.Kd)
        packed += struct.pack("<I", mc.reserve)

    for r in raw.reserve:
        packed += struct.pack("<I", r)

    # Pad to 32-bit word alignment if necessary
    if len(packed) % 4 != 0:
        packed += b"\x00" * (4 - (len(packed) % 4))

    # Convert to list of uint32 words
    words = list(struct.unpack("<" + "I" * (len(packed) // 4), packed))

    # Compute CRC (exclude last 32-bit word reserved for crc)
    raw.crc = crc32_core(words, len(words) - 1)
    msg.crc = raw.crc 

def crc32_core(data: list[int], length: int) -> int:
    CRC32 = 0xFFFFFFFF
    dwPolynomial = 0x04C11DB7

    for i in range(length):
        xbit = 1 << 31
        value = data[i] & 0xFFFFFFFF  # ensure 32-bit
        for _ in range(32):
            if CRC32 & 0x80000000:
                CRC32 = ((CRC32 << 1) ^ dwPolynomial) & 0xFFFFFFFF
            else:
                CRC32 = (CRC32 << 1) & 0xFFFFFFFF

            if value & xbit:
                CRC32 ^= dwPolynomial
            xbit >>= 1

    return CRC32 & 0xFFFFFFFF