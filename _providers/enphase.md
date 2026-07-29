---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 40
  human_in_the_loop: 7
  name: Enphase Agentic Access
  operation_count: 148
  slug: enphase-agentic-access
  summary_line: 148 operations · 40 acting · 7 human-in-the-loop
api_count: 3
apis:
- description: 'The Monitoring API is the consumer-data surface of the Enphase platform and the only self-serve one. Documented across 48 paths and eight tags — System Details, Site Level Production Monitoring, Site '
  name: Enphase Monitoring API
  slug: enphase-monitoring-api
- description: The Commissioning API is the installer-facing administrative surface, documented across 21 paths and eleven tags — Activations, Arrays, Companies, Users, Home Owner, Meters, Grid Profiles, Tariff, Est
  name: Enphase Commissioning API
  slug: enphase-commissioning-api
- description: The Virtual Power Plant API is the grid-services surface, sold only to utilities, aggregators, DERMS providers and third-party owners registered as Enphase Grid Services partners — the pricing page ca
  name: Enphase VPP API
  slug: enphase-vpp-api
artifact_total: 12
asyncapis:
- description: Server-sent event stream of a single Enphase system's real-time power state. Derived by API Evangelist from the published Monitoring API operation getLiveData, which produces text/event-stream and car
  name: Enphase Enlighten Live Status Stream
  slug: enphase-live-status-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/enphase-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enphase-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/enphase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://enphase.com/cybersecurity
- group: auth
  title: ''
  type: Authentication
  url: authentication/enphase-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/enphase-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/enphase-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/enphase-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/enphase-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer-v4.enphase.com/aboutproduct.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/enphase-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/enphase-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/enphase-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/enphase-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/enphase-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/enphase-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/enphase-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/enphase-tool-crosswalk.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/enphase-live-status-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/enphase-llms.txt
- group: company
  title: ''
  type: Website
  url: https://enphase.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer-v4.enphase.com
- group: start
  title: ''
  type: SignUp
  url: https://developer-v4.enphase.com/signup
- group: start
  title: ''
  type: Login
  url: https://developer-v4.enphase.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://developer-v4.enphase.com/docs/quickstart.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer-v4.enphase.com/docs/quickstart.html
- group: auth
  title: ''
  type: Authentication
  url: https://developer-v4.enphase.com/docs/quickstart.html
- group: commercial
  title: ''
  type: Plans
  url: https://developer-v4.enphase.com/developer-plans
- group: commercial
  title: ''
  type: Pricing
  url: https://developer-v4.enphase.com/developer-plans
- group: operate
  title: ''
  type: RateLimits
  url: https://developer-v4.enphase.com/developer-plans
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer-v4.enphase.com/docs/release_notes
- group: operate
  title: ''
  type: Support
  url: https://developer-v4.enphase.com/docs/support
- group: operate
  title: ''
  type: Community
  url: https://community.enphase.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://enphase.com/legal/terms-of-service
- group: commercial
  title: ''
  type: LicenseAgreement
  url: https://enphase.com/api-license-agreement-v4
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://enphase.com/legal/privacy-policy
- group: company
  title: ''
  type: About
  url: https://developer-v4.enphase.com/aboutproduct.html
- group: company
  title: ''
  type: Blog
  url: https://newsroom.enphase.com/newsroom
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.enphase.com/
- group: other
  title: ''
  type: Email
  url: mailto:api@enphaseenergy.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer-v4.enphase.com/docs/monitoring_api
- group: operate
  title: ''
  type: FAQ
  url: https://developer-v4.enphase.com/docs/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/enphase
- group: auth
  title: ''
  type: SecurityAdvisories
  url: https://enphase.com/cybersecurity/advisories
created: '2026-07-27'
description: 'Enphase Energy is a Petaluma, California home-energy technology manufacturer and the dominant supplier of solar microinverters in the United States, shipping IQ Microinverters, IQ Batteries, IQ EV Chargers and the Envoy/IQ Gateway that ties them together through the Enlighten cloud. It sits on the DER side of the energy value chain rather than the utility side: it does not own meters, sell electricity, or operate a grid, so no consumer energy data mandate reaches it — there is no Green Button, ESPI or NAESB implementation anywhere in its developer surface, and the United States has no compulsory retail energy data right to designate it under. Its API posture is nevertheless unusually open for this sector. The Enphase Developer Portal at developer-v4.enphase.com is a genuine self-serve 3scale portal where anyone can register, create an application and subscribe to a free Watt plan, and it publishes three complete, anonymously downloadable machine-readable contracts covering
  124 paths and 148 operations. The split that defines Enphase is consumer-data-open, market-data-closed: a third-party developer can retrieve an individual homeowner''s site production, consumption, battery and EV charger telemetry through documented OAuth 2.0 authorization-code flows with the system owner''s explicit approval, but Enphase publishes no open grid, wholesale market or system-wide generation data of any kind. Access is tiered — self-serve for monitoring, application-approval for installer commissioning (10+ installations required), and partner-only for the Virtual Power Plant API, which is the one place a real standard appears: OCPP 1.6 for EV charger control against third-party CSMS platforms.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: enphase-mcp.yml
  slug: enphase-mcpyml
modified: '2026-07-27'
name: Enphase Energy
nav: Providers
network: true
overview: 'Enphase Energy publishes 3 APIs on the [APIs.io](https://apis.io/) network: Enphase Monitoring API, Enphase Commissioning API, and Enphase VPP API. Tagged areas include Energy, United States, Solar, DER, and Renewables.


  The Enphase Energy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Enphase Energy''s developer surface includes authentication, changelog, signup flow, documentation, getting-started guide, pricing, support, and 38 more developer resources.'
plans:
- name: Enphase Plans
  plan_count: 5
  slug: enphase-plans
random_paper: 11
rate_limits:
- limit_count: 0
  name: Enphase Rate Limits
  slug: enphase-rate-limits
scopes:
- name: Enphase Scopes
  scope_count: 0
  slug: enphase-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.5
  delta: -1.5
  facets:
    commercial_clarity: 76.3
    contract_quality: 51.6
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 59.0
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Enphase Authentication
  slug: enphase-authentication
  summary_line: oauth2/apiKey/http · 6 schemes
- kind: domain-security
  name: Enphase Domain Security
  slug: enphase-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Enphase Vulnerability Disclosure
  slug: enphase-vulnerability-disclosure
  summary_line: Hackerone
slug: enphase
tags:
- Energy
- United States
- Solar
- DER
- Renewables
- Battery Storage
- EV Charging
- Demand Response
- Virtual Power Plant
- Grid Services
- Microinverters
- Home Energy Management
- Smart Metering
- Telemetry
website: https://enphase.com
---
