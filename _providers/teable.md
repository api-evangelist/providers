---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Teable Agentic Access
  operation_count: 34
  slug: teable-agentic-access
  summary_line: 34 operations · 21 acting
api_count: 1
apis:
- baseURL: https://app.teable.io/api
  baseurl_source: declared
  description: File attachments.
  name: Teable Attachment API
  slug: teable-attachment-api
- baseURL: https://app.teable.io/api
  baseurl_source: declared
  description: Postgres-backed databases within a space.
  name: Teable Base API
  slug: teable-base-api
- baseURL: https://app.teable.io/api
  baseurl_source: declared
  description: Columns within a table.
  name: Teable Field API
  slug: teable-field-api
- baseURL: https://app.teable.io/api
  baseurl_source: declared
  description: Rows within a table.
  name: Teable Record API
  slug: teable-record-api
- baseURL: https://app.teable.io/api
  baseurl_source: declared
  description: Top-level workspaces.
  name: Teable Space API
  slug: teable-space-api
- baseURL: https://app.teable.io/api
  baseurl_source: declared
  description: Spreadsheet-like tables within a base.
  name: Teable Table API
  slug: teable-table-api
- baseURL: https://app.teable.io/api
  baseurl_source: declared
  description: Views over a table.
  name: Teable View API
  slug: teable-view-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Teable Attachment API
  slug: open-teable-attachment-api
- collection_type: open
  name: Teable Attachment Base API
  slug: open-teable-base-api
- collection_type: open
  name: Teable Attachment Field API
  slug: open-teable-field-api
- collection_type: open
  name: Teable Attachment Record API
  slug: open-teable-record-api
- collection_type: open
  name: Teable Attachment Space API
  slug: open-teable-space-api
- collection_type: open
  name: Teable Attachment Table API
  slug: open-teable-table-api
- collection_type: open
  name: Teable Attachment View API
  slug: open-teable-view-api
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
overview: 'Teable publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Attachment API, Base API, Field API, and 4 more. Tagged areas include No-Code, Database, Airtable Alternative, Postgres, and Open-Source.


  Teable''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Teable Plans Pricing
  plan_count: 5
  slug: teable-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Teable Rate Limits
  slug: teable-rate-limits
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.9
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Open-Source
website: https://teable.io
---
