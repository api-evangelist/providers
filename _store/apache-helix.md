---
aid: apache-helix
name: Apache Helix
description: Apache Helix is a generic cluster management framework for partitioned and replicated distributed resources. It automates partition management, replication, fault tolerance, and cluster expansion for distributed systems, providing a REST API for cluster administration and a Java API for participant, spectator, and controller roles.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Cluster Management
  - Distributed Systems
  - Open Source
  - Partitioning
  - Replication
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-helix/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-helix:apache-helix-rest-api
    name: Apache Helix REST API
    description: REST API for managing Apache Helix clusters, instances, resources, and partition state assignments, including ideal state queries and external view inspection.
    humanURL: https://helix.apache.org/0.9.9-docs/tutorial_admin.html
    baseURL: http://localhost:9100
    tags:
      - Cluster Management
      - Instances
      - Partitions
      - REST
      - Resources
    properties:
      - type: Documentation
        url: https://helix.apache.org/0.9.9-docs/tutorial_admin.html
      - type: OpenAPI
        url: openapi/apache-helix-rest-openapi.yml
      - type: JSONSchema
        url: json-schema/helix-rest-cluster-schema.json
      - type: JSON-LD
        url: json-ld/apache-helix-rest-context.jsonld
  - aid: apache-helix:apache-helix-java-api
    name: Apache Helix Java API
    description: Java API for implementing Helix participant, spectator, and controller roles, with APIs for resource management, task execution, and state machine definitions.
    humanURL: https://helix.apache.org/0.9.9-docs/tutorial_participant.html
    tags:
      - Java
      - SDK
      - State Machine
    properties:
      - type: Documentation
        url: https://helix.apache.org/0.9.9-docs/tutorial_participant.html
      - type: SDK
        url: https://search.maven.org/artifact/org.apache.helix/helix-core
        title: Java SDK (Maven Central)
common:
  - type: Documentation
    url: https://helix.apache.org/
  - type: GettingStarted
    url: https://helix.apache.org/0.9.9-docs/Quickstart.html
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/helix
  - type: SpectralRules
    url: rules/apache-helix-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-helix-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/helix-cluster-management.yaml
  - type: Features
    data:
      - name: Automatic Partition Management
        description: Automatically assign and balance partitions across cluster nodes using pluggable rebalancer algorithms.
      - name: State Machine Framework
        description: Define custom resource state machines (e.g., Master-Slave, Leader-Standby) for any distributed service.
      - name: Fault Tolerance
        description: Detect node failures and automatically reassign partitions to maintain replication targets.
      - name: REST API
        description: HTTP REST API for cluster administration, resource management, and state inspection.
      - name: Task Framework
        description: Distributed task scheduling framework for batch jobs and recurring workflows with failure handling.
      - name: ZooKeeper Integration
        description: Uses Apache ZooKeeper as the distributed coordination backend for cluster state storage.
      - name: Spectator API
        description: Read-only API for external services to observe resource state and routing decisions.
      - name: Cloud-Aware Rebalancing
        description: Rack and zone-aware partition placement for fault-domain isolation in cloud environments.
  - type: UseCases
    data:
      - name: Distributed Database Cluster Management
        description: Manage shard assignment and replication for distributed databases like DistributedLog or Espresso.
      - name: Search Index Partition Management
        description: Automatically balance and assign search index shards across a cluster of query servers.
      - name: Distributed Task Scheduling
        description: Schedule and execute distributed batch tasks with automatic retry and failure recovery.
      - name: Microservices Load Balancing
        description: Use Helix spectator API to implement client-side load balancing based on partition state.
      - name: Stateful Service Migration
        description: Perform rolling upgrades and partition migrations without service downtime.
  - type: Integrations
    data:
      - name: Apache ZooKeeper
        description: ZooKeeper is the required coordination backend for Helix cluster state management.
      - name: Apache Kafka
        description: Helix is used internally by some Kafka ecosystem projects for partition management.
      - name: LinkedIn Pinot
        description: Apache Pinot uses Helix for real-time OLAP cluster partition and segment management.
      - name: LinkedIn Venice
        description: Venice feature store uses Helix for managing data store partition assignments.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
