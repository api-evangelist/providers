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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Block402 Xyz Agentic Access
  operation_count: 1
  slug: block402-xyz-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://api.block402.xyz
  baseurl_source: declared
  description: The Bitcoin API from block402-xyz — 1 operation(s) for bitcoin.
  name: block402-xyz Bitcoin API
  slug: block402-xyz-bitcoin-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/block402-xyz/agentic-access/block402-xyz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/block402-xyz-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/block402-xyz/rules/block402-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/block402-xyz-rules.yml
- group: design
  href: https://artifacts.apis.io/block402-xyz/vocabulary/block402-xyz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/block402-xyz-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/block402-xyz/conventions/block402-xyz-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/block402-xyz-conventions.yml
- group: design
  href: https://artifacts.apis.io/block402-xyz/conventions/block402-xyz-conventions.yml
  title: ''
  type: Conventions
  url: conventions/block402-xyz-conventions.yml
- group: design
  href: https://artifacts.apis.io/block402-xyz/errors/block402-xyz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/block402-xyz-problem-types.yml
- group: design
  href: https://artifacts.apis.io/block402-xyz/conformance/block402-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/block402-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/block402-xyz/llms/block402-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/block402-xyz-llms.txt
- group: other
  href: https://artifacts.apis.io/block402-xyz/hosts/block402-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/block402-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/block402-xyz/vendors/block402-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/block402-xyz-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://block402.xyz/agents/
- group: docs
  title: ''
  type: APIReference
  url: https://block402.xyz/docs/api.md
- group: auth
  href: https://artifacts.apis.io/block402-xyz/security/block402-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/block402-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://block402.xyz/
created: '2026-11-02'
description: Block402 offers a pay‑per‑request API that provides read‑only blockchain intelligence for AI agents. It supplies Ethereum and Bitcoin mainnet data, including balances, blocks, transactions, receipts, logs and proofs, accessed via JSON‑RPC calls. Payments are made in USDC on Base mainnet using the x402 protocol, with no subscription or credit‑card requirement.
layout: provider
modified: '2026-11-02'
name: block402-xyz
nav: Providers
network: true
overview: 'block402-xyz publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Bitcoin API. Tagged areas include Blockchain, AI Agents, Ethereum, Bitcoin, and Pay‑per‑request.


  The block402-xyz catalog on APIs.io includes 1 Spectral governance ruleset.


  block402-xyz''s developer surface includes getting-started guide, API reference, and 12 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: block402-xyz API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: block402-xyz-rules
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 49.6
    developer_ergonomics: 9.5
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Block402 Xyz Domain Security
  slug: block402-xyz-domain-security
  summary_line: TLSv1.3
slug: block402-xyz
tags:
- Blockchain
- AI Agents
- Ethereum
- Bitcoin
- Pay‑per‑request
- USDC
- x402
website: https://block402.xyz/
---
