---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-11-06'
api_count: 7
apis:
- baseURL: https://pago.qit.nu/checkout/merchantapi
  baseurl_source: declared
  description: The BackwardsCompatibilityCheck API from Qliro — 1 operation(s) for backwardscompatibilitycheck.
  name: Qliro Backwards Compatibility Check API
  slug: qliro-backwardscompatibilitycheck-api
- baseURL: https://pago.qit.nu/checkout/merchantapi
  baseurl_source: declared
  description: The CreditCheckInformation API from Qliro — 1 operation(s) for creditcheckinformation.
  name: Qliro Credit Check Information API
  slug: qliro-creditcheckinformation-api
- baseURL: https://pago.qit.nu/checkout/merchantapi
  baseurl_source: declared
  description: The InStore API from Qliro — 2 operation(s) for instore.
  name: Qliro In Store API
  slug: qliro-instore-api
- baseURL: https://pago.qit.nu/checkout/merchantapi
  baseurl_source: declared
  description: The MerchantCreditCard API from Qliro — 2 operation(s) for merchantcreditcard.
  name: Qliro Merchant Credit Card API
  slug: qliro-merchantcreditcard-api
- baseURL: https://pago.qit.nu/checkout/merchantapi
  baseurl_source: declared
  description: The PaymentOptions API from Qliro — 1 operation(s) for paymentoptions.
  name: Qliro Payment Options API
  slug: qliro-paymentoptions-api
- baseURL: https://pago.qit.nu/checkout/merchantapi
  baseurl_source: declared
  description: The PaymentWidget API from Qliro — 2 operation(s) for paymentwidget.
  name: Qliro Payment Widget API
  slug: qliro-paymentwidget-api
- baseURL: https://pago.qit.nu/checkout/merchantapi
  baseurl_source: declared
  description: The Upsell API from Qliro — 1 operation(s) for upsell.
  name: Qliro Upsell API
  slug: qliro-upsell-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/qliro/llms/qliro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qliro-llms.txt
- group: auth
  href: https://artifacts.apis.io/qliro/well-known/qliro-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/qliro-status-security.txt
- group: auth
  href: https://artifacts.apis.io/qliro/well-known/qliro-se-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/qliro-se-support-security.txt
- group: agent
  href: https://artifacts.apis.io/qliro/well-known/qliro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/qliro-well-known.yml
- group: other
  href: https://artifacts.apis.io/qliro/hosts/qliro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qliro-hosts.yml
- group: other
  href: https://artifacts.apis.io/qliro/vendors/qliro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qliro-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qliro.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://qliro.com/composable-payouts/price-list-for-currency-conversion-and-currencies
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Qliro
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.qliro.com/
- group: auth
  href: https://artifacts.apis.io/qliro/security/qliro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qliro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qliro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://qliro.com/for-merchants
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qliro.com/hubfs/New%20website%20-%20Privacy%20policy/Privacy%20Policy%20-%20Qliro.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qliro.com/sv/for-shoppare-villkor
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://qliro.com/mcp
  - status: 403
    url: https://assets.qliro.com/mcp
  - status: 200
    url: https://qliro.com/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Qliro provides flexible payment solutions for online and in‑store shoppers and merchants across Scandinavia. It offers “Buy now, pay later”, installment plans, and a consumer‑focused app, supporting multiple languages and currencies. The platform emphasizes secure, fast checkout experiences and integrates with e‑commerce merchants to boost conversion.
image: https://qliro.com/hubfs/Feature_B2CHomepage.png
layout: provider
modified: '2026-10-15'
name: Qliro
nav: Providers
network: true
overview: 'Qliro is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Backwards Compatibility Check API, Credit Check Information API, In Store API, and 4 more. Tagged areas include Company, Payments, Fintech, Buy Now Pay Later, and E-Commerce.


  The Qliro catalog on APIs.io includes 1 Spectral governance ruleset.


  Qliro''s developer surface includes pricing, documentation, and 13 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Qliro API Rules
  rule_count: 41
  severity_counts:
    error: 33
    hint: 0
    info: 4
    warn: 4
  slug: qliro-rules
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 44.0
    developer_ergonomics: 9.5
    discoverability: 69.6
    operational_transparency: 21.1
  previous_composite: 32.1
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/qliro/qliro-2026-11-03T141758.png
security:
- kind: domain-security
  name: Qliro Domain Security
  slug: qliro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qliro
tags:
- Company
- Payments
- Fintech
- Buy Now Pay Later
- E-Commerce
website: https://qliro.com/
---
