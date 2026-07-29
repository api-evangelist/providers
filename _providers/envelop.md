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
- description: The @envelop/core package exposes the envelop() function and a set of built-in plugins (useSchema, useEngine, useLogger, useMaskedErrors, useExtendContext) that wrap the GraphQL execution pipeline — p
  name: Envelop API
  slug: api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/envelop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://the-guild.dev/graphql/envelop
- group: docs
  title: ''
  type: Documentation
  url: https://the-guild.dev/graphql/envelop/docs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-guild-software
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/graphql-hive/envelop
- group: commercial
  title: ''
  type: Pricing
  url: https://the-guild.dev/graphql/envelop/plugins
- group: commercial
  title: ''
  type: Plans
  url: plans/envelop-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/envelop-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/envelop-finops.md
created: 2026-06-14
description: GraphQL plugin system from The Guild that wraps the GraphQL execution pipeline with composable hooks for auth, caching, tracing, error handling, and rate limiting.
graphqls:
- description: Envelop is a lightweight JavaScript/TypeScript plugin system for wrapping the GraphQL execution pipeline. Developed by The Guild, it exposes composable lifecycle hooks that intercept and extend the pa
  name: Envelop GraphQL Plugin API
  slug: envelop-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/envelop.png
layout: provider
modified: 2026-06-14
name: Envelop
nav: Providers
network: true
overview: 'Envelop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Plugins, Middleware, Execution, and Open Source.


  Envelop''s developer surface includes documentation, pricing, and 7 more developer resources.'
random_paper: 68
score:
  band: emerging
  composite: 23.2
  delta: 10.7
  facets:
    commercial_clarity: 10.5
    contract_quality: 48.1
    developer_ergonomics: 8.7
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/envelop/refs/heads/main/screenshots/envelop-2026-06-20T180735.png
security:
- kind: domain-security
  name: Envelop Domain Security
  slug: envelop-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: envelop
tags:
- GraphQL
- Plugins
- Middleware
- Execution
- Open Source
website: https://the-guild.dev/graphql/envelop
---
