# FINITE STATE MACHINE (STANDARD)

states = {
        0: {'0': 0, '1': 1},
        1: {'0': 2, '1': 0},
        2: {'0': 1, '1': 2}
    }

def FSMStandard(values):
    global states
    state = 0
    for value in values:
        state = states[state][value]
    return state