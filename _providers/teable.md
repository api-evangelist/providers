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
- acting_count: 21
  human_in_the_loop: 0
  name: Teable Agentic Access
  operation_count: 34
  slug: teable-agentic-access
  summary_line: 34 operations · 21 acting
api_count: 7
apis:
- description: File attachments.
  name: Teable Attachment API
  slug: teable-attachment-api
- description: Postgres-backed databases within a space.
  name: Teable Base API
  slug: teable-base-api
- description: Columns within a table.
  name: Teable Field API
  slug: teable-field-api
- description: Rows within a table.
  name: Teable Record API
  slug: teable-record-api
- description: Top-level workspaces.
  name: Teable Space API
  slug: teable-space-api
- description: Spreadsheet-like tables within a base.
  name: Teable Table API
  slug: teable-table-api
- description: Views over a table.
  name: Teable View API
  slug: teable-view-api
artifact_total: 14
collections:
- collection_type: open
  name: Teable API
  slug: open-teable
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/teable-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teable-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/teable-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teableio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teable
- group: company
  title: ''
  type: Website
  url: https://teable.io
- group: docs
  title: ''
  type: Documentation
  url: https://help.teable.ai/en/api-doc/overview
- group: commercial
  title: ''
  type: Plans
  url: plans/teable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/teable-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/teable-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://teable.io/blog
created: '2026-06-20'
description: Teable is an open-source, no-code database platform built on PostgreSQL and positioned as an Airtable alternative. It pairs a spreadsheet-style UI with a documented REST API for managing spaces, bases, tables, fields, records, views, and attachments, scaling to millions of rows while keeping data in a real Postgres database.
finops:
- name: Teable Finops
  service_category: Databases and Productivity
  slug: teable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teable.png
layout: provider
modified: '2026-06-20'
name: Teable
nav: Providers
network: true
overview: 'Teable publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Attachment API, Base API, Field API, and 4 more. Tagged areas include No-Code, Database, Airtable Alternative, Postgres, and Open Source.


  Teable''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Teable Plans Pricing
  plan_count: 5
  slug: teable-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 5
  name: Teable Rate Limits
  slug: teable-rate-limits
score:
  band: thin
  composite: 37.7
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/teable/refs/heads/main/screenshots/teable-2026-06-20T194954.png
security:
- kind: authentication
  name: Teable Authentication
  slug: teable-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Teable Domain Security
  slug: teable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: teable
tags:
- No-Code
- Database
- Airtable Alternative
- Postgres
- Open Source
website: https://teable.io
---
