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
  score: 27.9
  scored_at: '2026-07-28'
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
- description: ''
  name: waniwani-mcp.yml
  slug: waniwani-mcpyml
modified: '2026-07-21'
name: Waniwani
nav: Providers
network: true
overview: 'Waniwani publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Model Context Protocol, AI Distribution, and Conversational AI.


  Waniwani''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, pricing, support, and 26 more developer resources.'
random_paper: 15
scopes:
- name: Waniwani Scopes
  scope_count: 25
  slug: waniwani-scopes
  summary_line: 25 scopes
score:
  band: developing
  composite: 50.2
  delta: -2.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 87.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 39.5
  previous_composite: 52.3
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
- Model Context Protocol
- AI Distribution
- Conversational AI
- Lead Generation
- Insurance
- Fintech
- Agents
- SDK
website: https://www.waniwani.ai
---
