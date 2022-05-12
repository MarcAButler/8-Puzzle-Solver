# 8-Puzzle-Solver

<p align="center">
  <img alt="GIF of a short demo of the 8-Puzzle-Solver" src="https://github.com/MarcAButler/8-Puzzle-Solver/blob/master/Demo.gif">
</p>

The 8-Puzzle-Solver is an artificially intelligent puzzle solver based on 8-tiled version of the [sliding puzzle](https://en.wikipedia.org/wiki/Sliding_puzzle).
The way that this works is that a user may input 1 of 3 algorithms that will be used to solve an arbitrary puzzle of length 9.

### The three algorithms
1. BFS - [Breadth First Search algorithm](https://en.wikipedia.org/wiki/Breadth-first_search): Uses a queue
2. BSTFS - [Best First Search algorithm](https://en.wikipedia.org/wiki/Best-first_search#:~:text=Best%2Dfirst%20search%20is%20a,according%20to%20a%20specified%20rule.): Uses a priority queue rather than a simple queue
3. A* - [A Star algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm): Typically an effiecent, optimal, and complete algorithm

### Heurisitics
1. [Manhattan Distance](https://xlinux.nist.gov/dads/HTML/manhattanDistance.html): Distance between two points
2. Tiles out of Place: Simply the number of tiles out of place in as a means of heurisitics for our AI

### Proper Input
Proper inputs for the puzzle must consist of 9 characters--no more; no less. Each must be a different character in the form of **\[1-8\]** where a `-` must be inserted as well to denote the empty space. Only one of each character may be used per puzzle.

# Common Errors
The code will **fail** according to the following reasons:
1. The puzzle encoding was either greater or less than length of 9. For example `"4213-57866"` (❌) is too long and `"4213-578"` (❌) is too short. `"4213-5786"` (✅) is correct, however.
2. The puzzle encoding contained an unrecongized character. For example `"4213-a786"` (❌) is not allowed. Digits `"1-8"` (✅) are correct while digits `"1"` (❌) and `"9"` (❌) are incorrect. The only other character other than the previously mentioned are `"-"` (✅)

If any of these errors occurs the program will either fail silently or simply take the time of the total remainder of the universe to calculate a puzzle that cannot be solved. 🌎

# Download
An executable can be found in a `.tar.gz` or `.zip` file in the releases tab of this repo. Otherwise, it may compiled from source.
