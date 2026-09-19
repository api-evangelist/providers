---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
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
    event_surface_described: derived
    idempotency: false
    mcp_server: templated
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-09-18'
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
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/changelog/tellius-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tellius-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/lifecycle/tellius-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tellius-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/authentication/tellius-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tellius-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/scopes/tellius-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tellius-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/conventions/tellius-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tellius-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/conformance/tellius-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tellius-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/conformance/tellius-conformance.yml
  title: ''
  type: Compliance
  url: conformance/tellius-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/mcp/tellius-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tellius-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/mcp/tellius-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tellius-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/llms/tellius-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tellius-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/well-known/tellius-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tellius-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/components/tellius-components.yml
  title: ''
  type: Components
  url: components/tellius-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/data-model/tellius-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tellius-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/packages/tellius-packages.yml
  title: ''
  type: Packages
  url: packages/tellius-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/plans/tellius-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tellius-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/rate-limits/tellius-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tellius-rate-limits.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/asyncapi/tellius-search-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/tellius-search-asyncapi.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/security/tellius-domain-security.yml
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
random_paper: 0
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
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 58.9
    discoverability: 75.9
    operational_transparency: 18.4
  previous_composite: 49.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/tellius/refs/heads/main/screenshots/tellius-2026-09-02T162748.png
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
