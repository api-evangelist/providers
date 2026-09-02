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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: RedwoodJS exposes a schema-first GraphQL API via GraphQL Yoga at the /graphql endpoint. SDL files define queries and mutations while service functions act as resolvers; Redwood combines them automatic
  name: RedwoodJS GraphQL API
  slug: graphql-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redwoodjs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://redwoodjs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.redwoodjs.com/docs/introduction
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/redwoodjs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/redwoodjs
- group: commercial
  title: ''
  type: Pricing
  url: https://redwoodjs.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/redwoodjs-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/redwoodjs-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/redwoodjs-finops.md
created: 2026-06-14
description: Full-stack JavaScript framework with a built-in GraphQL API layer (Yoga + Envelop stack), schema-first development, and automatic SDL generation for Prisma-backed services.
graphqls:
- description: RedwoodJS exposes a schema-first GraphQL API powered by GraphQL Yoga and the Envelop plugin system. SDL files (*.sdl.ts) declare types, queries, and mutations while service functions serve as resolver
  name: RedwoodJS GraphQL API
  slug: redwoodjs-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/redwoodjs.png
layout: provider
modified: 2026-06-14
name: RedwoodJS
nav: Providers
network: true
overview: 'RedwoodJS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Full-Stack, JavaScript, Prisma, and React.


  RedwoodJS''s developer surface includes documentation, pricing, and 7 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 36.2
    developer_ergonomics: 9.5
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 20.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/redwoodjs/refs/heads/main/screenshots/redwoodjs-2026-06-20T192742.png
security:
- kind: domain-security
  name: Redwoodjs Domain Security
  slug: redwoodjs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: redwoodjs
tags:
- GraphQL
- Full-Stack
- JavaScript
- Prisma
- React
- Framework
website: https://redwoodjs.com
---
