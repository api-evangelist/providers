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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The WaniWani AI-distribution platform and its hosted MCP server — build MCP funnels with the open-source SDK/CLI, operate environments, API keys, analytics and sessions via the OAuth 2.1 MCP server.
  name: WaniWani Platform
  slug: waniwani-platform
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.waniwani.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.waniwani.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.waniwani.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.waniwani.ai/sdk/reference/entry-points
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.waniwani.ai/sdk/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.waniwani.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WaniWani-AI
- group: start
  title: ''
  type: SignUp
  url: https://app.waniwani.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://app.waniwani.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.waniwani.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.waniwani.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://github.com/WaniWani-AI/sdk/issues
- group: build
  title: ''
  type: Packages
  url: packages/waniwani-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/waniwani-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/waniwani-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/waniwani-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/waniwani-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/waniwani-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/waniwani-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/waniwani-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/waniwani-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://compliance.waniwani.ai/overview
- group: auth
  title: ''
  type: TrustCenter
  url: https://compliance.waniwani.ai/overview
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/waniwani-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/WaniWani-AI/sdk/blob/main/SECURITY.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/waniwani-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/waniwani-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/waniwani-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/waniwani-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/waniwani-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/waniwani-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/waniwani-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/waniwani-sdk-skill.md
created: '2026-07-17'
description: 'Waniwani is an AI distribution platform: it helps companies build, deploy, and optimize AI apps — lightweight services built on the Model Context Protocol (MCP) that represent a product inside AI conversations on ChatGPT, Claude, Gemini, and Perplexity. The platform spans an AI app builder, synthetic-buyer monitoring, full-funnel analytics, and continuous compliance monitoring (GDPR, EU AI Act, DORA, SOC 2). Its open-source TypeScript SDK (@waniwani/sdk) and CLI (@waniwani/cli) let any quote-based vendor — insurance, mortgage, software, home services — build multi-step conversational funnels (lead generation, booking, quotes) that compile to a single MCP tool, backed by a hosted MCP server for operating the platform from an AI client. Backed by an $8M seed round led by Seedcamp.'
image: https://compliance.waniwani.ai/brand/logo
layout: provider
mcp_servers:
- description: WaniWani's own hosted MCP server for operating the WaniWani platform conversationally from Claude, Cursor, or ChatGPT (manage environments, API keys, analytics digests, session breakdowns). This is di
  name: Waniwani MCP Server
  slug: waniwani-mcp-server
modified: '2026-07-21'
name: Waniwani
nav: Providers
network: true
overview: 'Waniwani publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, MCP, AI Distribution, and Conversational AI.


  Waniwani''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, pricing, support, and 26 more developer resources.'
random_paper: 1
scopes:
- name: Waniwani Scopes
  scope_count: 25
  slug: waniwani-scopes
  summary_line: 25 scopes
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 47.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 80.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/waniwani/refs/heads/main/screenshots/waniwani-2026-08-17T082836.png
security:
- kind: authentication
  name: Waniwani Authentication
  slug: waniwani-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Waniwani Domain Security
  slug: waniwani-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Waniwani Vulnerability Disclosure
  slug: waniwani-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Waniwani Trust Center
  slug: waniwani-trust-center
  summary_line: SOC 2 Type II, GDPR, EU AI Act, DORA
slug: waniwani
tags:
- Company
- Artificial Intelligence
- MCP
- AI Distribution
- Conversational AI
- Lead Generation
- Insurance
- Fintech
- Agents
- SDK
website: https://www.waniwani.ai
---
