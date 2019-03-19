from typing import Dict, Tuple, List, Any

from src.main.object_orientation import LabStatus


class Lab:
    def __init__(self, name: str = ""):
        self.lab_name: str = name


class Student:
    def __init__(self):
        self.labs: Dict[str, List[Any]] = {}

    def get_lab(self, lab_name: str) -> Lab:
        return self.labs[lab_name][0]

    def set_lab_status(self, lab_name: str, lab_status: LabStatus):
        if lab_name not in self.labs:
            raise ValueError()
        else:
            self.labs[lab_name][1] = lab_status

    def fork_lab(self, lab: Lab):
        self.labs[lab.lab_name] = [lab, LabStatus.PENDING]

    def get_lab_status(self, lab_name: str) -> LabStatus:
        return self.labs[lab_name][1]

    def __str__(self) -> str:
        result: str = ""
        for lab_name in sorted(self.labs):
            result += lab_name + " > " + str(self.labs[lab_name][1]).replace("LabStatus.", "") + "\n"
        return result[:-1]
