---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Coingate Agentic Access
  operation_count: 10
  slug: coingate-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.coingate.com/v2
  baseurl_source: declared
  description: Convert between currencies in ledger accounts
  name: CoinGate Conversions API
  slug: coingate-conversions-api
- baseURL: https://api.coingate.com/v2
  baseurl_source: declared
  description: Retrieve supported currencies and platforms
  name: CoinGate Currencies API
  slug: coingate-currencies-api
- baseURL: https://api.coingate.com/v2
  baseurl_source: declared
  description: Create and manage payment orders
  name: CoinGate Orders API
  slug: coingate-orders-api
- baseURL: https://api.coingate.com/v2
  baseurl_source: declared
  description: Process order refunds
  name: CoinGate Refunds API
  slug: coingate-refunds-api
- baseURL: https://api.coingate.com/v2
  baseurl_source: declared
  description: Send cryptocurrency payouts to beneficiaries
  name: CoinGate Send Requests API
  slug: coingate-send-requests-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CoinGate Payment Gateway Conversions API
  slug: open-coingate-conversions-api
- collection_type: open
  name: CoinGate Payment Gateway Conversions Currencies API
  slug: open-coingate-currencies-api
- collection_type: open
  name: CoinGate Payment Gateway Conversions Orders API
  slug: open-coingate-orders-api
- collection_type: open
  name: CoinGate Payment Gateway Conversions Refunds API
  slug: open-coingate-refunds-api
- collection_type: open
  name: CoinGate Payment Gateway Conversions Send Requests API
  slug: open-coingate-send-requests-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coingate-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coingate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coingate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coingate-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://coingate.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.coingate.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.coingate.com/reference/cryptocurrency-payment-api
- group: docs
  title: ''
  type: Documentation
  url: https://developer.coingate.com/docs/api-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://coingate.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://coingate.com/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/coingate
- group: build
  title: ''
  type: SDKs
  url: https://github.com/coingate/coingate-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/coingate/coingate-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/coingate/coingate-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/coingate/coingate-ruby
- group: start
  title: ''
  type: Signup
  url: https://coingate.com/register
- group: start
  title: ''
  type: Login
  url: https://coingate.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coingate.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coingate.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coingate.com
- group: operate
  title: ''
  type: Support
  url: https://coingate.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.coingate.com
created: '2026-06-13'
description: CoinGate is a cryptocurrency payment gateway providing REST APIs for creating and managing payment orders, processing crypto-to-fiat conversions, automating payouts, managing merchant ledger accounts, and accessing billing and reporting data. Merchants can accept 70+ cryptocurrencies and settle in fiat or crypto, with integrations available via hosted checkout, plugins, and direct API.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://coingate.com/images/coingate-logo.png
layout: provider
modified: '2026-06-13'
name: CoinGate
nav: Providers
network: true
overview: 'CoinGate publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Conversions API, Currencies API, Orders API, and 2 more. Tagged areas include Cryptocurrency, Payments, Payment Gateway, Crypto, and Fintech.


  CoinGate''s developer surface includes authentication, API reference, documentation, pricing, engineering blog, GitHub presence, signup flow, and 15 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 2
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 11
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 56.6
    commercial_clarity: 56.6
    contract_governance: 0.0
    contract_quality: 56.6
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coingate/refs/heads/main/screenshots/coingate-2026-06-20T174732.png
security:
- kind: authentication
  name: Coingate Authentication
  slug: coingate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Coingate Domain Security
  slug: coingate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coingate Vulnerability Disclosure
  slug: coingate-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: coingate
tags:
- Cryptocurrency
- Payments
- Payment Gateway
- Crypto
- Fintech
- Bitcoin
- Ethereum
- Merchant Services
website: https://coingate.com
---
