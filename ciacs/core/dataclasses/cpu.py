from dataclasses import dataclass


@dataclass
class CPU:
    manufacturer: str
    name: str
    cores: int
    threads: int
    speed: int
    bits: int
