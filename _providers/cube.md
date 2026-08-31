---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 15.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: GraphQL API that enables Cube to deliver data over HTTP to GraphQL-enabled data applications. Exposes measures, dimensions, segments, and filters defined in the Cube semantic layer for use in front-en
  name: Cube GraphQL API
  slug: graphql-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/cube-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cube-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cube.dev
- group: docs
  title: ''
  type: Documentation
  url: https://cube.dev/docs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cube-dev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cube-js
- group: commercial
  title: ''
  type: Pricing
  url: https://cube.dev/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/cube-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cube-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/cube-finops.md
- group: company
  title: ''
  type: Blog
  url: https://cube.dev/blog
created: 2026-06-14
description: Semantic layer and headless BI platform with a GraphQL API for querying measures, dimensions, and segments across any SQL database or data warehouse.
graphqls:
- description: Cube exposes a GraphQL API that sits on top of its semantic layer, allowing front-end applications and embedded analytics tools to query measures, dimensions, and time dimensions defined across any co
  name: Cube GraphQL API
  slug: cube-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cube.png
layout: provider
modified: 2026-06-14
name: Cube
nav: Providers
network: true
overview: 'Cube publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Semantic Layer, Business Intelligence, Embedded Analytics, and Data Warehouse.


  Cube''s developer surface includes documentation, pricing, engineering blog, and 8 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 36.2
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 22.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cube/refs/heads/main/screenshots/cube-2026-06-20T175326.png
security:
- kind: domain-security
  name: Cube Domain Security
  slug: cube-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Cube Trust Center
  slug: cube-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: cube
tags:
- GraphQL
- Semantic Layer
- Business Intelligence
- Embedded Analytics
- Data Warehouse
website: https://cube.dev
---
