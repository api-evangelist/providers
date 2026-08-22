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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Acorns Partner API combines OAuth and Partner APIs to allow authorized third parties (partners and aggregators) to access Acorns user data on behalf of said users. Organizations must complete an o
  name: Acorns Partner API
  slug: partner-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/acorns-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acorns-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.acorns.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.acorns.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acorns.com/pricing/
- group: auth
  title: ''
  type: Security
  url: https://www.acorns.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acorns.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acorns.com/terms
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.acorns.com/
- group: company
  title: ''
  type: Press
  url: https://www.acorns.com/press/
- group: company
  title: ''
  type: Blog
  url: https://www.acorns.com/learn/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Acornsgrow
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/acorns/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/acorns/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/acorns/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Acorns is a micro-investing and personal finance platform that helps everyday Americans grow their wealth through automated round-up investments, diversified portfolios, retirement accounts, high-yield savings, and financial wellness tools. The Acorns Partner API enables authorized third parties to access Acorns user data on behalf of users via OAuth 2.0.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/acorns.png
layout: provider
modified: '2026-06-13'
name: Acorns
nav: Providers
network: true
overview: 'Acorns publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Micro-Investing, Personal Finance, Fintech, Round-Ups, and Robo-Investing.


  Acorns'' developer surface includes pricing, engineering blog, GitHub presence, and 12 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 16
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 23.7
  delta: -2.3
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 26.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 25.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acorns/refs/heads/main/screenshots/acorns-2026-06-20T163923.png
security:
- kind: domain-security
  name: Acorns Domain Security
  slug: acorns-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Acorns Vulnerability Disclosure
  slug: acorns-vulnerability-disclosure
  summary_line: Bugcrowd
slug: acorns
tags:
- Micro-Investing
- Personal Finance
- Fintech
- Round-Ups
- Robo-Investing
- Retirement
- Savings
- Banking
- Financial Wellness
website: https://www.acorns.com/
---
