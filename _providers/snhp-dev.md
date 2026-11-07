---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
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
    agent_card: near-conformant
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
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 60
  human_in_the_loop: 1
  name: Snhp Dev Agentic Access
  operation_count: 105
  slug: snhp-dev-agentic-access
  summary_line: 105 operations · 60 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: 'Hosted streamable-HTTP MCP server (protocol 2025-06-18) with two doors on the same application: the core door https://snhp.dev/mcp/ (15 annotated tools — negotiate, negotiate_bundle, score_deal, aucti'
  name: SNHP MCP Server
  slug: mcp-server
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: The Arena API from SNHP — 9 operation(s) for arena.
  name: SNHP Arena API
  slug: snhp-dev-arena-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: 'Tier 2: single-unit auctions'
  name: SNHP Auctions API
  slug: snhp-dev-auctions-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: The billing API from SNHP — 22 operation(s) for billing.
  name: SNHP Billing API
  slug: snhp-dev-billing-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: The Block API from SNHP — 1 operation(s) for block.
  name: SNHP Block API
  slug: snhp-dev-block-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: Catalog + agent onboarding
  name: SNHP Discovery API
  slug: snhp-dev-discovery-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: The Divorce API from SNHP — 3 operation(s) for divorce.
  name: SNHP Divorce API
  slug: snhp-dev-divorce-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: The Health API from SNHP — 1 operation(s) for health.
  name: SNHP Health API
  slug: snhp-dev-health-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: The helper API from SNHP — 4 operation(s) for helper.
  name: SNHP Helper API
  slug: snhp-dev-helper-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: The Hit API from SNHP — 2 operation(s) for hit.
  name: SNHP Hit API
  slug: snhp-dev-hit-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: 'Tier 3: marketplace operator primitives'
  name: SNHP Mechanism API
  slug: snhp-dev-mechanism-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: The mpp API from SNHP — 2 operation(s) for mpp.
  name: SNHP Mpp API
  slug: snhp-dev-mpp-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: 'Tier 1: multi-round bargaining'
  name: SNHP Negotiation API
  slug: snhp-dev-negotiation-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: The notary API from SNHP — 2 operation(s) for notary.
  name: SNHP Notary API
  slug: snhp-dev-notary-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: 'General offer-graph engine: compile / profile / quote a JSON menu spec (discount-only, never above list)'
  name: SNHP Offer API
  slug: snhp-dev-offer-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: The Par API from SNHP — 12 operation(s) for par.
  name: SNHP Par API
  slug: snhp-dev-par-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: The rent API from SNHP — 2 operation(s) for rent.
  name: SNHP Rent API
  slug: snhp-dev-rent-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: The SNHP Evolution Arena API from SNHP — 1 operation(s) for snhp evolution arena.
  name: SNHP SNHP Evolution Arena API
  slug: snhp-dev-snhp-evolution-arena-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: The Stats API from SNHP — 1 operation(s) for stats.
  name: SNHP Stats API
  slug: snhp-dev-stats-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: The store API from SNHP — 12 operation(s) for store.
  name: SNHP Store API
  slug: snhp-dev-store-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: Opt-in data sharing + GDPR (export/delete)
  name: SNHP Telemetry API
  slug: snhp-dev-telemetry-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: The vend API from SNHP — 3 operation(s) for vend.
  name: SNHP Vend API
  slug: snhp-dev-vend-api
- baseURL: https://snhp.dev/mcp/
  baseurl_source: declared
  description: The World API from SNHP — 1 operation(s) for world.
  name: SNHP World API
  slug: snhp-dev-world-api
artifact_total: 38
common:
- group: other
  href: https://artifacts.apis.io/snhp-dev/capabilities/snhp-dev-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/snhp-dev-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/snhp-dev/overlays/snhp-dev-arena-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snhp-dev-arena-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://snhp.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://snhp.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://snhp.dev/redoc
- group: start
  title: ''
  type: GettingStarted
  url: https://snhp.dev/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/ryuxik/snhp/blob/main/PRICING.md
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ryuxik/snhp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ryuxik
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/ryuxik/snhp/blob/main/gametheory/CHANGELOG.md
- group: operate
  href: https://artifacts.apis.io/snhp-dev/changelog/snhp-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/snhp-dev-changelog.yml
- group: other
  title: ''
  type: Research
  url: https://snhp.dev/research
- group: agent
  href: https://artifacts.apis.io/snhp-dev/mcp/snhp-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/snhp-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/snhp-dev/a2a/snhp-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/snhp-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/snhp-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/snhp-dev/llms/snhp-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snhp-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/snhp-dev/well-known/snhp-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/snhp-dev-well-known.yml
- group: build
  href: https://artifacts.apis.io/snhp-dev/packages/snhp-dev-packages.yml
  title: ''
  type: Packages
  url: packages/snhp-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/snhp-dev/packages/snhp-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/snhp-dev-packages.yml
- group: auth
  href: https://artifacts.apis.io/snhp-dev/authentication/snhp-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/snhp-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/snhp-dev/conventions/snhp-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/snhp-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/snhp-dev/conventions/snhp-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/snhp-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/snhp-dev/conformance/snhp-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/snhp-dev-conformance.yml
