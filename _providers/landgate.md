---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Landgate Agentic Access
  operation_count: 27
  slug: landgate-agentic-access
  summary_line: 27 operations
api_count: 4
apis:
- description: The public tier of Landgate's Shared Location Information Platform (SLIP), served as an Esri ArcGIS Server 12.1 REST services directory. Confirmed anonymously reachable on 2026-07-26 with HTTP 200 and
  name: SLIP Public Services (ArcGIS REST)
  slug: slip-public-arcgis-rest-services
- description: OGC-standard web services fronting the same SLIP public data. A WMS 1.3.0 GetCapabilities document (56 layers) and a WFS 2.0.0 GetCapabilities document (38 feature types) were both retrieved anonymous
  name: SLIP Public OGC Web Services (WMS / WFS)
  slug: slip-public-ogc-services
- description: Landgate leads implementation of the WA Whole of Government Open Data Policy and operates data.wa.gov.au, whose catalogue runs CKAN with the standard /api/3/action surface exposed anonymously. Confirm
  name: Data WA CKAN Action API
  slug: data-wa-ckan-action-api
- description: Landgate's customer identity provider, running PingFederate. The OpenID Connect discovery document is served anonymously (HTTP 200, 2026-07-26) at /.well-known/openid-configuration and is saved verbat
  name: MyLandgate OpenID Connect / OAuth 2.0 (PingFederate)
  slug: mylandgate-openid-connect
artifact_total: 9
common:
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
  name: landgate-mcp.yml
  slug: landgate-mcpyml
modified: '2026-07-26'
name: Landgate
nav: Providers
network: true
overview: 'Landgate publishes 3 APIs on the [APIs.io](https://apis.io/) network: SLIP Public Services (ArcGIS REST), SLIP Public OGC Web Services (WMS / WFS), and Data WA CKAN Action API. Tagged areas include Real Estate, Australia, Land Registry, Title, and Valuation.


  Landgate''s developer surface includes documentation, pricing, support, developer portal, authentication, changelog, engineering blog, and 23 more developer resources.'
random_paper: 112
scopes:
- name: Landgate Scopes
  scope_count: 6
  slug: landgate-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 46.7
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 54.0
    developer_ergonomics: 38.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 64.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
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
- Real Estate
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
