---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'REST API for creating and managing interactive sales demos, personalizing demo environments, tracking prospect engagement, and accessing analytics. Available on the Scale (enterprise) plan with Demos '
  name: Walnut Demos API
  slug: walnut-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/walnut-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.walnut.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.walnut.io/hc/en-us
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/teamwalnut
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teamwalnut/
- group: company
  title: ''
  type: Blog
  url: https://www.walnut.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.walnut.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.walnut.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/walnutinc
- group: commercial
  title: ''
  type: Plans
  url: plans/walnut-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/walnut-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/walnut-finops.yml
created: '2026-06-13'
description: Walnut is an AI-powered sales demo platform that enables go-to-market teams to create, personalize, and embed interactive product demonstrations. The platform provides a REST API for creating personalized interactive product demos, managing demo environments, tracking engagement, and accessing analytics to drive faster sales cycles and higher conversions.
finops:
- name: Walnut Finops
  service_category: ''
  slug: walnut-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/walnut.png
layout: provider
modified: '2026-06-13'
name: Walnut
nav: Providers
network: true
overview: 'Walnut publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Demo, Interactive Demos, Product Demos, Sales Enablement, and Demo Analytics.


  Walnut''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Walnut Plans Pricing
  plan_count: 3
  slug: walnut-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 0
  name: Walnut Rate Limits
  slug: walnut-rate-limits
score:
  band: emerging
  composite: 21.8
  delta: -2.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 24.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/walnut/refs/heads/main/screenshots/walnut-2026-06-20T201221.png
security:
- kind: domain-security
  name: Walnut Domain Security
  slug: walnut-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: walnut
tags:
- Sales Demo
- Interactive Demos
- Product Demos
- Sales Enablement
- Demo Analytics
- Go-to-Market
- AI-Powered
website: https://www.walnut.io/
---
