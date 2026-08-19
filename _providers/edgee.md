---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.9
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: 'OpenAI-compatible AI Gateway API. One API for any model and any provider: chat completions, Anthropic-format messages, OpenAI Responses, a live model catalog, token counting, and a standalone token-co'
  name: Edgee AI Gateway API
  slug: edgee-ai-gateway
- description: 'Management API for an Edgee organization: export AI Gateway usage and cost data as CSV or JSON, create/list/update/delete AI Gateway API keys, and configure custom BYOK provider keys. Bearer-token aut'
  name: Edgee Console API
  slug: edgee-console
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edgee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.edgee.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.edgee.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.edgee.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.edgee.ai/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.edgee.ai/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.edgee.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edgee-ai
- group: operate
  title: ''
  type: Support
  url: https://www.edgee.ai/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.edgee.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.edgee.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.edgee.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.edgee.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.edgee.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.edgee.ai/changelog
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.edgee.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.edgee.ai/
- group: build
  title: ''
  type: Packages
  url: packages/edgee-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/edgee-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/edgee-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/edgee-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/edgee-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/edgee-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/edgee-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/edgee-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/edgee-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/edgee-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/edgee-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/edgee-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/edgee-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/edgee-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/edgee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/edgee-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-17'
description: Edgee is a French edge-native AI Gateway that sits between coding agents and LLM providers, intercepting, routing, compressing, metering and securing every request. Its OpenAI-compatible gateway API at edgee.io exposes chat completions, an Anthropic Messages endpoint, an OpenAI Responses endpoint, a model catalog of 230+ models across providers, token counting and a standalone compression endpoint, while a separate Console API at api.edgee.app handles organization management, gateway key management, BYOK provider keys and usage/cost export. A Rust CLI launches Claude Code, Codex, OpenCode, Cursor and VS Code Copilot through the gateway, and official TypeScript, Python, Go and Rust SDKs wrap the same surface. Edgee previously operated as an edge component runtime and data-collection platform at edgee.cloud; that documentation now redirects to the AI Gateway product at edgee.ai.
image: https://www.edgee.ai/assets/img/og/og.jpg
layout: provider
mcp_servers:
- description: ''
  name: edgee-mcp.yml
  slug: edgee-mcpyml
modified: '2026-08-17'
name: Edgee
nav: Providers
network: true
overview: 'Edgee publishes 1 API on the [APIs.io](https://apis.io/) network: AI Gateway API. Tagged areas include Company, AI, LLM, AI Gateway, and Agents.


  Edgee''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Edgee Plans Pricing
  plan_count: 3
  slug: edgee-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 0
  name: Edgee Rate Limits
  slug: edgee-rate-limits
score:
  band: strong
  composite: 59.8
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 16.7
    contract_quality: 59.0
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 18.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: authentication
  name: Edgee Authentication
  slug: edgee-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Edgee Domain Security
  slug: edgee-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Edgee Trust Center
  slug: edgee-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2
slug: edgee
tags:
- Company
- AI
- LLM
- AI Gateway
- Agents
- Developer Tools
- Observability
- FinOps
- Edge Computing
- Cost Management
website: https://www.edgee.ai/
---
