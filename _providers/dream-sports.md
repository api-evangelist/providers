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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.7
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 154
  human_in_the_loop: 4
  name: Dream Sports Agentic Access
  operation_count: 254
  slug: dream-sports-agentic-access
  summary_line: 254 operations · 154 acting · 4 human-in-the-loop
api_count: 62
apis:
- description: First-party Model Context Protocol server (stdio transport) published by Dream Horizon that exposes Odin — Dream Sports' internal developer platform — to agents. It adapts 45 documented tools onto the
  name: Odin MCP Server
  slug: odin-mcp-server
- description: The Access Keys API from Dream Sports — 2 operation(s) for access keys.
  name: Dream Sports Access Keys API
  slug: dream-sports-access-keys-api
- description: The AccessKeys API from Dream Sports — 1 operation(s) for accesskeys.
  name: Dream Sports Access Keys API
  slug: dream-sports-accesskeys-api
- description: The Account API from Dream Sports — 4 operation(s) for account.
  name: Dream Sports Account API
  slug: dream-sports-account-api
- description: The Acquisition API from Dream Sports — 6 operation(s) for acquisition.
  name: Dream Sports Acquisition API
  slug: dream-sports-acquisition-api
- description: The Admin API from Dream Sports — 1 operation(s) for admin.
  name: Dream Sports Admin API
  slug: dream-sports-admin-api
- description: Admin-only console user operations — user onboarding and updates that include project IDs (stored in Firebase custom claims). Requires appropriate admin authorization at the gateway.
  name: Dream Sports Admin - Console Users API
  slug: dream-sports-admin-console-users-api
- description: The Apps API from Dream Sports — 10 operation(s) for apps.
  name: Dream Sports Apps API
  slug: dream-sports-apps-api
- description: Authentication operations — Google login and token refresh
  name: Dream Sports Auth API
  slug: dream-sports-auth-api
- description: The Authentication API from Dream Sports — 7 operation(s) for authentication.
  name: Dream Sports Authentication API
  slug: dream-sports-authentication-api
- description: APIs for managing Behaviour Tags. Behaviour Tags define user segments and their exposure rules for CTAs. They control which CTAs are shown or hidden to specific user groups based on session limits, ti
  name: Dream Sports Behaviour Tags API
  slug: dream-sports-behaviour-tags-api
- description: The Cache Management API from Dream Sports — 1 operation(s) for cache management.
  name: Dream Sports Cache Management API
  slug: dream-sports-cache-management-api
- description: Client SDK operations — endpoints consumed by the SDK for active journeys and state machine snapshots
  name: Dream Sports Client SDK API
  slug: dream-sports-client-sdk-api
- description: The Collaborators API from Dream Sports — 2 operation(s) for collaborators.
  name: Dream Sports Collaborators API
  slug: dream-sports-collaborators-api
- description: The Communication API from Dream Sports — 2 operation(s) for communication.
  name: Dream Sports Communication API
  slug: dream-sports-communication-api
- description: System configuration endpoints (labels, priorities, platforms, etc.)
  name: Dream Sports Configuration API
  slug: dream-sports-configuration-api
- description: Console user management via Firebase Admin SDK
  name: Dream Sports Console Users API
  slug: dream-sports-console-users-api
- description: 'APIs for managing CTA lifecycle status transitions. CTAs move through states: DRAFT → SCHEDULED → LIVE → PAUSED → CONCLUDED/TERMINATED.'
  name: Dream Sports CTA Status API
  slug: dream-sports-cta-status-api
- description: APIs for managing Call-to-Actions (CTAs). Includes CRUD operations for creating, updating, retrieving, and listing CTAs with filtering and pagination support.
  name: Dream Sports CT As API
  slug: dream-sports-ctas-api
- description: The Deployments API from Dream Sports — 2 operation(s) for deployments.
  name: Dream Sports Deployments API
  slug: dream-sports-deployments-api
- description: The Device-Bound Authentication API from Dream Sports — 2 operation(s) for device-bound authentication.
  name: Dream Sports Device-Bound Authentication API
  slug: dream-sports-device-bound-authentication-api
- description: 'APIs for managing Events. Events define the structure and properties of user actions that can trigger CTAs. Events include event names and their associated properties with types, expected values, and '
  name: Dream Sports Events API
  slug: dream-sports-events-api
- description: Event schema management — create, update, and manage event definitions and their properties
  name: Dream Sports Events Catalog API
  slug: dream-sports-events-catalog-api
- description: APIs for retrieving filter values used in the admin UI. Provides available options for tags, teams, statuses, behaviour tags, and creators.
  name: Dream Sports Filters API
  slug: dream-sports-filters-api
- description: The Guest Authentication API from Dream Sports — 1 operation(s) for guest authentication.
  name: Dream Sports Guest Authentication API
  slug: dream-sports-guest-authentication-api
