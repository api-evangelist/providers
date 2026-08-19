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
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: National Interagency Fire Center Agentic Access
  operation_count: 4
  slug: national-interagency-fire-center-agentic-access
  summary_line: 4 operations
api_count: 3
apis:
- description: The FeatureServer API from National Interagency Fire Center — 1 operation(s) for featureserver.
  name: National Interagency Fire Center FeatureServer API
  slug: national-interagency-fire-center-featureserver-api
- description: The Layer API from National Interagency Fire Center — 2 operation(s) for layer.
  name: National Interagency Fire Center Layer API
  slug: national-interagency-fire-center-layer-api
- description: The Services API from National Interagency Fire Center — 1 operation(s) for services.
  name: National Interagency Fire Center Services API
  slug: national-interagency-fire-center-services-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NIFC ArcGIS REST Services FeatureServer API
  slug: open-national-interagency-fire-center-featureserver-api
- collection_type: open
  name: NIFC ArcGIS REST Services FeatureServer Layer API
  slug: open-national-interagency-fire-center-layer-api
- collection_type: open
  name: NIFC ArcGIS REST FeatureServer Services API
  slug: open-national-interagency-fire-center-services-api
- collection_type: open
  name: NIFC ArcGIS REST Services API
  slug: open-national-interagency-fire-center
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-interagency-fire-center-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/national-interagency-fire-center-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-interagency-fire-center-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-interagency-fire-center
- group: company
  title: ''
  type: Website
  url: https://www.nifc.gov/
- group: start
  title: ''
  type: Portal
  url: https://data-nifc.opendata.arcgis.com/
created: '2024-12-03'
description: The National Interagency Fire Center (NIFC) is a collaborative effort between multiple federal agencies to address wildfires and other emergency incidents around the United States. NIFC serves as a centralized command center for coordinating resources, personnel, and information to effectively respond to and manage wildfires. NIFC publishes authoritative geospatial data through ArcGIS REST services and its open data portal.
finops:
- name: National Interagency Fire Center Finops
  service_category: API
  slug: national-interagency-fire-center-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-interagency-fire-center.png
layout: provider
modified: '2026-05-19'
name: National Interagency Fire Center
nav: Providers
network: true
overview: 'National Interagency Fire Center publishes 3 APIs on the [APIs.io](https://apis.io/) network: FeatureServer API, Layer API, and Services API. Tagged areas include Emergency Management, Federal Government, Geospatial, and Wildfire.


  National Interagency Fire Center''s developer surface includes developer portal and 5 more developer resources.'
plans:
- name: National Interagency Fire Center Plans Pricing
  plan_count: 3
  slug: national-interagency-fire-center-plans-pricing
random_paper: 100
rate_limits:
- limit_count: 5
  name: National Interagency Fire Center Rate Limits
  slug: national-interagency-fire-center-rate-limits
score:
  band: emerging
  composite: 21.9
  delta: -3.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 25.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-interagency-fire-center/refs/heads/main/screenshots/national-interagency-fire-center-2026-06-20T190038.png
security:
- kind: domain-security
  name: National Interagency Fire Center Domain Security
  slug: national-interagency-fire-center-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: National Interagency Fire Center Vulnerability Disclosure
  slug: national-interagency-fire-center-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: national-interagency-fire-center
tags:
- Emergency Management
- Federal Government
- Geospatial
- Wildfire
website: https://www.nifc.gov/
---
