---
aid: apache-curator
name: Apache Curator
description: Apache Curator is a Java/JVM client library for Apache ZooKeeper, governed by the Apache Software Foundation, that provides a high-level API framework, fluent builders, and pre-built distributed coordination recipes including leader election, distributed locks, barriers, caches, counters, and service discovery. It significantly simplifies writing reliable distributed applications.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Distributed Coordination
  - Distributed Systems
  - Java
  - Maven
  - Open Source
  - Service Discovery
  - ZooKeeper
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-curator:apache-curator
    name: Apache Curator
    description: Curator provides a high-level Java API with fluent builders for ZooKeeper operations, along with pre-built recipes for leader election, distributed locks (shared, reentrant, read-write, semaphore), barriers, caches (CuratorCache, PathCache, TreeCache), distributed counters, queues, group membership, and service discovery via curator-x-discovery.
    humanURL: https://curator.apache.org/docs/about
    tags:
      - Barriers
      - Caches
      - Distributed Locks
      - Java
      - Leader Election
      - Maven
      - Queues
      - Service Discovery
      - ZooKeeper
    properties:
      - type: Documentation
        url: https://curator.apache.org/docs/about
      - type: APIReference
        url: https://curator.apache.org/apidocs/
      - type: GettingStarted
        url: https://curator.apache.org/docs/getting-started
      - type: GitHubRepository
        url: https://github.com/apache/curator
      - type: SDK
        url: https://mvnrepository.com/artifact/org.apache.curator/curator-framework
        title: curator-framework (Maven)
      - type: SDK
        url: https://mvnrepository.com/artifact/org.apache.curator/curator-recipes
        title: curator-recipes (Maven)
      - type: SDK
        url: https://mvnrepository.com/artifact/org.apache.curator/curator-x-discovery
        title: curator-x-discovery (Maven)
      - type: SDK
        url: https://mvnrepository.com/artifact/org.apache.curator/curator-async
        title: curator-async (Maven)
      - type: Tools
        url: https://mvnrepository.com/artifact/org.apache.curator/curator-test
        title: curator-test (Testing)
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/json-schema/apache-curator-distributed-lock-schema.json
        title: Distributed Lock
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/json-schema/apache-curator-leader-latch-state-schema.json
        title: Leader Latch State
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/json-schema/apache-curator-node-data-schema.json
        title: Node Data
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/json-schema/apache-curator-service-instance-schema.json
        title: Service Instance
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/json-structure/apache-curator-distributed-lock-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/json-structure/apache-curator-leader-latch-state-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/json-structure/apache-curator-node-data-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/json-structure/apache-curator-service-instance-structure.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/json-ld/apache-curator-context.jsonld
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/examples/apache-curator-distributed-lock-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/examples/apache-curator-leader-latch-state-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/examples/apache-curator-node-data-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/examples/apache-curator-service-instance-example.json
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: Portal
    url: https://curator.apache.org/
  - type: Documentation
    url: https://curator.apache.org/docs/
  - type: GettingStarted
    url: https://curator.apache.org/docs/getting-started
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/curator
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/curator
  - type: Features
    data:
      - name: High-Level ZooKeeper Client
        description: Wraps the raw ZooKeeper client with connection management, retry policies, and error handling for reliable distributed coordination.
      - name: Fluent Builder API
        description: Provides a chainable, readable Java DSL for all ZooKeeper CRUD operations including watchers, transactions, and ACLs.
      - name: Distributed Coordination Recipes
        description: 'Pre-built implementations of distributed patterns: leader election, locks, semaphores, barriers, counters, queues, and group membership.'
      - name: Service Discovery
        description: curator-x-discovery provides a ZooKeeper-based service registry and discovery mechanism with instance registration and lookup.
      - name: Asynchronous DSL
        description: curator-async provides a CompletionStage-based async API with O/R modeling and schema migration for ZooKeeper data.
      - name: Node Caching
        description: CuratorCache provides an efficient local replica of ZooKeeper subtrees with near-real-time change notifications.
      - name: Testing Support
        description: curator-test includes TestingServer (embedded ZooKeeper) and TestingCluster for writing reliable unit and integration tests.
      - name: Retry Policies
        description: Configurable retry policies (ExponentialBackoff, BoundedExponentialBackoff, RetryNTimes, etc.) for handling transient failures.
  - type: UseCases
    data:
      - name: Distributed Leader Election
        description: Elect a single leader across a cluster for coordinating distributed workloads, using LeaderLatch or LeaderSelector recipes.
      - name: Distributed Locking
        description: Prevent concurrent access to shared resources across JVMs using InterProcessMutex and related lock recipes.
      - name: Service Registry and Discovery
        description: Register microservices with ZooKeeper and discover them by type using curator-x-discovery.
      - name: Distributed Configuration
        description: Store and watch shared configuration data across a cluster with automatic change notifications via NodeCache.
      - name: Cluster Membership Tracking
        description: Track which nodes are alive in a distributed cluster using GroupMember and PersistentNode recipes.
      - name: Distributed Counters and IDs
        description: Generate globally unique sequential IDs or maintain shared atomic counters across a cluster.
  - type: Integrations
    data:
      - name: Apache ZooKeeper
        description: Curator is built on top of ZooKeeper and requires a running ZooKeeper ensemble.
      - name: Apache Kafka
        description: Earlier versions of Kafka used ZooKeeper (managed via Curator) for broker coordination and metadata.
      - name: Apache HBase
        description: HBase uses ZooKeeper for master election and region server coordination, often managed via Curator.
      - name: Apache Storm
        description: Storm uses Curator for its ZooKeeper-based cluster state management.
      - name: Spring Framework
        description: Spring Cloud Zookeeper integrates with Apache Curator for service discovery and distributed configuration.
      - name: Maven Central
        description: All Curator modules are published to Maven Central under org.apache.curator group ID.
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/vocabulary/apache-curator-vocabulary.yaml
---
