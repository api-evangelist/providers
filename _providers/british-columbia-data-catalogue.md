---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  - authentication
  - rate-limits
  - security
  - sandbox
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-11-06'
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
  description: The Tags API from British Columbia Data Catalogue — 2 operation(s) for tags.
  name: British Columbia Data Catalogue Tags API
  slug: british-columbia-data-catalogue-tags-api
- description: 'DataBC''s public OGC endpoint serves the spatial half of the BC Data Catalogue: 895 queryable WMS 1.3.0 layers and 896 WFS 2.0.0 feature types drawn from the BC Geographic Warehouse. 884 catalogue data'
  name: DataBC Public OGC Web Services (WMS/WFS)
  slug: databc-public-ogc-services
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: CKAN's Action API is a powerful, RPC-style API that exposes all of CKAN's core features to API clients.
  name: British Columbia Data Catalogue Action API
  slug: british-columbia-data-catalogue-action-api
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The FacebookPosts API from British Columbia Data Catalogue — 1 operation(s) for facebookposts.
  name: British Columbia Data Catalogue Facebook Posts API
  slug: british-columbia-data-catalogue-facebookposts-api
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The Home API from British Columbia Data Catalogue — 1 operation(s) for home.
  name: British Columbia Data Catalogue Home API
  slug: british-columbia-data-catalogue-home-api
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The Ministries API from British Columbia Data Catalogue — 3 operation(s) for ministries.
  name: British Columbia Data Catalogue Ministries API
  slug: british-columbia-data-catalogue-ministries-api
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The Newsletters API from British Columbia Data Catalogue — 5 operation(s) for newsletters.
  name: British Columbia Data Catalogue Newsletters API
  slug: british-columbia-data-catalogue-newsletters-api
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The Posts API from British Columbia Data Catalogue — 6 operation(s) for posts.
  name: British Columbia Data Catalogue Posts API
  slug: british-columbia-data-catalogue-posts-api
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The Sectors API from British Columbia Data Catalogue — 2 operation(s) for sectors.
  name: British Columbia Data Catalogue Sectors API
  slug: british-columbia-data-catalogue-sectors-api
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The Services API from British Columbia Data Catalogue — 2 operation(s) for services.
  name: British Columbia Data Catalogue Services API
  slug: british-columbia-data-catalogue-services-api
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The Slides API from British Columbia Data Catalogue — 2 operation(s) for slides.
  name: British Columbia Data Catalogue Slides API
  slug: british-columbia-data-catalogue-slides-api
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The Themes API from British Columbia Data Catalogue — 2 operation(s) for themes.
  name: British Columbia Data Catalogue Themes API
  slug: british-columbia-data-catalogue-themes-api
- baseURL: https://catalogue.data.gov.bc.ca/api/3
  baseurl_source: declared
  description: The Resource Links API from British Columbia Data Catalogue — 1 operation(s) for resource links.
  name: British Columbia Data Catalogue Resource Links API
  slug: british-columbia-data-catalogue-resource-links-api
artifact_total: 30
collections:
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
- group: commercial
  href: https://artifacts.apis.io/british-columbia-data-catalogue/finops/british-columbia-data-catalogue-finops.yml
  title: ''
  type: FinOps
  url: finops/british-columbia-data-catalogue-finops.yml
- group: auth
  href: https://artifacts.apis.io/british-columbia-data-catalogue/authentication/british-columbia-data-catalogue-authentication.yml
  title: ''
  type: Authentication
  url: authentication/british-columbia-data-catalogue-authentication.yml
- group: agent
  href: https://artifacts.apis.io/british-columbia-data-catalogue/agentic-access/british-columbia-data-catalogue-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/british-columbia-data-catalogue-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/british-columbia-data-catalogue/security/british-columbia-data-catalogue-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/british-columbia-data-catalogue-domain-security.yml
- group: design
  href: https://artifacts.apis.io/british-columbia-data-catalogue/conformance/british-columbia-data-catalogue-conformance.yml
  title: ''
  type: Conformance
  url: conformance/british-columbia-data-catalogue-conformance.yml
- group: design
  href: https://artifacts.apis.io/british-columbia-data-catalogue/conventions/british-columbia-data-catalogue-conventions.yml
  title: ''
  type: Conventions
  url: conventions/british-columbia-data-catalogue-conventions.yml
