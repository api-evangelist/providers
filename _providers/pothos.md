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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Plugin-based GraphQL schema builder for TypeScript that enables type-safe, code-first schema construction with zero runtime overhead and no code generation required. Supports plugins for Prisma, Relay
  name: Pothos GraphQL API
  slug: graphql-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pothos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pothos-graphql.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://pothos-graphql.dev/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hayes/pothos
- group: build
  title: ''
  type: NPM
  url: https://www.npmjs.com/package/@pothos/core
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/mNe73qvwAB
- group: commercial
  title: ''
  type: Plans
  url: plans/pothos-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pothos-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/pothos-finops.md
created: 2026-06-14
description: TypeScript-first GraphQL schema builder with a plugin system for Prisma, Relay, federation, simple objects, and code-first type-safe schema construction without code generation.
graphqls:
- description: Pothos is a TypeScript-first, code-first GraphQL schema builder library. It is not a hosted service with a network endpoint — it is an npm package that developers use to construct GraphQL schemas prog
  name: Pothos GraphQL API
  slug: pothos-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pothos.png
layout: provider
modified: 2026-06-14
name: Pothos
nav: Providers
network: true
overview: 'Pothos publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, TypeScript, Schema Builder, Code-First, and Plugin System.


  Pothos'' developer surface includes documentation and 8 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 20.6
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 14.3
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 20.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pothos/refs/heads/main/screenshots/pothos-2026-06-20T192022.png
security:
- kind: domain-security
  name: Pothos Domain Security
  slug: pothos-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: pothos
tags:
- GraphQL
- TypeScript
- Schema Builder
- Code-First
- Plugin System
website: https://pothos-graphql.dev/
---
