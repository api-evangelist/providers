---
aid: rocksdb
name: RocksDB
description: RocksDB is an embeddable persistent key-value store for fast storage, developed at Facebook (Meta) based on LevelDB. It uses a Log-Structured Merge (LSM) tree design optimized for fast, low-latency storage on flash and RAM. RocksDB provides a C++ library with language bindings for Java, Python, Ruby, Rust, and other languages, and is widely used as the storage engine inside databases, data streaming systems, and distributed key-value stores.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/rocksdb/refs/heads/main/apis.yml
tags:
  - RocksDB
  - Key-Value Store
  - Embedded Database
  - Storage Engine
  - Open Source
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rocksdb:rocksdb-embedded-api
    name: RocksDB Embedded API
    description: RocksDB C++ library API providing key-value storage operations including Get, Put, Delete, Merge, iterators, snapshots, column families, transactions, compaction, and backup. The primary interface for embedding RocksDB in applications as a persistent key-value store.
    tags:
      - Key-Value Store
      - Embedded Database
      - Storage Engine
      - C++
      - Open Source
    humanURL: https://rocksdb.org/
    baseURL: https://github.com/facebook/rocksdb
    properties:
      - url: https://rocksdb.org/
        type: Documentation
      - url: https://github.com/facebook/rocksdb/wiki
        type: Documentation
      - url: https://rocksdb.org/docs/getting-started.html
        type: GettingStarted
      - url: https://github.com/facebook/rocksdb
        type: GitHubRepository
    solutions:
      - Fast Storage Engine
      - Embedded Database
      - Write-Heavy Workloads
      - Time-Series Storage
      - Log-Structured Storage
    features:
      - Key-Value Operations (Get, Put, Delete, Merge)
      - Column Families
      - Transactions and ACID Properties
      - Snapshots and Iterators
      - Compaction (Leveled, Universal, FIFO)
      - Write-Ahead Log (WAL)
      - Backup and Restore
      - Compression Support
      - TTL (Time to Live)
      - BlobDB for Large Values
      - Rate Limiting
      - Block Cache
      - Direct I/O
      - Statistics and Monitoring
  - aid: rocksdb:rocksjava-api
    name: RocksJava API
    description: Official Java bindings for RocksDB providing full access to the RocksDB feature set from Java applications. Used in distributed systems like Apache Kafka Streams, Flink, and Cassandra as the underlying storage engine.
    tags:
      - Key-Value Store
      - Java
      - Embedded Database
      - Storage Engine
    humanURL: https://github.com/facebook/rocksdb/wiki/RocksJava-Basics
    baseURL: https://github.com/facebook/rocksdb
    properties:
      - url: https://github.com/facebook/rocksdb/wiki/RocksJava-Basics
        type: Documentation
      - url: https://github.com/facebook/rocksdb
        type: GitHubRepository
      - url: https://mvnrepository.com/artifact/org.rocksdb/rocksdbjni
        type: PackageManager
common:
  - url: https://rocksdb.org/
    type: Website
  - url: https://github.com/facebook/rocksdb
    type: GitHubRepository
  - url: https://github.com/facebook/rocksdb/wiki
    type: Documentation
  - url: https://rocksdb.org/docs/getting-started.html
    type: GettingStarted
  - url: https://github.com/facebook/rocksdb/tree/main/examples
    type: Examples
  - url: https://mvnrepository.com/artifact/org.rocksdb/rocksdbjni
    type: PackageManager
  - url: json-schema/rocksdb-options-schema.json
    type: JSONSchema
  - url: json-schema/rocksdb-key-value-schema.json
    type: JSONSchema
  - url: json-structure/rocksdb-options-structure.json
    type: JSONStructure
  - url: json-ld/rocksdb-context.jsonld
    type: JSONLDContext
  - url: vocabulary/rocksdb-vocabulary.yml
    type: Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
