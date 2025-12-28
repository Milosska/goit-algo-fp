# Final Project for "Basic Algorithms and Data Structures" Course
Final course project covering all studied topics and consisting of 7 tasks.

## Task Navigation

<div>
<ol>
<li><a href="#repository-usage-instructions">Repository Usage Instructions</a></li>
<li><a href="#task-1-data-structures-sorting-linked-list-operations">Task 1: Data Structures. Sorting. Linked List Operations</a></li>
<li><a href="#task-2-recursion-creating-pythagoras-tree-fractal">Task 2: Recursion. Creating Pythagoras Tree Fractal</a></li>
<li><a href="#task-3-trees-dijkstra-algorithm">Task 3: Trees, Dijkstra's Algorithm</a></li>
<li><a href="#task-4-pyramid-visualization-building-function-for-binary-heap-visualization">Task 4: Pyramid Visualization. Building Function for Binary Heap Visualization</a></li>
<li><a href="#task-5-binary-tree-traversal-visualization">Task 5: Binary Tree Traversal Visualization</a></li>
<li><a href="#task-6-greedy-algorithms-and-dynamic-programming">Task 6: Greedy Algorithms and Dynamic Programming</a></li>
<li><a href="#task-7-monte-carlo-method-usage">Task 7: Monte Carlo Method Usage</a></li>
</ol>
</div>

## Repository Usage Instructions

1. Clone the repository

```bash
git clone [repository-url]
cd goit-algo-fp
```

2. Navigate to the project directory and activate the virtual environment

```bash
 python -m venv .venv
 # On Windows:
 .venv\Scripts\activate
 # On Unix/MacOS:
 source .venv/bin/activate
```

3. Install the required dependencies

```bash
# Install all dependencies (including development tools)
pip install -r requirements.txt
```

4. Run the main.py file in the corresponding project folder

```bash
python -m task_1.main
```

## Task 1: Data Structures. Sorting. Linked List Operations
This task implements basic operations on a singly linked list:

- List reversal (reverse_list)
- List sorting using merge sort algorithm (merge_sort)
- Merging two sorted lists into a new sorted list (merge_sorted_lists)

### Key Implementation Details

**Data Structure:**
- Implementation of `Node` and `LinkedList` classes taken from the course materials

**List Reversal (`reverse_list`):**
- Changes the direction of all links between nodes iteratively
- Performed without creating new nodes, in-place
- Complexity: O(n) time, O(1) space

**Merge Sort (`sort`):**
- Uses merge sort algorithm adapted for singly linked lists
- Applies the "slow and fast pointers" technique to find the middle
- Recursively divides the list and merges sorted parts
- Complexity: O(n log n) time, O(log n) space (recursion stack)

**Merging Sorted Lists (`get_merge_sorted_lists`):**
- Takes two sorted LinkedList objects
- Creates a new LinkedList with merged and sorted elements
- Uses auxiliary function `merge_sorted_lists` from the algorithms module
- Complexity: O(n + m), where n and m are the sizes of the lists

**Technical Details:**
- All operations are performed at the node level for optimal efficiency
- Includes helper functions (`create_linked_list_from_array`) for convenience
- Demo program shows all implemented features
- Integrated with error handling system through decorators

## Task 2: Recursion. Creating Pythagoras Tree Fractal
This task implements a program for creating the "Pythagoras tree" fractal using recursion and visualization with the turtle library.

### Key Implementation Details

**Data Structure:**
- Uses the turtle module for graphical visualization
- Error handling system through custom exceptions and decorators

**Recursion Level Parsing (`parse_rec_depth`):**
- Validates the recursion level entered by the user
- Throws `DepthValueIsNotValidException` in case of incorrect input

**Recursive Branch Drawing (`draw_pythagoras_branch`):**
- Recursively draws one branch of the Pythagoras tree
- Complexity: O(2^n) time, O(n) space (recursion stack)

**Main Drawing Function (`draw_pythagoras_tree`):**
- Sets up initial turtle parameters (speed, position)
- Sets initial orientation (90° upward)
- Calls recursive function with initial length of 200 pixels

**Technical Details:**
- Uses turtle library for 2D graphics
- Each branch splits into two sub-branches at ±45° angles
- Branch length reduction coefficient: 0.7
- Integrated with error handling system through decorators

## Task 3: Trees, Dijkstra's Algorithm
This task implements Dijkstra's algorithm for finding shortest paths in a weighted graph using a binary heap. The task includes graph creation, using a heap to optimize vertex selection, and computing shortest paths from a starting vertex to all others.

### Key Implementation Details

**Data Structure:**
- Uses NetworkX library for graph operations
- Graph visualization using matplotlib
- Graph represents settlements of Obukhiv community, Kyiv region

**Graph Creation (`initialize_graph`):**
- Creates an undirected graph with 21 settlements
- Vertices have attributes: weight (size for visualization) and color
- Edges represent distances between settlements in kilometers
- Vertex coordinates correspond to real geographical coordinates

