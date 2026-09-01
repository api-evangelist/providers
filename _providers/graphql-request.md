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
- description: Minimal, type-safe GraphQL client API supporting HTTP and in-memory transports, custom scalars, file uploads, and a composable extension system for JavaScript and TypeScript applications.
  name: GraphQL Request GraphQL API
  slug: graphql-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graphql-request-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://graffle.js.org
- group: docs
  title: ''
  type: Documentation
  url: https://graffle.js.org/guides/getting-started
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/graphql-portal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/graffle-js/graffle
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/sponsors/jasonkuhrt
- group: build
  title: ''
  type: NpmPackage
  url: https://www.npmjs.com/package/graphql-request
- group: commercial
  title: ''
  type: Plans
  url: plans/graphql-request-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/graphql-request-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/graphql-request-finops.md
created: 2026-06-14
description: Minimal, isomorphic GraphQL client for JavaScript/TypeScript originally from the Prisma team, now evolved into Graffle — with support for file uploads, batch requests, custom headers, TypeScript type inference, and a powerful extension system. Runs in Node.js and browsers.
graphqls:
- description: GraphQL Request (now evolved into **Graffle**) is a minimal, isomorphic GraphQL client library for JavaScript and TypeScript. It does not expose a hosted GraphQL endpoint of its own — instead, it is a
  name: GraphQL Request GraphQL API
  slug: graphql-request-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/graphql-request.png
layout: provider
modified: 2026-06-14
name: GraphQL Request
nav: Providers
network: true
overview: 'GraphQL Request publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, GraphQL Client, JavaScript, TypeScript, and Open-Source.


  GraphQL Request''s developer surface includes documentation, pricing, and 8 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 9.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 22.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/graphql-request/refs/heads/main/screenshots/graphql-request-2026-06-20T182337.png
security:
- kind: domain-security
  name: Graphql Request Domain Security
  slug: graphql-request-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: graphql-request
tags:
- GraphQL
- GraphQL Client
- JavaScript
- TypeScript
- Open-Source
- Isomorphic
website: https://graffle.js.org
---
