---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 23
  human_in_the_loop: 1
  name: Lunar Energy Agentic Access
  operation_count: 54
  slug: lunar-energy-agentic-access
  summary_line: 54 operations · 23 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: Gridshare publishes a remote Model Context Protocol (MCP) server that exposes the Customer API as MCP tools for AI agents. Authenticated with the same Cognito-issued bearer tokens as the Customer API.
  name: Gridshare Remote MCP Server
  slug: gridshare-remote-mcp
- baseURL: https://developer-api.customer.mygridshare.com
  baseurl_source: spec
  description: List, get, and partially update customer devices
  name: Lunar Energy Devices API
  slug: lunar-energy-devices-api
- baseURL: https://developer-api.partner.us.mygridshare.com
  baseurl_source: spec
  description: Request and commit differential adjustments to a prognosis
  name: Lunar Energy Diff Requests API
  slug: lunar-energy-diff-requests-api
- baseURL: https://developer-api.partner.us.mygridshare.com
  baseurl_source: spec
  description: Manage dynamic time-series tariffs with 7-day pagination
  name: Lunar Energy Dynamic Tariffs API
  slug: lunar-energy-dynamic-tariffs-api
- baseURL: https://developer-api.partner.us.mygridshare.com
  baseurl_source: spec
  description: Opt participants out of an active flex dispatch
  name: Lunar Energy Flex Dispatches API
  slug: lunar-energy-flex-dispatches-api
- baseURL: https://developer-api.partner.us.mygridshare.com
  baseurl_source: spec
  description: Schedule and update flex events for a flex group
  name: Lunar Energy Flex Events API
  slug: lunar-energy-flex-events-api
- baseURL: https://developer-api.partner.us.mygridshare.com
  baseurl_source: spec
  description: Define and manage groups of DERs participating in flex programs
  name: Lunar Energy Flex Groups API
  slug: lunar-energy-flex-groups-api
- baseURL: https://developer-api.customer.mygridshare.com
  baseurl_source: spec
  description: Read or change the Gridshare operation mode of a device
  name: Lunar Energy Operation Mode API
  slug: lunar-energy-operation-mode-api
- baseURL: https://developer-api.partner.us.mygridshare.com
  baseurl_source: spec
  description: Manage periodical (recurring) tariffs
  name: Lunar Energy Periodical Tariffs API
  slug: lunar-energy-periodical-tariffs-api
- baseURL: https://developer-api.customer.mygridshare.com
  baseurl_source: spec
  description: Read or set overlay plans for short-term device dispatch
  name: Lunar Energy Plans API
  slug: lunar-energy-plans-api
- baseURL: https://developer-api.partner.us.mygridshare.com
  baseurl_source: spec
  description: Forecasted aggregate power profiles for flex groups
  name: Lunar Energy Prognoses API
  slug: lunar-energy-prognoses-api
- baseURL: https://developer-api.customer.mygridshare.com
  baseurl_source: spec
  description: List sites and read site topology
  name: Lunar Energy Sites API
  slug: lunar-energy-sites-api
- baseURL: https://developer-api.customer.mygridshare.com
  baseurl_source: spec
  description: Time-bucketed per-sensor telemetry readings
  name: Lunar Energy Telemetry API
  slug: lunar-energy-telemetry-api
- baseURL: https://developer-api.partner.us.mygridshare.com
  baseurl_source: spec
  description: Record on-site visits for installation or service
  name: Lunar Energy Visits API
  slug: lunar-energy-visits-api
artifact_total: 68
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gridshare Customer API
  slug: open-gridshare-customer-api
- collection_type: open
  name: Gridshare Partner API
  slug: open-gridshare-partner-api
- collection_type: open
  name: Gridshare Customer Devices API
  slug: open-lunar-energy-devices-api
- collection_type: open
  name: Gridshare Customer Devices Diff Requests API
  slug: open-lunar-energy-diff-requests-api
- collection_type: open
  name: Gridshare Customer Devices Dynamic Tariffs API
  slug: open-lunar-energy-dynamic-tariffs-api