**Graph Visualization (`handle_graph_build`):**
- Uses real geographical coordinates for vertex positioning
- Node size depends on their weight (inversely proportional)
- Color coding: red (center), blue (large cities), green (villages)

**Dijkstra's Algorithm (`dijkstra_heap_algorithm`):**
- Implemented using binary heap (heapq)
- Returns shortest distances and complete routes to all vertices
- Complexity: O((V + E) log V), where V is number of vertices, E is number of edges
- Optimized for working with large graphs

**Results Processing (`handle_dijkstra`):**
- Runs Dijkstra's algorithm from specified starting vertex (default "Обухів")
- Outputs shortest routes in readable format
- Shows sequence of settlements and total route length

**Technical Details:**
- Graph contains 21 vertices and 23 edges
- Binary heap ensures efficient selection of next vertex with minimum distance
- Stores complete route information (not just distance)
- Integrated with error handling system through decorators
- Supports displaying Ukrainian settlement names

## Task 4: Pyramid Visualization. Building Function for Binary Heap Visualization
This task implements a program for visualizing a binary heap (pyramid) by converting it into a binary tree and graphically displaying it using matplotlib and NetworkX.

### Key Implementation Details

**Data Structure:**
- Uses `Node` class with unique identifiers for each node
- Tree visualization performed using base `draw_tree` function from task using NetworkX libraries for graph creation and matplotlib for visualization

**Heap Creation (`build_heap`):**
- Supports two modes: base heap with predefined values and random heap
- Uses heapq module to create min-heap from random values

**Heap to Binary Tree Conversion (`get_binary_tree`):**
- Recursively builds binary tree from heap array
- Uses standard heap indexing formula: for parent at position i, left child at position 2*i+1, right child at position 2*i+2
- Complexity: O(n) time and space

**Technical Details:**
- Supports both basic and randomly generated heaps
- Integrated with error handling system through decorators
- Visualization blocks program execution until graph window is closed

## Task 5: Binary Tree Traversal Visualization
This task implements a program for visualizing binary tree traversal algorithms: depth-first (DFS) and breadth-first (BFS). The program uses code from task 4 for building the binary tree and adds color coding to display the order of node visits.

### Key Implementation Details

**Data Structure:**
- Uses existing Node class from task 4 for representing tree nodes
- Applies Queue for BFS and stack (list) for DFS algorithms

**Breadth-First Search Algorithm (`bfs_algorithm`):**
- Uses FIFO (First In, First Out) queue from the queue module
- Traverses tree level by level: first root, then all its children, then children's children
- Complexity: O(n) time, O(w) space, where w is maximum tree width

**Depth-First Search Algorithm (`dfs_algorithm`):**
- Uses LIFO (Last In, First Out) stack based on Python list
- Traverses tree depth-wise: root, complete left subtree, right subtree
- Adds children to stack in reverse order (first right, then left) for correct traversal
- Complexity: O(n) time, O(h) space, where h is tree height

