---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: The WorldFirst Enterprise Solution (World Account) API — a RESTful, JSON, signed-request interface covering customer onboarding, account and beneficiary management, statements, foreign exchange, trans
  name: WorldFirst Enterprise Solution API
  slug: worldfirst-enterprise-solution-api
- description: 'The WorldFirst Pay Solution (Cashier Payment) API lets overseas e-commerce merchants accept payments through a hosted checkout: create a payment order, let the customer complete payment, inquire about'
  name: WorldFirst Pay Solution API
  slug: worldfirst-pay-solution-api
- description: The WorldTrade Solution API supports cross-border trade transactions between partners and the WorldFirst platform — e.g. inquiryQuotes (FX quote lookup at /amsin/api/v1/payments/inquiryQuotes), create
  name: WorldFirst WorldTrade Solution API
  slug: worldfirst-worldtrade-solution-api
artifact_total: 6
asyncapis:
- description: ''
  name: Worldfirst Webhooks
  slug: worldfirst-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/worldfirst-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.worldfirst.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.worldfirst.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.worldfirst.com/docs/alipay-worldfirst/overview/home
- group: docs
  title: ''
  type: APIReference
  url: https://developers.worldfirst.com/docs/alipay-worldfirst/overview/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.worldfirst.com/docs/alipay-worldfirst/cashier_payment/getting_started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.worldfirst.com/uk/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.worldfirst.com/uk/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.worldfirst.com/uk/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.worldfirst.com/uk/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/world-first
- group: start
  title: ''
  type: SignUp
  url: https://portal.worldfirst.com/register?lang=en-GB&region=global
- group: start
  title: ''
  type: Login
  url: https://portal.worldfirst.com/login?lang=en-GB&region=global
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.worldfirst.com/help-center/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/worldfirst-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/worldfirst-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/worldfirst-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/worldfirst-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/worldfirst-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/worldfirst-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/worldfirst-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/worldfirst-conformance.yml
created: '2026-07-24'
description: 'WorldFirst is a United Kingdom-founded cross-border payments and money-movement company, headquartered in London and owned by Ant Group (Alipay) since 2019. It gives online sellers, marketplaces, and SMEs a multi-currency World Account to collect, hold, convert, and send money across borders, alongside a World Card for multi-currency spending and marketplace/supplier payouts. Its home market is the United Kingdom, but its book is global e-commerce and cross-border trade, serving merchants selling on Amazon and other marketplaces. WorldFirst ships a genuine, API-native developer platform at developers.worldfirst.com built on Ant Group''s Antom-style gateway (open-sea/open-eu/open-na hosts, /amsin/api/v1 paths): a RESTful, JSON, HTTPS-only interface segmented into an Enterprise Solution (account, beneficiary, FX, transfer, payout, invoicing, virtual-card credit), a Pay Solution (Cashier Payment / online checkout acceptance for merchants), and a WorldTrade Solution (cross-border
  trade orders). Requests are secured with RSA256/ECC224 digital signatures plus OAuth 2.0 access tokens; asynchronous notifications (webhooks) return payment and trade-order results. The public reference is documentation-and-console only — the underlying OpenAPI/Swagger is not offered as a downloadable spec (the gateway blocks anonymous spec fetches), so integration is gated behind partner onboarding and the console''s iMock/iTest tooling.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: WorldFirst
nav: Providers
network: true
overview: 'WorldFirst publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, United Kingdom, Cross-Border, Money Transfer, and Foreign Exchange.


  The WorldFirst catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WorldFirst''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, authentication, and 15 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 59.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 40.6
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/worldfirst/refs/heads/main/screenshots/worldfirst-2026-08-17T083002.png
security:
- kind: authentication
  name: Worldfirst Authentication
  slug: worldfirst-authentication
  summary_line: signature/oauth2 · 2 schemes
- kind: domain-security
  name: Worldfirst Domain Security
  slug: worldfirst-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: worldfirst
tags:
- Payments
- United Kingdom
- Cross-Border
- Money Transfer
- Foreign Exchange
- Payouts
- Payment Gateway
- E-Commerce
- Multi-Currency
- Card Issuing
website: https://www.worldfirst.com/
---
