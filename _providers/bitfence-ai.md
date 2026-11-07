---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/bitfence-ai/hosts/bitfence-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitfence-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bitfence-ai/vendors/bitfence-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitfence-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bitfence-ai/security/bitfence-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitfence-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitfence.ai/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 301
    url: https://bitfence.ai/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: Bitfence AI provides pre‑transaction risk infrastructure for autonomous AI agents operating on‑chain. It intercepts token transactions, evaluates them across weighted on‑chain risk categories, and returns a recommendation within 50 ms for cached responses. The service supports Base, Solana, Ethereum, Arbitrum, BSC and HyperEVM, helping agents make informed decisions before swaps or transfers.
layout: provider
modified: '2026-11-02'
name: Bitfence AI
nav: Providers
network: true
overview: Bitfence AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Blockchain, Risk Assessment, Tokens, and Autonomous Agents.
random_paper: 23
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bitfence Ai Domain Security
  slug: bitfence-ai-domain-security
  summary_line: TLSv1.3
slug: bitfence-ai
tags:
- Artificial Intelligence
- Blockchain
- Risk Assessment
- Tokens
- Autonomous Agents
- Company
website: https://bitfence.ai/
---
