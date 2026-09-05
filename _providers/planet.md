---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.6
  scored_at: '2026-09-04'
api_count: 6
apis:
- description: Programmatically search Planet's imagery catalog by geometry, date range, cloud cover and other filters, then discover the items and downloadable assets that match. Supports item search, asset activat
  name: Planet Data API
  slug: planet-data-api
- description: Request downloads and cloud delivery of Planet imagery, apply raster and band tools (clipping, harmonization, composites), and deliver results to cloud storage destinations.
  name: Planet Orders API
  slug: planet-orders-api
- description: Set up continuous, hands-off cloud delivery of new imagery and Planetary Variables for an area of interest as it becomes available.
  name: Planet Subscriptions API
  slug: planet-subscriptions-api
- description: Access and download Planet's global and regional basemap mosaics, list series and quads, and retrieve mosaic metadata.
  name: Planet Basemaps API
  slug: planet-basemaps-api
- description: Command high-resolution SkySat and Pelican satellites to capture new imagery of a target, manage tasking orders, and track capture status.
  name: Planet Tasking API
  slug: planet-tasking-api
- description: Save and manage reusable areas of interest (feature collections) that can be referenced across the Data, Orders, Subscriptions and Tasking APIs.
  name: Planet Features API
  slug: planet-features-api
artifact_total: 12
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.planet.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.planet.com/develop/apis/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.planet.com/develop/apis/data/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.planet.com/guides/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.planet.com/develop/authentication/
- group: build
  title: ''
  type: SDKs
  url: https://docs.planet.com/develop/sdks/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.planet.com/develop/changelog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.planet.com
- group: operate
  title: ''
  type: Support
  url: https://support.planet.com
- group: operate
  title: ''
  type: Community
  url: https://community.planet.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.planet.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.planet.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.planet.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/planetlabs
- group: company
  title: ''
  type: Blog
  url: https://www.planet.com/pulse/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/planet-labs
- group: build
  title: ''
  type: Packages
  url: packages/planet-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/planet-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/planet-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/planet-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/planet-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/planet-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/planet-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/planet-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/planet-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/planet-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/planet-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/planet-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/planet-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/planet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.planet.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/planet-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.planet.com/security/
created: '2026-07-17'
description: Planet Labs PBC operates the largest constellation of Earth-imaging satellites, capturing a daily scan of the planet's landmass and delivering that imagery, along with derived Planetary Variables and analytics, through a suite of public developer APIs. The Planet Platform exposes a Data API for searching the imagery catalog, an Orders API for requesting and delivering scenes, a Subscriptions API for continuous cloud delivery, a Basemaps API for mosaics, a Tasking API for commanding high-resolution SkySat and Pelican captures, and a Features API for managing areas of interest. All APIs are served from api.planet.com and secured with API keys (HTTP Basic) or OAuth2/OIDC through login.planet.com. Planet ships an official Python SDK and CLI, an experimental Model Context Protocol server, QGIS and ArcGIS plugins, and a large open-source notebook collection. Planet is a portfolio company of DCVC.
image: https://cdn.sanity.io/images/hvd5n54p/production/e3f218dc0fbfed32b27eca2c22c45fce2586acfb-1920x1080.jpg
layout: provider
mcp_servers:
- description: 'Official experimental Model Context Protocol server from Planet, built on the Planet Python SDK. Runs locally over stdio and lets an AI agent (Claude Desktop, Claude Code, Gemini CLI, GitHub Copilot) '
  name: Planet MCP Server
  slug: planet-mcp-server
modified: '2026-07-20'
name: Planet
nav: Providers
network: true
overview: 'Planet publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Satellite Imagery, Earth Observation, Geospatial, Remote Sensing, and Mapping.


  Planet''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, pricing, and 26 more developer resources.'
random_paper: 14
scopes:
- name: Planet Scopes
  scope_count: 5
  slug: planet-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 5.3
    developer_ergonomics: 71.4
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 39.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/planet/refs/heads/main/screenshots/planet-2026-09-02T151406.png
security:
- kind: authentication
  name: Planet Authentication
  slug: planet-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Planet Domain Security
  slug: planet-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Planet Vulnerability Disclosure
  slug: planet-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Planet Trust Center
  slug: planet-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 42001:2023, ISO 9001:2015, UK Cyber Essentials, CMMC Level 2
slug: planet
tags:
- Satellite Imagery
- Earth Observation
- Geospatial
- Remote Sensing
- Mapping
- Analytics
- Location
- Data
- GIS
- OGC
- STAC
- WMTS
- Company
website: https://docs.planet.com
---
