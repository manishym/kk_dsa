# Knowledge Knights DSA Learning Project

A comprehensive Data Structures and Algorithms (DSA) learning project designed to teach fresh graduates the fundamentals of algorithmic thinking, time complexity analysis, and problem-solving techniques.

## 🎯 Project Overview

This project is structured to provide a hands-on learning experience for Data Structures and Algorithms. It combines theoretical concepts with practical implementations, interactive Jupyter notebooks, and detailed notes to ensure a complete understanding of DSA concepts.

## 📁 Project Structure

```
knowledge-knights-dsa/
├── jupyter_notebooks/          # Interactive learning notebooks
│   Notebooks used to demonstrate complexieties.
├── lecture_code/               # Practical code implementations
│   Code that was used during lecture.
├── notes/                      # Detailed lecture notes and materials
|   Notes which were used during lecture discussion.
├── problem_hints/              # Problem-solving hints and solutions
│   hints about problems organized lecture wise.
├── .venv/                      # Python virtual environment
└── README.md                   # This file
```

## 📚 Learning Modules

### Lecture 1: Arrays and Time Complexity

**Location**: `lecture1_arrays_and_time_complexiety/`

#### 📖 Interactive Notebook (`time_complexiety.ipynb`)
- **Purpose**: Hands-on exploration of time complexity concepts
- **Contents**:
  - Implementation of various time complexity functions (O(1), O(log n), O(n), O(n log n), O(n²), O(n³), O(2ⁿ))
  - Real-time performance measurement and comparison
  - Interactive visualizations using matplotlib
  - Step-by-step analysis of algorithmic efficiency
  - Practical examples demonstrating how input size affects performance

#### 💻 Code Examples (`fib.py`)
- **Purpose**: Practical implementation of dynamic programming concepts
- **Contents**:
  - Efficient Fibonacci sequence implementation using dynamic programming
  - Time measurement utilities
  - Command-line interface for testing different input sizes
  - Demonstrates the difference between naive and optimized approaches



## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Jupyter Notebook or JupyterLab
- Required Python packages (install via pip):
  ```bash
  pip install jupyter matplotlib numpy
  ```

### Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd knowledge-knights-dsa
   ```

2. **Set up virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

4. **Navigate to the learning materials**:
   - Start with `jupyter_notebooks/lecture1_arrays_and_time_complexiety/time_complexiety.ipynb`
   - Review the corresponding notes in `notes/lecture1_arrays_and_time_complexiety/notes1.pdf`
   - Practice with the code examples in `lecture_code/lecture1_arrays_and_time_complexiety/fib.py`

## 🎓 Learning Path

### For Fresh Graduates

1. **Start with the Interactive Notebook**: 
   - Run through the `time_complexiety.ipynb` notebook
   - Experiment with different input sizes
   - Observe how algorithms perform with varying data sizes

2. **Review Theoretical Concepts**:
   - Read through `notes1.pdf` for comprehensive understanding
   - Take notes on key concepts and formulas

3. **Practice Implementation**:
   - Study the `fib.py` implementation
   - Modify the code to experiment with different approaches
   - Try implementing similar algorithms on your own

4. **Problem-Solving Practice**:
   - **Attempt problems first**: Try solving problems in `problem_hints/` without looking at hints
   - **Use progressive hints**: Start with easy approaches, then explore advanced solutions
   - **Understand multiple approaches**: Study how the same problem can be solved differently
   - **Analyze complexity**: Compare time and space complexity of different solutions

5. **Hands-on Practice**:
   - Implement the algorithms from scratch
   - Compare your implementations with the provided examples
   - Measure and analyze performance differences
   - Apply learned concepts to new problems

## 🧩 Using Problem Hints Effectively

### Problem-Solving Strategy
1. **Read the problem statement carefully** - understand the requirements and constraints
2. **Try to solve independently first** - spend 15-20 minutes attempting your own solution
3. **Start with the easy approach** - implement the basic solution before optimizing
4. **Study the advanced approach** - understand the mathematical reasoning behind efficient solutions
5. **Implement both approaches** - practice coding both the basic and optimized versions
6. **Compare performance** - measure and analyze the differences in time and space complexity

### Example: Find the Duplicate Number
- **Step 1**: Try solving with a simple approach (using a set)
- **Step 2**: Understand why this works and its limitations
- **Step 3**: Study the Floyd's cycle detection approach
- **Step 4**: Implement both solutions and compare their performance
- **Step 5**: Apply similar thinking patterns to related problems

## 🔧 Running Code Examples

### Fibonacci Implementation
```bash
cd lecture_code/lecture1_arrays_and_time_complexiety/
python fib.py 10  # Calculate 10th Fibonacci number
```

### Interactive Notebook
```bash
cd jupyter_notebooks/lecture1_arrays_and_time_complexiety/
jupyter notebook time_complexiety.ipynb
```

## 📈 Learning Objectives

By the end of this module, students should be able to:

- **Understand Time Complexity**: Analyze and compare different algorithmic approaches
- **Implement Efficient Algorithms**: Write code that considers performance implications
- **Visualize Performance**: Use graphs and charts to understand algorithm behavior
- **Apply Dynamic Programming**: Solve problems using memoization and optimization techniques
- **Think Algorithmically**: Approach problems with efficiency in mind



