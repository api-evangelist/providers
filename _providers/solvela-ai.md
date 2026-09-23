---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.7
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Solvela Ai Agentic Access
  operation_count: 4
  slug: solvela-ai-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.solvela.ai
  baseurl_source: declared
  description: 'OpenAI-compatible chat completions paid per request in USDC-SPL on Solana via x402: POST /v1/chat/completions without a PAYMENT-SIGNATURE header returns an HTTP 402 challenge quoting the USDC cost; si'
  name: Solvela Gateway API
  slug: solvela-gateway-api
artifact_total: 9
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/authentication/solvela-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/solvela-ai-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/security/solvela-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/solvela-ai-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/agentic-access/solvela-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/solvela-ai-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://solvela.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/solvela-ai/solvela/tree/main/dashboard/content/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/solvela-ai/solvela#quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/solvela-ai
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/solvela-ai/solvela
- group: commercial
  title: ''
  type: Pricing
  url: https://api.solvela.ai/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/solvela-ai/solvela/blob/main/CHANGELOG.md
- group: operate
  title: ''
  type: Support
  url: https://github.com/solvela-ai/solvela/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/solvela-ai/solvela/blob/main/LICENSE
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/a2a/solvela-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/solvela-ai-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/well-known/solvela-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/solvela-ai-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/mcp/solvela-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/solvela-ai-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/mcp/solvela-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/solvela-ai-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/packages/solvela-ai-packages.yml
  title: ''
  type: Packages
  url: packages/solvela-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/packages/solvela-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/solvela-ai-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/llms/solvela-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/solvela-ai-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/conformance/solvela-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/solvela-ai-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/errors/solvela-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/solvela-ai-problem-types.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/errors/solvela-ai-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/solvela-ai-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/lifecycle/solvela-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/solvela-ai-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/security/solvela-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/solvela-ai-vulnerability-disclosure.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/sandbox/solvela-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/solvela-ai-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/conventions/solvela-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/solvela-ai-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/changelog/solvela-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/solvela-ai-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/cli/solvela-ai-cli.yml
  title: ''
  type: CLI
  url: cli/solvela-ai-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/data-model/solvela-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/solvela-ai-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/plans/solvela-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/solvela-ai-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/rate-limits/solvela-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/solvela-ai-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/solvela-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/solvela-ai/solvela/blob/main/SECURITY.md
created: '2026-09-19'
description: 'Solvela is a Solana-native payment gateway for AI agents: an OpenAI-compatible LLM proxy at api.solvela.ai where every paid request is settled per call in USDC-SPL over the x402 protocol (HTTP 402 challenge, signed payment, retry) with no API key and no account, plus a trustless on-chain escrow scheme, a spend-down voucher channel, a 15-dimension smart router across 44 models from six upstream providers (OpenAI, Anthropic, Google, xAI, DeepSeek, NVIDIA NIM), an A2A 0.3.0 agent card, a stdio MCP server and SDKs in TypeScript, Python, Go and Rust. The gateway is open source (BUSL-1.1 gateway, Apache-2.0 libraries) at github.com/solvela-ai/solvela.'
image: https://avatars.githubusercontent.com/u/230226533?v=4
layout: provider
mcp_servers:
- description: ''
  name: Solvela MCP Server
  slug: solvela-mcp-server
- description: ''
  name: MCP server (npm, stdio)
  slug: mcp-server-npm-stdio
modified: '2026-09-19'
name: Solvela
nav: Providers
network: true
overview: 'Solvela publishes 1 API on the [APIs.io](https://apis.io/) network: Gateway API. Tagged areas include Company, Payments, Artificial Intelligence, LLM Gateway, and x402.


  Solvela''s developer surface includes authentication, documentation, getting-started guide, pricing, changelog, support, sandbox, and 26 more developer resources.'
plans:
- name: Solvela Ai Plans Pricing
  plan_count: 27
  slug: solvela-ai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 8
  name: Solvela Ai Rate Limits
  slug: solvela-ai-rate-limits
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 57.1
    developer_ergonomics: 68.5
    discoverability: 68.5
    operational_transparency: 63.2
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.9
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Solvela Ai Authentication
  slug: solvela-ai-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Solvela Ai Domain Security
  slug: solvela-ai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Solvela Ai Vulnerability Disclosure
  slug: solvela-ai-vulnerability-disclosure
  summary_line: Hackerone
slug: solvela-ai
tags:
- Company
- Payments
- Artificial Intelligence
- LLM Gateway
- x402
- Solana
- Stablecoins
- AI Agents
- MCP
- A2A
- Agentic Commerce
website: https://solvela.ai/
---
