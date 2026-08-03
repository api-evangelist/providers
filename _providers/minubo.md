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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Minubo Agentic Access
  operation_count: 8
  slug: minubo-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 3
apis:
- description: Auth endpoints
  name: Minubo Auth API
  slug: minubo-auth-api
- description: Data endpoints
  name: Minubo Data API
  slug: minubo-data-api
- description: ETL endpoints
  name: Minubo ETL API
  slug: minubo-etl-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Authenticate, discover the tenant schema, and run a data query.
  name: Query Minubo commerce data
  slug: minubo-query-commerce-data
- description: Authenticate, start an ETL process, and read its status.
  name: Trigger a Minubo ETL run and monitor it
  slug: minubo-trigger-etl-and-monitor
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://www.minubo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.minubo.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.minubo.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.minubo.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://api.minubo.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.minubo.com/de/preise
- group: company
  title: ''
  type: Blog
  url: https://blog.minubo.com/de/ecommerce-insights
- group: operate
  title: ''
  type: Support
  url: https://minubo.atlassian.net/servicedesk/customer/portals
- group: start
  title: ''
  type: SignUp
  url: https://app.minubo.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.minubo.com/de-de/legal/datenschutzbedingungen
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.minubo.com/de-de/legal/agb
- group: operate
  title: ''
  type: StatusPage
  url: https://status.minubo.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/minubo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/minubo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/minubo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/minubo-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/minubo-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/minubo-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/minubo-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/minubo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/minubo-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/minubo-query-commerce-data.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/minubo-trigger-etl-and-monitor.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/minubo-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/minubo-agentic-access.yml
created: '2026-07-17'
description: Minubo is a German business-intelligence platform for e-commerce and retail that integrates, models, and contextualizes commerce data — orders, products, customers, and suppliers — into AI Insights, Profit Management, reporting, and a supplier portal. Minubo also exposes a public REST API (Auth, ETL, and Data services) so tenants can authenticate with a JWT, trigger and monitor data loads, discover their queryable schema, and run queries against their modeled commerce data, plus connectors to tools like Power BI, Superset, n8n, and LLMs.
image: https://www.minubo.com/hubfs/minubo_logo_rz_POS_20210924.svg
layout: provider
mcp_servers:
- description: ''
  name: minubo-mcp.yml
  slug: minubo-mcpyml
modified: '2026-07-20'
name: Minubo
nav: Providers
network: true
overview: 'Minubo publishes 3 APIs on the [APIs.io](https://apis.io/) network: Auth API, Data API, and ETL API. Tagged areas include Company, E-Commerce, Business Intelligence, Analytics, and Retail.


  Minubo''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, signup flow, and 19 more developer resources.'
random_paper: 80
rate_limits:
- limit_count: 1
  name: Minubo Rate Limits
  slug: minubo-rate-limits
score:
  band: developing
  composite: 49.3
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 59.4
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 49.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Minubo Authentication
  slug: minubo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Minubo Domain Security
  slug: minubo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: minubo
tags:
- Company
- E-Commerce
- Business Intelligence
- Analytics
- Retail
- Data
- ETL
- Reporting
website: https://www.minubo.com/
---
