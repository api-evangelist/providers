---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Coil Trade Agentic Access
  operation_count: 52
  slug: coil-trade-agentic-access
  summary_line: 52 operations · 3 acting
api_count: 1
apis:
- baseURL: https://coil.trade
  baseurl_source: declared
  description: Free credentials — an instant email key, or wallet sign-in (SIWX, CAIP-122). Signatures move no funds.
  name: Coil Access & Keys API
  slug: coil-trade-access-keys-api
- baseURL: https://coil.trade
  baseurl_source: declared
  description: 'The polling loop: hash the board for free, buy the delta only when it moves. An unchanged hash is never billed.'
  name: Coil Change Detection API
  slug: coil-trade-change-detection-api
- baseURL: https://coil.trade
  baseurl_source: declared
  description: 'Subscription lane ($49/mo): the engine-grade feed and the served, versioned trading discipline. License key, never sold per call.'
  name: Coil Coil Live API
  slug: coil-trade-coil-live-api
- baseURL: https://coil.trade
  baseurl_source: declared
  description: Paid per-read slices of the scored board — regime, buy list, per-name and per-sector reads, crypto. USDC over x402; no account, no key.
  name: Coil Market Data API
  slug: coil-trade-market-data-api
- baseURL: https://coil.trade
  baseurl_source: declared
  description: The Paid reads API from Coil — 2 operation(s) for paid reads.
  name: Coil Paid reads API
  slug: coil-trade-paid-reads-api
- baseURL: https://coil.trade
  baseurl_source: declared
  description: The Research API from Coil — 11 operation(s) for research.
  name: Coil Research API
  slug: coil-trade-research-api
- baseURL: https://coil.trade
  baseurl_source: declared
  description: Free, before any payment — the append-only commitment log, the forward-return audit of our own scores, and the engine's record vs SPY/QQQ. Check the publisher before trusting it.
  name: Coil Verification API
  slug: coil-trade-verification-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/coil-trade/agentic-access/coil-trade-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coil-trade-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/coil-trade/rules/coil-trade-rules.yml
  title: ''
  type: Spectral
  url: rules/coil-trade-rules.yml
- group: design
  href: https://artifacts.apis.io/coil-trade/vocabulary/coil-trade-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coil-trade-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/coil-trade/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/coil-trade/authentication/coil-trade-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coil-trade-authentication.yml
- group: design
  href: https://artifacts.apis.io/coil-trade/errors/coil-trade-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coil-trade-problem-types.yml
- group: design
  href: https://artifacts.apis.io/coil-trade/conformance/coil-trade-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coil-trade-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coil-trade/llms/coil-trade-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coil-trade-llms.txt
- group: other
  href: https://artifacts.apis.io/coil-trade/a2a/coil-trade-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/coil-trade-a2a.yml
- group: agent
  href: https://artifacts.apis.io/coil-trade/well-known/coil-trade-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coil-trade-well-known.yml
- group: other
  href: https://artifacts.apis.io/coil-trade/hosts/coil-trade-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coil-trade-hosts.yml
- group: other
  href: https://artifacts.apis.io/coil-trade/vendors/coil-trade-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coil-trade-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://coil.trade/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coil.trade/terms
- group: auth
  title: ''
  type: Security
  url: https://coil.trade/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coil.trade/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/joeyfife
- group: docs
  title: ''
  type: Documentation
  url: https://coil.trade/guides/automate-soxl-soxs-ai-agent
- group: company
  title: ''
  type: Blog
  url: https://coil.trade/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://coil.trade/agents/quickstart
- group: auth
  href: https://artifacts.apis.io/coil-trade/security/coil-trade-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coil-trade-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coil.trade/
created: '2026-11-04'
description: Coil is a solo-built AI-powered stock scanner that provides real-time market data and trading signals for users and AI agents. It offers a live board, a scanner tool, and an MCP server for agents to access market information programmatically. The platform emphasizes honesty, transparency, and privacy, with clear rules governing claims and data usage. Coil aims to empower both individuals and automated agents in making informed trading decisions.
image: https://coil.trade/assets/img/og-cover.png?v=9
layout: provider
modified: '2026-11-04'
name: Coil
nav: Providers
network: true
overview: 'Coil publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access & Keys API, Change Detection API, Coil Live API, and 4 more. Tagged areas include Finance, Artificial Intelligence, Stock-Scanner, Real-Time Data, and Trading.


  The Coil catalog on APIs.io includes 1 Spectral governance ruleset.


  Coil''s developer surface includes authentication, documentation, engineering blog, API reference, and 18 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Coil API Rules
  rule_count: 56
  severity_counts:
    error: 46
    hint: 0
    info: 2
    warn: 8
  slug: coil-trade-rules
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 51.1
    developer_ergonomics: 32.7
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 25.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Coil Trade Authentication
  slug: coil-trade-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Coil Trade Domain Security
  slug: coil-trade-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: coil-trade-market-overview
  slug: coil-trade-market-overview
slug: coil-trade
tags:
- Finance
- Artificial Intelligence
- Stock-Scanner
- Real-Time Data
- Trading
website: https://coil.trade/
---
