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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Hosted Model Context Protocol server (15 tools) plus REST API for compiling and querying codebase context: architecture overviews, code maps, file and symbol documentation, source retrieval, changelog'
  name: Driver Platform API & MCP Server
  slug: driver-platform-api-mcp-server
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.driver.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.driver.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.driver.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.driver.ai/docs/mcp-tools
- group: start
  title: ''
  type: GettingStarted
  url: https://www.driver.ai/docs/introduction-to-driver
- group: operate
  title: ''
  type: Support
  url: https://support.driver.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.driver.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/driver-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.driver.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.driver.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.driver.ai/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.driver.ai/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/driver-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/driver-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/driver-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/driver-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/driver-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/driver-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/driver-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/driver-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/driver-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/driver-llms.txt
created: '2026-07-17'
description: Driver is an AI platform that compiles exhaustive, structured context for codebases so AI coding agents and engineers can understand architecture, dependencies, and history without manually assembling context. It analyzes repositories, generates symbol-complete technical documentation, and keeps it synchronized as code changes, exposing the result through a hosted Model Context Protocol (MCP) server (15 tools) and a REST API. Driver integrates with Claude Code, Cursor, and VS Code + Copilot, supports multi-repository and multi-branch codebases, and offers enterprise SSO (SAML 2.0), SCIM 2.0 provisioning, machine identities, and single-tenant/FedRAMP deployment options. Backed by GV and Techstars.
image: https://www.driver.ai/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: driver-mcp.yml
  slug: driver-mcpyml
modified: '2026-07-18'
name: Driver
nav: Providers
network: true
overview: 'Driver publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Developer Tools, Code Documentation, and MCP.


  Driver''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 15 more developer resources.'
random_paper: 20
scopes:
- name: Driver Scopes
  scope_count: 3
  slug: driver-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 33.0
  delta: 0.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 32.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/driver/refs/heads/main/screenshots/driver-2026-07-25T212415.png
security:
- kind: authentication
  name: Driver Authentication
  slug: driver-authentication
  summary_line: oauth2/http/apiKey · 4 schemes
- kind: domain-security
  name: Driver Domain Security
  slug: driver-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Driver Trust Center
  slug: driver-trust-center
  summary_line: trust center published
slug: driver
tags:
- Company
- AI
- Developer Tools
- Code Documentation
- MCP
- Codebase Intelligence
- Agents
- Developer Experience
website: https://www.driver.ai
---
