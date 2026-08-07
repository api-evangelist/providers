---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Ordnance Survey Agentic Access
  operation_count: 62
  slug: ordnance-survey-agentic-access
  summary_line: 62 operations · 1 acting
api_count: 12
apis:
- description: OGC API - Features conformant access to the OS National Geographic Database, serving building, land, address, and transport feature collections as GeoJSON. The OpenAPI 3.0.1 description is served live
  name: OS NGD API - Features
  slug: os-ngd-api-features
- description: OGC API - Tiles conformant vector tile service over the OS National Geographic Database, including tile matrix sets and styles. The OpenAPI 3.0.1 description is served live and anonymously at /api.
  name: OS NGD API - Tiles
  slug: os-ngd-api-tiles
- description: 'Automated bulk download of OS OpenData and OS Premium datasets. The OpenData half of this API answers anonymously with no key - 26 open products including OS Open UPRN, OS Open TOID, Code-Point Open, '
  name: OS Downloads API
  slug: os-downloads-api
- description: High-precision GNSS data from the OS Net network of continuously operating reference stations across Great Britain, including station metadata, health, and RINEX observation files.
  name: OS Net API
  slug: os-net-api
- description: Address search and geocoding over AddressBase Premium - every UPRN in the United Kingdom, Jersey, Guernsey, and the Isle of Man, with current, provisional, and historic address records and TOID cross-
  name: OS Places API
  slug: os-places-api
- description: A geographic directory of identifiable places, roads, and settlements in Great Britain, with find and nearest operations.
  name: OS Names API
  slug: os-names-api
- description: Resolves the relationships between properties, streets, and OS MasterMap identifiers - UPRN to TOID to USRN - which is the join key between OS data, HM Land Registry records, and local authority prope
  name: OS Linked Identifiers API
  slug: os-linked-identifiers-api
- description: 'Matched and cleansed supplied address strings against OS authoritative addressing data, returning a matched AddressBase record and confidence score. WITHDRAWN: end of life 31 March 2026, announced 24 '
  name: OS Match & Cleanse API (withdrawn)
  slug: os-match-and-cleanse-api
- description: OGC Web Feature Service (WFS 2.0.0) over OS MasterMap and premium feature data, with getCapabilities, describeFeatureType, and getFeature operations plus a product archive. XML/WFS rather than OpenAPI
  name: OS Features API
  slug: os-features-api
- description: Pre-rendered raster map tiles in multiple OS styles, served as OGC WMTS and as ZXY tiles.
  name: OS Maps API
  slug: os-maps-api
- description: Vector tile service delivering detailed OS MasterMap data as styleable vector tiles.
  name: OS Vector Tile API
  slug: os-vector-tile-api
- description: OAuth 2.0 client credentials token service issuing time-limited access tokens for OS Data Hub APIs, so project API keys need not be embedded in browser code. The token URL is https://api.os.uk/oauth2/
  name: OS OAuth 2 API
  slug: os-oauth2-api
artifact_total: 30
collections:
- collection_type: postman
  name: Ordnance Survey Download API
  slug: postman-ordnance-survey-downloads
- collection_type: postman
  name: OS Features API
  slug: postman-ordnance-survey-features-wfs-openapi
- collection_type: postman
  name: OS Linked Identifiers API
  slug: postman-ordnance-survey-linked-identifiers-openapi
- collection_type: postman
  name: OS Maps API
  slug: postman-ordnance-survey-maps-openapi
- collection_type: postman
  name: OS Names API
  slug: postman-ordnance-survey-names-openapi
- collection_type: postman
  name: OS NGD API – Features
  slug: postman-ordnance-survey-ngd-features-openapi
- collection_type: postman
  name: OS NGD API - Tiles
  slug: postman-ordnance-survey-ngd-tiles-openapi
- collection_type: postman
  name: OS Net API
  slug: postman-ordnance-survey-osnet
- collection_type: postman
  name: OS Places API
  slug: postman-ordnance-survey-places-openapi
- collection_type: postman
  name: OS Vector Tiles API
  slug: postman-ordnance-survey-vector-tile-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ordnance-survey/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ordnance-survey-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ordnance-survey-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ordnance-survey-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ordnance-survey-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.ordnancesurvey.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://osdatahub.os.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.os.uk/os-apis
- group: auth
  title: ''
  type: Authentication
  url: https://docs.os.uk/os-apis/core-concepts/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.os.uk/os-apis/core-concepts/getting-started-with-an-api-project
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.os.uk/os-apis/core-concepts/rate-limiting-policy
- group: commercial
  title: ''
  type: Plans
  url: https://osdatahub.os.uk/plans
