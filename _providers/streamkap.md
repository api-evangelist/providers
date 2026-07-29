---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
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
  score: 32.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Streamkap Agentic Access
  operation_count: 32
  slug: streamkap-agentic-access
  summary_line: 32 operations · 17 acting
api_count: 9
apis:
- description: Create, configure, deploy, pause, resume, restart, and reset source connectors that capture change data from databases and other systems, plus snapshot control (blocking, incremental, parallel), metri
  name: Streamkap Sources API
  slug: streamkap-sources-api
- description: 'Manage sink destinations - Snowflake, Databricks, BigQuery, ClickHouse, Redshift, S3, Iceberg, and more - including create, update, deploy, lifecycle control, configuration schemas, metrics, and bulk '
  name: Streamkap Destinations API
  slug: streamkap-destinations-api
- description: Create and manage end-to-end pipelines that wire a source to a destination (optionally through transforms), with lifecycle management, per-pipeline metrics and logs, and bulk operations.
  name: Streamkap Pipelines API
  slug: streamkap-pipelines-api
- description: Discover the catalog of available source and destination connector types and their configuration schemas so sources and destinations can be provisioned programmatically against the correct connector d
  name: Streamkap Connectors API
  slug: streamkap-connectors-api
- description: Author, clone, unit-test, preview, and deploy in-stream transforms (SQL, Python, TypeScript) running on Flink, including input/output topic wiring, checkpoints, DLQ errors, and job status.
  name: Streamkap Transforms API
  slug: streamkap-transforms-api
- description: Create, inspect, and manage the underlying Kafka topics - browse messages and message values, read topic metrics, statistics, and Kafka broker metadata, publish records, and drive topic-level snapshot
  name: Streamkap Topics API
  slug: streamkap-topics-api
- description: Create, search, update, and delete tags used to label and group sources, destinations, pipelines, transforms, and topics for organization and bulk operations.
  name: Streamkap Tags API
  slug: streamkap-tags-api
- description: Provision Kafka users and their ACLs for direct broker access, inspect consumer groups and reset their offsets, and browse the Schema Registry subjects and versions backing the streams.
  name: Streamkap Kafka Access API
  slug: streamkap-kafka-access-api
- description: Exchange a client-id and secret (or a project key) for a JWT access token, refresh tokens, manage client credentials and project keys, and inspect the caller's identity, permissions, and roles.
  name: Streamkap Authentication API
  slug: streamkap-authentication-api
artifact_total: 17
collections:
- collection_type: open
  name: Streamkap API
  slug: open-streamkap
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/streamkap-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/streamkap-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/streamkap-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/streamkap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/streamkap-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/streamkap-com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/streamkap
- group: company
  title: ''
  type: Website
  url: https://streamkap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.streamkap.com
- group: commercial
  title: ''
  type: Plans
  url: plans/streamkap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/streamkap-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/streamkap-finops.yml
created: '2026-07-01'
description: Streamkap is a real-time streaming ETL and change data capture (CDC) platform built on Apache Kafka and Apache Flink. It streams data from operational databases (PostgreSQL, MySQL, MongoDB, SQL Server, Oracle) to cloud warehouses, lakes, and other destinations with sub-second latency, and its REST API lets teams provision and operate sources, destinations, pipelines, transforms, and Kafka access programmatically.
finops:
- name: Streamkap Finops
  service_category: Analytics
  slug: streamkap-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-01'
name: Streamkap
nav: Providers
network: true
overview: 'Streamkap publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Sources API, Destinations API, Pipelines API, and 6 more. Tagged areas include Streaming, ETL, CDC, Kafka, and Flink.


  Streamkap''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Streamkap Plans Pricing
  plan_count: 4
  slug: streamkap-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 4
  name: Streamkap Rate Limits
  slug: streamkap-rate-limits
score:
  band: thin
  composite: 35.7
  delta: -4.9
  facets:
    commercial_clarity: 47.4
    contract_quality: 40.3
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Streamkap Authentication
  slug: streamkap-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Streamkap Domain Security
  slug: streamkap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Streamkap Trust Center
  slug: streamkap-trust-center
  summary_line: SOC 2, ISO 27001
slug: streamkap
tags:
- Streaming
- ETL
- CDC
- Kafka
- Flink
- Data Integration
- Real Time
website: https://streamkap.com/
---
