---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: 'An authenticated Model Context Protocol (MCP) endpoint served from Aera Technology''s own corporate WordPress host. Anonymous discovery works: the site publishes RFC 9728 protected-resource metadata an'
  name: Aera Technology MCP Server
  slug: aera-technology-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.aeratechnology.com/
- group: company
  title: ''
  type: Blog
  url: https://www.aeratechnology.com/resources/?category=blogs
- group: company
  title: ''
  type: BlogRSS
  url: https://www.aeratechnology.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://community.aeratechnology.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aeratechnology.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aeratechnology.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aeratechnology.com/aera-security-privacy-documentation/
- group: auth
  title: ''
  type: TrustCenter
  url: security/aera-technology-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trustcenter.aeratechnology.com/
- group: auth
  title: ''
  type: Security
  url: https://app.sprinto.com/rdp/view/cc144494-8eb2-4c06-ad55-671eeba8881f
- group: company
  title: ''
  type: Partners
  url: https://www.aeratechnology.com/partners/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aera-technology-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aera-technology-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aera-technology-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aera-technology-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aera-technology-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aera-technology-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aera-technology-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aera-technology-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aera-technology-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aera-technology-problem-types.yml
coverage:
  checked: '2026-08-06'
  detail: Aera Decision Cloud's Document360 documentation site at docs.aeratechnology.com 302-redirects to Aera's identity provider (idp-dev.aeratechnology.com), so the product API reference and any spec require an active customer tenant; the only publicly discoverable machine surface is an auth-gated MCP server on the corporate WordPress host.
  evidence:
  - status: 302
    url: https://docs.aeratechnology.com/
  - status: 401
    url: https://www.aeratechnology.com/wp-json/mcp/mcp-oauth-server
  - status: 200
    url: https://www.aeratechnology.com/.well-known/oauth-protected-resource
  - status: 404
    url: https://www.aeratechnology.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-08-06'
description: Aera Technology is the Decision Intelligence company behind Aera Decision Cloud, an enterprise platform that digitizes, augments and automates operational decision making across supply chain, procurement, finance and commercial functions. The platform combines the Aera Decision Data Model, the Cortex AI/ML engine, multi-engine orchestration and agentic ambient intelligence with packaged Aera Skills, and is built and extended by customers through Aera Developer using low-code builders plus SQL, Java, Python and R. Aera Decision Cloud runs as a multi-tenant SaaS across US and EU regions; its developer documentation and API reference sit behind a customer SSO login, so no public OpenAPI or developer portal is available. The corporate site does publish an authenticated Model Context Protocol server discoverable through RFC 8414 / RFC 9728 well-known metadata.
image: https://www.aeratechnology.com/wp-content/uploads/2025/11/aera-logo.png
layout: provider
mcp_servers:
- description: ''
  name: aera-technology-mcp.yml
  slug: aera-technology-mcpyml
modified: '2026-08-06'
name: Aera Technology
nav: Providers
network: true
overview: 'Aera Technology publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Decision Intelligence, Artificial Intelligence, Enterprise Software, and Supply Chain.


  Aera Technology''s developer surface includes engineering blog, support, authentication, and 18 more developer resources.'
random_paper: 30
scopes:
- name: Aera Technology Scopes
  scope_count: 1
  slug: aera-technology-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 26.2
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 26.3
  previous_composite: 26.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Aera Technology Authentication
  slug: aera-technology-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Aera Technology Domain Security
  slug: aera-technology-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Aera Technology Vulnerability Disclosure
  slug: aera-technology-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aera Technology Trust Center
  slug: aera-technology-trust-center
  summary_line: ISO 27001, SOC 2, ISO 42001, GDPR, CPRA (formerly CCPA)
slug: aera-technology
tags:
- Company
- Decision Intelligence
- Artificial Intelligence
- Enterprise Software
- Supply Chain
- Automation
- Analytics
- Agents
website: https://www.aeratechnology.com/
---
