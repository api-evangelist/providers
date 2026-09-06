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
- group: company
  title: ''
  type: Website
  url: https://www.encentive.de/en
- group: company
  title: ''
  type: Blog
  url: https://www.encentive.de/en/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.encentive.de/en/resources/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.encentive.de/en/imprint
- group: auth
  title: ''
  type: DomainSecurity
  url: security/encentive-domain-security.yml
created: '2026-07-17'
description: encentive GmbH is a German industrial energy-technology company founded in 2020 and headquartered in Neumuenster. Its AI-driven smart energy management platform, flexOn, automatically optimizes and controls electricity consumption for industrial and commercial operations, orchestrating assets such as PV/solar systems, battery storage, heat pumps, cooling and thermal storage, CHP, wind, and EV charging infrastructure alongside existing energy management systems. flexOn combines plant data, weather forecasts, and real-time market prices to shift loads to periods when energy is cheapest and greenest, cutting energy costs by up to 20% and CO2 emissions by up to 30%. It integrates with industrial assets over REST API, SFTP, OPC UA, and Modbus TCP. encentive publishes no public developer API, portal, or specification; integration is delivered as part of its managed platform, so this profile carries identity and domain-security signals only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/encentive.png
layout: provider
modified: '2026-07-20'
name: Encentive
nav: Providers
network: true
overview: 'Encentive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy Management, Industrial Energy, Artificial Intelligence, and Demand Response.


  Encentive''s developer surface includes engineering blog, support, and 3 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/encentive/refs/heads/main/screenshots/encentive-2026-07-25T213259.png
security:
- kind: domain-security
  name: Encentive Domain Security
  slug: encentive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: encentive
tags:
- Company
- Energy Management
- Industrial Energy
- Artificial Intelligence
- Demand Response
- Energy Optimization
- Sustainability
- Flexibility
- Germany
website: https://www.encentive.de/en
---
