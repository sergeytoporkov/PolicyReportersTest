import unittest
from modulo_three import modThree
from fsm_standard import FSMStandard, states
from fsm_advanced import FSMAdvanced

class TestModuloThree(unittest.TestCase):

    def test_1(self):
        result = modThree("1101")
        self.assertEqual(result,1)

    def test_2(self):
        result = modThree("1110")
        self.assertEqual(result, 2)

    def test_3(self):
        result = modThree("1111")
        self.assertEqual(result, 0)

class TestFSM_Standard(unittest.TestCase):

    def test_1(self):
        result = FSMStandard("1101")
        self.assertEqual(result,1)

    def test_2(self):
        result = FSMStandard("1110")
        self.assertEqual(result, 2)

    def test_3(self):
        result = FSMStandard("1111")
        self.assertEqual(result, 0)

class TestFSM_Advanced(unittest.TestCase):
    # setting all that can set by the user
    # transactions can be custom, but for this case we take exercise transactions
    fsm = FSMAdvanced()
    fsm.setStates([0, 1, 2])
    fsm.setSigmas([0, 1])
    fsm.transactions = states

    def test_1(self):
        self.fsm.setBinary("1101")
        self.assertEqual(self.fsm.getModulo(),1)

    def test_2(self):
        self.fsm.setBinary("1110")
        self.assertEqual(self.fsm.getModulo(),2)

    def test_3(self):
        self.fsm.setBinary("1111")
        self.assertEqual(self.fsm.getModulo(),0)

if __name__ == '__main__':
    unittest.main()