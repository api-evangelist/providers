---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.9
  scored_at: '2026-09-20'
api_count: 3
apis:
- baseURL: https://api.trustboost.dev
  baseurl_source: declared
  description: 'REST contract for the sanitizer: POST /sanitize (redact PII from up to 10,000 characters with an optional context mode, gated by tx_hash=TRIAL, an x402 payment header or a Solana bundle tx_hash), POST'
  name: TrustBoost PII Sanitizer API
  slug: trustboost-pii-sanitizer-api
- description: 'Remote Model Context Protocol server at https://api.trustboost.dev/mcp (HTTP JSON-RPC 2.0, protocol version 2024-11-05, serverInfo trustboost 2.6.0). initialize and tools/list answer anonymously with '
  name: TrustBoost MCP Server
  slug: trustboost-mcp-server
- description: 'Agent2Agent surface: an agent card served from https://api.trustboost.dev/.well-known/agent-card.json (version 2.6.0, no protocolVersion, capabilities object of product flags, three skills — sanitize_'
  name: TrustBoost A2A Agent
  slug: trustboost-a2a-agent
artifact_total: 9
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trustboost-dev/refs/heads/main/security/trustboost-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trustboost-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.trustboost.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/teodorofodocrispin-cmyk/TrustBoost-PII-Sanitizer
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/teodorofodocrispin-cmyk/TrustBoost-PII-Sanitizer/blob/main/AGENTS.md
- group: docs
  title: ''
  type: APIReference
  url: https://api.trustboost.dev/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://api.trustboost.dev/pricing.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://github.com/teodorofodocrispin-cmyk/TrustBoost-PII-Sanitizer/blob/main/PRIVACY.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/teodorofodocrispin-cmyk/TrustBoost-PII-Sanitizer/blob/main/PRIVACY.md
- group: operate
  title: ''
  type: Support
  url: https://github.com/teodorofodocrispin-cmyk/TrustBoost-PII-Sanitizer/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teodorofodocrispin-cmyk
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/trustboost-dev/refs/heads/main/a2a/trustboost-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/trustboost-dev-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trustboost-dev/refs/heads/main/mcp/trustboost-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/trustboost-dev-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trustboost-dev/refs/heads/main/well-known/trustboost-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trustboost-dev-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trustboost-dev/refs/heads/main/llms/trustboost-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trustboost-dev-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trustboost-dev/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trustboost-dev/refs/heads/main/conventions/trustboost-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/trustboost-dev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trustboost-dev/refs/heads/main/errors/trustboost-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trustboost-dev-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trustboost-dev/refs/heads/main/data-model/trustboost-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trustboost-dev-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/trustboost-dev/refs/heads/main/rate-limits/trustboost-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/trustboost-dev-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/trustboost-dev/refs/heads/main/plans/trustboost-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trustboost-dev-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/trustboost-dev/refs/heads/main/sandbox/trustboost-dev-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/trustboost-dev-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trustboost-dev/refs/heads/main/conformance/trustboost-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trustboost-dev-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trustboost-dev/refs/heads/main/lifecycle/trustboost-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/trustboost-dev-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/trustboost-dev/refs/heads/main/packages/trustboost-dev-packages.yml
  title: ''
  type: Packages
  url: packages/trustboost-dev-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trustboost-dev/refs/heads/main/authentication/trustboost-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trustboost-dev-authentication.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://github.com/teodorofodocrispin-cmyk/TrustBoost-PII-Sanitizer/blob/main/PRIVACY.md
- group: other
  title: ''
  type: Subprocessors
  url: https://github.com/teodorofodocrispin-cmyk/TrustBoost-PII-Sanitizer/blob/main/PRIVACY.md
- group: other
  title: ''
  type: DataResidency
  url: https://github.com/teodorofodocrispin-cmyk/TrustBoost-PII-Sanitizer/blob/main/PRIVACY.md
- group: other
  title: ''
  type: AITransparency
  url: https://github.com/teodorofodocrispin-cmyk/TrustBoost-PII-Sanitizer/blob/main/PRIVACY.md
created: '2026-09-19'
description: 'TrustBoost PII Sanitizer is a pay-per-call "privacy firewall" for autonomous AI agent pipelines, built and operated by an individual developer (Teodoro Crispin, GitHub teodorofodocrispin-cmyk) and served entirely from https://api.trustboost.dev — the apex trustboost.dev has no DNS record. An agent POSTs text to /sanitize and gets it back with emails, phone numbers, national IDs (RFC, CUIT, CPF, CNPJ, Personalausweis, マイナンバー, NIR, Codice Fiscale, RRN and more across 8 languages), API keys and financial data replaced by [REDACTED], plus a safety_score, a risk_category and an entity list; five context modes (general, legal, financial, medical, code) tune the redaction. There is no account and no API key: 50 free calls per wallet with tx_hash=TRIAL, a free 3-per-hour preview, then x402 payment in USDC on Base or Solana ($0.01 per call or a 149 USDC prepaid bundle of 10,000), with every paid sanitization anchored on Solana as a verifiable "Proof of Sanitization". The same service
  is exposed three ways from one host: a 9-operation OpenAPI 3.0.0 REST contract, a remote MCP server at /mcp (one tool, sanitize_pii), and an A2A-flavored agent card at /.well-known/agent-card.json with three skills. The provider''s own privacy policy describes it as a learning prototype that sends raw text to OpenAI GPT-4o-mini for detection and has no certified security audit.'
image: https://raw.githubusercontent.com/teodorofodocrispin-cmyk/TrustBoost-PII-Sanitizer/main/logo.png
layout: provider
mcp_servers:
- description: ''
  name: TrustBoost PII Sanitizer MCP Server
  slug: trustboost-pii-sanitizer-mcp-server
- description: ''
  name: TrustBoost MCP endpoint (HTTP JSON-RPC)
  slug: trustboost-mcp-endpoint-http-json-rpc
modified: '2026-09-19'
name: TrustBoost PII Sanitizer
nav: Providers
network: true
overview: 'TrustBoost PII Sanitizer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Privacy, PII Redaction, Data Protection, LLM Security, and AI Safety.


  TrustBoost PII Sanitizer''s developer surface includes documentation, getting-started guide, API reference, pricing, support, sandbox, authentication, and 22 more developer resources.'
plans:
- name: Trustboost Dev Plans Pricing
  plan_count: 4
  slug: trustboost-dev-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Trustboost Dev Rate Limits
  slug: trustboost-dev-rate-limits
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 41.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 35.0
    developer_ergonomics: 59.5
    discoverability: 81.5
    operational_transparency: 23.7
  previous_composite: 5.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Trustboost Dev Authentication
  slug: trustboost-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Trustboost Dev Domain Security
  slug: trustboost-dev-domain-security
  summary_line: TLSv1.3
slug: trustboost-dev
tags:
- Privacy
- PII Redaction
- Data Protection
- LLM Security
- AI Safety
- Agents
- A2A
- MCP
- x402
- Agentic Commerce
- Solana
- Compliance
- agent-native
website: https://api.trustboost.dev/
---
