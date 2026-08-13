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
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: British Columbia Data Catalogue Agentic Access
  operation_count: 13
  slug: british-columbia-data-catalogue-agentic-access
  summary_line: 13 operations
api_count: 7
apis:
- description: The BC Data Catalogue exposes a CKAN v3 REST API at https://catalogue.data.gov.bc.ca/api/3/action/ providing programmatic access to BC government open datasets. Key endpoints include package_list (lis
  name: BC Data Catalogue CKAN API
  slug: ckan-api
- description: The Datasets API from British Columbia Data Catalogue — 4 operation(s) for datasets.
  name: British Columbia Data Catalogue Datasets API
  slug: british-columbia-data-catalogue-datasets-api
- description: The Groups API from British Columbia Data Catalogue — 2 operation(s) for groups.
  name: British Columbia Data Catalogue Groups API
  slug: british-columbia-data-catalogue-groups-api
- description: The Organizations API from British Columbia Data Catalogue — 2 operation(s) for organizations.
  name: British Columbia Data Catalogue Organizations API
  slug: british-columbia-data-catalogue-organizations-api
- description: The Resources API from British Columbia Data Catalogue — 2 operation(s) for resources.
  name: British Columbia Data Catalogue Resources API
  slug: british-columbia-data-catalogue-resources-api
- description: The Site API from British Columbia Data Catalogue — 1 operation(s) for site.
  name: British Columbia Data Catalogue Site API
  slug: british-columbia-data-catalogue-site-api
- description: The Tags API from British Columbia Data Catalogue — 2 operation(s) for tags.
  name: British Columbia Data Catalogue Tags API
  slug: british-columbia-data-catalogue-tags-api
artifact_total: 13
collections:
- collection_type: open
  name: BC Data Catalogue CKAN API
  slug: open-british-columbia-data-catalogue
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/british-columbia-data-catalogue-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/british-columbia-data-catalogue-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catalogue.data.gov.bc.ca/
- group: other
  title: ''
  type: APIBaseURL
  url: https://catalogue.data.gov.bc.ca/api/3/action/
- group: other
  title: ''
  type: DatasetList
  url: https://catalogue.data.gov.bc.ca/api/3/action/package_list
- group: other
  title: ''
  type: DatasetSearch
  url: https://catalogue.data.gov.bc.ca/api/3/action/package_search
- group: start
  title: ''
  type: GovernmentPortal
  url: https://www2.gov.bc.ca/gov/content/data/bc-data-catalogue
- group: agent
  title: ''
  type: LlmsText
  url: https://catalogue.data.gov.bc.ca/llms.txt
created: '2024-11-07'
description: The British Columbia Data Catalogue is the official open data portal for the Government of British Columbia, Canada. Built on the CKAN open data platform, it provides programmatic access to thousands of BC government datasets spanning census and demographic data, environmental and climate information, geospatial and mapping data, financial reports, transportation and infrastructure data, and health and social services statistics. The CKAN API at api/3/action/ enables searching, listing, and retrieving dataset metadata and resources without authentication.
finops:
- name: British Columbia Data Catalogue Finops
  service_category: API
  slug: british-columbia-data-catalogue-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/british-columbia-data-catalogue.png
layout: provider
modified: '2026-04-21'
name: British Columbia Data Catalogue
nav: Providers
network: true
overview: British Columbia Data Catalogue publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Groups API, Organizations API, and 3 more. Tagged areas include Open Data, Government, Canadian Government, British Columbia, and Provincial Data.
plans:
- name: British Columbia Data Catalogue Plans Pricing
  plan_count: 3
  slug: british-columbia-data-catalogue-plans-pricing
random_paper: 95
rate_limits:
- limit_count: 5
  name: British Columbia Data Catalogue Rate Limits
  slug: british-columbia-data-catalogue-rate-limits
score:
  band: emerging
  composite: 22.0
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 50.0
    developer_ergonomics: 0.0
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 22.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/british-columbia-data-catalogue/refs/heads/main/screenshots/british-columbia-data-catalogue-2026-06-20T173712.png
security:
- kind: domain-security
  name: British Columbia Data Catalogue Domain Security
  slug: british-columbia-data-catalogue-domain-security
  summary_line: TLSv1.3
slug: british-columbia-data-catalogue
tags:
- Open Data
- Government
- Canadian Government
- British Columbia
- Provincial Data
- CKAN
- Geospatial
website: https://catalogue.data.gov.bc.ca/
---
