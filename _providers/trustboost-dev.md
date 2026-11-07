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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: three_quarters
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Remote Model Context Protocol server at https://api.trustboost.dev/mcp (HTTP JSON-RPC 2.0, protocol version 2024-11-05, serverInfo trustboost 2.6.0). initialize and tools/list answer anonymously with '
  name: TrustBoost MCP Server
  slug: trustboost-mcp-server
- description: 'Agent2Agent surface: an agent card served from https://api.trustboost.dev/.well-known/agent-card.json (version 2.6.0, no protocolVersion, capabilities object of product flags, three skills — sanitize_'
  name: TrustBoost A2A Agent
  slug: trustboost-a2a-agent
- baseURL: https://api.trustboost.dev/mcp
  baseurl_source: declared
  description: The Budget API from TrustBoost PII Sanitizer — 1 operation(s) for budget.
  name: TrustBoost PII Sanitizer Budget API
  slug: trustboost-dev-budget-api
- baseURL: https://api.trustboost.dev/mcp
  baseurl_source: declared
  description: The Health API from TrustBoost PII Sanitizer — 1 operation(s) for health.
  name: TrustBoost PII Sanitizer Health API
  slug: trustboost-dev-health-api
- baseURL: https://api.trustboost.dev/mcp
  baseurl_source: declared
  description: The Mcp API from TrustBoost PII Sanitizer — 1 operation(s) for mcp.
  name: TrustBoost PII Sanitizer MCP API
  slug: trustboost-dev-mcp-api
- baseURL: https://api.trustboost.dev/mcp
  baseurl_source: declared
  description: The Message API from TrustBoost PII Sanitizer — 1 operation(s) for message.
  name: TrustBoost PII Sanitizer Message API
  slug: trustboost-dev-message-api
- baseURL: https://api.trustboost.dev/mcp
  baseurl_source: declared
  description: The Sanitize API from TrustBoost PII Sanitizer — 2 operation(s) for sanitize.
  name: TrustBoost PII Sanitizer Sanitize API
  slug: trustboost-dev-sanitize-api
- baseURL: https://api.trustboost.dev/mcp
  baseurl_source: declared
  description: The Score API from TrustBoost PII Sanitizer — 1 operation(s) for score.
  name: TrustBoost PII Sanitizer Score API
  slug: trustboost-dev-score-api
- baseURL: https://api.trustboost.dev/mcp
  baseurl_source: declared
  description: The Verify API from TrustBoost PII Sanitizer — 1 operation(s) for verify.
  name: TrustBoost PII Sanitizer Verify API
  slug: trustboost-dev-verify-api
artifact_total: 18
common:
- group: other
  href: https://artifacts.apis.io/trustboost-dev/capabilities/trustboost-dev-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/trustboost-dev-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/trustboost-dev/overlays/trustboost-dev-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/trustboost-dev-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/trustboost-dev/security/trustboost-dev-domain-security.yml
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
  href: https://artifacts.apis.io/trustboost-dev/a2a/trustboost-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/trustboost-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/trustboost-dev/mcp/trustboost-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/trustboost-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/trustboost-dev/well-known/trustboost-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trustboost-dev-well-known.yml
- group: agent
  href: https://artifacts.apis.io/trustboost-dev/llms/trustboost-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trustboost-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/trustboost-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/trustboost-dev/conventions/trustboost-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/trustboost-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/trustboost-dev/errors/trustboost-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trustboost-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/trustboost-dev/data-model/trustboost-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trustboost-dev-data-model.yml
- group: operate
  href: https://artifacts.apis.io/trustboost-dev/rate-limits/trustboost-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/trustboost-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/trustboost-dev/plans/trustboost-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trustboost-dev-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/trustboost-dev/sandbox/trustboost-dev-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/trustboost-dev-sandbox.yml
- group: design
  href: https://artifacts.apis.io/trustboost-dev/conformance/trustboost-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trustboost-dev-conformance.yml
- group: design
  href: https://artifacts.apis.io/trustboost-dev/lifecycle/trustboost-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/trustboost-dev-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/trustboost-dev/packages/trustboost-dev-packages.yml
  title: ''
  type: Packages
  url: packages/trustboost-dev-packages.yml
- group: auth
  href: https://artifacts.apis.io/trustboost-dev/authentication/trustboost-dev-authentication.yml
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
finops:
- has_sources: true
  method: derived
  name: Trustboost Dev Finops
  primary_unit: request
  service_category: ''
  slug: trustboost-dev-finops
  template: false
image: https://raw.githubusercontent.com/teodorofodocrispin-cmyk/TrustBoost-PII-Sanitizer/main/logo.png
layout: provider
mcp_servers:
- description: 'TrustBoost operates ONE remote MCP server at https://api.trustboost.dev/mcp, on the same host as its website, OpenAPI and agent card. It answers JSON-RPC 2.0 over plain HTTP POST: initialize returned '
  name: TrustBoost PII Sanitizer MCP Server
  slug: trustboost-dev-mcp-yml
modified: '2026-09-19'
name: TrustBoost PII Sanitizer
nav: Providers
network: true
overview: 'TrustBoost PII Sanitizer publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Budget API, Health API, MCP API, and 6 more. Tagged areas include Privacy, PII Redaction, Data Protection, LLM Security, and AI Safety.


  The TrustBoost PII Sanitizer catalog on APIs.io includes 1 Spectral governance ruleset.


  TrustBoost PII Sanitizer''s developer surface includes documentation, getting-started guide, API reference, pricing, support, sandbox, authentication, and 24 more developer resources.'
plans:
- name: Trustboost Dev Plans Pricing
  plan_count: 3
  slug: trustboost-dev-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Trustboost Dev Rate Limits
  slug: trustboost-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: TrustBoost PII Sanitizer API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: trustboost-dev-rules
score:
  band: strong
  composite: 54.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 71.1
    contract_governance: 31.8
    contract_quality: 46.4
    developer_ergonomics: 59.5
    discoverability: 75.0
    operational_transparency: 23.7
  previous_composite: 53.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/trustboost-dev/trustboost-dev-2026-10-11T131232.png
security:
- kind: authentication
  name: Trustboost Dev Authentication
  slug: trustboost-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Trustboost Dev Domain Security
  slug: trustboost-dev-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: trustboost-pii-sanitizer
  slug: trustboost-dev-pii-sanitizer-SKILL
- name: trustboost-dev-verify-and-score
  slug: trustboost-dev-verify-and-score
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
- Agent-Native
website: https://api.trustboost.dev/
---
