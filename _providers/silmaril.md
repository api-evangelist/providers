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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 22.2
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: AI application firewall classify API. A Firewall client sends each sanitized classification input (user input, tool response, model output, or system prompt) with a hook label and optional tool name t
  name: Silmaril Firewall API
  slug: silmaril-firewall-api
artifact_total: 5
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://silmaril.dev/docs
- group: docs
  title: ''
  type: Documentation
  url: https://silmaril.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://silmaril.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://silmaril.dev/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Silmaril-Security
- group: operate
  title: ''
  type: Support
  url: https://cal.com/silmaril/30min
- group: operate
  title: ''
  type: StatusPage
  url: https://silmaril.dev/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://silmaril.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://silmaril.dev/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/silmaril-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/silmaril-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/silmaril-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/silmaril-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/silmaril-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/silmaril-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/silmaril-error-codes.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/silmaril-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/silmaril-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/silmaril-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/silmaril-data-model.yml
- group: auth
  title: ''
  type: Security
  url: security/silmaril-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/silmaril-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silmaril-domain-security.yml
created: '2026-07-17'
description: Silmaril is a Y Combinator-backed runtime security company that builds an AI application firewall for agentic systems. The Silmaril Firewall classifies prompts, retrieved context, tool calls, tool responses, model output, and accumulated execution state before harmful outcomes materialize, returning a benign/malicious prediction plus a primary-outcome classification across secret exposure, information disclosure, control abuse, system compromise, and service disruption. It ships first-party TypeScript, Python, Go, and Java SDKs, LiteLLM and Vercel AI gateway guardrails, LangChain/LangGraph handlers, and agent plugins for Codex, Claude Code, OpenClaw, and Hermes, plus a hosted read-only MCP evidence server. Offered as managed and customer-controlled self-hosted container deployments.
image: https://www.silmaril.dev/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: silmaril-mcp.yml
  slug: silmaril-mcpyml
modified: '2026-07-21'
name: Silmaril
nav: Providers
network: true
overview: 'Silmaril publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Security, AI Firewall, Prompt Injection, and Agent Security.


  Silmaril''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, and 17 more developer resources.'
random_paper: 116
score:
  band: thin
  composite: 32.2
  delta: -0.3
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 32.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Silmaril Authentication
  slug: silmaril-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Silmaril Domain Security
  slug: silmaril-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Silmaril Vulnerability Disclosure
  slug: silmaril-vulnerability-disclosure
  summary_line: contact published
slug: silmaril
tags:
- Company
- AI Security
- AI Firewall
- Prompt Injection
- Agent Security
- Runtime Security
- Guardrails
- MCP
- LLM Security
- Developer Tools
website: https://silmaril.dev/docs
---
