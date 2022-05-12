<img align="center" src="https://github.com/MarcAButler/8-Puzzle-Solver/blob/master/Demo.gif">


![GIF of a short demo of the 8-Puzzle-Solver](https://github.com/MarcAButler/8-Puzzle-Solver/blob/master/Demo.gif)



# 8-Puzzle-Solver
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

# Download
An executable can be found in a `.tar.gz` or `.zip` file in the releases tab of this repo.
