from dataclasses import dataclass
from ciacs.core.dataclasses.cpu import CPU
from ciacs.core.dataclasses.gpu import GPU
from ciacs.core.dataclasses.ram import RAM
from ciacs.core.dataclasses.disk import Disk
from ciacs.core.dataclasses.motherboard import MotherBoard


@dataclass
class Hardware:
    motherboard: MotherBoard
    cpu: CPU
    gpu: GPU
    ram: RAM
    disk: Disk
