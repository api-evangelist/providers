---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Risingwave Agentic Access
  operation_count: 3
  slug: risingwave-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 6
apis:
- description: PostgreSQL-compatible SQL interface for ingesting streaming data, defining materialized views, running analytical queries, and managing streaming jobs. Accessible via psql, JDBC, and any PostgreSQL-co
  name: RisingWave SQL API
  slug: sql-api
- description: Model Context Protocol server that connects AI agents to running RisingWave instances, exposing over 100 tools for querying, schema inspection, DDL operations, streaming job monitoring, and cluster ma
  name: RisingWave MCP Server
  slug: mcp-server
- description: 'The RisingWave Cloud CLI (rwc) provides infrastructure management for RisingWave Cloud, including cluster provisioning, authentication, snapshots, and agent skill installation. Supports install of AI '
  name: RisingWave Cloud CLI
  slug: cloud-api
- description: The Events API from RisingWave — 1 operation(s) for events.
  name: RisingWave Events API
  slug: risingwave-events-api
- description: The Healthz API from RisingWave — 1 operation(s) for healthz.
  name: RisingWave Healthz API
  slug: risingwave-healthz-api
- description: The Sql API from RisingWave — 1 operation(s) for sql.
  name: RisingWave Sql API
  slug: risingwave-sql-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RisingWave Events API
  slug: open-risingwave-events-api
- collection_type: open
  name: RisingWave Events Healthz API
  slug: open-risingwave-healthz-api
- collection_type: open
  name: RisingWave Events Sql API
  slug: open-risingwave-sql-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/risingwave-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/risingwave-domain-security.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/risingwavelabs/agent-skills
- group: company
  title: ''
  type: Website
  url: https://risingwave.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.risingwave.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/risingwavelabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/risingwave
- group: other
  title: ''
  type: X
  url: https://x.com/RisingWaveLabs
- group: company
  title: ''
  type: Blog
  url: https://risingwave.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://risingwave.com/pricing/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.risingwave.com/changelog/release-notes
- group: operate
  title: ''
  type: Slack
  url: https://go.risingwave.com/slack
- group: commercial
  title: ''
  type: Plans
  url: plans/risingwave-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/risingwave-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/risingwave-finops.yml
created: '2026-06-12'
description: RisingWave is a distributed SQL streaming platform that continuously ingests event streams from Kafka, Kinesis, and other sources, transforms them using PostgreSQL-compatible SQL, and serves low-latency results through incrementally maintained materialized views. It delivers sub-100ms freshness for operational workloads and supports streaming analytics via Apache Iceberg integration with exactly-once semantics. The platform offers a decoupled compute and storage architecture for cost efficiency, with transparent dynamic scaling and instant failure recovery. RisingWave is available as open-source (Apache 2.0), as a managed cloud service (RisingWave Cloud) on AWS, GCP, and Azure, and as a self-managed deployment on Kubernetes.
examples:
- key_count: 3
  name: Risingwave Execute Sql Example
  slug: risingwave-execute-sql-example
- key_count: 3
  name: Risingwave Ingest Event Example
  slug: risingwave-ingest-event-example
finops:
- name: Risingwave Finops
  service_category: Database
  slug: risingwave-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/risingwave.png
json_schemas:
- name: QueryResponse
  property_count: 4
  slug: risingwave-query-response
jsonld:
- class_count: 19
  name: Risingwave Context
  property_count: 5
  slug: risingwave-context
layout: provider
modified: '2026-06-12'
name: RisingWave
nav: Providers
network: true
overview: 'RisingWave publishes 3 APIs on the [APIs.io](https://apis.io/) network: Events API, Healthz API, and Sql API. Tagged areas include Streaming, SQL, Database, Real-Time, and Kafka.


  The RisingWave catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RisingWave''s developer surface includes documentation, engineering blog, pricing, changelog, and 11 more developer resources.'
plans:
- name: Risingwave Plans Pricing
  plan_count: 4
  slug: risingwave-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 3
  name: Risingwave Rate Limits
  slug: risingwave-rate-limits
rules:
- name: RisingWave API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: risingwave-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 59.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/risingwave/refs/heads/main/screenshots/risingwave-2026-06-20T193128.png
security:
- kind: domain-security
  name: Risingwave Domain Security
  slug: risingwave-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: risingwave-best-practices
  slug: risingwave-best-practices
- name: risingwave
  slug: risingwave
slug: risingwave
tags:
- Streaming
- SQL
- Database
- Real-Time
- Kafka
- Materialized Views
- PostgreSQL
- Apache Iceberg
website: https://risingwave.com/
---
