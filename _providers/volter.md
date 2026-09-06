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
  url: security/volter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getvolter.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/volter-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/volter-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://volter-marketing-site.s3.eu-west-2.amazonaws.com/get_volter_ltd_privacy_policy.pdf
- group: operate
  title: ''
  type: Support
  url: https://getvolter.com/contact
- group: start
  title: ''
  type: Login
  url: https://app.getvolter.com/
created: '2026-07-17'
description: Volter (Get Volter Ltd) is a London-based energy platform that connects UK businesses with renewable generators to procure cheaper, greener electricity, and helps commercial real estate owners and generators deploy, optimize, and monetize rooftop solar and other onsite renewable assets. The platform spans renewable energy matching, solar optimization, and a forthcoming energy management suite with analytics, anomaly detection, flexible asset control, and battery storage. Backed by Transition and Seedcamp with a $3.2M pre-seed round in 2024. Volter does not currently publish a public API or developer documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/volter.png
layout: provider
modified: '2026-07-21'
name: Volter
nav: Providers
network: true
overview: 'Volter is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Renewable Energy, Solar, and Energy Management.


  Volter''s developer surface includes support and 6 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 9.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/volter/refs/heads/main/screenshots/volter-2026-09-02T170222.png
security:
- kind: domain-security
  name: Volter Domain Security
  slug: volter-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: volter
tags:
- Company
- Energy
- Renewable Energy
- Solar
- Energy Management
- Real-Estate
- Sustainability
website: https://getvolter.com
---