- group: design
  href: https://artifacts.apis.io/snhp-dev/errors/snhp-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/snhp-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/snhp-dev/lifecycle/snhp-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/snhp-dev-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/snhp-dev/plans/snhp-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/snhp-dev-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/snhp-dev/rate-limits/snhp-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/snhp-dev-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/snhp-dev/sandbox/snhp-dev-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/snhp-dev-sandbox.yml
- group: design
  href: https://artifacts.apis.io/snhp-dev/data-model/snhp-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/snhp-dev-data-model.yml
- group: other
  href: https://artifacts.apis.io/snhp-dev/overlays/snhp-dev-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snhp-dev-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/snhp-dev/security/snhp-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snhp-dev-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/snhp-dev/agentic-access/snhp-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/snhp-dev-agentic-access.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://snhp.dev/llms.txt
created: '2026-09-19'
description: 'SNHP (snhp.dev, operated by gametheory.dev / github.com/ryuxik and listed in the a2aregistry.org harvest as "Negotiation Copilot for Agents") is free, LLM-free game-theory negotiation math for AI agents: a hosted FastAPI "Game Theory Layer" with 74 operations served anonymously as OpenAPI 3.1 on snhp.dev that returns the math-optimal next move in a single-price or multi-issue negotiation in plain dollars, plus auction bidding and reserve pricing, mechanism design (Gale-Shapley, Myerson, posted-price clearance), a cryptographic first-strike commitment, and a verified-peer agent-to-agent flow that settles into signed AP2 Cart/Intent mandates. The same engine is exposed as a live streamable-HTTP MCP server with a 15-tool core door and a 54-tool pro door (listed in the official MCP registry and on Smithery), as a stdio server and Python library on PyPI (snhp, Apache-2.0), and behind an A2A agent card at the canonical well-known path. The core math is free with no key; a self-issued
  gt_* key unlocks a prepaid millicent wallet — funded by Stripe Checkout or agent-natively by the Machine Payments Protocol (Stripe Shared Payment Tokens) — that buys $2 receipted deterministic negotiation sessions and blind-custody encrypted agent memory, every settled call returning an Ed25519-signed receipt verifiable offline. A second application, the Evolution Arena on arena.snhp.dev, publishes its own OpenAPI for the live strategy-evolution sim, the gauntlet certificate and the PAR game. Single deployment, best-effort SLA stated in the API itself, no legal pages, GDPR access/erasure exposed as API operations.'
finops:
- has_sources: true
  method: derived
  name: Snhp Dev Finops
  primary_unit: ''
  service_category: ''
  slug: snhp-dev-finops
  template: true
image: https://snhp.dev/favicon.svg
layout: provider
mcp_servers:
- description: 'SNHP runs a live, hosted, streamable-HTTP MCP server with TWO doors on the same application: the CORE door at https://snhp.dev/mcp/ (15 "hero-first" tools) and the PRO door at https://snhp.dev/mcp/pro'
  name: SNHP MCP Server
  slug: gametheory
- description: ''
  name: MCP endpoint — pro door (54 tools)
  slug: mcp-endpoint-pro-door-54-tools
modified: '2026-09-19'
name: SNHP
nav: Providers
network: true
overview: 'SNHP publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Arena API, Auctions API, Billing API, and 20 more. Tagged areas include Negotiation, Game Theory, AI Agents, MCP, and A2A.


  The SNHP catalog on APIs.io includes 1 Spectral governance ruleset.


  SNHP''s developer surface includes documentation, API reference, getting-started guide, pricing, changelog, authentication, sandbox, and 26 more developer resources.'
plans:
- name: Snhp Dev Plans Pricing
  plan_count: 5
  slug: snhp-dev-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Snhp Dev Rate Limits
  slug: snhp-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: SNHP API Rules
  rule_count: 47
  severity_counts:
    error: 36
    hint: 0
    info: 4
    warn: 7
  slug: snhp-dev-rules
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 42.1
    contract_governance: 31.8
    contract_quality: 41.7
    developer_ergonomics: 50.6
    discoverability: 80.0
    operational_transparency: 21.1
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 22
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/snhp-dev/snhp-dev-2026-10-11T130023.png
security:
- kind: authentication
  name: Snhp Dev Authentication
  slug: snhp-dev-authentication
  summary_line: apiKey/http-bearer/body-field/none · 5 schemes
- kind: domain-security
  name: Snhp Dev Domain Security
  slug: snhp-dev-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 6
skills:
- name: Logroll a multi-issue deal with SNHP (free)
  slug: snhp-dev-logroll-a-multi-issue-deal
- name: Negotiate a single price with SNHP (free, no key)
  slug: snhp-dev-negotiate-a-price
- name: Open a $2 receipted negotiation session (key, wallet, session, receipt)
  slug: snhp-dev-open-a-receipted-session
- name: Opt in to telemetry, report an outcome, export and erase your rows (GDPR Art. 15/17)
  slug: snhp-dev-opt-in-telemetry-and-gdpr-erase
- name: Save and load encrypted agent memory across sessions (blind locker)
  slug: snhp-dev-save-and-load-agent-memory
- name: Verified-peer A2A deal with AP2 settlement (both agents run SNHP)
  slug: snhp-dev-verified-peer-deal-and-ap2-settlement
slug: snhp-dev
tags:
- Negotiation
- Game Theory
- AI Agents
- MCP
- A2A
- Agentic Payments
- Auctions
- Mechanism Design
- Pricing Optimization
- Artificial Intelligence
- Agent-Native
- Developer Tools
website: https://snhp.dev/
---
