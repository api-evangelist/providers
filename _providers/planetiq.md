---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://planetiq.com/
- group: other
  title: ''
  type: Products
  url: https://planetiq.com/products/
- group: operate
  title: ''
  type: Support
  url: https://planetiq.com/company/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://planetiq.com/company/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://planetiq.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/planetiq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/planetiq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://planetiq.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://planetiq.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/planetiq-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/planetiq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/planetiq-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/planetiq-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/planetiq-packages.yml
coverage:
  checked: '2026-08-26'
  detail: PlanetiQ sells GNSS radio occultation data as netCDF files under NOAA and NASA contracts and redistributes it through NASA's own Satellite Data Explorer, so it operates no developer program of its own — api., data., portal., docs., developer. and app.planetiq.com all fail DNS resolution and every spec path on planetiq.com 404s, while the products page ends in a Contact Us form rather than an endpoint.
  evidence:
  - status: 404
    url: https://planetiq.com/openapi.json
  - status: 404
    url: https://planetiq.com/swagger.json
  - status: 404
    url: https://planetiq.com/api-docs
  - status: 0
    url: https://api.planetiq.com/
  - status: 200
    url: https://planetiq.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: PlanetiQ is a commercial space-weather and atmospheric data company headquartered in Golden, Colorado, operating the GNOMES constellation of small satellites carrying its Pyxis GNSS radio occultation (GNSS-RO) sensor. Pyxis receives signals from all four global navigation constellations (GPS, GLONASS, Galileo and BeiDou) and turns the refracted signal into vertical atmospheric profiles of temperature, pressure, density, refractivity and humidity at 100 m vertical resolution, plus ionospheric total electron content, scintillation phase and polarimetric precipitation observations. The data is sold as Level 1B calibrated phase/SNR and Level 2 bending angle/refractivity products, primarily under U.S. government contracts (NOAA Commercial Data Program radio occultation data buys, NASA Commercial Satellite Data Acquisition, U.S. Air Force STRATFI) and redistributed to authorized users in netCDF via NASA's Satellite Data Explorer. PlanetiQ publishes no public developer program, no
  API, and no machine-readable API contract; commercial and defense access runs through a sales conversation rather than self-service onboarding.
image: https://planetiq.com/wp-content/uploads/2025/07/planetIQ-white-color-logo.svg
layout: provider
modified: '2026-08-26'
name: PlanetiQ
nav: Providers
network: true
overview: 'PlanetiQ is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Satellite, Earth Observation, and Space Weather.


  PlanetiQ''s developer surface includes support, engineering blog, and 12 more developer resources.'
plans:
- name: Planetiq Plans Pricing
  plan_count: 0
  slug: planetiq-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Planetiq Rate Limits
  slug: planetiq-rate-limits
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/planetiq/refs/heads/main/screenshots/planetiq-2026-09-02T151419.png
security:
- kind: domain-security
  name: Planetiq Domain Security
  slug: planetiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: planetiq
tags:
- Company
- Weather
- Satellite
- Earth Observation
- Space Weather
- Atmospheric Data
- GNSS Radio Occultation
- Climate
- Aerospace
- Defense
- Geospatial
website: https://planetiq.com/
---
