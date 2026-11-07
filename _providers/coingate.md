---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Coingate Agentic Access
  operation_count: 10
  slug: coingate-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 2
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
- baseURL: https://api.coingate.com/api/v2
  baseurl_source: declared
  description: The Beneficiaries API from CoinGate — 2 operation(s) for beneficiaries.
  name: CoinGate Beneficiaries API
  slug: coingate-beneficiaries-api
- baseURL: https://api.coingate.com/api/v2
  baseurl_source: declared
  description: The Beneficiary Payout Settings API from CoinGate — 1 operation(s) for beneficiary payout settings.
  name: CoinGate Beneficiary Payout Settings API
  slug: coingate-beneficiary-payout-settings-api
- baseURL: https://api.coingate.com/api/v2
  baseurl_source: declared
  description: The Billing API from CoinGate — 9 operation(s) for billing.
  name: CoinGate Billing API
  slug: coingate-billing-api
- baseURL: https://api.coingate.com/api/v2
  baseurl_source: declared
  description: The Contacts API from CoinGate — 3 operation(s) for contacts.
  name: CoinGate Contacts API
  slug: coingate-contacts-api
- baseURL: https://api.coingate.com/api/v2
  baseurl_source: declared
  description: The Countries API from CoinGate — 2 operation(s) for countries.
  name: CoinGate Countries API
  slug: coingate-countries-api
- baseURL: https://api.coingate.com/api/v2
  baseurl_source: declared
  description: The Deposits API from CoinGate — 1 operation(s) for deposits.
  name: CoinGate Deposits API
  slug: coingate-deposits-api
- baseURL: https://api.coingate.com/api/v2
  baseurl_source: declared
  description: The Industries API from CoinGate — 1 operation(s) for industries.
  name: CoinGate Industries API
  slug: coingate-industries-api
- baseURL: https://api.coingate.com/api/v2
  baseurl_source: declared
  description: The Invoice API from CoinGate — 2 operation(s) for invoice.
  name: CoinGate Invoice API
  slug: coingate-invoice-api
- baseURL: https://api.coingate.com/api/v2
  baseurl_source: declared
  description: The Ledger API from CoinGate — 7 operation(s) for ledger.
  name: CoinGate Ledger API
  slug: coingate-ledger-api
- baseURL: https://api.coingate.com/api/v2
  baseurl_source: declared
  description: The Mass Payouts API from CoinGate — 6 operation(s) for mass payouts.
  name: CoinGate Mass Payouts API
  slug: coingate-mass-payouts-api
- baseURL: https://api.coingate.com/api/v2
  baseurl_source: declared
  description: The New Endpoint API from CoinGate — 1 operation(s) for new endpoint.
  name: CoinGate New Endpoint API
  slug: coingate-new-endpoint-api
- baseURL: https://api.coingate.com/api/v2
  baseurl_source: declared
  description: The Payment Channels API from CoinGate — 4 operation(s) for payment channels.
  name: CoinGate Payment Channels API
  slug: coingate-payment-channels-api
- baseURL: https://api.coingate.com/api/v2
  baseurl_source: declared
  description: The Payout Links API from CoinGate — 3 operation(s) for payout links.
  name: CoinGate Payout Links API
  slug: coingate-payout-links-api
- baseURL: https://api.coingate.com/api/v2
  baseurl_source: declared
  description: The Ping API from CoinGate — 1 operation(s) for ping.
  name: CoinGate Ping API
  slug: coingate-ping-api
- baseURL: https://api.coingate.com/api/v2
  baseurl_source: declared
  description: The Platforms API from CoinGate — 2 operation(s) for platforms.
  name: CoinGate Platforms API
  slug: coingate-platforms-api
- baseURL: https://api.coingate.com/api/v2
  baseurl_source: declared
  description: The Rates API from CoinGate — 2 operation(s) for rates.
  name: CoinGate Rates API
  slug: coingate-rates-api
artifact_total: 35
collections:
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
- group: other
  href: https://artifacts.apis.io/coingate/capabilities/coingate-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/coingate-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/coingate/plans/plans.yml
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  href: https://artifacts.apis.io/coingate/rate-limits/rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/coingate/finops/finops.yml
  title: ''
  type: FinOps
  url: finops/finops.yml
- group: agent
  href: https://artifacts.apis.io/coingate/agentic-access/coingate-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coingate-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/coingate/security/coingate-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coingate-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/coingate/security/coingate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coingate-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/coingate/authentication/coingate-authentication.yml
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
- has_sources: true
  method: derived
  name: Finops
  primary_unit: transaction
  service_category: ''
  slug: finops
  template: false
image: https://coingate.com/images/coingate-logo.png
layout: provider
modified: '2026-06-13'
name: CoinGate
nav: Providers
network: true
overview: 'CoinGate publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Conversions API, Currencies API, Orders API, and 18 more. Tagged areas include Cryptocurrency, Payments, Payment Gateway, Fintech, and Bitcoin.


  The CoinGate catalog on APIs.io includes 1 Spectral governance ruleset.


  CoinGate''s developer surface includes authentication, API reference, documentation, pricing, engineering blog, GitHub presence, signup flow, and 19 more developer resources.'
plans:
- name: Coingate Price Estimates
  plan_count: 0
  slug: coingate-price-estimates
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 2
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: CoinGate API Rules
  rule_count: 55
  severity_counts:
    error: 41
    hint: 0
    info: 4
    warn: 10
  slug: coingate-rules
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.7
  facets:
    access_clarity: 35.5
    contract_governance: 13.6
    contract_quality: 46.0
    developer_ergonomics: 57.1
    discoverability: 66.1
    operational_transparency: 47.4
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/coingate/coingate-2026-06-20T174732.png
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
- Fintech
- Bitcoin
- Ethereum
- Merchant Services
website: https://coingate.com
---
