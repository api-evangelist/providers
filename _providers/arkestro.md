---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 68.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Arkestro Agentic Access
  operation_count: 46
  slug: arkestro-agentic-access
  summary_line: 46 operations · 22 acting
api_count: 2
apis:
- description: Public REST API for managing an Arkestro instance without a user session. Covers the creation and execution of sourcing events, event schedules and awards, event and document submissions, quote submis
  name: Arkestro API V2
  slug: arkestro-api-v2
- description: Remote Model Context Protocol server operated by Arkestro, authorized with OAuth 2.1 authorization code flow and mandatory PKCE S256 against the mcp:read, mcp:write and offline_access scopes. The endp
  name: Arkestro MCP Server
  slug: arkestro-mcp-server
artifact_total: 9
asyncapis:
- description: ''
  name: Arkestro Webhooks
  slug: arkestro-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://arkestro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.arkestro.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.arkestro.com/api-docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.arkestro.com/
- group: start
  title: ''
  type: Login
  url: https://app.arkestro.com/login
- group: operate
  title: ''
  type: Support
  url: https://arkestro.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://arkestro.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bid-ops-development
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arkestro.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arkestro.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.arkestrostatus.com/
- group: auth
  title: ''
  type: Compliance
  url: https://arkestro.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/arkestro-trust-center.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/arkestro-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/arkestro-mcp.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/arkestro-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arkestro-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/arkestro-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/arkestro-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/arkestro-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arkestro-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/arkestro-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/arkestro-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/arkestro-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arkestro-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arkestro-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arkestro-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/arkestro-api-v2-overlay.yaml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/arkestro-tool-crosswalk.yml
created: '2026-08-06'
description: Arkestro is a predictive procurement orchestration platform for enterprise sourcing teams, applying negotiation science, supplier science and process science to run competitive sourcing events at scale. The platform covers sourcing events and their schedules, supplier organizations and contacts, corporate item and category catalogs, purchase orders, document and quote submissions, awards, and event analytics. It serves automotive, oil and gas, high-tech manufacturing, construction, financial services and food and beverage buyers. Arkestro publishes a public OpenAPI 3.1.1 contract for its API V2 at api.arkestro.com and operates an OAuth 2.1 remote MCP server, though its developer documentation portal sits behind a customer sign-in wall.
image: https://arkestro.com/wp-content/uploads/arkestro_logo_featured_default.jpg
layout: provider
mcp_servers:
- description: ''
  name: arkestro-mcp.yml
  slug: arkestro-mcpyml
modified: '2026-08-06'
name: Arkestro
nav: Providers
network: true
overview: 'Arkestro publishes 1 API on the [APIs.io](https://apis.io/) network: API V2. Tagged areas include procurement, sourcing, supply-chain, spend-management, and e-sourcing.


  The Arkestro catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Arkestro''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 25 more developer resources.'
random_paper: 84
scopes:
- name: Arkestro Scopes
  scope_count: 3
  slug: arkestro-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 51.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 62.4
    developer_ergonomics: 56.5
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 28.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Arkestro Authentication
  slug: arkestro-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Arkestro Domain Security
  slug: arkestro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Arkestro Trust Center
  slug: arkestro-trust-center
  summary_line: ISO 27001:2022, SOC 2 Type II
slug: arkestro
tags:
- procurement
- sourcing
- supply-chain
- spend-management
- e-sourcing
- supplier-management
- purchase-orders
- procurement-analytics
- enterprise-software
- predictive-procurement
- mcp
- webhooks
website: https://arkestro.com/
---
