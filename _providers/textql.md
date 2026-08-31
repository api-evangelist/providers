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
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.7
  scored_at: '2026-08-30'
api_count: 8
apis:
- description: The REST-native second generation of the TextQL Platform API. Standard HTTP methods, resource IDs in the path, query-parameter filtering and cursor pagination, a plain JSON error envelope, and SSE str
  name: TextQL v2 API
  slug: textql-v2-api
- description: The first-generation TextQL Platform API, exposed as Connect-RPC over HTTP POST. Documented as deprecated in favour of the v2 REST API but still published and served. Covers chat execution and streami
  name: TextQL Platform API (v1)
  slug: textql-platform-api-v1
- description: The full public Connect-RPC surface of the TextQL platform, generated from the protobuf service definitions and published with code samples. 407 operations across twenty services — dashboards, connect
  name: TextQL Public RPC API
  slug: textql-public-rpc-api
- description: TextQL's hosted, remote Model Context Protocol server. Any MCP-compatible client — Claude, Claude Code, Cursor, Windsurf, ChatGPT, Microsoft Copilot — points at the endpoint, authorizes once over OAut
  name: Ana MCP Server
  slug: textql-ana-mcp-server
artifact_total: 13
asyncapis:
- description: ''
  name: Textql Webhooks
  slug: textql-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://textql.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.textql.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.textql.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.textql.com/api-reference/v2/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.textql.com/core/get-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://textql.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TextQLLabs
- group: commercial
  title: ''
  type: Pricing
  url: https://textql.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.textql.com/
- group: start
  title: ''
  type: Login
  url: https://app.textql.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.textql.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.textql.com/
- group: auth
  title: ''
  type: Compliance
  url: security/textql-trust-center.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.textql.com/product/changelog
- group: other
  title: ''
  type: AgentCard
  url: a2a/textql-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/textql-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/textql-well-known.yml
- group: other
  title: ''
  type: OpenIDConnectDiscovery
  url: well-known/textql-openid-configuration.json
- group: build
  title: ''
  type: Packages
  url: packages/textql-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/textql-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/textql-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/textql-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/textql-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/textql-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/textql-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/textql-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/textql-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/textql-components.yml
- group: build
  title: ''
  type: CLI
  url: cli/textql-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/textql-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/textql-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/textql-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/textql-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/textql-problem-types.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/textql-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/textql-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/textql-webhooks.yml
created: '2026-08-30'
description: TextQL is an enterprise AI data platform built around Ana, an AI data scientist that connects to a company's warehouses, databases, BI tools and SaaS APIs and answers questions in plain language. Ana writes SQL, runs Python in a managed gVisor sandbox, searches the web, and produces charts, dashboards, scheduled reports (Playbooks) and long-running monitors (Agents) on top of a governed Ontology semantic layer. TextQL ships a public REST platform API in two generations — a v1 Connect-RPC surface and a REST-native v2 — plus an OAuth-authorized remote MCP server that exposes Ana to Claude, Cursor, ChatGPT, Copilot and any MCP-compatible client. First-party TypeScript and Python SDKs, embeddable iframe surfaces for Ana, dashboards and data apps, SAML/OIDC single sign-on with SCIM 2.0 provisioning, and self-hosted Helm deployment into a customer VPC round out the developer surface.
image: https://raw.githubusercontent.com/api-evangelist/textql/main/images/textql-og-card.png
layout: provider
mcp_servers:
- description: ''
  name: Ana MCP Server
  slug: ana-mcp-server
modified: '2026-08-30'
name: TextQL
nav: Providers
network: true
overview: 'TextQL publishes 3 APIs on the [APIs.io](https://apis.io/) network: v2 API, Platform API (v1), and Public RPC API. Tagged areas include Company, Artificial Intelligence, Analytics, Business Intelligence, and Data.


  The TextQL catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TextQL''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 31 more developer resources.'
plans:
- name: Textql Plans Pricing
  plan_count: 3
  slug: textql-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Textql Rate Limits
  slug: textql-rate-limits
scopes:
- name: Textql Scopes
  scope_count: 0
  slug: textql-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 24
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 54.5
    developer_ergonomics: 73.8
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 34.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
security:
- kind: authentication
  name: Textql Authentication
  slug: textql-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 5 schemes
- kind: domain-security
  name: Textql Domain Security
  slug: textql-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Textql Vulnerability Disclosure
  slug: textql-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Textql Trust Center
  slug: textql-trust-center
  summary_line: SOC 2 Type II, HIPAA, GDPR, SOX
slug: textql
tags:
- Company
- Artificial Intelligence
- Analytics
- Business Intelligence
- Data
- Agents
- MCP
- Semantic Layer
- Text-to-SQL
- Data Warehouse
- Enterprise
website: https://textql.com/
---
