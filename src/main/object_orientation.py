from enum import Enum


class LabStatus(Enum):
    PENDING = 1,
    COMPLETED = 2,
    INCOMPLETE = 3


class RockPaperScissorHandSign(Enum):
    ROCK = "PAPER", "SCISSOR",
    PAPER = "SCISSOR", "ROCK",
    SCISSOR = "ROCK", "PAPER"

    def get_winner(self) -> str:
        return self.value[0]

    def get_loser(self) -> str:
        return self.value[1]
