---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-10-17'
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
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/prestmit/refs/heads/main/plans/prestmit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/prestmit-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/prestmit/refs/heads/main/rate-limits/prestmit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/prestmit-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/prestmit/refs/heads/main/finops/prestmit-finops.yml
  title: ''
  type: FinOps
  url: finops/prestmit-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.prestmit.io/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/prestmit/refs/heads/main/agentic-access/prestmit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/prestmit-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/prestmit/refs/heads/main/security/prestmit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prestmit-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/prestmit/refs/heads/main/authentication/prestmit-authentication.yml
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
- has_sources: false
  method: generated
  name: Prestmit Finops
  primary_unit: ''
  service_category: API
  slug: prestmit-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prestmit.png
layout: provider
modified: '2026-04-28'
name: Prestmit
nav: Providers
network: true
overview: 'Prestmit publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bank Accounts API, General API, Gift Cards - Buy API, and 4 more. Tagged areas include Bills, Cryptocurrency, Fintech, Gift Cards, and Payments.


  Prestmit''s developer surface includes authentication, developer portal, documentation, sandbox, signup flow, engineering blog, support, and 12 more developer resources.'
plans:
- name: Prestmit Plans Pricing
  plan_count: 3
  slug: prestmit-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Prestmit Rate Limits
  slug: prestmit-rate-limits
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 14.5
    contract_governance: 0.0
    contract_quality: 45.3
    developer_ergonomics: 39.3
    discoverability: 64.3
    operational_transparency: 7.9
  previous_composite: 29.1
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
    score: 10.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Cryptocurrency
- Fintech
- Gift Cards
- Payments
website: https://www.prestmit.io/
---
