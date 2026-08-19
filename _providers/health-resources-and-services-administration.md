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
api_count: 2
apis:
- description: The HRSA Health Center Data Service enables users to query for health centers by state, county, or ZIP Code, providing access to federally qualified health center location and service information.
  name: HRSA Health Center Data Service
  slug: hrsa-health-center-data-service
- description: The HRSA Ryan White HIV/AIDS Medical Care Provider Data Service enables users to query for HIV/AIDS care providers around a specified latitude and longitude, supporting access to Ryan White HIV/AIDS P
  name: HRSA Ryan White HIV/AIDS Medical Care Provider Data Service
  slug: hrsa-ryan-white-medical-care-provider
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/health-resources-and-services-administration-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HHS-HRSA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hrsagov
- group: company
  title: ''
  type: Website
  url: https://www.hrsa.gov/
- group: start
  title: ''
  type: Portal
  url: https://data.hrsa.gov
- group: other
  title: ''
  type: Web Services
  url: https://data.hrsa.gov/tools/web-services
- group: operate
  title: ''
  type: Support
  url: https://www.hrsa.gov/about/contact/programsupport.html
created: '2024-12-03'
description: The Health Resources and Services Administration (HRSA) is the primary Federal agency for improving access to health care services for people who are uninsured, isolated, or medically vulnerable. HRSA provides data and web services for healthcare resources, facility locations, and program information.
finops:
- name: Health Resources And Services Administration Finops
  service_category: API
  slug: health-resources-and-services-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/health-resources-and-services-administration.png
layout: provider
modified: '2026-04-28'
name: Health Resources and Services Administration
nav: Providers
network: true
overview: 'Health Resources and Services Administration publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government, Healthcare, Open Data, and Public Health.


  Health Resources and Services Administration''s developer surface includes developer portal, support, and 5 more developer resources.'
plans:
- name: Health Resources And Services Administration Plans Pricing
  plan_count: 3
  slug: health-resources-and-services-administration-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Health Resources And Services Administration Rate Limits
  slug: health-resources-and-services-administration-rate-limits
score:
  band: emerging
  composite: 11.7
  delta: -1.4
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/health-resources-and-services-administration/refs/heads/main/screenshots/health-resources-and-services-administration-2026-06-20T182556.png
security:
- kind: domain-security
  name: Health Resources And Services Administration Domain Security
  slug: health-resources-and-services-administration-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: health-resources-and-services-administration
tags:
- Federal Government
- Healthcare
- Open Data
- Public Health
website: https://www.hrsa.gov/
---
