from unittest import TestCase

from src.main.object_orientation import RockPaperScissorHandSign


class PaperTest(TestCase):
    def setUp(self):
        self.sign = RockPaperScissorHandSign.PAPER

    def testGetLoser(self):
        loser = RockPaperScissorHandSign.ROCK
        self.assertEqual(loser.name, self.sign.get_loser())

    def testGetWinner(self):
        loser = RockPaperScissorHandSign.SCISSOR
        self.assertEqual(loser.name, self.sign.get_winner())


class RockTest(TestCase):
    def setUp(self):
        self.sign = RockPaperScissorHandSign.ROCK

    def testGetLoser(self):
        loser = RockPaperScissorHandSign.SCISSOR
        self.assertEqual(loser.name, self.sign.get_loser())

    def testGetWinner(self):
        loser = RockPaperScissorHandSign.PAPER
        self.assertEqual(loser.name, self.sign.get_winner())


class ScissorTest(TestCase):
    def setUp(self):
        self.sign = RockPaperScissorHandSign.SCISSOR

    def testGetLoser(self):
        loser = RockPaperScissorHandSign.PAPER
        self.assertEqual(loser.name, self.sign.get_loser())

    def testGetWinner(self):
        loser = RockPaperScissorHandSign.ROCK
        self.assertEqual(loser.name, self.sign.get_winner())
