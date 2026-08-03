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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 74
  human_in_the_loop: 0
  name: Kayhan Space Agentic Access
  operation_count: 151
  slug: kayhan-space-agentic-access
  summary_line: 151 operations · 74 acting
api_count: 20
apis:
- description: The Authentication API from Kayhan Space — 8 operation(s) for authentication.
  name: Kayhan Space Authentication API
  slug: kayhan-space-authentication-api
- description: The Catalog API from Kayhan Space — 3 operation(s) for catalog.
  name: Kayhan Space Catalog API
  slug: kayhan-space-catalog-api
- description: The Conjunction API from Kayhan Space — 8 operation(s) for conjunction.
  name: Kayhan Space Conjunction API
  slug: kayhan-space-conjunction-api
- description: The Ephemeris API from Kayhan Space — 11 operation(s) for ephemeris.
  name: Kayhan Space Ephemeris API
  slug: kayhan-space-ephemeris-api
- description: The Events API from Kayhan Space — 2 operation(s) for events.
  name: Kayhan Space Events API
  slug: kayhan-space-events-api
- description: The Health API from Kayhan Space — 1 operation(s) for health.
  name: Kayhan Space Health API
  slug: kayhan-space-health-api
- description: The Launch Screening API from Kayhan Space — 5 operation(s) for launch screening.
  name: Kayhan Space Launch Screening API
  slug: kayhan-space-launch-screening-api
- description: The LEOP API from Kayhan Space — 5 operation(s) for leop.
  name: Kayhan Space LEOP API
  slug: kayhan-space-leop-api
- description: The Maneuver Designer API from Kayhan Space — 6 operation(s) for maneuver designer.
  name: Kayhan Space Maneuver Designer API
  slug: kayhan-space-maneuver-designer-api
- description: The Metrics API from Kayhan Space — 1 operation(s) for metrics.
  name: Kayhan Space Metrics API
  slug: kayhan-space-metrics-api
- description: The Mission Planning API from Kayhan Space — 3 operation(s) for mission planning.
  name: Kayhan Space Mission Planning API
  slug: kayhan-space-mission-planning-api
- description: The Mitigation API from Kayhan Space — 4 operation(s) for mitigation.
  name: Kayhan Space Mitigation API
  slug: kayhan-space-mitigation-api
- description: The NLP API from Kayhan Space — 3 operation(s) for nlp.
  name: Kayhan Space NLP API
  slug: kayhan-space-nlp-api
- description: The Orbital Determination API from Kayhan Space — 7 operation(s) for orbital determination.
  name: Kayhan Space Orbital Determination API
  slug: kayhan-space-orbital-determination-api
- description: The Plot API from Kayhan Space — 7 operation(s) for plot.
  name: Kayhan Space Plot API
  slug: kayhan-space-plot-api
- description: The Propagation API from Kayhan Space — 11 operation(s) for propagation.
  name: Kayhan Space Propagation API
  slug: kayhan-space-propagation-api
- description: The Satcat Service API API from Kayhan Space — 1 operation(s) for satcat service api.
  name: Kayhan Space Satcat Service API API
  slug: kayhan-space-satcat-service-api-api
- description: The Screening API from Kayhan Space — 23 operation(s) for screening.
  name: Kayhan Space Screening API
  slug: kayhan-space-screening-api
- description: The State Vector API from Kayhan Space — 4 operation(s) for state vector.
  name: Kayhan Space State Vector API
  slug: kayhan-space-state-vector-api
- description: The Two Line Elements (TLEs) API from Kayhan Space — 2 operation(s) for two line elements (tles).
  name: Kayhan Space Two Line Elements (TLEs) API
  slug: kayhan-space-two-line-elements-tles-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Upload CCSDS Conjunction Data Messages, attach one to a conjunction event, and inspect a specific CDM to support a mitigation decision.
  name: Ingest CDMs and inspect a conjunction event
  slug: kayhan-space-cdm-event-review
- description: Upload an operator ephemeris to Satcat, make it operational, run a conjunction screening, and pull the resulting CDMs and plot.
  name: Screen an ephemeris and review conjunctions
  slug: kayhan-space-screen-ephemeris
artifact_total: 28
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.satcat.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.satcat.com
- group: docs
  title: ''
  type: APIReference
  url: https://api.satcat.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.satcat.com/key-concepts/
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/2AuzMTBuJM
- group: company
  title: ''
  type: Blog
  url: https://kayhan.space/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kayhan-Space
- group: operate
  title: ''
  type: StatusPage
  url: https://status.satcat.com
- group: start
  title: ''
  type: Login
  url: https://www.satcat.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kayhan.space/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kayhan.space/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/kayhan-space-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kayhan-space-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kayhan-space-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kayhan-space-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/kayhan-space-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kayhan-space-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kayhan-space-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kayhan-space-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/kayhan-space-satcat-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/kayhan-space-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kayhan-space-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kayhan-space-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kayhan-space-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kayhan-space-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kayhan-space-screen-ephemeris.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kayhan-space-cdm-event-review.yml
- group: company
  title: ''
  type: Website
  url: https://kayhan.space/
created: '2026-07-17'
description: Kayhan Space is a spaceflight-safety company building autonomous space traffic coordination and collision-avoidance technology for satellite operators. Its Satcat platform delivers space situational awareness, conjunction assessment (CDM ingestion and analysis), on-orbit screening, ephemeris and Two-Line Element (TLE) catalog services, propagation, orbit determination, maneuver design, and collision-avoidance (COLA) planning through the Satcat Service API. Kayhan also offers Dynamics, an astrodynamics estimation and orbit-simulation engine. Founded in 2019 and backed by Initialized Capital and Techstars, Kayhan Space serves commercial, civil, and defense satellite operators.
image: https://www.satcat.com/og.png
layout: provider
mcp_servers:
- description: ''
  name: kayhan-space-mcp.yml
  slug: kayhan-space-mcpyml
modified: '2026-07-19'
name: Kayhan Space
nav: Providers
network: true
overview: 'Kayhan Space publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Catalog API, Conjunction API, and 17 more. Tagged areas include Company, Frontier Tech, Space, Satellite, and Space Situational Awareness.


  Kayhan Space''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 23 more developer resources.'
random_paper: 65
scopes:
- name: Kayhan Space Scopes
  scope_count: 1
  slug: kayhan-space-scopes
  summary_line: 1 scope · password/clientCredentials
score:
  band: developing
  composite: 47.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 55.7
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kayhan-space/refs/heads/main/screenshots/kayhan-space-2026-07-25T223529.png
security:
- kind: authentication
  name: Kayhan Space Authentication
  slug: kayhan-space-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Kayhan Space Domain Security
  slug: kayhan-space-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: kayhan-space
tags:
- Company
- Frontier Tech
- Space
- Satellite
- Space Situational Awareness
- Collision Avoidance
- Space Traffic Management
- Aerospace
- Astrodynamics
website: https://kayhan.space/
---
