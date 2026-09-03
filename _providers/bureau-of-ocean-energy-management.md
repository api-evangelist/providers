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
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: MarineCadastre.gov is the authoritative source for marine cadastre data and services. It provides an interactive map viewer with integrated submerged lands information including legal, property owners
  name: MarineCadastre.gov
  slug: marine-cadastre
- description: BOEM provides ArcGIS REST Services exposing geospatial data for the Outer Continental Shelf (OCS) regions. Data includes active leases, offshore block grids, boundaries, wells, and pipelines for Atlan
  name: BOEM ArcGIS REST Services
  slug: boem-arcgis-rest-services
- description: ESPIS provides access to BOEM's environmental studies data, including research reports, environmental impact studies, and scientific literature related to offshore energy development. Searchable by to
  name: Environmental Studies Program Information System (ESPIS)
  slug: espis
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bureau-of-ocean-energy-management-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-ocean-energy-management-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boemgov
- group: company
  title: ''
  type: Website
  url: https://www.boem.gov
- group: start
  title: ''
  type: Portal
  url: https://marinecadastre.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boem.gov/privacy-policy
- group: other
  title: ''
  type: Mapping and Data
  url: https://www.boem.gov/oil-gas-energy/mapping-and-data
- group: start
  title: ''
  type: Data Portal
  url: https://catalog.data.gov/dataset?organization=boem-gov
- group: company
  title: ''
  type: Blog
  url: https://www.boem.gov/rss.xml
created: '2024-11-30'
description: The Bureau of Ocean Energy Management (BOEM) manages the nation's offshore resources in an environmentally and economically responsible way. BOEM oversees the responsible development of U.S. Outer Continental Shelf energy and mineral resources while protecting the environment and conserving natural resources.
finops:
- name: Bureau Of Ocean Energy Management Finops
  service_category: API
  slug: bureau-of-ocean-energy-management-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-ocean-energy-management.png
layout: provider
modified: '2026-04-23'
name: Bureau of Ocean Energy Management
nav: Providers
network: true
overview: 'Bureau of Ocean Energy Management publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Federal-Government, Marine, Oceans, and GIS.


  Bureau of Ocean Energy Management''s developer surface includes developer portal, engineering blog, and 7 more developer resources.'
plans:
- name: Bureau Of Ocean Energy Management Plans Pricing
  plan_count: 3
  slug: bureau-of-ocean-energy-management-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Bureau Of Ocean Energy Management Rate Limits
  slug: bureau-of-ocean-energy-management-rate-limits
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 6
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-ocean-energy-management/refs/heads/main/screenshots/bureau-of-ocean-energy-management-2026-06-20T173814.png
security:
- kind: domain-security
  name: Bureau Of Ocean Energy Management Domain Security
  slug: bureau-of-ocean-energy-management-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bureau Of Ocean Energy Management Vulnerability Disclosure
  slug: bureau-of-ocean-energy-management-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bureau-of-ocean-energy-management
tags:
- Energy
- Federal-Government
- Marine
- Oceans
- GIS
- Offshore
- Environmental
website: https://www.boem.gov
---