- collection_type: open
  name: Gridshare Customer Devices Flex Dispatches API
  slug: open-lunar-energy-flex-dispatches-api
- collection_type: open
  name: Gridshare Customer Devices Flex Events API
  slug: open-lunar-energy-flex-events-api
- collection_type: open
  name: Gridshare Customer Devices Flex Groups API
  slug: open-lunar-energy-flex-groups-api
- collection_type: open
  name: Gridshare Customer Devices Operation Mode API
  slug: open-lunar-energy-operation-mode-api
- collection_type: open
  name: Gridshare Customer Devices Periodical Tariffs API
  slug: open-lunar-energy-periodical-tariffs-api
- collection_type: open
  name: Gridshare Customer Devices Plans API
  slug: open-lunar-energy-plans-api
- collection_type: open
  name: Gridshare Customer Devices Prognoses API
  slug: open-lunar-energy-prognoses-api
- collection_type: open
  name: Gridshare Customer Devices Sites API
  slug: open-lunar-energy-sites-api
- collection_type: open
  name: Gridshare Customer Devices Telemetry API
  slug: open-lunar-energy-telemetry-api
- collection_type: open
  name: Gridshare Customer Devices Visits API
  slug: open-lunar-energy-visits-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lunar-energy-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lunar-energy-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lunar-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lunar-energy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lunar-energy-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.lunarenergy.com
- group: start
  title: ''
  type: Portal
  url: https://www.gridshare.com
- group: start
  title: ''
  type: Portal
  url: https://developers.gridshare.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gridshare.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.gridshare.com/reference/authentication
- group: other
  title: ''
  type: Product
  url: https://www.lunarenergy.com/lunar-system
- group: other
  title: ''
  type: Product
  url: https://www.gridshare.com
- group: docs
  title: ''
  type: Documentation
  url: https://installerhub.lunarenergy.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gridshare.com/reference/telemetry-key-concepts
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gridshare.com/reference/topology-key-concepts
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gridshare.com/reference/fleet-management
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gridshare.com/reference/energy-management
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gridshare.com/reference/vpp
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gridshare.com/reference/websocket-connection
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gridshare.com/reference/customer-remote-mcp
- group: operate
  title: ''
  type: Support
  url: mailto:developers@gridshare.com
- group: operate
  title: ''
  type: Support
  url: mailto:business@lunarenergy.com
- group: operate
  title: ''
  type: Contact
  url: https://www.lunarenergy.com/contact
- group: company
  title: ''
  type: Careers
  url: https://www.lunarenergy.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lunar-energy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Lunar_Energy
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@lunar_energy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lunarenergy
- group: commercial
  title: ''
  type: Plans
  url: plans/lunar-energy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lunar-energy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lunar-energy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.lunarenergy.com/blog
created: '2026-05-25'
description: Lunar Energy is a Mountain View, California-based residential clean-energy company founded in August 2020 by former Tesla Energy executive Kunal Girotra. The company designs and manufactures the Lunar System — a modular home battery (15–30 kWh, 9.6 kW continuous / 15 kW peak), Lunar Inverter, Lunar Maximizers (module-level power optimizers), Lunar Bridge meter socket adapter, and Eaton AbleEdge smart-breaker integration — controlled by the Lunar App with Lunar AI optimization. Its Gridshare platform is a grid-edge DERMS (Distributed Energy Resource Management System) and virtual power plant engine that manages 130,000+ residential distributed energy resources representing 1.2 GWh of connected storage across multiple manufacturers and third-party operators. Gridshare powers utility demand response and VPP programs through flex groups, flex dispatches, prognoses, dynamic and periodical tariffs, and per-device remote operation-mode control. Lunar Energy is backed by SunPower and
  Sunrun partnerships; SoftBank Energy is a major investor. The Gridshare Partner API and Customer API are gated behind business onboarding — credentials are issued by Lunar Energy after contacting developers@gridshare.com.
