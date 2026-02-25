from dataclasses import dataclass
from ciacs.core.dataclasses.os import OS
from ciacs.core.dataclasses.hardware import Hardware
from ciacs.core.dataclasses.software import Software


@dataclass
class Computer():
    id: bytes
    ip: str
    os: OS
    hardware: Hardware
    software: Software
