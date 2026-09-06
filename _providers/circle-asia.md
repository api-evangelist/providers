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
    error_semantics: false
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
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/circle-asia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getcircle.ai
- group: operate
  title: ''
  type: Support
  url: mailto:hello@getcircle.ai
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.getcircle.ai/faq
- group: auth
  title: ''
  type: Compliance
  url: https://www.getcircle.ai/baomat
- group: design
  title: ''
  type: Conformance
  url: conformance/circle-asia-conformance.yml
created: '2026-07-17'
description: Circle Asia Technologies is a Singapore-headquartered consumer fintech (offices at 68 Circular Road, Singapore, and Ho Chi Minh City, Vietnam) behind the Circle app and the VPBank Circle PayLater credit card, a digital buy-now-pay-later card issued in partnership with Vietnam Prosperity Joint Stock Commercial Bank (VPBank). The product lets consumers onboard with only an ID and phone number, waives the lifetime annual fee, and pairs a physical and virtual card with AI-assisted expense management, spending limits, one-tap card lock, biometric (face/fingerprint) authentication, and real-time SMS/app transaction alerts. The company is PCI DSS v4.0.1 certified and Visa-compliant, ships native iOS and Android apps, and is backed by 500 Global. Circle Asia is a consumer application company with no public developer API; this profile captures its identity, security posture, and compliance claims for the API Evangelist network.
image: https://static.wixstatic.com/media/d9a4dd_c7c2e84652e04a14ae768d27a9eedf27~mv2.png
layout: provider
modified: '2026-07-18'
name: Circle Asia
nav: Providers
network: true
overview: 'Circle Asia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Credit Cards, and Buy Now Pay Later.


  Circle Asia''s developer surface includes support and 5 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 8.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/circle-asia/refs/heads/main/screenshots/circle-asia-2026-07-25T205403.png
security:
- kind: domain-security
  name: Circle Asia Domain Security
  slug: circle-asia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: circle-asia
tags:
- Company
- Fintech
- Payments
- Credit Cards
- Buy Now Pay Later
- Consumer Finance
- Mobile Banking
- Vietnam
- Southeast Asia
website: https://getcircle.ai
---
