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
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 154
  human_in_the_loop: 4
  name: Dream Sports Agentic Access
  operation_count: 254
  slug: dream-sports-agentic-access
  summary_line: 254 operations · 154 acting · 4 human-in-the-loop
api_count: 8
apis:
- description: First-party Model Context Protocol server (stdio transport) published by Dream Horizon that exposes Odin — Dream Sports' internal developer platform — to agents. It adapts 45 documented tools onto the
  name: Odin MCP Server
  slug: odin-mcp-server
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Access Keys API from Dream Sports — 2 operation(s) for access keys.
  name: Dream Sports Access Keys API
  slug: dream-sports-access-keys-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The AccessKeys API from Dream Sports — 1 operation(s) for accesskeys.
  name: Dream Sports Access Keys API
  slug: dream-sports-accesskeys-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Account API from Dream Sports — 4 operation(s) for account.
  name: Dream Sports Account API
  slug: dream-sports-account-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Acquisition API from Dream Sports — 6 operation(s) for acquisition.
  name: Dream Sports Acquisition API
  slug: dream-sports-acquisition-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Admin API from Dream Sports — 1 operation(s) for admin.
  name: Dream Sports Admin API
  slug: dream-sports-admin-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: Admin-only console user operations — user onboarding and updates that include project IDs (stored in Firebase custom claims). Requires appropriate admin authorization at the gateway.
  name: Dream Sports Admin - Console Users API
  slug: dream-sports-admin-console-users-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Apps API from Dream Sports — 10 operation(s) for apps.
  name: Dream Sports Apps API
  slug: dream-sports-apps-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: Authentication operations — Google login and token refresh
  name: Dream Sports Auth API
  slug: dream-sports-auth-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Authentication API from Dream Sports — 7 operation(s) for authentication.
  name: Dream Sports Authentication API
  slug: dream-sports-authentication-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: APIs for managing Behaviour Tags. Behaviour Tags define user segments and their exposure rules for CTAs. They control which CTAs are shown or hidden to specific user groups based on session limits, ti
  name: Dream Sports Behaviour Tags API
  slug: dream-sports-behaviour-tags-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Cache Management API from Dream Sports — 1 operation(s) for cache management.
  name: Dream Sports Cache Management API
  slug: dream-sports-cache-management-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: Client SDK operations — endpoints consumed by the SDK for active journeys and state machine snapshots
  name: Dream Sports Client SDK API
  slug: dream-sports-client-sdk-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Collaborators API from Dream Sports — 2 operation(s) for collaborators.
  name: Dream Sports Collaborators API
  slug: dream-sports-collaborators-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Communication API from Dream Sports — 2 operation(s) for communication.
  name: Dream Sports Communication API
  slug: dream-sports-communication-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: System configuration endpoints (labels, priorities, platforms, etc.)
  name: Dream Sports Configuration API
  slug: dream-sports-configuration-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: Console user management via Firebase Admin SDK
  name: Dream Sports Console Users API
  slug: dream-sports-console-users-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: 'APIs for managing CTA lifecycle status transitions. CTAs move through states: DRAFT → SCHEDULED → LIVE → PAUSED → CONCLUDED/TERMINATED.'
  name: Dream Sports CTA Status API
  slug: dream-sports-cta-status-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: APIs for managing Call-to-Actions (CTAs). Includes CRUD operations for creating, updating, retrieving, and listing CTAs with filtering and pagination support.
  name: Dream Sports CT As API
  slug: dream-sports-ctas-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Deployments API from Dream Sports — 2 operation(s) for deployments.
  name: Dream Sports Deployments API
  slug: dream-sports-deployments-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Device-Bound Authentication API from Dream Sports — 2 operation(s) for device-bound authentication.
  name: Dream Sports Device-Bound Authentication API
  slug: dream-sports-device-bound-authentication-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: 'APIs for managing Events. Events define the structure and properties of user actions that can trigger CTAs. Events include event names and their associated properties with types, expected values, and '
  name: Dream Sports Events API
  slug: dream-sports-events-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: Event schema management — create, update, and manage event definitions and their properties
  name: Dream Sports Events Catalog API
  slug: dream-sports-events-catalog-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: APIs for retrieving filter values used in the admin UI. Provides available options for tags, teams, statuses, behaviour tags, and creators.
  name: Dream Sports Filters API
  slug: dream-sports-filters-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Guest Authentication API from Dream Sports — 1 operation(s) for guest authentication.
  name: Dream Sports Guest Authentication API
  slug: dream-sports-guest-authentication-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Health API from Dream Sports — 2 operation(s) for health.
  name: Dream Sports Health API
  slug: dream-sports-health-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Healthcheck API from Dream Sports — 2 operation(s) for healthcheck.
  name: Dream Sports Healthcheck API
  slug: dream-sports-healthcheck-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: Journey behaviour tag management — define and manage behaviour tags linked to journeys
  name: Dream Sports Journey Behaviour API
  slug: dream-sports-journey-behaviour-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: 'Journey lifecycle status transitions. Journeys move through states: DRAFT -> SCHEDULED -> LIVE -> PAUSED -> CONCLUDED/TERMINATED. Each status transition has its own dedicated endpoint.'
  name: Dream Sports Journey Lifecycle API
  slug: dream-sports-journey-lifecycle-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: Test journey operations — create and remove test journeys for validating behaviour before going live
  name: Dream Sports Journey Test API
  slug: dream-sports-journey-test-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: Journey management operations — create, read, update, and delete journeys
  name: Dream Sports Journeys API
  slug: dream-sports-journeys-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Key Management API from Dream Sports — 1 operation(s) for key management.
  name: Dream Sports Key Management API
  slug: dream-sports-key-management-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Metrics API from Dream Sports — 1 operation(s) for metrics.
  name: Dream Sports Metrics API
  slug: dream-sports-metrics-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: Nudge preview management — create, update, and retrieve nudge preview templates with TTL configuration
  name: Dream Sports Nudge Preview API
  slug: dream-sports-nudge-preview-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: APIs for managing Nudge Previews. Nudge Previews are used to preview nudge templates before they are used in CTAs. The preview includes the nudge template and TTL (time-to-live) configuration.
  name: Dream Sports Nudge Previews API
  slug: dream-sports-nudge-previews-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The OIDC API from Dream Sports — 7 operation(s) for oidc.
  name: Dream Sports OIDC API
  slug: dream-sports-oidc-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The OIDC Client Management API from Dream Sports — 3 operation(s) for oidc client management.
  name: Dream Sports OIDC Client Management API
  slug: dream-sports-oidc-client-management-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The OIDC Client Scope Management API from Dream Sports — 1 operation(s) for oidc client scope management.
  name: Dream Sports OIDC Client Scope Management API
  slug: dream-sports-oidc-client-scope-management-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The OIDC Discovery API from Dream Sports — 1 operation(s) for oidc discovery.
  name: Dream Sports OIDC Discovery API
  slug: dream-sports-oidc-discovery-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The OIDC Scope Management API from Dream Sports — 2 operation(s) for oidc scope management.
  name: Dream Sports OIDC Scope Management API
  slug: dream-sports-oidc-scope-management-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Openapi API from Dream Sports — 1 operation(s) for openapi.
  name: Dream Sports Openapi API
  slug: dream-sports-openapi-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Openapi.{type} API from Dream Sports — 1 operation(s) for openapi.{type}.
  name: Dream Sports Openapi.{type} API
  slug: dream-sports-openapi-type-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: Organization management endpoints
  name: Dream Sports Organizations API
  slug: dream-sports-organizations-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Password API from Dream Sports — 3 operation(s) for password.
  name: Dream Sports Password API
  slug: dream-sports-password-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Passwordless API from Dream Sports — 6 operation(s) for passwordless.
  name: Dream Sports Passwordless API
  slug: dream-sports-passwordless-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: Project management endpoints
  name: Dream Sports Projects API
  slug: dream-sports-projects-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Provider API from Dream Sports — 1 operation(s) for provider.
  name: Dream Sports Provider API
  slug: dream-sports-provider-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Public Keys API from Dream Sports — 1 operation(s) for public keys.
  name: Dream Sports Public Keys API
  slug: dream-sports-public-keys-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Releases API from Dream Sports — 4 operation(s) for releases.
  name: Dream Sports Releases API
  slug: dream-sports-releases-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: Reporting and download endpoints
  name: Dream Sports Reports API
  slug: dream-sports-reports-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: Test run management endpoints
  name: Dream Sports Runs API
  slug: dream-sports-runs-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: APIs for SDK clients to interact with Thunder. These endpoints handle app launch, state machine synchronization, and nudge preview retrieval for mobile and web clients.
  name: Dream Sports SDK API
  slug: dream-sports-sdk-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Session Management API from Dream Sports — 5 operation(s) for session management.
  name: Dream Sports Session Management API
  slug: dream-sports-session-management-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Sessions API from Dream Sports — 1 operation(s) for sessions.
  name: Dream Sports Sessions API
  slug: dream-sports-sessions-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Social API from Dream Sports — 6 operation(s) for social.
  name: Dream Sports Social API
  slug: dream-sports-social-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Tenants API from Dream Sports — 2 operation(s) for tenants.
  name: Dream Sports Tenants API
  slug: dream-sports-tenants-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: Test case management endpoints
  name: Dream Sports Tests API
  slug: dream-sports-tests-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Token Exchange API from Dream Sports — 1 operation(s) for token exchange.
  name: Dream Sports Token Exchange API
  slug: dream-sports-token-exchange-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The Token Management API from Dream Sports — 1 operation(s) for token management.
  name: Dream Sports Token Management API
  slug: dream-sports-token-management-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The User API from Dream Sports — 2 operation(s) for user.
  name: Dream Sports User API
  slug: dream-sports-user-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: The User Flow Block API from Dream Sports — 3 operation(s) for user flow block.
  name: Dream Sports User Flow Block API
  slug: dream-sports-user-flow-block-api
