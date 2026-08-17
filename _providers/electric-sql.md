---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
  score: 27.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Electric Sql Agentic Access
  operation_count: 3
  slug: electric-sql-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 3
apis:
- description: 'The official @electric-sql/client NPM package that wraps the HTTP Sync API with two high-level primitives: ShapeStream (low-level message stream) and Shape (materialized view). Supports SSE, long-poll'
  name: Electric TypeScript Client
  slug: typescript-client
- description: 'Environment-variable-driven configuration interface for the Electric sync service (Elixir/Docker). Controls database connectivity, storage backends, concurrent request limits (initial: 300, live: 10 0'
  name: Electric Sync Service Configuration API
  slug: sync-service-config-api
- description: The Shape API from ElectricSQL — 1 operation(s) for shape.
  name: ElectricSQL Shape API
  slug: electric-sql-shape-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Electric HTTP Shape API
  slug: open-electric-sql-shape-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/electric-sql-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/electric-sql-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://electric.ax
- group: docs
  title: ''
  type: Documentation
  url: https://electric.ax/docs/sync/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/electric-sql
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/electric-sql
- group: company
  title: ''
  type: Blog
  url: https://electric.ax/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://electric.ax/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://electric.ax/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/ElectricSQL
- group: operate
  title: ''
  type: Discord
  url: https://discord.electric-sql.com
- group: commercial
  title: ''
  type: Plans
  url: plans/electric-sql-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/electric-sql-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/electric-sql-finops.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/electric-sql-shape-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/electric-sql-subset-snapshot-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/electric-sql-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/electric-sql-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-12'
description: ElectricSQL (Electric) is a local-first sync engine for Postgres that streams live database changes to embedded clients in browsers, apps, and AI agents via an HTTP-based Shape sync protocol. It exposes a low-level HTTP API and TypeScript, Elixir, and other client SDKs that materialize real-time Postgres data into local state with sub-millisecond reactivity. Developers can run Electric self-hosted as a Docker service or use Electric Cloud, a managed offering with pay-as-you-go and subscription plans. The platform also underpins PGlite (an embeddable Postgres under 3 MB) and Durable Streams for reliable agent messaging, making it a broader data-infrastructure toolkit for building collaborative and multi-agent systems.
examples:
- key_count: 3
  name: Electric Sql Delete Shape Example
  slug: electric-sql-delete-shape-example
- key_count: 3
  name: Electric Sql Get Shape Example
  slug: electric-sql-get-shape-example
- key_count: 3
  name: Electric Sql Post Shape Subset Example
  slug: electric-sql-post-shape-subset-example
finops:
- name: Electric Sql Finops
  service_category: Database / Data Synchronization
  slug: electric-sql-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/electric-sql.png
json_schemas:
- name: ShapeMessage
  property_count: 4
  slug: electric-sql-shape-message
- name: SubsetSnapshot
  property_count: 2
  slug: electric-sql-subset-snapshot
jsonld:
- class_count: 4
  name: Electric Sql Context
  property_count: 25
  slug: electric-sql-context
layout: provider
modified: '2026-06-12'
name: ElectricSQL
nav: Providers
network: true
overview: 'ElectricSQL publishes 1 API on the [APIs.io](https://apis.io/) network: Shape API. Tagged areas include Developer Tools, Database, Sync, Local-First, and Postgres.


  The ElectricSQL catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ElectricSQL''s developer surface includes documentation, engineering blog, changelog, pricing, and 15 more developer resources.'
plans:
- name: Electric Sql Plans Pricing
  plan_count: 4
  slug: electric-sql-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 3
  name: Electric Sql Rate Limits
  slug: electric-sql-rate-limits
rules:
- name: ElectricSQL API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: electric-sql-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 54.5
    developer_ergonomics: 15.2
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/electric-sql/refs/heads/main/screenshots/electric-sql-2026-06-20T180546.png
security:
- kind: domain-security
  name: Electric Sql Domain Security
  slug: electric-sql-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: electric-sql
tags:
- Developer Tools
- Database
- Sync
- Local-First
- Postgres
- Real-Time
- Open Source
website: https://electric.ax
---
