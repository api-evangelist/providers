---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
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
  scored_at: '2026-08-10'
api_count: 5
apis:
- description: REST API for managing KakaoBank accounts including demand deposits, savings accounts, and group accounts. Provides access to account balances, transaction history, and account holder information for a
  name: KakaoBank Account Management API
  slug: account-management-api
- description: REST API enabling fund transfers between KakaoBank accounts and external bank accounts within South Korea's open banking network. Supports peer-to-peer transfers, interbank transfers, and overseas rem
  name: KakaoBank Transfer API
  slug: transfer-api
- description: REST API for loan origination and management including credit loans, business owner credit loans, and housing-related loans. Provides programmatic access to loan applications, repayment schedules, and
  name: KakaoBank Loan API
  slug: loan-api
- description: 'REST API providing alternative credit scoring capabilities powered by KakaoBank''s data-driven credit models. Integrates with partners such as NICE Credit to assess creditworthiness beyond traditional '
  name: KakaoBank Credit Scoring API
  slug: credit-scoring-api
- description: REST API connecting to South Korea's national open banking switchboard, enabling aggregated views of balances and transactions from multiple financial institutions. Supports real-time multi-account in
  name: KakaoBank Open Banking API
  slug: open-banking-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kakaobank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kakaobank.com
- group: docs
  title: ''
  type: Documentation
  url: https://eng.kakaobank.com/products
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/kakaobank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kakaobank
- group: company
  title: ''
  type: Blog
  url: https://tech.kakaobank.com
- group: commercial
  title: ''
  type: Pricing
  url: https://eng.kakaobank.com/products
- group: operate
  title: ''
  type: StatusPage
  url: https://www.kakaobank.com
- group: other
  title: ''
  type: X
  url: https://x.com/kakaobank
- group: commercial
  title: ''
  type: Plans
  url: plans/kakaobank-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kakaobank-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kakaobank-finops.yml
created: '2026-06-13'
description: KakaoBank is South Korea's leading internet-only bank, offering REST APIs for account management, fund transfers, loans, credit scoring, and open banking data connectivity for the Korean market. Founded in 2016 and backed by Kakao Corp., KakaoBank serves over 26 million customers through a fully mobile and API-first digital banking platform.
finops:
- name: Kakaobank Finops
  service_category: ''
  slug: kakaobank-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kakaobank.png
layout: provider
modified: '2026-06-13'
name: KakaoBank
nav: Providers
network: true
overview: 'KakaoBank publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Finance, Open Banking, Korea, and Fintech.


  KakaoBank''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Kakaobank Plans Pricing
  plan_count: 3
  slug: kakaobank-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Kakaobank Rate Limits
  slug: kakaobank-rate-limits
score:
  band: emerging
  composite: 23.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 23.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kakaobank/refs/heads/main/screenshots/kakaobank-2026-06-20T183912.png
security:
- kind: domain-security
  name: Kakaobank Domain Security
  slug: kakaobank-domain-security
  summary_line: TLSv1.2 · HSTS
slug: kakaobank
tags:
- Banking
- Finance
- Open Banking
- Korea
- Fintech
- Account Management
- Transfers
- Loans
- Credit Scoring
- Mobile Banking
website: https://www.kakaobank.com
---
