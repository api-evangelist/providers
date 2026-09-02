---
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
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The Tellius backend REST and WebSocket API. Authenticate against /api/auth/login for a JWT (or a cookie session), then call the Insights APIs (list, delete, notifications), the Search APIs (a WebSocke
  name: Tellius Platform API
  slug: tellius-platform-api
- description: 'Tellius exposes its analytics engine through a hosted MCP server that runs inside each Tellius deployment. It speaks MCP over streamable HTTP (SSE available for older clients) and publishes 25 tools, '
  name: Tellius MCP Server
  slug: tellius-mcp-server
artifact_total: 9
asyncapis:
- description: Tellius' Search surface is not REST. Clients open a WebSocket, then exchange request and response messages that are correlated by a caller-generated `corrId`. The same channel delivers asynchronous jo
  name: Tellius Search and Job Notification WebSocket API
  slug: tellius-search-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.tellius.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.tellius.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://help.tellius.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.tellius.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.tellius.com/getting-started/quick-start-guides
- group: operate
  title: ''
  type: Support
  url: https://support.tellius.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.tellius.com/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tellius
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tellius.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.tellius.com/free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tellius.com/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tellius.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tellius-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tellius-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tellius-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tellius-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tellius-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tellius-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/tellius-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tellius-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tellius-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tellius-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tellius-well-known.yml
- group: design
  title: ''
  type: Components
  url: components/tellius-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tellius-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/tellius-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tellius-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tellius-rate-limits.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/tellius-search-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tellius-domain-security.yml
created: '2026-08-30'
description: 'Tellius is an agentic analytics platform that deploys AI agents ("Kaiya") on governed enterprise data to automate root cause analysis, variance decomposition and insight delivery across structured and unstructured sources. It sits above the data warehouse (Snowflake, Databricks, BigQuery, Redshift) without moving data, and exposes its analytics engine to developers three ways: a REST + WebSocket platform API (login/JWT, Search, Insights and ML prediction endpoints), an iFrame + postMessage embedding surface for Vizpads, Search, Kaiya and Feeds, and a hosted MCP server that any MCP client can call over streamable HTTP with OAuth. Because Tellius ships as a per-customer Kubernetes deployment, every API base URL and MCP endpoint is tenant-specific rather than a single shared public host. Founded by Ajay Khanna; SOC 2 Type II certified; 5x Gartner Magic Quadrant Visionary for Analytics and BI Platforms (2022-2026).'
image: https://cdn.prod.website-files.com/67fcfe6c0c7705918e4d7984/67fcfe6c0c7705918e4d798e_logo.svg
layout: provider
mcp_servers:
- description: Tellius exposes its analytics engine through an MCP server that runs inside each Tellius deployment. The server holds no data of its own — it forwards each request to Kaiya, which interprets the quest
  name: Tellius MCP Server
  slug: tellius-mcp-server
modified: '2026-08-30'
name: Tellius
nav: Providers
network: true
overview: 'Tellius publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Business Intelligence, Agentic Analytics, and Decision Intelligence.


  The Tellius catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tellius'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Tellius Plans Pricing
  plan_count: 2
  slug: tellius-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Tellius Rate Limits
  slug: tellius-rate-limits
scopes:
- name: Tellius Scopes
  scope_count: 1
  slug: tellius-scopes
  summary_line: 1 scope
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 19
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.3
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 50.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Tellius Authentication
  slug: tellius-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Tellius Domain Security
  slug: tellius-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tellius
tags:
- Company
- Analytics
- Business Intelligence
- Agentic Analytics
- Decision Intelligence
- Artificial Intelligence
- Machine-Learning
- Data
- Embedded Analytics
- MCP
- Natural Language Query
- Pharmaceuticals
- Consumer Packaged Goods
- Financial Planning
website: https://www.tellius.com/
---
