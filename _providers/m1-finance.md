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
api_count: 3
apis:
- description: M1 Invest provides automated fractional share portfolio management using the Pies system, allowing users to set target allocations across stocks and ETFs with dynamic rebalancing, auto-invest, and div
  name: M1 Invest
  slug: m1-invest
- description: M1 Borrow provides a portfolio line of credit (margin loans) allowing users to borrow up to 50% of their eligible brokerage portfolio value at a competitive variable rate that tracks the Federal Funds
  name: M1 Borrow
  slug: m1-borrow
- description: M1 Earn offers high-yield cash accounts for individuals and joint account holders with 3.10% APY and FDIC insurance coverage up to $4.75 million aggregate through program banks, providing a secure, hi
  name: M1 Earn
  slug: m1-earn
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/m1-finance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://m1.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.m1.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/m1finance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/m1-finance
- group: company
  title: ''
  type: Blog
  url: https://m1.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://m1.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.m1.com/
- group: other
  title: ''
  type: X
  url: https://x.com/m1finance
- group: commercial
  title: ''
  type: Plans
  url: plans/m1-finance-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/m1-finance-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/m1-finance-finops.yml
created: 2026-06-13
description: M1 Finance is an automated investing platform offering fractional share portfolio management, smart money movement, margin borrowing, and integrated banking and credit features. The platform combines self-directed and automated investing through its Pies system, commission-free trading, a portfolio line of credit (M1 Borrow), high-yield cash accounts (M1 Earn), and a rewards credit card. M1 uses a GraphQL API gateway internally across 17+ microservices built on Scala and TypeScript to power its Finance Super App experience.
finops:
- name: M1 Finance Finops
  service_category: ''
  slug: m1-finance-finops
graphqls:
- description: M1 Finance is a Finance Super App that uses a GraphQL API gateway internally across 17+ microservices built on Scala and TypeScript. The platform does not expose a public or partner-facing GraphQL API
  name: M1 Finance GraphQL API
  slug: m1-finance-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/m1-finance.png
layout: provider
modified: 2026-06-13
name: M1 Finance
nav: Providers
network: true
overview: 'M1 Finance publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Investing, Fintech, Fractional Shares, Portfolio-Management, and Robo-Advisor.


  M1 Finance''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: M1 Finance Plans Pricing
  plan_count: 1
  slug: m1-finance-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: M1 Finance Rate Limits
  slug: m1-finance-rate-limits
score:
  band: thin
  composite: 26.2
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 26.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/m1-finance/refs/heads/main/screenshots/m1-finance-2026-06-20T184822.png
security:
- kind: domain-security
  name: M1 Finance Domain Security
  slug: m1-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: m1-finance
tags:
- Investing
- Fintech
- Fractional Shares
- Portfolio-Management
- Robo-Advisor
- Margin Loans
- Banking
- Automated Investing
- Finance Super App
- Wealth Management
website: https://m1.com/
---