- baseURL: https://auth.dream11.com/
  baseurl_source: declared
  description: User management endpoints
  name: Dream Sports Users API
  slug: dream-sports-users-api
artifact_total: 129
asyncapis:
- description: ''
  name: Dream Sports Webhooks
  slug: dream-sports-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Delivr OTA Server Access Keys API
  slug: open-dream-sports-access-keys-api
- collection_type: open
  name: DOTA Access Keys API
  slug: open-dream-sports-accesskeys-api
- collection_type: open
  name: Dream Sports Account API
  slug: open-dream-sports-account-api
- collection_type: open
  name: Delivr OTA Server Acquisition API
  slug: open-dream-sports-acquisition-api
- collection_type: open
  name: Guardian Admin API
  slug: open-dream-sports-admin-api
- collection_type: open
  name: Raven Journey Admin - Console Users API
  slug: open-dream-sports-admin-console-users-api
- collection_type: open
  name: Dream Sports Apps API
  slug: open-dream-sports-apps-api
- collection_type: open
  name: Raven Journey Auth API
  slug: open-dream-sports-auth-api
- collection_type: open
  name: Delivr OTA Server Authentication API
  slug: open-dream-sports-authentication-api
- collection_type: open
  name: Thunder Admin Behaviour Tags API
  slug: open-dream-sports-behaviour-tags-api
