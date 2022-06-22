# MODULO THREE EXERCISE

We can just simply do this task with lambda-one-liner: 
`modThree = lambda x: int(x,2) % 3`.
But as I was told to use other "features", so: firstly we're getting a number from string,
then also we need some variables to work with `value, i`, checking if we still have
something to work with in a while loop, getting reminder from 10 using `%`, using value
to store our seeking int value, simply by summing the reminder multiplied by
current step(repr of a length of the input string), then we are cutting our value with
floor division by 10 and incrementing i-step and lastly returning value `%` by 3
using prints to test it with exercise data
_P.S. I'm not asked to provide class, so I used just a function :)_

# FINITE STATE MACHINE (STANDARD)

We determine dict of states `(0,1,2)` as `keys` for this exercise, and step-states as values
accessing to global dict in `FSMStandard` func, setting first state to 0, then simply
returning `key,value` pair in state, finally returning state we get, using simple prints to test it
_P.S. I'm not asked to provide class, so I used just a function and global dict to reduce memory usage :)_

# FINITE STATE MACHINE (ADVANCED)

So the main idea of advanced task is to provide solution, which can be used
by other devs in team, the best way to make it - is to provide class-based solution
for this exercise I do not doing it in other .py file, in real-life projects,
I would do smth like `FSM.py` or use prebuilt solutions after testing... :)
then we could call our class like: `from FMS import FSMAdvanced` and work with it
after init we're sending some data to FSM object, we have list for all states,
to change it call `setStates`, list for sigmas, to change it call `setSigmas`,
start state as 0, also we could change it with `setStartState`
we set finals equals to states, or we can change it with `setFinals`
to get all Transactions call `getTransactions`, to get modulo - call `getModulo`
to get Finals - call `getFinals`, returns `True` if current state after some ops is in finals list.

# TESTS

