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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: The HUD USER FMR/IL API publishes Fair Market Rents (FMRs), Small Area Fair Market Rents, and Income Limits (IL) for U.S. metropolitan and non-metropolitan areas. It exposes endpoints for listing stat
  name: HUD USER FMR/IL API
  slug: hud-user-fmr-il-api
- description: The HUD eGIS storefront publishes ArcGIS-based REST services and feature layers for the Department's geospatial assets, including Continuum of Care boundaries, CPD activities, public housing locations
  name: HUD eGIS ArcGIS REST Services
  slug: hud-egis-arcgis
- description: The FHA Mortgage Limits service lets users look up the FHA or Government-Sponsored Enterprise (GSE) mortgage limits for one or more areas, by state, county, or Metropolitan Statistical Area, with resu
  name: FHA Mortgage Limits
  slug: fha-mortgage-limits
- description: The HUD Open Data Catalog at data.hud.gov is curated by HUD's Office of the Chief Data Officer and lists the Department's open datasets across housing, community development, and fair housing. Dataset
  name: HUD Open Data Catalog
  slug: hud-data-catalog
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/department-of-housing-and-urban-development-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hud
- group: company
  title: ''
  type: Website
  url: https://www.hud.gov
- group: other
  title: ''
  type: Open Data
  url: https://data.hud.gov/
- group: other
  title: ''
  type: HUD USER
  url: https://www.huduser.gov/portal/home.html
- group: other
  title: ''
  type: HUD GIS
  url: https://hudgis-hud.opendata.arcgis.com/
- group: other
  title: ''
  type: FHA
  url: https://www.hud.gov/fha
- group: other
  title: ''
  type: HUD Exchange
  url: https://www.hudexchange.info/
- group: company
  title: ''
  type: News
  url: https://www.hud.gov/press
- group: operate
  title: ''
  type: Contact
  url: https://www.hud.gov/contact_us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hud.gov/notices/privacy_policy
- group: other
  title: ''
  type: Data.gov HUD Catalog
  url: https://catalog.data.gov/organization/hud-gov
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HUD-USER
- group: design
  title: ''
  type: JSONLD
  url: json-ld/department-of-housing-and-urban-development-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/department-of-housing-and-urban-development-vocabulary.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/department-of-housing-and-urban-development-capabilities.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hud.gov/rss.xml
created: '2024-12-25'
description: The U.S. Department of Housing and Urban Development (HUD) is the federal agency responsible for overseeing programs that address the country's housing needs and promote sustainable urban development. HUD exposes programmatic data through the HUD USER FMR/IL API for Fair Market Rents and Income Limits, the HUD eGIS storefront and ArcGIS REST services for geospatial assets, the data.hud.gov data catalog, and various FHA tools including mortgage limits and condominium lookup services.
finops:
- name: Department Of Housing And Urban Development Finops
  service_category: API
  slug: department-of-housing-and-urban-development-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/department-of-housing-and-urban-development.png
jsonld:
- class_count: 0
  name: Department Of Housing And Urban Development Context
  property_count: 5
  slug: department-of-housing-and-urban-development-context
layout: provider
modified: '2026-04-28'
name: Department of Housing and Urban Development
nav: Providers
network: true
overview: 'Department of Housing and Urban Development publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Affordable Housing, Fair Market Rents, Federal Government, FHA, and GIS.


  The Department of Housing and Urban Development catalog on APIs.io includes 1 JSON-LD context.


  Department of Housing and Urban Development''s developer surface includes product news, engineering blog, and 15 more developer resources.'
plans:
- name: Department Of Housing And Urban Development Plans Pricing
  plan_count: 3
  slug: department-of-housing-and-urban-development-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Department Of Housing And Urban Development Rate Limits
  slug: department-of-housing-and-urban-development-rate-limits
score:
  band: emerging
  composite: 26.2
  delta: -3.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 8.1
    developer_ergonomics: 2.2
    discoverability: 74.1
    governance: 10.4
    operational_transparency: 36.8
  previous_composite: 29.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 27.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/department-of-housing-and-urban-development/refs/heads/main/screenshots/department-of-housing-and-urban-development-2026-06-20T175917.png
security:
- kind: domain-security
  name: Department Of Housing And Urban Development Domain Security
  slug: department-of-housing-and-urban-development-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: department-of-housing-and-urban-development
tags:
- Affordable Housing
- Fair Market Rents
- Federal Government
- FHA
- GIS
- Housing
- HUD
- Income Limits
- Mortgage
- Open Data
website: https://www.hud.gov
---
