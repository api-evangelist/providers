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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 74
  human_in_the_loop: 0
  name: Kayhan Space Agentic Access
  operation_count: 151
  slug: kayhan-space-agentic-access
  summary_line: 151 operations · 74 acting
api_count: 1
apis:
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Authentication API from Kayhan Space — 8 operation(s) for authentication.
  name: Kayhan Space Authentication API
  slug: kayhan-space-authentication-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Catalog API from Kayhan Space — 3 operation(s) for catalog.
  name: Kayhan Space Catalog API
  slug: kayhan-space-catalog-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Conjunction API from Kayhan Space — 8 operation(s) for conjunction.
  name: Kayhan Space Conjunction API
  slug: kayhan-space-conjunction-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Ephemeris API from Kayhan Space — 11 operation(s) for ephemeris.
  name: Kayhan Space Ephemeris API
  slug: kayhan-space-ephemeris-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Events API from Kayhan Space — 2 operation(s) for events.
  name: Kayhan Space Events API
  slug: kayhan-space-events-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Health API from Kayhan Space — 1 operation(s) for health.
  name: Kayhan Space Health API
  slug: kayhan-space-health-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Launch Screening API from Kayhan Space — 5 operation(s) for launch screening.
  name: Kayhan Space Launch Screening API
  slug: kayhan-space-launch-screening-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The LEOP API from Kayhan Space — 5 operation(s) for leop.
  name: Kayhan Space LEOP API
  slug: kayhan-space-leop-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Maneuver Designer API from Kayhan Space — 6 operation(s) for maneuver designer.
  name: Kayhan Space Maneuver Designer API
  slug: kayhan-space-maneuver-designer-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Metrics API from Kayhan Space — 1 operation(s) for metrics.
  name: Kayhan Space Metrics API
  slug: kayhan-space-metrics-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Mission Planning API from Kayhan Space — 3 operation(s) for mission planning.
  name: Kayhan Space Mission Planning API
  slug: kayhan-space-mission-planning-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Mitigation API from Kayhan Space — 4 operation(s) for mitigation.
  name: Kayhan Space Mitigation API
  slug: kayhan-space-mitigation-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The NLP API from Kayhan Space — 3 operation(s) for nlp.
  name: Kayhan Space NLP API
  slug: kayhan-space-nlp-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Orbital Determination API from Kayhan Space — 7 operation(s) for orbital determination.
  name: Kayhan Space Orbital Determination API
  slug: kayhan-space-orbital-determination-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Plot API from Kayhan Space — 7 operation(s) for plot.
  name: Kayhan Space Plot API
  slug: kayhan-space-plot-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Propagation API from Kayhan Space — 11 operation(s) for propagation.
  name: Kayhan Space Propagation API
  slug: kayhan-space-propagation-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Satcat Service API API from Kayhan Space — 1 operation(s) for satcat service api.
  name: Kayhan Space Satcat Service API API
  slug: kayhan-space-satcat-service-api-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Screening API from Kayhan Space — 23 operation(s) for screening.
  name: Kayhan Space Screening API
  slug: kayhan-space-screening-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The State Vector API from Kayhan Space — 4 operation(s) for state vector.
  name: Kayhan Space State Vector API
  slug: kayhan-space-state-vector-api
- baseURL: https://api.satcat.com/api/satcat
  baseurl_source: declared
  description: The Two Line Elements (TLEs) API from Kayhan Space — 2 operation(s) for two line elements (tles).
  name: Kayhan Space Two Line Elements (TLEs) API
  slug: kayhan-space-two-line-elements-tles-api
arazzos:
- description: Upload CCSDS Conjunction Data Messages, attach one to a conjunction event, and inspect a specific CDM to support a mitigation decision.
  name: Ingest CDMs and inspect a conjunction event
  slug: kayhan-space-cdm-event-review
- description: Upload an operator ephemeris to Satcat, make it operational, run a conjunction screening, and pull the resulting CDMs and plot.
  name: Screen an ephemeris and review conjunctions
  slug: kayhan-space-screen-ephemeris
artifact_total: 48
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Satcat Service Authentication API
  slug: open-kayhan-space-authentication-api
- collection_type: open
  name: Satcat Service Authentication Catalog API
  slug: open-kayhan-space-catalog-api
- collection_type: open
  name: Satcat Service Authentication Conjunction API
  slug: open-kayhan-space-conjunction-api
- collection_type: open
  name: Satcat Service Authentication Ephemeris API
  slug: open-kayhan-space-ephemeris-api
- collection_type: open
  name: Satcat Service Authentication Events API
  slug: open-kayhan-space-events-api
- collection_type: open
  name: Satcat Service Authentication Health API
  slug: open-kayhan-space-health-api
- collection_type: open
  name: Satcat Service Authentication Launch Screening API
  slug: open-kayhan-space-launch-screening-api
- collection_type: open
  name: Satcat Service Authentication LEOP API
  slug: open-kayhan-space-leop-api
- collection_type: open
  name: Satcat Service Authentication Maneuver Designer API
  slug: open-kayhan-space-maneuver-designer-api
- collection_type: open
  name: Satcat Service Authentication Metrics API
  slug: open-kayhan-space-metrics-api
- collection_type: open
  name: Satcat Service Authentication Mission Planning API
  slug: open-kayhan-space-mission-planning-api
- collection_type: open
  name: Satcat Service Authentication Mitigation API
  slug: open-kayhan-space-mitigation-api
- collection_type: open
  name: Satcat Service Authentication NLP API
  slug: open-kayhan-space-nlp-api
- collection_type: open
  name: Satcat Service Authentication Orbital Determination API
  slug: open-kayhan-space-orbital-determination-api
- collection_type: open
  name: Satcat Service Authentication Plot API
  slug: open-kayhan-space-plot-api
- collection_type: open
  name: Satcat Service Authentication Propagation API
  slug: open-kayhan-space-propagation-api
- collection_type: open
  name: Satcat Service Authentication Satcat Service API API
  slug: open-kayhan-space-satcat-service-api-api
- collection_type: open
  name: Satcat Service Authentication Screening API
  slug: open-kayhan-space-screening-api
- collection_type: open
  name: Satcat Service Authentication State Vector API
  slug: open-kayhan-space-state-vector-api
- collection_type: open
  name: Satcat Service Authentication Two Line Elements (TLEs) API
  slug: open-kayhan-space-two-line-elements-tles-api
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
  name: Kayhan Space MCP Server
  slug: kayhan-space-mcp-server
modified: '2026-07-19'
name: Kayhan Space
nav: Providers
network: true
overview: 'Kayhan Space publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Catalog API, Conjunction API, and 17 more. Tagged areas include Company, Frontier Tech, Space, Satellite, and Space Situational Awareness.


  Kayhan Space''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 23 more developer resources.'
random_paper: 8
scopes:
- name: Kayhan Space Scopes
  scope_count: 1
  slug: kayhan-space-scopes
  summary_line: 1 scope · password/clientCredentials
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 53.3
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 42.2
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
