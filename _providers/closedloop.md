---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Read-only /v1 REST API, team- and region-scoped, authenticated via X-API-Key. Exposes insights, products, themes, features, coverage/evidence, customers, customer context, competitors, trends, facets,
  name: ClosedLoop AI REST API
  slug: closedloop-ai-rest-api
- description: 'Hosted, first-class MCP server over HTTP with OAuth auth (interactive auto-registration or client_credentials for M2M). Ships MCP tools (query insights, context, customers, themes, competitors) and a '
  name: ClosedLoop AI MCP Server
  slug: closedloop-ai-mcp-server
- description: 'Set of ~25 pre-built Claude Code skills distributed as the ''closedloop-skills'' plugin via the Anthropic community marketplace, grouped by team (product/eng/sales/marketing/CS/leadership). Examples: De'
  name: ClosedLoop AI Claude Code Skills
  slug: closedloop-ai-claude-code-skills
artifact_total: 13
asyncapis:
- description: ''
  name: Closedloop Webhooks
  slug: closedloop-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://closedloop.sh/docs
- group: docs
  title: ''
  type: Documentation
  url: https://closedloop.sh/docs
- group: docs
  title: ''
  type: APIReference
  url: https://closedloop.sh/docs/api-reference/introduction
- group: start
  title: ''
  type: Quickstart
  url: https://closedloop.sh/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://closedloop.sh/pricing
- group: company
  title: ''
  type: Blog
  url: https://closedloop.sh/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.closedloop.sh/signup
- group: start
  title: ''
  type: Login
  url: https://app.closedloop.sh/login
- group: operate
  title: ''
  type: Support
  url: https://closedloop.sh/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://closedloop.sh/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://closedloop.sh/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/closed-loop-ai
- group: other
  title: ''
  type: AgentCard
  url: a2a/closedloop-a2a.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/closedloop-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/closedloop-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/closedloop-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/closedloop-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/closedloop-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/closedloop-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/closedloop-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/closedloop-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/closedloop-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/closedloop-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/closedloop-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/closedloop-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/closedloop-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/closedloop-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/closedloop-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/closedloop-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/closedloop-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://closedloop.sh/docs/llms.txt
created: '2026-08-30'
description: Product-intelligence platform that turns customer conversations and feedback (Gong, Fireflies, Slack, Zendesk, Intercom, Salesforce, HubSpot, surveys, product usage; 40+ integrations) into structured, source-traceable product insights, themes, buildable features, and prioritized roadmap decisions. Exposes a read-only /v1 REST API, a hosted MCP server, an llms.txt index, and published Claude Code skills.
image: https://closedloop.sh/assets/images/og-image.png
layout: provider
mcp_servers:
- description: 'Hosted remote MCP over Streamable HTTP with OAuth 2.1. deployment.mode=remote, endpoint https://mcp.closedloop.sh (EU: https://eu.mcp.closedloop.sh). Verified by probe 2026-08-30: POST tools/list retu'
  name: ClosedLoop AI MCP Server
  slug: closedloop-ai-mcp-server
- description: LIVE MCP, OAuth-gated. NOTE the path -- the endpoint is the HOST ROOT; https://mcp.closedloop.sh/mcp returns 404 ROUTE_NOT_FOUND. Verified 2026-08-30.
  name: ClosedLoop AI MCP Server
  slug: closedloop-ai-mcp-server-2
- description: EU regional MCP endpoint. Verified 2026-08-30, same 401 OAuth challenge.
  name: ClosedLoop AI MCP Server
  slug: closedloop-ai-mcp-server-3
modified: '2026-08-30'
name: ClosedLoop AI
nav: Providers
network: true
overview: 'ClosedLoop AI publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Product Intelligence, Customer Feedback, Voice of Customer, Product Management, and Agentic AI.


  The ClosedLoop AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ClosedLoop AI''s developer surface includes documentation, API reference, quickstart, pricing, engineering blog, signup flow, support, and 25 more developer resources.'
plans:
- name: Closedloop Plans Pricing
  plan_count: 3
  slug: closedloop-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Closedloop Rate Limits
  slug: closedloop-rate-limits
scopes:
- name: Closedloop Scopes
  scope_count: 0
  slug: closedloop-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.8
  coverage:
    artifact_dirs: 23
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.7
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 63.4
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 62.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Closedloop Authentication
  slug: closedloop-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Closedloop Domain Security
  slug: closedloop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Closedloop Trust Center
  slug: closedloop-trust-center
  summary_line: SOC 2 Type II, ISO 27001, PCI DSS, HIPAA, FedRAMP
slug: closedloop
tags:
- Product Intelligence
- Customer Feedback
- Voice of Customer
- Product Management
- Agentic AI
- MCP
- SaaS analytics
- A2A
- SCIM
- Product Discovery
website: https://closedloop.sh/docs
---
