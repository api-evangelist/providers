---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Investment-as-a-service REST API that allows developers to embed regulated investment products (savings, mutual funds, treasury bills, Eurobonds, equities) into their applications. Supports user accou
  name: Cowrywise Embed API
  slug: embed-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cowrywise-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cowrywise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cowrywise.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cowrywise.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/cowrywise
- group: company
  title: ''
  type: LinkedIn
  url: https://ng.linkedin.com/company/cowrywise
- group: company
  title: ''
  type: Blog
  url: https://cowrywise.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://cowrywise.com/embed
- group: other
  title: ''
  type: X
  url: https://twitter.com/cowrywise
- group: commercial
  title: ''
  type: Plans
  url: plans/cowrywise-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cowrywise-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cowrywise-finops.yml
created: '2026-06-13'
description: Cowrywise is a Nigerian wealth management platform and SEC-licensed fund manager offering savings plans, investment portfolios, dollar accounts, and financial goal tracking for individuals. The Embed API provides investment-as-a-service capabilities, enabling developers to integrate regulated African investment products — including savings, mutual funds, treasury bills, Eurobonds, and equities — into their own applications via a single REST API with OAuth 2.0 authentication.
finops:
- name: Cowrywise Finops
  service_category: ''
  slug: cowrywise-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cowrywise.png
layout: provider
modified: '2026-06-13'
name: Cowrywise
nav: Providers
network: true
overview: 'Cowrywise publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Wealth Management, Investments, Savings, and Mutual Funds.


  Cowrywise''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Cowrywise Plans Pricing
  plan_count: 2
  slug: cowrywise-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 3
  name: Cowrywise Rate Limits
  slug: cowrywise-rate-limits
score:
  band: emerging
  composite: 21.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cowrywise/refs/heads/main/screenshots/cowrywise-2026-06-20T175153.png
security:
- kind: domain-security
  name: Cowrywise Domain Security
  slug: cowrywise-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Cowrywise Vulnerability Disclosure
  slug: cowrywise-vulnerability-disclosure
  summary_line: disclosure policy published
slug: cowrywise
tags:
- Fintech
- Wealth Management
- Investments
- Savings
- Mutual Funds
- Nigeria
- Africa
- Financial Services
- REST API
website: https://cowrywise.com/
---
