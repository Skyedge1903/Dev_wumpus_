# Wumpus World Solver :video_game:

## Introduction :wave:

This README provides an overview of the Wumpus World Solver code. The code implements a solver for the Wumpus World environment, a classic artificial intelligence problem. The solver uses a modified version of the A* algorithm to navigate the world, collect information, and ultimately find the optimal path to the goal. Let's dive into the details of the code! :mag:

## Code Overview :computer:

The code utilizes a modified version of the A* algorithm to explore and navigate the Wumpus World environment. Here's how it works:

1. The solver initializes the Wumpus World environment.
2. The code defines a function `suiv` to calculate the adjacent cells of a given cell.
3. The `convert` function is used to convert cell coordinates to matrix indices.
4. The solver iterates through multiple iterations to explore and gather information in the environment.
5. The solver maintains a dictionary `ma_dimension` to track the probabilities of hazards and wumpus presence in each cell.
6. The solver calculates the type of each cell using the `probe` or `cautious_probe` functions from the Wumpus World environment.
7. The solver updates the probabilities in `ma_dimension` based on the information obtained.
8. The solver evaluates and iteratively updates the probabilities to make informed decisions.
9. The solver calculates the total cost of exploration and displays the average cost over multiple iterations.

## How to Use :rocket:

1. Import the necessary Wumpus World library.
2. Run the code with the library to solve the Wumpus World environment.
3. Observe the solver's progress and the average cost of exploration.

## Additional Information :information_source:

- The code includes comments for understanding each section's functionality. :memo:
- Modify the solver's behavior by adjusting the exploration and decision-making strategies. :wrench:
- The solver's performance can vary based on the Wumpus World environment's configuration. :game_die:

Feel free to explore the code and experiment with different strategies to tackle the Wumpus World challenge! :video_game:

The approach for solving the Wumpus World problem appears to be based on a heuristic search approach using a modified version of the A* algorithm. The use of a heuristic approach is appropriate for solving this type of problem, as it allows for efficient navigation through the environment using partial information to make informed decisions.

The approach involves iteratively exploring the environment while updating the probabilities of the presence of dangers (pits) and the Wumpus in each cell. The use of the `probe` and `cautious_probe` functions to gather information about the type of cell is a smart strategy to collect information about adjacent cells without risking the player's life.

Updating probabilities based on obtained information and making decisions based on these probabilities reflects an intelligent approach to solving the Wumpus World problem. Additionally, calculating the total exploration cost and displaying the average cost over multiple iterations provides a performance measurement and improvement of the algorithm.

In summary, the chosen approach appears to be well-suited for solving the Wumpus World problem using heuristic search and probability techniques to make efficient decisions while minimizing risk.
