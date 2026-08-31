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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.3
  scored_at: '2026-08-30'
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
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Runway Export API
  slug: open-runway-financial-export-api
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
- description: Runway's hosted (remote) MCP server lets Claude and other AI tools read a Runway workspace. The connection authenticates with OAuth through the browser login (no API keys to manage). All hosted MCP to
  name: Runway Financial MCP Server
  slug: runway-financial-mcp-server
modified: '2026-07-21'
name: Runway Financial
nav: Providers
network: true
overview: 'Runway Financial publishes 1 API on the [APIs.io](https://apis.io/) network: Runway Export API. Tagged areas include Company, Financial Planning, FP&A, Forecasting, and Budgeting.


  Runway Financial''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, authentication, and 19 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 1
  name: Runway Financial Rate Limits
  slug: runway-financial-rate-limits
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 16
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 14.3
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/runway-financial/refs/heads/main/screenshots/runway-financial-2026-08-17T081657.png
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
- Software-as-a-Service
website: https://runway.cfo.ai
---
