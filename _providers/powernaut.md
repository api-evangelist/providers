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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 22
  human_in_the_loop: 5
  name: Powernaut Agentic Access
  operation_count: 38
  slug: powernaut-agentic-access
  summary_line: 38 operations · 22 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.powernaut.io
  baseurl_source: declared
  description: Authenticating with the Powernaut platform.
  name: Powernaut authentication API
  slug: powernaut-authentication-api
- baseURL: https://api.powernaut.io
  baseurl_source: declared
  description: 'With baselining, you indicate your normal consumption/production behaviour. This baseline is essential to provide flexibility, which is then defined as a deviation from this baseline. You can provide '
  name: Powernaut baselining API
  slug: powernaut-baselining-api
- baseURL: https://api.powernaut.io
  baseurl_source: declared
  description: A bid tells us how much flexibility is available in a certain time window.
  name: Powernaut creating_bids API
  slug: powernaut-creating-bids-api
- baseURL: https://api.powernaut.io
  baseurl_source: declared
  description: Events are EMS-initiated control actions that deviate from a resource's default behaviour (e.g. PV curtailment due to negative tariffs). Reporting these events helps us maintain clean training data fo
  name: Powernaut events API
  slug: powernaut-events-api
- baseURL: https://api.powernaut.io
  baseurl_source: declared
  description: 'You can retrieve forecasts to help plan your flexibility offerings and understand expected power consumption or production patterns. See the [guide](/guides/connect/forecasting/getting-forecasts) for '
  name: Powernaut getting_forecasts API
  slug: powernaut-getting-forecasts-api
- baseURL: https://api.powernaut.io
  baseurl_source: declared
  description: Upload historical meter data for your sites. Use these endpoints to import historical consumption and production data via CSV files.
  name: Powernaut historical_data API
  slug: powernaut-historical-data-api
