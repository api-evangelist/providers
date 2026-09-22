---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-09-21'
api_count: 1
apis:
- baseURL: https://eqbuilder.dev/api
  baseurl_source: declared
  description: 'REST API (OpenAPI 3.1, 133 operations) for scoring AI-generated text against 28 human personality profiles. Free anonymous surface: three lifetime scores per caller (POST /api/score with data_consent)'
  name: EQ Scoring Platform API
  slug: eq-scoring-platform-api
- description: Official remote MCP server (streamable HTTP, protocol 2025-06-18) at https://eqbuilder.dev/api/mcp with no authentication. Eight free, read-only tools — score_text (three trial scores), list_profiles,
  name: Marz Greta-Lock Network MCP Server
  slug: marz-greta-lock-network-mcp-server
- description: 'A2A agent card served at /.well-known/agent-card.json (aliases /.well-known/agent.json and /.well-known/agents.json): protocolVersion 1.0, six skills (agent-buy-and-run, storelayer-recommend, storelay'
  name: Marz Greta-Lock Network A2A Agent Card
  slug: marz-greta-lock-network-a2a-agent-card
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://eqbuilder.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://eqbuilder.dev/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://eqbuilder.dev/api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://eqbuilder.dev/api/starter-kit/PAY_AND_SCORE.md
- group: commercial
  title: ''
  type: Pricing
  url: https://eqbuilder.dev/api/pricing
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/llms/eqbuilder-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eqbuilder-dev-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://eqbuilder.dev/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/well-known/eqbuilder-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/eqbuilder-dev-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/a2a/eqbuilder-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/eqbuilder-dev-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/mcp/eqbuilder-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/eqbuilder-dev-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/mcp/eqbuilder-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/eqbuilder-dev-tool-crosswalk.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/conformance/eqbuilder-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eqbuilder-dev-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/lifecycle/eqbuilder-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/eqbuilder-dev-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/authentication/eqbuilder-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/eqbuilder-dev-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/conventions/eqbuilder-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/eqbuilder-dev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/conventions/eqbuilder-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/eqbuilder-dev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/errors/eqbuilder-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/eqbuilder-dev-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/data-model/eqbuilder-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eqbuilder-dev-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/plans/eqbuilder-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eqbuilder-dev-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/rate-limits/eqbuilder-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/eqbuilder-dev-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/sandbox/eqbuilder-dev-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/eqbuilder-dev-sandbox.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/overlays/eqbuilder-dev-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/eqbuilder-dev-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/packages/eqbuilder-dev-packages.yml
  title: ''
  type: Packages
  url: packages/eqbuilder-dev-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/packages/eqbuilder-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/eqbuilder-dev-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/components/eqbuilder-dev-components.yml
  title: ''
  type: Components
  url: components/eqbuilder-dev-components.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/changelog/eqbuilder-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/eqbuilder-dev-changelog.yml
- group: learn
  title: ''
  type: TrainingDataSummary
  url: https://eqbuilder.dev/api/corpus/evidence
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/eqbuilder-dev/refs/heads/main/security/eqbuilder-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eqbuilder-dev-domain-security.yml
created: '2026-09-19'
description: 'Marz Greta-Lock Network operates eqbuilder.dev, an EQ benchmark for AI agents: a machine-to-machine API that scores AI-generated text for human-likeness against 28 human personality profiles (EQ, formality, directness, hesitation, punctuation, response-delay cadence) with deterministic statistics and no LLM calls, returns a ready-to-paste system-prompt fix with every score, and sells validated benchmarks, deep analysis, rewrites, script-adherence checks, bot-vs-bot duels, role-play rooms and coaching packs per call through x402 v2 (gasless USDC on Base, legacy Solana) or prepaid card credit packs. The surface is published as an OpenAPI 3.1 document (133 operations), a free anonymous remote MCP server (8 tools), an A2A agent card, an OpenAI plugin manifest, an x402 payable-resource catalog, llms.txt and first-party Python and Node SDKs; it also hosts a read-only recommendation matcher over the third-party Storelayer storefront-widget catalog.'
image: https://eqbuilder.dev/logo.png
layout: provider
mcp_servers:
- description: 'Official remote MCP server operated by the provider on its own host. Streamable HTTP at https://eqbuilder.dev/api/mcp, no authentication: initialize answered with protocolVersion 2025-06-18 and server'
  name: Marz Greta-Lock Network — AI Text Human-Likeness Benchmark
  slug: marz-greta-lock-network-ai-text-human-likeness-benchmark
modified: '2026-09-19'
name: Marz Greta-Lock Network
nav: Providers
network: true
overview: 'Marz Greta-Lock Network publishes 1 API on the [APIs.io](https://apis.io/) network: EQ Scoring Platform API. Tagged areas include Company, AI Agents, Agent Evaluation, Benchmarking, and Text Analysis.


  Marz Greta-Lock Network''s developer surface includes documentation, API reference, getting-started guide, pricing, authentication, sandbox, changelog, and 22 more developer resources.'
plans:
- name: Eqbuilder Dev Plans Pricing
  plan_count: 7
  slug: eqbuilder-dev-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Eqbuilder Dev Rate Limits
  slug: eqbuilder-dev-rate-limits
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 44.9
    developer_ergonomics: 56.5
    discoverability: 75.9
    operational_transparency: 47.4
  previous_composite: 45.3
  provenance:
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
    score: 26.6
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Eqbuilder Dev Authentication
  slug: eqbuilder-dev-authentication
  summary_line: none (anonymous free surface)/x402 payment-as-authorization (header)/apiKey-style secret token (header)/ownership proof (query)/apiKey (header) + cookie session (operator/admin only) · 7 schemes
- kind: domain-security
  name: Eqbuilder Dev Domain Security
  slug: eqbuilder-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eqbuilder-dev
tags:
- Company
- AI Agents
- Agent Evaluation
- Benchmarking
- Text Analysis
- Emotional Intelligence
- Conversational AI
- x402
- Agent Payments
- MCP
- A2A
- Developer Tools
website: https://eqbuilder.dev/
---
