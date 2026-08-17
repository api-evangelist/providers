---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Triplit Agentic Access
  operation_count: 18
  slug: triplit-agentic-access
  summary_line: 18 operations · 16 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: RESTful HTTP API for interacting with a Triplit sync server, supporting fetch, insert, bulk-insert, update, delete, delete-all, and healthcheck operations. Authenticated via JWT Bearer tokens (Service
  name: Triplit HTTP API
  slug: http-api
- description: 'TypeScript/JavaScript client library for interacting with Triplit databases locally and remotely. Provides query subscriptions, optimistic updates, offline support, and real-time sync via WebSockets. '
  name: Triplit Client SDK
  slug: client-sdk
- description: Command-line interface tool for scaffolding Triplit projects, running the local full-stack development environment, managing schemas and migrations, and deploying to Triplit Cloud. Installable via npm
  name: Triplit CLI
  slug: cli
- description: Low-level replication and change management endpoints
  name: Triplit Advanced API
  slug: triplit-advanced-api
- description: Authentication and token management
  name: Triplit Auth API
  slug: triplit-auth-api
- description: CRUD operations on collection entities
  name: Triplit Data API
  slug: triplit-data-api
- description: Database schema management
  name: Triplit Schema API
  slug: triplit-schema-api
- description: Server health, version, and administrative endpoints
  name: Triplit System API
  slug: triplit-system-api
- description: Webhook configuration management
  name: Triplit Webhooks API
  slug: triplit-webhooks-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Triplit HTTP Advanced API
  slug: open-triplit-advanced-api
- collection_type: open
  name: Triplit HTTP Advanced Auth API
  slug: open-triplit-auth-api
- collection_type: open
  name: Triplit HTTP Advanced Data API
  slug: open-triplit-data-api
- collection_type: open
  name: Triplit HTTP Advanced Schema API
  slug: open-triplit-schema-api
- collection_type: open
  name: Triplit HTTP Advanced System API
  slug: open-triplit-system-api
- collection_type: open
  name: Triplit HTTP Advanced Webhooks API
  slug: open-triplit-webhooks-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/aspen-cloud/triplit/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/triplit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/triplit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/triplit-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.triplit.dev
- group: docs
  title: ''
  type: Documentation
  url: https://www.triplit.dev/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aspen-cloud
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/aspen-cloud/triplit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/triplitdev
- group: company
  title: ''
  type: Blog
  url: https://www.triplit.dev/blog
- group: other
  title: ''
  type: X
  url: https://x.com/triplit_dev
- group: commercial
  title: ''
  type: Plans
  url: plans/triplit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/triplit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/triplit-finops.yml
created: '2026-06-12'
description: Triplit is an open-source full-stack database that syncs data between server and browser in real-time, combining a client-side store with a server sync engine and schema-defined collections. It offers a TypeScript-first SDK for building real-time, collaborative, and offline-capable web applications, supporting frameworks like React, Svelte, Vue, Solid, Angular, and Vue. Triplit provides an HTTP REST API and WebSocket-based sync protocol secured with JWT authentication, along with a CLI for scaffolding and managing projects. Developers can self-host Triplit on their own infrastructure or deploy via Triplit Cloud.
examples:
- key_count: 3
  name: Triplit Bulk Insert Example
  slug: triplit-bulk-insert-example
- key_count: 3
  name: Triplit Delete Example
  slug: triplit-delete-example
- key_count: 3
  name: Triplit Fetch Example
  slug: triplit-fetch-example
- key_count: 3
  name: Triplit Insert Example
  slug: triplit-insert-example
- key_count: 3
  name: Triplit Update Example
  slug: triplit-update-example
finops:
- name: Triplit Finops
  service_category: Database
  slug: triplit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/triplit.png
json_schemas:
- name: Triplit Collection Query
  property_count: 6
  slug: triplit-collection-query
- name: Triplit Entity
  property_count: 1
  slug: triplit-entity
- name: Triplit Error Response
  property_count: 3
  slug: triplit-error
- name: Triplit Schema Response
  property_count: 2
  slug: triplit-schema-response
jsonld:
- class_count: 9
  name: Triplit Context
  property_count: 23
  slug: triplit-context
layout: provider
modified: '2026-06-12'
name: Triplit
nav: Providers
network: true
overview: 'Triplit publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Advanced API, Auth API, Data API, and 3 more. Tagged areas include Database, Real-time, Sync, Local-first, and Developer Tools.


  The Triplit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Triplit''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Triplit Plans Pricing
  plan_count: 1
  slug: triplit-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 2
  name: Triplit Rate Limits
  slug: triplit-rate-limits
rules:
- name: Triplit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: triplit-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 68.3
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Triplit Authentication
  slug: triplit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Triplit Domain Security
  slug: triplit-domain-security
  summary_line: no transport/DNS hardening detected
slug: triplit
tags:
- Database
- Real-time
- Sync
- Local-first
- Developer Tools
- TypeScript
- Open Source
website: https://www.triplit.dev
---
