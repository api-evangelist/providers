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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Stash provides a mobile-first investing and banking platform enabling fractional share purchases, automated smart portfolio management, retirement accounts, and a Stock-Back debit card. The platform i
  name: Stash Investing API
  slug: stash-investing-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/stash-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stash-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/stash/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/stash/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/stash/refs/heads/main/finops/finops.yml
- group: operate
  title: ''
  type: Status
  url: https://status.stash.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stash.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stash.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.stashinvest.com/security
- group: company
  title: ''
  type: Blog
  url: https://www.stash.com/learn
- group: company
  title: ''
  type: EngineeringBlog
  url: https://medium.com/stash-engineering
- group: company
  title: ''
  type: Press
  url: https://www.stash.com/press
created: '2026-06-13'
description: Stash is an investing and banking app that enables fractional share investing, automated portfolio building, bank account management with a Stock-Back debit card, custodial accounts for minors, IRA retirement accounts, and financial education content. Stash serves over one million customers and has $4.3 billion under management, offering subscription-based access to a hybrid DIY and robo-advisor investing experience starting at $3 per month.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stash.png
layout: provider
modified: '2026-06-13'
name: Stash
nav: Providers
network: true
overview: 'Stash publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Investing, Banking, Fractional Shares, and Portfolio Management.


  Stash''s developer surface includes status page, engineering blog, and 10 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 100
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 20.8
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 20.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 24.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stash/refs/heads/main/screenshots/stash-2026-06-20T194517.png
security:
- kind: domain-security
  name: Stash Domain Security
  slug: stash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Stash Trust Center
  slug: stash-trust-center
  summary_line: PCI DSS
slug: stash
tags:
- Fintech
- Investing
- Banking
- Fractional Shares
- Portfolio Management
- Financial Education
- Robo-Advisor
- Stock-Back
- Custodial Accounts
- IRA
---
