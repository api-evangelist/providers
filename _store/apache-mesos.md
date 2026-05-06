---
aid: apache-mesos
name: Apache Mesos
description: Apache Mesos is a retired cluster manager (now in the Apache Attic) that provided efficient resource isolation and sharing across distributed applications or frameworks. It abstracted CPU, memory, storage, and other compute resources from machines, enabling fault-tolerant and elastic distributed systems. Mesos exposed comprehensive HTTP APIs for schedulers, operators, executors, and agents.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cluster Management
  - Distributed Systems
  - Resource Management
  - Scheduling
  - Retired
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-mesos/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-mesos:mesos-operator-http-api
    name: Apache Mesos Operator HTTP API
    description: The Mesos Operator HTTP API provides a POST-based API at /api/v1 on both master and agent nodes for cluster administration including health checks, state queries, resource reservation, maintenance scheduling, quota management, and agent lifecycle management. Supports JSON and Protobuf encoding.
    humanURL: https://mesos.apache.org/documentation/latest/operator-http-api/
    tags:
      - Cluster Management
      - HTTP API
      - Operations
      - Resource Management
    properties:
      - type: Documentation
        url: https://mesos.apache.org/documentation/latest/operator-http-api/
      - type: GitHubRepository
        url: https://github.com/apache/mesos
  - aid: apache-mesos:mesos-scheduler-http-api
    name: Apache Mesos Scheduler HTTP API
    description: The Mesos Scheduler HTTP API at /api/v1/scheduler enables framework schedulers to subscribe to resource offers, launch tasks, kill tasks, reconcile status, and manage framework lifecycle over a persistent HTTP connection with RecordIO-encoded streaming responses.
    humanURL: https://mesos.apache.org/documentation/latest/scheduler-http-api/
    tags:
      - Framework
      - HTTP API
      - Scheduling
      - Tasks
    properties:
      - type: Documentation
        url: https://mesos.apache.org/documentation/latest/scheduler-http-api/
      - type: GitHubRepository
        url: https://github.com/apache/mesos
common:
  - type: Portal
    url: https://mesos.apache.org/
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/mesos
  - type: Documentation
    url: https://mesos.apache.org/documentation/latest/
  - type: Blog
    url: https://mesos.apache.org/blog/
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Features
    data:
      - name: Resource Abstraction
        description: Abstracts CPU, memory, storage, and other compute resources from physical machines across the entire cluster.
      - name: Two-Level Scheduling
        description: Framework schedulers receive resource offers from Mesos and decide how to use them, enabling coexistence of diverse workloads.
      - name: Linear Scalability
        description: Proven to scale to tens of thousands of nodes with fault-tolerant replicated master using ZooKeeper.
      - name: Container Support
        description: Native Docker and AppC container image support for running containerized workloads.
      - name: HTTP API
        description: Comprehensive HTTP API supporting JSON and Protobuf encoding for schedulers, operators, executors, and agents.
      - name: High Availability
        description: Fault-tolerant master failover via ZooKeeper with automatic leader election and state recovery.
      - name: Resource Reservations
        description: Static and dynamic resource reservations for frameworks and roles with quota management.
      - name: Maintenance Scheduling
        description: Built-in maintenance window scheduling for graceful draining and reactivation of agent nodes.
  - type: UseCases
    data:
      - name: Distributed Systems Orchestration
        description: Run multiple distributed frameworks including Hadoop, Spark, and Kafka on shared cluster resources.
      - name: Container Orchestration
        description: Schedule and manage containerized workloads across a datacenter with resource isolation.
      - name: Big Data Processing
        description: Run Apache Spark, Hadoop MapReduce, and other big data frameworks on Mesos-managed resources.
      - name: Microservices Platform
        description: Host microservices workloads with Marathon framework providing long-running service scheduling on Mesos.
  - type: Integrations
    data:
      - name: Apache Hadoop
        description: Run Hadoop MapReduce jobs on Mesos-managed cluster resources.
      - name: Apache Spark
        description: Apache Spark supports Mesos as a cluster manager for distributed job execution.
      - name: Apache Kafka
        description: Kafka brokers can be scheduled and managed on Mesos clusters.
      - name: Apache ZooKeeper
        description: ZooKeeper provides leader election and state storage for Mesos master high availability.
      - name: Docker
        description: Native Docker container image and runtime support for containerized workload execution.
      - name: Elasticsearch
        description: Elasticsearch can be deployed and managed as a framework on Mesos clusters.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
