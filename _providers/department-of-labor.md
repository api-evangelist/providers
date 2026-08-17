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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 5
apis:
- description: The DOL Open Data API v4 is the Department of Labor's modernized REST API replacing the retired developer.dol.gov APIv1 and APIv2. It is served from the DOL Data Portal at dataportal.dol.gov and expos
  name: DOL Open Data API V4
  slug: dol-api-v4
- description: The Bureau of Labor Statistics Public Data API v2 provides programmatic access to historical BLS time series data in JSON or Excel. Version 2 requires registration to obtain a registrationkey query pa
  name: BLS Public Data API V2
  slug: bls-public-data-api
- description: The DOL Enforcement Data site at data.dol.gov publishes the Department's enforcement records from agencies including the Wage and Hour Division, OSHA, MSHA, OFCCP, and the Employee Benefits Security A
  name: DOL Enforcement Data
  slug: dol-enforcement-data
- description: The DOL API Sampler is an interactive playground for exploring the DOL Open Data API v4 endpoints. It serves as a quick way to issue sample requests, browse parameters, and inspect responses against t
  name: DOL API Sampler
  slug: dol-api-sampler
- description: The Department of Labor Open Data Catalog publishes datasets across labor statistics, enforcement, employment training, and worker protection programs. Datasets are surfaced on Data.gov under the dol-
  name: DOL Open Data Catalog
  slug: dol-open-data-catalog
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/department-of-labor-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/u-s-department-of-labor
- group: company
  title: ''
  type: Website
  url: https://www.dol.gov
- group: start
  title: ''
  type: Open Data Portal
  url: https://dataportal.dol.gov/
- group: operate
  title: ''
  type: Developer Community
  url: https://usdepartmentoflabor.github.io/DOLAPI/
- group: other
  title: ''
  type: Bureau of Labor Statistics
  url: https://www.bls.gov
- group: other
  title: ''
  type: Enforcement Data
  url: https://data.dol.gov/
- group: build
  title: ''
  type: API Sampler
  url: https://devtools.dol.gov/apisampler
- group: other
  title: ''
  type: OSHA
  url: https://www.osha.gov
- group: other
  title: ''
  type: MSHA
  url: https://www.msha.gov
- group: other
  title: ''
  type: ETA
  url: https://www.dol.gov/agencies/eta
- group: other
  title: ''
  type: Wage and Hour Division
  url: https://www.dol.gov/agencies/whd
- group: other
  title: ''
  type: EBSA
  url: https://www.dol.gov/agencies/ebsa
- group: other
  title: ''
  type: OFCCP
  url: https://www.dol.gov/agencies/ofccp
- group: other
  title: ''
  type: Data.gov DOL Catalog
  url: https://catalog.data.gov/organization/dol-gov
- group: company
  title: ''
  type: News
  url: https://www.dol.gov/newsroom
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dol.gov/general/privacynotice
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USDepartmentofLabor
- group: design
  title: ''
  type: JSONLD
  url: json-ld/department-of-labor-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/department-of-labor-vocabulary.yml
created: '2024-12-03'
description: The U.S. Department of Labor (DOL) is the federal department that fosters, promotes, and develops the welfare of wage earners, job seekers, and retirees, improves working conditions, advances opportunities for profitable employment, and assures work-related benefits and rights. DOL exposes a portfolio of public APIs and data feeds including the modernized DOL APIv4 served from the DOL Open Data Portal, the Bureau of Labor Statistics Public Data API, the DOL Enforcement Data site, and Data.gov.
finops:
- name: Department Of Labor Finops
  service_category: API
  slug: department-of-labor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/department-of-labor.png
jsonld:
- class_count: 0
  name: Department Of Labor Context
  property_count: 5
  slug: department-of-labor-context
layout: provider
modified: '2026-04-28'
name: Department of Labor
nav: Providers
network: true
overview: 'Department of Labor publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include BLS, Employment, Enforcement, Federal Government, and Labor.


  The Department of Labor catalog on APIs.io includes 1 JSON-LD context.


  Department of Labor''s developer surface includes product news and 19 more developer resources.'
plans:
- name: Department Of Labor Plans Pricing
  plan_count: 3
  slug: department-of-labor-plans-pricing
random_paper: 119
rate_limits:
- limit_count: 5
  name: Department Of Labor Rate Limits
  slug: department-of-labor-rate-limits
score:
  band: emerging
  composite: 19.2
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 8.1
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 10.4
    operational_transparency: 13.2
  previous_composite: 19.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 27.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/department-of-labor/refs/heads/main/screenshots/department-of-labor-2026-06-20T175920.png
security:
- kind: domain-security
  name: Department Of Labor Domain Security
  slug: department-of-labor-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: department-of-labor
tags:
- BLS
- Employment
- Enforcement
- Federal Government
- Labor
- Open Data
- Statistics
- Wages
- Workforce
website: https://www.dol.gov
---
