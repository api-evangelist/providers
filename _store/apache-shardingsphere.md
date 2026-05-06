---
aid: apache-shardingsphere
name: Apache ShardingSphere
description: Apache ShardingSphere is an open-source ecosystem for distributed database systems providing data sharding, distributed transactions, and database governance. It supports MySQL, PostgreSQL, and other databases with transparent sharding capabilities.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Database
  - Distributed SQL
  - Read-Write Splitting
  - Sharding
  - SQL
  - Apache
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-shardingsphere/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-shardingsphere:apache-shardingsphere
    name: Apache ShardingSphere
    description: ShardingSphere provides ShardingSphere-JDBC for Java applications, ShardingSphere-Proxy with MySQL/PostgreSQL wire protocol compatibility, DistSQL for distributed database management, and a Governance API for cluster management.
    humanURL: https://shardingsphere.apache.org/document/current/en/overview/
    tags:
      - Database
      - Distributed SQL
      - REST
      - Apache
      - Open Source
    properties:
      - type: Documentation
        url: https://shardingsphere.apache.org/document/current/en/overview/
      - type: Documentation
        url: https://shardingsphere.apache.org/document/current/
      - type: OpenAPI
        url: openapi/apache-shardingsphere-rest-api.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/shardingsphere
  - type: Documentation
    url: https://shardingsphere.apache.org/
  - type: SpectralRules
    url: rules/apache-shardingsphere-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-shardingsphere-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shardingsphere-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-shardingsphere-context.jsonld
  - type: Features
    data:
      - name: Database Sharding
        description: Horizontal database sharding with flexible sharding algorithms
      - name: Read-Write Splitting
        description: Transparent primary/replica read-write splitting
      - name: Distributed Transactions
        description: XA and BASE distributed transaction support
      - name: Data Encryption
        description: Transparent data encryption at the SQL layer
      - name: Shadow Database
        description: Shadow database for production traffic testing
      - name: DistSQL
        description: SQL-based distributed database management language
      - name: Database Federation
        description: Query across heterogeneous database instances
  - type: UseCases
    data:
      - name: Database Scale-Out
        description: Horizontally scale relational databases without changing application code
      - name: Multi-Tenant Sharding
        description: Shard data by tenant ID for SaaS applications
      - name: Read Scaling
        description: Scale read traffic with primary/replica splitting
      - name: Data Migration
        description: Online data migration between database clusters
  - type: Integrations
    data:
      - name: MySQL
        description: MySQL-compatible sharding and proxy
      - name: PostgreSQL
        description: PostgreSQL protocol support for sharding
      - name: Apache ZooKeeper
        description: Cluster coordination and configuration storage
      - name: Spring Boot
        description: ShardingSphere Spring Boot starter for Java applications
      - name: Kubernetes
        description: Kubernetes operator for cloud-native deployment
---
