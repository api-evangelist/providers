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
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 36
  human_in_the_loop: 3
  name: Starlink Agentic Access
  operation_count: 63
  slug: starlink-agentic-access
  summary_line: 63 operations · 36 acting · 3 human-in-the-loop
api_count: 7
apis:
- description: The Starlink Public API V2 manages accounts, addresses, contacts, service lines, user terminals, WiFi routers, data pools, and billing for business and enterprise Starlink accounts. The public OpenAPI
  name: Starlink Public API V2
  slug: starlink-public-api-v2
- description: A low-latency JSON over HTTP streaming API for device telemetry, consumed by repeated small-batch POST requests with batchSize and maxLingerMs parameters. POST /public/v2/telemetry/stream returns comp
  name: Starlink Telemetry Stream API
  slug: starlink-telemetry-stream-api
- description: A gated feature within the Starlink Public API V2 exposing Starlink Mobile radio access network data, usage and beam reliability timeseries, and map data, each partitioned by timestamp date and hour a
  name: Starlink Mobile Data API
  slug: starlink-mobile-data-api
- description: 'A single endpoint, POST /public/v2/flights/status, for posting real-time flight events from a Starlink-equipped aircraft. It is only callable from an aviation account and requires the Aviation flight '
  name: Starlink Aviation Flight Status API
  slug: starlink-aviation-flight-status-api
- description: SpaceX's officially supported local gRPC API on Starlink hardware, defined in protobuf and published verbatim on GitHub as device.proto. The SpaceX.API.Device service exposes a single Handle RPC carry
  name: Starlink Local Device API
  slug: starlink-local-device-api
- description: 'An optional HTTPS server hosted on the Starlink WiFi router itself, enabled through a router config in the Starlink dashboard with an enterprise-managed TLS certificate, key, and CORS allowed-origins '
  name: Starlink Router Local HTTPS API
  slug: starlink-router-local-https-api
- description: 'The API behind space-safety.starlink.com, SpaceX''s free conjunction screening and maneuver coordination platform for satellite operators. Version 0.1 of the reference documents five resource groups - '
  name: Starlink Space Traffic Coordination API
  slug: starlink-space-traffic-coordination-api
artifact_total: 15
asyncapis:
- description: 'Event surface for Starlink enterprise device telemetry. Starlink exposes it as a poll-based JSON-over-HTTP stream rather than a broker: the consumer makes continuous small-batch POST requests to /publ'
  name: Starlink Telemetry Stream and Device Alerts
  slug: starlink-telemetry-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.starlink.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://starlink.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://starlink.readme.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://starlink.readme.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://starlink.readme.io/reference
- group: docs
  title: ''
  type: SwaggerUI
  url: https://starlink.com/api/public/swagger/index.html?urls.primaryName=V2
- group: docs
  title: ''
  type: OpenAPI Source
  url: https://starlink.com/api/public/swagger/v2/swagger.json
- group: auth
  title: ''
  type: Authentication
  url: https://starlink.readme.io/docs/authentication
- group: auth
  title: ''
  type: Authentication
  url: authentication/starlink-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/starlink-scopes.yml
- group: other
  title: ''
  type: OpenIDConfiguration
  url: https://starlink.com/api/auth/.well-known/openid-configuration
- group: operate
  title: ''
  type: RateLimits
  url: https://starlink.readme.io/docs/rate-limits-1
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/starlink-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/starlink-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://starlink.readme.io/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/starlink-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/starlink-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://starlink.readme.io/docs/starlink-api-status
- group: operate
  title: ''
  type: Deprecation
  url: https://starlink.readme.io/docs/60-day-deprecation-policy
- group: design
  title: ''
  type: Conformance
  url: conformance/starlink-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/starlink-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/starlink-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/starlink-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/starlink-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/starlink-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/starlink-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/starlink-agentic-access.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/starlink-telemetry-asyncapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/starlink-public-api-v2-overlay.yaml
- group: other
  title: ''
  type: Protobuf
  url: proto/starlink-device.proto
- group: agent
  title: ''
  type: LlmsText
  url: https://starlink.readme.io/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/starlink-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/starlink-well-known.yml
- group: start
  title: ''
  type: Portal
  url: https://www.starlink.com/account/settings
- group: start
  title: ''
  type: Login
  url: https://www.starlink.com/account
- group: start
  title: ''
  type: SignUp
  url: https://www.starlink.com/account
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SpaceExplorationTechnologies
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/SpaceExplorationTechnologies/enterprise-api
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/starlink-security.txt
- group: auth
  title: ''
  type: Security
  url: https://starlink.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/starlink-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/starlink-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://starlink.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.starlink.com/updates
- group: commercial
  title: ''
  type: Pricing
  url: https://www.starlink.com/business
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.starlink.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.starlink.com/legal
created: '2026-07-25'
description: Starlink is the low-Earth-orbit satellite internet constellation operated by SpaceX from Hawthorne, California, delivering broadband and non-terrestrial connectivity to residential, business, maritime, aviation, and government customers in the United States and roughly a hundred other markets. In the telecom value chain Starlink is an access-network operator that sells connectivity directly to end customers and wholesales capacity to airlines, shipping lines, and mobile network operators, rather than a CPaaS aggregator or a GSMA-affiliated mobile network operator. Its API posture is unusually open for an access provider and unusually narrow in scope. The Starlink Public API V2 is fully documented in public at starlink.readme.io, its OpenAPI 3.0.4 description is downloadable anonymously from starlink.com with no login, and SpaceX publishes an official gRPC protobuf for the local device API on GitHub. But the API is operational rather than developer-product, covering account,
  service line, user terminal, router, billing, and telemetry management, and credentials are gated behind an enterprise or business Starlink account whose admin must mint a V2 service account. No CAMARA implementation, no GSMA Open Gateway participation, and no TM Forum Open API conformance was found anywhere in Starlink's published material.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: starlink-mcp.yml
  slug: starlink-mcpyml
modified: '2026-07-25'
name: Starlink
nav: Providers
network: true
overview: 'Starlink publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Public API V2, Telemetry Stream API, Mobile Data API, and 1 more. Tagged areas include Telecommunications, United States, Satellite, Broadband, and Non-Terrestrial Networks.


  The Starlink catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Starlink''s developer surface includes documentation, getting-started guide, API reference, authentication, changelog, sandbox, developer portal, and 41 more developer resources.'
random_paper: 60
rate_limits:
- limit_count: 3
  name: Starlink Rate Limits
  slug: starlink-rate-limits
scopes:
- name: Starlink Scopes
  scope_count: 5
  slug: starlink-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: strong
  composite: 59.8
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 58.7
    developer_ergonomics: 62.5
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 86.8
  previous_composite: 59.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 75.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Starlink Authentication
  slug: starlink-authentication
  summary_line: oauth2/http/mutualTLS · 4 schemes
- kind: domain-security
  name: Starlink Domain Security
  slug: starlink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Starlink Vulnerability Disclosure
  slug: starlink-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: starlink
tags:
- Telecommunications
- United States
- Satellite
- Broadband
- Non-Terrestrial Networks
- Connectivity
- Device Management
- Telemetry
- Aviation
- Maritime
- Enterprise
website: https://www.starlink.com/
---
