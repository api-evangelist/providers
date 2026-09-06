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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bureau Of Land Management Agentic Access
  operation_count: 17
  slug: bureau-of-land-management-agentic-access
  summary_line: 17 operations
api_count: 6
apis:
- description: The BLM Geospatial Business Platform is a public tool and publication platform for exploring and downloading GIS data. Built on ArcGIS Online, it provides REST endpoints for BLM geospatial data includ
  name: BLM Geospatial Business Platform (GBP) Hub
  slug: blm-geospatial-business-platform
- description: 'The Mineral and Land Records System (MLRS) is an online platform delivering state-of-the-art mineral and land records transactions, tracking, mapping, and more for BLM customers and staff. It manages '
  name: BLM Mineral and Land Records System (MLRS)
  slug: blm-mineral-land-records
- description: The General Land Office (GLO) Records provide access to federal land conveyance records including land patents, survey plats, and field notes from 1788 to the present. The system contains over 10 mill
  name: BLM General Land Office Records
  slug: blm-general-land-office-records
- description: BLM ePlanning provides public access to land use planning documents, environmental impact statements, and resource management plans. Citizens can track planning projects and participate in comment per
  name: BLM ePlanning
  slug: blm-eplanning
- baseURL: https://gbp-blm-egis.hub.arcgis.com
  baseurl_source: declared
  description: The only OpenAPI the Bureau of Land Management serves. A 17-operation OGC API - Records catalog over BLM's 803 published geospatial datasets, with keyword, bounding-box and CQL2 filtering, facet aggre
  name: BLM GBP Hub Search API (OGC API - Records)
  slug: blm-gbp-hub-search-api
- description: 'BLM''s own ArcGIS Server estate, operated on blm.gov infrastructure rather than a hosted platform: thirteen REST instances — one national plus Alaska, Arizona, California, Colorado, Eastern States, Ida'
  name: BLM National and State ArcGIS REST / OGC WMS Services
  slug: blm-arcgis-gis-services
artifact_total: 14
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bureau-of-land-management-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bureau-of-land-management-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-land-management-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-land-management
- group: company
  title: ''
  type: Website
  url: https://www.blm.gov
- group: start
  title: ''
  type: Portal
  url: https://gbp-blm-egis.hub.arcgis.com/
- group: start
  title: ''
  type: Data Portal
  url: https://catalog.data.gov/dataset?organization=blm-gov
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/bureau-of-land-management-gbp-hub-search-openapi.json
- group: design
  title: ''
  type: Conformance
  url: conformance/bureau-of-land-management-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bureau-of-land-management-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.blm.gov/.well-known/security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.blm.gov/info/notices/vulnerability-disclosure
- group: auth
  title: ''
  type: Authentication
  url: authentication/bureau-of-land-management-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bureau-of-land-management-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bureau-of-land-management-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bureau-of-land-management-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bureau-of-land-management-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bureau-of-land-management-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/bureau-of-land-management-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bureau-of-land-management-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/bureau-of-land-management-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bureau-of-land-management-gbp-hub-search-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bureau-of-land-management-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bureau-of-land-management-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bureau-of-land-management-plans-pricing.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gbp-blm-egis.hub.arcgis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.blm.gov/services/geospatial/GISData
- group: docs
  title: ''
  type: APIReference
  url: https://gis.blm.gov/arcgis/rest/services
- group: start
  title: ''
  type: GettingStarted
  url: https://www.blm.gov/services/geospatial
- group: operate
  title: ''
  type: Support
  url: https://www.blm.gov/contact
- group: company
  title: ''
  type: Blog
  url: https://www.blm.gov/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DOI-BLM
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doi.gov/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.doi.gov/disclaimer
- group: other
  title: ''
  type: DataAPI
  url: https://gbp-blm-egis.hub.arcgis.com/data.json
- group: other
  title: ''
  type: OGCAPI
  url: https://gbp-blm-egis.hub.arcgis.com/api/search/v1
- group: other
  title: ''
  type: WSDL
  url: wsdl/bureau-of-land-management-sma-mapserver.wsdl
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bureau-of-land-management-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://gis.blm.gov/arcgis/rest/services
created: '2024-11-30'
description: 'The Bureau of Land Management (BLM) is the U.S. Department of the Interior bureau that administers 245 million surface acres of public land and 700 million acres of subsurface mineral estate — about one in every ten acres of the United States — for outdoor recreation, livestock grazing, mineral and energy development, conservation and cultural heritage. Its public API surface is geospatial and entirely anonymous: a catalog of 803 datasets served as OGC API - Records and DCAT-US 1.1, and 785 ArcGIS Server services across thirteen REST instances (one national, twelve state) that BLM operates itself on gis.blm.gov, 42 of which also publish OGC WMS 1.3.0. There is no API key, no plan and no quota — and equally no versioning policy, changelog, status page or developer support channel. Every published operation is read-only; the transactional systems (MLRS mining claims and land records, GLO Records land patents, ePlanning NEPA documents) sit behind a login and publish no contract.'
finops:
- name: Bureau Of Land Management Finops
  service_category: API
  slug: bureau-of-land-management-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-land-management.png
layout: provider
modified: '2026-09-05'
name: Bureau of Land Management
nav: Providers
network: true
overview: 'Bureau of Land Management publishes 1 API on the [APIs.io](https://apis.io/) network: BLM GBP Hub Search API (OGC API - Records). Tagged areas include Environment, Federal-Government, Land, Resources, and GIS.


  Bureau of Land Management''s developer surface includes developer portal, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 33 more developer resources.'
plans:
- name: Bureau Of Land Management Plans Pricing
  plan_count: 0
  slug: bureau-of-land-management-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Bureau Of Land Management Rate Limits
  slug: bureau-of-land-management-rate-limits
scopes:
- name: Bureau Of Land Management Scopes
  scope_count: 12
  slug: bureau-of-land-management-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 32.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 35.5
    developer_ergonomics: 56.5
    discoverability: 85.2
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 14.5
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 75.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-land-management/refs/heads/main/screenshots/bureau-of-land-management-2026-06-20T173814.png
security:
- kind: authentication
  name: Bureau Of Land Management Authentication
  slug: bureau-of-land-management-authentication
  summary_line: none/oauth2/openIdConnect · 6 schemes
- kind: domain-security
  name: Bureau Of Land Management Domain Security
  slug: bureau-of-land-management-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bureau Of Land Management Vulnerability Disclosure
  slug: bureau-of-land-management-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: bureau-of-land-management
tags:
- Environment
- Federal-Government
- Land
- Resources
- GIS
- Geospatial
- Mining
- Public-Lands
- Open-Data
- OGC
- Cadastral
- Recreation
- Grazing
- ArcGIS
- DCAT
- Conservation
- Mapping
website: https://www.blm.gov
---
