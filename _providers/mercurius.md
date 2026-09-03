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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: GraphQL adapter for Fastify enabling high-performance GraphQL servers and gateways with JIT compilation, query caching, subscriptions, and federation.
  name: Mercurius API
  slug: api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mercurius-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mercurius.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://mercurius.dev/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mercuriusinc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mercurius-js
- group: other
  title: ''
  type: Licensing
  url: https://github.com/mercurius-js/mercurius/blob/master/LICENSE
- group: commercial
  title: ''
  type: Plans
  url: plans/mercurius-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mercurius-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/mercurius-finops.md
created: 2026-06-14
description: High-performance GraphQL server for Fastify with Just-In-Time compilation via graphql-jit, automatic query caching, N+1 prevention via dataloader integration, federation support, subscription via WebSocket, batched query support, and GraphQL Playground integration.
graphqls:
- description: Mercurius is a GraphQL adapter for Fastify. It exposes a GraphQL endpoint that handles queries, mutations, and subscriptions over HTTP and WebSocket.
  name: Mercurius GraphQL
  slug: mercurius-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mercurius.png
layout: provider
modified: 2026-06-14
name: Mercurius
nav: Providers
network: true
overview: 'Mercurius publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Fastify, Node.js, Federation, and WebSocket.


  Mercurius'' developer surface includes documentation and 8 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 36.2
    developer_ergonomics: 9.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 19.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mercurius/refs/heads/main/screenshots/mercurius-2026-06-20T185212.png
security:
- kind: domain-security
  name: Mercurius Domain Security
  slug: mercurius-domain-security
  summary_line: TLSv1.3
slug: mercurius
tags:
- GraphQL
- Fastify
- Node.js
- Federation
- WebSocket
- Open-Source
website: https://mercurius.dev/
---
