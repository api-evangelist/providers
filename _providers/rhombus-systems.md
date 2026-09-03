---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 62.1
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: wss://ws.rhombussystems.com:8443/websocket
  baseurl_source: declared
  description: Real-time organization change events delivered over a STOMP 1.2 session framed on a secure WebSocket. Clients subscribe to /topic/change/{orgUuid} and receive a MESSAGE frame for every entity change i
  name: Rhombus Console WebSocket API
  slug: rhombus-systems-console-websocket-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Access Control Integrations Webservice API from Rhombus Systems — 101 operation(s) for access control integrations webservice.
  name: Rhombus Systems Access Control Integrations Webservice API
  slug: rhombus-systems-access-control-integrations-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Access Control Webservice API from Rhombus Systems — 65 operation(s) for access control webservice.
  name: Rhombus Systems Access Control Webservice API
  slug: rhombus-systems-access-control-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Alarm Monitoring Keypad Webservice API from Rhombus Systems — 5 operation(s) for alarm monitoring keypad webservice.
  name: Rhombus Systems Alarm Monitoring Keypad Webservice API
  slug: rhombus-systems-alarm-monitoring-keypad-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Alert Monitoring Webservice API from Rhombus Systems — 11 operation(s) for alert monitoring webservice.
  name: Rhombus Systems Alert Monitoring Webservice API
  slug: rhombus-systems-alert-monitoring-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The AudioGateway Webservice API from Rhombus Systems — 10 operation(s) for audiogateway webservice.
  name: Rhombus Systems AudioGateway Webservice API
  slug: rhombus-systems-audiogateway-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The AudioPlayback Webservice API from Rhombus Systems — 6 operation(s) for audioplayback webservice.
  name: Rhombus Systems AudioPlayback Webservice API
  slug: rhombus-systems-audioplayback-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Badge Reader Webservice API from Rhombus Systems — 2 operation(s) for badge reader webservice.
  name: Rhombus Systems Badge Reader Webservice API
  slug: rhombus-systems-badge-reader-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The BLE Webservice API from Rhombus Systems — 1 operation(s) for ble webservice.
  name: Rhombus Systems BLE Webservice API
  slug: rhombus-systems-ble-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Button Webservice API from Rhombus Systems — 8 operation(s) for button webservice.
  name: Rhombus Systems Button Webservice API
  slug: rhombus-systems-button-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Camera Webservice API from Rhombus Systems — 61 operation(s) for camera webservice.
  name: Rhombus Systems Camera Webservice API
  slug: rhombus-systems-camera-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The ClaimKey Webservice API from Rhombus Systems — 3 operation(s) for claimkey webservice.
  name: Rhombus Systems ClaimKey Webservice API
  slug: rhombus-systems-claimkey-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Climate Webservice API from Rhombus Systems — 12 operation(s) for climate webservice.
  name: Rhombus Systems Climate Webservice API
  slug: rhombus-systems-climate-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Component Webservice API from Rhombus Systems — 62 operation(s) for component webservice.
  name: Rhombus Systems Component Webservice API
  slug: rhombus-systems-component-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Customer Webservice API from Rhombus Systems — 6 operation(s) for customer webservice.
  name: Rhombus Systems Customer Webservice API
  slug: rhombus-systems-customer-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Developer Webservice API from Rhombus Systems — 4 operation(s) for developer webservice.
  name: Rhombus Systems Developer Webservice API
  slug: rhombus-systems-developer-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Device Config Webservice API from Rhombus Systems — 2 operation(s) for device config webservice.
  name: Rhombus Systems Device Config Webservice API
  slug: rhombus-systems-device-config-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Door Controller Webservice API from Rhombus Systems — 2 operation(s) for door controller webservice.
  name: Rhombus Systems Door Controller Webservice API
  slug: rhombus-systems-door-controller-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Door Webservice API from Rhombus Systems — 4 operation(s) for door webservice.
  name: Rhombus Systems Door Webservice API
  slug: rhombus-systems-door-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Doorbell Camera Webservice API from Rhombus Systems — 10 operation(s) for doorbell camera webservice.
  name: Rhombus Systems Doorbell Camera Webservice API
  slug: rhombus-systems-doorbell-camera-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Elevator Webservice API from Rhombus Systems — 6 operation(s) for elevator webservice.
  name: Rhombus Systems Elevator Webservice API
  slug: rhombus-systems-elevator-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Event Search Webservice API from Rhombus Systems — 2 operation(s) for event search webservice.
  name: Rhombus Systems Event Search Webservice API
  slug: rhombus-systems-event-search-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Event Webservice API from Rhombus Systems — 42 operation(s) for event webservice.
  name: Rhombus Systems Event Webservice API
  slug: rhombus-systems-event-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Export Webservice API from Rhombus Systems — 16 operation(s) for export webservice.
  name: Rhombus Systems Export Webservice API
  slug: rhombus-systems-export-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Face Recognition Event Webservice API from Rhombus Systems — 4 operation(s) for face recognition event webservice.
  name: Rhombus Systems Face Recognition Event Webservice API
  slug: rhombus-systems-face-recognition-event-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Face Recognition Matchmaker Webservice API from Rhombus Systems — 9 operation(s) for face recognition matchmaker webservice.
  name: Rhombus Systems Face Recognition Matchmaker Webservice API
  slug: rhombus-systems-face-recognition-matchmaker-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Face Recognition Person Webservice API from Rhombus Systems — 8 operation(s) for face recognition person webservice.
  name: Rhombus Systems Face Recognition Person Webservice API
  slug: rhombus-systems-face-recognition-person-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Feature Webservice API from Rhombus Systems — 5 operation(s) for feature webservice.
  name: Rhombus Systems Feature Webservice API
  slug: rhombus-systems-feature-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Guest Management Kiosk Webservice API from Rhombus Systems — 1 operation(s) for guest management kiosk webservice.
  name: Rhombus Systems Guest Management Kiosk Webservice API
  slug: rhombus-systems-guest-management-kiosk-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Help Webservice API from Rhombus Systems — 7 operation(s) for help webservice.
  name: Rhombus Systems Help Webservice API
  slug: rhombus-systems-help-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Incident Management Integrations Webservice API from Rhombus Systems — 34 operation(s) for incident management integrations webservice.
  name: Rhombus Systems Incident Management Integrations Webservice API
  slug: rhombus-systems-incident-management-integrations-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Integrations Webservice API from Rhombus Systems — 32 operation(s) for integrations webservice.
  name: Rhombus Systems Integrations Webservice API
  slug: rhombus-systems-integrations-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Internal Webservice API from Rhombus Systems — 1 operation(s) for internal webservice.
  name: Rhombus Systems Internal Webservice API
  slug: rhombus-systems-internal-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The IoT Integrations Webservice API from Rhombus Systems — 12 operation(s) for iot integrations webservice.
  name: Rhombus Systems IoT Integrations Webservice API
  slug: rhombus-systems-iot-integrations-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The License Webservice API from Rhombus Systems — 16 operation(s) for license webservice.
  name: Rhombus Systems License Webservice API
  slug: rhombus-systems-license-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Location Webservice API from Rhombus Systems — 13 operation(s) for location webservice.
  name: Rhombus Systems Location Webservice API
  slug: rhombus-systems-location-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Lockdown Plan Webservice API from Rhombus Systems — 17 operation(s) for lockdown plan webservice.
  name: Rhombus Systems Lockdown Plan Webservice API
  slug: rhombus-systems-lockdown-plan-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Logistics Webservice API from Rhombus Systems — 4 operation(s) for logistics webservice.
  name: Rhombus Systems Logistics Webservice API
  slug: rhombus-systems-logistics-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Media Device Webservice API from Rhombus Systems — 1 operation(s) for media device webservice.
  name: Rhombus Systems Media Device Webservice API
  slug: rhombus-systems-media-device-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The OAuth Webservice API from Rhombus Systems — 6 operation(s) for oauth webservice.
  name: Rhombus Systems OAuth Webservice API
  slug: rhombus-systems-oauth-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Occupancy Webservice API from Rhombus Systems — 4 operation(s) for occupancy webservice.
  name: Rhombus Systems Occupancy Webservice API
  slug: rhombus-systems-occupancy-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Org Integrations Webservice API from Rhombus Systems — 4 operation(s) for org integrations webservice.
  name: Rhombus Systems Org Integrations Webservice API
  slug: rhombus-systems-org-integrations-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Org Webservice API from Rhombus Systems — 47 operation(s) for org webservice.
  name: Rhombus Systems Org Webservice API
  slug: rhombus-systems-org-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Partner Webservice API from Rhombus Systems — 22 operation(s) for partner webservice.
  name: Rhombus Systems Partner Webservice API
  slug: rhombus-systems-partner-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Permission Webservice API from Rhombus Systems — 10 operation(s) for permission webservice.
  name: Rhombus Systems Permission Webservice API
  slug: rhombus-systems-permission-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Policy Webservice API from Rhombus Systems — 54 operation(s) for policy webservice.
  name: Rhombus Systems Policy Webservice API
  slug: rhombus-systems-policy-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Proximity Webservice API from Rhombus Systems — 4 operation(s) for proximity webservice.
  name: Rhombus Systems Proximity Webservice API
  slug: rhombus-systems-proximity-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The RapidSOS Webservice API from Rhombus Systems — 1 operation(s) for rapidsos webservice.
  name: Rhombus Systems RapidSOS Webservice API
  slug: rhombus-systems-rapidsos-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Relay Webservice API from Rhombus Systems — 27 operation(s) for relay webservice.
  name: Rhombus Systems Relay Webservice API
  slug: rhombus-systems-relay-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Report Webservice API from Rhombus Systems — 30 operation(s) for report webservice.
  name: Rhombus Systems Report Webservice API
  slug: rhombus-systems-report-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Rules Records Webservice API from Rhombus Systems — 3 operation(s) for rules records webservice.
  name: Rhombus Systems Rules Records Webservice API
  slug: rhombus-systems-rules-records-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Rules Webservice API from Rhombus Systems — 10 operation(s) for rules webservice.
  name: Rhombus Systems Rules Webservice API
  slug: rhombus-systems-rules-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Scene Query Webservice API from Rhombus Systems — 9 operation(s) for scene query webservice.
  name: Rhombus Systems Scene Query Webservice API
  slug: rhombus-systems-scene-query-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Schedule Webservice API from Rhombus Systems — 12 operation(s) for schedule webservice.
  name: Rhombus Systems Schedule Webservice API
  slug: rhombus-systems-schedule-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Search Webservice API from Rhombus Systems — 4 operation(s) for search webservice.
  name: Rhombus Systems Search Webservice API
  slug: rhombus-systems-search-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Sensor Webservice API from Rhombus Systems — 3 operation(s) for sensor webservice.
  name: Rhombus Systems Sensor Webservice API
  slug: rhombus-systems-sensor-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Service Management Integrations Webservice API from Rhombus Systems — 14 operation(s) for service management integrations webservice.
  name: Rhombus Systems Service Management Integrations Webservice API
  slug: rhombus-systems-service-management-integrations-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Storage Integrations Webservice API from Rhombus Systems — 18 operation(s) for storage integrations webservice.
  name: Rhombus Systems Storage Integrations Webservice API
  slug: rhombus-systems-storage-integrations-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The TvOs Config Webservice API from Rhombus Systems — 3 operation(s) for tvos config webservice.
  name: Rhombus Systems TvOs Config Webservice API
  slug: rhombus-systems-tvos-config-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Upload Webservice API from Rhombus Systems — 7 operation(s) for upload webservice.
  name: Rhombus Systems Upload Webservice API
  slug: rhombus-systems-upload-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The User Metadata Webservice API from Rhombus Systems — 8 operation(s) for user metadata webservice.
  name: Rhombus Systems User Metadata Webservice API
  slug: rhombus-systems-user-metadata-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The User Webservice API from Rhombus Systems — 12 operation(s) for user webservice.
  name: Rhombus Systems User Webservice API
  slug: rhombus-systems-user-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Vehicle Webservice API from Rhombus Systems — 12 operation(s) for vehicle webservice.
  name: Rhombus Systems Vehicle Webservice API
  slug: rhombus-systems-vehicle-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Video Webservice API from Rhombus Systems — 21 operation(s) for video webservice.
  name: Rhombus Systems Video Webservice API
  slug: rhombus-systems-video-webservice-api
