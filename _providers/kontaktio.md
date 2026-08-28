---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.8
  scored_at: '2026-08-26'
api_count: 4
apis:
- description: REST API for managing Kontakt.io devices in Kio Cloud — devices, configs, firmware, firmware upgrade schedules, commands, orders, managers, namespaces, proximity UUIDs, venues, device sharing and thir
  name: Kontakt.io Device Management API
  slug: kontaktio-device-management-api
- description: 'REST and streaming API for Kio Cloud location intelligence — campuses, buildings, floors, rooms, footfall spaces, location images, room/seat/footfall/sensor occupancy, telemetry, device positions and '
  name: Kontakt.io Location & Occupancy API
  slug: kontaktio-location-occupancy-api
- description: Smart Location Spaces API for Kio Cloud Apps, covering the spaces resource used to group rooms and seats for occupancy reporting.
  name: Kontakt.io Spaces API
  slug: kontaktio-spaces-api
- description: Integration API for batch importing and updating Entities such as Staff and Assets into the Kontakt.io Kio Apps platform, and retrieving their current configuration. Secured with OAuth2 client credent
  name: Kontakt.io Entity Management Integration API
  slug: kontaktio-entity-management-integration-api
artifact_total: 12
asyncapis:
- description: ''
  name: Kontaktio Streams Events
  slug: kontaktio-streams-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kontaktio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kontaktio-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://kontakt.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.kontakt.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kontakt.io/docs/dev-ctr-device-api/a09dcbf0d03de-device-management-api-introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.kontakt.io/docs/dev-ctr-device-api/40960a0b6f340-device-management-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.kontakt.io/docs/dev-ctr-device-api/e1e3f6ec0e943-authentication
- group: operate
  title: ''
  type: Support
  url: https://support.kontakt.io/hc/en-gb
- group: company
  title: ''
  type: Blog
  url: https://kontakt.io/resources/content-hub/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kontaktio
- group: start
  title: ''
  type: SignUp
  url: https://app.cloud.us.kontakt.io/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kontakt.io/legal-documents/terms-of-sale-and-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kontakt.io/legal-documents/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kontakt.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.kontakt.io/
- group: auth
  title: ''
  type: Compliance
  url: https://kontakt.io/legal-documents/security/
- group: build
  title: ''
  type: Packages
  url: packages/kontaktio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kontaktio-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kontaktio-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kontaktio-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/kontaktio-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kontaktio-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/kontaktio-device-management-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/kontaktio-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kontaktio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kontaktio-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kontaktio-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kontaktio-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kontaktio-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kontaktio-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kontaktio-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kontaktio-streams-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kontaktio-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kontaktio-plans-pricing.yml
created: '2026-08-23'
description: 'Kontakt.io is an AI-powered real-time location system (RTLS) and IoT platform for healthcare operations, founded in 2013 with offices in New York and Krakow. Its Kio Cloud platform combines BLE/UWB tags, badges, gateways and sensors with software for asset tracking, staff safety, patient flow, room and seat occupancy, and environmental telemetry. Developers integrate through the Kontakt.io Developer Center, which publishes four OpenAPI contracts: a Device Management API for provisioning, configuring and firmware-upgrading devices, a Location & Occupancy API for real-time and historical positions, presences, occupancy and telemetry plus a Streams API for event subscriptions, a Spaces API, and an Entity Management Integration API for batch import of staff and asset entities. Kio Cloud runs in US and UK regions and ships iOS and Android SDKs.'
image: https://kontakt.io/app/uploads/2025/06/why-kontakt-hero-image-scaled-1.jpg
layout: provider
mcp_servers:
- description: ''
  name: Kontakt.io MCP Server
  slug: kontaktio-mcp-server
modified: '2026-08-23'
name: Kontakt.io
nav: Providers
network: true
overview: 'Kontakt.io publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Device Management API, Location & Occupancy API, Spaces API, and 1 more. Tagged areas include Company, IoT, RTLS, Healthcare, and Asset Tracking.


  The Kontakt.io catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kontakt.io''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 28 more developer resources.'
plans:
- name: Kontaktio Plans Pricing
  plan_count: 0
  slug: kontaktio-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Kontaktio Rate Limits
  slug: kontaktio-rate-limits
scopes:
- name: Kontaktio Scopes
  scope_count: 4
  slug: kontaktio-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: strong
  composite: 65.7
  delta: -3.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 16.7
    contract_quality: 65.9
    developer_ergonomics: 73.2
    discoverability: 85.2
    governance: 16.7
    operational_transparency: 73.7
  previous_composite: 68.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Kontaktio Authentication
  slug: kontaktio-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Kontaktio Domain Security
  slug: kontaktio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kontaktio Trust Center
  slug: kontaktio-trust-center
  summary_line: SOC 2 Type II, HIPAA Security Rule / HITECH, GDPR, ISO 27001
slug: kontaktio
tags:
- Company
- IoT
- RTLS
- Healthcare
- Asset Tracking
- Location
- Occupancy
- Bluetooth
- Device Management
- Telemetry
- Sensors
- Streaming
website: https://kontakt.io/
---
