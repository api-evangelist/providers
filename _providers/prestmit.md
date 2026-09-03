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
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Prestmit Agentic Access
  operation_count: 31
  slug: prestmit-agentic-access
  summary_line: 31 operations · 9 acting
api_count: 1
apis:
- description: The Prestmit Partner API allows developers to automate the buying and selling of gift cards, manage wallet balances and payouts, and integrate Prestmit transactions into their own applications. The AP
  name: Prestmit Partner API
  slug: prestmit-partner-api
- baseURL: https://api.prestmit.io
  baseurl_source: spec
  description: Manage Naira and Cedis payout bank accounts.
  name: Prestmit Bank Accounts API
  slug: prestmit-bank-accounts-api
- baseURL: https://api.prestmit.io
  baseurl_source: spec
  description: Account profile, commissions, service availability, and bank lookups.
  name: Prestmit General API
  slug: prestmit-general-api
- baseURL: https://api.prestmit.io
  baseurl_source: spec
  description: Purchase gift cards programmatically.
  name: Prestmit Gift Cards - Buy API
  slug: prestmit-gift-cards-buy-api
- baseURL: https://api.prestmit.io
  baseurl_source: spec
  description: Sell gift cards and configure payout methods.
  name: Prestmit Gift Cards - Sell API
  slug: prestmit-gift-cards-sell-api
- baseURL: https://api.prestmit.io
  baseurl_source: spec
  description: Reference data for banks, gift card categories, and payout methods.
  name: Prestmit Lookup API
  slug: prestmit-lookup-api
- baseURL: https://api.prestmit.io
  baseurl_source: spec
  description: Wallet balance and fiat withdrawal management.
  name: Prestmit Wallet API
  slug: prestmit-wallet-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Prestmit Partner Bank Accounts API
  slug: open-prestmit-bank-accounts-api
- collection_type: open
  name: Prestmit Partner Bank Accounts General API
  slug: open-prestmit-general-api
- collection_type: open
  name: Prestmit Partner Bank Accounts Gift Cards - Buy API
  slug: open-prestmit-gift-cards-buy-api
- collection_type: open
  name: Prestmit Partner Bank Accounts Gift Cards - Sell API
  slug: open-prestmit-gift-cards-sell-api
- collection_type: open
  name: Prestmit Partner Bank Accounts Lookup API
  slug: open-prestmit-lookup-api
- collection_type: open
  name: Prestmit Partner Bank Accounts Wallet API
  slug: open-prestmit-wallet-api
- collection_type: open
  name: Prestmit Partner API
  slug: open-prestmit
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prestmit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prestmit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prestmit-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prestmit
- group: start
  title: ''
  type: Portal
  url: https://prestmit.io/
- group: other
  title: ''
  type: Developers
  url: https://prestmit.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.prestmit.io/
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.prestmit.io/
- group: start
  title: ''
  type: Signup
  url: https://prestmit.io/signup
- group: start
  title: ''
  type: Login
  url: https://prestmit.io/login
- group: company
  title: ''
  type: Blog
  url: https://prestmit.io/blog
- group: operate
  title: ''
  type: Support
  url: https://prestmit.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://prestmit.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prestmit.io/privacy-policy
- group: agent
  title: ''
  type: LlmsText
  url: https://prestmit.io/llms.txt
created: '2025-02-08'
description: Prestmit is a digital trading platform that lets users buy and sell gift cards, exchange cryptocurrencies, pay bills, and purchase airtime and data. The Prestmit Partner API enables developers to programmatically buy and sell gift cards, manage wallets and payouts, and tap into Prestmits network of trusted partners and seamless transactions.
finops:
- name: Prestmit Finops
  service_category: API
  slug: prestmit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prestmit.png
layout: provider
modified: '2026-04-28'
name: Prestmit
nav: Providers
network: true
overview: 'Prestmit publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Bank Accounts API, General API, Gift Cards - Buy API, and 3 more. Tagged areas include Bills, Crypto, Fintech, Gift Cards, and Payments.


  Prestmit''s developer surface includes authentication, developer portal, documentation, sandbox, signup flow, engineering blog, support, and 8 more developer resources.'
plans:
- name: Prestmit Plans Pricing
  plan_count: 3
  slug: prestmit-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Prestmit Rate Limits
  slug: prestmit-rate-limits
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 39.3
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prestmit/refs/heads/main/screenshots/prestmit-2026-06-20T192051.png
security:
- kind: authentication
  name: Prestmit Authentication
  slug: prestmit-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Prestmit Domain Security
  slug: prestmit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: prestmit
tags:
- Bills
- Crypto
- Fintech
- Gift Cards
- Payments
website: https://prestmit.io/
---