- collection_type: open
  name: Guardian Cache Management API
  slug: open-dream-sports-cache-management-api
- collection_type: open
  name: Raven Journey Client SDK API
  slug: open-dream-sports-client-sdk-api
- collection_type: open
  name: Delivr OTA Server Collaborators API
  slug: open-dream-sports-collaborators-api
- collection_type: open
  name: Guardian integration endpoints Communication API
  slug: open-dream-sports-communication-api
- collection_type: open
  name: Checkmate Test Management Configuration API
  slug: open-dream-sports-configuration-api
- collection_type: open
  name: Raven Journey Console Users API
  slug: open-dream-sports-console-users-api
- collection_type: open
  name: Thunder Admin CTA Status API
  slug: open-dream-sports-cta-status-api
- collection_type: open
  name: Thunder Admin CT As API
  slug: open-dream-sports-ctas-api
- collection_type: open
  name: Delivr OTA Server Deployments API
  slug: open-dream-sports-deployments-api
- collection_type: open
  name: Guardian Device-Bound Authentication API
  slug: open-dream-sports-device-bound-authentication-api
- collection_type: open
  name: Thunder Admin Events API
  slug: open-dream-sports-events-api
- collection_type: open
  name: Raven Journey Events Catalog API
  slug: open-dream-sports-events-catalog-api
- collection_type: open
  name: Thunder Admin Filters API
  slug: open-dream-sports-filters-api
- collection_type: open
  name: Guardian Guest Authentication API
  slug: open-dream-sports-guest-authentication-api
- collection_type: open
  name: Dream Sports Health API
  slug: open-dream-sports-health-api
- collection_type: open
  name: Dream Sports Healthcheck API
  slug: open-dream-sports-healthcheck-api
- collection_type: open
  name: Raven Journey Journey Behaviour API
  slug: open-dream-sports-journey-behaviour-api
- collection_type: open
  name: Raven Journey Journey Lifecycle API
  slug: open-dream-sports-journey-lifecycle-api
- collection_type: open
  name: Raven Journey Journey Test API
  slug: open-dream-sports-journey-test-api
