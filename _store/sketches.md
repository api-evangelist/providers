---
aid: sketches
url: https://raw.githubusercontent.com/api-evangelist/sketches/refs/heads/main/apis.yml
name: Sketches
description: Sketches are probabilistic data structures used in computing and data engineering to approximate answers to queries over large data streams with controlled error bounds and dramatically reduced memory requirements. Common sketches include Count-Min Sketch (frequency estimation), HyperLogLog (cardinality estimation), Bloom Filter (membership testing), and T-Digest (quantile estimation). APIs in this domain include sketch-native databases like Apache DataSketches, Redis probabilistic data structures, and cloud analytics services that implement sketch algorithms for real-time analytics, approximate query processing, and streaming analytics.
tags:
  - Data Structures
  - Probabilistic Algorithms
  - Streaming Analytics
  - Approximate Query Processing
  - Big Data
  - Real-Time Analytics
created: '2025'
modified: '2026-05-02'
apis:
  - aid: sketches:apache-datasketches-api
    name: Apache DataSketches API
    description: Apache DataSketches is the open-source library providing production-quality implementations of sketch algorithms including Theta Sketches (set operations), Quantiles Sketches (percentile estimation), HLL (HyperLogLog for cardinality), CPC, Frequency, and Tuple sketches. It is widely used in data warehouses and OLAP systems including Apache Druid, Apache Spark, and Amazon Redshift. The library provides Java, C++, and Python APIs.
    humanURL: https://datasketches.apache.org
    baseURL: https://datasketches.apache.org
    tags:
      - Open Source
      - Apache
      - Data Structures
      - Probabilistic Algorithms
      - Analytics
    properties:
      - url: https://datasketches.apache.org
        type: Documentation
      - url: https://github.com/apache/datasketches-java
        type: GitHubOrg
  - aid: sketches:redis-probabilistic-api
    name: Redis Probabilistic Data Structures API
    description: Redis provides native probabilistic data structure commands through the Redis Stack (RedisBloom module), offering server-side implementations of Bloom Filter, Cuckoo Filter, Count-Min Sketch, Top-K, and HyperLogLog. These are accessible via the Redis command interface and all official Redis client libraries, enabling high-throughput approximate data processing without external dependencies.
    humanURL: https://redis.io/docs/data-types/probabilistic/
    baseURL: https://redis.io
    tags:
      - Redis
      - Probabilistic Data Structures
      - Real-Time
      - In-Memory
    properties:
      - url: https://redis.io/docs/data-types/probabilistic/
        type: Documentation
      - url: https://redis.io
        type: Website
  - aid: sketches:amazon-redshift-sketches-api
    name: Amazon Redshift Approximate Query API
    description: Amazon Redshift supports approximate query processing using HyperLogLog sketch functions (HLL_CREATE_SKETCH, HLL_COMBINE, HLL_CARDINALITY) for fast cardinality estimation on large datasets. These native SQL functions enable analytics teams to run near-instantaneous approximate COUNT DISTINCT queries on billions of rows with controlled error bounds.
    humanURL: https://docs.aws.amazon.com/redshift/latest/dg/r_HLL_function.html
    baseURL: https://aws.amazon.com
    tags:
      - AWS
      - Redshift
      - Analytics
      - HyperLogLog
      - SQL
    properties:
      - url: https://docs.aws.amazon.com/redshift/latest/dg/r_HLL_function.html
        type: Documentation
common:
  - type: Website
    url: https://datasketches.apache.org
  - type: JSON-LD
    url: json-ld/sketches-context.jsonld
  - type: Vocabulary
    url: vocabulary/sketches-vocabulary.yml
---
