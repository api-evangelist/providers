---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-11-06'
api_count: 8
apis:
- description: Banking-as-a-Service JSON-RPC 2.0 API that lets partners embed payments, transfers and account and card operations inside Uzbekistan's national payment system. Covers account balance, history and atta
  name: Uzum BaaS Payment Hub
  slug: uzum-payment-hub-baas
- description: Seller-cabinet API for Uzum Market used to synchronise marketplace orders, inventory and prices for both Fulfilment by Operator (FBO) and Fulfilment by Seller (FBS) models. Access requires an API toke
  name: Uzum Market Seller API
  slug: uzum-market-seller
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: The API MFO API from Uzum — 8 operation(s) for api mfo.
  name: Uzum API MFO API
  slug: uzum-api-mfo-api
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: The Auxiliary Methods API from Uzum — 4 operation(s) for auxiliary methods.
  name: Uzum Auxiliary Methods API
  slug: uzum-auxiliary-methods-api
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: The Back-to-back Payment API from Uzum — 1 operation(s) for back-to-back payment.
  name: Uzum Back-to-back Payment API
  slug: uzum-back-to-back-payment-api
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: This method allows you to check the basic functionality and availability of the fiscalization service.
  name: Uzum Check Service Status API
  slug: uzum-check-service-status-api
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: The Common methods API from Uzum — 5 operation(s) for common methods.
  name: Uzum Common methods API
  slug: uzum-common-methods-api
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: Methods for cross-border payments for services in Uzbekistan
  name: Uzum Cross-border payments API
  slug: uzum-cross-border-payments-api
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: In this section, the API provides methods for working with fiscal receipts. `/v2/receipt` method allows you to register a sale operation and generate a fiscal receipt that complies with all legal requ
  name: Uzum Fiscalization API
  slug: uzum-fiscalization-api
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: Methods for transfers from Uzbekistan
  name: Uzum From Uzbekistan API
  slug: uzum-from-uzbekistan-api
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: Auxiliary Information Methods
  name: Uzum Information retrieval API
  slug: uzum-information-retrieval-api
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: The Managing Credit Cards Bindings API from Uzum — 3 operation(s) for managing credit cards bindings.
  name: Uzum Managing Credit Cards Bindings API
  slug: uzum-managing-credit-cards-bindings-api
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: QR CRM methods that are used to create an order, check the status of the order and transfer links to the fiscal receipt and cancel payment transactions.
  name: Uzum Methods API
  slug: uzum-methods-api
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: The One-Step Payment API from Uzum — 2 operation(s) for one-step payment.
  name: Uzum One-Step Payment API
  slug: uzum-one-step-payment-api
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: The partner API from Uzum — 2 operation(s) for partner.
  name: Uzum Partner API
  slug: uzum-partner-api
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: 'The method is designed to send information about payments made using QR codes directly to the tax authority. Using this method allows automating the fiscalization process for payments made at offline '
  name: Uzum Submit QR Code Payment Receipt to Tax Authorities API
  slug: uzum-submit-qr-code-payment-receipt-to-tax-authorities-api
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: Methods for transfers to Uzbekistan
  name: Uzum To Uzbekistan API
  slug: uzum-to-uzbekistan-api
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: Methods used in the transfer process
  name: Uzum Transfer process API
  slug: uzum-transfer-process-api
- baseURL: https://crossborder.transfer.uz
  baseurl_source: declared
  description: The Two-Step Payment API from Uzum — 2 operation(s) for two-step payment.
  name: Uzum Two-Step Payment API
  slug: uzum-two-step-payment-api
artifact_total: 32
asyncapis:
- description: ''
  name: Uzum Merchant Webhooks
  slug: uzum-merchant-webhooks
common:
- group: other
  href: https://artifacts.apis.io/uzum/capabilities/uzum-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/uzum-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://uzum.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.uzumbank.uz/en/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uzumbank.uz/en/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.uzumbank.uz/en/checkout
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.uzumbank.uz/en/paymenthub/testing/getting-started/
- group: start
  title: ''
  type: SignUp
  url: https://merchants.uzumbank.uz/en/
- group: company
  title: ''
  type: Blog
  url: https://uzum.com/en/press-center/news-and-press-releases/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uzum.com/en/privacy-and-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uzum.com/en/privacy-and-terms/
- group: operate
  title: ''
  type: Support
  url: https://uzum.com/en/contacts/
- group: build
  title: ''
  type: Postman
  url: https://developer.uzumbank.uz/remitcore/remitcore_postman_collection_credit.json
- group: build
  href: https://artifacts.apis.io/uzum/packages/uzum-packages.yml
  title: ''
  type: Packages
  url: packages/uzum-packages.yml
- group: agent
  href: https://artifacts.apis.io/uzum/mcp/uzum-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/uzum-mcp.yml
- group: agent
  href: https://artifacts.apis.io/uzum/llms/uzum-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/uzum-llms.txt
- group: other
  href: https://artifacts.apis.io/uzum/overlays/uzum-checkout-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/uzum-checkout-overlay.yaml
