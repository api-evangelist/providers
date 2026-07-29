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
- description: The Sourcehut GraphQL API provides programmatic access to all sr.ht services including git hosting, Mercurial hosting, build pipelines, mailing lists, bug tracking, and account management. Each servic
  name: Sourcehut GraphQL GraphQL API
  slug: graphql-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sourcehut-graphql-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sourcehut.org/
- group: docs
  title: ''
  type: Documentation
  url: https://man.sr.ht/graphql.md
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sourcehut/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sourcehut
- group: commercial
  title: ''
  type: Pricing
  url: https://sourcehut.org/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/sourcehut-graphql-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sourcehut-graphql-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/sourcehut-graphql-finops.md
- group: company
  title: ''
  type: Blog
  url: https://sourcehut.org/blog/index.xml
created: 2026-06-14
description: Sourcehut (sr.ht) is an open-source software forge offering version control, build automation, bug tracking, mailing lists, and more through a unified GraphQL API. Each service — git.sr.ht, builds.sr.ht, lists.sr.ht, todo.sr.ht, and others — exposes its own GraphQL endpoint at /query, enabling developers to query and manage their projects programmatically with a consistent interface.
graphqls:
- description: The Sourcehut (sr.ht) GraphQL API provides programmatic access to the git.sr.ht version control service. It exposes types for repositories, git objects (commits, trees, blobs, tags), references, acces
  name: Sourcehut GraphQL GraphQL API
  slug: sourcehut-graphql-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sourcehut-graphql.png
layout: provider
modified: 2026-06-14
name: Sourcehut GraphQL
nav: Providers
network: true
overview: 'Sourcehut GraphQL publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Developer Tools, Software Forge, Version Control, and Open Source.


  Sourcehut GraphQL''s developer surface includes documentation, pricing, engineering blog, and 7 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 23.4
  delta: 9.2
  facets:
    commercial_clarity: 10.5
    contract_quality: 43.2
    developer_ergonomics: 10.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/sourcehut-graphql/refs/heads/main/screenshots/sourcehut-graphql-2026-06-20T194224.png
security:
- kind: domain-security
  name: Sourcehut Graphql Domain Security
  slug: sourcehut-graphql-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sourcehut-graphql
tags:
- GraphQL
- Developer Tools
- Software Forge
- Version Control
- Open Source
- CI/CD
- Git
website: https://sourcehut.org/
---
