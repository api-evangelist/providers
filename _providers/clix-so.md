---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Agent2Agent (A2A) protocol surface: a public agent card at https://api.clix.so/.well-known/agent-card.json (0.3.0 shape by default, 1.0 shape under the A2A-Version: 1.0 header; graded conformant) and '
  name: Clix A2A Agent
  slug: clix-a2a-agent
- description: 'Model Context Protocol surfaces, both documentation-only: the provider''s stdio server @clix-so/clix-mcp-server 0.1.4 (npx -y @clix-so/clix-mcp-server@latest; tools search_docs and search_sdk over the '
  name: Clix MCP Server
  slug: clix-mcp-server
- baseURL: https://api.clix.so
  baseurl_source: declared
  description: The ClixExternalService API from Clix — 10 operation(s) for clixexternalservice.
  name: Clix Clix External Service API
  phrasing_intents:
  - id: ClixExternalService_CreateOrUpdateDevices
    intent: Register or update app devices
    question: Can I register new app installs as devices in Clix so they can receive messages?
  - id: ClixExternalService_SetProjectUserIdForDevice
    intent: Link a device to a project user ID
    question: How do I associate a device with my own user ID after someone logs in?
  - id: ClixExternalService_CreateOrUpdateUsersPropertiesByDeviceId
    intent: Set user properties via a device ID
    question: Can I update a user's properties when I only know their device ID?
  - id: ClixExternalService_CreateEvents
    intent: Track user events
    question: How do I send in-app events like purchases or sign-ups to Clix?
  - id: ClixExternalService_HealthCheck
    intent: Check that the service is up
    question: Is the external service API currently healthy and reachable?
  - id: ClixExternalService_SendPushNotifications
    intent: Send push notifications to devices
    question: How do I send a push notification to a user's phone?
  - id: ClixExternalService_CreateUser
    intent: Create a user
    question: How do I create a new user record keyed by my own user ID?
  - id: ClixExternalService_UpdateUser
    intent: Update an existing user's properties
    question: How do I change properties on a user I already created, using their project user ID?
  phrasing_ops: 11
  slug: clix-so-clixexternalservice-api
artifact_total: 19
asyncapis:
- description: ''
  name: Clix So Webhooks
  slug: clix-so-webhooks
common:
- group: other
  href: https://artifacts.apis.io/clix-so/capabilities/clix-so-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/clix-so-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/clix-so/overlays/clix-so-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clix-so-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://clix.so/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.clix.so/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clix.so/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.clix.so/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.clix.so/sdk-quickstart-ios
- group: start
  title: ''
  type: Login
  url: https://console.clix.so/
- group: commercial
  title: ''
  type: Pricing
  url: https://clix.so/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clix.so/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clix.so/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://clix.so/status
- group: operate
  title: ''
  type: SLA
  url: https://clix.so/availability
- group: company
  title: ''
  type: Blog
  url: https://blog.clix.so/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.clix.so/rss/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clix-so
- group: operate
  title: ''
  type: Support
  url: https://docs.clix.so/troubleshooting/not-getting-push-notification
- group: agent
  href: https://artifacts.apis.io/clix-so/llms/clix-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clix-so-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.clix.so/llms.txt
- group: other
  href: https://artifacts.apis.io/clix-so/a2a/clix-so-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/clix-so-a2a.yml
- group: agent
  href: https://artifacts.apis.io/clix-so/mcp/clix-so-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clix-so-mcp.yml
- group: build
  href: https://artifacts.apis.io/clix-so/mcp/clix-so-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/clix-so-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/clix-so/well-known/clix-so-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clix-so-well-known.yml
- group: build
  href: https://artifacts.apis.io/clix-so/packages/clix-so-packages.yml
  title: ''
  type: Packages
  url: packages/clix-so-packages.yml
- group: build
  href: https://artifacts.apis.io/clix-so/packages/clix-so-packages.yml
  title: ''
  type: SDKs
  url: packages/clix-so-packages.yml
- group: build
  href: https://artifacts.apis.io/clix-so/cli/clix-so-cli.yml
  title: ''
  type: CLI
  url: cli/clix-so-cli.yml
- group: auth
  href: https://artifacts.apis.io/clix-so/authentication/clix-so-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clix-so-authentication.yml
- group: design
  href: https://artifacts.apis.io/clix-so/conventions/clix-so-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clix-so-conventions.yml
- group: design
  href: https://artifacts.apis.io/clix-so/conventions/clix-so-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/clix-so-conventions.yml
- group: design
  href: https://artifacts.apis.io/clix-so/errors/clix-so-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clix-so-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clix-so/lifecycle/clix-so-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/clix-so-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/clix-so/changelog/clix-so-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/clix-so-changelog.yml