- group: design
  href: https://artifacts.apis.io/uzum/conformance/uzum-conformance.yml
  title: ''
  type: Conformance
  url: conformance/uzum-conformance.yml
- group: auth
  href: https://artifacts.apis.io/uzum/conformance/uzum-conformance.yml
  title: ''
  type: Compliance
  url: conformance/uzum-conformance.yml
- group: design
  href: https://artifacts.apis.io/uzum/errors/uzum-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/uzum-problem-types.yml
- group: build
  href: https://artifacts.apis.io/uzum/errors/uzum-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/uzum-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/uzum/lifecycle/uzum-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/uzum-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/uzum/authentication/uzum-authentication.yml
  title: ''
  type: Authentication
  url: authentication/uzum-authentication.yml
- group: auth
  href: https://artifacts.apis.io/uzum/security/uzum-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uzum-domain-security.yml
- group: start
  href: https://artifacts.apis.io/uzum/sandbox/uzum-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/uzum-sandbox.yml
- group: design
  href: https://artifacts.apis.io/uzum/conventions/uzum-conventions.yml
  title: ''
  type: Conventions
  url: conventions/uzum-conventions.yml
- group: operate
  href: https://artifacts.apis.io/uzum/changelog/uzum-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/uzum-changelog.yml
- group: design
  href: https://artifacts.apis.io/uzum/data-model/uzum-data-model.yml
  title: ''
  type: DataModel
  url: data-model/uzum-data-model.yml
- group: design
  href: https://artifacts.apis.io/uzum/asyncapi/uzum-merchant-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/uzum-merchant-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/uzum/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/uzum/plans/uzum-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/uzum-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/uzum/rate-limits/uzum-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/uzum-rate-limits.yml
created: '2026-09-02'
description: 'Uzum is an Uzbekistan-based digital ecosystem headquartered in Tashkent that bundles e-commerce, fintech and digital banking into a single group: Uzum Market (the country''s largest online marketplace), Uzum Tezkor (rapid food and grocery delivery), Uzum Bank (a licensed digital bank), and Uzum Nasiya (consumer BNPL / installment lending). Its developer-facing API surface is published by Uzum Bank at developer.uzumbank.uz, where nine OpenAPI contracts and a JSON-RPC 2.0 Banking-as-a-Service hub cover card acquiring (Uzum Checkout), QR and cash-register payments (Uzum Fast Pay, Dynamic QR), tax receipt fiscalization to the Uzbek State Tax Committee (Uzum Fiscalization), inbound and outbound cross-border money transfer (Uzum CrossBorder Transfer, Remit Core), installment contract origination (Uzum Nasiya Partner API), in-app merchant billing (Merchant API webhooks) and FX rate quoting (RateKeeper). Uzum Market additionally operates a seller-cabinet API at api-seller.uzum.uz for
  FBO/FBS order, inventory and price synchronization, which is credential-gated. All Uzum Bank API programs are onboarded through an account manager rather than self-service signup.'
finops:
- has_sources: true
  method: derived
  name: Uzum Finops
  primary_unit: ''
  service_category: ''
  slug: uzum-finops
  template: true
image: https://developer.uzumbank.uz/en/img/logo.svg
layout: provider
modified: '2026-09-02'
name: Uzum
nav: Providers
network: true
overview: 'Uzum publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including API MFO API, Auxiliary Methods API, Back-to-back Payment API, and 16 more. Tagged areas include Company, Payments, Banking, Financial Services, and E-Commerce.


  The Uzum catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Uzum''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, support, authentication, and 24 more developer resources.'
plans:
- name: Uzum Plans Pricing
  plan_count: 0
  slug: uzum-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Uzum Rate Limits
  slug: uzum-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Uzum API Rules
  rule_count: 54
  severity_counts:
    error: 32
    hint: 0
    info: 5
    warn: 17
  slug: uzum-rules
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 53.1
    developer_ergonomics: 57.7
    discoverability: 71.4
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - uzbekistan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 47.9
  provenance:
    conformance: derived
    contracts:
      callable: 17.6
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/uzum/uzum-2026-10-11T131542.png
security:
- kind: authentication
  name: Uzum Authentication
  slug: uzum-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Uzum Domain Security
  slug: uzum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 6
skills:
- name: uzum-accept-card-payment
  slug: uzum-accept-card-payment
- name: uzum-fiscalize-a-receipt
  slug: uzum-fiscalize-a-receipt
- name: uzum-offer-installments
  slug: uzum-offer-installments
- name: uzum-receive-in-app-payments
  slug: uzum-receive-in-app-payments
- name: uzum-send-cross-border-transfer
  slug: uzum-send-cross-border-transfer
- name: uzum-take-qr-payment-at-pos
  slug: uzum-take-qr-payment-at-pos
slug: uzum
tags:
- Company
- Payments
- Banking
- Financial Services
- E-Commerce
- Marketplace
- Money Transfer
- Remittances
- Buy Now Pay Later
- Acquiring
- QR Payments
- Fiscalization
- Banking as a Service
- Uzbekistan
- Central Asia
website: https://uzum.com/en/
---
