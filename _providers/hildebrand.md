---
access_model:
  confidence: high
  label: Paid · Contract required for organisational access; free self-serve for your own meter data via Bright
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://data.glowforindustry.com/
  - https://docs.glowmarkt.com/GlowmarktAPIDataRetrievalDocumentationIndividualUserForBright.pdf
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 45
  human_in_the_loop: 4
  name: Hildebrand Agentic Access
  operation_count: 106
  slug: hildebrand-agentic-access
  summary_line: 106 operations · 45 acting · 4 human-in-the-loop
api_count: 5
apis:
- description: 'User, account, authentication and consent management for the Glow Platform. Covers user registration, account profiles and sessions, JWT issuance via POST /auth, an OAuth 2.0 authorization-code grant '
  name: Glowmarkt User System API
  slug: glowmarkt-user-system-api
- description: Time-series energy data retrieval. A resource is a single data stream — electricity consumption, electricity cost, gas consumption, gas cost, electricity export, reactive import/export — each carrying
  name: Glowmarkt Resource System API
  slug: glowmarkt-resource-system-api
- description: CRUD over Virtual Entities — the Glow Platform's model of a physical "thing" such as a home or a site, made up of metadata and a collection of resources. Lists the virtual entities a caller has access
  name: Glowmarkt Virtual Entity System API
  slug: glowmarkt-virtual-entity-system-api
- description: Registration and status of the physical hardware feeding the platform — gateways such as the Glow CAD and GlowStick, sensors such as smart electricity meters, and actuators such as auxiliary load cont
  name: Glowmarkt Device Management System API
  slug: glowmarkt-device-management-system-api
- description: Alerting and messaging for Glow-based applications. Defines alert types, manages per-channel and per-culture message templates, sends alerts to users, and reports notification delivery and logs. Serve
  name: Glowmarkt Notification System API
  slug: glowmarkt-notification-system-api
artifact_total: 11
asyncapis:
- description: ''
  name: Hildebrand Event Surface
  slug: hildebrand-event-surface
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.glowmarkt.com/GlowmarktAPIDataRetrievalDocumentationIndividualUserForBright.pdf
- group: company
  title: ''
  type: Blog
  url: https://data.glowforindustry.com/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HildebrandTechnology
- group: auth
  title: ''
  type: Compliance
  url: https://www.hildebrand.co.uk/about
- group: design
  title: ''
  type: Conformance
  url: conformance/hildebrand-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hildebrand-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hildebrand-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hildebrand-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hildebrand-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/hildebrand-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hildebrand-plans.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hildebrand-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hildebrand-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hildebrand-event-surface.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hildebrand-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hildebrand-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hildebrand-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hildebrand.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://api.glowmarkt.com/api-docs/v0-1/resourcesys/
- group: docs
  title: ''
  type: APIReference
  url: https://api.glowmarkt.com/api-docs/v0-1/usersys/usertypes/
- group: start
  title: ''
  type: SignUp
  url: https://data.glowforindustry.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://data.glowforindustry.com/#pricing
- group: operate
  title: ''
  type: Support
  url: https://www.hildebrand.co.uk/contact-us
- group: operate
  title: ''
  type: Forum
  url: https://forum.glowmarkt.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hildebrand/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hildebrand.co.uk/privacy-policy
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-27'
description: 'Hildebrand Technology Limited is a London-based energy data company and, since 2019, the United Kingdom''s first independent DCC Other User with a direct connection to the Smart Data Communications Company network. It sits between Britain''s mandated smart-metering infrastructure and the applications built on top of it: it makes Glow hardware (CADs, in-home displays, sub-meters, temperature sensors), ingests and stores smart-meter reads at scale, and republishes them through the Glowmarkt Platform APIs, the consumer Bright app, and the commercial Glow Data Service. Its API posture is an honest reflection of the British market seam — Britain mandated the metering INFRASTRUCTURE, not a consumer data right, so there is no Consumer Data Right or Green Button obligation on Hildebrand and no standards-conformant data-sharing surface to point at. What exists instead is a proprietary but genuinely well-documented platform: five public Swagger 2.0 definitions are served anonymously
  from api.glowmarkt.com/api-docs, and any individual who installs Bright, creates an account and passes meter-point verification can call the same production API for their own household data with a published applicationId. Third-party organisational access to other people''s data is the closed half — it runs through Glow Data Service on a signed contract from GBP 595/month per MPxN, with consumer verification and consent captured per meter point. Hildebrand publishes no open grid or market data of any kind: every documented endpoint returns HTTP 400 without an applicationId header, so this is a closed-market-data, consent-gated-consumer-data provider.'
image: https://www.hildebrand.co.uk/images/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: hildebrand-mcp.yml
  slug: hildebrand-mcpyml
modified: '2026-07-27'
name: Hildebrand
nav: Providers
network: true
overview: 'Hildebrand publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Glowmarkt User System API, Glowmarkt Resource System API, Glowmarkt Virtual Entity System API, and 2 more. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Gas.


  The Hildebrand catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hildebrand''s developer surface includes getting-started guide, engineering blog, authentication, documentation, API reference, signup flow, pricing, and 21 more developer resources.'
plans:
- name: Hildebrand Plans
  plan_count: 3
  slug: hildebrand-plans
random_paper: 20
score:
  band: developing
  composite: 50.8
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 63.7
    developer_ergonomics: 47.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 13.2
  previous_composite: 50.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 35.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Hildebrand Authentication
  slug: hildebrand-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Hildebrand Domain Security
  slug: hildebrand-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hildebrand
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Smart Metering
- Energy Data
- Demand Response
- IoT
- Metering
website: https://www.hildebrand.co.uk/
---
