---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Revvo Agentic Access
  operation_count: 15
  slug: revvo-agentic-access
  summary_line: 15 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.revvo.ai/v0
  baseurl_source: declared
  description: Api key management (requires admin access)
  name: Revvo Api-keys API
  slug: revvo-api-keys-api
- baseURL: https://api.revvo.ai/v0
  baseurl_source: declared
  description: Get authorization token using an API key
  name: Revvo Auth API
  slug: revvo-auth-api
- baseURL: https://api.revvo.ai/v0
  baseurl_source: declared
  description: The Device API
  name: Revvo Device API
  slug: revvo-device-api
- baseURL: https://api.revvo.ai/v0
  baseurl_source: declared
  description: The Event API
  name: Revvo Event API
  slug: revvo-event-api
- baseURL: https://api.revvo.ai/v0
  baseurl_source: declared
  description: The Fleet API
  name: Revvo Fleet API
  slug: revvo-fleet-api
- baseURL: https://api.revvo.ai/v0
  baseurl_source: declared
  description: The Tire Operation API
  name: Revvo Tire Operation API
  slug: revvo-tire-operation-api
- baseURL: https://api.revvo.ai/v0
  baseurl_source: declared
  description: The Vehicle API
  name: Revvo Vehicle API
  slug: revvo-vehicle-api
arazzos:
- description: Authenticate, create a vehicle, register its gateway and sensors, then verify.
  name: Onboard a vehicle and its tire sensors
  slug: revvo-onboard-vehicle
- description: Authenticate and read tire events/alerts for a fleet over a time window.
  name: Pull tire events for a fleet
  slug: revvo-pull-tire-events
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: revvo-api Api-keys API
  slug: open-revvo-api-keys-api
- collection_type: open
  name: revvo-api Api-keys Auth API
  slug: open-revvo-auth-api
- collection_type: open
  name: revvo-api Api-keys Device API
  slug: open-revvo-device-api
- collection_type: open
  name: revvo-api Api-keys Event API
  slug: open-revvo-event-api
- collection_type: open
  name: revvo-api Api-keys Fleet API
  slug: open-revvo-fleet-api
- collection_type: open
  name: revvo-api Api-keys Tire Operation API
  slug: open-revvo-tire-operation-api
- collection_type: open
  name: revvo-api Api-keys Vehicle API
  slug: open-revvo-vehicle-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/revvo-capability-edges.yml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-21'
name: Revvo
nav: Providers
network: true
overview: 'Revvo publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Api-keys API, Auth API, Device API, and 4 more. Tagged areas include Company, Fleet Management, Transportation, Tire Management, and TPMS.


  Revvo''s developer surface includes documentation, API reference, engineering blog, support, signup flow, pricing, authentication, and 19 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 52.1
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/revvo/refs/heads/main/screenshots/revvo-2026-09-02T153731.png
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
website: https://www.revvo.ai
---
