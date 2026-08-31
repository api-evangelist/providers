---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Ordnance Survey Agentic Access
  operation_count: 62
  slug: ordnance-survey-agentic-access
  summary_line: 62 operations · 1 acting
api_count: 10
apis:
- description: 'Matched and cleansed supplied address strings against OS authoritative addressing data, returning a matched AddressBase record and confidence score. WITHDRAWN: end of life 31 March 2026, announced 24 '
  name: OS Match & Cleanse API (withdrawn)
  slug: os-match-and-cleanse-api
- description: OAuth 2.0 client credentials token service issuing time-limited access tokens for OS Data Hub APIs, so project API keys need not be embedded in browser code. The token URL is https://api.os.uk/oauth2/
  name: OS OAuth 2 API
  slug: os-oauth2-api
- description: Find all addresses inside a bounding box.
  name: Ordnance Survey Bounding box API
  slug: ordnance-survey-bounding-box-api
- description: Retrieve information about collections
  name: Ordnance Survey Collections API
  slug: ordnance-survey-collections-api
- description: The Data Collections API from Ordnance Survey — 2 operation(s) for data collections.
  name: Ordnance Survey Data Collections API
  slug: ordnance-survey-data-collections-api
- description: Operations providing access to data packages. To access data packages you must supply a valid API key or OAuth 2 access token.
  name: Ordnance Survey Data Packages API
  slug: ordnance-survey-data-packages-api
- description: Retrieve features
  name: Ordnance Survey Features API
  slug: ordnance-survey-features-api
- description: A free string text search of OS Names, intended to be an ambiguous/fuzzy search.
  name: Ordnance Survey Find API
  slug: ordnance-survey-find-api
- description: Returns a metadata document describing the WFS service provided by the server as well as valid WFS operations and parameters.
  name: Ordnance Survey Get Capabilities API
  slug: ordnance-survey-getcapabilities-api
- description: Ordnance Survey NGD API – Features
  name: Ordnance Survey Landing Page API
  slug: ordnance-survey-landing-page-api
- description: Find the features closest to a given point.
  name: Ordnance Survey Nearest API
  slug: ordnance-survey-nearest-api
- description: Operations providing access to OpenData products.
  name: Ordnance Survey Open Data API
  slug: ordnance-survey-opendata-api
- description: Operations available to customers using the OpenData plan
  name: Ordnance Survey OS OpenData Users API
  slug: ordnance-survey-os-opendata-users-api
- description: Find all addresses in a polygon or multi-polygon object.
  name: Ordnance Survey Polygon API
  slug: ordnance-survey-polygon-api
- description: A search based on a property’s postcode
  name: Ordnance Survey Postcode API
  slug: ordnance-survey-postcode-api
- description: Find all addresses that intersect a given circle.
  name: Ordnance Survey Radius API
  slug: ordnance-survey-radius-api
- description: The Rinex API from Ordnance Survey — 5 operation(s) for rinex.
  name: Ordnance Survey Rinex API
  slug: ordnance-survey-rinex-api
- description: Service Metadata for OS Vector Tiles API
  name: Ordnance Survey Service Metadata API
  slug: ordnance-survey-service-metadata-api
- description: The Stations API from Ordnance Survey — 5 operation(s) for stations.
  name: Ordnance Survey Stations API
  slug: ordnance-survey-stations-api
- description: The Styles API from Ordnance Survey — 5 operation(s) for styles.
  name: Ordnance Survey Styles API
  slug: ordnance-survey-styles-api
- description: Access and download data for a specific tile
  name: Ordnance Survey Tile Request API
  slug: ordnance-survey-tile-request-api
- description: The Tile Sets API from Ordnance Survey — 2 operation(s) for tile sets.
  name: Ordnance Survey Tile Sets API
  slug: ordnance-survey-tile-sets-api
- description: The Tiling Schemes API from Ordnance Survey — 2 operation(s) for tiling schemes.
  name: Ordnance Survey Tiling Schemes API
  slug: ordnance-survey-tiling-schemes-api
- description: A search that takes a UPRN as the search parameter.
  name: Ordnance Survey UPRN API
  slug: ordnance-survey-uprn-api
- description: The Vector Tiles API from Ordnance Survey — 2 operation(s) for vector tiles.
  name: Ordnance Survey Vector Tiles API
  slug: ordnance-survey-vector-tiles-api
artifact_total: 51
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
- collection_type: open
  name: OS Features API
  slug: open-ordnance-survey-features-wfs
- collection_type: open
  name: OS Linked Identifiers API
  slug: open-ordnance-survey-linked-identifiers
- collection_type: open
  name: OS Maps API
  slug: open-ordnance-survey-maps
- collection_type: open
  name: OS Names API
  slug: open-ordnance-survey-names
- collection_type: open
  name: OS NGD API – Features
  slug: open-ordnance-survey-ngd-features
- collection_type: open
  name: OS NGD API - Tiles
  slug: open-ordnance-survey-ngd-tiles
- collection_type: open
  name: OS Places API
  slug: open-ordnance-survey-places
- collection_type: open
  name: OS Vector Tiles API
  slug: open-ordnance-survey-vector-tile
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ordnance-survey-ngd-features-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ordnance-survey-ngd-tiles-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ordnance-survey-downloads-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ordnance-survey-osnet-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ordnance-survey-places-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ordnance-survey-names-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ordnance-survey-linked-identifiers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ordnance-survey-features-wfs-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ordnance-survey-maps-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ordnance-survey-vector-tile-overlay.yaml
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
layout: provider
mcp_servers:
- description: A candidate MCP tool surface for the Ordnance Survey APIs, one tool per OpenAPI operation that an agent would realistically call. Every tool's source_operation points at a real path/operationId in a s
  name: Ordnance Survey MCP Server
  slug: ordnance-survey-mcp-server
modified: '2026-07-26'
name: Ordnance Survey
nav: Providers
network: true
overview: 'Ordnance Survey publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Bounding box API, Collections API, Data Collections API, and 20 more. Tagged areas include Real-Estate, United Kingdom, Land Registry, Geospatial, and Addressing.


  Ordnance Survey''s developer surface includes authentication, documentation, getting-started guide, SDKs, sandbox, changelog, API reference, and 59 more developer resources.'
plans:
- name: Ordnance Survey Plans
  plan_count: 3
  slug: ordnance-survey-plans
random_paper: 19
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
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 25
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 48.7
    commercial_clarity: 48.7
    contract_governance: 18.2
    contract_quality: 45.5
    developer_ergonomics: 68.5
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 68.4
  previous_composite: 60.1
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
    score: 68.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ordnance-survey/refs/heads/main/screenshots/ordnance-survey-2026-08-07T190917.png
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
- Real-Estate
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
