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
  url: security/neocarbon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.neocarbon.tech/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neocarbon.tech/privacy
created: '2026-07-17'
description: NeoCarbon GmbH is a Berlin-based climate-technology company building integrated cooling and carbon-capture systems for data centers. Its patented Hollow Fiber platform converts low-grade waste heat (30-55C) simultaneously into efficient cooling, captured CO2 for industrial reuse, and recovered water, deployed as a retrofit without redesigning existing infrastructure. Backed by Speedinvest, the company operates as an industrial hardware and climate-infrastructure business and does not publish a public developer API, SDKs, or an API developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neocarbon.png
layout: provider
modified: '2026-07-20'
name: Neocarbon
nav: Providers
network: true
overview: Neocarbon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate Tech, Carbon Capture, Data Centers, and Cooling.
random_paper: 6
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 7.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neocarbon/refs/heads/main/screenshots/neocarbon-2026-08-07T184836.png
security:
- kind: domain-security
  name: Neocarbon Domain Security
  slug: neocarbon-domain-security
  summary_line: TLSv1.3 · DMARC
slug: neocarbon
tags:
- Company
- Climate Tech
- Carbon Capture
- Data Centers
- Cooling
- Sustainability
- Waste Heat Recovery
- Berlin
website: https://www.neocarbon.tech/
---
