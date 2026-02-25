from dataclasses import dataclass


@dataclass
class GPU:
    manufacturer: str
    name: str
    capacity: int