- group: other
  title: ''
  type: OpenData
  url: https://api.os.uk/downloads/v1/products
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OrdnanceSurvey
- group: build
  title: ''
  type: SDK
  url: https://github.com/OrdnanceSurvey/osdatahub
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.os.uk/os-apis/llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/ordnance-survey-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ordnance-survey-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ordnance-survey-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/ordnance-survey-api-catalog.json
- group: other
  title: ''
  type: ContentSignal
  url: well-known/ordnance-survey-docs-robots.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ordnance-survey-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ordnance-survey-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/ordnance-survey-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ordnance-survey-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ordnance-survey-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://osdatahub.os.uk/support/status
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.os.uk/os-apis/accessing-os-apis/os-match-and-cleanse-api/end-of-life-information
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ordnance-survey-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.ordnancesurvey.co.uk/governance/policies/vulnerability-disclosure
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ordnance-survey-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ordnance-survey-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ordnance-survey-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.os.uk/os-apis/service-and-data-status/change-log
- group: design
  title: ''
  type: Components
  url: components/ordnance-survey-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ordnance-survey-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ordnance-survey-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ordnance-survey-plans.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/ordnance-survey-authenticate.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/ordnance-survey-resolve-address-to-uprn.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/ordnance-survey-join-property-identifiers.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/ordnance-survey-query-ngd-features.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/ordnance-survey-download-opendata.md
- group: docs
  title: ''
  type: APIReference
  url: https://docs.os.uk/os-apis/accessing-os-apis
- group: start
  title: ''
  type: Quickstart
  url: https://docs.os.uk/os-apis/core-concepts/getting-started-with-an-api-project
- group: operate
  title: ''
  type: Support
  url: https://osdatahub.os.uk/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.os.uk/os-apis/core-concepts/faqs
- group: company
  title: ''
  type: Blog
  url: https://www.ordnancesurvey.co.uk/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://osdatahub.os.uk/plans
- group: start
  title: ''
  type: SignUp
  url: https://osdatahub.os.uk/register
- group: start
  title: ''
  type: Login
  url: https://osdatahub.os.uk/signIn
- group: commercial
  title: ''
  type: TermsOfService
  url: https://osdatahub.os.uk/legal/termsConditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ordnancesurvey.co.uk/governance/policies/privacy
- group: learn
  title: ''
  type: Tutorials
  url: https://labs.os.uk/public/os-data-hub-tutorials/
- group: other
  title: ''
  type: Accessibility
  url: https://docs.os.uk/os-apis/extra-links/accessibility
- group: commercial
  title: ''
  type: PlannedMaintenance
  url: https://docs.os.uk/os-apis/service-and-data-status/planned-maintenance
created: '2026-07-26'
description: 'Ordnance Survey is Great Britain''s national mapping agency, a government-owned company that maintains the addressing and mapping layer the UK property market runs on - the Unique Property Reference Number (UPRN), the TOID, AddressBase, and the OS National Geographic Database. The UK has no MLS; residential listings sit behind the Rightmove/Zoopla duopoly and agency CRM software, so the open layer in this market is public-sector rather than private, and OS is one half of it alongside HM Land Registry. Its API posture is unusually honest for this sector - the OS Data Hub is a self-serve developer portal with real machine-readable contracts, including OGC-conformant OpenAPI 3.0 documents served live and anonymously at api.os.uk for OS NGD API - Features and Tiles, plus published OpenAPI for the OS Downloads and OS Net APIs. The split that matters is licensing, not reachability: OS OpenData products (OS Open UPRN, OS Open TOID, Code-Point Open, OS Open Names, Boundary-Line, OS
  Open Linked Identifiers) are free and downloadable with no API key at all through the OS Downloads API, while the premium addressing and mapping products behind OS Places API, OS Features API, and the NGD collections require a paid Premium plan or Public Sector Geospatial Agreement (PSGA) membership. RESO plays no part here - the Real Estate Standards Organization standards are a US MLS construct and appear nowhere in the OS estate. Home market is the United Kingdom.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
mcp_servers:
- description: ''
  name: ordnance-survey-mcp.yml
  slug: ordnance-survey-mcpyml
modified: '2026-07-26'
name: Ordnance Survey
nav: Providers
network: true
overview: 'Ordnance Survey publishes 10 APIs on the [APIs.io](https://apis.io/) network, including OS NGD API - Features, OS NGD API - Tiles, OS Downloads API, and 7 more. Tagged areas include Real Estate, United Kingdom, Land Registry, Geospatial, and Addressing.


  Ordnance Survey''s developer surface includes authentication, documentation, getting-started guide, SDKs, sandbox, changelog, API reference, and 49 more developer resources.'
plans:
- name: Ordnance Survey Plans
  plan_count: 3
  slug: ordnance-survey-plans
random_paper: 104
rate_limits:
- limit_count: 3
  name: Ordnance Survey Rate Limits
  slug: ordnance-survey-rate-limits
scopes:
- name: Ordnance Survey Scopes
  scope_count: 1
  slug: ordnance-survey-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: exemplar
  composite: 67.2
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 50.8
    developer_ergonomics: 73.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 86.8
  previous_composite: 67.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 60.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 75.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Ordnance Survey Authentication
  slug: ordnance-survey-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Ordnance Survey Domain Security
  slug: ordnance-survey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ordnance Survey Vulnerability Disclosure
  slug: ordnance-survey-vulnerability-disclosure
  summary_line: Hackerone · security.txt
slug: ordnance-survey
tags:
- Real Estate
- United Kingdom
- Land Registry
- Geospatial
- Addressing
- Open Data
- Property Data
- PropTech
- Government
- Mapping
- OGC
- UPRN
- National Mapping
- GNSS
- Vector Tiles
website: https://www.ordnancesurvey.co.uk/
---
