---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Revvo Agentic Access
  operation_count: 15
  slug: revvo-agentic-access
  summary_line: 15 operations · 10 acting
api_count: 7
apis:
- description: Api key management (requires admin access)
  name: Revvo Api-keys API
  slug: revvo-api-keys-api
- description: Get authorization token using an API key
  name: Revvo Auth API
  slug: revvo-auth-api
- description: The Device API
  name: Revvo Device API
  slug: revvo-device-api
- description: The Event API
  name: Revvo Event API
  slug: revvo-event-api
- description: The Fleet API
  name: Revvo Fleet API
  slug: revvo-fleet-api
- description: The Tire Operation API
  name: Revvo Tire Operation API
  slug: revvo-tire-operation-api
- description: The Vehicle API
  name: Revvo Vehicle API
  slug: revvo-vehicle-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Authenticate, create a vehicle, register its gateway and sensors, then verify.
  name: Onboard a vehicle and its tire sensors
  slug: revvo-onboard-vehicle
- description: Authenticate and read tire events/alerts for a fleet over a time window.
  name: Pull tire events for a fleet
  slug: revvo-pull-tire-events
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.revvo.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.revvo.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.revvo.ai/product/revvo-api/
- group: docs
  title: ''
  type: APIReference
  url: https://api.revvo.ai/v0/swagger-ui
- group: company
  title: ''
  type: Blog
  url: https://www.revvo.ai/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.revvo.ai/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://www.revvo.ai/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.revvo.ai/product/revvo-api/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.revvo.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.revvo.ai/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.revvo.ai
- group: auth
  title: ''
  type: Authentication
  url: authentication/revvo-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/revvo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revvo-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/revvo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/revvo-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/revvo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/revvo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/revvo-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/revvo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revvo-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/revvo-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/revvo-onboard-vehicle.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/revvo-pull-tire-events.yml
created: '2026-07-17'
description: 'Revvo is an AI-powered tire and fleet management platform. Its TireIQ engine connects to OEM and aftermarket TPMS sensors and turns raw tire data into real-time pressure, temperature, tread-wear, puncture and vehicle-off alerts delivered by SMS, email or API. The Revvo API is a v0 REST interface that lets fleets register gateways and sensors, manage vehicles and tires, and pull tire events, all scoped to a fleet. Authentication is a two-step exchange: a fleet API key is presented to POST /auth to mint a short-lived JWT, which is then sent as a bearer token on every operation. Revvo integrates with Geotab, Samsara, Motive, Fleetio, Lytx, Azuga and Zapier, and serves fleets across logistics, waste, food and beverage, oil and gas, and passenger transit.'
image: https://www.revvo.ai/wp-content/uploads/2023/11/cropped-Revvo_Icon_Black.png
layout: provider
mcp_servers:
- description: ''
  name: revvo-mcp.yml
  slug: revvo-mcpyml
modified: '2026-07-21'
name: Revvo
nav: Providers
network: true
overview: 'Revvo publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Api-keys API, Auth API, Device API, and 4 more. Tagged areas include Company, Fleet Management, Transportation, Tire Management, and TPMS.


  Revvo''s developer surface includes documentation, API reference, engineering blog, support, signup flow, pricing, authentication, and 18 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 41.2
  delta: -3.8
  facets:
    commercial_clarity: 44.7
    contract_quality: 46.5
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Revvo Authentication
  slug: revvo-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Revvo Domain Security
  slug: revvo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: revvo
tags:
- Company
- Fleet Management
- Transportation
- Tire Management
- TPMS
- Telematics
- IoT
- Logistics
- API
website: https://www.revvo.ai
---