- collection_type: open
  name: Raven Journey Journeys API
  slug: open-dream-sports-journeys-api
- collection_type: open
  name: Guardian Key Management API
  slug: open-dream-sports-key-management-api
- collection_type: open
  name: Delivr OTA Server Metrics API
  slug: open-dream-sports-metrics-api
- collection_type: open
  name: Guardian OIDC API
  slug: open-dream-sports-oidc-api
- collection_type: open
  name: Guardian OIDC Client Management API
  slug: open-dream-sports-oidc-client-management-api
- collection_type: open
  name: Guardian OIDC Client Scope Management API
  slug: open-dream-sports-oidc-client-scope-management-api
- collection_type: open
  name: Guardian OIDC Discovery API
  slug: open-dream-sports-oidc-discovery-api
- collection_type: open
  name: Guardian OIDC Scope Management API
  slug: open-dream-sports-oidc-scope-management-api
- collection_type: open
  name: Dream Sports Openapi API
  slug: open-dream-sports-openapi-api
- collection_type: open
  name: Dream Sports Openapi.{type} Openapi.{type} API
  slug: open-dream-sports-openapi-type-api
- collection_type: open
  name: Checkmate Test Management Organizations API
  slug: open-dream-sports-organizations-api
- collection_type: open
  name: Guardian Password API
  slug: open-dream-sports-password-api
- collection_type: open
  name: Guardian Passwordless API
  slug: open-dream-sports-passwordless-api
- collection_type: open
  name: Checkmate Test Management Projects API
  slug: open-dream-sports-projects-api
- collection_type: open
  name: Guardian integration endpoints Provider API
  slug: open-dream-sports-provider-api
- collection_type: open
  name: Guardian Public Keys API
  slug: open-dream-sports-public-keys-api
- collection_type: open
  name: Delivr OTA Server Releases API
  slug: open-dream-sports-releases-api
- collection_type: open
  name: Checkmate Test Management Reports API
  slug: open-dream-sports-reports-api
- collection_type: open
  name: Checkmate Test Management Runs API
  slug: open-dream-sports-runs-api
- collection_type: open
  name: Thunder SDK API
  slug: open-dream-sports-sdk-api
- collection_type: open
  name: Guardian Session Management API
  slug: open-dream-sports-session-management-api
- collection_type: open
  name: Delivr OTA Server Sessions API
  slug: open-dream-sports-sessions-api
- collection_type: open
  name: Guardian Social API
  slug: open-dream-sports-social-api
- collection_type: open
  name: Dream Sports Tenants API
  slug: open-dream-sports-tenants-api
- collection_type: open
  name: Checkmate Test Management Tests API
  slug: open-dream-sports-tests-api
- collection_type: open
  name: Guardian Token Exchange API
  slug: open-dream-sports-token-exchange-api
- collection_type: open
  name: Guardian Token Management API
  slug: open-dream-sports-token-management-api
- collection_type: open
  name: Guardian integration endpoints User API
  slug: open-dream-sports-user-api
- collection_type: open
  name: Guardian User Flow Block API
  slug: open-dream-sports-user-flow-block-api
- collection_type: open
  name: Checkmate Test Management Users API
  slug: open-dream-sports-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/dream-sports-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/dream-sports-checkmate-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/dream-horizon-org/odin-mcp/issues
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
- description: 'First-party Model Context Protocol server that exposes Odin — Dream Sports'' internal developer platform — to agents. It is a thin adapter: business logic stays in the Java services, and the server cal'
  name: Dream Sports MCP Server
  slug: dream-sports-mcp-server
modified: '2026-08-04'
name: Dream Sports
nav: Providers
network: true
overview: 'Dream Sports publishes 61 APIs on the [APIs.io](https://apis.io/) network, including Access Keys API, Account API, and 59 more. Tagged areas include Company, Sports Technology, Fantasy Sports, Open-Source, and Developer Tools.


  The Dream Sports catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dream Sports'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, authentication, and 28 more developer resources.'
random_paper: 10
scopes:
- name: Dream Sports Scopes
  scope_count: 7
  slug: dream-sports-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 24
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 58.3
    developer_ergonomics: 73.2
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 59.0
      derived: 0
      marker_coverage: 0.0
      total: 61
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- Sports Technology
- Fantasy Sports
- Open-Source
- Developer Tools
- Platform Engineering
- Authentication
- OpenID Connect
- Mobile
- React Native
- DevOps
- Observability
- Test Management
- OTA Updates
- Feature Flags
- India
- MCP
- agent-native
website: https://www.dreamsports.group/
---
