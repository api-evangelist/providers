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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-08-19'
api_count: 8
apis:
- description: The agent API from Groundwork Open Source — 8 operation(s) for agent.
  name: Groundwork Open Source agent API
  slug: groundwork-open-source-agent-api
- description: The alert API from Groundwork Open Source — 3 operation(s) for alert.
  name: Groundwork Open Source alert API
  slug: groundwork-open-source-alert-api
- description: The connector API from Groundwork Open Source — 8 operation(s) for connector.
  name: Groundwork Open Source connector API
  slug: groundwork-open-source-connector-api
- description: The downtimes API from Groundwork Open Source — 2 operation(s) for downtimes.
  name: Groundwork Open Source downtimes API
  slug: groundwork-open-source-downtimes-api
- description: The event API from Groundwork Open Source — 3 operation(s) for event.
  name: Groundwork Open Source event API
  slug: groundwork-open-source-event-api
- description: The inventory API from Groundwork Open Source — 1 operation(s) for inventory.
  name: Groundwork Open Source inventory API
  slug: groundwork-open-source-inventory-api
- description: The metric API from Groundwork Open Source — 1 operation(s) for metric.
  name: Groundwork Open Source metric API
  slug: groundwork-open-source-metric-api
- description: The metrics API from Groundwork Open Source — 1 operation(s) for metrics.
  name: Groundwork Open Source metrics API
  slug: groundwork-open-source-metrics-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Groundwork Open Source agent API
  slug: open-groundwork-open-source-agent-api
- collection_type: open
  name: Groundwork Open Source agent alert API
  slug: open-groundwork-open-source-alert-api
- collection_type: open
  name: Groundwork Open Source agent connector API
  slug: open-groundwork-open-source-connector-api
- collection_type: open
  name: Groundwork Open Source agent downtimes API
  slug: open-groundwork-open-source-downtimes-api
- collection_type: open
  name: Groundwork Open Source agent event API
  slug: open-groundwork-open-source-event-api
- collection_type: open
  name: Groundwork Open Source agent inventory API
  slug: open-groundwork-open-source-inventory-api
- collection_type: open
  name: Groundwork Open Source agent metric API
  slug: open-groundwork-open-source-metric-api
- collection_type: open
  name: Groundwork Open Source agent metrics API
  slug: open-groundwork-open-source-metrics-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/gwos/tcg/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/gwos/tcg/blob/master/LICENSE
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/groundwork-open-source-tcg-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/groundwork-open-source-tcg-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/groundwork-open-source-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/groundwork-open-source-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/groundwork-open-source-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/groundwork-open-source-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/groundwork-open-source-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/groundwork-open-source-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/groundwork-open-source-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/groundwork-open-source-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/groundwork-open-source-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/groundwork-open-source-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/gwos/tcg#readme
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/gwos/tcg/blob/master/docs/swagger.yaml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/gwos/tcg
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gwos
created: '2026-07-17'
description: GroundWork Open Source, Inc. builds GroundWork Monitor, an open-source-based IT and network monitoring platform for hybrid infrastructure, assembling Nagios Core, Telegraf, InfluxDB, and Grafana into a unified availability, event, and metrics monitoring product. Its integration layer, the Transit Connection Generator (TCG), exposes a Controller REST API and a Go SDK for feeding host/ service inventory, metrics, alert events, and downtime windows into the GroundWork Foundation server. The platform is self-hosted; all source lives on GitHub under the gwos organization (TCG, Nagios Core, Grafana, and Telegraf forks). Surfaced as a portfolio company of Canaan Partners and enriched here from its live GitHub org and published Swagger 2.0 API specification.
image: https://raw.githubusercontent.com/gwos/tcg/master/.github/img/readme_image.png
layout: provider
mcp_servers:
- description: ''
  name: groundwork-open-source-mcp.yml
  slug: groundwork-open-source-mcpyml
modified: '2026-07-19'
name: Groundwork Open Source
nav: Providers
network: true
overview: 'Groundwork Open Source publishes 8 APIs on the [APIs.io](https://apis.io/) network, including agent API, alert API, connector API, and 5 more. Tagged areas include Company, Monitoring, Network Monitoring, IT Infrastructure, and Observability.


  Groundwork Open Source''s developer surface includes authentication, documentation, API reference, and 16 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 25.9
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 35.5
    developer_ergonomics: 37.5
    discoverability: 72.2
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 25.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/groundwork-open-source/refs/heads/main/screenshots/groundwork-open-source-2026-07-25T220352.png
security:
- kind: authentication
  name: Groundwork Open Source Authentication
  slug: groundwork-open-source-authentication
  summary_line: apiKey · 2 schemes
slug: groundwork-open-source
tags:
- Company
- Monitoring
- Network Monitoring
- IT Infrastructure
- Observability
- Metrics
- Events
- Open Source
- Nagios
---
