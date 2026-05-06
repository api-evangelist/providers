---
aid: apache-bookkeeper
name: Apache BookKeeper
description: Apache BookKeeper is a scalable, fault-tolerant, and low-latency storage service optimized for real-time workloads developed by the Apache Software Foundation. It provides a simple log-oriented storage abstraction called ledgers for reliable, replicated storage of sequential data. BookKeeper is used as the durable log storage layer in Apache Pulsar and other distributed messaging and stream processing systems. It provides a Java client API and an HTTP Admin REST API for cluster management, bookie monitoring, and auto-recovery operations.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Distributed Systems
  - Log Storage
  - Open Source
  - Storage
  - Streaming
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-bookkeeper/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-bookkeeper:apache-bookkeeper-admin-api
    name: Apache BookKeeper Admin API
    description: The Apache BookKeeper HTTP Admin API provides REST endpoints for managing and monitoring BookKeeper clusters, bookies, ledgers, and auto-recovery operations. It enables programmatic cluster administration, ledger inspection, bookie health monitoring, and garbage collection management.
    humanURL: https://bookkeeper.apache.org/docs/admin/http
    baseURL: http://localhost:8080
    tags:
      - Administration
      - Cluster Management
      - Monitoring
    properties:
      - type: Documentation
        url: https://bookkeeper.apache.org/docs/admin/http
      - type: OpenAPI
        url: openapi/apache-bookkeeper-admin-openapi.yaml
      - type: GettingStarted
        url: https://bookkeeper.apache.org/docs/getting-started/installation
  - aid: apache-bookkeeper:apache-bookkeeper-java-client
    name: Apache BookKeeper Java Client API
    description: The BookKeeper Java client API provides programmatic access for creating, writing, reading, and managing ledgers. It supports both the legacy LedgerHandle API and the newer Ledger API with explicit durability guarantees.
    humanURL: https://bookkeeper.apache.org/docs/api/ledger-api
    tags:
      - Java
      - Ledger
      - Storage
    properties:
      - type: Documentation
        url: https://bookkeeper.apache.org/docs/api/ledger-api
      - type: APIReference
        url: https://bookkeeper.apache.org/docs/api/javadoc/
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/bookkeeper
  - type: Documentation
    url: https://bookkeeper.apache.org/
  - type: GettingStarted
    url: https://bookkeeper.apache.org/docs/getting-started/installation
  - type: Support
    url: https://bookkeeper.apache.org/community/mailing-lists
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: ChangeLog
    url: https://github.com/apache/bookkeeper/releases
  - type: SpectralRules
    url: rules/apache-bookkeeper-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-bookkeeper-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/bookkeeper-cluster-management.yaml
  - type: Features
    data:
      - name: Ledger Storage
        description: Append-only log segments called ledgers provide the foundational storage primitive for reliable sequential data storage.
      - name: Ensemble Replication
        description: Data is written to a configurable ensemble of bookies with write quorum and ack quorum parameters for fault tolerance.
      - name: Auto-Recovery
        description: Built-in under-replication detection and automatic ledger re-replication when bookie nodes fail.
      - name: HTTP Admin API
        description: RESTful HTTP Admin API for managing ledgers, bookies, cluster configuration, and triggering recovery operations.
      - name: Metrics Export
        description: Prometheus-format metrics endpoint for monitoring bookie performance and storage utilization.
      - name: Auditor Election
        description: ZooKeeper-based leader election for the auditor role responsible for detecting under-replicated ledgers.
      - name: Garbage Collection
        description: Configurable garbage collection for reclaiming storage from deleted or expired ledger data.
      - name: Journal and Ledger Storage
        description: Separate journal and ledger storage paths optimized for sequential write throughput and random read performance.
  - type: UseCases
    data:
      - name: Durable Log Storage
        description: Serve as the replicated, durable write-ahead log for Apache Pulsar topics and distributed streaming systems.
      - name: Distributed Transaction Logs
        description: Store distributed transaction log segments for systems requiring exactly-once semantics and durable commit records.
      - name: Metadata Store
        description: Persist metadata and configuration data for distributed systems requiring consistent, replicated storage.
      - name: Stream Processing Storage
        description: Provide low-latency, high-throughput sequential storage for real-time stream processing pipelines.
      - name: Cluster Administration
        description: Monitor and manage BookKeeper clusters using the HTTP Admin API for operational visibility and recovery.
  - type: Integrations
    data:
      - name: Apache Pulsar
        description: BookKeeper serves as the durable log storage layer for Apache Pulsar messaging topics.
      - name: Apache ZooKeeper
        description: ZooKeeper is used for bookie coordination, auditor election, and cluster metadata management.
      - name: Apache Hadoop
        description: BookKeeper can be used with Hadoop ecosystem tools for reliable log storage alongside HDFS.
      - name: Prometheus
        description: BookKeeper exports Prometheus-format metrics for cluster monitoring and alerting.
      - name: Grafana
        description: Grafana dashboards consume BookKeeper Prometheus metrics for operational visibility.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
