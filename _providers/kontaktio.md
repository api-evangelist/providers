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
  scored_at: '2026-08-30'
api_count: 8
apis:
- description: The Buildings API from Kontakt.io — 2 operation(s) for buildings.
  name: Kontakt.io Buildings API
  slug: kontaktio-buildings-api
- description: The Campuses API from Kontakt.io — 2 operation(s) for campuses.
  name: Kontakt.io Campuses API
  slug: kontaktio-campuses-api
- description: The Colocations API from Kontakt.io — 1 operation(s) for colocations.
  name: Kontakt.io Colocations API
  slug: kontaktio-colocations-api
- description: Commands are a special type of Configs used for initiating some management tasks, e.g. entering bootloader mode
  name: Kontakt.io Command API
  slug: kontaktio-command-api
- description: 'Pending configs represent new values for beacon settings that should be applied to actual devices via e.g. Kontakt.io Administration Apps. Creating a new config does not automatically change anything '
  name: Kontakt.io Config API
  slug: kontaktio-config-api
- description: 'NOTE: this set of endpoints has been superseded by External Devices functionality. These endpoints provide a way to integrate 3rd party Bluetooth-enabled scanning devices into Kontakt.io platform. As '
  name: Kontakt.io Device (3rd party) API
  slug: kontaktio-device-3rd-party-api
- description: The Device resource represents Kontakt.io devices assigned to a particular Kontakt.io Panel account, as well as devices shared with that account from different accounts.
  name: Kontakt.io Device API
  slug: kontaktio-device-api
- description: These endpoints are designed to assist with storing metadata associated with Portal Beams
  name: Kontakt.io Device (Portal Beam) API
  slug: kontaktio-device-portal-beam-api
- description: The device tags
  name: Kontakt.io Device tags API
  slug: kontaktio-device-tags-api
- description: Helper resources for working with Eddystone beacons
  name: Kontakt.io Eddystone API
  slug: kontaktio-eddystone-api
- description: The entity-integration API from Kontakt.io — 2 operation(s) for entity-integration.
  name: Kontakt.io Entity Integration API
  slug: kontaktio-entity-integration-api
- description: External Device feature is a method of adding arbitrary external devices to the system. Such devices have MAC, unique id, and other virtual attributes, but they cannot be managed (configured).
  name: Kontakt.io External Device API
  slug: kontaktio-external-device-api
- description: Firmware resources
  name: Kontakt.io Firmware API
  slug: kontaktio-firmware-api
- description: The Floors API from Kontakt.io — 1 operation(s) for floors.
  name: Kontakt.io Floors API
  slug: kontaktio-floors-api
- description: The Footfall Spaces API from Kontakt.io — 1 operation(s) for footfall spaces.
  name: Kontakt.io Footfall Spaces API
  slug: kontaktio-footfall-spaces-api
- description: The Gateways API from Kontakt.io — 1 operation(s) for gateways.
  name: Kontakt.io Gateways API
  slug: kontaktio-gateways-api
- description: The Location Images API from Kontakt.io — 1 operation(s) for location images.
  name: Kontakt.io Location Images API
  slug: kontaktio-location-images-api
- description: Managers represent user accounts that can manage Kontakt.io Devices. Everyone can freely create an account on [Kontakt.io Web Panel](https://panel.kontakt.io) and then use it to work with this API.
  name: Kontakt.io Manager API
  slug: kontaktio-manager-api
- description: The Occupancy API from Kontakt.io — 1 operation(s) for occupancy.
  name: Kontakt.io Occupancy API
  slug: kontaktio-occupancy-api
- description: 'The Occupancy: Footfall API from Kontakt.io — 2 operation(s) for occupancy: footfall.'
  name: 'Kontakt.io Occupancy: Footfall API'
  slug: kontaktio-occupancy-footfall-api
- description: 'The Occupancy: Room API from Kontakt.io — 2 operation(s) for occupancy: room.'
  name: 'Kontakt.io Occupancy: Room API'
  slug: kontaktio-occupancy-room-api
- description: 'The Occupancy: Seats API from Kontakt.io — 2 operation(s) for occupancy: seats.'
  name: 'Kontakt.io Occupancy: Seats API'
  slug: kontaktio-occupancy-seats-api
- description: An Order represents all devices that have been purchased in Kontakt.io Web Store in a single transaction. Before these devices can be used with Kontakt.io platform, they need to be added to Kontakt.io
  name: Kontakt.io Order API
  slug: kontaktio-order-api
- description: The Positions API from Kontakt.io — 2 operation(s) for positions.
  name: Kontakt.io Positions API
  slug: kontaktio-positions-api
- description: The Presences API from Kontakt.io — 2 operation(s) for presences.
  name: Kontakt.io Presences API
  slug: kontaktio-presences-api
- description: List of iBeacon Proximity UUIDs used on beacons belonging to a Manager
  name: Kontakt.io Proximities API
  slug: kontaktio-proximities-api
- description: The Rooms API from Kontakt.io — 2 operation(s) for rooms.
  name: Kontakt.io Rooms API
  slug: kontaktio-rooms-api
- description: The Spaces API from Kontakt.io — 2 operation(s) for spaces.
  name: Kontakt.io Spaces API
  slug: kontaktio-spaces-api
- description: The Stream API from Kontakt.io — 9 operation(s) for stream.
  name: Kontakt.io Stream API
  slug: kontaktio-stream-api
- description: The Telemetry API from Kontakt.io — 1 operation(s) for telemetry.
  name: Kontakt.io Telemetry API
  slug: kontaktio-telemetry-api
artifact_total: 38
asyncapis:
- description: ''
  name: Kontaktio Streams Events
  slug: kontaktio-streams-events
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/kontaktio-capability-edges.yml
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
overview: 'Kontakt.io publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Buildings API, Campuses API, Colocations API, and 27 more. Tagged areas include Company, IoT, RTLS, Healthcare, and Asset Tracking.


  The Kontakt.io catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kontakt.io''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 29 more developer resources.'
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
  composite: 62.6
  coverage:
    artifact_dirs: 22
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 65.8
    developer_ergonomics: 73.2
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 73.7
  previous_composite: 62.6
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
