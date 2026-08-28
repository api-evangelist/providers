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
- description: Schema-first Go library for building type-safe GraphQL servers with automatic code generation, resolver scaffolding, DataLoader integration, subscriptions, and middleware support.
  name: gqlgen GraphQL API
  slug: graphql-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gqlgen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gqlgen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://gqlgen.com/getting-started/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/posts/alsgladkikh_graphql-in-go-gqlgen-tutorial-activity-7086977174150221824-Ksa8
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/99designs/gqlgen
- group: commercial
  title: ''
  type: Pricing
  url: https://pkg.go.dev/github.com/99designs/gqlgen
- group: commercial
  title: ''
  type: Plans
  url: plans/gqlgen-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gqlgen-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/gqlgen-finops.md
created: 2026-06-14
description: Go library for building GraphQL servers with a schema-first approach, automatic code generation for resolvers and models, DataLoader support, and OpenTelemetry tracing.
graphqls:
- description: 'gqlgen is a schema-first Go library for building type-safe GraphQL servers. It takes a GraphQL SDL schema as input and generates Go server-side boilerplate — resolver interfaces, model structs, and a '
  name: gqlgen GraphQL API
  slug: gqlgen-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gqlgen.png
layout: provider
modified: 2026-06-14
name: gqlgen
nav: Providers
network: true
overview: 'gqlgen publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Go, Code Generation, Schema-First, and Open-Source.


  gqlgen''s developer surface includes documentation, pricing, and 7 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 20.4
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 20.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gqlgen/refs/heads/main/screenshots/gqlgen-2026-06-20T182306.png
security:
- kind: domain-security
  name: Gqlgen Domain Security
  slug: gqlgen-domain-security
  summary_line: TLSv1.3
slug: gqlgen
tags:
- GraphQL
- Go
- Code Generation
- Schema-First
- Open-Source
website: https://gqlgen.com/
---
