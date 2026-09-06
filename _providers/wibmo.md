---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Documented product APIs across Token Hub tokenization, the Areion Payment Gateway (3-D Secure authentication and authorization), Prepaid card issuance/lifecycle/transaction management, Fraud Risk Mana
  name: Wibmo Developer Platform
  slug: wibmo-developer-platform
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wibmo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wibmo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.wibmo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wibmo.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.wibmo.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.wibmo.com/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://wibmo.co/blogs/
- group: operate
  title: ''
  type: Support
  url: https://wibmo.co/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wibmo.co/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wibmo-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/wibmo-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wibmo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://wibmo.co/security-and-privacy/
- group: build
  title: ''
  type: Packages
  url: packages/wibmo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wibmo-packages.yml
created: '2026-07-17'
description: Wibmo is a full-stack PayTech company (acquired by PayU / Naspers in 2019) providing payment security, digital payments, and digital financial services to banks, fintechs, and businesses worldwide. Its platforms and products include the Areion Payment Gateway, Token Hub tokenization, Trident FRM fraud risk management, Tridentity identity and multi-factor authentication, the ACCOSA IVS 3-D Secure authentication server, and a white-label digital wallet and prepaid card-issuing platform. The Wibmo developer portal documents Token Hub, Payment Gateway (3-D Secure authentication and authorization), Prepaid card issuance and lifecycle management, Fraud Risk Management, DFS/Wallet, and Android and iOS MFA (Tridentity) SDKs.
image: https://wibmo.com/wp-content/uploads/2023/01/wibmo-logo.png
layout: provider
modified: '2026-07-21'
name: WIBMO
nav: Providers
network: true
overview: 'WIBMO publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Payments, Fintech, and Payment Gateway.


  WIBMO''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 9 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 27.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Wibmo Authentication
  slug: wibmo-authentication
  summary_line: payload-encryption · 1 scheme
- kind: domain-security
  name: Wibmo Domain Security
  slug: wibmo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: wibmo
tags:
- Company
- Consumer
- Payments
- Fintech
- Payment Gateway
- Tokenization
- Fraud Detection
- 3D Secure
- Authentication
- Digital Wallet
- Prepaid Cards
- India
website: https://wibmo.com/
---
