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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-07-28'
api_count: 10
apis:
- description: Redpanda implements the Apache Kafka wire protocol natively, allowing existing Kafka clients (producers, consumers, AdminClient, Streams, Connect) to work unchanged against Redpanda brokers on TCP por
  name: Redpanda Kafka API
  slug: redpanda-kafka-api
- description: The Redpanda Admin API is a built-in HTTP REST API (default port 9644) exposing cluster operations not covered by the Kafka protocol — broker membership, decommissioning, rebalance, license, debug bun
  name: Redpanda Admin API
  slug: redpanda-admin-api
- description: The Redpanda Schema Registry API is a Confluent-Schema-Registry-compatible REST API for managing Avro, JSON Schema, and Protobuf schema versions and subjects bound to topic events.
  name: Redpanda Schema Registry API
  slug: redpanda-schema-registry-api
- description: The Redpanda HTTP Proxy (Pandaproxy) provides a REST API for producing and consuming topic data without a Kafka client library, useful for environments where embedding a Kafka driver is impractical.
  name: Redpanda HTTP Proxy (Pandaproxy) API
  slug: redpanda-http-proxy-api
- description: The Redpanda Cloud Control Plane API manages organization-wide resources — clusters, networks, resource groups, users, and serverless namespaces — across the Redpanda Cloud (Serverless, Dedicated, BYO
  name: Redpanda Cloud Control Plane API
  slug: redpanda-cloud-control-plane-api
- description: The Redpanda Cloud Data Plane API manages in-cluster resources — topics, ACLs, RBAC, users, schema registry, and connectors — for an individual Redpanda Cloud cluster.
  name: Redpanda Cloud Data Plane API
  slug: redpanda-cloud-data-plane-api
- description: The Redpanda Console API powers the Redpanda Console UI (open-source) — topics, consumer groups, broker view, schema registry browsing, and ACL management — and can be called directly to embed Console
  name: Redpanda Console API
  slug: redpanda-console-api
- description: Redpanda Connect (formerly Benthos) is a declarative stream-processor exposing an HTTP API for managing pipelines, inputs, outputs, processors, and metrics — bridging Kafka, S3, databases, and HTTP si
  name: Redpanda Connect (Benthos) API
  slug: redpanda-connect-api
- description: rpk is the Redpanda command-line tool, wrapping the Kafka, Admin, Schema Registry, and Cloud APIs into operator-friendly commands for deployment, configuration, topic management, ACLs, and benchmarkin
  name: Redpanda rpk CLI Surface
  slug: redpanda-rpk-api
- description: Redpanda Iceberg Topics expose topic data as Apache Iceberg tables in object storage, accessible from the Iceberg REST catalog and consumable by query engines like Spark, Trino, and Snowflake.
  name: Redpanda Iceberg Topic API
  slug: redpanda-iceberg-topic-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-redpanda-admin-broker
- collection_type: open
  name: API Collection
  slug: open-redpanda-admin-cluster
- collection_type: open
  name: API Collection
  slug: open-redpanda-admin-debug
- collection_type: open
  name: API Collection
  slug: open-redpanda-admin-partition
- collection_type: open
  name: API Collection
  slug: open-redpanda-admin-transform
- collection_type: open
  name: API Collection
  slug: open-redpanda-admin-usage
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/redpanda-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/redpanda-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redpanda-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/redpanda-data
- group: company
  title: ''
  type: Website
  url: https://redpanda.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.redpanda.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.redpanda.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.redpanda.com/current/get-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.redpanda.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://cloud.redpanda.com/signup
- group: start
  title: ''
  type: Login
  url: https://cloud.redpanda.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/redpanda-data
- group: other
  title: ''
  type: Source
  url: https://github.com/redpanda-data/redpanda
- group: commercial
  title: ''
  type: License
  url: https://github.com/redpanda-data/redpanda/blob/dev/licenses/bsl.md
- group: other
  title: ''
  type: Helm Charts
  url: https://github.com/redpanda-data/helm-charts
- group: start
  title: ''
  type: Console
  url: https://github.com/redpanda-data/console
- group: other
  title: ''
  type: Connect
  url: https://github.com/redpanda-data/connect
- group: other
  title: ''
  type: Operator
  url: https://github.com/redpanda-data/redpanda-operator
- group: build
  title: ''
  type: Examples
  url: https://github.com/redpanda-data/redpanda-examples
- group: operate
  title: ''
  type: StatusPage
  url: https://status.redpanda.com/
- group: company
  title: ''
  type: Blog
  url: https://www.redpanda.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.redpanda.com/current/release-notes/
- group: other
  title: ''
  type: Governance
  url: https://www.redpanda.com/about
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/redpandadata
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@RedpandaData
- group: operate
  title: ''
  type: Slack Community
  url: https://redpandacommunity.slack.com/
- group: build
  title: ''
  type: rpk CLI
  url: https://docs.redpanda.com/current/reference/rpk/
- group: commercial
  title: ''
  type: Plans
  url: plans/redpanda-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/redpanda-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/redpanda-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://www.redpanda.com/blog/building-low-code-mcp-servers-in-redpanda-cloud
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.redpanda.com/llms.txt
created: '2026-05-08'
description: Redpanda is a Kafka API-compatible streaming data platform written in C++ with no JVM and no ZooKeeper, optimized for low latency and operational simplicity. The core broker (redpanda) is open source and available under the Business Source License 1.1, and a fully managed cloud service (Redpanda Cloud — Serverless, Dedicated, BYOC) is offered commercially. Redpanda Connect (formerly Benthos) provides stream processing. The platform exposes the Kafka wire protocol, an Admin API, a Schema Registry API, an HTTP Proxy (Pandaproxy), Kafka-compatible client APIs, and the Redpanda Cloud Control Plane and Data Plane APIs for managed deployments.
finops:
- name: Redpanda Finops
  service_category: Streaming
  slug: redpanda-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/redpanda.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Redpanda
nav: Providers
network: true
overview: 'Redpanda publishes 1 API on the [APIs.io](https://apis.io/) network: Admin API. Tagged areas include Streaming, Kafka, Event Streaming, Real-Time, and Data Platform.


  Redpanda''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, developer console, code examples, and 25 more developer resources.'
plans:
- name: Redpanda Plans Pricing
  plan_count: 5
  slug: redpanda-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 6
  name: Redpanda Rate Limits
  slug: redpanda-rate-limits
score:
  band: developing
  composite: 45.4
  delta: -3.3
  facets:
    commercial_clarity: 71.1
    contract_quality: 32.3
    developer_ergonomics: 43.5
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 48.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/redpanda/refs/heads/main/screenshots/redpanda-2026-06-20T192835.png
security:
- kind: domain-security
  name: Redpanda Domain Security
  slug: redpanda-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Redpanda Vulnerability Disclosure
  slug: redpanda-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Redpanda Trust Center
  slug: redpanda-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: redpanda
tags:
- Streaming
- Kafka
- Event Streaming
- Real-Time
- Data Platform
- Open Source
- C++
- Stream Processing
website: https://redpanda.com/
---
