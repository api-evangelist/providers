---
agent_readiness:
  band: agent-ready
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.6
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Avalix Ai Agentic Access
  operation_count: 33
  slug: avalix-ai-agentic-access
  summary_line: 33 operations · 24 acting
api_count: 3
apis:
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: 'Agent-consumable REST API for Autonoma, Avalix''s disclosed autonomous AI operator. 33 paths under https://avalix.ai/autonoma: free deterministic previews (POST /v1/demo, POST /v1/trust/preview), a pub'
  name: Autonoma Trust Gate API
  slug: autonoma-trust-gate-api
- description: 'Remote Model Context Protocol server at https://avalix.ai/autonoma/mcp (Streamable HTTP, POST only — a GET returns the site''s JSON 404). initialize answers anonymously with protocolVersion 2025-11-25 '
  name: Autonoma MCP Server
  slug: autonoma-mcp-server
- description: 'Agent2Agent (A2A) protocol surface: an agent card served from https://avalix.ai/.well-known/agent-card.json (and mirrored at /.well-known/agent.json''s sibling path on www and under /autonoma/), protoc'
  name: Autonoma A2A Agent
  slug: autonoma-a2a-agent
artifact_total: 11
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/agentic-access/avalix-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/avalix-ai-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/security/avalix-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avalix-ai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/security/avalix-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avalix-ai-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/authentication/avalix-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/avalix-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://avalix.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://avalix.ai/autonoma/agents
- group: docs
  title: ''
  type: APIReference
  url: https://avalix.ai/autonoma/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://avalix.ai/autonoma/services
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avalix.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avalix.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://avalix.ai/contact
- group: start
  title: ''
  type: Login
  url: https://avalix.ai/login
- group: operate
  title: ''
  type: FAQ
  url: https://avalix.ai/faq
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/llms/avalix-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avalix-ai-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/a2a/avalix-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/avalix-ai-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/mcp/avalix-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/avalix-ai-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/well-known/avalix-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avalix-ai-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/well-known/avalix-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avalix-ai-security.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/plans/avalix-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avalix-ai-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/sandbox/avalix-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/avalix-ai-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://avalix.ai/.well-known/security.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/conventions/avalix-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/avalix-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/errors/avalix-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/avalix-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/data-model/avalix-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/avalix-ai-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/rate-limits/avalix-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/avalix-ai-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/conformance/avalix-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avalix-ai-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/lifecycle/avalix-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/avalix-ai-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avalix-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: AITransparency
  url: https://avalix.ai/autonoma/
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://avalix.ai/privacy
- group: other
  title: ''
  type: Subprocessors
  url: https://avalix.ai/privacy
created: '2026-09-19'
description: 'Avalix (avalix.ai, est. 2026) is a custom AI implementation team — "three cyber engineers and one CTO" — that audits small and mid-size businesses for time and revenue leaks and builds "AI employees" around them (lead capture across calls, SMS, email and social, one CRM timeline, booking, follow-up, payments and closeout), with quote-based enterprise engagements. Its public API surface is Autonoma, Avalix''s disclosed autonomous AI operator: a 33-path OpenAPI 3.1.0 "Autonoma Trust Gate" contract at https://avalix.ai/autonoma/openapi.json that sells deterministic agent trust checks and signed Trust Passports, A2A agent-card linting, MCP compatibility tests, OpenAPI structural repair, receipt verification, data distillation, a seven-day integration warranty and fixed-price bounded technical work — paid per call in USDC on Base through x402 (HTTP 402 + Payment-Required), with card, Ethereum USDT and Robinhood Chain ETH rails for quoted tasks; a remote MCP server at https://avalix.ai/autonoma/mcp
  that answers an anonymous initialize and tools/list with six tools; and an A2A 1.0.0 agent card at /.well-known/agent-card.json backed by a live JSON-RPC endpoint at https://avalix.ai/autonoma/a2a/v1.'
image: https://avalix.ai/brand/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Avalix MCP Server
  slug: avalix-mcp-server
- description: ''
  name: Autonoma MCP endpoint (Streamable HTTP)
  slug: autonoma-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: Avalix
nav: Providers
network: true
overview: 'Avalix publishes 1 API on the [APIs.io](https://apis.io/) network: Autonoma Trust Gate API. Tagged areas include Agents, Agentic Commerce, A2A, MCP, and x402.


  Avalix''s developer surface includes authentication, documentation, API reference, pricing, support, FAQ, sandbox, and 24 more developer resources.'
plans:
- name: Avalix Ai Plans Pricing
  plan_count: 22
  slug: avalix-ai-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Avalix Ai Rate Limits
  slug: avalix-ai-rate-limits
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 41.5
    developer_ergonomics: 42.3
    discoverability: 81.5
    operational_transparency: 10.5
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Avalix Ai Authentication
  slug: avalix-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Avalix Ai Domain Security
  slug: avalix-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Avalix Ai Vulnerability Disclosure
  slug: avalix-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: avalix-ai
tags:
- Agents
- Agentic Commerce
- A2A
- MCP
- x402
- AI Trust
- Agent Security
- Data Validation
- AI Implementation
- Custom AI
- Agent-Native
website: https://avalix.ai/
---