features:
- Lunar System home battery — 15–30 kWh modular wall-mounted tower
- 9.6 kW continuous / 15 kW peak (5s) per battery; 12.5-year warranty
- Lunar Inverter and Lunar Maximizers (650 W module-level power optimizers)
- Lunar Bridge (200 A meter socket adapter) connects the home to the grid
- Eaton AbleEdge smart breakers for automatic load-shedding during outages
- Lunar App for real-time monitoring and control
- Lunar AI generates daily energy plans from utility rates, weather, and home patterns
- Solar-ready — Maximizers attach to existing panels without relocation
- Virtual Power Plant participation — earn revenue by sharing storage with the grid
- Gridshare DERMS manages 130,000+ residential DERs and 1.2 GWh of storage
- Multi-vendor support — Gridshare manages devices from different manufacturers and 3rd-party operators
- Partner API for fleet operators (utilities, retailers, DER aggregators)
- Customer API for app developers acting on behalf of homeowners
- OAuth 2.0 — client-credentials for Partner, Authorization Code for Customer
- Per-device Operation Mode — Simple, Schedule, Smart (AI-optimized), Unknown
- Overlay Plans for short-term device dispatch
- Periodical Tariffs and Dynamic Tariffs (7-day pagination windows)
- Flex Groups, Flex Events, Flex Dispatches, and Flex Dispatch opt-outs
- Prognoses, Prognosis Diff Requests, and Diff Orders for coordinated network flex
- Counterfactual telemetry — what the device would have done un-managed
- WebSocket telemetry streams
- Remote MCP server exposes the Customer API as agent tools
- Octopus Energy partnership — battery electricity plans in Texas
- Sunrun and SunPower installer Okta SSO
finops:
- name: Lunar Energy Finops
  service_category: Energy and Distributed Resources
  slug: lunar-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lunar-energy.png
json_schemas:
- name: Gridshare Device
  property_count: 9
  slug: gridshare-device
- name: Gridshare Flex Event
  property_count: 8
  slug: gridshare-flex-event
- name: Gridshare Telemetry
  property_count: 2
  slug: gridshare-telemetry
jsonld:
- class_count: 0
  name: Lunar Energy Context
  property_count: 8
  slug: lunar-energy-context
layout: provider
modified: '2026-05-25'
name: Lunar Energy
nav: Providers
network: true
overview: 'Lunar Energy publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Devices API, Diff Requests API, Dynamic Tariffs API, and 10 more. Tagged areas include Energy, Home Battery, Solar, Virtual Power Plant, and DERMS.


  The Lunar Energy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Lunar Energy''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, YouTube channel, engineering blog, and 25 more developer resources.'
plans:
- name: Lunar Energy Plans Pricing
  plan_count: 4
  slug: lunar-energy-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Lunar Energy Rate Limits
  slug: lunar-energy-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Lunar Energy API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: gridshare-rules
- effective_rule_count: 5
  extends: []
  name: Lunar Energy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: lunar-energy-jsonschema-spectral-rules
scopes:
- name: Lunar Energy Scopes
  scope_count: 4
  slug: lunar-energy-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 33.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 54.5
    contract_quality: 56.1
    developer_ergonomics: 44.0
    discoverability: 59.3
    governance: 54.5
    operational_transparency: 34.2
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 52.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lunar-energy/refs/heads/main/screenshots/lunar-energy-2026-06-20T184758.png
security:
- kind: authentication
  name: Lunar Energy Authentication
  slug: lunar-energy-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Lunar Energy Domain Security
  slug: lunar-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Lunar Energy Trust Center
  slug: lunar-energy-trust-center
  summary_line: SOC 2, ISO 27001
slug: lunar-energy
tags:
- Energy
- Home Battery
- Solar
- Virtual Power Plant
- DERMS
- Distributed Energy Resources
- Grid Services
- Demand Response
- Storage
- Inverter
- Smart Home
- Energy Management
- Tariffs
- Telemetry
- VPP
- Flex Events
website: https://www.lunarenergy.com
---
