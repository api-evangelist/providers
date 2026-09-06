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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: British Columbia Data Catalogue Agentic Access
  operation_count: 13
  slug: british-columbia-data-catalogue-agentic-access
  summary_line: 13 operations
api_count: 1
apis:
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The BC Data Catalogue exposes a CKAN v3 REST API at https://catalogue.data.gov.bc.ca/api/3/action/ providing programmatic access to BC government open datasets. Key endpoints include package_list (lis
  name: BC Data Catalogue CKAN API
  slug: ckan-api
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The Datasets API from British Columbia Data Catalogue — 4 operation(s) for datasets.
  name: British Columbia Data Catalogue Datasets API
  slug: british-columbia-data-catalogue-datasets-api
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The Groups API from British Columbia Data Catalogue — 2 operation(s) for groups.
  name: British Columbia Data Catalogue Groups API
  slug: british-columbia-data-catalogue-groups-api
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The Organizations API from British Columbia Data Catalogue — 2 operation(s) for organizations.
  name: British Columbia Data Catalogue Organizations API
  slug: british-columbia-data-catalogue-organizations-api
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The Resources API from British Columbia Data Catalogue — 2 operation(s) for resources.
  name: British Columbia Data Catalogue Resources API
  slug: british-columbia-data-catalogue-resources-api
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The Site API from British Columbia Data Catalogue — 1 operation(s) for site.
  name: British Columbia Data Catalogue Site API
  slug: british-columbia-data-catalogue-site-api
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The Tags API from British Columbia Data Catalogue — 2 operation(s) for tags.
  name: British Columbia Data Catalogue Tags API
  slug: british-columbia-data-catalogue-tags-api
- description: 'DataBC''s public OGC endpoint serves the spatial half of the BC Data Catalogue: 895 queryable WMS 1.3.0 layers and 896 WFS 2.0.0 feature types drawn from the BC Geographic Warehouse. 884 catalogue data'
  name: DataBC Public OGC Web Services (WMS/WFS)
  slug: databc-public-ogc-services
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BC Data Catalogue CKAN Datasets API
  slug: open-british-columbia-data-catalogue-datasets-api
- collection_type: open
  name: BC Data Catalogue CKAN Datasets Groups API
  slug: open-british-columbia-data-catalogue-groups-api
- collection_type: open
  name: BC Data Catalogue CKAN Datasets Organizations API
  slug: open-british-columbia-data-catalogue-organizations-api
- collection_type: open
  name: BC Data Catalogue CKAN Datasets Resources API
  slug: open-british-columbia-data-catalogue-resources-api
- collection_type: open
  name: BC Data Catalogue CKAN Datasets Site API
  slug: open-british-columbia-data-catalogue-site-api
- collection_type: open
  name: BC Data Catalogue CKAN Datasets Tags API
  slug: open-british-columbia-data-catalogue-tags-api
- collection_type: open
  name: BC Data Catalogue CKAN API
  slug: open-british-columbia-data-catalogue
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/british-columbia-data-catalogue-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/british-columbia-data-catalogue-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/british-columbia-data-catalogue-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/british-columbia-data-catalogue-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/british-columbia-data-catalogue-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/british-columbia-data-catalogue-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/british-columbia-data-catalogue-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/british-columbia-data-catalogue-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/british-columbia-data-catalogue-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/british-columbia-data-catalogue-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/british-columbia-data-catalogue-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/british-columbia-data-catalogue-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/british-columbia-data-catalogue-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/british-columbia-data-catalogue-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/british-columbia-data-catalogue-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/british-columbia-data-catalogue-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/british-columbia-data-catalogue-bcdc-api-overlay.yaml
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
- group: docs
  title: ''
  type: Documentation
  url: https://bcgov.github.io/data-publication/pages/dps_bcdc_api_w_how_to_use.html
- group: docs
  title: ''
  type: APIReference
  url: https://bcgov.github.io/data-publication/pages/dps_bcdc_api_w_common_calls.html
- group: start
  title: ''
  type: GettingStarted
  url: https://bcgov.github.io/data-publication/pages/dps_bcdc.html
- group: operate
  title: ''
  type: Support
  url: https://dpdd.atlassian.net/servicedesk/customer/portal/1
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bcgov
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcgov/api-specs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www2.gov.bc.ca/gov/content?id=D1EE0A405E584363B205CD4353E02C88
- group: commercial
  title: ''
  type: License
  url: https://www2.gov.bc.ca/gov/content?id=A519A56BC2BF44E4A008B33FCF527F61
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www2.gov.bc.ca/gov/content/home/privacy
- group: start
  title: ''
  type: GovernmentPortal
  url: https://www2.gov.bc.ca/gov/content/data
created: '2024-11-07'
description: The British Columbia Data Catalogue is the official open data portal for the Government of British Columbia, Canada. Built on the CKAN open data platform, it provides programmatic access to thousands of BC government datasets spanning census and demographic data, environmental and climate information, geospatial and mapping data, financial reports, transportation and infrastructure data, and health and social services statistics. The CKAN API at api/3/action/ enables searching, listing, and retrieving dataset metadata and resources without authentication. DataBC publishes a first-party OpenAPI 3.0.0 for the catalogue in github.com/bcgov/api-specs, and serves the spatial half of the catalogue separately as OGC WMS 1.3.0 and WFS 2.0.0 at openmaps.gov.bc.ca — 895 layers and 896 feature types from the BC Geographic Warehouse, referenced by 884 catalogue datasets. Everything is published under the Open Government Licence — British Columbia and is free to use with attribution.
finops:
- name: British Columbia Data Catalogue Finops
  service_category: API
  slug: british-columbia-data-catalogue-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/british-columbia-data-catalogue.png
layout: provider
mcp_servers:
- description: ''
  name: British Columbia Data Catalogue MCP Server
  slug: british-columbia-data-catalogue-mcp-server
modified: '2026-09-04'
name: British Columbia Data Catalogue
nav: Providers
network: true
overview: 'British Columbia Data Catalogue publishes 7 APIs on the [APIs.io](https://apis.io/) network, including BC Data Catalogue CKAN API, Datasets API, Groups API, and 4 more. Tagged areas include Open Data, Government, Canadian Government, British Columbia, and Provincial Data.


  British Columbia Data Catalogue''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, and 26 more developer resources.'
plans:
- name: British Columbia Data Catalogue Plans Pricing
  plan_count: 0
  slug: british-columbia-data-catalogue-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: British Columbia Data Catalogue Rate Limits
  slug: british-columbia-data-catalogue-rate-limits
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 46.5
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/british-columbia-data-catalogue/refs/heads/main/screenshots/british-columbia-data-catalogue-2026-06-20T173712.png
security:
- kind: authentication
  name: British Columbia Data Catalogue Authentication
  slug: british-columbia-data-catalogue-authentication
  summary_line: none/apiKey · 3 schemes
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
- OGC
- WMS
- WFS
- Dataset Search
- Public Sector
website: https://catalogue.data.gov.bc.ca/
---
