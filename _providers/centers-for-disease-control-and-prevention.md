---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Centers For Disease Control And Prevention Agentic Access
  operation_count: 6
  slug: centers-for-disease-control-and-prevention-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 1
apis:
- description: 'The CDC Socrata Open Data API (SODA) provides programmatic JSON, CSV, and GeoJSON access to hundreds of data.cdc.gov datasets covering COVID-19 case surveillance, vaccination coverage, excess deaths, '
  name: CDC Socrata Open Data API (data.cdc.gov)
  slug: cdc-socrata-open-data-api
- description: CDC WONDER (Wide-ranging ONline Data for Epidemiologic Research) is a suite of public-use ad-hoc query databases covering underlying and multiple cause of death, natality, cancer statistics, tuberculo
  name: CDC WONDER API
  slug: cdc-wonder-api
- description: PLACES (Population Level Analysis and Community Estimates) provides model-based small-area estimates for chronic disease risk factors, health outcomes, and prevention practices for counties, ZCTAs, ce
  name: CDC PLACES / 500 Cities API
  slug: cdc-places-api
- description: The Environmental Public Health Tracking Network API provides a REST interface over the National Tracking Network's JSON-formatted data for air quality, water quality, climate and health, childhood le
  name: CDC Environmental Public Health Tracking Network API
  slug: cdc-ephtn-api
- description: The CDC Public Health Media Library Content Syndication API lets developers and partner sites programmatically retrieve CDC health content (articles, infographics, videos, widgets, images, and microsi
  name: CDC Public Health Media Library (Content Syndication)
  slug: cdc-content-syndication
- description: open.cdc.gov is CDC's Open Technology landing site that indexes the agency's public APIs, open-source GitHub repositories, and open data assets, serving as a catalog entry point for developers seeking
  name: CDC Open Technology API Index
  slug: open-cdc-apis-index
- description: 'The National Notifiable Diseases Surveillance System (NNDSS) and Morbidity and Mortality Weekly Report (MMWR) tables are published as Socrata datasets on data.cdc.gov, providing weekly and historical '
  name: CDC NNDSS / MMWR Socrata Data
  slug: cdc-tb-nndss-socrata
- description: Stable Socrata Open Data API used for the majority of data.cdc.gov queries.
  name: Centers for Disease Control and Prevention SODA v2.1 API
  slug: centers-for-disease-control-and-prevention-soda-v2-1-api
- description: Next-generation query and export endpoints.
  name: Centers for Disease Control and Prevention SODA v3 API
  slug: centers-for-disease-control-and-prevention-soda-v3-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDC Socrata Open Data API (data.cdc.gov) SODA v2.1 API
  slug: open-centers-for-disease-control-and-prevention-soda-v2-1-api
- collection_type: open
  name: CDC Socrata Open Data API (data.cdc.gov) SODA v2.1 SODA v3 API
  slug: open-centers-for-disease-control-and-prevention-soda-v3-api
- collection_type: open
  name: CDC Socrata Open Data API (data.cdc.gov)
  slug: open-centers-for-disease-control-and-prevention
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/centers-for-disease-control-and-prevention-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/centers-for-disease-control-and-prevention-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/centers-for-disease-control-and-prevention-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/centers-for-disease-control-and-prevention
- group: company
  title: ''
  type: Website
  url: https://www.cdc.gov/
- group: other
  title: ''
  type: OpenData
  url: https://data.cdc.gov/
- group: start
  title: ''
  type: Portal
  url: https://open.cdc.gov/
- group: other
  title: ''
  type: APIs
  url: https://open.cdc.gov/apis.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CDCgov
- group: other
  title: ''
  type: WONDER
  url: https://wonder.cdc.gov/
- group: other
  title: ''
  type: Socrata
  url: https://dev.socrata.com/
- group: other
  title: ''
  type: ContentSyndication
  url: https://tools.cdc.gov/medialibrary/
- group: other
  title: ''
  type: EPHTN
  url: https://ephtracking.cdc.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cdc.gov/other/privacy.html
created: '2024-12-03'
description: The Centers for Disease Control and Prevention (CDC) is the United States' national public health agency, part of the Department of Health and Human Services. CDC operates a broad portfolio of public APIs and open data services including the Socrata-powered data.cdc.gov (Open Data API for hundreds of COVID-19, chronic disease, environmental health, immunization, injury, and mortality datasets), the WONDER online query databases for mortality, natality, and cancer statistics, the PLACES / BRFSS and Environmental Public Health Tracking Network APIs, the Content Syndication platform, and the open.cdc.gov developer portal that indexes these resources for civic technologists and public-health researchers.
finops:
- name: Centers For Disease Control And Prevention Finops
  service_category: API
  slug: centers-for-disease-control-and-prevention-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/centers-for-disease-control-and-prevention.png
layout: provider
modified: '2026-04-23'
name: Centers for Disease Control and Prevention
nav: Providers
network: true
overview: 'Centers for Disease Control and Prevention publishes 2 APIs on the [APIs.io](https://apis.io/) network: SODA v2.1 API and SODA v3 API. Tagged areas include CDC, Environmental Health, Epidemiology, Federal-Government, and Healthcare.


  Centers for Disease Control and Prevention''s developer surface includes authentication, developer portal, and 12 more developer resources.'
plans:
- name: Centers For Disease Control And Prevention Plans Pricing
  plan_count: 3
  slug: centers-for-disease-control-and-prevention-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Centers For Disease Control And Prevention Rate Limits
  slug: centers-for-disease-control-and-prevention-rate-limits
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 50.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 29.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/centers-for-disease-control-and-prevention/refs/heads/main/screenshots/centers-for-disease-control-and-prevention-2026-06-20T174125.png
security:
- kind: authentication
  name: Centers For Disease Control And Prevention Authentication
  slug: centers-for-disease-control-and-prevention-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Centers For Disease Control And Prevention Domain Security
  slug: centers-for-disease-control-and-prevention-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: centers-for-disease-control-and-prevention
tags:
- CDC
- Environmental Health
- Epidemiology
- Federal-Government
- Healthcare
- Open Data
- Public Health
- Socrata
- Surveillance
- WONDER
website: https://www.cdc.gov/
---
