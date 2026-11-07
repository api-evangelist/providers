---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Avalix Ai Agentic Access
  operation_count: 33
  slug: avalix-ai-agentic-access
  summary_line: 33 operations · 24 acting
api_count: 1
apis:
- description: 'Remote Model Context Protocol server at https://avalix.ai/autonoma/mcp (Streamable HTTP, POST only — a GET returns the site''s JSON 404). initialize answers anonymously with protocolVersion 2025-11-25 '
  name: Autonoma MCP Server
  slug: autonoma-mcp-server
- description: 'Agent2Agent (A2A) protocol surface: an agent card served from https://avalix.ai/.well-known/agent-card.json (and mirrored at /.well-known/agent.json''s sibling path on www and under /autonoma/), protoc'
  name: Autonoma A2A Agent
  slug: autonoma-a2a-agent
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Agent Audit API from Avalix — 1 operation(s) for agent audit.
  name: Avalix Agent Audit API
  slug: avalix-ai-agent-audit-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Agent Card Lint API from Avalix — 1 operation(s) for agent card lint.
  name: Avalix Agent Card Lint API
  slug: avalix-ai-agent-card-lint-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Agent Contract API from Avalix — 1 operation(s) for agent contract.
  name: Avalix Agent Contract API
  slug: avalix-ai-agent-contract-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Agent Risk Scan API from Avalix — 1 operation(s) for agent risk scan.
  name: Avalix Agent Risk Scan API
  slug: avalix-ai-agent-risk-scan-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Agent Security Test API from Avalix — 1 operation(s) for agent security test.
  name: Avalix Agent Security Test API
  slug: avalix-ai-agent-security-test-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Data Distill API from Avalix — 1 operation(s) for data distill.
  name: Avalix Data Distill API
  slug: avalix-ai-data-distill-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Demo API from Avalix — 1 operation(s) for demo.
  name: Avalix Demo API
  slug: avalix-ai-demo-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Health API from Avalix — 1 operation(s) for health.
  name: Avalix Health API
  slug: avalix-ai-health-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Integration Warranty 7d API from Avalix — 1 operation(s) for integration warranty 7d.
  name: Avalix Integration Warranty 7d API
  slug: avalix-ai-integration-warranty-7d-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Jobs API from Avalix — 1 operation(s) for jobs.
  name: Avalix Jobs API
  slug: avalix-ai-jobs-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Mcp Compatibility API from Avalix — 1 operation(s) for mcp compatibility.
  name: Avalix Mcp Compatibility API
  slug: avalix-ai-mcp-compatibility-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Monitor API from Avalix — 1 operation(s) for monitor.
  name: Avalix Monitor API
  slug: avalix-ai-monitor-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Offers API from Avalix — 1 operation(s) for offers.
  name: Avalix Offers API
  slug: avalix-ai-offers-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Openapi Repair API from Avalix — 1 operation(s) for openapi repair.
  name: Avalix Openapi Repair API
  slug: avalix-ai-openapi-repair-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Projects API from Avalix — 2 operation(s) for projects.
  name: Avalix Projects API
  slug: avalix-ai-projects-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Ready API from Avalix — 1 operation(s) for ready.
  name: Avalix Ready API
  slug: avalix-ai-ready-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Receipt Verifier API from Avalix — 1 operation(s) for receipt verifier.
  name: Avalix Receipt Verifier API
  slug: avalix-ai-receipt-verifier-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Research Brief API from Avalix — 1 operation(s) for research brief.
  name: Avalix Research Brief API
  slug: avalix-ai-research-brief-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Tasks API from Avalix — 7 operation(s) for tasks.
  name: Avalix Tasks API
  slug: avalix-ai-tasks-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Trust API from Avalix — 3 operation(s) for trust.
  name: Avalix Trust API
  slug: avalix-ai-trust-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Trust Preflight API from Avalix — 1 operation(s) for trust preflight.
  name: Avalix Trust Preflight API
  slug: avalix-ai-trust-preflight-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The Warranties API from Avalix — 1 operation(s) for warranties.
  name: Avalix Warranties API
  slug: avalix-ai-warranties-api
