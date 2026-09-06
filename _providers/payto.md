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
api_count: 1
apis:
- description: PayTo's public developer surface, published by Australian Payments Plus (AP+) and NPP Australia. Rather than a self-serve API hosted by the scheme, this covers the AP+ Developer Portal (login-gated AP
  name: PayTo / NPP Developer Resources
  slug: payto-npp-developer-resources
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payto-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/payto-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/payto-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/auspayplus
- group: company
  title: ''
  type: Website
  url: https://www.auspayplus.com.au/brands/payto
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.developers.auspayplus.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.developers.auspayplus.com.au/docs/
- group: start
  title: ''
  type: SignUp
  url: https://www.developers.auspayplus.com.au/api/auth/signup/
- group: company
  title: ''
  type: Blog
  url: https://www.auspayplus.com.au/news
- group: operate
  title: ''
  type: Support
  url: https://www.auspayplus.com.au/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.auspayplus.com.au/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.auspayplus.com.au/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/auspayplus
created: '2026-07-24'
description: 'PayTo is Australia''s real-time mandated-payments service, operated by Australian Payments Plus (AP+) as an overlay on the New Payments Platform (NPP). It lets merchants, billers, and payment service providers establish digital, pre-authorised agreements (mandates) that debit a customer''s bank account in real time using either a PayID or BSB and account number, with the mandate authorised, viewed, and managed by the account holder inside their own banking app. PayTo is positioned as the modern successor to the legacy BECS direct-debit rails, adding instant settlement, richer ISO 20022 data, and central mandate management via the NPP Mandate Management Service. As a domestic rail and scheme operator, AP+/NPP Australia is documentation- and rulebook-first: it publishes the NPP API Framework (v5.0, aligned to ISO 20022) that defines the mandatory data attributes and technical approach for PayTo and NPP APIs, but it does not itself host or offer a self-serve public API. The actual
  PayTo APIs are implemented and exposed by NPP Participants (banks) and connected payment service providers, so the company''s public developer surface is a portal, framework, sandbox, and message specifications rather than a downloadable OpenAPI.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: PayTo
nav: Providers
network: true
overview: 'PayTo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Australia, Real-Time Payments, Account-to-Account, and ISO 20022.


  PayTo''s developer surface includes documentation, signup flow, engineering blog, support, and 9 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 18.6
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 24.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payto/refs/heads/main/screenshots/payto-2026-08-07T191702.png
security:
- kind: domain-security
  name: Payto Domain Security
  slug: payto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: payto
tags:
- Payments
- Australia
- Real-Time Payments
- Account-to-Account
- ISO 20022
- Direct Debit
- Mandates
- New Payments Platform
- Scheme Operator
- Open Banking
website: https://www.auspayplus.com.au/brands/payto
---