- baseURL: https://api2.rhombussystems.com/api
  baseurl_source: declared
  description: The Webhook Integrations Webservice API from Rhombus Systems — 7 operation(s) for webhook integrations webservice.
  name: Rhombus Systems Webhook Integrations Webservice API
  slug: rhombus-systems-webhook-integrations-webservice-api
artifact_total: 73
asyncapis:
- description: ''
  name: Rhombus Systems Webhooks
  slug: rhombus-systems-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/rhombus-systems-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/rhombus-systems-openapi-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rhombus-systems-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rhombus-systems-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rhombus-systems-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.rhombus.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.rhombus.community/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.rhombus.community/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.rhombus.community/_llms/en/api-reference.md
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.rhombus.community/index.md
- group: operate
  title: ''
  type: Support
  url: https://www.rhombus.community/
- group: company
  title: ''
  type: Blog
  url: https://www.rhombus.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RhombusSystems
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rhombus.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://console.rhombus.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rhombus.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rhombus.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rhombus.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.rhombus.com/trust/
- group: auth
  title: ''
  type: Security
  url: security/rhombus-systems-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/rhombus-systems-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rhombus-systems-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/rhombus-systems-cli.yml
- group: design
  title: ''
  type: Components
  url: components/rhombus-systems-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rhombus-systems-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/rhombus-systems-api-catalog.json
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/rhombus-systems-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rhombus-systems-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/rhombus-systems-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/rhombus-systems-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rhombus-systems-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/rhombus-systems-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/rhombus-systems-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rhombus-systems-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rhombus-systems-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/rhombus-systems-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rhombus-systems-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rhombus-systems-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rhombus-systems-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rhombus-systems-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rhombus-systems-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rhombus-systems-webhooks.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/rhombus-systems-console-websocket-asyncapi.json
created: '2026-08-26'
description: 'Rhombus Systems is a Sacramento, California enterprise physical-security platform that unifies AI-powered security cameras, door access control, environmental and IoT sensors, audio gateways and TMA Five Diamond alarm monitoring in a single cloud console. The platform is API-first: every feature in the web console, mobile apps and firmware is backed by the same public REST API, which publishes an OpenAPI 3.0 contract of 952 operations across 64 service groups covering cameras and video streaming, access control credentials and doors, lockdown plans, face recognition, license plate and vehicle recognition, scene query, occupancy and reporting, policy alerts, webhooks, partner/MSP org management, and SAML SSO with SCIM provisioning. Rhombus also ships an AsyncAPI 3.0 contract for its STOMP-over-WebSocket change-event stream, an RFC 9727 API catalog, RFC 9728/8414 OAuth discovery, an A2A agent card, an llms.txt family, a Model Context Protocol server, a Go CLI, a React SDK, and
  a published Claude Code skills library.'
