---
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/novo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/novo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://novo.co
- group: operate
  title: ''
  type: Support
  url: https://novo.co/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://novo.co/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://novo.co/legal
- group: company
  title: ''
  type: Blog
  url: https://novo.co/learn
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/banknovo
- group: docs
  title: ''
  type: Documentation
  url: https://plaid.com/institutions/novo/
- group: start
  title: ''
  type: SignUp
  url: https://app.novo.co/signup
- group: start
  title: ''
  type: GettingStarted
  url: https://www.novo.co/get-started
- group: auth
  title: ''
  type: Compliance
  url: https://trust.novo.co/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/novo-llms.txt
created: '2026-07-23'
description: Novo is a New York- and Miami-based financial technology company, founded in 2016, that operates a digital business-banking platform for small businesses, entrepreneurs, and freelancers. Novo is not itself a chartered bank; it is a service provider to Middlesex Federal Savings, F.A. (Member FDIC), which holds the deposits and provides the underlying banking products accessed through Novo's app. The platform offers fee-free business checking, invoicing, Novo Reserves, expense management, a business debit/credit card, working-capital funding, and inbound integrations with tools like QuickBooks, Stripe, Shopify, and Wise. On open-finance posture, Novo publishes no first-party public developer API and runs no developer portal; consumer-permissioned account data (Auth, Balance, Identity, Transactions) is reached by third parties only through the Plaid aggregator. No documented FDX participation or CFPB Section 1033 data-access commitment is published as of this review.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Novo
nav: Providers
network: true
overview: 'Novo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, Neobank, and Small Business Banking.


  Novo''s developer surface includes support, engineering blog, documentation, signup flow, getting-started guide, and 8 more developer resources.'
random_paper: 102
score:
  band: emerging
  composite: 21.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 24.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/novo/refs/heads/main/screenshots/novo-2026-08-07T185621.png
security:
- kind: domain-security
  name: Novo Domain Security
  slug: novo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Novo Trust Center
  slug: novo-trust-center
  summary_line: SOC 2
slug: novo
tags:
- Financial Services
- Banking
- United States
- Neobank
- Small Business Banking
- Fintech
- Open Finance
- Data Aggregation
website: https://novo.co
---