- description: The Health API from Dream Sports — 2 operation(s) for health.
  name: Dream Sports Health API
  slug: dream-sports-health-api
- description: The Healthcheck API from Dream Sports — 2 operation(s) for healthcheck.
  name: Dream Sports Healthcheck API
  slug: dream-sports-healthcheck-api
- description: Journey behaviour tag management — define and manage behaviour tags linked to journeys
  name: Dream Sports Journey Behaviour API
  slug: dream-sports-journey-behaviour-api
- description: 'Journey lifecycle status transitions. Journeys move through states: DRAFT -> SCHEDULED -> LIVE -> PAUSED -> CONCLUDED/TERMINATED. Each status transition has its own dedicated endpoint.'
  name: Dream Sports Journey Lifecycle API
  slug: dream-sports-journey-lifecycle-api
- description: Test journey operations — create and remove test journeys for validating behaviour before going live
  name: Dream Sports Journey Test API
  slug: dream-sports-journey-test-api
- description: Journey management operations — create, read, update, and delete journeys
  name: Dream Sports Journeys API
  slug: dream-sports-journeys-api
- description: The Key Management API from Dream Sports — 1 operation(s) for key management.
  name: Dream Sports Key Management API
  slug: dream-sports-key-management-api
- description: The Metrics API from Dream Sports — 1 operation(s) for metrics.
  name: Dream Sports Metrics API
  slug: dream-sports-metrics-api
- description: Nudge preview management — create, update, and retrieve nudge preview templates with TTL configuration
  name: Dream Sports Nudge Preview API
  slug: dream-sports-nudge-preview-api
- description: APIs for managing Nudge Previews. Nudge Previews are used to preview nudge templates before they are used in CTAs. The preview includes the nudge template and TTL (time-to-live) configuration.
  name: Dream Sports Nudge Previews API
  slug: dream-sports-nudge-previews-api
- description: The OIDC API from Dream Sports — 7 operation(s) for oidc.
  name: Dream Sports OIDC API
  slug: dream-sports-oidc-api
- description: The OIDC Client Management API from Dream Sports — 3 operation(s) for oidc client management.
  name: Dream Sports OIDC Client Management API
  slug: dream-sports-oidc-client-management-api
- description: The OIDC Client Scope Management API from Dream Sports — 1 operation(s) for oidc client scope management.
  name: Dream Sports OIDC Client Scope Management API
  slug: dream-sports-oidc-client-scope-management-api
- description: The OIDC Discovery API from Dream Sports — 1 operation(s) for oidc discovery.
  name: Dream Sports OIDC Discovery API
  slug: dream-sports-oidc-discovery-api
- description: The OIDC Scope Management API from Dream Sports — 2 operation(s) for oidc scope management.
  name: Dream Sports OIDC Scope Management API
  slug: dream-sports-oidc-scope-management-api
- description: The Openapi API from Dream Sports — 1 operation(s) for openapi.
  name: Dream Sports Openapi API
  slug: dream-sports-openapi-api
- description: The Openapi.{type} API from Dream Sports — 1 operation(s) for openapi.{type}.
  name: Dream Sports Openapi.{type} API
  slug: dream-sports-openapi-type-api
- description: Organization management endpoints
  name: Dream Sports Organizations API
  slug: dream-sports-organizations-api
- description: The Password API from Dream Sports — 3 operation(s) for password.
  name: Dream Sports Password API
  slug: dream-sports-password-api
- description: The Passwordless API from Dream Sports — 6 operation(s) for passwordless.
  name: Dream Sports Passwordless API
  slug: dream-sports-passwordless-api
- description: Project management endpoints
  name: Dream Sports Projects API
  slug: dream-sports-projects-api
- description: The Provider API from Dream Sports — 1 operation(s) for provider.
  name: Dream Sports Provider API
  slug: dream-sports-provider-api
- description: The Public Keys API from Dream Sports — 1 operation(s) for public keys.
  name: Dream Sports Public Keys API
  slug: dream-sports-public-keys-api
- description: The Releases API from Dream Sports — 4 operation(s) for releases.
  name: Dream Sports Releases API
  slug: dream-sports-releases-api
- description: Reporting and download endpoints
  name: Dream Sports Reports API
  slug: dream-sports-reports-api
- description: Test run management endpoints
  name: Dream Sports Runs API
  slug: dream-sports-runs-api
- description: APIs for SDK clients to interact with Thunder. These endpoints handle app launch, state machine synchronization, and nudge preview retrieval for mobile and web clients.
  name: Dream Sports SDK API
  slug: dream-sports-sdk-api
- description: The Session Management API from Dream Sports — 5 operation(s) for session management.
  name: Dream Sports Session Management API
  slug: dream-sports-session-management-api
- description: The Sessions API from Dream Sports — 1 operation(s) for sessions.
  name: Dream Sports Sessions API
  slug: dream-sports-sessions-api
