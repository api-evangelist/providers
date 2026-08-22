---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Amuncore Agentic Access
  operation_count: 5
  slug: amuncore-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: Generated REST API over a connected database — full CRUD across chosen tables, with auth, pagination and docs handled by the platform.
  name: AmunCore API
  slug: amuncore-api
artifact_total: 11
asyncapis:
- description: ''
  name: Amuncore Webhooks
  slug: amuncore-webhooks
collections:
- collection_type: open
  name: 'AmunCore API Engine: Dynamic API'
  slug: open-amuncore-dynamic-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amuncore-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amuncore-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amuncore.com
- group: docs
  title: ''
  type: Documentation
  url: https://amuncore.com/swagger
- group: agent
  title: ''
  type: LLMsTxt
  url: https://amuncore.com/llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/amuncore-dynamic-api-openapi.yml
- group: build
  title: ''
  type: Examples
  url: examples/amuncore-dynamic-api-examples.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/amuncore-dynamic-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amuncore-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amuncore-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amuncore-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/amuncore-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amuncore-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/amuncore-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amuncore-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amuncore-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/amuncore-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amuncore-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amuncore-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amuncore-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amuncore-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/amuncore-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/amuncore-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/amuncore-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/amuncore-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://amuncore.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://amuncore.com/Register
- group: start
  title: ''
  type: Login
  url: https://amuncore.com/Auth/Login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amuncore.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amuncore.com/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://amuncore.com/#contact
- group: company
  title: ''
  type: About
  url: https://amuncore.com/about.html
created: '2026-08-03'
description: 'AmunCore turns a database into a secure REST API without writing a backend. You connect a database, pick tables, and endpoints go live with routing, authentication, validation, pagination, joins, errors, logs and docs already handled — the layer between a database and HTTP that would otherwise be a two-to-six-week project. It supports SQL Server, MySQL, MariaDB, PostgreSQL, Oracle and SQLite, with a visual builder that is the same regardless of the engine underneath. It is MCP-native by design: the endpoints you build become tools an AI assistant can call under the same keys, permissions and audit trail, and the MCP endpoint is live, token-gated and now fronted by RFC 8414/9728 OAuth discovery. A public OpenAPI 3.0.1 describes the five generated CRUD operations; REST auth is an X-Api-Key header. Built and operated by HYNOWorld, with a self-hosted option for regulated deployments. Full CRUD, a free plan forever, and paid tiers from $29/mo.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amuncore.png
layout: provider
mcp_servers:
- description: ''
  name: amuncore-mcp.yml
  slug: amuncore-mcpyml
modified: '2026-08-10'
name: AmunCore
nav: Providers
network: true
overview: 'AmunCore publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Database, API Management, Backend, No Code, and SQL.


  The AmunCore catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AmunCore''s developer surface includes documentation, code examples, authentication, sandbox, pricing, signup flow, support, and 26 more developer resources.'
plans:
- name: Amuncore Plans Pricing
  plan_count: 4
  slug: amuncore-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Amuncore Rate Limits
  slug: amuncore-rate-limits
scopes:
- name: Amuncore Scopes
  scope_count: 1
  slug: amuncore-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 56.3
  delta: -1.1
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 30.3
    contract_quality: 64.3
    developer_ergonomics: 35.1
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 39.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 57.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amuncore/refs/heads/main/screenshots/amuncore-2026-08-07T161347.png
security:
- kind: authentication
  name: Amuncore Authentication
  slug: amuncore-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Amuncore Domain Security
  slug: amuncore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Amuncore Trust Center
  slug: amuncore-trust-center
  summary_line: trust center published
slug: amuncore
tags:
- Database
- API Management
- Backend
- No Code
- SQL
- PostgreSQL
- MySQL
- Oracle
- MCP
- Agents
- Data
- SQL Server
- Webhooks
- OpenAPI
- Low Code
- Egypt
website: https://amuncore.com
---
