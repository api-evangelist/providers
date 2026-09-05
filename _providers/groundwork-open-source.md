---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The agent API from Groundwork Open Source — 8 operation(s) for agent.
  name: Groundwork Open Source agent API
  slug: groundwork-open-source-agent-api
- description: The alert API from Groundwork Open Source — 3 operation(s) for alert.
  name: Groundwork Open Source alert API
  slug: groundwork-open-source-alert-api
- description: The downtimes API from Groundwork Open Source — 2 operation(s) for downtimes.
  name: Groundwork Open Source downtimes API
  slug: groundwork-open-source-downtimes-api
- description: The inventory API from Groundwork Open Source — 1 operation(s) for inventory.
  name: Groundwork Open Source inventory API
  slug: groundwork-open-source-inventory-api
- description: The metric API from Groundwork Open Source — 1 operation(s) for metric.
  name: Groundwork Open Source metric API
  slug: groundwork-open-source-metric-api
- description: The metrics API from Groundwork Open Source — 1 operation(s) for metrics.
  name: Groundwork Open Source metrics API
  slug: groundwork-open-source-metrics-api
artifact_total: 16
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
  type: X-MCPServerCandidate
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
modified: '2026-07-19'
name: Groundwork Open Source
nav: Providers
network: true
overview: 'Groundwork Open Source publishes 6 APIs on the [APIs.io](https://apis.io/) network, including agent API, alert API, downtimes API, and 3 more. Tagged areas include Company, Monitoring, Network Monitoring, IT Infrastructure, and Observability.


  Groundwork Open Source''s developer surface includes authentication, documentation, API reference, and 16 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 37.8
    developer_ergonomics: 37.5
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 24.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Event
- Open-Source
- Nagios
---
