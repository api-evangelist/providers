---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The Aqwire Connect (Access) API is a developer-facing payments API that lets merchants integrate their application with Aqwire to create cross-border payment transactions. The reference documentation '
  name: Aqwire Connect API
  slug: aqwire-connect-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qwikwire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aqwire.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.aqwire.io
- group: docs
  title: ''
  type: APIReference
  url: https://developers.aqwire.io
- group: start
  title: ''
  type: SignUp
  url: https://app.aqwire.io
- group: start
  title: ''
  type: Login
  url: https://app.aqwire.io
- group: operate
  title: ''
  type: Support
  url: https://aqwire.zohodesk.com/portal/en/home
- group: operate
  title: ''
  type: HelpCenter
  url: https://aqwire.zohodesk.com/portal/en/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aqwire.co/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aqwire.co/privacy-policy/
created: '2026-07-17'
description: Qwikwire, now operating as Aqwire, is a Philippine-founded cross-border payments company backed by 500 Global that bridges international payers with Philippine recipients, with a primary focus on the real estate sector. The platform lets overseas home buyers and investors pay property developers in multiple currencies while handling collection, reconciliation, and delivery of Philippine pesos to local bank accounts. Aqwire for Enterprise provides a payment dashboard for creating payment links, tracking transactions in real time, running auto-debit enrollments, and receiving daily automated reports, plus the Aqwire Connect (Access) API so merchants can integrate payment transaction creation into their own applications. This profile was surfaced as a portfolio company of 500 Global and enriched by the API Evangelist pipeline.
image: https://aqwire.io/assets/logo-brand.png
layout: provider
modified: '2026-07-20'
name: Qwikwire
nav: Providers
network: true
overview: 'Qwikwire publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Cross-Border Payments, Real-Estate, and Fintech.


  Qwikwire''s developer surface includes API reference, signup flow, support, and 7 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 3
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qwikwire/refs/heads/main/screenshots/qwikwire-2026-09-02T152737.png
security:
- kind: domain-security
  name: Qwikwire Domain Security
  slug: qwikwire-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: qwikwire
tags:
- Company
- Payments
- Cross-Border Payments
- Real-Estate
- Fintech
- Philippines
- Multi-Currency
- Remittance
website: https://aqwire.io
---
