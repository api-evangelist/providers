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
    asyncapi_events: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-07-28'
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
overview: 'Caisy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Headless CMS, Content Management, Content API, and Multi-site.


  Caisy''s developer surface includes documentation, pricing, changelog, engineering blog, and 7 more developer resources.'
random_paper: 57
score:
  band: emerging
  composite: 24.5
  delta: 9.5
  facets:
    commercial_clarity: 10.5
    contract_quality: 43.2
    developer_ergonomics: 10.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
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
- Content API
- Multi-site
website: https://caisy.io/
---
