from dataclasses import dataclass


@dataclass
class OS:
    name: str
    build: str
    bits: int
