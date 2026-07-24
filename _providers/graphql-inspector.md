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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Command-line tool for comparing two GraphQL schemas and generating a detailed list of breaking, non-breaking, and dangerous changes. Also validates documents and fragments, measures schema coverage, a
  name: GraphQL Inspector CLI
  slug: graphql-inspector-cli
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graphql-inspector-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://the-guild.dev/graphql/inspector
- group: docs
  title: ''
  type: Documentation
  url: https://the-guild.dev/graphql/inspector/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/graphql-hive
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-guild-software
- group: company
  title: ''
  type: Blog
  url: https://the-guild.dev/blog/tag/graphql-inspector
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/marketplace/graphql-inspector
- group: commercial
  title: ''
  type: Plans
  url: plans/graphql-inspector-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/graphql-inspector-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/graphql-inspector-finops.md
created: '2026-06-14'
description: Schema change detection and validation tooling that checks for breaking changes, deprecated fields, and coverage gaps between GraphQL schema versions, available as CLI, CI, and GitHub Action.
graphqls:
- description: GraphQL Inspector is a CLI tool and GitHub Action for schema change detection and validation — it consumes GraphQL schemas rather than exposing a live GraphQL endpoint. There is no public hosted Graph
  name: GraphQL Inspector GraphQL API
  slug: graphql-inspector-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/graphql-inspector.png
layout: provider
modified: '2026-06-14'
name: GraphQL Inspector
nav: Providers
network: true
overview: 'GraphQL Inspector publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Schema Validation, Breaking Change Detection, Developer Tools, and Open Source.


  GraphQL Inspector''s developer surface includes documentation, engineering blog, pricing, and 7 more developer resources.'
random_paper: 45
score:
  band: minimal
  composite: 11.7
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/graphql-inspector/refs/heads/main/screenshots/graphql-inspector-2026-06-20T182337.png
security:
- kind: domain-security
  name: Graphql Inspector Domain Security
  slug: graphql-inspector-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: graphql-inspector
tags:
- GraphQL
- Schema Validation
- Breaking Change Detection
- Developer Tools
- Open Source
- CI/CD
- GitHub Actions
website: https://the-guild.dev/graphql/inspector
---