**Color Coding (`color_nodes`):**
- Implements gradient coloring from blue (#0000FF) to yellow (#FFFF00)
- Uses linear interpolation in RGB space for smooth color transitions
- Each node gets unique color depending on its position in traversal sequence

**Color Helper Functions:**
- `hex_to_rgb`: converts HEX format to RGB tuple
- `rgb_to_hex`: converts RGB tuple to HEX format
- `interpolate_color`: calculates intermediate color between start and end colors

**Technical Details:**
- Uses base heap from task 4 for demonstrating both algorithms
- Color visualization shows difference between traversal algorithms
- DFS shows vertical traversal (depth-wise through branches)
- BFS shows horizontal traversal (level by level)
- Integrated with error handling system through decorators
- Smooth gradient from dark (early nodes) to light shades (late nodes)

## Task 6: Greedy Algorithms and Dynamic Programming
This task implements a program for solving the food selection problem with maximum total calories within a limited budget, using two approaches: greedy algorithm and dynamic programming.

### Key Implementation Details

**Data Structure:**
- Uses `food_items` dictionary with dish information (name, cost, calories)
- Available dishes: pizza (50/300), hamburger (40/250), hot-dog (30/200), pepsi (10/100), cola (15/220), potato (25/350)
- Format: {"name": {"cost": cost, "calories": calories}}

**Greedy Algorithm (`greedy_algorithm`):**
- Calculates calorie-to-cost ratio for each dish
- Sorts dishes by descending efficiency (calories/cost)
- Selects dishes in order of best ratio until budget is exhausted
- Complexity: O(n log n) due to sorting, where n is number of dishes

**Dynamic Programming (`dynamic_programming`):**
- Creates table of optimal solutions for all possible budgets from 0 to given amount
- For each budget finds maximum calories and optimal dish selection
- Tracks selected products for reconstructing optimal menu
- Complexity: O(budget × n), where budget is budget size, n is number of dishes

**Performance Measurement (`execute_and_measure_time`):**
- Uses `timeit` module for precise execution time measurement
- Calculates total calories, cost, and remainder for each algorithm
- Formats results in understandable form with menu details

**Helper Functions:**
- `calculate_menu_stats`: calculates total calories and cost of selected menu
- `get_menu_results`: formats algorithm execution results in text form

### Comparative Algorithm Analysis

**Testing Results on Different Budgets:**

| Budget | Algorithm | Calories | Cost | Remainder | Execution Time |
|--------|-----------|----------|------|-----------|----------------|
| 126 UAH | Greedy | 1760 kcal | 120 UAH | 6 UAH | ~8.3×10⁻⁶ sec |
| 126 UAH | Dynamic | 1800 kcal | 125 UAH | 1 UAH | ~7.1×10⁻⁵ sec |
| 1055 UAH | Greedy | 15400 kcal | 1050 UAH | 5 UAH | ~5.7×10⁻⁶ sec |
| 1055 UAH | Dynamic | 15440 kcal | 1055 UAH | 0 UAH | ~6.3×10⁻⁴ sec |
| 15294 UAH | Greedy | 224180 kcal | 15285 UAH | 9 UAH | ~4.1×10⁻⁵ sec |
| 15294 UAH | Dynamic | 224220 kcal | 15290 UAH | 4 UAH | ~9.9×10⁻³ sec |

**Analysis Conclusions:**
- **Optimality**: Dynamic programming always gives optimal result with higher calories
- **Speed**: Greedy algorithm is significantly faster, especially on large budgets
- **Scalability**: Speed difference grows exponentially with budget increase
- **Practicality**: Greedy algorithm gives acceptable results with minimal time cost

**Technical Details:**
- Uses efficient calorie/cost ratio calculation for greedy approach
- Dynamic programming builds complete state table for guaranteed optimum
- Integrated with error handling system through decorators
- Modular architecture with separation of algorithms, constants, and helper functions
- Comparison performed on three different budgets to demonstrate scalability

## Task 7: Monte Carlo Method Usage
This task implements a program for calculating probabilities of sums when rolling two dice using the Monte Carlo method. The program simulates a large number of rolls, counts the frequency of each sum, and compares results with analytical calculations.

### Key Implementation Details

**Data Structure:**
- Uses `analytic_probabilities` dictionary with theoretical probabilities for each sum (2-12)
- Simulation results stored in similar dictionary for comparison

**Monte Carlo Algorithm (`monte_carlo_simulation`):**
- Generates specified number of random rolls of two dice (default 100,000)
- Uses `random.randint(1, 6)` to simulate six-sided die
- Counts frequency of each possible sum from 2 to 12
- Calculates probabilities as ratio of occurrences to total number of rolls

**Comparison Table (`show_probability_comparison_table`):**
- Formats results as structured table
- Displays analytical and experimental probabilities side by side for easy comparison
- Uses percentage format for result clarity

**Graphical Visualization (`show_probability_comparison_graph`):**
- Creates comparison histogram using matplotlib
- Shows two sets of bars: theoretical (orange) and experimental (blue) probabilities
- Includes legend, axis labels, and grid for better perception

### Comparative Results Analysis

**Simulation Results (100,000 rolls):**

| Sum | Analytical Probability | Monte Carlo Probability | Absolute Error |
|-----|------------------------|-------------------------|----------------|
| 2   | 2.78%                  | 2.81%                   | 0.03%          |
| 3   | 5.56%                  | 5.55%                   | 0.01%          |
| 4   | 8.33%                  | 8.16%                   | 0.17%          |
| 5   | 11.11%                 | 11.14%                  | 0.03%          |
| 6   | 13.89%                 | 13.88%                  | 0.01%          |
| 7   | 16.67%                 | 16.62%                  | 0.05%          |
| 8   | 13.89%                 | 13.98%                  | 0.09%          |
| 9   | 11.11%                 | 11.21%                  | 0.10%          |
| 10  | 8.33%                  | 8.36%                   | 0.03%          |
| 11  | 5.56%                  | 5.50%                   | 0.06%          |
| 12  | 2.78%                  | 2.80%                   | 0.02%          |

**Calculation Accuracy Conclusions:**

- **High Accuracy**: Maximum absolute error is only 0.17%, confirming correct Monte Carlo method implementation
- **Convergence to Theoretical Values**: All experimental probabilities are within statistical error margin from analytical calculations
- **Highest Accuracy for Central Sums**: Sums 6, 7, 8 (most probable) have smallest relative error, which corresponds to statistical laws
- **Large Sample Efficiency**: 100,000 iterations provide sufficient accuracy for practical applications

**Theoretical Justification:**
- Sum 7 has highest probability (16.67%) as it can be obtained in 6 ways: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)
- Sums 2 and 12 have lowest probability (2.78%) as each can be obtained in only one way: (1,1) and (6,6) respectively
- Probability distribution is symmetric around sum 7, confirmed both analytically and experimentally

**Technical Details:**
- Uses `random` module for pseudo-random number generation
- Modular architecture with separation of simulation, constants, and result processing
- Visualization performed using matplotlib with interactive graphs
- Integrated with error handling system through decorators
- Supports different iteration counts for studying method convergence