- group: design
  href: https://artifacts.apis.io/british-columbia-data-catalogue/errors/british-columbia-data-catalogue-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/british-columbia-data-catalogue-problem-types.yml
- group: design
  href: https://artifacts.apis.io/british-columbia-data-catalogue/lifecycle/british-columbia-data-catalogue-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/british-columbia-data-catalogue-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/british-columbia-data-catalogue/data-model/british-columbia-data-catalogue-data-model.yml
  title: ''
  type: DataModel
  url: data-model/british-columbia-data-catalogue-data-model.yml
- group: start
  href: https://artifacts.apis.io/british-columbia-data-catalogue/sandbox/british-columbia-data-catalogue-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/british-columbia-data-catalogue-sandbox.yml
- group: build
  href: https://artifacts.apis.io/british-columbia-data-catalogue/packages/british-columbia-data-catalogue-packages.yml
  title: ''
  type: Packages
  url: packages/british-columbia-data-catalogue-packages.yml
- group: build
  href: https://artifacts.apis.io/british-columbia-data-catalogue/packages/british-columbia-data-catalogue-packages.yml
  title: ''
  type: SDKs
  url: packages/british-columbia-data-catalogue-packages.yml
- group: commercial
  href: https://artifacts.apis.io/british-columbia-data-catalogue/plans/british-columbia-data-catalogue-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/british-columbia-data-catalogue-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/british-columbia-data-catalogue/rate-limits/british-columbia-data-catalogue-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/british-columbia-data-catalogue-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/british-columbia-data-catalogue/mcp/british-columbia-data-catalogue-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/british-columbia-data-catalogue-mcp.yml
- group: build
  href: https://artifacts.apis.io/british-columbia-data-catalogue/mcp/british-columbia-data-catalogue-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/british-columbia-data-catalogue-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/british-columbia-data-catalogue/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/british-columbia-data-catalogue/llms/british-columbia-data-catalogue-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/british-columbia-data-catalogue-llms.txt
- group: other
  href: https://artifacts.apis.io/british-columbia-data-catalogue/overlays/british-columbia-data-catalogue-bcdc-api-overlay.yaml
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
- has_sources: false
  method: generated
  name: British Columbia Data Catalogue Finops
  primary_unit: request
  service_category: API
  slug: british-columbia-data-catalogue-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/british-columbia-data-catalogue.png
layout: provider
mcp_servers:
- description: MCP server; 11 tools listed. A candidate, not confirmed as published by the provider.
  name: British Columbia Data Catalogue MCP Server
  slug: british-columbia-data-catalogue-mcp-yml
modified: '2026-09-04'
name: British Columbia Data Catalogue
nav: Providers
network: true
overview: 'British Columbia Data Catalogue publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Tags API, Action API, Facebook Posts API, and 10 more. Tagged areas include Open Data, Government, Canadian Government, British Columbia, and Provincial Data.


  The British Columbia Data Catalogue catalog on APIs.io includes 1 Spectral governance ruleset.


  British Columbia Data Catalogue''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, and 27 more developer resources.'
plans:
- name: British Columbia Data Catalogue Plans Pricing
  plan_count: 0
  slug: british-columbia-data-catalogue-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: British Columbia Data Catalogue Rate Limits
  slug: british-columbia-data-catalogue-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: British Columbia Data Catalogue API Rules
  rule_count: 56
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 3
  slug: british-columbia-data-catalogue-rules
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 41.2
    developer_ergonomics: 61.3
    discoverability: 73.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 57.9
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/british-columbia-data-catalogue/british-columbia-data-catalogue-2026-06-20T173712.png
security:
- kind: authentication
  name: British Columbia Data Catalogue Authentication
  slug: british-columbia-data-catalogue-authentication
  summary_line: none/apiKey · 3 schemes
- kind: domain-security
  name: British Columbia Data Catalogue Domain Security
  slug: british-columbia-data-catalogue-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: find-a-bc-dataset
  slug: british-columbia-data-catalogue-find-a-bc-dataset
- name: load-a-bc-map-layer
  slug: british-columbia-data-catalogue-load-a-bc-map-layer
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
