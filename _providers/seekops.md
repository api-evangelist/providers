---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The authenticated backend behind Celsius, SeekOps' cloud analytics and emissions-reconciliation dashboard. Observed as a Django REST Framework service at https://celsius.seekops.com/api/ — every probe
  name: SeekOps Celsius Platform API
  slug: celsius
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://seekops.com/
- group: company
  title: ''
  type: About
  url: https://seekops.com/about/
- group: company
  title: ''
  type: Blog
  url: https://seekops.com/news/
- group: operate
  title: ''
  type: Support
  url: https://seekops.com/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://seekops.com/faq/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seekops.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://seekops.com/iso-9001-certification/
- group: design
  title: ''
  type: Conformance
  url: conformance/seekops-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seekops-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seekops-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/seekops-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/seekops-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: SeekOps runs a real Django REST Framework API behind its Celsius analytics product at https://celsius.seekops.com/api/, but every collection answers HTTP 401 with no anonymous schema endpoint, and the documentation host docs.seekops.com redirects straight to a Microsoft Entra ID sign-in — so the contract is readable only by an operator who has already signed a survey contract and been issued a tenant account.
  evidence:
  - status: 401
    url: https://celsius.seekops.com/api/
  - status: 401
    url: https://celsius.seekops.com/api/sites/
  - status: 200
    url: https://docs.seekops.com/
  - status: 200
    url: https://fastr.seekops.com/
  - status: 404
    url: https://celsius.seekops.com/api/schema/
  - status: 404
    url: https://seekops.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-26'
description: 'SeekOps Inc. is an Austin, Texas emissions-measurement company that detects and quantifies methane and carbon dioxide from industrial facilities using drone-mounted laser spectroscopy. Its SeekIR sensor suite applies tunable diode laser absorption spectroscopy (TDLAS) originally developed at NASA''s Jet Propulsion Laboratory to search for methane on Mars, hardened for terrestrial energy operations. SeekOps sells measurement as a service — Leak Detection and Quantification (LDAQ) surveys flown over upstream and midstream oil and gas sites, offshore platforms, landfills, biogas digesters and renewable natural gas facilities — and delivers the results through two software surfaces: Celsius, a cloud analytics and reconciliation-reporting dashboard, and FASTR, a real-time telemetry view. Founded in 2017, the company has surveyed facilities across six continents and is backed by Equinor Ventures and OGCI Climate Investments. Its software is customer-only: both Celsius and FASTR sit
  behind authentication and SeekOps publishes no public developer program, API documentation or machine-readable contract.'
image: https://seekops.com/wp-content/themes/seekops-theme/assets/img/logo-nav.svg
layout: provider
modified: '2026-08-26'
name: SeekOps
nav: Providers
network: true
overview: 'SeekOps publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Oil and Gas, Emissions, and Methane.


  SeekOps'' developer surface includes engineering blog, support, FAQ, and 9 more developer resources.'
plans:
- name: Seekops Plans Pricing
  plan_count: 0
  slug: seekops-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Seekops Rate Limits
  slug: seekops-rate-limits
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 18.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 35.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/seekops/refs/heads/main/screenshots/seekops-2026-09-02T154745.png
security:
- kind: authentication
  name: Seekops Authentication
  slug: seekops-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Seekops Domain Security
  slug: seekops-domain-security
  summary_line: TLSv1.3 · HSTS
slug: seekops
tags:
- Company
- Energy
- Oil and Gas
- Emissions
- Methane
- Environmental Monitoring
- Sensors
- Drones
- Remote Sensing
- Climate
- ESG
- Sustainability
- Analytics
- Measurements
website: https://seekops.com/
---
