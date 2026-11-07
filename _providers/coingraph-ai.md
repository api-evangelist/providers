---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Coingraph Ai Agentic Access
  operation_count: 25
  slug: coingraph-ai-agentic-access
  summary_line: 25 operations · 10 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://coingraph.ai/api/v1
  baseurl_source: declared
  description: 5 ready-made agents built on the data above. Each returns a verdict, a plain summary, sourced reasons and a proof id.
  name: CoinGraph Agents API
  slug: coingraph-ai-agents-api
- baseURL: https://coingraph.ai/api/v1
  baseurl_source: declared
  description: Ask CoinGraph to think. Creates objects with ids that go into the public record.
  name: CoinGraph Decide API
  slug: coingraph-ai-decide-api
- baseURL: https://coingraph.ai/api/v1
  baseurl_source: declared
  description: Find what CoinGraph covers and whether it is healthy. Free.
  name: CoinGraph Discover API
  slug: coingraph-ai-discover-api
- baseURL: https://coingraph.ai/api/v1
  baseurl_source: declared
  description: Check CoinGraph's record and prove what you were told.
  name: CoinGraph Trust API
  slug: coingraph-ai-trust-api
- baseURL: https://coingraph.ai/api/v1
  baseurl_source: declared
  description: Everything CoinGraph knows, as data.
  name: CoinGraph Understand API
  slug: coingraph-ai-understand-api
- baseURL: https://coingraph.ai/api/v1
  baseurl_source: declared
  description: Get told when something changes.
  name: CoinGraph Watch API
  slug: coingraph-ai-watch-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/coingraph-ai/agentic-access/coingraph-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coingraph-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/coingraph-ai/plans/coingraph-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coingraph-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/coingraph-ai/rules/coingraph-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/coingraph-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/coingraph-ai/json-ld/coingraph-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coingraph-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/coingraph-ai/vocabulary/coingraph-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coingraph-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/coingraph-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/coingraph-ai/data-model/coingraph-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coingraph-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/coingraph-ai/authentication/coingraph-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coingraph-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/coingraph-ai/errors/coingraph-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coingraph-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/coingraph-ai/conformance/coingraph-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coingraph-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coingraph-ai/llms/coingraph-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coingraph-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/coingraph-ai/well-known/coingraph-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coingraph-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/coingraph-ai/hosts/coingraph-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coingraph-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coingraph.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coingraph.ai/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://coingraph.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://coingraph.ai/signin
- group: docs
  title: ''
  type: Documentation
  url: https://coingraph.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://coingraph.ai/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://coingraph.ai/docs/api
- group: auth
  href: https://artifacts.apis.io/coingraph-ai/security/coingraph-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coingraph-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coingraph.ai/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://coingraph.ai/openapi.json
  - status: 401
    url: https://coingraph.ai/mcp
  - status: 200
    url: https://coingraph.ai/
  reason: partner-login
  state: gated
created: '2026-11-04'
description: CoinGraph provides provable cryptocurrency data for AI agents, covering trades, tokens, wallets, and markets. Built in Singapore by BlockEXC Pte. Ltd., it offers real‑time market insights, token analytics, and secure data APIs for developers and autonomous agents.
image: https://coingraph.ai/opengraph-image?3fe3b41e8b8e1f36
json_schemas:
- name: Brief
  property_count: 13
  slug: coingraph-ai-brief
- name: EvaluateRequest
  property_count: 3
  slug: coingraph-ai-evaluate-request
- name: Evaluation
  property_count: 9
  slug: coingraph-ai-evaluation
- name: History
  property_count: 7
  slug: coingraph-ai-history
- name: MonitorRequest
  property_count: 3
  slug: coingraph-ai-monitor-request
- name: ResponseProof
  property_count: 4
  slug: coingraph-ai-response-proof
jsonld:
- class_count: 9
  name: Coingraph Ai Context
  property_count: 42
  slug: coingraph-ai-context
layout: provider
modified: '2026-11-04'
name: CoinGraph
nav: Providers
network: true
overview: 'CoinGraph publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Decide API, Discover API, and 3 more. Tagged areas include Crypto Data, AI Agents, trading agents, Wallets, and On-Chain Data.


  The CoinGraph catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CoinGraph''s developer surface includes authentication, pricing, documentation, getting-started guide, API reference, and 17 more developer resources.'
plans:
- name: Coingraph Ai Plans Pricing
  plan_count: 4
  slug: coingraph-ai-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: CoinGraph API Rules
  rule_count: 62
  severity_counts:
    error: 54
    hint: 0
    info: 4
    warn: 4
  slug: coingraph-ai-rules
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 65.5
    developer_ergonomics: 42.3
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Coingraph Ai Authentication
  slug: coingraph-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Coingraph Ai Domain Security
  slug: coingraph-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: coingraph-ai-decide-token-action
  slug: coingraph-ai-decide-token-action
- name: coingraph-ai-watch-monitor
  slug: coingraph-ai-watch-monitor
slug: coingraph-ai
tags:
- Crypto Data
- AI Agents
- trading agents
- Wallets
- On-Chain Data
- Market Data
website: https://coingraph.ai/
---
