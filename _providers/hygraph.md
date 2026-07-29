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
api_count: 2
apis:
- description: 'Native GraphQL API that auto-generates queries, mutations, and real-time subscriptions from the project content schema. Supports content federation, multi-environment delivery, and a high-performance '
  name: Hygraph GraphQL Content API
  slug: graphql-content-api
- description: GraphQL API for programmatically managing Hygraph project schema, content models, fields, environments, webhooks, and API tokens. Used for schema migrations and automated project provisioning.
  name: Hygraph Management API
  slug: management-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hygraph-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hygraph.com
- group: docs
  title: ''
  type: Documentation
  url: https://hygraph.com/docs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hygraph
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hygraph
- group: company
  title: ''
  type: Blog
  url: https://hygraph.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://hygraph.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/hygraph/refs/heads/main/plans/hygraph-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/hygraph/refs/heads/main/rate-limits/hygraph-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/hygraph/refs/heads/main/finops/hygraph-finops.md
- group: operate
  title: ''
  type: ChangeLog
  url: https://hygraph.com/changelog
- group: learn
  title: ''
  type: Learn
  url: https://hygraph.com/learn
- group: docs
  title: ''
  type: MCPDocumentation
  url: https://hygraph.com/docs/hygraph-ai/mcp-server
created: '2026-06-14'
description: GraphQL-native headless CMS (formerly GraphCMS) with content federation, content environments, webhooks, and a flexible GraphQL Content API for building headless applications.
graphqls:
- description: Hygraph (formerly GraphCMS) is a GraphQL-native headless CMS that auto-generates a full GraphQL Content API from your project's content schema. Every content model you define becomes a set of queries,
  name: Hygraph GraphQL API
  slug: hygraph-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hygraph.png
layout: provider
modified: '2026-07-25'
name: Hygraph
nav: Providers
network: true
overview: 'Hygraph publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Headless CMS, Content Management, Content Federation, and Webhooks.


  Hygraph''s developer surface includes documentation, engineering blog, pricing, changelog, and 9 more developer resources.'
random_paper: 44
score:
  band: emerging
  composite: 25.0
  delta: 10.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 48.1
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/hygraph/refs/heads/main/screenshots/hygraph-2026-06-20T183039.png
security:
- kind: domain-security
  name: Hygraph Domain Security
  slug: hygraph-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hygraph
tags:
- GraphQL
- Headless CMS
- Content Management
- Content Federation
- Webhooks
- Digital Experience
website: https://hygraph.com
---
