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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Real-time GraphQL content API for querying and mutating content stored in Caisy projects. Supports filtering, pagination, sorting, nested document referencing, and rich text as AST. Each project expos
  name: Caisy API
  slug: api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caisy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caisy.io/
- group: docs
  title: ''
  type: Documentation
  url: https://caisy.io/developer/docs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cyclus-digital
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/caisy-io
- group: commercial
  title: ''
  type: Pricing
  url: https://caisy.io/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://caisy.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://caisy.io/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/caisy-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/caisy-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/caisy-finops.md
created: 2026-06-14
description: GraphQL-native headless CMS with a real-time GraphQL content API, rich text as AST, multi-site support, and component-based content blueprints.
graphqls:
- description: Caisy's entire content API is GraphQL-native, built on the Relay specification. Every project gets its own dedicated GraphQL endpoint.
  name: Caisy GraphQL API
  slug: caisy-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/caisy.png
layout: provider
modified: 2026-06-14
name: Caisy
nav: Providers
network: true
overview: 'Caisy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Headless CMS, Content Management, content-api, and Multi-Site.


  Caisy''s developer surface includes documentation, pricing, changelog, engineering blog, and 7 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 23.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/caisy/refs/heads/main/screenshots/caisy-2026-06-20T173839.png
security:
- kind: domain-security
  name: Caisy Domain Security
  slug: caisy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: caisy
tags:
- GraphQL
- Headless CMS
- Content Management
- content-api
- Multi-Site
website: https://caisy.io/
---
