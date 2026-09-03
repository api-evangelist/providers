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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: 'REST API for the Epsilon3 operations platform, organized into roughly twenty API families: Builds (work orders, parts, inventory, purchase and sale orders, vendors, tooling, shipments), Chat, Commandi'
  name: Epsilon3 REST API
  slug: epsilon3-rest-api
- description: 'SocketIO and webhook realtime interface for integrating third-party systems with running Epsilon3 procedures. Four namespaces are published: commanding (/v1/commands/realtime), external data (/v1/exte'
  name: Epsilon3 Realtime API
  slug: epsilon3-realtime-api
- description: 'Hosted, remote Model Context Protocol server exposing Epsilon3 procedures, runs, parts and inventory, and issues to MCP-capable assistants. Read-only in the current preview: it can search, open, query'
  name: Epsilon3 MCP Server
  slug: epsilon3-mcp-server
artifact_total: 11
asyncapis:
- description: ''
  name: Epsilon3 Realtime Webhooks
  slug: epsilon3-realtime-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.epsilon3.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.epsilon3.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.epsilon3.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.epsilon3.io/#introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://support.epsilon3.io/en/articles/8779712-generate-api-key
- group: operate
  title: ''
  type: Support
  url: https://www.epsilon3.io/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.epsilon3.io/
- group: company
  title: ''
  type: Blog
  url: https://www.epsilon3.io/behind-the-console
- group: commercial
  title: ''
  type: Pricing
  url: https://www.epsilon3.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.epsilon3.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.epsilon3.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.epsilon3.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.epsilon3.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/epsilon3-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.epsilon3.io/security
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/epsilon3-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/epsilon3-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/epsilon3-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/epsilon3-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/epsilon3-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/epsilon3-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/epsilon3-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/epsilon3-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/epsilon3-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/epsilon3-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/epsilon3-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/epsilon3-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/epsilon3-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/epsilon3-realtime-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/epsilon3-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/epsilon3-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epsilon3-domain-security.yml
created: '2026-08-12'
description: Epsilon3 is a US-based operations software provider whose platform turns static procedures into live, executable, auditable workflows for high-reliability teams in space, defense, aerospace manufacturing, and energy. The product spans procedure authoring and execution (runs), work orders, parts and inventory, purchase and sale orders, tooling and maintenance, shipments, project schedules, issues, test and requirements management, skills, and telemetry/commanding. Its developer surface is a per-workspace API-key REST API at api.epsilon3.io/v1 documented across roughly twenty API families and 200-plus endpoints, a SocketIO and webhook realtime interface for commanding, external data, notifications and telemetry streaming, and a hosted read-only Model Context Protocol server at mcp.epsilon3.io fronted by OAuth 2.1 with dynamic client registration and fifteen published scopes. Customers include NASA, Blue Origin, Redwire, Axiom Space and AeroVironment; deployment options span multi-tenant
  cloud, UK and EU regions, on-premises, and FedRAMP High on AWS GovCloud.
image: https://static1.squarespace.com/static/602ec1c9965913605a250907/t/666747f4afb0bc6004370ebf/1785952863858/Epsilon3+Logo+2130x1200.jpg?format=1500w
layout: provider
mcp_servers:
- description: ''
  name: Epsilon3 MCP Server
  slug: epsilon3-mcp-server
modified: '2026-08-12'
name: Epsilon3
nav: Providers
network: true
overview: 'Epsilon3 publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Space, Defense, and Manufacturing.


  The Epsilon3 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Epsilon3''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Epsilon3 Plans Pricing
  plan_count: 3
  slug: epsilon3-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Epsilon3 Rate Limits
  slug: epsilon3-rate-limits
scopes:
- name: Epsilon3 Scopes
  scope_count: 15
  slug: epsilon3-scopes
  summary_line: 15 scopes · authorizationCode
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 17
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 53.6
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 78.9
  previous_composite: 57.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/epsilon3/refs/heads/main/screenshots/epsilon3-2026-08-17T080928.png
security:
- kind: authentication
  name: Epsilon3 Authentication
  slug: epsilon3-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Epsilon3 Domain Security
  slug: epsilon3-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Epsilon3 Trust Center
  slug: epsilon3-trust-center
  summary_line: SOC 2 Type II, FedRAMP High Authorization, NIST SP 800-171, DFARS 252.204-7012, CMMC, ITAR, EAR
slug: epsilon3
tags:
- Company
- Aerospace
- Space
- Defense
- Manufacturing
- Procedures
- Workflows
- Inventory
- Telemetry
- Test Management
- Project Management
- MCP
website: https://www.epsilon3.io/
---
