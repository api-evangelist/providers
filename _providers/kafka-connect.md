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
    asyncapi_events: false
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 3
  name: Kafka Connect Agentic Access
  operation_count: 22
  slug: kafka-connect-agentic-access
  summary_line: 22 operations · 12 acting · 3 human-in-the-loop
api_count: 3
apis:
- description: The Connector Plugins API from Kafka Connect — 2 operation(s) for connector plugins.
  name: Kafka Connect Connector Plugins API
  slug: kafka-connect-connector-plugins-api
- description: The Connectors API from Kafka Connect — 14 operation(s) for connectors.
  name: Kafka Connect Connectors API
  slug: kafka-connect-connectors-api
- description: The Kafka Connect REST API API from Kafka Connect — 1 operation(s) for kafka connect rest api.
  name: Kafka Connect Kafka Connect REST API API
  slug: kafka-connect-kafka-connect-rest-api-api
artifact_total: 10
collections:
- collection_type: open
  name: Kafka Connect REST API
  slug: open-kafka-connect
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kafka-connect-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kafka-connect-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kafka-connect-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apachekafka
- group: company
  title: ''
  type: Website
  url: https://kafka.apache.org/documentation/#connect
- group: docs
  title: ''
  type: Documentation
  url: https://kafka.apache.org/documentation/#connect
- group: start
  title: ''
  type: GettingStarted
  url: https://kafka.apache.org/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/kafka
- group: company
  title: ''
  type: Blog
  url: https://kafka.apache.org/blog
created: '2024-01-01'
description: Kafka Connect is a tool for scalably and reliably streaming data between Apache Kafka and other systems. It makes it simple to quickly define connectors that move large collections of data into and out of Kafka.
finops:
- name: Kafka Connect Finops
  service_category: API
  slug: kafka-connect-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kafka-connect.png
layout: provider
modified: '2026-05-30'
name: Kafka Connect
nav: Providers
network: true
overview: 'Kafka Connect publishes 3 APIs on the [APIs.io](https://apis.io/) network: Connector Plugins API, Connectors API, and Kafka Connect REST API API. Tagged areas include Apache Kafka, Connectors, Data Integration, ETL, and Streaming.


  Kafka Connect''s developer surface includes documentation, getting-started guide, engineering blog, and 6 more developer resources.'
plans:
- name: Kafka Connect Plans Pricing
  plan_count: 3
  slug: kafka-connect-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 5
  name: Kafka Connect Rate Limits
  slug: kafka-connect-rate-limits
score:
  band: thin
  composite: 32.8
  delta: -2.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 37.3
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kafka-connect/refs/heads/main/screenshots/kafka-connect-2026-06-20T183852.png
security:
- kind: domain-security
  name: Kafka Connect Domain Security
  slug: kafka-connect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kafka Connect Vulnerability Disclosure
  slug: kafka-connect-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kafka-connect
tags:
- Apache Kafka
- Connectors
- Data Integration
- ETL
- Streaming
website: https://kafka.apache.org/documentation/#connect
---