- baseURL: https://avalix.ai/autonoma
  baseurl_source: declared
  description: The X402 API from Avalix — 2 operation(s) for x402.
  name: Avalix X402 API
  slug: avalix-ai-x402-api
artifact_total: 37
common:
- group: other
  href: https://artifacts.apis.io/avalix-ai/capabilities/avalix-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/avalix-ai-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/avalix-ai/overlays/avalix-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avalix-ai-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/avalix-ai/agentic-access/avalix-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/avalix-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/avalix-ai/security/avalix-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avalix-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/avalix-ai/security/avalix-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avalix-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/avalix-ai/authentication/avalix-ai-authentication.yml
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
  href: https://artifacts.apis.io/avalix-ai/llms/avalix-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avalix-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/avalix-ai/a2a/avalix-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/avalix-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/avalix-ai/mcp/avalix-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/avalix-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/avalix-ai/well-known/avalix-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avalix-ai-well-known.yml
- group: auth
  href: https://artifacts.apis.io/avalix-ai/well-known/avalix-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avalix-ai-security.txt
- group: commercial
  href: https://artifacts.apis.io/avalix-ai/plans/avalix-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avalix-ai-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/avalix-ai/sandbox/avalix-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/avalix-ai-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://avalix.ai/.well-known/security.txt
- group: design
  href: https://artifacts.apis.io/avalix-ai/conventions/avalix-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/avalix-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/avalix-ai/errors/avalix-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/avalix-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/avalix-ai/data-model/avalix-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/avalix-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/avalix-ai/rate-limits/avalix-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/avalix-ai-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/avalix-ai/conformance/avalix-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avalix-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/avalix-ai/lifecycle/avalix-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/avalix-ai-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/avalix-ai/skills/_index.yml
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
finops:
- has_sources: true
  method: derived
  name: Avalix Ai Finops
  primary_unit: ''
  service_category: ''
  slug: avalix-ai-finops
  template: true
image: https://avalix.ai/brand/og-image.png
layout: provider
mcp_servers:
- description: Avalix operates ONE remote MCP server at https://avalix.ai/autonoma/mcp — the same origin as its website, the Autonoma OpenAPI and the A2A JSON-RPC endpoint. It is POST-only Streamable HTTP (a GET ret
  name: Avalix MCP Server
  slug: avalix-ai-mcp-yml
modified: '2026-09-19'
name: Avalix
nav: Providers
network: true
overview: 'Avalix publishes 25 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Audit API, Agent Card Lint API, Agent Contract API, and 22 more. Tagged areas include Agents, Agentic Commerce, A2A, MCP, and x402.


  The Avalix catalog on APIs.io includes 1 Spectral governance ruleset.


  Avalix''s developer surface includes authentication, documentation, API reference, pricing, support, FAQ, sandbox, and 26 more developer resources.'
plans:
- name: Avalix Ai Plans Pricing
  plan_count: 22
  slug: avalix-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Avalix Ai Rate Limits
  slug: avalix-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Avalix API Rules
  rule_count: 46
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 4
  slug: avalix-ai-rules
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 53.9
    contract_governance: 31.8
    contract_quality: 48.2
    developer_ergonomics: 31.5
    discoverability: 75.0
    operational_transparency: 5.3
  previous_composite: 50.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 23
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/avalix-ai/avalix-ai-2026-10-11T101037.png
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
skill_count: 3
skills:
- name: avalix-ai-free-check-then-paid-lint
  slug: avalix-ai-free-check-then-paid-lint
- name: avalix-ai-integration-warranty
  slug: avalix-ai-integration-warranty
- name: avalix-ai-quote-and-commission-task
  slug: avalix-ai-quote-and-commission-task
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
