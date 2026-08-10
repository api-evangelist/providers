---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 13
common:
- group: docs
  title: ''
  type: Reference
  url: https://en.wikipedia.org/wiki/Big_O_notation
- group: docs
  title: ''
  type: Reference
  url: https://www.bigocheatsheet.com
- group: design
  title: ''
  type: Vocabulary
  url: ''
created: '2025-01-01'
description: Big O Notation is a mathematical notation used in computer science to describe the performance or complexity of algorithms, providing a way to classify algorithms by how their runtime or space requirements grow as input size grows. It is foundational to algorithm design, API performance benchmarking, and software engineering education.
features:
- description: Algorithm runtime does not change with input size. Example - hash table lookups.
  name: O(1) - Constant Time
- description: Runtime grows logarithmically with input. Example - binary search.
  name: O(log n) - Logarithmic Time
- description: Runtime grows linearly with input size. Example - linear search.
  name: O(n) - Linear Time
- description: Runtime grows as n multiplied by log n. Example - merge sort, heap sort.
  name: O(n log n) - Linearithmic Time
- description: Runtime grows quadratically with input size. Example - bubble sort, nested loops.
  name: O(n²) - Quadratic Time
- description: Runtime doubles with each additional input element. Example - recursive Fibonacci.
  name: O(2^n) - Exponential Time
- description: Runtime grows factorially. Example - brute-force traveling salesman.
  name: O(n!) - Factorial Time
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/big-o-notation.png
layout: provider
modified: '2026-04-21'
name: Big O Notation
nav: Providers
network: true
overview: Big O Notation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Algorithms, Big O Notation, Complexity, Computer Science, and Performance.
random_paper: 107
score:
  band: minimal
  composite: 7.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 50.0
    governance: 10.4
    operational_transparency: 0.0
  previous_composite: 7.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/big-o-notation/refs/heads/main/screenshots/big-o-notation-2026-06-20T173227.png
slug: big-o-notation
tags:
- Algorithms
- Big O Notation
- Complexity
- Computer Science
- Performance
- Data Structures
use_cases:
- description: Choosing the most efficient algorithm for a given problem based on complexity class.
  name: Algorithm Selection
- description: Analyzing API endpoint performance characteristics under varying data sizes.
  name: API Performance Benchmarking
- description: Evaluating the time and space complexity of code changes during review.
  name: Code Review
- description: Understanding complexity of database operations to optimize query performance.
  name: Database Query Optimization
- description: Predicting how software will perform as data volumes grow at scale.
  name: Scalability Analysis
- description: Preparing for technical interviews requiring algorithm complexity analysis.
  name: Interview Preparation
---
