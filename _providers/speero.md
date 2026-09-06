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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://speero.net
- group: company
  title: ''
  type: About
  url: https://speero.net/about-us/
- group: company
  title: ''
  type: Blog
  url: https://speero.net/blog/
- group: start
  title: ''
  type: Login
  url: https://speero.net/customer-login/
- group: operate
  title: ''
  type: Support
  url: https://wa.me/966920031983
- group: commercial
  title: ''
  type: TermsOfService
  url: https://speero.net/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://speero.net/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/speero-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/speero-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/speero-api-catalog.json
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/speero-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/speero-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/speero-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/speero-vulnerability-disclosure.yml
created: '2026-07-17'
description: Speero (سبيرو) is Saudi Arabia's online marketplace for authentic automotive spare parts, accessories, and professional vehicle services. The platform helps car owners find OEM and aftermarket parts for their specific make and model across all major categories (engine, brakes, suspension, lighting, AC, exhaust, and more) and book maintenance, detailing, paint and dent repair, tinting, and tire care at trusted workshops across the Kingdom. It supports browse-by-vehicle, installment payment options, and WhatsApp-based customer support. Speero is a 500 Global portfolio company. It is a consumer marketplace and publishes no public developer API, but it does expose a machine-discovery surface (llms.txt, RFC 9116 security.txt, and an RFC 9727 api-catalog linkset).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/speero.png
layout: provider
modified: '2026-07-21'
name: Speero
nav: Providers
network: true
overview: 'Speero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Marketplace, E-Commerce, and Spare Parts.


  Speero''s developer surface includes engineering blog, support, and 12 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - saudi-arabia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 14.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/speero/refs/heads/main/screenshots/speero-2026-09-02T160409.png
security:
- kind: domain-security
  name: Speero Domain Security
  slug: speero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Speero Vulnerability Disclosure
  slug: speero-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: speero
tags:
- Company
- Automotive
- Marketplace
- E-Commerce
- Spare Parts
- Vehicle Services
- Auto Parts
- Saudi Arabia
website: https://speero.net
---
