---
aid: big-o-notation
name: Big O Notation
description: Big O Notation is a mathematical notation used in computer science to describe the performance or complexity of algorithms, providing a way to classify algorithms by how their runtime or space requirements grow as input size grows. It is foundational to algorithm design, API performance benchmarking, and software engineering education.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Algorithms
  - Big O Notation
  - Complexity
  - Computer Science
  - Performance
  - Data Structures
url: https://raw.githubusercontent.com/api-evangelist/big-o-notation/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
apis: []
common:
  - type: Reference
    url: https://en.wikipedia.org/wiki/Big_O_notation
  - type: Reference
    url: https://www.bigocheatsheet.com
  - type: Features
    data:
      - name: O(1) - Constant Time
        description: Algorithm runtime does not change with input size. Example - hash table lookups.
      - name: O(log n) - Logarithmic Time
        description: Runtime grows logarithmically with input. Example - binary search.
      - name: O(n) - Linear Time
        description: Runtime grows linearly with input size. Example - linear search.
      - name: O(n log n) - Linearithmic Time
        description: Runtime grows as n multiplied by log n. Example - merge sort, heap sort.
      - name: O(n²) - Quadratic Time
        description: Runtime grows quadratically with input size. Example - bubble sort, nested loops.
      - name: O(2^n) - Exponential Time
        description: Runtime doubles with each additional input element. Example - recursive Fibonacci.
      - name: O(n!) - Factorial Time
        description: Runtime grows factorially. Example - brute-force traveling salesman.
  - type: UseCases
    data:
      - name: Algorithm Selection
        description: Choosing the most efficient algorithm for a given problem based on complexity class.
      - name: API Performance Benchmarking
        description: Analyzing API endpoint performance characteristics under varying data sizes.
      - name: Code Review
        description: Evaluating the time and space complexity of code changes during review.
      - name: Database Query Optimization
        description: Understanding complexity of database operations to optimize query performance.
      - name: Scalability Analysis
        description: Predicting how software will perform as data volumes grow at scale.
      - name: Interview Preparation
        description: Preparing for technical interviews requiring algorithm complexity analysis.
  - type: Vocabulary
    data:
      - term: Time Complexity
        definition: Measure of computation time as a function of input size.
      - term: Space Complexity
        definition: Measure of memory usage as a function of input size.
      - term: Best Case
        definition: Minimum time required for algorithm execution (Omega notation).
      - term: Worst Case
        definition: Maximum time required for algorithm execution (Big O notation).
      - term: Average Case
        definition: Expected time required for algorithm execution (Theta notation).
      - term: Asymptotic Analysis
        definition: Behavior of algorithm as input size approaches infinity.
      - term: Amortized Analysis
        definition: Average performance of operations over time accounting for occasional expensive operations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