image: https://rhombus.com/img/meta-homepage.png
layout: provider
mcp_servers:
- description: ''
  name: Rhombus Systems MCP Server
  slug: rhombus-systems-mcp-server
modified: '2026-08-26'
name: Rhombus Systems
nav: Providers
network: true
overview: 'Rhombus Systems publishes 65 APIs on the [APIs.io](https://apis.io/) network, including Rhombus Console WebSocket API, Access Control Integrations Webservice API, Access Control Webservice API, and 62 more. Tagged areas include Physical Security, Video Surveillance, Access Control, IoT Sensors, and Cloud Video Management.


  The Rhombus Systems catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rhombus Systems'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 37 more developer resources.'
plans:
- name: Rhombus Systems Plans Pricing
  plan_count: 4
  slug: rhombus-systems-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Rhombus Systems Rate Limits
  slug: rhombus-systems-rate-limits
score:
  band: strong
  composite: 58.7
  coverage:
    artifact_dirs: 24
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 64.1
    developer_ergonomics: 59.5
    discoverability: 70.4
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 58.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 64
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rhombus-systems/refs/heads/main/screenshots/rhombus-systems-2026-09-02T153758.png
security:
- kind: authentication
  name: Rhombus Systems Authentication
  slug: rhombus-systems-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Rhombus Systems Domain Security
  slug: rhombus-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Rhombus Systems Vulnerability Disclosure
  slug: rhombus-systems-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Rhombus Systems Trust Center
  slug: rhombus-systems-trust-center
  summary_line: SOC 2, GDPR, HIPAA, PCI, BIPA, PIPEDA, CMMC, NIST, CJIS, NDAA, TAA
slug: rhombus-systems
tags:
- Physical Security
- Video Surveillance
- Access Control
- IoT Sensors
- Cloud Video Management
- Alarm Monitoring
- Computer-Vision
- Building Management
- Security Cameras
- Company
website: https://www.rhombus.com/
---
