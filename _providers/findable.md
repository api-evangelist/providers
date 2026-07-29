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
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for AI-powered document search and Q&A across building documentation, plus management of buildings, documents, building owners, reports, and building categories. Supports SSE streaming on the
  name: Findable Partner API
  slug: findable-partner-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/findable-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.findable.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.findable.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.findable.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.findable.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.findable.ai/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.findable.ai/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/findable-no
- group: start
  title: ''
  type: Login
  url: https://app.findable.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.findable.ai/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.findable.ai/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.findable.ai/en/security
- group: agent
  title: ''
  type: MCPServer
  url: mcp/findable-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/findable-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/findable-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/findable-packages.yml
- group: design
  title: ''
  type: Components
  url: components/findable-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/findable-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/findable-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/findable-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/findable-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/findable-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/findable-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.findable.ai/en/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/findable-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/findable-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/findable-llms.txt
created: '2026-07-17'
description: Findable is an AI-powered building intelligence platform (findable.ai, formerly findable.no) that makes construction and property documentation searchable, structured, and audit-ready. It uses AI to classify building documents against standards such as BS 9991 and NS 3451, detect missing or expiring documents, support Golden Thread / Building Safety Act compliance, and answer natural-language questions across a building's documentation. Findable exposes a Partner API (api.findable.ai) for document search and AI Q&A, a hosted MCP server (mcp.findable.ai) with ~28 tools, and official TypeScript SDK and React component libraries. Used by 150+ property organizations across Norway and the UK.
image: https://www.findable.ai/images/logos/findable-logo-dark.png
layout: provider
mcp_servers:
- description: ''
  name: findable-mcp.yml
  slug: findable-mcpyml
modified: '2026-07-19'
name: Findable
nav: Providers
network: true
overview: 'Findable publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Building Intelligence, Property Technology, PropTech, and Facilities Management.


  Findable''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 20 more developer resources.'
random_paper: 31
score:
  band: thin
  composite: 36.6
  delta: -0.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 73.9
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 36.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/findable/refs/heads/main/screenshots/findable-2026-07-25T214513.png
security:
- kind: authentication
  name: Findable Authentication
  slug: findable-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Findable Domain Security
  slug: findable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Findable Trust Center
  slug: findable-trust-center
  summary_line: ISO/IEC 27001:2022, SOC 2 Type I
slug: findable
tags:
- Company
- Building Intelligence
- Property Technology
- PropTech
- Facilities Management
- Building Documentation
- Compliance
- Artificial Intelligence
- Document Search
- Construction
website: https://www.findable.ai
---
