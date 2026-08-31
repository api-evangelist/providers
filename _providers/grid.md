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
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://withgrid.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.saasgrid.com/
- group: operate
  title: ''
  type: Support
  url: https://help.saasgrid.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.saasgrid.com/articles/4405613168-getting-your-data-into-saasgrid
- group: company
  title: ''
  type: Blog
  url: https://www.withgrid.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.withgrid.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.withgrid.com/register
- group: start
  title: ''
  type: Login
  url: https://app.withgrid.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.withgrid.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.withgrid.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/grid-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grid-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SaaSGrid
- group: agent
  title: ''
  type: MCPServer
  url: mcp/grid-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/grid-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/grid-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/grid-trust-center.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/grid-plans-pricing.yml
created: '2026-07-17'
description: Grid (formerly SaaSGrid) is a revenue operations and financial platform that gives SaaS finance teams, CFOs, and RevOps a single source of truth for pipeline, billing, ARR, retention, revenue, and cash. It connects CRMs, billing systems, and ERPs — including Salesforce, HubSpot, NetSuite, QuickBooks, Sage Intacct, and Xero — to automate invoicing and reconciliation, produce real-time ARR, NDR, and churn reporting, and power revenue forecasting and scenario planning inside shareable dashboards. Surfaced as a portfolio company of craft-ventures, kindred-ventures, and obvious-ventures.
image: https://app.saasgrid.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: Grid operates an official REMOTE MCP server over the streamable-HTTP transport. It is the only programmatic surface Grid publishes — there is no public REST API, no OpenAPI, and no developer portal. T
  name: Grid MCP Server
  slug: grid-mcp-server
modified: '2026-08-13'
name: Grid
nav: Providers
network: true
overview: 'Grid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Revenue Operations, SaaS Metrics, and Billing.


  Grid''s developer surface includes documentation, support, getting-started guide, engineering blog, pricing, signup flow, authentication, and 11 more developer resources.'
plans:
- name: Grid Plans Pricing
  plan_count: 2
  slug: grid-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Grid Rate Limits
  slug: grid-rate-limits
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 29.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grid/refs/heads/main/screenshots/grid-2026-07-25T220324.png
security:
- kind: authentication
  name: Grid Authentication
  slug: grid-authentication
  summary_line: oauth2/http-bearer/saml2 · 3 schemes
- kind: domain-security
  name: Grid Domain Security
  slug: grid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Grid Trust Center
  slug: grid-trust-center
  summary_line: SOC 2 Type II
slug: grid
tags:
- Company
- Infrastructure
- Revenue Operations
- SaaS Metrics
- Billing
- Forecasting
- Financial Reporting
- FinOps
website: https://withgrid.com
---
