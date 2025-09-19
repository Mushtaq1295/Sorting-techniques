# Sorting Techniques

This folder contains Python implementations of common sorting algorithms. Each algorithm is implemented in its own file for clarity and modularity.

## Contents

- **merge_sort.py** – Implementation of Merge Sort (Divide and Conquer approach).
- **insertion_sort.py** – Implementation of Insertion Sort (Simple comparison-based algorithm).
- **selection_sort.py** – Implementation of Selection Sort (Finds the minimum repeatedly).
- **quick_sort.py** – Implementation of Quick Sort (Efficient Divide and Conquer algorithm).

## Algorithms Overview

### 1. Merge Sort
- **Time Complexity:** O(n log n) in all cases  
- **Space Complexity:** O(n)  
- **Stability:** Stable  

### 2. Insertion Sort
- **Time Complexity:** O(n²) worst/average, O(n) best (when nearly sorted)  
- **Space Complexity:** O(1)  
- **Stability:** Stable  

### 3. Selection Sort
- **Time Complexity:** O(n²) in all cases  
- **Space Complexity:** O(1)  
- **Stability:** Not Stable  

### 4. Quick Sort
- **Time Complexity:** O(n²) worst case, O(n log n) average/best case  
- **Space Complexity:** O(log n) (for recursion stack)  
- **Stability:** Not Stable  

## How to Run

Clone the repository or navigate to the folder, then run the desired sorting script with Python:

```bash
python merge_sort.py
python insertion_sort.py
python selection_sort.py
python quick_sort.py
