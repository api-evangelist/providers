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
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Access ERS data products in machine-readable formats for analysis or integration into your own applications. Delivered via api.data.gov as REST endpoints. Requires an api.data.gov key.
  name: USDA ERS Data APIs
  slug: ers-data-apis
- description: Integrate ERS map layers into the GIS package of your choice, on their own or mashed up with other geospatial data.
  name: USDA ERS Geospatial APIs
  slug: ers-geospatial-apis
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/economic-research-service-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usda-ers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usda-economic-research-service
- group: company
  title: ''
  type: Website
  url: https://www.ers.usda.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ers.usda.gov/developer/
- group: company
  title: ''
  type: Blog
  url: https://www.ers.usda.gov/amber-waves
created: '2024-12-25'
description: The Economic Research Service (ERS) is a division of the United States Department of Agriculture (USDA) that conducts economic research and analysis related to agriculture, food, and rural development. ERS provides policymakers, stakeholders, and the public with valuable information and data to help inform decision-making and policy development.
finops:
- name: Economic Research Service Finops
  service_category: API
  slug: economic-research-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/economic-research-service.png
layout: provider
modified: '2026-04-28'
name: Economic Research Service
nav: Providers
network: true
overview: 'Economic Research Service publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Economics, Federal-Government, and Research.


  Economic Research Service''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Economic Research Service Plans Pricing
  plan_count: 3
  slug: economic-research-service-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Economic Research Service Rate Limits
  slug: economic-research-service-rate-limits
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 14.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/economic-research-service/refs/heads/main/screenshots/economic-research-service-2026-06-20T180437.png
security:
- kind: domain-security
  name: Economic Research Service Domain Security
  slug: economic-research-service-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: economic-research-service
tags:
- Agriculture
- Economics
- Federal-Government
- Research
website: https://www.ers.usda.gov/
---
