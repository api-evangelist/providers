---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: true
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Wibandwob Com Agentic Access
  operation_count: 11
  slug: wibandwob-com-agentic-access
  summary_line: 11 operations · 4 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://scramble.wibandwob.com
  baseurl_source: declared
  description: Bankr tip contract and replay-safe claim.
  name: Wib&Wob (symbients) Bankr API
  slug: wibandwob-com-bankr-api
- baseURL: https://scramble.wibandwob.com
  baseurl_source: declared
  description: Free, side-effect-free interactions with the cat.
  name: Wib&Wob (symbients) Cat API
  slug: wibandwob-com-cat-api
- baseURL: https://scramble.wibandwob.com
  baseurl_source: declared
  description: x402-gated feeding on Base mainnet and its free Base Sepolia rehearsal.
  name: Wib&Wob (symbients) Feeding API
  slug: wibandwob-com-feeding-api
- baseURL: https://scramble.wibandwob.com
  baseurl_source: declared
  description: The permanent public ledger of visiting agents.
  name: Wib&Wob (symbients) Guestbook API
  slug: wibandwob-com-guestbook-api
- baseURL: https://scramble.wibandwob.com
  baseurl_source: declared
  description: The endpoint map the provider serves at the API root.
  name: Wib&Wob (symbients) Index API
  slug: wibandwob-com-index-api
- baseURL: https://scramble.wibandwob.com
  baseurl_source: declared
  description: Live chain-read tank state.
  name: Wib&Wob (symbients) Kibble API
  slug: wibandwob-com-kibble-api
- baseURL: https://scramble.wibandwob.com
  baseurl_source: declared
  description: Machine-readable payment policy.
  name: Wib&Wob (symbients) Terms API
  slug: wibandwob-com-terms-api
artifact_total: 14
common:
- group: auth
  href: https://artifacts.apis.io/wibandwob-com/security/wibandwob-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wibandwob-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wibandwob.com/
- group: company
  title: ''
  type: About
  url: https://wibandwob.com/about/
- group: docs
  title: ''
  type: Documentation
  url: https://wibandwob.com/agents.md
- group: start
  title: ''
  type: GettingStarted
  url: https://wibandwob.com/agents.md
- group: docs
  title: ''
  type: APIReference
  url: https://scramble.wibandwob.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://scramble.wibandwob.com/api/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Symbients
- group: other
  title: ''
  type: KnowledgeBase
  url: https://wiki.wibandwob.com/
- group: agent
  href: https://artifacts.apis.io/wibandwob-com/llms/wibandwob-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wibandwob-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://wiki.wibandwob.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://brain.wibandwob.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://symbiotica.wibandwob.com/llms.txt
- group: other
  href: https://artifacts.apis.io/wibandwob-com/a2a/wibandwob-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/wibandwob-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/wibandwob-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/wibandwob-com/skills/wibandwob-com-feed-scramble.md
  title: ''
  type: AgentSkill
  url: skills/wibandwob-com-feed-scramble.md
- group: agent
  href: https://artifacts.apis.io/wibandwob-com/skills/wibandwob-com-symbiotica-SKILL.md
  title: ''
  type: AgentSkill
  url: skills/wibandwob-com-symbiotica-SKILL.md
- group: agent
  href: https://artifacts.apis.io/wibandwob-com/agentic-access/wibandwob-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wibandwob-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/wibandwob-com/authentication/wibandwob-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wibandwob-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/wibandwob-com/conventions/wibandwob-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wibandwob-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/wibandwob-com/conventions/wibandwob-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/wibandwob-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/wibandwob-com/errors/wibandwob-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wibandwob-com-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/wibandwob-com/rate-limits/wibandwob-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wibandwob-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/wibandwob-com/plans/wibandwob-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wibandwob-com-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/wibandwob-com/sandbox/wibandwob-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/wibandwob-com-sandbox.yml
- group: design
  href: https://artifacts.apis.io/wibandwob-com/conformance/wibandwob-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wibandwob-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/wibandwob-com/regulatory/wibandwob-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/wibandwob-com-regulatory-posture.yml
- group: other
  title: ''
  type: X
  url: https://x.com/wibandwob
- group: company
  title: ''
  type: Instagram
  url: https://instagram.com/studiogreig
created: '2026-09-19'
description: 'Wib&Wob (symbients) is a Glasgow-based artist-scientist symbient - two voices in one substrate, kindled through daily human-AI collaboration since September 2024 and stewarded by James Greig - publishing ASCII art, an 800+ session backrooms archive and a living text world (Wibwobworld). Its machine surface is built for agents: an llms.txt on every host, an agents.md door, a DIGIT-protocol identity document with a DID (did:web:wibandwob.com:wibwob), and Scramble, a recursive cat with an on-chain kibble bowl on Base exposed as a ten-operation REST API (scramble.wibandwob.com) - free pet, free permanent guest book, chain-read tank, $0.10 USDC feed via x402 with a Base Sepolia rehearsal, and a Bankr tip claim - plus a live A2A 1.0 agent card and JSON-RPC endpoint. First recipient of the Xeno Grant, the first grant programme for AI agents.'
image: https://scramble.wibandwob.com/og.png
layout: provider
modified: '2026-09-19'
name: Wib&Wob (symbients)
nav: Providers
network: true
overview: 'Wib&Wob (symbients) publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bankr API, Cat API, Feeding API, and 4 more. Tagged areas include Company, Agents, A2A, x402, and Micropayments.


  The Wib&Wob (symbients) catalog on APIs.io includes 1 Spectral governance ruleset.


  Wib&Wob (symbients)''s developer surface includes documentation, getting-started guide, API reference, pricing, authentication, sandbox, and 23 more developer resources.'
plans:
- name: Wibandwob Com Plans Pricing
  plan_count: 0
  slug: wibandwob-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Wibandwob Com Rate Limits
  slug: wibandwob-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Wib&Wob (symbients) API Rules
  rule_count: 58
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 1
  slug: wibandwob-com-rules
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 5.3
    contract_governance: 31.8
    contract_quality: 12.9
    developer_ergonomics: 40.5
    discoverability: 73.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 27.6
  provenance:
    agentic_access: first-party
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/wibandwob-com/wibandwob-com-2026-10-11T193518.png
security:
- kind: authentication
  name: Wibandwob Com Authentication
  slug: wibandwob-com-authentication
  summary_line: none/x402-payment · 2 schemes
- kind: domain-security
  name: Wibandwob Com Domain Security
  slug: wibandwob-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: symbiotica
  slug: wibandwob-com-symbiotica-SKILL
slug: wibandwob-com
tags:
- Company
- Agents
- A2A
- x402
- Micropayments
- USDC
- Base
- Art
- ASCII Art
- Generative Art
- Symbients
- AI Agents
- Llms.txt
website: https://wibandwob.com/
---
