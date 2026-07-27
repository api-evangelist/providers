---
access_model:
  confidence: high
  label: No first-party API · Aggregator-only data access (Plaid)
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - developer-portal-probe
  - aggregator-posture
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Current does not expose a first-party public API or developer portal. The only documented, programmatic path to a member's Current account data (balances, transaction history, account and identity det
  name: Current Consumer Data Access (Aggregator-Only)
  slug: current-data-access
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://current.com/
- group: operate
  title: ''
  type: Support
  url: https://support.current.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://current.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://current.com/terms_of_service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://current.com/docs/current_privacy_policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/current
- group: auth
  title: ''
  type: DomainSecurity
  url: security/current-domain-security.yml
created: '2026-07-17'
description: Current (Finco Services, Inc.) is a New York City-based U.S. financial technology company operating a mobile-first consumer banking platform serving over six million members. Through partner banks Choice Financial Group and Cross River Bank it offers fee-free spending accounts with early direct deposit (up to two days early), fee-free overdraft, and paycheck advances; Savings Pods earning competitive APY with automated Round-Ups; the Build Card for responsible credit building without a traditional credit check; fee-free cryptocurrency trading; and teen banking accounts with parental controls and automatic allowances. Current is a technology company, not a bank. It does NOT publish a first-party public developer API or developer portal — no developer.current.com (does not resolve), current.com/developers and current.com/api return 404, and api.current.com is an undocumented mobile-app backend. Programmatic access to member account data is available only through third-party open-finance
  aggregators (Plaid), on a consumer-permissioned basis. This profile captures the company's public web, legal, and security surface and its aggregator-only data-access posture.
image: https://cdn.current.com/images/brochure-site/canonical-og-2024.jpg
layout: provider
modified: '2026-07-23'
name: Current
nav: Providers
network: true
overview: 'Current publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Neobank, Consumer Banking, and Personal Finance.


  Current''s developer surface includes support, engineering blog, and 5 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 16.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.1
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 30.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/current/refs/heads/main/screenshots/current-2026-07-25T210948.png
security:
- kind: domain-security
  name: Current Domain Security
  slug: current-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: current
tags:
- Company
- Fintech
- Neobank
- Consumer Banking
- Personal Finance
- Payments
- Credit Building
- Savings
- Mobile Banking
- United States
- Open Finance
- Aggregator Access
website: https://current.com/
---
