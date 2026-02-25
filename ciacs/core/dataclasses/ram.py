from dataclasses import dataclass


@dataclass
class RAM:
    manufacturer: str
    name: str
    type: str
    capacity: int
