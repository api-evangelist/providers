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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: National Geospatial Intelligence Agency Agentic Access
  operation_count: 6
  slug: national-geospatial-intelligence-agency-agentic-access
  summary_line: 6 operations
api_count: 4
apis:
- description: Navdata clock state files.
  name: National Geospatial-Intelligence Agency Clock API
  slug: national-geospatial-intelligence-agency-clock-api
- description: Earth Orientation Parameter Predictions in multiple formats.
  name: National Geospatial-Intelligence Agency EOPP API
  slug: national-geospatial-intelligence-agency-eopp-api
- description: GPS ephemeris products, including Center of Mass and Antenna Phase Center variants.
  name: National Geospatial-Intelligence Agency Ephemeris API
  slug: national-geospatial-intelligence-agency-ephemeris-api
- description: Short-term orbit prediction products.
  name: National Geospatial-Intelligence Agency Orbit API
  slug: national-geospatial-intelligence-agency-orbit-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NGA Earth-Info REST Clock API
  slug: open-national-geospatial-intelligence-agency-clock-api
- collection_type: open
  name: NGA Earth-Info REST Clock EOPP API
  slug: open-national-geospatial-intelligence-agency-eopp-api
- collection_type: open
  name: NGA Earth-Info REST Clock Ephemeris API
  slug: open-national-geospatial-intelligence-agency-ephemeris-api
- collection_type: open
  name: NGA Earth-Info REST Clock Orbit API
  slug: open-national-geospatial-intelligence-agency-orbit-api
- collection_type: open
  name: NGA Earth-Info REST API
  slug: open-national-geospatial-intelligence-agency
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-geospatial-intelligence-agency-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-geospatial-intelligence-agency-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ngageoint
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nga
- group: company
  title: ''
  type: Website
  url: https://www.nga.mil/
- group: start
  title: ''
  type: Portal
  url: https://earth-info.nga.mil/
- group: other
  title: ''
  type: Tearline
  url: https://www.tearline.mil/
- group: operate
  title: ''
  type: Contact
  url: mailto:geomatics@nga.mil
created: '2024-12-25'
description: The National Geospatial-Intelligence Agency (NGA) is a combat support agency within the U.S. Department of Defense that provides geospatial intelligence in support of national security. Through its Office of Geomatics, NGA publishes the Earth-Info portal, which exposes a REST API in OpenAPI format for downloading GPS ephemeris products, Earth Orientation Parameter Predictions (EOPP), Navdata clock state files, and short-term orbit prediction products. NGA also maintains the WGS 84 reference frame, EGM2008 gravitational model, and the GEOTRANS coordinate conversion tool.
finops:
- name: National Geospatial Intelligence Agency Finops
  service_category: API
  slug: national-geospatial-intelligence-agency-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-geospatial-intelligence-agency.png
layout: provider
modified: '2026-05-19'
name: National Geospatial-Intelligence Agency
nav: Providers
network: true
overview: 'National Geospatial-Intelligence Agency publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Clock API, EOPP API, Ephemeris API, and 1 more. Tagged areas include Federal-Government, Geospatial, Intelligence, Defense, and Geomatics.


  National Geospatial-Intelligence Agency''s developer surface includes developer portal and 7 more developer resources.'
plans:
- name: National Geospatial Intelligence Agency Plans Pricing
  plan_count: 3
  slug: national-geospatial-intelligence-agency-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: National Geospatial Intelligence Agency Rate Limits
  slug: national-geospatial-intelligence-agency-rate-limits
score:
  band: emerging
  composite: 21.5
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 21.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-geospatial-intelligence-agency/refs/heads/main/screenshots/national-geospatial-intelligence-agency-2026-06-20T190021.png
security:
- kind: domain-security
  name: National Geospatial Intelligence Agency Domain Security
  slug: national-geospatial-intelligence-agency-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-geospatial-intelligence-agency
tags:
- Federal-Government
- Geospatial
- Intelligence
- Defense
- Geomatics
website: https://www.nga.mil/
---
