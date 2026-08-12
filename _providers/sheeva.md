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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Sheeva Agentic Access
  operation_count: 53
  slug: sheeva-agentic-access
  summary_line: 53 operations · 29 acting
api_count: 15
apis:
- description: The Authentication API from Sheeva — 1 operation(s) for authentication.
  name: Sheeva Authentication API
  slug: sheeva-authentication-api
- description: The Credit Cards API from Sheeva — 5 operation(s) for credit cards.
  name: Sheeva Credit Cards API
  slug: sheeva-credit-cards-api
- description: The Driver Alerts API from Sheeva — 2 operation(s) for driver alerts.
  name: Sheeva Driver Alerts API
  slug: sheeva-driver-alerts-api
- description: The Driver API from Sheeva — 5 operation(s) for driver.
  name: Sheeva Driver API
  slug: sheeva-driver-api
- description: The Feedback API from Sheeva — 3 operation(s) for feedback.
  name: Sheeva Feedback API
  slug: sheeva-feedback-api
- description: The Loyalty API from Sheeva — 2 operation(s) for loyalty.
  name: Sheeva Loyalty API
  slug: sheeva-loyalty-api
- description: The Parking API from Sheeva — 2 operation(s) for parking.
  name: Sheeva Parking API
  slug: sheeva-parking-api
- description: The Payments API from Sheeva — 3 operation(s) for payments.
  name: Sheeva Payments API
  slug: sheeva-payments-api
- description: The Service Hubs (Points Of Interest) API from Sheeva — 2 operation(s) for service hubs (points of interest).
  name: Sheeva Service Hubs (Points Of Interest) API
  slug: sheeva-service-hubs-points-of-interest-api
- description: The Session API from Sheeva — 7 operation(s) for session.
  name: Sheeva Session API
  slug: sheeva-session-api
- description: The Transactions API from Sheeva — 3 operation(s) for transactions.
  name: Sheeva Transactions API
  slug: sheeva-transactions-api
- description: The UPI API from Sheeva — 2 operation(s) for upi.
  name: Sheeva UPI API
  slug: sheeva-upi-api
- description: The Vehicle API from Sheeva — 3 operation(s) for vehicle.
  name: Sheeva Vehicle API
  slug: sheeva-vehicle-api
- description: The Vehicle Events API from Sheeva — 1 operation(s) for vehicle events.
  name: Sheeva Vehicle Events API
  slug: sheeva-vehicle-events-api
- description: The Webhooks API from Sheeva — 3 operation(s) for webhooks.
  name: Sheeva Webhooks API
  slug: sheeva-webhooks-api
artifact_total: 20
asyncapis:
- description: ''
  name: Sheeva Webhooks
  slug: sheeva-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://sheeva.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sheeva.ai/sheevaconnect-platform
- group: docs
  title: ''
  type: Documentation
  url: https://api-spec.sheeva.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api-spec.sheeva.ai/
- group: build
  title: ''
  type: Postman
  url: https://api-spec.sheeva.ai/
- group: company
  title: ''
  type: Blog
  url: https://sheeva.ai/blogs
- group: operate
  title: ''
  type: Support
  url: https://sheeva.ai/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://sheeva.ai/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sheeva.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sheeva.ai/legal/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sheevaai/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCgTP1ZcjfmfvAf_IxV1ucKQ
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/sheeva-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sheeva-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sheeva-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sheeva-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sheeva-agentic-access.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sheeva-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sheeva-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/sheeva-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/sheeva-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sheeva-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sheeva-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sheeva-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sheeva-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sheeva-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sheeva-domain-security.yml
created: '2026-07-17'
description: Sheeva.AI (legally Parkofon Inc.) builds transaction infrastructure for connected vehicles. Its SheevaConnect platform lets a vehicle discover nearby Sheeva Pay outlets, authenticate the driver, and pay for real-world services - fueling, EV charging, parking, tolling, QSR and curbside pickup, and car wash - directly from the infotainment system, using patented location intelligence (SheevaLocate, SheevaFence) and tokenized in-vehicle payments (SheevaPay). The SheevaConnect partner API 2.0 exposes drivers, vehicles, sessions, service hubs, payments, wallets and cards, loyalty, feedback, and HMAC-signed status webhooks across US and India regions.
image: https://cdn.prod.website-files.com/66e526d793f281dac248b0c4/677c3e75f423e08e3219b26e_SheevaLogowebclip.png
layout: provider
mcp_servers:
- description: ''
  name: sheeva-mcp.yml
  slug: sheeva-mcpyml
modified: '2026-07-21'
name: Sheeva
nav: Providers
network: true
overview: 'Sheeva publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Credit Cards API, Driver Alerts API, and 12 more. Tagged areas include Company, Connected Vehicles, Automotive, Payments, and Fintech.


  The Sheeva catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sheeva''s developer surface includes documentation, API reference, engineering blog, support, signup flow, YouTube channel, authentication, and 21 more developer resources.'
random_paper: 56
score:
  band: developing
  composite: 43.7
  delta: -1.5
  facets:
    commercial_clarity: 34.2
    contract_quality: 67.4
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Sheeva Authentication
  slug: sheeva-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Sheeva Domain Security
  slug: sheeva-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sheeva
tags:
- Company
- Connected Vehicles
- Automotive
- Payments
- Fintech
- In-Vehicle Payments
- EV Charging
- Parking
- Location Intelligence
- Mobility
website: https://sheeva.ai/
---
