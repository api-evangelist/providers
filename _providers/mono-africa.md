---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Mono Africa Agentic Access
  operation_count: 19
  slug: mono-africa-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 6
apis:
- description: Account linking authorization and re-authorization.
  name: Mono Connect API
  slug: mono-africa-connect-api
- description: Affordability and credit-decisioning analysis.
  name: Mono Creditworthiness API
  slug: mono-africa-creditworthiness-api
- description: Direct bank payment collection.
  name: Mono DirectPay API
  slug: mono-africa-directpay-api
- description: Read financial data from a linked account.
  name: Mono Financial Data API
  slug: mono-africa-financial-data-api
- description: Investment holdings for a linked account.
  name: Mono Investment API
  slug: mono-africa-investment-api
- description: Identity and data verification for KYC/KYB.
  name: Mono Lookup API
  slug: mono-africa-lookup-api
artifact_total: 13
collections:
- collection_type: open
  name: Mono API
  slug: open-mono-africa
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mono-africa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mono-africa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mono-africa-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withmono
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/withmono
- group: company
  title: ''
  type: Website
  url: https://mono.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mono.co
- group: commercial
  title: ''
  type: Plans
  url: plans/mono-africa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mono-africa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mono-africa-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://mono.co/blog
created: '2026-07-12'
description: Mono is an open banking and financial data infrastructure company for Africa (often described as the "Plaid for Africa"), headquartered in Lagos, Nigeria and now part of Flutterwave. Its REST APIs let businesses link customer bank accounts and retrieve financial data (accounts, transactions, identity, income, balance, statements, assets, earnings), assess creditworthiness, collect direct bank payments via DirectPay (direct debit), and verify identity data (BVN, NIN, CAC, account numbers) through the Lookup services. Server-to-server calls authenticate with a secret key sent in the `mono-sec-key` header, and account linking is completed through the hosted Mono Connect widget.
finops:
- name: Mono Africa Finops
  service_category: Financial Infrastructure and Open Banking
  slug: mono-africa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mono-africa.png
layout: provider
modified: '2026-07-12'
name: Mono
nav: Providers
network: true
overview: 'Mono publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Connect API, Creditworthiness API, DirectPay API, and 3 more. Tagged areas include Open Banking, Financial Data, Payments, Fintech, and Account Linking.


  Mono''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Mono Africa Plans Pricing
  plan_count: 3
  slug: mono-africa-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 3
  name: Mono Africa Rate Limits
  slug: mono-africa-rate-limits
score:
  band: thin
  composite: 33.9
  delta: -5.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 47.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 20.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Mono Africa Authentication
  slug: mono-africa-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mono Africa Domain Security
  slug: mono-africa-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mono-africa
tags:
- Open Banking
- Financial Data
- Payments
- Fintech
- Account Linking
- Direct Debit
- Bank Data
- Africa
- Nigeria
- Financial Infrastructure
website: https://mono.co/
---
