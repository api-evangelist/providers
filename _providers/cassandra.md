---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Cassandra Agentic Access
  operation_count: 26
  slug: cassandra-agentic-access
  summary_line: 26 operations · 15 acting
api_count: 12
apis:
- description: Cassandra Query Language (CQL) is the primary interface to Apache Cassandra. Clients speak the binary CQL native protocol over TCP (default port 9042). Official drivers are maintained for Java, Python
  name: Apache Cassandra CQL Native Protocol
  slug: cassandra-cql-native-protocol
- description: HTTP/JSON REST API for Cassandra provided by the Stargate data gateway. Enables CRUD operations and SQL-like query via REST without the CQL driver.
  name: Cassandra REST API (Stargate)
  slug: cassandra-rest-api-stargate
- description: GraphQL endpoint for Cassandra, enabling flexible, typed queries and mutations against Cassandra tables through the Stargate gateway.
  name: Cassandra GraphQL API (Stargate)
  slug: cassandra-graphql-api-stargate
- description: Schemaless Document API that stores JSON documents in Cassandra, offering a MongoDB-like developer experience backed by Cassandra.
  name: Cassandra Document API (Stargate)
  slug: cassandra-document-api-stargate
- description: High-performance gRPC API for Cassandra through Stargate, designed for low-latency service-to-service communication.
  name: Cassandra gRPC API (Stargate)
  slug: cassandra-grpc-api-stargate
- description: Java Management Extensions (JMX) interface for monitoring and administering Cassandra nodes, including metrics, compaction, repairs, and configuration.
  name: Cassandra JMX Management Interface
  slug: cassandra-jmx-metrics
- description: The Columns API from Apache Cassandra — 2 operation(s) for columns.
  name: Apache Cassandra Columns API
  slug: cassandra-columns-api
- description: The Indexes API from Apache Cassandra — 2 operation(s) for indexes.
  name: Apache Cassandra Indexes API
  slug: cassandra-indexes-api
- description: The Keyspaces API from Apache Cassandra — 2 operation(s) for keyspaces.
  name: Apache Cassandra Keyspaces API
  slug: cassandra-keyspaces-api
- description: The Rows API from Apache Cassandra — 3 operation(s) for rows.
  name: Apache Cassandra Rows API
  slug: cassandra-rows-api
- description: The Tables API from Apache Cassandra — 2 operation(s) for tables.
  name: Apache Cassandra Tables API
  slug: cassandra-tables-api
- description: The Types API from Apache Cassandra — 2 operation(s) for types.
  name: Apache Cassandra Types API
  slug: cassandra-types-api
artifact_total: 54
collections:
- collection_type: open
  name: Apache Cassandra REST API (via Stargate)
  slug: open-cassandra
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cassandra-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cassandra-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cassandra-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cassandra-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://cassandra.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://cassandra.apache.org/doc/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://cassandra.apache.org/doc/latest/cassandra/getting_started/
- group: other
  title: ''
  type: Download
  url: https://cassandra.apache.org/download/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/apache/cassandra
- group: build
  title: ''
  type: GitHub
  url: https://github.com/apache/cassandra
- group: operate
  title: ''
  type: IssueTracker
  url: https://issues.apache.org/jira/projects/CASSANDRA
- group: company
  title: ''
  type: Blog
  url: https://cassandra.apache.org/blog/
- group: operate
  title: ''
  type: Community
  url: https://cassandra.apache.org/community/
- group: other
  title: ''
  type: MailingList
  url: https://cassandra.apache.org/community/#discussions
- group: operate
  title: ''
  type: Slack
  url: https://cassandra.apache.org/community/#slack
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/cassandra
- group: other
  title: ''
  type: X
  url: https://twitter.com/cassandra
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apache-cassandra/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@PlanetCassandra
- group: other
  title: ''
  type: DockerHub
  url: https://hub.docker.com/_/cassandra
- group: start
  title: ''
  type: PackageRegistry
  url: https://central.sonatype.com/artifact/org.apache.cassandra/cassandra-all
- group: commercial
  title: ''
  type: License
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: other
  title: ''
  type: Governance
  url: https://www.apache.org/foundation/governance/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://cassandra.apache.org/_/security.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apache.org/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/foundation/license-faq.html
- group: other
  title: ''
  type: Ecosystem
  url: https://cassandra.apache.org/_/ecosystem.html
- group: other
  title: ''
  type: ThirdParty
  url: https://cassandra.apache.org/_/ecosystem.html
created: '2024-01-01'
description: Apache Cassandra is a highly scalable, distributed open-source NoSQL database designed to handle massive amounts of data across many commodity servers, providing high availability with no single point of failure. It is governed by the Apache Software Foundation (ASF) under the Apache License 2.0 and is used in production by Netflix, Apple, Bloomberg, Backblaze, and many others. Cassandra exposes its CQL native protocol for clients and a family of HTTP, REST, GraphQL, Document, and gRPC APIs via the Stargate data gateway.
features:
- name: Distributed
- name: Masterless
- name: Linear Scalability
- name: Multi-Datacenter Replication
- name: High Availability
- name: Fault Tolerance
- name: Tunable Consistency
- name: CQL Query Language
- name: Secondary Indexes
- name: Materialized Views
- name: User Defined Types
- name: User Defined Functions
- name: Vector Search
- name: Time Series Storage
- name: Cross-Region Replication
- name: Role Based Access Control
- name: TLS/SSL Encryption
- name: At-Rest Encryption
- name: Snapshot Backups
- name: Incremental Repairs
- name: Apache License 2.0
finops:
- name: Cassandra Finops
  service_category: API
  slug: cassandra-finops
graphqls:
- description: GraphQL endpoint for Cassandra, enabling flexible, typed queries and mutations against Cassandra tables through the Stargate gateway.
  name: Apache Cassandra GraphQL API
  slug: cassandra-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cassandra.png
layout: provider
modified: '2026-04-23'
name: Apache Cassandra
nav: Providers
network: true
overview: 'Apache Cassandra publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Cassandra REST API (Stargate), Columns API, Indexes API, and 4 more. Tagged areas include Apache, Big Data, Database, Distributed, and NoSQL.


  Apache Cassandra''s developer surface includes authentication, documentation, getting-started guide, GitHub presence, engineering blog, Stack Overflow tag, YouTube channel, and 21 more developer resources.'
plans:
- name: Cassandra Plans Pricing
  plan_count: 3
  slug: cassandra-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: Cassandra Rate Limits
  slug: cassandra-rate-limits
score:
  band: developing
  composite: 44.4
  delta: -2.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 49.2
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cassandra/refs/heads/main/screenshots/cassandra-2026-06-20T174035.png
security:
- kind: authentication
  name: Cassandra Authentication
  slug: cassandra-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cassandra Domain Security
  slug: cassandra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cassandra Vulnerability Disclosure
  slug: cassandra-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cassandra
tags:
- Apache
- Big Data
- Database
- Distributed
- NoSQL
- Open Source
use_cases:
- name: Event Logging
- name: IoT Telemetry
- name: Time Series Data
- name: Product Catalogs
- name: Messaging Platforms
- name: Fraud Detection
- name: Recommendation Engines
- name: Activity Feeds
- name: Audit Logs
- name: Real-Time Analytics
- name: Mobile Application Backends
- name: Vector Similarity Search
website: https://cassandra.apache.org/
---
