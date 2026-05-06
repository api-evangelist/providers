---
aid: acid
url: https://raw.githubusercontent.com/api-evangelist/acid/refs/heads/main/apis.yml
name: ACID
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - ACID
  - Database
  - Transactions
  - Atomicity
  - Consistency
  - Isolation
  - Durability
  - Distributed Systems
description: ACID (Atomicity, Consistency, Isolation, Durability) is a set of properties that guarantee database transactions are processed reliably even in the face of errors, power failures, or system crashes. These four properties ensure that data remains accurate and consistent, making ACID compliance a fundamental requirement for relational databases, distributed systems, and financial APIs.
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - name: PostgreSQL Transaction API
    description: PostgreSQL provides full ACID compliance through its transaction management system including BEGIN, COMMIT, ROLLBACK, SAVEPOINT, and isolation level controls (READ COMMITTED, REPEATABLE READ, SERIALIZABLE). PostgreSQL uses Multi-Version Concurrency Control (MVCC) to provide high concurrency while maintaining strong data consistency guarantees.
    humanURL: https://www.postgresql.org/docs/current/transaction-iso.html
    baseURL: https://www.postgresql.org/
    tags:
      - PostgreSQL
      - RDBMS
      - MVCC
      - ACID
      - SQL
    properties:
      - type: Documentation
        url: https://www.postgresql.org/docs/current/transaction-iso.html
      - type: Documentation
        url: https://www.postgresql.org/docs/current/sql-begin.html
        title: PostgreSQL BEGIN Transaction
      - type: GitHubRepository
        url: https://github.com/postgres/postgres
  - name: CockroachDB Distributed SQL API
    description: CockroachDB is a distributed SQL database providing serializable ACID transactions across multiple nodes and regions. It uses the Raft consensus algorithm and supports the PostgreSQL wire protocol. CockroachDB offers REST and SQL APIs for managing distributed transactions while maintaining global consistency without a central coordinator.
    humanURL: https://www.cockroachlabs.com/docs/stable/
    baseURL: https://cockroachlabs.cloud/
    tags:
      - CockroachDB
      - Distributed SQL
      - ACID
      - Serializable
      - Cloud Native
    properties:
      - type: Documentation
        url: https://www.cockroachlabs.com/docs/stable/
      - type: Documentation
        url: https://www.cockroachlabs.com/docs/stable/transactions.html
        title: CockroachDB Transactions
      - type: GitHubRepository
        url: https://github.com/cockroachdb/cockroach
  - name: Google Spanner API
    description: Google Spanner is a globally distributed, externally consistent database providing ACID transactions at global scale using TrueTime clock synchronization (GPS receivers and atomic clocks). The Cloud Spanner API offers both read-write transactions and read-only transactions with configurable staleness bounds. It is available via REST and gRPC.
    humanURL: https://cloud.google.com/spanner/docs/transactions
    baseURL: https://spanner.googleapis.com/
    tags:
      - Google Spanner
      - Distributed Database
      - Global Scale
      - ACID
      - TrueTime
    properties:
      - type: Documentation
        url: https://cloud.google.com/spanner/docs/transactions
      - type: APIReference
        url: https://cloud.google.com/spanner/docs/reference/rest
      - type: OpenAPI
        url: https://raw.githubusercontent.com/APIs-guru/openapi-directory/main/APIs/googleapis.com/spanner/v1/openapi.yaml
  - name: Amazon Aurora Transactions API
    description: Amazon Aurora provides ACID-compliant transactions for both MySQL-compatible and PostgreSQL-compatible editions. Aurora's distributed storage layer provides durability across 3 availability zones with 6-way replication. The Aurora Data API enables HTTP-based serverless SQL transactions with automatic commit and rollback capabilities.
    humanURL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html
    baseURL: https://rds.amazonaws.com/
    tags:
      - AWS Aurora
      - MySQL
      - PostgreSQL
      - ACID
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html
      - type: APIReference
        url: https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/
        title: Aurora Data API Reference
  - name: Atomikos Transaction API
    description: Atomikos provides ACID transaction management middleware for distributed microservices, supporting XA transactions across REST services using the Try-Confirm/Cancel (TCC) pattern. It enables ACID guarantees spanning multiple databases and message brokers without requiring a central coordinator in many scenarios.
    humanURL: https://www.atomikos.com/
    baseURL: https://www.atomikos.com/
    tags:
      - Atomikos
      - Distributed Transactions
      - TCC Pattern
      - Microservices
      - XA
    properties:
      - type: Documentation
        url: https://www.atomikos.com/
      - type: Documentation
        url: https://www.atomikos.com/Blog/ACIDTransactionsAcrossMicroservices
        title: ACID Transactions Across Microservices
