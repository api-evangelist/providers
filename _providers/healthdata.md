---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'The Socrata Open Data API (SODA) provides programmatic access to all public datasets hosted on HealthData.gov. Each dataset is accessible through a unique eight-character identifier inserted into the '
  name: HealthData.gov SODA API
  slug: healthdatagov-soda-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/healthdata-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://healthdata.gov
- group: other
  title: ''
  type: Developer
  url: https://dev.socrata.com/consumers/getting-started.html
- group: docs
  title: ''
  type: Documentation
  url: https://dev.socrata.com/docs/endpoints.html
- group: auth
  title: ''
  type: Authentication
  url: https://dev.socrata.com/docs/authentication.html
- group: auth
  title: ''
  type: AppTokenRegistration
  url: https://dev.socrata.com/docs/app-tokens.html
- group: other
  title: ''
  type: DataCatalog
  url: https://healthdata.gov/browse
- group: build
  title: ''
  type: GitHub
  url: https://github.com/HHS/healthdata.gov
- group: commercial
  title: ''
  type: TermsOfService
  url: https://healthdata.gov/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://healthdata.gov/privacy-policy
- group: company
  title: ''
  type: AboutPage
  url: https://healthdata.gov/stories/s/About-Healthdata-gov/jw2e-4hhu/
- group: company
  title: ''
  type: Blog
  url: https://healthdata.gov/blog
- group: other
  title: ''
  type: HHSDeveloperCenter
  url: https://www.hhs.gov/web/developer/index.html
- group: commercial
  title: ''
  type: OpenDataPlan
  url: https://cdo.hhs.gov/s/open-data
created: '2026-06-13'
description: HealthData.gov is the U.S. Department of Health and Human Services open data platform providing public access to federal health datasets including Medicare claims, hospital quality ratings, drug utilization data, public health indicators, and data from agencies such as CMS, CDC, FDA, and NIH. The platform is powered by the Socrata Open Data API (SODA) and exposes every dataset through a consistent REST API using SoQL query language, enabling developers to build applications, conduct research, and create data visualizations from authoritative government health data.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/healthdata.png
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: HealthData.gov
nav: Providers
network: true
overview: 'HealthData.gov publishes 1 API on the [APIs.io](https://apis.io/) network: SODA API. Tagged areas include Health, Open Data, Federal-Government, Medicare, and Medicaid.


  The HealthData.gov catalog on APIs.io includes 1 JSON-LD context.


  HealthData.gov''s developer surface includes developer portal, documentation, authentication, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 11
rate_limits:
- limit_count: 1
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 50.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 33.3
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 33.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/healthdata/refs/heads/main/screenshots/healthdata-2026-06-20T182600.png
security:
- kind: domain-security
  name: Healthdata Domain Security
  slug: healthdata-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: healthdata
tags:
- Health
- Open Data
- Federal-Government
- Medicare
- Medicaid
- Hospital Quality
- Drug Utilization
- Public Health
- CDC
- CMS
- FDA
- NIH
- SODA
- Socrata
website: https://healthdata.gov
---
