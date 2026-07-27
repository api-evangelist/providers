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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-27'
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
random_paper: 29
rate_limits:
- limit_count: 0
  name: Neso Data Portal Rate Limits
  slug: neso-data-portal-rate-limits
score:
  band: thin
  composite: 30.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 37.7
    developer_ergonomics: 13.0
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.6
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 34.8
  schema_version: 0.5
  scored_at: '2026-07-27'
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
