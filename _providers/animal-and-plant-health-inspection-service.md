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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: The APHIS Public Search Tool provides public access to search APHIS program data, permits, and regulatory information related to animal and plant health programs.
  name: APHIS Public Search Tool
  slug: aphis-public-search-api
- description: APHIS eFile is the web-based permitting system for submitting animal and plant health import/export permit applications, tracking application status, applying for renewals and amendments, and receivin
  name: APHIS eFile Permitting System
  slug: aphis-efile-api
- description: The Agricultural Commodity Import Requirements (ACIR) system provides searchable access to APHIS import requirements for agricultural commodities, including plants, plant products, animals, and animal
  name: Agricultural Commodity Import Requirements (ACIR)
  slug: aphis-acir-api
- description: The APHIS and AMS Geospatial Hub provides GIS mapping applications, spatial data layers, and geospatial analysis tools for animal and plant health surveillance, pest and disease tracking, and quaranti
  name: APHIS and AMS Geospatial Hub
  slug: aphis-geospatial-hub
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/animal-and-plant-health-inspection-service-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usda-aphis
- group: company
  title: ''
  type: Website
  url: https://www.aphis.usda.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.aphis.usda.gov/efile
- group: start
  title: ''
  type: Portal
  url: https://efile.aphis.usda.gov/s/
- group: start
  title: ''
  type: Portal
  url: https://acir.aphis.usda.gov/s/
- group: start
  title: ''
  type: Portal
  url: https://aphis.my.site.com/PublicSearchTool/s/
- group: start
  title: ''
  type: GISPortal
  url: https://www.aphis.usda.gov/aphis-ams-geospatial-hub
- group: other
  title: ''
  type: DataVisualization
  url: https://www.aphis.usda.gov/data-visualization-tools
- group: other
  title: ''
  type: DataAPI
  url: https://www.aphis.usda.gov/wildlife-services/publications/pdr
- group: other
  title: ''
  type: OpenData
  url: https://catalog.data.gov/organization/aphis-usda-gov
- group: operate
  title: ''
  type: Contact
  url: https://www.aphis.usda.gov/contact/mrpbs-informatics
- group: other
  title: ''
  type: FOIA
  url: https://www.aphis.usda.gov/about/foia
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aphis.usda.gov/about/privacy-policy
created: '2024-11-21'
description: USDA's Animal and Plant Health Inspection Service (APHIS) protects the health and value of U.S. agriculture and natural resources by safeguarding against agricultural pests and diseases, ensuring the welfare of animals, and supporting sustainable agricultural practices. APHIS provides digital services including the eFile permitting system for import/export permits, the Agricultural Commodity Import Requirements (ACIR) portal, a geospatial hub for spatial analysis, data visualization tools, and open datasets via data.gov.
finops:
- name: Animal And Plant Health Inspection Service Finops
  service_category: API
  slug: animal-and-plant-health-inspection-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/animal-and-plant-health-inspection-service.png
layout: provider
modified: '2026-04-19'
name: Animal and Plant Health Inspection Service
nav: Providers
network: true
overview: 'Animal and Plant Health Inspection Service publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Animal Health, Animal Welfare, Biotechnology, and Federal Government.


  Animal and Plant Health Inspection Service''s developer surface includes developer portal and 13 more developer resources.'
plans:
- name: Animal And Plant Health Inspection Service Plans Pricing
  plan_count: 3
  slug: animal-and-plant-health-inspection-service-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Animal And Plant Health Inspection Service Rate Limits
  slug: animal-and-plant-health-inspection-service-rate-limits
score:
  band: emerging
  composite: 15.1
  delta: -0.8
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 15.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/animal-and-plant-health-inspection-service/refs/heads/main/screenshots/animal-and-plant-health-inspection-service-2026-06-20T172003.png
security:
- kind: domain-security
  name: Animal And Plant Health Inspection Service Domain Security
  slug: animal-and-plant-health-inspection-service-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: animal-and-plant-health-inspection-service
tags:
- Agriculture
- Animal Health
- Animal Welfare
- Biotechnology
- Federal Government
- Import Export
- Permits
- Pest Control
- Plant Health
- Regulatory
- USDA
- Wildlife
website: https://www.aphis.usda.gov/
---
