---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.2
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Datarails Agentic Access
  operation_count: 5
  slug: datarails-agentic-access
  summary_line: 5 operations
api_count: 2
apis:
- description: Hosted Model Context Protocol server that connects an AI assistant to a tenant's Datarails financial data. Exposes read-only tools for discovering data models and fields, profiling numeric and categor
  name: Datarails FinanceOS MCP Server
  slug: financeos-mcp
- description: REST file-upload endpoint used to push a CSV or Excel file into a Datarails Filebox. Authenticated with HTTP Basic using a base64-encoded Datarails sync user (which must not have MFA enabled). The tar
  name: Datarails Data Gateway Service (DGS)
  slug: data-gateway-service
artifact_total: 11
collections:
- collection_type: open
  name: Datarails Finance OS MCP Server
  slug: open-datarails-financeos-mcp
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Datarails/dr-claude-code-plugins-re/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Datarails/dr-claude-code-plugins-re/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/Datarails/dr-claude-code-plugins-re/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.datarails.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.datarails.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://support.datarails.com/hc/en-us/articles/14616773038620-Data-Gateway-Service-DGS-API-Documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://support.datarails.com/hc/en-us/articles/25873904696860-Getting-Started-with-Datarails-on-Claude-Desktop
- group: operate
  title: ''
  type: Support
  url: https://support.datarails.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.datarails.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Datarails
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datarails.com/datarails-pricing/
- group: start
  title: ''
  type: Login
  url: https://auth.datarails.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datarails.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.datarails.com/terms-of-service/
- group: commercial
  title: ''
  type: AITerms
  url: https://www.datarails.com/datarails-ai-terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://datarails.statuspage.io/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.datarails.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/datarails-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datarails-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/datarails-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/datarails-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/datarails-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/datarails-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/datarails-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/datarails-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/datarails-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/datarails-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/datarails-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/datarails-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/datarails-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/datarails-packages.yml
- group: design
  title: ''
  type: Components
  url: components/datarails-components.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datarails-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/datarails-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/datarails-plans.yml
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/datarails_stock/
created: '2026-08-01'
description: 'Datarails is an Excel-native financial planning and analysis (FP&A) platform for the office of the CFO, marketed as FinanceOS. It consolidates data from ERP, CRM, HRIS, billing and operational systems into a single finance data model, then lets finance teams budget, forecast, consolidate, report and build dashboards while continuing to work in Excel through the Datarails Flex add-in. Its API surface is deliberately narrow and unusually agent-first: the primary programmatic interface is a hosted Model Context Protocol server at mcp.datarails.com, secured with OAuth 2.1 and PKCE, exposing roughly two dozen read-only tools for discovering data models, profiling fields, running filtered queries and asynchronous aggregations, and extracting validated financials into Excel. Datarails also ships a first-party Claude Code plugin carrying nineteen published Agent Skills, plus connectors for ChatGPT, Microsoft 365 Copilot and Lovable. The only documented conventional REST operation is
  the Data Gateway Service file-upload endpoint used to push CSV and Excel files into a Filebox.'
image: https://www.datarails.com/wp-content/uploads/2024/10/datarails-logo-1.png
layout: provider
mcp_servers:
- description: ''
  name: Datarails MCP Server
  slug: datarails-mcp-server
modified: '2026-08-01'
name: Datarails
nav: Providers
network: true
overview: 'Datarails publishes 1 API on the [APIs.io](https://apis.io/) network: FinanceOS MCP Server. Tagged areas include Company, FP&A, Financial Planning, Finance, and Accounting.


  Datarails'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 30 more developer resources.'
plans:
- name: Datarails Plans
  plan_count: 3
  slug: datarails-plans
random_paper: 4
rate_limits:
- limit_count: 1
  name: Datarails Rate Limits
  slug: datarails-rate-limits
scopes:
- name: Datarails Scopes
  scope_count: 1
  slug: datarails-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 57.7
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 30.3
    contract_quality: 34.7
    developer_ergonomics: 61.9
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 55.3
  previous_composite: 57.7
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datarails/refs/heads/main/screenshots/datarails-2026-08-07T164205.png
security:
- kind: authentication
  name: Datarails Authentication
  slug: datarails-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Datarails Domain Security
  slug: datarails-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Datarails Trust Center
  slug: datarails-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR
slug: datarails
tags:
- Company
- FP&A
- Financial Planning
- Finance
- Accounting
- Budgeting
- Forecasting
- Business Intelligence
- Reporting
- Data Integration
- MCP
- Artificial Intelligence
- Excel
- Software-as-a-Service
website: https://www.datarails.com/
---