- baseURL: https://api.powernaut.io
  baseurl_source: declared
  description: Manage your bids. You can update, cancel and receive notifications about bids. When a bid is accepted, you either get notified or you poll for status updates. Read more [here](/guides/connect/activati
  name: Powernaut managing_bids API
  slug: powernaut-managing-bids-api
- baseURL: https://api.powernaut.io
  baseurl_source: declared
  description: Markets are the electricity markets in which you can participate. Each market has a set of eligibility criteria, which you can query to see if you can participate in a certain market. Read our [guide]
  name: Powernaut markets API
  slug: powernaut-markets-api
- baseURL: https://api.powernaut.io
  baseurl_source: declared
  description: Metrics reported by resources and sites
  name: Powernaut metrics API
  slug: powernaut-metrics-api
- baseURL: https://api.powernaut.io
  baseurl_source: declared
  description: Register, modify or delete flexible resources. You can add flexible resources to each site, such as batteries, heat pumps, electric vehicles, ... They are the physical resource that can offer flexibil
  name: Powernaut resources API
  slug: powernaut-resources-api
- baseURL: https://api.powernaut.io
  baseurl_source: declared
  description: Read raw time series data from sensors attached to your sites, such as irradiance sensors on PV installations. Useful when you need measured conditions alongside metering data, for example to estimate
  name: Powernaut sensor_data API
  slug: powernaut-sensor-data-api
- baseURL: https://api.powernaut.io
  baseurl_source: declared
  description: Register, modify or delete sites. Sites are the start of everything, they are required to uniquely identify the end consumer's connection to the grid. They define the meter point(s) for which flexibil
  name: Powernaut sites API
  slug: powernaut-sites-api
- baseURL: https://api.powernaut.io
  baseurl_source: declared
  description: Sharing your forecasts helps us better understand your resources' expected behaviour, leading to improved flexibility opportunities and optimised market participation. See the [guide](/guides/connect/
  name: Powernaut uploading_forecasts API
  slug: powernaut-uploading-forecasts-api
- baseURL: https://api.powernaut.io
  baseurl_source: declared
  description: The accepting_bids API from Powernaut — 0 operation(s) for accepting_bids.
  name: Powernaut Accepting Bids API
  slug: powernaut-accepting-bids-api
artifact_total: 33
asyncapis:
- description: ''
  name: Powernaut Webhooks
  slug: powernaut-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Powernaut authentication API
  slug: open-powernaut-authentication-api
- collection_type: open
  name: Powernaut authentication baselining API
  slug: open-powernaut-baselining-api
- collection_type: open
  name: Powernaut authentication creating_bids API
  slug: open-powernaut-creating-bids-api
- collection_type: open
  name: Powernaut authentication events API
  slug: open-powernaut-events-api
- collection_type: open
  name: Powernaut authentication getting_forecasts API
  slug: open-powernaut-getting-forecasts-api
- collection_type: open
  name: Powernaut authentication historical_data API
  slug: open-powernaut-historical-data-api
- collection_type: open
  name: Powernaut authentication managing_bids API
  slug: open-powernaut-managing-bids-api
- collection_type: open
  name: Powernaut authentication markets API
  slug: open-powernaut-markets-api
- collection_type: open
  name: Powernaut authentication metrics API
  slug: open-powernaut-metrics-api
- collection_type: open
  name: Powernaut authentication resources API
  slug: open-powernaut-resources-api
- collection_type: open
  name: Powernaut authentication sensor_data API
  slug: open-powernaut-sensor-data-api
- collection_type: open
  name: Powernaut authentication sites API
  slug: open-powernaut-sites-api
- collection_type: open
  name: Powernaut authentication uploading_forecasts API
  slug: open-powernaut-uploading-forecasts-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/powernaut-partner-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: http://powernaut.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.powernaut.io/partner-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.powernaut.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.powernaut.io/partner-api
- group: operate
  title: ''
  type: Support
  url: https://powernaut.io/contact-us
- group: company
  title: ''
  type: Blog
  url: https://powernaut.io/insights
- group: start
  title: ''
  type: Login
  url: https://portal.powernaut.io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.powernaut.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/powernaut-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/powernaut-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/powernaut-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/powernaut-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/powernaut-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/powernaut-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/powernaut-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/powernaut-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/powernaut-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/powernaut-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/powernaut-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/powernaut-llms.txt
created: '2026-07-17'
description: Powernaut is a Virtual Power Plant (VPP) and energy-flexibility platform for energy retailers and independent power producers. Its Energy Operations Workspace connects and aggregates distributed energy resources — solar, batteries, EVs and HVAC — then forecasts, optimizes and trades their flexibility across day-ahead, intraday, imbalance, congestion and ancillary-service markets. The Powernaut Partner API (OpenAPI 3.0) exposes site and resource connectivity, credential management, baselining, market bidding, forecasting, sensor readings and metrics. Powernaut BV is based in Gent, Belgium and is backed by Seedcamp.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/powernaut.png
layout: provider
mcp_servers:
- description: ''
  name: Powernaut MCP Server
  slug: powernaut-mcp-server
modified: '2026-07-20'
name: Powernaut
nav: Providers
network: true
overview: 'Powernaut publishes 14 APIs on the [APIs.io](https://apis.io/) network, including authentication API, baselining API, creating_bids API, and 11 more. Tagged areas include Company, Energy, Virtual Power Plant, Distributed Energy Resources, and Energy Trading.


  The Powernaut catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Powernaut''s developer surface includes documentation, API reference, support, engineering blog, authentication, sandbox, and 16 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 66.4
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/powernaut/refs/heads/main/screenshots/powernaut-2026-09-02T151845.png
security:
- kind: authentication
  name: Powernaut Authentication
  slug: powernaut-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Powernaut Domain Security
  slug: powernaut-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: powernaut
tags:
- Company
- Energy
- Virtual Power Plant
- Distributed Energy Resources
- Energy Trading
- Flexibility
- Forecasting
- Grid
website: http://powernaut.io
---
