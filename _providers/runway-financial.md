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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 72.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Runway Financial Agentic Access
  operation_count: 4
  slug: runway-financial-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: 'Limited, read-only REST API to programmatically export Runway model pages (submodels) and database pages as CSV, optionally within a proposal (scenario) layer. Bearer-authenticated with an API secret '
  name: Runway Export API
  slug: runway-export-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/runway-financial-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/runway-financial-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://runway.cfo.ai/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runway-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://runway.cfo.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://runway-docs.cfo.ai
- group: docs
  title: ''
  type: Documentation
  url: https://runway-docs.cfo.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://runway-docs.cfo.ai/get-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://runway.cfo.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://runway.cfo.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://runway.cfo.ai/demo
- group: start
  title: ''
  type: Login
  url: https://v2.cfo.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runway.cfo.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runway.cfo.ai/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@cfo.ai
- group: agent
  title: ''
  type: MCPServer
  url: mcp/runway-financial-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/runway-financial-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/runway-financial-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/runway-financial-agentic-access.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/runway-financial-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/runway-financial-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/runway-financial-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/runway-financial-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/runway-financial-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://runway.cfo.ai/security
created: '2026-07-17'
description: Runway is a financial planning and analysis (FP&A) platform for high-growth teams, offering collaborative planning, budgeting, revenue and headcount forecasting, scenario modeling, and variance analysis over 750+ connected data sources (accounting, HRIS, CRM, revenue, and data warehouses). Beyond the application, Runway exposes a limited bearer-authenticated Export API for programmatic CSV export of model and database pages, and a hosted, OAuth-based read-only MCP server so Claude and other AI tools can search and read a Runway workspace. Runway migrated its primary domain from runway.com to cfo.ai and is a 500 Global portfolio company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/runway-financial.png
layout: provider
mcp_servers:
- description: ''
  name: runway-financial-mcp.yml
  slug: runway-financial-mcpyml
modified: '2026-07-21'
name: Runway Financial
nav: Providers
network: true
overview: 'Runway Financial publishes 1 API on the [APIs.io](https://apis.io/) network: Runway Export API. Tagged areas include Company, Financial Planning, FP&A, Forecasting, and Budgeting.


  Runway Financial''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, authentication, and 19 more developer resources.'
random_paper: 24
rate_limits:
- limit_count: 1
  name: Runway Financial Rate Limits
  slug: runway-financial-rate-limits
score:
  band: developing
  composite: 52.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 60.2
    developer_ergonomics: 60.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 52.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Runway Financial Authentication
  slug: runway-financial-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Runway Financial Domain Security
  slug: runway-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Runway Financial Vulnerability Disclosure
  slug: runway-financial-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Runway Financial Trust Center
  slug: runway-financial-trust-center
  summary_line: SOC 2, GDPR
slug: runway-financial
tags:
- Company
- Financial Planning
- FP&A
- Forecasting
- Budgeting
- Finance
- MCP
- Export API
- SaaS
website: https://runway.cfo.ai
---
