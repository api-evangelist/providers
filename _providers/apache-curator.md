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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Curator provides a high-level Java API with fluent builders for ZooKeeper operations, along with pre-built recipes for leader election, distributed locks (shared, reentrant, read-write, semaphore), ba
  name: Apache Curator
  slug: apache-curator
artifact_total: 40
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/curator/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apache/curator/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/curator/blob/master/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-curator-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-curator-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://curator.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://curator.apache.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://curator.apache.org/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/curator
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/curator
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/vocabulary/apache-curator-vocabulary.yaml
created: '2026-03-16'
description: Apache Curator is a Java/JVM client library for Apache ZooKeeper, governed by the Apache Software Foundation, that provides a high-level API framework, fluent builders, and pre-built distributed coordination recipes including leader election, distributed locks, barriers, caches, counters, and service discovery. It significantly simplifies writing reliable distributed applications.
examples:
- key_count: 4
  name: Apache Curator Distributed Lock Example
  slug: apache-curator-distributed-lock-example
- key_count: 5
  name: Apache Curator Leader Latch State Example
  slug: apache-curator-leader-latch-state-example
- key_count: 3
  name: Apache Curator Node Data Example
  slug: apache-curator-node-data-example
- key_count: 9
  name: Apache Curator Service Instance Example
  slug: apache-curator-service-instance-example
features:
- description: Wraps the raw ZooKeeper client with connection management, retry policies, and error handling for reliable distributed coordination.
  name: High-Level ZooKeeper Client
- description: Provides a chainable, readable Java DSL for all ZooKeeper CRUD operations including watchers, transactions, and ACLs.
  name: Fluent Builder API
- description: 'Pre-built implementations of distributed patterns: leader election, locks, semaphores, barriers, counters, queues, and group membership.'
  name: Distributed Coordination Recipes
- description: curator-x-discovery provides a ZooKeeper-based service registry and discovery mechanism with instance registration and lookup.
  name: Service Discovery
- description: curator-async provides a CompletionStage-based async API with O/R modeling and schema migration for ZooKeeper data.
  name: Asynchronous DSL
- description: CuratorCache provides an efficient local replica of ZooKeeper subtrees with near-real-time change notifications.
  name: Node Caching
- description: curator-test includes TestingServer (embedded ZooKeeper) and TestingCluster for writing reliable unit and integration tests.
  name: Testing Support
- description: Configurable retry policies (ExponentialBackoff, BoundedExponentialBackoff, RetryNTimes, etc.) for handling transient failures.
  name: Retry Policies
finops:
- name: Apache Curator Finops
  service_category: API
  slug: apache-curator-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-curator.png
integrations:
- description: Curator is built on top of ZooKeeper and requires a running ZooKeeper ensemble.
  name: Apache ZooKeeper
- description: Earlier versions of Kafka used ZooKeeper (managed via Curator) for broker coordination and metadata.
  name: Apache Kafka
- description: HBase uses ZooKeeper for master election and region server coordination, often managed via Curator.
  name: Apache HBase
- description: Storm uses Curator for its ZooKeeper-based cluster state management.
  name: Apache Storm
- description: Spring Cloud Zookeeper integrates with Apache Curator for service discovery and distributed configuration.
  name: Spring Framework
- description: All Curator modules are published to Maven Central under org.apache.curator group ID.
  name: Maven Central
json_schemas:
- name: DistributedLock
  property_count: 4
  slug: apache-curator-distributed-lock
- name: LeaderLatchState
  property_count: 5
  slug: apache-curator-leader-latch-state
- name: NodeData
  property_count: 3
  slug: apache-curator-node-data
- name: ServiceInstance
  property_count: 9
  slug: apache-curator-service-instance
json_structures:
- name: Apache Curator Distributed Lock Structure
  property_count: 4
  slug: apache-curator-distributed-lock-structure
- name: Apache Curator Leader Latch State Structure
  property_count: 5
  slug: apache-curator-leader-latch-state-structure
- name: Apache Curator Node Data Structure
  property_count: 3
  slug: apache-curator-node-data-structure
- name: Apache Curator Service Instance Structure
  property_count: 9
  slug: apache-curator-service-instance-structure
jsonld:
- class_count: 5
  name: Apache Curator Context
  property_count: 27
  slug: apache-curator-context
layout: provider
modified: '2026-04-19'
name: Apache Curator
nav: Providers
network: true
overview: 'Apache Curator publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Apache, Distributed Coordination, Distributed Systems, Java, and Maven.


  The Apache Curator catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apache Curator''s developer surface includes developer portal, documentation, getting-started guide, Stack Overflow tag, and 9 more developer resources.'
plans:
- name: Apache Curator Plans Pricing
  plan_count: 3
  slug: apache-curator-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Apache Curator Rate Limits
  slug: apache-curator-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache Curator API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-curator-jsonschema-spectral-rules
score:
  band: thin
  composite: 27.3
  delta: -7.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 29.6
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 35.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-curator/refs/heads/main/screenshots/apache-curator-2026-06-20T172050.png
security:
- kind: domain-security
  name: Apache Curator Domain Security
  slug: apache-curator-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Curator Vulnerability Disclosure
  slug: apache-curator-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-curator
tags:
- Apache
- Distributed Coordination
- Distributed Systems
- Java
- Maven
- Open Source
- Service Discovery
- ZooKeeper
use_cases:
- description: Elect a single leader across a cluster for coordinating distributed workloads, using LeaderLatch or LeaderSelector recipes.
  name: Distributed Leader Election
- description: Prevent concurrent access to shared resources across JVMs using InterProcessMutex and related lock recipes.
  name: Distributed Locking
- description: Register microservices with ZooKeeper and discover them by type using curator-x-discovery.
  name: Service Registry and Discovery
- description: Store and watch shared configuration data across a cluster with automatic change notifications via NodeCache.
  name: Distributed Configuration
- description: Track which nodes are alive in a distributed cluster using GroupMember and PersistentNode recipes.
  name: Cluster Membership Tracking
- description: Generate globally unique sequential IDs or maintain shared atomic counters across a cluster.
  name: Distributed Counters and IDs
website: https://curator.apache.org/
---
