🐍 Wumpus World Solver 🌍

This project demonstrates a heuristic-based approach to solving the classic Wumpus World problem using Python. The Wumpus World is a grid-based environment where the player's goal is to navigate through the grid to find the gold while avoiding dangers such as pits and a deadly Wumpus creature.

🔍 Approach:
The approach for solving the Wumpus World problem is based on a heuristic search algorithm, using a modified version of the A* algorithm. The use of a heuristic approach is suitable for this problem, as it efficiently navigates the environment using partial information to make informed decisions.

The approach involves iterative exploration of the environment while updating the probabilities of dangers (pits) and the Wumpus creature's presence in each cell. The `probe` and `cautious_probe` functions are used to gather information about the type of cell, intelligently collecting information about adjacent cells without risking the player's life.

The probabilities are updated based on the obtained information, and decisions are made based on these probabilities. This reflects an intelligent approach to solving the Wumpus World problem, making use of heuristic search and probability techniques to make efficient decisions while minimizing risk.

📊 Cost Calculation:
The project also calculates the total cost of exploration and displays the average cost over multiple iterations. This provides a measure of performance and improvement of the algorithm, allowing for comparison and analysis of different strategies.

🚀 Getting Started:
To run the Wumpus World solver, make sure you have the required libraries and dependencies installed. Then, simply execute the Python script to see the solver in action!

🔗 Dependencies:
- `lib.wumpus2`: A library that simulates the Wumpus World environment.

💡 Note:
- The solver's approach is written in Python and focuses on heuristic-based exploration and probabilistic decision-making.
- The README is written in English to provide a clear understanding of the project's approach and details.

👏 Enjoy solving the Wumpus World problem using this heuristic-based approach and learn more about intelligent decision-making in uncertain environments!
