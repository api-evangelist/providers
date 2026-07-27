---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: REST APIs powering Ellevest's wealth management platform, including portfolio management, financial goal tracking, investment account operations, financial coaching scheduling, and personalized financ
  name: Ellevest Wealth Management API
  slug: ellevest-wealth-management-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ellevest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ellevest.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ellevest.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Ellevest
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ellevest
- group: company
  title: ''
  type: Blog
  url: https://www.ellevest.com/magazine
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ellevest.com/wealth-management
- group: operate
  title: ''
  type: StatusPage
  url: https://www.ellevest.com/
- group: other
  title: ''
  type: X
  url: https://x.com/ellevest
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/ellevest/refs/heads/main/plans/ellevest-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/ellevest/refs/heads/main/rate-limits/ellevest-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/ellevest/refs/heads/main/finops/ellevest-finops.yml
created: '2026-06-13'
description: Ellevest is a women-founded, women-led wealth management and financial planning firm dedicated to closing the gender wealth gap. The platform delivers personalized investment management and comprehensive financial planning for high-net-worth individuals, families, and institutions, with services including portfolio management, retirement and estate planning, tax strategy, and cash flow analysis. Ellevest leverages REST-based internal APIs for portfolio management, financial coaching, banking operations, and personalized investment goal tracking, with third-party account connectivity available through Open Banking aggregators such as Plaid.
finops:
- name: Ellevest Finops
  service_category: ''
  slug: ellevest-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ellevest.png
layout: provider
modified: '2026-06-13'
name: Ellevest
nav: Providers
network: true
overview: 'Ellevest publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Wealth Management, Investing, Financial Planning, and Women Finance.


  Ellevest''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Ellevest Plans Pricing
  plan_count: 2
  slug: ellevest-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 0
  name: Ellevest Rate Limits
  slug: ellevest-rate-limits
score:
  band: emerging
  composite: 22.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 22.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ellevest/refs/heads/main/screenshots/ellevest-2026-06-20T180612.png
security:
- kind: domain-security
  name: Ellevest Domain Security
  slug: ellevest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ellevest
tags:
- Financial Services
- Wealth Management
- Investing
- Financial Planning
- Women Finance
- Robo-Advisory
- Portfolio Management
website: https://www.ellevest.com/
---
