---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 72.5
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 62
  human_in_the_loop: 0
  name: Egym Agentic Access
  operation_count: 117
  slug: egym-agentic-access
  summary_line: 117 operations · 62 acting
api_count: 10
apis:
- description: The current member-management-system integration API. RESTful contract for gym management software to sync member accounts and memberships into EGYM Cloud, manage profile pictures, RFID and NFC creden
  name: EGYM MMS API V2
  slug: mms-api-v2
- description: The legacy member-management-system API (Gym API v1). Publishes and reads member profiles, gym and user products, check-in / check-out events, trainer tasks and a liveness endpoint. EGYM documents thi
  name: EGYM MMS API v1
  slug: mms-api-v1
- description: Analytics and measurement export API for the authenticated gym location. Offers six synchronous CSV/JSON export endpoints — general analytics, Smart Strength workouts, Smart Strength assessments, flex
  name: EGYM Data Hub API
  slug: data-hub
- description: 'Per-account export API returning a member''s workouts and their strength, cardio and body measurements. Marked "Alpha preview" by EGYM. Notable discovery property: this API is listed in EGYM''s AI-agent'
  name: EGYM Data Export API
  slug: data-export
- description: 'Device-to-server API for equipment vendors integrating cardio, strength and measurement hardware directly with EGYM Cloud. Covers OAuth token exchange (RFID, NFC wallet, encrypted/obfuscated user id, '
  name: EGYM Equipment Vendor API (standalone clients)
  slug: equipment-vendor-standalone
- description: 'Backend-to-backend API for equipment vendors whose measurement devices report through the vendor''s own cloud rather than talking to EGYM directly. Covers OAuth token creation with RFID / NFC-wallet / '
  name: EGYM Equipment Vendor API (server-to-server)
  slug: equipment-vendor-server
- description: User-authorized API that lets third-party fitness and wearable apps write a member's own data into their EGYM ID account. Accepts workout submissions and cardio measurements — VO2 max, resting heart r
  name: EGYM User Connect API
  slug: user-connect
- description: 'An inverted contract: rather than an API EGYM operates, this is an "API blueprint" that EGYM publishes for member-management-system vendors to IMPLEMENT on their own hosts, so EGYM''s white-label membe'
  name: EGYM Canonical GroupX Classes API (blueprint)
  slug: canonical-groupx-classes
- description: Authorization-and-capture API for booking platforms. A Wellpass member generates a single-use booking code in the Wellpass app for a specific gym; the partner platform validates the code (dryRun true)
  name: EGYM Pay with Wellpass API
  slug: pay-with-wellpass
- description: Official hosted Model Context Protocol server published by EGYM at developer.egym.com/mcp and documented on the portal with copy-paste Codex configuration. Exposes six tools over the API catalog and d
  name: EGYM Documentation MCP Server
  slug: mcp-docs
artifact_total: 19
asyncapis:
- description: ''
  name: Egym Events Webhooks
  slug: egym-events-webhooks
- description: DERIVED, NOT PUBLISHED BY EGYM. EGYM documents its webhook surface in prose at https://developer.egym.com/general/webhooks and manages subscriptions through the MMS API V2 OpenAPI document, but publis
  name: EGYM MMS Webhook Events
  slug: egym-mms-events-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/egym-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://egym.com/int
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.egym.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.egym.com/general/general-info
- group: docs
  title: ''
  type: APIReference
  url: https://developer.egym.com/mms-api-v2/apis/mms-v2
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.egym.com/mms-api-v2/guide
- group: operate
  title: ''
  type: Support
  url: https://egym.com/int/contact
- group: company
  title: ''
  type: Blog
  url: https://egym.com/us/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/egym
- group: commercial
  title: ''
  type: Pricing
  url: https://egym.com/int/contact
- group: start
  title: ''
  type: SignUp
  url: https://developer.egym.com/general/general-info
- group: commercial
  title: ''
  type: TermsOfService
  url: https://us.egym.com/en-us/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://egym.com/int/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://egym.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.egym.com/mms-api-v2/change-log
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/egym-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/egym-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/egym-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/egym-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/egym-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/egym-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/egym-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/egym-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/egym-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/egym-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/egym-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/egym-events-webhooks.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/egym-mms-events-asyncapi.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/egym-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/egym-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/egym-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/egym-packages.yml
- group: design
  title: ''
  type: Components
  url: components/egym-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/egym-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/egym-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/egym-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/egym-sandbox.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/egym-decline-codes.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/egym-mms-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/egym-canonical-groupx-classes-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/egym-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/egym-tool-crosswalk.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/egym-mms-api-v2-openapi.yml
created: '2026-08-12'
description: 'EGYM is a Munich-headquartered fitness and health technology company that builds the connected-gym platform used by commercial fitness operators worldwide: Smart Strength and Smart Flex networked equipment, the EGYM Genius AI training engine, the EGYM Fitness Hub and Trainer apps, and the EGYM Wellpass / Corporate Fitness membership network that lets employers give staff access to thousands of partner venues. For developers, EGYM operates a public developer portal at developer.egym.com covering eight machine-readable APIs across three integration audiences — member-management-system (MMS) vendors syncing members, memberships, RFID/NFC credentials, check-ins, products and trainer tasks into EGYM Cloud; equipment vendors submitting body, cardio and flexibility measurements from devices or backends; and analytics consumers exporting workout and measurement data. EGYM also publishes an official documentation MCP server, an llms.txt, a written AI-agent instruction page, a dated
  change log, published rate limits and a documented webhook event catalog.'
image: https://developer.egym.com/assets/egym-logo.60dd444402b44525ca41f7a89573481ea8fffc6f40134e177d7b3a7f13d6e6b2.9c1bb791.svg
layout: provider
mcp_servers:
- description: ''
  name: egym-mcp.yml
  slug: egym-mcpyml
modified: '2026-08-12'
name: EGYM
nav: Providers
network: true
overview: 'EGYM publishes 8 APIs on the [APIs.io](https://apis.io/) network, including MMS API V2, MMS API v1, Data Hub API, and 5 more. Tagged areas include Company, Fitness, Health, Wellness, and Corporate Wellness.


  The EGYM catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  EGYM''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Egym Plans Pricing
  plan_count: 0
  slug: egym-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 1
  name: Egym Rate Limits
  slug: egym-rate-limits
scopes:
- name: Egym Scopes
  scope_count: 0
  slug: egym-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.8
  facets:
    commercial_clarity: 44.7
    contract_quality: 67.3
    developer_ergonomics: 80.4
    discoverability: 72.2
    governance: 20.8
    operational_transparency: 73.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: authentication
  name: Egym Authentication
  slug: egym-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Egym Domain Security
  slug: egym-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: egym
tags:
- Company
- Fitness
- Health
- Wellness
- Corporate Wellness
- Connected Equipment
- Gym Management
- Member Management
- Check-In
- Measurements
- Workouts
- Analytics
- Webhooks
- Germany
website: https://egym.com/int
---
