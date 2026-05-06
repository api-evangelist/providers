---
aid: apache-zookeeper
name: Apache ZooKeeper
description: Apache ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services for distributed systems. It provides a hierarchical key-value store (znodes), watches for change notifications, ephemeral nodes for presence detection, and sequential nodes for leader election and distributed locking. ZooKeeper exposes a Java/C client API and an HTTP Admin Server API for monitoring and management. It is widely used by Kafka, Hadoop, HBase, Storm, and other distributed systems.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Configuration Management
  - Distributed Coordination
  - Leader Election
  - Service Discovery
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-zookeeper/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-zookeeper:apache-zookeeper-admin-api
    name: Apache ZooKeeper Admin Server API
    description: The ZooKeeper Admin Server provides HTTP endpoints on port 8080 that expose the four-letter-word equivalent commands as REST endpoints for cluster monitoring, configuration, and diagnostics. Endpoints include /commands/conf (server configuration), /commands/stats (server statistics), /commands/mntr (monitoring metrics), /commands/envi (environment info), /commands/dump (session/ephemeral node dump), /commands/crst (connection reset), and /commands/leader (leader info for QuorumPeerMain).
    humanURL: https://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_4lw
    baseURL: http://localhost:8080/commands
    tags:
      - REST
      - Admin
      - Monitoring
      - Cluster Management
    properties:
      - type: Documentation
        url: https://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_4lw
      - type: OpenAPI
        url: openapi/zookeeper-admin-api.yml
  - aid: apache-zookeeper:apache-zookeeper-client-api
    name: Apache ZooKeeper Client API
    description: The ZooKeeper client API provides Java and C language bindings for distributed coordination operations. Operations include create (create znodes), delete, exists (check existence), getData, setData, getChildren, getACL, setACL, and multi (batch operations). Watch mechanisms notify clients of znode changes. Curator is the recommended high-level Java client with recipes for distributed locks, leader elections, service discovery, and caches.
    humanURL: https://zookeeper.apache.org/doc/current/zookeeperProgrammers.html
    tags:
      - Java
      - C
      - Coordination
      - Leader Election
    properties:
      - type: Documentation
        url: https://zookeeper.apache.org/doc/current/zookeeperProgrammers.html
      - type: APIReference
        url: https://zookeeper.apache.org/doc/current/apidocs/zookeeper-server/
      - type: SDK
        url: https://search.maven.org/search?q=org.apache.zookeeper
        title: Java Maven SDK
      - type: SDK
        url: https://curator.apache.org/
        title: Apache Curator (High-Level Java Client)
common:
  - type: GitHubRepository
    url: https://github.com/apache/zookeeper
  - type: Documentation
    url: https://zookeeper.apache.org/doc/current/
  - type: Portal
    url: https://zookeeper.apache.org/
  - type: GettingStarted
    url: https://zookeeper.apache.org/doc/current/zookeeperStarted.html
  - type: ReleaseNotes
    url: https://github.com/apache/zookeeper/releases
  - type: Support
    url: https://zookeeper.apache.org/lists.html
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: SpectralRules
    url: rules/apache-zookeeper-spectral-rules.yml
  - type: SDK
    url: https://pypi.org/project/kazoo/
    title: Python Kazoo Client
  - type: SDK
    url: https://www.npmjs.com/package/node-zookeeper-client
    title: Node.js Client
  - type: Features
    data:
      - name: Hierarchical Namespace
        description: Tree-structured znode namespace similar to a filesystem for organized configuration storage.
      - name: Watch Notifications
        description: Client watches on znodes trigger one-time callbacks on change events for reactive patterns.
      - name: Ephemeral Nodes
        description: Nodes that disappear when the creating client session expires for presence detection.
      - name: Sequential Nodes
        description: Auto-incrementing sequential znodes for implementing distributed queues and leader election.
      - name: Atomic Operations
        description: Compare-and-set and multi-operation batches for consistent distributed state updates.
      - name: ACL Security
        description: Per-znode access control lists for authentication and authorization of znode operations.
      - name: Observer Mode
        description: Read-only observer servers for scaling read throughput without affecting write quorum.
  - type: UseCases
    data:
      - name: Leader Election
        description: Distributed leader election using ephemeral sequential znodes for coordination.
      - name: Distributed Configuration Management
        description: Centralized configuration storage with watch-based change notification to services.
      - name: Service Registry and Discovery
        description: Service registration and lookup using ephemeral znodes as presence indicators.
      - name: Distributed Locking
        description: Distributed mutex and read/write locks using ephemeral sequential znode recipes.
      - name: Cluster Coordination
        description: Kafka broker coordination, HBase region server management, and Hadoop NameNode fencing.
  - type: Integrations
    data:
      - name: Apache Kafka
        description: ZooKeeper (legacy) for Kafka broker metadata and controller election (replaced by KRaft).
      - name: Apache HBase
        description: ZooKeeper for HBase region server coordination and master election.
      - name: Apache Hadoop
        description: ZooKeeper for HDFS NameNode HA fencing and YARN ResourceManager HA.
      - name: Apache Storm
        description: ZooKeeper for Storm Nimbus coordination and worker heartbeat tracking.
      - name: Apache Solr
        description: ZooKeeper for SolrCloud cluster coordination, configuration, and leader election.
      - name: Apache Curator
        description: High-level ZooKeeper client with recipes for common distributed patterns.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
