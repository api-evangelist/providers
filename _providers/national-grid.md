---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: Official Carbon Intensity forecast API for Great Britain, developed by NESO in partnership with EDF Europe, University of Oxford, and WWF. Provides 96+ hour ahead national and regional carbon intensit
  name: Carbon Intensity API
  slug: carbon-intensity-api
- description: CKAN-based REST API providing programmatic access to hundreds of electricity system datasets published by the National Energy System Operator. Covers ancillary services, balancing costs, carbon intens
  name: NESO Data Portal API
  slug: neso-data-portal-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/national-grid-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-grid-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.neso.energy/data-portal
- group: company
  title: ''
  type: News
  url: https://www.neso.energy/news-and-events
- group: other
  title: ''
  type: MediaCentre
  url: https://www.neso.energy/news-and-events/media-centre
- group: company
  title: ''
  type: About
  url: https://www.neso.energy/
- group: commercial
  title: ''
  type: License
  url: https://creativecommons.org/licenses/by/4.0/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/carbon-intensity/terms
- group: operate
  title: ''
  type: FAQ
  url: https://www.neso.energy/data-portal/about-data-portal
- group: operate
  title: ''
  type: Support
  url: mailto:box.OpenData.ESO@nationalgrideso.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carbon-intensity
created: '2026-06-13'
description: National Energy System Operator (NESO) provides open data APIs for the UK electricity system, including carbon intensity forecasts, demand data, generation mix, ancillary services, balancing costs, and operational data for Great Britain's electricity network. The Carbon Intensity API delivers 96+ hour ahead forecasts at both national and regional levels, while the NESO Data Portal (CKAN-based) exposes hundreds of datasets covering the full spectrum of electricity system operations.
finops:
- name: Neso Finops
  service_category: ''
  slug: neso-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-grid.png
layout: provider
modified: '2026-06-13'
name: National Grid ESO
nav: Providers
network: true
overview: 'National Grid ESO publishes 1 API on the [APIs.io](https://apis.io/) network: Carbon Intensity API. Tagged areas include Energy, Electricity, Carbon Intensity, UK, and Open Data.


  National Grid ESO''s developer surface includes developer portal, product news, FAQ, support, and 7 more developer resources.'
plans:
- name: Neso Data Portal Plans
  plan_count: 1
  slug: neso-data-portal-plans
random_paper: 45
rate_limits:
- limit_count: 2
  name: Neso Data Portal Rate Limits
  slug: neso-data-portal-rate-limits
score:
  band: emerging
  composite: 27.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 27.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 21.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-grid/refs/heads/main/screenshots/national-grid-2026-06-20T190017.png
security:
- kind: domain-security
  name: National Grid Domain Security
  slug: national-grid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: National Grid Vulnerability Disclosure
  slug: national-grid-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: national-grid
tags:
- Energy
- Electricity
- Carbon Intensity
- UK
- Open Data
- Sustainability
- Grid Operations
website: https://www.neso.energy/data-portal
---
