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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 11
  human_in_the_loop: 2
  name: Apache Storm Agentic Access
  operation_count: 25
  slug: apache-storm-agentic-access
  summary_line: 25 operations · 11 acting · 2 human-in-the-loop
api_count: 9
apis:
- description: The Storm Topology API provides Java and other language bindings for building real-time processing topologies composed of spouts (data sources) and bolts (processing units). It supports various stream
  name: Apache Storm Topology API
  slug: apache-storm-topology-api
- description: The Cluster API from Apache Storm — 2 operation(s) for cluster.
  name: Apache Storm Cluster API
  slug: apache-storm-cluster-api
- description: The Drpc API from Apache Storm — 2 operation(s) for drpc.
  name: Apache Storm Drpc API
  slug: apache-storm-drpc-api
- description: The History API from Apache Storm — 1 operation(s) for history.
  name: Apache Storm History API
  slug: apache-storm-history-api
- description: The Nimbus API from Apache Storm — 1 operation(s) for nimbus.
  name: Apache Storm Nimbus API
  slug: apache-storm-nimbus-api
- description: The Owner Resources API from Apache Storm — 1 operation(s) for owner resources.
  name: Apache Storm Owner Resources API
  slug: apache-storm-owner-resources-api
- description: The Supervisor API from Apache Storm — 2 operation(s) for supervisor.
  name: Apache Storm Supervisor API
  slug: apache-storm-supervisor-api
- description: The Topology API from Apache Storm — 14 operation(s) for topology.
  name: Apache Storm Topology API
  slug: apache-storm-topology-api
- description: The Topology Workers API from Apache Storm — 1 operation(s) for topology workers.
  name: Apache Storm Topology Workers API
  slug: apache-storm-topology-workers-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Storm UI REST Cluster API
  slug: open-apache-storm-cluster-api
- collection_type: open
  name: Apache Storm UI REST Cluster Drpc API
  slug: open-apache-storm-drpc-api
- collection_type: open
  name: Apache Storm UI REST Cluster History API
  slug: open-apache-storm-history-api
- collection_type: open
  name: Apache Storm UI REST Cluster Nimbus API
  slug: open-apache-storm-nimbus-api
- collection_type: open
  name: Apache Storm UI REST Cluster Owner Resources API
  slug: open-apache-storm-owner-resources-api
- collection_type: open
  name: Apache Storm UI REST Cluster Supervisor API
  slug: open-apache-storm-supervisor-api
- collection_type: open
  name: Apache Storm UI REST Cluster Topology API
  slug: open-apache-storm-topology-api
- collection_type: open
  name: Apache Storm UI REST Cluster Topology Workers API
  slug: open-apache-storm-topology-workers-api
- collection_type: open
  name: Apache Storm UI REST API
  slug: open-apache-storm
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/storm/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/storm/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/storm/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-storm-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-storm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-storm-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/storm
- group: docs
  title: ''
  type: Documentation
  url: https://storm.apache.org/documentation/Home.html
- group: start
  title: ''
  type: Portal
  url: https://storm.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://storm.apache.org/releases/current/Setting-up-development-environment.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/apache/storm/releases
- group: operate
  title: ''
  type: Support
  url: https://storm.apache.org/contribute/People.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: company
  title: ''
  type: Blog
  url: https://storm.apache.org/index.html
created: '2026-03-16'
description: Apache Storm is a free and open-source distributed real-time computation system that makes it easy to reliably process unbounded streams of data at scale. It provides a simple programming model (topologies with spouts and bolts), guaranteed message processing, horizontal scalability, and fault tolerance. Storm integrates with queuing and database technologies including Apache Kafka and Apache Cassandra and is governed by the Apache Software Foundation.
features:
- description: At-least-once processing guarantees through ack/fail tracking mechanism.
  name: Guaranteed Message Processing
- description: Horizontally scalable stream processing topologies with configurable parallelism.
  name: Scalable Topologies
- description: High-level micro-batch processing abstraction with stateful streaming and exactly-once semantics.
  name: Trident API
- description: Distributed Remote Procedure Calls for synchronous distributed computation.
  name: DRPC
- description: Tumbling and sliding window processing over bounded time or count windows.
  name: Windowing Operations
- description: Topology components written in Java, Python, Ruby, and other languages via Multilang protocol.
  name: Multi-Language Support
finops:
- name: Apache Storm Finops
  service_category: API
  slug: apache-storm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-storm.png
integrations:
- description: Kafka Spout for consuming messages from Kafka topics as Storm data sources.
  name: Apache Kafka
- description: CassandraBolt for writing processed stream data to Cassandra.
  name: Apache Cassandra
- description: HiveBolt for streaming inserts into Apache Hive tables.
  name: Apache Hive
- description: Redis integration for stateful lookups and caching in Storm bolts.
  name: Redis
- description: ElasticsearchBolt for indexing stream data into Elasticsearch.
  name: Elasticsearch
layout: provider
modified: '2026-05-19'
name: Apache Storm
nav: Providers
network: true
overview: 'Apache Storm publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Topology API, Cluster API, Drpc API, and 6 more. Tagged areas include Distributed Computing, Event Processing, Real-Time, Stream Processing, and Open-Source.


  Apache Storm''s developer surface includes documentation, developer portal, getting-started guide, release notes, support, engineering blog, and 9 more developer resources.'
plans:
- name: Apache Storm Plans Pricing
  plan_count: 3
  slug: apache-storm-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Apache Storm Rate Limits
  slug: apache-storm-rate-limits
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 4.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 34.7
    developer_ergonomics: 45.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 75.0
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-storm/refs/heads/main/screenshots/apache-storm-2026-06-20T172147.png
security:
- kind: domain-security
  name: Apache Storm Domain Security
  slug: apache-storm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Storm Vulnerability Disclosure
  slug: apache-storm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-storm
tags:
- Distributed Computing
- Event Processing
- Real-Time
- Stream Processing
- Open-Source
use_cases:
- description: Continuous computation over live event streams for operational dashboards.
  name: Real-Time Analytics
- description: Real-time data transformation and enrichment pipelines.
  name: ETL Processing
- description: Online scoring of ML models against streaming feature data.
  name: Machine Learning Scoring
- description: Low-latency fraud detection rules applied to transaction streams.
  name: Fraud Detection
website: https://storm.apache.org/
---
