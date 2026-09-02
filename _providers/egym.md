---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 62
  human_in_the_loop: 0
  name: Egym Agentic Access
  operation_count: 117
  slug: egym-agentic-access
  summary_line: 117 operations · 62 acting
api_count: 16
apis:
- description: Authorization-and-capture API for booking platforms. A Wellpass member generates a single-use booking code in the Wellpass app for a specific gym; the partner platform validates the code (dryRun true)
  name: EGYM Pay with Wellpass API
  slug: pay-with-wellpass
- description: Official hosted Model Context Protocol server published by EGYM at developer.egym.com/mcp and documented on the portal with copy-paste Codex configuration. Exposes six tools over the API catalog and d
  name: EGYM Documentation MCP Server
  slug: mcp-docs
- description: API for submitting cardio measurements
  name: EGYM 1. Cardio Measurements API
  slug: egym-1-cardio-measurements-api
- description: API for submitting workouts
  name: EGYM 2. Workouts API
  slug: egym-2-workouts-api
- description: The alive API from EGYM — 1 operation(s) for alive.
  name: EGYM Alive API
  slug: egym-alive-api
- description: Background export jobs that produce downloadable JSON, JSONL, or CSV files.
  name: EGYM Asynchronous exports API
  slug: egym-asynchronous-exports-api
- description: The Body Measurement API from EGYM — 2 operation(s) for body measurement.
  name: EGYM Body Measurement API
  slug: egym-body-measurement-api
- description: The Cardio Measurement API from EGYM — 2 operation(s) for cardio measurement.
  name: EGYM Cardio Measurement API
  slug: egym-cardio-measurement-api
- description: The Cardio Test API from EGYM — 3 operation(s) for cardio test.
  name: EGYM Cardio Test API
  slug: egym-cardio-test-api
- description: The Cardio Workouts API from EGYM — 2 operation(s) for cardio workouts.
  name: EGYM Cardio Workouts API
  slug: egym-cardio-workouts-api
- description: The Flexibility Measurement API from EGYM — 2 operation(s) for flexibility measurement.
  name: EGYM Flexibility Measurement API
  slug: egym-flexibility-measurement-api
- description: The gym API from EGYM — 2 operation(s) for gym.
  name: EGYM Gym API
  slug: egym-gym-api
- description: These operations are needed to transmit the information to EGYM, that a specific member is currently in the gym. Based on that information several business logics are built, to provide a seamless trai
  name: EGYM Gym Visit API
  slug: egym-gym-visit-api
- description: The Image API from EGYM — 1 operation(s) for image.
  name: EGYM Image API
  slug: egym-image-api
- description: Operations related to L2 level of integration
  name: EGYM L2 API
  slug: egym-l2-api
- description: Operations related to L3 level of integration
  name: EGYM L3 API
  slug: egym-l3-api
- description: The Machine API from EGYM — 1 operation(s) for machine.
  name: EGYM Machine API
  slug: egym-machine-api
- description: These operations are needed to retrieve measurements with corresponding metrics. Additional permissions are required to access these endpoints.
  name: EGYM Measurements API
  slug: egym-measurements-api
- description: These operations are needed to create and update member accounts and their membership information.
  name: EGYM Member Account API
  slug: egym-member-account-api
- description: Note that NFC API endpoints are in beta as we've been tuning setup processes on both EGYM and partner sides.
  name: EGYM Member Account NFC API
  slug: egym-member-account-nfc-api
- description: These operation are needed to assign and retrieve member account roles
  name: EGYM Member Account Roles API
  slug: egym-member-account-roles-api
- description: Operations with RFIDs
  name: EGYM Member RFIDs API
  slug: egym-member-rfids-api
- description: These operations are needed to migrate members from V1 API to V2 API.
  name: EGYM Migrating members API
  slug: egym-migrating-members-api
- description: The OAuth API from EGYM — 2 operation(s) for oauth.
  name: EGYM O Auth API
  slug: egym-oauth-api
- description: The Open Exercise Workouts API from EGYM — 1 operation(s) for open exercise workouts.
  name: EGYM Open Exercise Workouts API
  slug: egym-open-exercise-workouts-api
