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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Glide Apps Agentic Access
  operation_count: 12
  slug: glide-apps-agentic-access
  summary_line: 12 operations · 8 acting
api_count: 4
apis:
- description: Query a Big Table with SQL.
  name: Glide Queries API
  slug: glide-apps-queries-api
- description: List, read, add, update, and delete rows in a Big Table.
  name: Glide Rows API
  slug: glide-apps-rows-api
- description: Stage large data payloads in serial chunks for bulk loads.
  name: Glide Stashes API
  slug: glide-apps-stashes-api
- description: Create, overwrite, and list Big Tables.
  name: Glide Tables API
  slug: glide-apps-tables-api
artifact_total: 12
collections:
- collection_type: open
  name: Glide API
  slug: open-glide-apps
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/glide-apps-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/glide-apps-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glide-apps-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/glide-apps-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/glideapps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/glideapps
- group: company
  title: ''
  type: Website
  url: https://www.glideapps.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.glideapps.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/glide-apps-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/glide-apps-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/glide-apps-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.glideapps.com/blog
created: '2026-06-20'
description: Glide is a no-code platform for building custom business apps from your data. The Glide REST API (v2) lets you programmatically work with Glide Big Tables - creating tables, listing and paginating rows, adding, updating, and deleting rows, staging large batches with stashes, and querying tables with SQL - using a Bearer API token.
finops:
- name: Glide Apps Finops
  service_category: Application Development and No-Code
  slug: glide-apps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glide-apps.png
layout: provider
modified: '2026-06-20'
name: Glide
nav: Providers
network: true
overview: 'Glide publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Queries API, Rows API, Stashes API, and 1 more. Tagged areas include No Code, App Builder, Tables, Big Tables, and Data.


  Glide''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Glide Apps Plans Pricing
  plan_count: 5
  slug: glide-apps-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 4
  name: Glide Apps Rate Limits
  slug: glide-apps-rate-limits
score:
  band: thin
  composite: 41.9
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 63.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glide-apps/refs/heads/main/screenshots/glide-apps-2026-06-20T181910.png
security:
- kind: authentication
  name: Glide Apps Authentication
  slug: glide-apps-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Glide Apps Domain Security
  slug: glide-apps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Glide Apps Trust Center
  slug: glide-apps-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: glide-apps
tags:
- No Code
- App Builder
- Tables
- Big Tables
- Data
- AI
website: https://www.glideapps.com
---
