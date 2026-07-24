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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 71.2
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 22
  human_in_the_loop: 5
  name: Powernaut Agentic Access
  operation_count: 38
  slug: powernaut-agentic-access
  summary_line: 38 operations · 22 acting · 5 human-in-the-loop
api_count: 13
apis:
- description: Authenticating with the Powernaut platform.
  name: Powernaut authentication API
  slug: powernaut-authentication-api
- description: 'With baselining, you indicate your normal consumption/production behaviour. This baseline is essential to provide flexibility, which is then defined as a deviation from this baseline. You can provide '
  name: Powernaut baselining API
  slug: powernaut-baselining-api
- description: A bid tells us how much flexibility is available in a certain time window.
  name: Powernaut creating_bids API
  slug: powernaut-creating-bids-api
- description: Events are EMS-initiated control actions that deviate from a resource's default behaviour (e.g. PV curtailment due to negative tariffs). Reporting these events helps us maintain clean training data fo
  name: Powernaut events API
  slug: powernaut-events-api
- description: 'You can retrieve forecasts to help plan your flexibility offerings and understand expected power consumption or production patterns. See the [guide](/guides/connect/forecasting/getting-forecasts) for '
  name: Powernaut getting_forecasts API
  slug: powernaut-getting-forecasts-api
- description: Upload historical meter data for your sites. Use these endpoints to import historical consumption and production data via CSV files.
  name: Powernaut historical_data API
  slug: powernaut-historical-data-api
- description: Manage your bids. You can update, cancel and receive notifications about bids. When a bid is accepted, you either get notified or you poll for status updates. Read more [here](/guides/connect/activati
  name: Powernaut managing_bids API
  slug: powernaut-managing-bids-api
- description: Markets are the electricity markets in which you can participate. Each market has a set of eligibility criteria, which you can query to see if you can participate in a certain market. Read our [guide]
  name: Powernaut markets API
  slug: powernaut-markets-api
- description: Metrics reported by resources and sites
  name: Powernaut metrics API
  slug: powernaut-metrics-api
- description: Register, modify or delete flexible resources. You can add flexible resources to each site, such as batteries, heat pumps, electric vehicles, ... They are the physical resource that can offer flexibil
  name: Powernaut resources API
  slug: powernaut-resources-api
- description: Read raw time series data from sensors attached to your sites, such as irradiance sensors on PV installations. Useful when you need measured conditions alongside metering data, for example to estimate
  name: Powernaut sensor_data API
  slug: powernaut-sensor-data-api
- description: Register, modify or delete sites. Sites are the start of everything, they are required to uniquely identify the end consumer's connection to the grid. They define the meter point(s) for which flexibil
  name: Powernaut sites API
  slug: powernaut-sites-api
- description: Sharing your forecasts helps us better understand your resources' expected behaviour, leading to improved flexibility opportunities and optimised market participation. See the [guide](/guides/connect/
  name: Powernaut uploading_forecasts API
  slug: powernaut-uploading-forecasts-api
artifact_total: 18
asyncapis:
- description: ''
  name: Powernaut Webhooks
  slug: powernaut-webhooks
common:
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
  name: powernaut-mcp.yml
  slug: powernaut-mcpyml
modified: '2026-07-20'
name: Powernaut
nav: Providers
network: true
overview: 'Powernaut publishes 13 APIs on the [APIs.io](https://apis.io/) network, including authentication API, baselining API, creating_bids API, and 10 more. Tagged areas include Company, Energy, Virtual Power Plant, Distributed Energy Resources, and Energy Trading.


  The Powernaut catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Powernaut''s developer surface includes documentation, API reference, support, engineering blog, authentication, sandbox, and 15 more developer resources.'
random_paper: 28
score:
  band: developing
  composite: 46.3
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 71.8
    developer_ergonomics: 63.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 46.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
