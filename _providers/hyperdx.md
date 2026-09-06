---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The documented v1 API on HyperDX Cloud, covering alerts, dashboards and chart series queries at api.hyperdx.io under /api/v1, authenticated with a Bearer personal API key. Documented as prose on hyper
  name: HyperDX Cloud API (v1)
  slug: hyperdx-cloud-api-v1
- description: 'First-party Model Context Protocol server shipped inside the HyperDX API package, served at /api/mcp on your instance over Streamable HTTP with Bearer authentication. Exposes 27 tools covering source '
  name: HyperDX (ClickStack) MCP Server
  slug: hyperdx-mcp-server
- baseURL: https://{hyperdx-instance-host}/api/v2
  baseurl_source: declared
  description: Endpoints for managing monitoring alerts
  name: HyperDX Alerts API
  slug: hyperdx-alerts-api
- baseURL: https://{hyperdx-instance-host}/api/v2
  baseurl_source: declared
  description: Endpoints for querying chart data
  name: HyperDX Charts API
  slug: hyperdx-charts-api
- baseURL: https://{hyperdx-instance-host}/api/v2
  baseurl_source: declared
  description: Endpoints for managing ClickHouse connections
  name: HyperDX Connections API
  slug: hyperdx-connections-api
- baseURL: https://{hyperdx-instance-host}/api/v2
  baseurl_source: declared
  description: Endpoints for managing dashboards and their visualizations
  name: HyperDX Dashboards API
  slug: hyperdx-dashboards-api
- baseURL: https://{hyperdx-instance-host}/api/v2
  baseurl_source: declared
  description: The Saved Searches API from HyperDX — 2 operation(s) for saved searches.
  name: HyperDX Saved Searches API
  slug: hyperdx-saved-searches-api
- baseURL: https://{hyperdx-instance-host}/api/v2
  baseurl_source: declared
  description: Endpoints for querying raw data from log and trace sources
  name: HyperDX Search API
  slug: hyperdx-search-api
- baseURL: https://{hyperdx-instance-host}/api/v2
  baseurl_source: declared
  description: Endpoints for managing data sources
  name: HyperDX Sources API
  slug: hyperdx-sources-api
- baseURL: https://{hyperdx-instance-host}/api/v2
  baseurl_source: declared
  description: The Team API from HyperDX — 6 operation(s) for team.
  name: HyperDX Team API
  slug: hyperdx-team-api
- baseURL: https://{hyperdx-instance-host}/api/v2
  baseurl_source: declared
  description: Endpoints for managing webhooks
  name: HyperDX Webhooks API
  slug: hyperdx-webhooks-api
artifact_total: 17
asyncapis:
- description: ''
  name: Hyperdx Webhooks
  slug: hyperdx-webhooks
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/hyperdxio/hyperdx/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyperdx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hyperdx-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hyperdx.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.hyperdx.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.hyperdx.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.hyperdx.io/docs/api/alerts
- group: start
  title: ''
  type: GettingStarted
  url: https://www.hyperdx.io/docs/install
- group: company
  title: ''
  type: Blog
  url: https://www.hyperdx.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hyperdx.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.hyperdx.io/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hyperdx.io/terms/service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hyperdx.io/terms/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hyperdxio
- group: operate
  title: ''
  type: Support
  url: https://www.hyperdx.io/discord
- group: operate
  title: ''
  type: StatusPage
  url: https://hyperdx.statuspage.io/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/hyperdxio/hyperdx
- group: build
  title: ''
  type: Packages
  url: packages/hyperdx-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hyperdx-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/hyperdx-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hyperdx-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hyperdx-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hyperdx-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hyperdx-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hyperdx-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hyperdx-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hyperdx-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hyperdx-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hyperdx-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hyperdx-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hyperdx-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hyperdx-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hyperdx-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/hyperdx-external-api-overlay.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/hyperdx-external-api-openapi.json
created: '2026-08-27'
description: HyperDX is an open-source observability platform that unifies logs, metrics, traces, session replay and errors on top of ClickHouse and OpenTelemetry, giving engineers one place to search raw events, correlate a log line to its trace and that span to a session replay, build dashboards and run threshold alerts. It ships as an MIT-licensed self-hostable stack (the app, a Node.js API, an opinionated OpenTelemetry collector distribution and ClickHouse), as HyperDX Cloud at hyperdx.io, and as the user interface of ClickStack after ClickHouse acquired the company in March 2025. Its developer surface is a REST management API for dashboards, alerts, sources, saved searches, connections and webhooks, plus a first-party MCP server and an agent-friendly terminal CLI.
image: https://avatars.githubusercontent.com/u/130113031?v=4
layout: provider
mcp_servers:
- description: HyperDX ships a first-party Model Context Protocol server inside the product itself. It is served by the HyperDX API package at the /api/mcp path on the instance you run, over the Streamable HTTP tran
  name: HyperDX (ClickStack) MCP Server
  slug: hyperdx-clickstack-mcp-server
modified: '2026-08-27'
name: HyperDX
nav: Providers
network: true
overview: 'HyperDX publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Charts API, Connections API, and 6 more. Tagged areas include Company, Observability, Monitoring, Logging, and Tracing.


  The HyperDX catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HyperDX''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Hyperdx Plans Pricing
  plan_count: 4
  slug: hyperdx-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Hyperdx Rate Limits
  slug: hyperdx-rate-limits
score:
  band: strong
  composite: 64.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 65.3
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 63.2
  previous_composite: 64.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyperdx/refs/heads/main/screenshots/hyperdx-2026-09-02T145808.png
security:
- kind: authentication
  name: Hyperdx Authentication
  slug: hyperdx-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hyperdx Domain Security
  slug: hyperdx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hyperdx
tags:
- Company
- Observability
- Monitoring
- Logging
- Tracing
- Metrics
- OpenTelemetry
- ClickHouse
- Open-Source
- Alerting
- Dashboards
- Session Replay
- Developer Tools
- Agents
website: https://www.hyperdx.io/
---
