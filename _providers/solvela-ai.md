---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-11-06'
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
  description: The Health API from Solvela — 1 operation(s) for health.
  name: Solvela Health API
  slug: solvela-ai-health-api
- baseURL: https://api.solvela.ai
  baseurl_source: declared
  description: The Models API from Solvela — 1 operation(s) for models.
  name: Solvela Models API
  slug: solvela-ai-models-api
- baseURL: https://api.solvela.ai
  baseurl_source: declared
  description: The Receipts API from Solvela — 1 operation(s) for receipts.
  name: Solvela Receipts API
  slug: solvela-ai-receipts-api
- baseURL: https://api.solvela.ai
  baseurl_source: declared
  description: The Chat Completions API from Solvela — 1 operation(s) for chat completions.
  name: Solvela Chat Completions API
  slug: solvela-ai-chat-completions-api
artifact_total: 17
common:
- group: other
  href: https://artifacts.apis.io/solvela-ai/capabilities/solvela-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/solvela-ai-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/solvela-ai/overlays/solvela-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/solvela-ai-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://www.npmjs.com/package/@solvela/mcp-server
- group: auth
  href: https://artifacts.apis.io/solvela-ai/authentication/solvela-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/solvela-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/solvela-ai/security/solvela-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/solvela-ai-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/solvela-ai/agentic-access/solvela-ai-agentic-access.yml
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
  href: https://artifacts.apis.io/solvela-ai/a2a/solvela-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/solvela-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/solvela-ai/well-known/solvela-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/solvela-ai-well-known.yml
- group: agent
  href: https://artifacts.apis.io/solvela-ai/mcp/solvela-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/solvela-ai-mcp.yml
- group: build
  href: https://artifacts.apis.io/solvela-ai/mcp/solvela-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/solvela-ai-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/solvela-ai/packages/solvela-ai-packages.yml
  title: ''
  type: Packages
  url: packages/solvela-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/solvela-ai/packages/solvela-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/solvela-ai-packages.yml
- group: agent
  href: https://artifacts.apis.io/solvela-ai/llms/solvela-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/solvela-ai-llms.txt
- group: design
  href: https://artifacts.apis.io/solvela-ai/conformance/solvela-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/solvela-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/solvela-ai/errors/solvela-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/solvela-ai-problem-types.yml
- group: build
  href: https://artifacts.apis.io/solvela-ai/errors/solvela-ai-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/solvela-ai-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/solvela-ai/lifecycle/solvela-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/solvela-ai-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/solvela-ai/security/solvela-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/solvela-ai-vulnerability-disclosure.yml
- group: start
  href: https://artifacts.apis.io/solvela-ai/sandbox/solvela-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/solvela-ai-sandbox.yml
- group: design
  href: https://artifacts.apis.io/solvela-ai/conventions/solvela-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/solvela-ai-conventions.yml
- group: operate
  href: https://artifacts.apis.io/solvela-ai/changelog/solvela-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/solvela-ai-changelog.yml
- group: build
  href: https://artifacts.apis.io/solvela-ai/cli/solvela-ai-cli.yml
  title: ''
  type: CLI
  url: cli/solvela-ai-cli.yml
- group: design
  href: https://artifacts.apis.io/solvela-ai/data-model/solvela-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/solvela-ai-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/solvela-ai/plans/solvela-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/solvela-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/solvela-ai/rate-limits/solvela-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/solvela-ai-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/solvela-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/solvela-ai/solvela/blob/main/SECURITY.md
created: '2026-09-19'
description: 'Solvela is a Solana-native payment gateway for AI agents: an OpenAI-compatible LLM proxy at api.solvela.ai where every paid request is settled per call in USDC-SPL over the x402 protocol (HTTP 402 challenge, signed payment, retry) with no API key and no account, plus a trustless on-chain escrow scheme, a spend-down voucher channel, a 15-dimension smart router across 44 models from six upstream providers (OpenAI, Anthropic, Google, xAI, DeepSeek, NVIDIA NIM), an A2A 0.3.0 agent card, a stdio MCP server and SDKs in TypeScript, Python, Go and Rust. The gateway is open source (BUSL-1.1 gateway, Apache-2.0 libraries) at github.com/solvela-ai/solvela.'
finops:
- has_sources: true
  method: derived
  name: Solvela Ai Finops
  primary_unit: million input tokens
  service_category: ''
  slug: solvela-ai-finops
  template: false
image: https://avatars.githubusercontent.com/u/230226533?v=4
layout: provider
mcp_servers:
- description: ''
  name: Solvela MCP Server
  slug: mcp-server
- description: 'Solvela ships ONE official MCP server, and it is a local stdio package, not a hosted endpoint: @solvela/mcp-server on npm (0.1.1, published 2026-07-08, Apache-2.0, bin solvela-mcp), source at sdks/mcp'
  name: Solvela MCP Server
  slug: solvela-ai-mcp-yml
modified: '2026-09-19'
name: Solvela
nav: Providers
network: true
overview: 'Solvela publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health API, Models API, Receipts API, and 1 more. Tagged areas include Company, Payments, Artificial Intelligence, LLM Gateway, and x402.


  The Solvela catalog on APIs.io includes 1 Spectral governance ruleset.


  Solvela''s developer surface includes authentication, documentation, getting-started guide, pricing, changelog, support, sandbox, and 29 more developer resources.'
plans:
- name: Solvela Ai Plans Pricing
  plan_count: 8
  slug: solvela-ai-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 8
  name: Solvela Ai Rate Limits
  slug: solvela-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Solvela API Rules
  rule_count: 62
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 1
  slug: solvela-ai-rules
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 44.7
    contract_governance: 31.8
    contract_quality: 55.4
    developer_ergonomics: 51.8
    discoverability: 65.0
    operational_transparency: 47.4
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 19.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/solvela-ai/solvela-ai-2026-10-11T130108.png
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
skill_count: 3
skills:
- name: solvela-ai-escrow-paid-request
  slug: solvela-ai-escrow-paid-request
- name: solvela-ai-free-tier-and-a2a
  slug: solvela-ai-free-tier-and-a2a
- name: solvela-ai-pay-per-call-chat
  slug: solvela-ai-pay-per-call-chat
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
