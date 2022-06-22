# FINITE STATE MACHINE (ADVANCED)

class FSMAdvanced():
    def __init__(self):
        self.states = []
        self.sigma = []
        self.state = 0
        self.finals = []
        self.transactions = {}
        self.binary = None

    def setStates(self, statesList):
        self.states = statesList
        self.finals = self.states

    def setSigmas(self, sigmasList):
        self.sigma = [str(x) for x in sigmasList]

    def setStartState(self, startValue):
        self.state = int(startValue)

    def setFinals(self, finalsList):
        self.finals = finalsList

    def setBinary(self, binaryValue):
        self.binary = str(binaryValue)

    def getTransactions(self):
        for i in range(len(self.states)):
            self.transactions[self.states[i]] = {}

        for key,value in self.transactions.items():
            for i in self.sigma:
                print(f"Enter S{key} {i}'s transaction")
                value[i] = int(input())

    def getModulo(self):
        temp = self.state
        for value in self.binary:
            temp = self.transactions[temp][value]

        return temp

    def getFinals(self):
        return True if self.state in self.finals else False
