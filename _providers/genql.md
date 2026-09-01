---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
- description: Fully-typed TypeScript client generated from any GraphQL schema, enabling type-safe query building with IDE auto-completion, batching support, subscriptions, and zero runtime dependencies across brows
  name: Genql GraphQL API
  slug: graphql-api
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/remorses/genql/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/remorses/genql/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/remorses/genql/blob/master/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/remorses/genql/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/genql-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://genql.dev
- group: docs
  title: ''
  type: Documentation
  url: https://genql.dev/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/remorses/genql
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.genql.dev
- group: commercial
  title: ''
  type: Plans
  url: plans/genql-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/genql-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/genql-finops.md
created: '2026-03-25'
description: TypeScript code generator and GraphQL client that generates a fully-typed client from any GraphQL schema, supporting batched queries, retries, and works with any HTTP endpoint.
finops:
- name: Genql Finops
  service_category: API
  slug: genql-finops
graphqls:
- description: Genql is a TypeScript code generator and type-safe GraphQL client library. It does **not** expose a hosted GraphQL server or API endpoint of its own. Instead, it reads any GraphQL schema (from a local
  name: Genql GraphQL API
  slug: genql-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/genql.png
layout: provider
modified: '2026-06-14'
name: Genql
nav: Providers
network: true
overview: 'Genql publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, TypeScript, Code Generation, SDK, and Developer Tools.


  Genql''s developer surface includes documentation, changelog, and 10 more developer resources.'
plans:
- name: Genql Plans Pricing
  plan_count: 3
  slug: genql-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Genql Rate Limits
  slug: genql-rate-limits
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 36.2
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 40.0
  previous_composite: 27.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/genql/refs/heads/main/screenshots/genql-2026-06-20T181736.png
security:
- kind: domain-security
  name: Genql Domain Security
  slug: genql-domain-security
  summary_line: TLSv1.3 · HSTS
slug: genql
tags:
- GraphQL
- TypeScript
- Code Generation
- SDK
- Developer Tools
website: https://genql.dev
---
