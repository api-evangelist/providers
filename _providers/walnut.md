---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - https://www.walnut.io/pricing
  - https://help.walnut.io/help/api/customer-data-api
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Read-only REST API for Walnut demo analytics. Two data endpoints plus a health check — GET /demo-sessions returns individual demo-session records across 29 documented fields with filtering, offset pag
  name: Walnut Customer Data API
  slug: walnut-api
artifact_total: 9
asyncapis:
- description: ''
  name: Walnut Webhooks
  slug: walnut-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.walnut.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.walnut.io/help/api
- group: docs
  title: ''
  type: Documentation
  url: https://help.walnut.io/
- group: docs
  title: ''
  type: APIReference
  url: https://help.walnut.io/help/api/customer-data-api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.walnut.io/help/api/quick-start
- group: operate
  title: ''
  type: Support
  url: https://help.walnut.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/teamwalnut
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teamwalnut
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teamwalnut/
- group: company
  title: ''
  type: Blog
  url: https://www.walnut.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.walnut.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.walnut.io/get-a-demo/
- group: start
  title: ''
  type: Login
  url: https://app.teamwalnut.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.walnut.io/msa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.walnut.io/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.walnut.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/walnutinc
- group: commercial
  title: ''
  type: Plans
  url: plans/walnut-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/walnut-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/walnut-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/walnut-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/walnut-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/walnut-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/walnut-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/walnut-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/walnut-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/walnut-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/walnut-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/walnut-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/walnut-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/walnut-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/walnut-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/walnut-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/walnut-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/walnut-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/walnut-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/walnut-llms.txt
created: '2026-06-13'
description: Walnut is an AI-powered interactive demo platform for B2B go-to-market teams, used to capture a live product into an editable demo, personalize it at scale, embed it, and measure how buyers engage with it. Its developer surface is the Walnut Customer Data API — a read-only REST analytics API at customer-api.teamwalnut.com that returns demo-session records with 29 documented fields, plus filtering, offset pagination, field selection and multi-dimensional aggregation. Walnut also ships a first-party Model Context Protocol server that wraps the same three operations for AI assistants, and two signed webhook events for demo and playlist session completion. API and MCP access are exclusive to the enterprise Scale plan, and keys are issued by an account representative rather than self-service.
finops:
- name: Walnut Finops
  service_category: ''
  slug: walnut-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/walnut.png
layout: provider
mcp_servers:
- description: Walnut publishes a first-party Model Context Protocol server that wraps the Walnut Customer Data API and exposes its three read operations as MCP tools to Claude Desktop, Cursor, VS Code and any other
  name: Walnut MCP Server
  slug: walnut-mcp-server
modified: '2026-08-13'
name: Walnut
nav: Providers
network: true
overview: 'Walnut publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Demo, Interactive Demos, Product Demos, Sales Enablement, and Demo Analytics.


  The Walnut catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Walnut''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Walnut Plans Pricing
  plan_count: 3
  slug: walnut-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Walnut Rate Limits
  slug: walnut-rate-limits
score:
  band: strong
  composite: 64.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 48.1
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 64.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/walnut/refs/heads/main/screenshots/walnut-2026-06-20T201221.png
security:
- kind: authentication
  name: Walnut Authentication
  slug: walnut-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Walnut Domain Security
  slug: walnut-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Walnut Trust Center
  slug: walnut-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA
slug: walnut
tags:
- Sales Demo
- Interactive Demos
- Product Demos
- Sales Enablement
- Demo Analytics
- Go-To-Market
- AI-Powered
- Webhook
- MCP
- Analytics
website: https://www.walnut.io/
---
