---
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 251
  human_in_the_loop: 11
  name: Mavenlink Agentic Access
  operation_count: 419
  slug: mavenlink-agentic-access
  summary_line: 419 operations · 251 acting · 11 human-in-the-loop
api_count: 3
apis:
- description: REST API for the Kantata OX (formerly Mavenlink) professional services automation platform. 419 operations across 218 paths cover workspaces (projects), stories (tasks), assignments, time entries, tim
  name: Kantata OX API
  slug: kantata-ox-api
- description: Remote Model Context Protocol server operated by Kantata on the Mavenlink API host. Advertised anonymously through RFC 9728 protected-resource metadata at https://api.mavenlink.com/.well-known/oauth-p
  name: Kantata OX MCP Server
  slug: kantata-ox-mcp-server
- description: Agent surface published on the Kantata developer portal. Serves an A2A agent card at /.well-known/agent-card.json (protocolVersion 0.3.0) that advertises an MCP extension, and an anonymous documentati
  name: Kantata OX Developer Documentation Agent
  slug: kantata-ox-developer-documentation-agent
artifact_total: 15
asyncapis:
- description: ''
  name: Mavenlink Event Surface
  slug: mavenlink-event-surface
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mavenlink-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mavenlink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kantata.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.kantata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kantata.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.kantata.com/kantata/specification
- group: start
  title: ''
  type: GettingStarted
  url: https://knowledge.kantata.com/hc/en-us/articles/202811760-Kantata-API-Overview
- group: operate
  title: ''
  type: Support
  url: https://www.kantata.com/customer-resources
- group: operate
  title: ''
  type: HelpCenter
  url: https://knowledge.kantata.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.kantata.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mavenlink
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kantata.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.mavenlink.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kantata.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kantata.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/mavenlink-trust-center.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mavenlink.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mavenlink-changelog.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/mavenlink-openapi.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/mavenlink-connector.proto
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mavenlink-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mavenlink-well-known.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/mavenlink-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mavenlink-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/mavenlink-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mavenlink-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mavenlink-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mavenlink-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mavenlink-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mavenlink-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mavenlink-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mavenlink-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mavenlink-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/mavenlink-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mavenlink-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mavenlink-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mavenlink-rate-limits.yml
created: '2026-08-25'
description: 'Mavenlink is the professional services automation (PSA) platform now shipped as Kantata OX, following the 2022 merger of Mavenlink and Kimble Applications that formed Kantata. It combines project management, resource management and forecasting, time and expense tracking, project accounting, invoicing, rate cards, and business intelligence for services organizations. The public REST API is still served from the original Mavenlink domain at https://api.mavenlink.com/api/v1/ and is documented as the "Kantata OX API" at developer.kantata.com: a Swagger 2.0 contract covering 419 operations across 218 paths and roughly 100 resource groups, authenticated with OAuth 2.0 authorization-code bearer tokens issued from app.mavenlink.com. Alongside REST the company operates an OAuth-gated remote MCP server at https://api.mavenlink.com/mcp, publishes an A2A agent card and an anonymous documentation MCP server on its developer portal, and ships a gRPC connector service definition that third
  parties implement to extend the Kantata Workflow Platform with custom triggers and actions.'
image: https://www.kantata.com/images/logos/Kantata.png
layout: provider
mcp_servers:
- description: ''
  name: Mavenlink MCP Server
  slug: mavenlink-mcp-server
- description: ''
  name: Mavenlink MCP Server
  slug: mavenlink-mcp-server-2
- description: ''
  name: Mavenlink MCP Server
  slug: mavenlink-mcp-server-3
modified: '2026-08-25'
name: Mavenlink
nav: Providers
network: true
overview: 'Mavenlink publishes 1 API on the [APIs.io](https://apis.io/) network: Kantata OX API. Tagged areas include Professional Services Automation, Project Management, Resource Management, Time Tracking, and Expense Management.


  The Mavenlink catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mavenlink''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 31 more developer resources.'
plans:
- name: Mavenlink Plans Pricing
  plan_count: 0
  slug: mavenlink-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Mavenlink Rate Limits
  slug: mavenlink-rate-limits
scopes:
- name: Mavenlink Scopes
  scope_count: 6
  slug: mavenlink-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 52.1
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 16.7
    contract_quality: 55.8
    developer_ergonomics: 66.1
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 34.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Mavenlink Authentication
  slug: mavenlink-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Mavenlink Domain Security
  slug: mavenlink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mavenlink Vulnerability Disclosure
  slug: mavenlink-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Mavenlink Trust Center
  slug: mavenlink-trust-center
  summary_line: trust center published
slug: mavenlink
tags:
- Professional Services Automation
- Project Management
- Resource Management
- Time Tracking
- Expense Management
- Invoicing
- Project Accounting
- Business Intelligence
- Workflow Automation
- MCP
- agent-native
- Company
website: https://www.kantata.com/
---
