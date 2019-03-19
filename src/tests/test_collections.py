from unittest import TestCase

from src.main.collections import Lab, Student
from src.main.object_orientation import LabStatus


class Fork(TestCase):
    def test1(self):
        lab = Lab("duplicate deleter")
        student = Student()
        expected = LabStatus.PENDING
        student.fork_lab(lab)
        actual = student.get_lab_status(lab.lab_name)
        self.assertEqual(expected, actual)

    def test2(self):
        lab = Lab("learner lab")
        student = Student()
        expected = LabStatus.PENDING
        student.fork_lab(lab)
        actual = student.get_lab_status(lab.lab_name)
        self.assertEqual(expected, actual)


class GetLabTest(TestCase):
    def test1(self):
        lab_name = "duplicate deleter"
        expected = Lab(lab_name)
        student = Student()
        student.fork_lab(expected)
        actual = student.labs[lab_name][0]
        self.assertEqual(expected, actual)

    def test2(self):
        lab_name = "learner lab"
        expected = Lab(lab_name)
        student = Student()
        student.fork_lab(expected)
        actual = student.labs[lab_name][0]
        self.assertEqual(expected, actual)


class SetLabStatusOfForked(TestCase):
    def testCompleted(self):
        lab_name = "duplicate deleter"
        lab = Lab(lab_name)
        student = Student()
        expected = LabStatus.COMPLETED
        student.fork_lab(lab)
        student.labs[lab_name][1] = expected
        actual = student.get_lab_status(lab_name)
        self.assertEqual(expected, actual)

    def testPending(self):
        lab_name = "duplicate deleter"
        lab = Lab(lab_name)
        student = Student()
        expected = LabStatus.PENDING
        student.fork_lab(lab)
        student.labs[lab_name][1] = expected
        actual = student.get_lab_status(lab_name)
        self.assertEqual(expected, actual)

    def testIncomplete(self):
        lab_name = "duplicate deleter"
        lab = Lab(lab_name)
        student = Student()
        expected = LabStatus.INCOMPLETE
        student.fork_lab(lab)
        student.labs[lab_name][1] = expected
        actual = student.get_lab_status(lab_name)
        self.assertEqual(expected, actual)


class SetLabStatusOfUnforked(TestCase):
    def testCompleted(self):
        lab_name = "duplicate deleter"
        lab = Lab(lab_name)
        student = Student()
        self.assertRaises(ValueError, student.set_lab_status, lab_name, LabStatus.INCOMPLETE)

    def testPending(self):
        lab_name = "duplicate deleter"
        lab = Lab(lab_name)
        student = Student()
        expected = LabStatus.PENDING
        self.assertRaises(ValueError, student.set_lab_status, lab_name, expected)

    def testIncomplete(self):
        lab_name = "duplicate deleter"
        lab = Lab(lab_name)
        student = Student()
        expected = LabStatus.INCOMPLETE
        self.assertRaises(ValueError, student.set_lab_status, lab_name, expected)


class ToStringTest(TestCase):
    def test1(self):
        lab_name = "duplicate deleter"
        duplicate_deleter = Lab("duplicate deleter")
        learner = Lab("learner lab")
        student = Student()
        completed = LabStatus.COMPLETED
        expected = "duplicate deleter > COMPLETED\nlearner lab > PENDING"
        student.fork_lab(learner)
        student.fork_lab(duplicate_deleter)
        student.labs[lab_name][1] = completed
        actual = str(student)
        self.assertEqual(expected, actual)

    def test2(self):
        casino_lab_name = "casino"
        learner_lab_name = "learner lab"
        casino = Lab(casino_lab_name)
        learner = Lab(learner_lab_name)
        student = Student()
        expected = "casino > COMPLETED\nlearner lab > INCOMPLETE"
        student.fork_lab(learner)
        student.fork_lab(casino)
        student.labs[casino_lab_name][1] = LabStatus.COMPLETED
        student.labs[learner_lab_name][1] = LabStatus.INCOMPLETE
        actual = str(student)
        self.assertEqual(expected, actual)
