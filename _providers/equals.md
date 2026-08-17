---
access_model:
  confidence: high
  label: Paid · Sales-gated
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://equals.com/pricing
  - plans/equals-plans-pricing.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 66.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Equals Agentic Access
  operation_count: 5
  slug: equals-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 2
apis:
- description: REST API for managing the facts the Equals AI analyst remembers about a workspace — the context it has learned from conversations or that a user added on the Memories page. Five operations (list, get,
  name: Equals Memories API
  slug: equals-memories-api
- description: Hosted, remote Model Context Protocol server that gives AI assistants direct access to an Equals workspace — search and list workbooks including team-trusted analyses, list connected datasources and e
  name: Equals MCP Server
  slug: equals-mcp-server
artifact_total: 8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/equals-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://equals.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.equals.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.equals.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.equals.com/docs/getting-started.md
- group: operate
  title: ''
  type: Support
  url: https://docs.equals.com/docs/resources.md
- group: commercial
  title: ''
  type: Pricing
  url: https://equals.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://go.equals.com/
- group: start
  title: ''
  type: Login
  url: https://go.equals.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://equals.com/policies/equals-online-terms-and-conditions-GP-april-11-22.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://equals.com/policies/privacy-policy.pdf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EqualsHQ
- group: operate
  title: ''
  type: StatusPage
  url: https://status.equals.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/equals-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/equals-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/equals-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/equals-domain-security.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.equals.com/docs/memories-api
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/equals-memories-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/equals-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/equals-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/equals-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/equals-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/equals-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/equals-plans-pricing.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/equals-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/equals-well-known.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/equals-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/equals-packages.yml
- group: design
  title: ''
  type: Components
  url: components/equals-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/equals-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.equals.com/docs/faq
- group: operate
  title: ''
  type: ChangeLog
  url: https://equals.com/launches/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/equals-changelog.yml
created: '2026-07-17'
description: Equals is an AI analytics platform that builds trusted spreadsheets and dashboards for revenue operations and go-to-market teams. It connects directly to databases and SaaS tools — PostgreSQL, MySQL, BigQuery, Snowflake, Redshift, Azure SQL, Supabase, Stripe, Salesforce, HubSpot, Intercom, and more — syncs data into a managed Equals Warehouse powered by Snowflake, and layers a familiar spreadsheet calculation, pivot, and charting surface with AI-powered querying on top. Teams use it to establish a single source of truth for metrics like ARR, pipeline, and retention, then auto-distribute live dashboards to Slack and email. Equals exposes a hosted Model Context Protocol (MCP) server so agents can discover workbooks, query connected datasources, and ask natural-language questions of company data.
image: https://avatars.githubusercontent.com/u/16228084?v=4
layout: provider
mcp_servers:
- description: ''
  name: equals-mcp.yml
  slug: equals-mcpyml
modified: '2026-08-14'
name: Equals
nav: Providers
network: true
overview: 'Equals publishes 1 API on the [APIs.io](https://apis.io/) network: Memories API. Tagged areas include Company, Analytics, Spreadsheets, Business Intelligence, and Dashboards.


  Equals'' developer surface includes documentation, getting-started guide, support, pricing, signup flow, API reference, authentication, and 28 more developer resources.'
plans:
- name: Equals Plans Pricing
  plan_count: 3
  slug: equals-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 0
  name: Equals Rate Limits
  slug: equals-rate-limits
score:
  band: strong
  composite: 60.0
  delta: 34.3
  facets:
    commercial_clarity: 84.2
    contract_quality: 60.7
    developer_ergonomics: 65.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 25.7
  provenance:
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/equals/refs/heads/main/screenshots/equals-2026-07-25T213540.png
security:
- kind: authentication
  name: Equals Authentication
  slug: equals-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Equals Domain Security
  slug: equals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: equals
tags:
- Company
- Analytics
- Spreadsheets
- Business Intelligence
- Dashboards
- Data
- Revenue Operations
- Reporting
- MCP
website: https://equals.com
---
