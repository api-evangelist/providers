---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - scopes
  - security
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
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Landgate Agentic Access
  operation_count: 27
  slug: landgate-agentic-access
  summary_line: 27 operations
api_count: 10
apis:
- description: Landgate's customer identity provider, running PingFederate. The OpenID Connect discovery document is served anonymously (HTTP 200, 2026-07-26) at /.well-known/openid-configuration and is saved verbat
  name: MyLandgate OpenID Connect / OAuth 2.0 (PingFederate)
  slug: mylandgate-openid-connect
- baseURL: https://public-services.slip.wa.gov.au/public/rest/services
  baseurl_source: declared
  description: Dataset (package) discovery and retrieval
  name: Landgate Datasets API
  slug: landgate-datasets-api
- baseURL: https://public-services.slip.wa.gov.au/public/rest/services
  baseurl_source: declared
  description: Autocomplete, resource search and the DCAT catalog
  name: Landgate Discovery API
  slug: landgate-discovery-api
- baseURL: https://public-services.slip.wa.gov.au/public/rest/services
  baseurl_source: declared
  description: Publishing organizations and groups
  name: Landgate Organizations API
  slug: landgate-organizations-api
- baseURL: https://public-services.slip.wa.gov.au/public/rest/services
  baseurl_source: declared
  description: Feature query, identify and image export
  name: Landgate Query API
  slug: landgate-query-api
- baseURL: https://public-services.slip.wa.gov.au/public/rest/services
  baseurl_source: declared
  description: Server-level information and the services directory
  name: Landgate Server API
  slug: landgate-server-api
- baseURL: https://public-services.slip.wa.gov.au/public/rest/services
  baseurl_source: declared
  description: Map service and layer metadata
  name: Landgate Services API
  slug: landgate-services-api
- baseURL: https://public-services.slip.wa.gov.au/public/rest/services
  baseurl_source: declared
  description: Catalogue-level status and reference lists
  name: Landgate Site API
  slug: landgate-site-api
- baseURL: https://public-services.slip.wa.gov.au/public/rest/services
  baseurl_source: declared
  description: OGC Web Feature Service 2.0.0
  name: Landgate WFS API
  slug: landgate-wfs-api
- baseURL: https://public-services.slip.wa.gov.au/public/rest/services
  baseurl_source: declared
  description: OGC Web Map Service 1.3.0
  name: Landgate WMS API
  slug: landgate-wms-api
artifact_total: 21
collections:
- collection_type: open
  name: Data WA CKAN Action API (operated by Landgate)
  slug: open-landgate-data-wa-ckan
- collection_type: open
  name: API Collection
  slug: open-landgate-mylandgate-openid-configuration
- collection_type: open
  name: API Collection
  slug: open-landgate-slip-public-arcgis-rest-services
- collection_type: open
  name: Landgate SLIP Public Services (ArcGIS REST)
  slug: open-landgate-slip-public-arcgis
- collection_type: open
  name: Landgate SLIP Public OGC Web Services (WMS / WFS)
  slug: open-landgate-slip-public-ogc
- collection_type: open
  name: API Collection
  slug: open-landgate-slip-public-services-folder
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/landgate-slip-public-arcgis-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/landgate-slip-public-ogc-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/landgate-data-wa-ckan-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/landgate-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/landgate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/landgate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.landgate.wa.gov.au/
- group: company
  title: ''
  type: About
  url: https://www.landgate.wa.gov.au/about-us/
- group: docs
  title: ''
  type: Documentation
  url: https://www.landgate.wa.gov.au/location-data-and-services/discovering-landgate-data/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.landgate.wa.gov.au/location-data-and-services/discovering-landgate-data/licensing/
- group: other
  title: ''
  type: Licensing
  url: https://www.landgate.wa.gov.au/location-data-and-services/discovering-landgate-data/licensing/
- group: operate
  title: ''
  type: Support
  url: https://www.landgate.wa.gov.au/help-centre/
- group: start
  title: ''
  type: Login
  url: https://land-enquiry.app.landgate.wa.gov.au/
- group: start
  title: ''
  type: Portal
  url: https://www.data.wa.gov.au/
- group: agent
  title: ''
  type: WellKnown
  url: https://sign-on.app.landgate.wa.gov.au/.well-known/openid-configuration
- group: auth
  title: ''
  type: Authentication
  url: authentication/landgate-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/landgate-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/landgate-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/landgate-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/landgate-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/landgate-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/landgate-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.landgate.wa.gov.au/about-us/customer-news-and-media/news-and-media-articles/
- group: design
  title: ''
  type: Conformance
  url: conformance/landgate-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/landgate-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/landgate-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/landgate-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Landgate
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.landgate.wa.gov.au/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.landgate.wa.gov.au/about-us/customer-news-and-media/news-and-media-articles/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.landgate.wa.gov.au/help-centre/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.landgate.wa.gov.au/disclaimer
created: '2026-07-26'
description: Landgate is the Western Australian Land Information Authority — the WA government agency that maintains the state land titles register, values every rateable property in Western Australia, and curates the state's foundational location data (cadastre, tenure, property addresses, sales evidence, imagery, elevation, geographic names). In the Australian real estate value chain Landgate sits underneath the listing portals (REA Group's realestate.com.au and Domain) and underneath PEXA's electronic conveyancing rail as the authoritative source of the public land record for WA; since 2019 the automated land titling and registry operations have been operated under a commercial services arrangement while Landgate retains the Registrar of Titles function and the data custodianship. Its API posture is genuinely split and should not be overstated — a real, anonymously callable public surface exists (the SLIP Shared Location Information Platform ArcGIS REST directory plus OGC WMS/WFS services,
  and the Data WA CKAN Action API that Landgate operates for the whole WA public sector), while the richer registry and subscription data sits behind SLIP subscription, transaction, publication, broker, distributor and value-added-reseller licences that must be signed and, for bulk downloads, behind a MyLandgate account login. There is no developer portal, no published OpenAPI, no API key self-service, and no RESO involvement of any kind — RESO is a North American MLS standard and is absent from this Australian government registry.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Landgate MCP Server
  slug: landgate-mcp-server
modified: '2026-07-26'
name: Landgate
nav: Providers
network: true
overview: 'Landgate publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Discovery API, Organizations API, and 6 more. Tagged areas include Real-Estate, Australia, Land Registry, Title, and Valuation.


  Landgate''s developer surface includes documentation, pricing, support, developer portal, authentication, changelog, engineering blog, and 26 more developer resources.'
random_paper: 13
scopes:
- name: Landgate Scopes
  scope_count: 6
  slug: landgate-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 12.2
    developer_ergonomics: 47.0
    discoverability: 85.2
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 79.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/landgate/refs/heads/main/screenshots/landgate-2026-07-27T125338.png
security:
- kind: authentication
  name: Landgate Authentication
  slug: landgate-authentication
  summary_line: none/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Landgate Domain Security
  slug: landgate-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: landgate
tags:
- Real-Estate
- Australia
- Land Registry
- Title
- Valuation
- Property Data
- Open Data
- Geospatial
- Government
- Conveyancing
- PropTech
website: https://www.landgate.wa.gov.au/
---
