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
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Betterment investment and cash account data is accessible to third-party developers via the Plaid open banking aggregator. Through Plaid, developers can retrieve account balances, holdings, transactio
  name: Betterment via Plaid (Open Banking)
  slug: betterment-via-plaid-open-banking
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/betterment-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/betterment-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.betterment.com
- group: company
  title: ''
  type: Blog
  url: https://www.betterment.com/engineering
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Betterment
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/betterment/
- group: other
  title: ''
  type: X
  url: https://twitter.com/Betterment
- group: commercial
  title: ''
  type: Pricing
  url: https://www.betterment.com/pricing
- group: operate
  title: ''
  type: Contact
  url: https://www.betterment.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.betterment.com/security/privacypolicy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wwws.betterment.com/app/terms/everyday
- group: auth
  title: ''
  type: DataAggregationDisclosure
  url: https://www.betterment.com/legal/data-aggregation-disclosure
- group: auth
  title: ''
  type: SecurityPage
  url: https://www.betterment.com/resources/built-two-factor-authentication-betterment-accounts/
- group: commercial
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/finops.yml
- group: other
  title: ''
  type: ProductPage
  url: https://www.betterment.com/work/payroll-integrations
created: 2026-06-13
description: Betterment is a robo-advisor and financial planning platform offering automated investment management, tax-loss harvesting, retirement planning, and goal-based portfolio rebalancing. Founded in 2010, Betterment serves individual investors through its Digital and Premium Advisory plans, and employers through Betterment at Work — a 401(k) plan administration product that integrates with 350+ payroll providers via a private partner API. Betterment does not offer a public developer API; third-party application developers access Betterment account data through open banking aggregators such as Plaid and BankSync. Betterment Engineering maintains an active open-source presence on GitHub, publishing internal tools for background job processing, split testing, Flutter golden testing, and Rails security.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/betterment.png
layout: provider
modified: '2026-07-25'
name: Betterment
nav: Providers
network: true
overview: 'Betterment publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Robo-Advisor, Automated Investing, Financial Planning, Tax-Loss Harvesting, and Retirement Planning.


  Betterment''s developer surface includes engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 65
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 23.8
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 23.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 24.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/betterment/refs/heads/main/screenshots/betterment-2026-06-20T173216.png
security:
- kind: domain-security
  name: Betterment Domain Security
  slug: betterment-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Betterment Trust Center
  slug: betterment-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: betterment
tags:
- Robo-Advisor
- Automated Investing
- Financial Planning
- Tax-Loss Harvesting
- Retirement Planning
- Portfolio Management
- 401k
- Fintech
- Wealth Management
- Investment Rebalancing
- Open Banking
website: https://www.betterment.com
---
