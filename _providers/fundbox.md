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
- description: The Fundbox Partner API provides an API stack for platforms to embed white-labeled net payment terms, credit underwriting, and working capital financing directly within their B2B applications. The API
  name: Fundbox Partner API
  slug: fundbox-partner-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fundbox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fundbox.com
- group: docs
  title: ''
  type: Documentation
  url: https://fundbox.com/partners/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/fundbox
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fundbox/
- group: company
  title: ''
  type: Blog
  url: https://fundbox.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://fundbox.com/partners/
- group: other
  title: ''
  type: X
  url: https://x.com/fundbox
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/fundbox/refs/heads/main/plans/fundbox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/fundbox/refs/heads/main/rate-limits/fundbox-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/fundbox/refs/heads/main/finops/fundbox-finops.yml
created: 2026-06-13
description: Fundbox is an API-first embedded working capital platform that enables B2B sellers and platforms to offer net payment terms, credit underwriting, and working capital financing. Founded in 2013 and headquartered in Plano, TX, Fundbox has unlocked over $6 billion in capital for more than 170,000 small businesses. The platform provides a fully white-labeled, embedded lending API stack that allows B2B platforms to integrate credit decisioning, compliance, and servicing in two weeks or less.
finops:
- name: Fundbox Finops
  service_category: ''
  slug: fundbox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fundbox.png
layout: provider
modified: 2026-06-13
name: Fundbox
nav: Providers
network: true
overview: 'Fundbox publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, B2B Credit, Embedded Finance, Net Terms, and Working Capital.


  Fundbox''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Fundbox Plans Pricing
  plan_count: 2
  slug: fundbox-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 2
  name: Fundbox Rate Limits
  slug: fundbox-rate-limits
score:
  band: emerging
  composite: 22.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fundbox/refs/heads/main/screenshots/fundbox-2026-06-20T181616.png
security:
- kind: domain-security
  name: Fundbox Domain Security
  slug: fundbox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fundbox
tags:
- Fintech
- B2B Credit
- Embedded Finance
- Net Terms
- Working Capital
- Small Business
- Lending
- Credit Underwriting
website: https://fundbox.com
---
