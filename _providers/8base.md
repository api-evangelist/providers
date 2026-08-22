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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The 8base GraphQL API provides auto-generated queries, mutations, and subscriptions for every data table in a workspace, covering full CRUD operations out-of-the-box. Each workspace is assigned a uniq
  name: 8base GraphQL API
  slug: graphql-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/8base-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.8base.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.8base.com/backend/graphql-api/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/8base
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/8base
- group: commercial
  title: ''
  type: Pricing
  url: https://www.8base.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/8base-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/8base-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/8base-finops.md
- group: company
  title: ''
  type: Blog
  url: https://www.8base.com/blog
created: 2026-06-14
description: 8base is a comprehensive Backend-as-a-Service platform that transforms the entire software development lifecycle by providing AI-assisted design, auto-generated serverless GraphQL infrastructure powered by AWS, and low-code full-stack App Builder tools. The platform enables developers and digital agencies to build scalable, production-grade cloud applications with SOC 2 and HIPAA compliance options without managing DevOps complexity.
graphqls:
- description: 'The 8base GraphQL API provides auto-generated queries, mutations, and subscriptions for every data table in a workspace. Each workspace gets a unique endpoint and receives full CRUD operations out of '
  name: 8base GraphQL API
  slug: 8base-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/8base.png
layout: provider
modified: 2026-06-14
name: 8base
nav: Providers
network: true
overview: '8base publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Backend as a Service, Low-Code, Serverless, and App Builder.


  8base''s developer surface includes documentation, pricing, engineering blog, and 7 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 22.5
  delta: -0.9
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 38.9
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 23.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/8base/refs/heads/main/screenshots/8base-2026-06-20T162859.png
security:
- kind: domain-security
  name: 8Base Domain Security
  slug: 8base-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 8base
tags:
- GraphQL
- Backend as a Service
- Low-Code
- Serverless
- App Builder
- Database
- Cloud Platform
website: https://www.8base.com
---
