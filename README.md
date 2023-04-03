[![Repo Checks](https://github.com/sta663-sp23/hw01_lab02_team06/workflows/Repo%20Checks/badge.svg)](https://github.com/sta663-sp23/hw01_lab02_team06/actions?query=workflow:%22Repo%20Checks%22)



Team Members:Feng Ying, Gu Claire, Liang Cassie, Yuan Yiliang 


## Task 1 - Wordle

### Background

Last year the word game
[WORDLE](https://www.powerlanguage.co.uk/wordle/) seemed to take over
the world, or at least twitter. Your task here is to come up with a
Wordle puzzle solver in Python.

If you are not familiar with the game, a basic description follows: you
will be presented with an unknown/secret 5 letter word - your goal is to
guess that word with at most 6 guesses. Each time you guess the game
will report back whether each of the guessed letters occurs in the
secret word either in exactly that position (🟩) or in some other
position (🟨), or if it does not occur in the secret word (⬜).

We have implemented a basic Wordle game in Python which you can play by
importing the `worldle` module, which contains the `puzzle` class.

``` python
import wordle
```

To play a game you can create a puzzle with `wordle.puzzle()` for a
random secret word or `wordle.puzzle(seed=123)` to get a specific word,
just change the value of seed. Once created, you can make guesses with
the `guess()` method. See an example game below.

### Example game

``` python
p = wordle.puzzle(123)
p.guess("acute")
```

    ['🟨', '⬜', '⬜', '⬜', '⬜']

``` python
p.guess("lairs")
```

    ['⬜', '🟩', '🟨', '⬜', '🟨']

``` python
p.guess("basin")
```

    ['🟩', '🟩', '🟩', '🟩', '⬜']

``` python
p.guess("basij")
```

    ['🟩', '🟩', '🟩', '🟩', '🟩']

``` python
p
```

    Wordle puzzle: (Solved)
    1. 🟨 ⬜ ⬜ ⬜ ⬜ (acute)
    2. ⬜ 🟩 🟨 ⬜ 🟨 (lairs)
    3. 🟩 🟩 🟩 🟩 ⬜ (basin)
    4. 🟩 🟩 🟩 🟩 🟩 (basij)

``` python
p.is_solved()
```

    True

``` python
p.n_guesses()
```

    4

From the session above you can see that the progress of the game can be
checked by printing the puzzle object and the solution status is
returned by the `is_solved()` method. A couple of other important rules
for this version of the game:

- All guesses must be 5 letters, lowercase, and a word in the word list.
- The solution must be found within 6 guesses or the puzzle is failed
  (and further guesses will not be allowed).
- If you want to give up and see the secret word, use the `reveal()`
  method. Once done this will prevent you from guessing further.

### Solver

Using the function definition provided below, implement a solver which
will attempt to solve any Wordle puzzle object it is given. You may
assume that the puzzle is new and that no guesses have been made and
that the secret word is part one of the words in the word list provided
by the `worlde` module, see `wordle.words`. Your solution may make use
of this word list in order to better solve the puzzles, be careful to
not modify this list accidentally.

### Assessment

We will be assessing your solver by applying it to a large random sample
of puzzles and determining how many puzzles were solved and what the
average number of guesses needed.

The code used for this assessment is include in `hw1.ipynb` (with the
seed and number of puzzles being attempted). We encourage you to
regularly test your implementation using this code.

The solver which achieves the lowest average number of guesses for our
test set will receive extra credit.

## Task 2

The following question is derived from a task given as part of last
year’s [Advent of Code](https://adventofcode.com/2021). We are
presenting a simplified version here for you to work on.

For this task you will be given a matrix which is composed of the
character values: “.”, “\>”, and “v” and represents the current state of
an evolving system. Your goal is to write a function that will iterate
this system one step at a time using a specific set of rules until the
system reaches steady state (i.e. the state did not change between the
previous step and the current step) and report the number of steps
required to reach this point. The following rules are used to iterate
the state:

- ‘.’ elements are considered empty

- ‘\>’ elements will move to their right if that position is empty,
  their current position becomes empty.

- ‘v’ elements will move down if that position is empty, their current
  position becomes empty.

- Elements that move off the right or bottom of the matrix wrap around
  to the left or top position respectively. These wrapped positions are
  considered for the purpose of deciding if a move is made or not.

- Each step occurs as follows:

  - First all of the ‘\>’ elements’ moves are considered simultaneously,
    so an element cannot move into a position being freed up by another
    ‘\>’ moving.

  - Second all of the ‘v’ elements’ moves are considerted
    simultaneously, again elements cannot move into a position being
    freed up by another ‘v’ moving.

For example consider a single row with elements `.>>..`, it will iterate
as follows:

0.  `.>>..` - Initial state
1.  `.>.>.` - Step 1, only the rightmost `>` moves
2.  `..>.>` - Step 2, both `>` may now move
3.  `>..>.` - Step 3, both `>` move, rightmost wraps to the left side

The advent module has been provided which contains a `small` (9 x 10)
and `large` (137 x 139) system, these data are stored as a list of
lists.

**Note** - when working with the state object you will need to make a
copy (at one or more points) in your code. Because the state object is a
list of lists it is not sufficient to use the `copy()` method, instead
you should use the `deepcopy()` function from the `copy` library.

For the two inputs, the correct answer is 58 and 351 steps
respectively - the `hw1` notebook contains `assert`s to validate that
the correct answer was obtained by your `advent_solve()` function.

## Task 3

For this task you will reimplement `advent_step()` and `advent_solve()`
using a NumPy ndarray instead of a list of lists and compare the
performance between the two implementations. The ndarray versions of the
small and large state are available within the `advent` module as
`small_np` and `large_np` respectively. Note, due to their structure,
using the `copy()` method is sufficient for these ndarray objects.

Once again we have included a cell with `assert`s to validate that the
correct answer was obtained by your `advent_solve_np()` function.

Once the new implementation is working correctly, run the included cells
with the `%timeit` magic to obtain some basic performance metrics for
the two implementations.

In the markdown cell provided discuss which implementation was faster?
Explain why you think this is?

## Submission and Marking

This homework is due by 5:00 pm on Friday, February 3rd. You are to
complete the assignment as a team and to keep everything (code, write
ups, etc.) in your team’s repository (commit early and often). Only the
work committed to the repositories’ main branch by the deadline will be
marked. As mentioned in syllabus, all team members are expected to
contribute equal effort for this assignment - individual contributions
will be assessed after the assignment is completed via peer evaluations
and commits.

The final product for this assignment should be a single notebook
(hw1.ipynb) that contains all code and text for the tasks described
above. This document should be clearly and cleanly formatted and present
all of your results. Style and formatting does count for this
assignment, so please take the time to make sure everything looks good
and your text and code are properly formatted. This document must be
reproducible and we must be able to rerun it with minimal intervention -
documents that do not compile will be penalized.

Finally, we will not be enforcing any particular coding style, however
it is important that the code your team produces is readable and
consistent in its formatting. As a team you should decide on what
conventions you will use and the entire team should conform to them.