common:
  - type: Website
    url: https://en.wikipedia.org/wiki/ACID
    title: ACID Wikipedia Reference
  - type: GitHubRepository
    url: https://github.com/cockroachdb/cockroach
    title: CockroachDB Open Source Repository
  - type: Features
    data:
      - name: Atomicity
        description: 'Transactions are all-or-nothing: either all operations in a transaction succeed and are committed, or none are applied and the database is rolled back to its prior state.'
      - name: Consistency
        description: A transaction brings the database from one valid, consistent state to another, enforcing all defined constraints, triggers, and cascades. No transaction can leave data in an invalid state.
      - name: Isolation
        description: Concurrent transactions execute as if they were serialized, preventing interference. Isolation levels (READ COMMITTED, REPEATABLE READ, SERIALIZABLE) control the degree of visibility between concurrent transactions.
      - name: Durability
        description: Once a transaction is committed, it remains committed even in the event of system crashes, power failures, or other errors, typically achieved through write-ahead logging (WAL) and replication.
      - name: Distributed ACID
        description: Modern distributed databases extend ACID guarantees across multiple nodes, regions, and data centers using consensus algorithms (Raft, Paxos) and synchronized clocks (TrueTime).
      - name: REST API Transaction Patterns
        description: Design patterns for ACID-like guarantees in REST APIs include Two-Phase Commit (2PC), Try-Confirm/Cancel (TCC), and Saga patterns for managing distributed transactions across microservices.
  - type: UseCases
    data:
      - name: Financial Transactions
        description: Banking and payment systems require ACID compliance to ensure monetary transfers are atomic — debits and credits always balance — and durable across system failures.
      - name: Inventory Management
        description: E-commerce and supply chain systems use ACID transactions to prevent overselling by ensuring inventory decrements and order creation are atomic.
      - name: Distributed Microservices Coordination
        description: Microservices architectures use Saga and TCC patterns to achieve eventual consistency with compensating transactions when full ACID across services is not feasible.
      - name: Multi-Region Database Replication
        description: Global applications use databases like Google Spanner and CockroachDB to maintain ACID consistency across geographic regions without sacrificing availability.
      - name: Idempotent API Design
        description: REST APIs use database transactions to implement idempotency keys, ensuring duplicate requests produce the same result without double processing.
  - type: Integrations
    data:
      - name: PostgreSQL
        description: The most widely deployed open-source RDBMS with full ACID compliance via MVCC and configurable transaction isolation levels.
      - name: MySQL / MariaDB
        description: Popular open-source databases providing ACID compliance through the InnoDB storage engine with row-level locking and MVCC.
      - name: MongoDB Multi-Document Transactions
        description: MongoDB added multi-document ACID transactions in version 4.0, extending its document model with ACID guarantees across documents and collections.
      - name: Apache Kafka Transactions
        description: Kafka's transactional API (since 0.11) enables exactly-once semantics with atomic writes to multiple partitions, providing ACID-like guarantees for stream processing pipelines.
      - name: Saga Pattern / Orchestration
        description: The Saga pattern decomposes long-running transactions into a series of local transactions with compensating actions for distributed consistency without 2PC overhead.
  - type: JSON-LD
    url: https://raw.githubusercontent.com/api-evangelist/acid/refs/heads/main/json-ld/acid-context.jsonld
    title: ACID JSON-LD Context
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/acid/refs/heads/main/vocabulary/acid-vocabulary.yaml
    title: ACID Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
