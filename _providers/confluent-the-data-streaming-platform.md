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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
  score: 35.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Confluent The Data Streaming Platform Agentic Access
  operation_count: 19
  slug: confluent-the-data-streaming-platform-agentic-access
  summary_line: 19 operations · 9 acting
api_count: 11
apis:
- description: The Confluent Cloud REST API is the management plane for Confluent Cloud. It is used to manage organizations, environments, Kafka and Flink clusters, service accounts, API keys, role bindings, network
  name: Confluent Cloud REST API
  slug: cloud-rest-api
- description: The Kafka REST API (Confluent REST Proxy in self-managed deployments, Kafka REST in Cloud) provides HTTP access to Apache Kafka topics, consumers, partitions, brokers, and ACLs. Clients without a nati
  name: Confluent Kafka REST API
  slug: kafka-rest-api
- description: The Schema Registry REST API stores and serves Avro, JSON Schema, and Protobuf schemas with versioning and compatibility enforcement. It is available both as a managed Confluent Cloud service and as a
  name: Confluent Schema Registry REST API
  slug: schema-registry-api
- description: The Kafka Connect REST API manages connectors, tasks, and worker configuration. Operators use it to deploy, configure, pause, resume, and delete source and sink connectors, inspect task status, and re
  name: Kafka Connect REST API
  slug: connect-rest-api
- description: The ksqlDB REST API exposes ksqlDB, Confluent's streaming SQL engine, over HTTP. Clients submit streaming SQL statements, query streams and tables (push and pull queries), and inspect server status.
  name: ksqlDB REST API
  slug: ksqldb-rest-api
- description: The Confluent Cloud for Apache Flink REST API manages Flink compute pools, statements, and workspaces for stateful stream processing on Confluent Cloud. It is part of the Confluent Cloud REST surface.
  name: Confluent Cloud for Apache Flink REST API
  slug: flink-rest-api
- description: The API Keys API from Confluent | the Data Streaming Platform — 2 operation(s) for api keys.
  name: Confluent | the Data Streaming Platform API Keys API
  slug: confluent-the-data-streaming-platform-api-keys-api
- description: The Clusters API from Confluent | the Data Streaming Platform — 2 operation(s) for clusters.
  name: Confluent | the Data Streaming Platform Clusters API
  slug: confluent-the-data-streaming-platform-clusters-api
- description: The Environments API from Confluent | the Data Streaming Platform — 2 operation(s) for environments.
  name: Confluent | the Data Streaming Platform Environments API
  slug: confluent-the-data-streaming-platform-environments-api
- description: The Organizations API from Confluent | the Data Streaming Platform — 2 operation(s) for organizations.
  name: Confluent | the Data Streaming Platform Organizations API
  slug: confluent-the-data-streaming-platform-organizations-api
- description: The Service Accounts API from Confluent | the Data Streaming Platform — 2 operation(s) for service accounts.
  name: Confluent | the Data Streaming Platform Service Accounts API
  slug: confluent-the-data-streaming-platform-service-accounts-api
artifact_total: 31
collections:
- collection_type: open
  name: Confluent Cloud REST API (selected)
  slug: open-confluent-the-data-streaming-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/confluent-the-data-streaming-platform-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/confluent-the-data-streaming-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/confluent-the-data-streaming-platform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/confluent-the-data-streaming-platform-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/confluentinc/agent-skills
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/confluent
- group: company
  title: ''
  type: Website
  url: https://www.confluent.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.confluent.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.confluent.io/
- group: docs
  title: ''
  type: Cloud API Reference
  url: https://docs.confluent.io/cloud/current/api.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/confluentinc
- group: company
  title: ''
  type: Blog
  url: https://www.confluent.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.confluent.io/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.confluent.cloud/
- group: start
  title: ''
  type: Login
  url: https://confluent.cloud/login
- group: other
  title: ''
  type: Marketplace
  url: https://www.confluent.io/hub/
- group: learn
  title: ''
  type: Training
  url: https://training.confluent.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.confluent.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.confluent.io/privacy-policy/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.confluent.io/llms.txt
created: '2025-08-19'
description: Confluent is a fully managed data streaming platform built by the original creators of Apache Kafka. It lets organizations stream, connect, process, and govern data in motion through a cloud-native service (Confluent Cloud) and the on-prem/self-managed Confluent Platform. Confluent's developer surface includes the Confluent Cloud REST API for managing clusters, environments, and access; the Kafka REST Proxy for producing and consuming events over HTTP; the Schema Registry REST API for governance of Avro, JSON Schema, and Protobuf schemas; the Kafka Connect REST API for managing connectors; the ksqlDB REST API for stream processing; and managed Apache Flink. Authentication is API-key based (Cloud) or HTTP/mTLS/OAuth (Platform).
finops:
- name: Confluent The Data Streaming Platform Finops
  service_category: API
  slug: confluent-the-data-streaming-platform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/confluent-the-data-streaming-platform.png
layout: provider
modified: '2026-04-28'
name: Confluent | the Data Streaming Platform
nav: Providers
network: true
overview: 'Confluent | the Data Streaming Platform publishes 5 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Clusters API, Environments API, and 2 more. Tagged areas include Apache Flink, Apache Kafka, Confluent Cloud, Connectors, and Data Streaming.


  Confluent | the Data Streaming Platform''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, training material, and 14 more developer resources.'
plans:
- name: Confluent The Data Streaming Platform Plans Pricing
  plan_count: 3
  slug: confluent-the-data-streaming-platform-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Confluent The Data Streaming Platform Rate Limits
  slug: confluent-the-data-streaming-platform-rate-limits
score:
  band: developing
  composite: 48.7
  delta: -2.6
  facets:
    commercial_clarity: 84.2
    contract_quality: 50.0
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 51.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/screenshots/confluent-the-data-streaming-platform-2026-06-20T174902.png
security:
- kind: authentication
  name: Confluent The Data Streaming Platform Authentication
  slug: confluent-the-data-streaming-platform-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Confluent The Data Streaming Platform Domain Security
  slug: confluent-the-data-streaming-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Confluent The Data Streaming Platform Vulnerability Disclosure
  slug: confluent-the-data-streaming-platform-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 12
skills:
- name: Bad_Frontmatter
  slug: bad-frontmatter
- name: confluent-cloud-cdc-tableflow
  slug: confluent-cloud-cdc-tableflow
- name: confluent-skill-creator
  slug: confluent-skill-creator
- name: confluent-skill-reviewer
  slug: confluent-skill-reviewer
- name: developing-kafka-python-client
  slug: developing-kafka-python-client
- name: flink-udf
  slug: flink-udf
- name: good-skill
  slug: good-skill
- name: inlined-refs
  slug: inlined-refs
- name: kafka-schema-registry
  slug: kafka-schema-registry
- name: kafka-streams-programming
  slug: kafka-streams-programming
- name: stale-expectations
  slug: stale-expectations
- name: trigger-overlap
  slug: trigger-overlap
slug: confluent-the-data-streaming-platform
tags:
- Apache Flink
- Apache Kafka
- Confluent Cloud
- Connectors
- Data Streaming
- Event Streaming
- Kafka Connect
- ksqlDB
- Real-Time Data
- REST
- Schema Registry
- Stream Processing
website: https://www.confluent.io/
---
