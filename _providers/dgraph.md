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
- description: Native GraphQL API layer that auto-generates queries, mutations, and real-time subscriptions from a user-defined schema, backed by Dgraph's distributed graph engine.
  name: Dgraph GraphQL API
  slug: dgraph-graphql-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dgraph-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://site.dgraph.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dgraph.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dgraph-labs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dgraph-io
- group: company
  title: ''
  type: Blog
  url: https://discuss.dgraph.io/c/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://site.dgraph.io/pricing
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/dgraph/refs/heads/main/plans/dgraph-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/dgraph/refs/heads/main/rate-limits/dgraph-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/dgraph/refs/heads/main/finops/dgraph-finops.md
- group: start
  title: ''
  type: CloudConsole
  url: https://cloud.dgraph.io/
- group: other
  title: ''
  type: Discuss
  url: https://discuss.dgraph.io/
created: '2026-06-14'
description: Distributed graph database with a native GraphQL API, automatic type enforcement, real-time subscriptions, horizontal scaling, and built-in authorization directives.
graphqls:
- description: Dgraph provides a native GraphQL API layer that sits directly on top of its distributed graph backend. Unlike adapter-based GraphQL implementations, Dgraph generates a complete GraphQL API — including
  name: Dgraph GraphQL API
  slug: dgraph-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dgraph.png
layout: provider
modified: '2026-06-14'
name: Dgraph
nav: Providers
network: true
overview: 'Dgraph publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Graph Database, Distributed Database, Real-Time, and Open-Source.


  Dgraph''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 5.3
    commercial_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 19.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dgraph/refs/heads/main/screenshots/dgraph-2026-06-20T175958.png
security:
- kind: domain-security
  name: Dgraph Domain Security
  slug: dgraph-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dgraph
tags:
- GraphQL
- Graph Database
- Distributed Database
- Real-Time
- Open-Source
- Knowledge Graph
website: https://site.dgraph.io/
---
