---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: pvfactors is an open-source Python library for modeling diffuse shading and bifacial photovoltaic (PV) irradiance. It implements 2D geometry and view-factor mathematics to account for reflections betw
  name: pvfactors
  slug: pvfactors
- description: PVMismatch is an open-source Python library for calculating mismatch losses in photovoltaic systems. It models I-V and P-V curves for PV cells, modules, and strings to quantify power loss from cell-to
  name: PVMismatch
  slug: pvmismatch
- description: SolarUtils is an open-source Python package providing solar position algorithms and utility functions for solar energy calculations, including sun position (azimuth, elevation, zenith), sunrise/sunset
  name: SolarUtils
  slug: solar-utils
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sunpower-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sunpower-corporation
- group: company
  title: ''
  type: Website
  url: https://www.sunpower.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SunPower
- group: company
  title: ''
  type: Blog
  url: https://us.sunpower.com/blog
created: '2026-05-02'
description: 'SunPower is a residential solar energy company (Nasdaq: SPWR) that designs, installs, and finances solar systems and battery storage for homeowners. The original SunPower Corporation filed for Chapter 11 bankruptcy in August 2024; its assets were acquired by Complete Solaria in September 2024, which rebranded as SunPower Inc. in April 2025. SunPower maintains the GitHub org github.com/SunPower, hosting open-source solar modeling tools including pvfactors (view-factor model for bifacial PV modeling), PVMismatch (mismatch loss calculations), and SolarUtils. These Python libraries are used by solar energy professionals and researchers for photovoltaic system modeling and simulation.'
finops:
- name: Sunpower Finops
  service_category: API
  slug: sunpower-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sunpower.png
layout: provider
modified: '2026-05-02'
name: SunPower
nav: Providers
network: true
overview: 'SunPower publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Solar Energy, Renewable Energy, Photovoltaics, Open-Source, and Python.


  SunPower''s developer surface includes engineering blog and 4 more developer resources.'
plans:
- name: Sunpower Plans Pricing
  plan_count: 3
  slug: sunpower-plans-pricing
press:
- date: '2026-05-25'
  title: Our Chairman and CEO, T.J. Rodgers, is leading ...
  url: https://www.facebook.com/sunpower/posts/our-chairman-and-ceo-tj-rodgers-is-leading-sunpower-into-a-new-era-of-innovation/1021881723476273/
- date: '2026-05-25'
  title: SunPower and EagleView partner for precise, faster solar ...
  url: https://www.eagleview.com/solar/sunpower-eagleview-partnership-automate-faster-precise-solar-installations/
- date: '2026-05-25'
  title: 'Sony Vs SUNPOWER: Which is a Better Buy? AI Stock ...'
  url: https://danelfin.com/stocks/SONY-sony-vs-SPWR-sunpower-compare
- date: '2026-05-25'
  title: SunPower and EagleView Automate Home Survey ...
  url: https://www.prnewswire.com/news-releases/sunpower-and-eagleview-automate-home-survey-process-for-faster-more-precise-solar-installations-301218922.html
- date: '2026-05-25'
  title: SunPower Adds $5M to Recent $41M Offering
  url: https://natlawreview.com/press-releases/sunpower-adds-5m-recent-41m-offering
random_paper: 17
rate_limits:
- limit_count: 5
  name: Sunpower Rate Limits
  slug: sunpower-rate-limits
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sunpower/refs/heads/main/screenshots/sunpower-2026-06-20T194655.png
security:
- kind: domain-security
  name: Sunpower Domain Security
  slug: sunpower-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sunpower
tags:
- Solar Energy
- Renewable Energy
- Photovoltaics
- Open-Source
- Python
website: https://www.sunpower.com
---
