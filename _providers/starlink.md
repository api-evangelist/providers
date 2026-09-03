---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 36
  human_in_the_loop: 3
  name: Starlink Agentic Access
  operation_count: 63
  slug: starlink-agentic-access
  summary_line: 63 operations · 36 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://starlink.com/api/public/v2
  baseurl_source: declared
  description: A low-latency JSON over HTTP streaming API for device telemetry, consumed by repeated small-batch POST requests with batchSize and maxLingerMs parameters. POST /public/v2/telemetry/stream returns comp
  name: Starlink Telemetry Stream API
  slug: starlink-telemetry-stream-api
- description: SpaceX's officially supported local gRPC API on Starlink hardware, defined in protobuf and published verbatim on GitHub as device.proto. The SpaceX.API.Device service exposes a single Handle RPC carry
  name: Starlink Local Device API
  slug: starlink-local-device-api
- description: 'An optional HTTPS server hosted on the Starlink WiFi router itself, enabled through a router config in the Starlink dashboard with an enterprise-managed TLS certificate, key, and CORS allowed-origins '
  name: Starlink Router Local HTTPS API
  slug: starlink-router-local-https-api
- description: 'The API behind space-safety.starlink.com, SpaceX''s free conjunction screening and maneuver coordination platform for satellite operators. Version 0.1 of the reference documents five resource groups - '
  name: Starlink Space Traffic Coordination API
  slug: starlink-space-traffic-coordination-api
- baseURL: https://starlink.com/api/public/v2
  baseurl_source: declared
  description: The Account API from Starlink — 3 operation(s) for account.
  name: Starlink Account API
  slug: starlink-account-api
- baseURL: https://starlink.com/api/public/v2
  baseurl_source: declared
  description: The Addresses API from Starlink — 2 operation(s) for addresses.
  name: Starlink Addresses API
  slug: starlink-addresses-api
- baseURL: https://starlink.com/api/public/v2
  baseurl_source: declared
  description: The Billing API from Starlink — 3 operation(s) for billing.
  name: Starlink Billing API
  slug: starlink-billing-api
- baseURL: https://starlink.com/api/public/v2
  baseurl_source: declared
  description: The Contacts API from Starlink — 2 operation(s) for contacts.
  name: Starlink Contacts API
  slug: starlink-contacts-api
- baseURL: https://starlink.com/api/public/v2
  baseurl_source: declared
  description: The Data Pools API from Starlink — 3 operation(s) for data pools.
  name: Starlink Data Pools API
  slug: starlink-data-pools-api
- baseURL: https://starlink.com/api/public/v2
  baseurl_source: declared
  description: The Flights API from Starlink — 1 operation(s) for flights.
  name: Starlink Flights API
  slug: starlink-flights-api
- baseURL: https://starlink.com/api/public/v2
  baseurl_source: declared
  description: The Managed Accounts API from Starlink — 2 operation(s) for managed accounts.
  name: Starlink Managed Accounts API
  slug: starlink-managed-accounts-api
- baseURL: https://starlink.com/api/public/v2
  baseurl_source: declared
  description: The Managed API from Starlink — 1 operation(s) for managed.
  name: Starlink Managed API
  slug: starlink-managed-api
- baseURL: https://starlink.com/api/public/v2
  baseurl_source: declared
  description: The Mobile API from Starlink — 3 operation(s) for mobile.
  name: Starlink Mobile API
  slug: starlink-mobile-api
- baseURL: https://starlink.com/api/public/v2
  baseurl_source: declared
  description: The Routers API from Starlink — 10 operation(s) for routers.
  name: Starlink Routers API
  slug: starlink-routers-api
- baseURL: https://starlink.com/api/public/v2
  baseurl_source: declared
  description: The Service Lines API from Starlink — 13 operation(s) for service lines.
  name: Starlink Service Lines API
  slug: starlink-service-lines-api
- baseURL: https://starlink.com/api/public/v2
  baseurl_source: declared
  description: The User Terminals API from Starlink — 6 operation(s) for user terminals.
  name: Starlink User Terminals API
  slug: starlink-user-terminals-api
artifact_total: 24
asyncapis:
- description: 'Event surface for Starlink enterprise device telemetry. Starlink exposes it as a poll-based JSON-over-HTTP stream rather than a broker: the consumer makes continuous small-batch POST requests to /publ'
  name: Starlink Telemetry Stream and Device Alerts
  slug: starlink-telemetry-asyncapi
collections:
- collection_type: open
  name: Starlink Public API
  slug: open-starlink-public-api-v2
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/starlink-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/SpaceExplorationTechnologies/enterprise-api/issues
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
  type: X-MCPServerCandidate
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
modified: '2026-07-25'
name: Starlink
nav: Providers
network: true
overview: 'Starlink publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Telemetry Stream API, Account API, Addresses API, and 10 more. Tagged areas include Telecommunications, United States, Satellite, Broadband, and Non-Terrestrial Networks.


  The Starlink catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Starlink''s developer surface includes documentation, getting-started guide, API reference, authentication, changelog, sandbox, developer portal, and 43 more developer resources.'
random_paper: 11
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
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 25
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 3.8
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 54.0
    developer_ergonomics: 47.0
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 59.2
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 63.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/starlink/refs/heads/main/screenshots/starlink-2026-08-17T082120.png
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
