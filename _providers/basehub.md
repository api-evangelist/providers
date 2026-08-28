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
- description: GraphQL API for programmatically querying and mutating content in BaseHub repositories. Authenticated via x-basehub-token header, with a TypeScript-native SDK that generates type-safe clients from the
  name: BaseHub API
  slug: api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/basehub-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://basehub.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.basehub.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/basehubai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/basehub-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://basehub.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/basehub-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/basehub-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/basehub-finops.md
- group: company
  title: ''
  type: Blog
  url: https://basehub.com/blog/rss.xml
created: 2026-06-14
description: GraphQL-first documentation and content platform where content is queried via a TypeScript-native GraphQL client with full type safety generated from the content schema.
graphqls:
- description: BaseHub is a GraphQL-first headless CMS and content platform where every repository exposes a fully type-safe GraphQL API. Because BaseHub schemas are dynamically generated from each repository's cont
  name: BaseHub GraphQL API
  slug: basehub-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/basehub.png
layout: provider
modified: 2026-06-14
name: BaseHub
nav: Providers
network: true
overview: 'BaseHub publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Headless CMS, Content Management, AI-Native, and TypeScript.


  BaseHub''s developer surface includes documentation, pricing, engineering blog, and 7 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 22.2
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 22.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/basehub/refs/heads/main/screenshots/basehub-2026-06-20T173048.png
security:
- kind: domain-security
  name: Basehub Domain Security
  slug: basehub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: basehub
tags:
- GraphQL
- Headless CMS
- Content Management
- AI-Native
- TypeScript
website: https://basehub.com
---