- description: The Social API from Dream Sports — 6 operation(s) for social.
  name: Dream Sports Social API
  slug: dream-sports-social-api
- description: The Tenants API from Dream Sports — 2 operation(s) for tenants.
  name: Dream Sports Tenants API
  slug: dream-sports-tenants-api
- description: Test case management endpoints
  name: Dream Sports Tests API
  slug: dream-sports-tests-api
- description: The Token Exchange API from Dream Sports — 1 operation(s) for token exchange.
  name: Dream Sports Token Exchange API
  slug: dream-sports-token-exchange-api
- description: The Token Management API from Dream Sports — 1 operation(s) for token management.
  name: Dream Sports Token Management API
  slug: dream-sports-token-management-api
- description: The User API from Dream Sports — 2 operation(s) for user.
  name: Dream Sports User API
  slug: dream-sports-user-api
- description: The User Flow Block API from Dream Sports — 3 operation(s) for user flow block.
  name: Dream Sports User Flow Block API
  slug: dream-sports-user-flow-block-api
- description: User management endpoints
  name: Dream Sports Users API
  slug: dream-sports-users-api
artifact_total: 69
asyncapis:
- description: ''
  name: Dream Sports Webhooks
  slug: dream-sports-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dream-sports-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dream-sports-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dreamsports.group/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dreamhorizon.org/
- group: docs
  title: ''
  type: Documentation
  url: https://dreamhorizon.org/projects
- group: docs
  title: ''
  type: APIReference
  url: https://guardianhq.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://guardianhq.io/docs/
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/HrJZCrkeAs
- group: company
  title: ''
  type: Blog
  url: https://blog.dream11engineering.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dream-horizon-org
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dreamsports.group/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dreamsports.group/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://github.com/dream-horizon-org/logwise/blob/master/SECURITY.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dream-sports-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/dream-sports-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dream-sports-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dream-sports-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/dream-sports-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dream-sports-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/dream-sports-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dream-sports-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dream-sports-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dream-sports-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dream-sports-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dream-sports-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dream-sports-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dream-sports-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dream-sports-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dream-sports-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dream-sports-webhooks.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://dream-horizon-org.github.io/odin/docs/roadmap/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: 'Dream Sports is India''s largest sports technology company, founded by Harsh Jain and Bhavit Sheth, whose consumer brands include Dream11 (fantasy sports), FanCode (sports content, streaming and commerce), DreamSetGo (sports travel and experiences), Dream Cricket, Dream Money and DreamStreet, alongside the Dream Sports Foundation. Its public machine-readable API surface is not a consumer product API but two engineering surfaces: the "Login with Dream11" OpenID Connect identity service at auth.dream11.com, which publishes an OIDC discovery document, and Dream Horizon (also branded HorizonOS) — the company''s open-source initiative that releases the platform engineering stack built to run Dream11 at 250M+ users. Dream Horizon publishes real OpenAPI 3.x specifications for Guardian (authentication and authorization), Checkmate (test management), Raven and Raven Thunder (in-app messaging and journeys), Delivr and DOTA (over-the-air mobile updates), protobuf service definitions for
  Odin (its internal developer platform), a first-party stdio MCP server for Odin, an llms.txt, and client SDKs published to npm under the @d11 scope and to LuaRocks under the dream11 namespace.'
image: https://www.dreamsports.group/images/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: dream-sports-mcp.yml
  slug: dream-sports-mcpyml
modified: '2026-08-04'
name: Dream Sports
nav: Providers
network: true
overview: 'Dream Sports publishes 61 APIs on the [APIs.io](https://apis.io/) network, including Access Keys API, Account API, and 59 more. Tagged areas include Company, sports-technology, fantasy-sports, open-source, and developer-tools.


  The Dream Sports catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dream Sports'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, authentication, and 25 more developer resources.'
random_paper: 89
scopes:
- name: Dream Sports Scopes
  scope_count: 7
  slug: dream-sports-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 48.4
  delta: -1.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 56.4
    developer_ergonomics: 75.5
    discoverability: 77.8
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 12.5
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dream-sports/refs/heads/main/screenshots/dream-sports-2026-08-07T164521.png
security:
- kind: authentication
  name: Dream Sports Authentication
  slug: dream-sports-authentication
  summary_line: apiKey/http/openIdConnect · 6 schemes
- kind: domain-security
  name: Dream Sports Domain Security
  slug: dream-sports-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dream Sports Vulnerability Disclosure
  slug: dream-sports-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: dream-sports
tags:
- Company
- sports-technology
- fantasy-sports
- open-source
- developer-tools
- platform-engineering
- authentication
- openid-connect
- oauth2
- mobile
- react-native
- devops
- observability
- test-management
- ota-updates
- feature-flags
- india
- mcp
- agent-native
website: https://www.dreamsports.group/
---
