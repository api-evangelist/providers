---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Ledgy Agentic Access
  operation_count: 1
  slug: ledgy-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The GraphQL API from Ledgy — 1 operation(s) for graphql.
  name: Ledgy GraphQL API
  slug: ledgy-graphql-api
artifact_total: 10
collections:
- collection_type: open
  name: Ledgy GraphQL API
  slug: open-ledgy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ledgy-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ledgy-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ledgy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ledgy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ledgy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ledgy
- group: company
  title: ''
  type: Website
  url: https://www.ledgy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ledgy.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/ledgy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ledgy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ledgy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ledgy.com/blog
created: '2026-06-21'
description: Ledgy is a European equity-management platform for cap tables, ESOP/equity plans, stakeholder and investor relations, and financing rounds. The Ledgy GraphQL API exposes a company's cap table, transactions (convertibles, grants, transfers), share classes, financing rounds, ESOP grants, and portfolio data through a single Bearer-authenticated endpoint at https://app.ledgy.com/graphql.
finops:
- name: Ledgy Finops
  service_category: Management and Governance
  slug: ledgy-finops
graphqls:
- description: '[Ledgy](https://www.ledgy.com/) is a European equity-management platform for cap tables,'
  name: Ledgy GraphQL API
  slug: ledgy-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ledgy.png
layout: provider
modified: '2026-06-21'
name: Ledgy
nav: Providers
network: true
overview: 'Ledgy publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Equity Management, Cap Table, ESOP, Stakeholders, and GraphQL.


  Ledgy''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Ledgy Plans Pricing
  plan_count: 3
  slug: ledgy-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Ledgy Rate Limits
  slug: ledgy-rate-limits
score:
  band: thin
  composite: 38.7
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 61.9
    developer_ergonomics: 21.7
    discoverability: 60.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Ledgy Authentication
  slug: ledgy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ledgy Domain Security
  slug: ledgy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Ledgy Trust Center
  slug: ledgy-trust-center
  summary_line: SOC 2, ISO 27001
slug: ledgy
tags:
- Equity Management
- Cap Table
- ESOP
- Stakeholders
- GraphQL
website: https://www.ledgy.com/
---
