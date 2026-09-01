---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Apache Zookeeper Agentic Access
  operation_count: 21
  slug: apache-zookeeper-agentic-access
  summary_line: 21 operations
api_count: 1
apis:
- description: The ZooKeeper client API provides Java and C language bindings for distributed coordination operations. Operations include create (create znodes), delete, exists (check existence), getData, setData, g
  name: Apache ZooKeeper Client API
  slug: apache-zookeeper-client-api
- description: Cluster and ensemble information
  name: Apache ZooKeeper Cluster API
  slug: apache-zookeeper-cluster-api
- description: Server configuration information
  name: Apache ZooKeeper Configuration API
  slug: apache-zookeeper-configuration-api
- description: Server health checks
  name: Apache ZooKeeper Health API
  slug: apache-zookeeper-health-api
- description: Server statistics and metrics
  name: Apache ZooKeeper Monitoring API
  slug: apache-zookeeper-monitoring-api
- description: ZooKeeper watch information
  name: Apache ZooKeeper Watches API
  slug: apache-zookeeper-watches-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache ZooKeeper Admin Server Cluster API
  slug: open-apache-zookeeper-cluster-api
- collection_type: open
  name: Apache ZooKeeper Admin Server Cluster Configuration API
  slug: open-apache-zookeeper-configuration-api
- collection_type: open
  name: Apache ZooKeeper Admin Server Cluster Health API
  slug: open-apache-zookeeper-health-api
- collection_type: open
  name: Apache ZooKeeper Admin Server Cluster Monitoring API
  slug: open-apache-zookeeper-monitoring-api
- collection_type: open
  name: Apache ZooKeeper Admin Server Cluster Watches API
  slug: open-apache-zookeeper-watches-api
- collection_type: open
  name: Apache ZooKeeper Admin Server API
  slug: open-zookeeper-admin-api
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/zookeeper/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-zookeeper-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-zookeeper-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-zookeeper-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/zookeeper
- group: docs
  title: ''
  type: Documentation
  url: https://zookeeper.apache.org/doc/current/
- group: start
  title: ''
  type: Portal
  url: https://zookeeper.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://zookeeper.apache.org/doc/current/zookeeperStarted.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/apache/zookeeper/releases
- group: operate
  title: ''
  type: Support
  url: https://zookeeper.apache.org/lists.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-zookeeper-spectral-rules.yml
- group: build
  title: Python Kazoo Client
  type: SDKs
  url: https://pypi.org/project/kazoo/
- group: build
  title: Node.js Client
  type: SDKs
  url: https://www.npmjs.com/package/node-zookeeper-client
created: '2026-03-16'
description: Apache ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services for distributed systems. It provides a hierarchical key-value store (znodes), watches for change notifications, ephemeral nodes for presence detection, and sequential nodes for leader election and distributed locking. ZooKeeper exposes a Java/C client API and an HTTP Admin Server API for monitoring and management. It is widely used by Kafka, Hadoop, HBase, Storm, and other distributed systems.
features:
- description: Tree-structured znode namespace similar to a filesystem for organized configuration storage.
  name: Hierarchical Namespace
- description: Client watches on znodes trigger one-time callbacks on change events for reactive patterns.
  name: Watch Notifications
- description: Nodes that disappear when the creating client session expires for presence detection.
  name: Ephemeral Nodes
- description: Auto-incrementing sequential znodes for implementing distributed queues and leader election.
  name: Sequential Nodes
- description: Compare-and-set and multi-operation batches for consistent distributed state updates.
  name: Atomic Operations
- description: Per-znode access control lists for authentication and authorization of znode operations.
  name: ACL Security
- description: Read-only observer servers for scaling read throughput without affecting write quorum.
  name: Observer Mode
finops:
- name: Apache Zookeeper Finops
  service_category: API
  slug: apache-zookeeper-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-zookeeper.png
integrations:
- description: ZooKeeper (legacy) for Kafka broker metadata and controller election (replaced by KRaft).
  name: Apache Kafka
- description: ZooKeeper for HBase region server coordination and master election.
  name: Apache HBase
- description: ZooKeeper for HDFS NameNode HA fencing and YARN ResourceManager HA.
  name: Apache Hadoop
- description: ZooKeeper for Storm Nimbus coordination and worker heartbeat tracking.
  name: Apache Storm
- description: ZooKeeper for SolrCloud cluster coordination, configuration, and leader election.
  name: Apache Solr
- description: High-level ZooKeeper client with recipes for common distributed patterns.
  name: Apache Curator
layout: provider
modified: '2026-05-19'
name: Apache ZooKeeper
nav: Providers
network: true
overview: 'Apache ZooKeeper publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Cluster API, Configuration API, Health API, and 2 more. Tagged areas include Configuration Management, Distributed Coordination, Leader Election, Service Discovery, and Open-Source.


  The Apache ZooKeeper catalog on APIs.io includes 1 Spectral governance ruleset.


  Apache ZooKeeper''s developer surface includes documentation, developer portal, getting-started guide, release notes, support, and 10 more developer resources.'
plans:
- name: Apache Zookeeper Plans Pricing
  plan_count: 3
  slug: apache-zookeeper-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Apache Zookeeper Rate Limits
  slug: apache-zookeeper-rate-limits
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Apache ZooKeeper API Rules
  rule_count: 12
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 3
  slug: apache-zookeeper-spectral-rules
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 60.5
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.6
    commercial_clarity: 28.6
    contract_governance: 13.6
    contract_quality: 46.9
    developer_ergonomics: 59.5
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 28.9
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-zookeeper/refs/heads/main/screenshots/apache-zookeeper-2026-06-20T172200.png
security:
- kind: domain-security
  name: Apache Zookeeper Domain Security
  slug: apache-zookeeper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Zookeeper Vulnerability Disclosure
  slug: apache-zookeeper-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-zookeeper
tags:
- Configuration Management
- Distributed Coordination
- Leader Election
- Service Discovery
- Open-Source
use_cases:
- description: Distributed leader election using ephemeral sequential znodes for coordination.
  name: Leader Election
- description: Centralized configuration storage with watch-based change notification to services.
  name: Distributed Configuration Management
- description: Service registration and lookup using ephemeral znodes as presence indicators.
  name: Service Registry and Discovery
- description: Distributed mutex and read/write locks using ephemeral sequential znode recipes.
  name: Distributed Locking
- description: Kafka broker coordination, HBase region server management, and Hadoop NameNode fencing.
  name: Cluster Coordination
website: https://zookeeper.apache.org/
---
