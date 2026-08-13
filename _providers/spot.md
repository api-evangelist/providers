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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Spot Agentic Access
  operation_count: 43
  slug: spot-agentic-access
  summary_line: 43 operations · 22 acting
api_count: 15
apis:
- description: The Analytics API from Spot — 3 operation(s) for analytics.
  name: Spot Analytics API
  slug: spot-analytics-api
- description: The Appliances API from Spot — 2 operation(s) for appliances.
  name: Spot Appliances API
  slug: spot-appliances-api
- description: The Audio API from Spot — 1 operation(s) for audio.
  name: Spot Audio API
  slug: spot-audio-api
- description: The Cameras API from Spot — 8 operation(s) for cameras.
  name: Spot Cameras API
  slug: spot-cameras-api
- description: The Embeds API from Spot — 2 operation(s) for embeds.
  name: Spot Embeds API
  slug: spot-embeds-api
- description: The Historical Footage API from Spot — 2 operation(s) for historical footage.
  name: Spot Historical Footage API
  slug: spot-historical-footage-api
- description: The Integration Devices API from Spot — 3 operation(s) for integration devices.
  name: Spot Integration Devices API
  slug: spot-integration-devices-api
- description: The Integration Event Types API from Spot — 2 operation(s) for integration event types.
  name: Spot Integration Event Types API
  slug: spot-integration-event-types-api
- description: The Integration Events API from Spot — 3 operation(s) for integration events.
  name: Spot Integration Events API
  slug: spot-integration-events-api
- description: The Integrations API from Spot — 2 operation(s) for integrations.
  name: Spot Integrations API
  slug: spot-integrations-api
- description: The Locations API from Spot — 1 operation(s) for locations.
  name: Spot Locations API
  slug: spot-locations-api
- description: The LPI API from Spot — 1 operation(s) for lpi.
  name: Spot LPI API
  slug: spot-lpi-api
- description: The LPR API from Spot — 1 operation(s) for lpr.
  name: Spot LPR API
  slug: spot-lpr-api
- description: The Shared Search API from Spot — 2 operation(s) for shared search.
  name: Spot Shared Search API
  slug: spot-shared-search-api
- description: The Zones API from Spot — 1 operation(s) for zones.
  name: Spot Zones API
  slug: spot-zones-api
artifact_total: 21
asyncapis:
- description: ''
  name: Spot Webhooks
  slug: spot-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/spot-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spot-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spot-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spot-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.spot.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.spot.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.spot.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.spot.ai/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.spot.ai/reference/authentication
- group: operate
  title: ''
  type: Support
  url: https://www.spot.ai/support
- group: company
  title: ''
  type: Blog
  url: https://www.spot.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spot.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.spot.ai/
- group: start
  title: ''
  type: Login
  url: https://dashboard.spot.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spot.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spot.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spotai
- group: auth
  title: ''
  type: Security
  url: https://www.spot.ai/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.spot.ai/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spot-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spot-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spot-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spot-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spot-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spot-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/spot-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spot-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/spot-devices-overlay.yaml
created: '2026-07-17'
description: 'Spot AI is a physical-security video-AI platform that turns surveillance cameras into AI agents which monitor spaces 24/7, detect suspicious activity, and trigger automated responses across retail, manufacturing, construction, healthcare, and education. The Spot AI Developer API is a JSON REST API on https://dev-api.spot.ai/ (bearer API-key auth) with three surfaces: Devices (locations, appliances, cameras, live/VOD embeds, historical footage, zones, shared searches, audio playback), Intelligence (people/vehicle counting, idle/presence analytics, and License Plate Recognition interest lists), and Spot Connect (a beta integrations platform that links external business events to camera footage via integrations, devices, event types, and events, with signed RSA256 webhooks for real-time delivery).'
image: /assets/icons/spot.png
layout: provider
mcp_servers:
- description: ''
  name: spot-mcp.yml
  slug: spot-mcpyml
modified: '2026-07-21'
name: Spot
nav: Providers
network: true
overview: 'Spot publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Appliances API, Audio API, and 12 more. Tagged areas include Company, Video, Physical Security, Surveillance, and Computer Vision.


  The Spot catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Spot''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 22 more developer resources.'
random_paper: 94
score:
  band: developing
  composite: 54.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 68.9
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 23.7
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Spot Authentication
  slug: spot-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spot Domain Security
  slug: spot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Spot Trust Center
  slug: spot-trust-center
  summary_line: SOC 2, HIPAA
slug: spot
tags:
- Company
- Video
- Physical Security
- Surveillance
- Computer Vision
- Artificial Intelligence
- Cameras
- Analytics
- License Plate Recognition
- Webhooks
- Integrations
website: https://www.spot.ai/
---