- group: design
  href: https://artifacts.apis.io/clix-so/conformance/clix-so-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clix-so-conformance.yml
- group: operate
  href: https://artifacts.apis.io/clix-so/rate-limits/clix-so-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/clix-so-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/clix-so/plans/clix-so-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clix-so-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/clix-so/asyncapi/clix-so-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/clix-so-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/clix-so/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/clix-so/data-model/clix-so-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clix-so-data-model.yml
- group: auth
  href: https://artifacts.apis.io/clix-so/security/clix-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clix-so-domain-security.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://clix.so/privacy
- group: other
  title: ''
  type: DataResidency
  url: https://clix.so/availability
- group: operate
  title: ''
  type: IncidentNotification
  url: https://docs.clix.so/ops/incident-communication
created: '2026-09-19'
description: 'Clix is a US-based, developer-first mobile push notification platform for iOS, Android, React Native and Flutter — one CLI command (clix install) automates Firebase Cloud Messaging and APNs setup, and the console adds behaviour-triggered and API-triggered campaigns, real-time delivery logs, full-funnel analytics and device/user lifecycle management, priced free to 100K active devices then $30/month. For developers and agents it publishes a small REST API at https://api.clix.so (OpenAPI 3.1.0 generated from clix/external/v1/clix.proto: 11 operations across users, devices, events, messages:send, live-activities:start and campaigns/{id}:trigger, authenticated with X-Clix-Project-ID + X-Clix-API-Key), an A2A agent at https://api.clix.so/a2a whose card at /.well-known/agent-card.json is served in both 0.3.0 and 1.0 shapes and exposes four skills (create-user, track-event, send-push-notification, trigger-campaign) with idempotency keys, SSE streaming, task cancellation and task webhooks,
  a stdio MCP server (@clix-so/clix-mcp-server) plus a Mintlify docs MCP endpoint — both documentation-only — an open agent-skills repo, first-party SDKs on Maven Central, CocoaPods/SwiftPM, pub.dev and npm, a self-hosted status page with a published 99.5% monthly SLO, and console-configured PUSH_SENT/PUSH_FAILED webhooks.'
finops:
- has_sources: true
  method: derived
  name: Clix So Finops
  primary_unit: active devices
  service_category: ''
  slug: clix-so-finops
  template: false
image: https://clix.so/opengraph-image?04675f86137dbf70
layout: provider
mcp_servers:
- description: Clix has two MCP surfaces and neither one executes Clix operations — both retrieve documentation. (1) The provider-built "Clix MCP Server" is a stdio npm package, @clix-so/clix-mcp-server 0.1.4, run w
  name: Clix MCP Server
  slug: clix-so-mcp-yml
modified: '2026-09-19'
name: Clix
nav: Providers
network: true
overview: 'Clix publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Clix External Service API, and 2 more. Tagged areas include Push Notifications, Mobile, Messaging, Campaigns, and Event Tracking.


  The Clix catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Clix''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, CLI, and 35 more developer resources.'
plans:
- name: Clix So Plans Pricing
  plan_count: 3
  slug: clix-so-plans-pricing
- name: Clix So Price Estimates
  plan_count: 0
  slug: clix-so-price-estimates
random_paper: 7
rate_limits:
- limit_count: 1
  name: Clix So Rate Limits
  slug: clix-so-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Clix API Rules
  rule_count: 45
  severity_counts:
    error: 39
    hint: 0
    info: 2
    warn: 4
  slug: clix-so-rules
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.5
  facets:
    access_clarity: 61.8
    contract_governance: 31.8
    contract_quality: 55.9
    developer_ergonomics: 56.0
    discoverability: 75.0
    operational_transparency: 51.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 71.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/clix-so/clix-so-2026-10-11T103047.png
security:
- kind: authentication
  name: Clix So Authentication
  slug: clix-so-authentication
  summary_line: apiKey · 5 schemes
- kind: domain-security
  name: Clix So Domain Security
  slug: clix-so-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 7
skills:
- name: clix-api-triggered-campaigns
  slug: clix-so-api-triggered-campaigns
- name: Clix
  slug: clix-so-docs-skill
- name: clix-event-tracking
  slug: clix-so-event-tracking
- name: clix-integration
  slug: clix-so-integration
- name: clix-personalization
  slug: clix-so-personalization
- name: clix-so-send-push-notification
  slug: clix-so-send-push-notification
- name: clix-user-management
  slug: clix-so-user-management
slug: clix-so
tags:
- Push Notifications
- Mobile
- Messaging
- Campaigns
- Event Tracking
- Customer Engagement
- A2A
- MCP
- Agents
- SDK
- United States
- Company
website: https://clix.so/
---