- description: The Partners API from EGYM — 1 operation(s) for partners.
  name: EGYM Partners API
  slug: egym-partners-api
- description: Operations on EGYM products. Currently available products are EGYM Smart Strength (Machine Admission) and EGYM+
  name: EGYM Products booking API
  slug: egym-products-booking-api
- description: Send push notifications to EGYM mobile apps
  name: EGYM Push notifications API
  slug: egym-push-notifications-api
- description: The Resource API from EGYM — 2 operation(s) for resource.
  name: EGYM Resource API
  slug: egym-resource-api
- description: The Statistics API from EGYM — 2 operation(s) for statistics.
  name: EGYM Statistics API
  slug: egym-statistics-api
- description: The Strength Workouts API from EGYM — 2 operation(s) for strength workouts.
  name: EGYM Strength Workouts API
  slug: egym-strength-workouts-api
- description: Immediate paginated JSON exports for weekly analytics and recent event data.
  name: EGYM Synchronous exports API
  slug: egym-synchronous-exports-api
- description: The task API from EGYM — 2 operation(s) for task.
  name: EGYM Task API
  slug: egym-task-api
- description: These operations are needed to create and update trainer tasks.
  name: EGYM Trainer Task API
  slug: egym-trainer-task-api
- description: The User API from EGYM — 9 operation(s) for user.
  name: EGYM User API
  slug: egym-user-api
- description: The User Details API from EGYM — 1 operation(s) for user details.
  name: EGYM User Details API
  slug: egym-user-details-api
- description: Operations with webhooks
  name: EGYM Webhooks API
  slug: egym-webhooks-api
- description: These operations are needed to retrieve workouts. Additional permissions are required to access these endpoints.
  name: EGYM Workouts API
  slug: egym-workouts-api
artifact_total: 55
asyncapis:
- description: ''
  name: Egym Events Webhooks
  slug: egym-events-webhooks
- description: DERIVED, NOT PUBLISHED BY EGYM. EGYM documents its webhook surface in prose at https://developer.egym.com/general/webhooks and manages subscriptions through the MMS API V2 OpenAPI document, but publis
  name: EGYM MMS Webhook Events
  slug: egym-mms-events-asyncapi
collections:
- collection_type: open
  name: Canonical GroupX Classes API
  slug: open-egym-canonical-groupx-classes
- collection_type: open
  name: DATA EXPORT API
  slug: open-egym-data-export
- collection_type: open
  name: Data Hub API
  slug: open-egym-data-hub
- collection_type: open
  name: Equipment Vendor API (for server-to-server cases)
  slug: open-egym-equipment-vendor-server
- collection_type: open
  name: Equipment Vendor API (for standalone clients)
  slug: open-egym-equipment-vendor-standalone
- collection_type: open
  name: MMS API v1
  slug: open-egym-mms-api-v1
- collection_type: open
  name: MMS API V2
  slug: open-egym-mms-api-v2
- collection_type: open
  name: OpenAPI definition
  slug: open-egym-user-connect
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/egym-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/egym-mms-api-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/egym-data-hub-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/egym-data-export-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/egym-equipment-vendor-standalone-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/egym-equipment-vendor-server-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/egym-user-connect-overlay.yaml
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
  name: EGYM MCP Server
  slug: egym-mcp-server
modified: '2026-08-12'
name: EGYM
nav: Providers
network: true
overview: 'EGYM publishes 36 APIs on the [APIs.io](https://apis.io/) network, including 1. Cardio Measurements API, 2. Workouts API, Alive API, and 33 more. Tagged areas include Company, Fitness, Health, Wellness, and Corporate Wellness.


  The EGYM catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  EGYM''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 44 more developer resources.'
plans:
- name: Egym Plans Pricing
  plan_count: 0
  slug: egym-plans-pricing
random_paper: 14
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
  composite: 62.6
  coverage:
    artifact_dirs: 26
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 66.4
    developer_ergonomics: 73.2
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 71.1
  previous_composite: 62.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 94.4
      derived: 0
      marker_coverage: 0.0
      total: 36
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/egym/refs/heads/main/screenshots/egym-2026-08-17T080915.png
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
- Check-in
- Measurements
- Workouts
- Analytics
- Webhook
- Germany
website: https://egym.com/int
---
