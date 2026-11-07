---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
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
    agent_skills: unknown
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Addshuffle Com Agentic Access
  operation_count: 17
  slug: addshuffle-com-agentic-access
  summary_line: 17 operations · 12 acting
api_count: 1
apis:
- baseURL: https://www.textshuffle.com
  baseurl_source: declared
  description: The Credits API from Shuffle — 4 operation(s) for credits.
  name: Shuffle Credits API
  slug: addshuffle-com-credits-api
- baseURL: https://www.textshuffle.com
  baseurl_source: declared
  description: The L402 API from Shuffle — 3 operation(s) for l402.
  name: Shuffle L402 API
  slug: addshuffle-com-l402-api
- baseURL: https://www.textshuffle.com
  baseurl_source: declared
  description: The Manual Mode API from Shuffle — 5 operation(s) for manual mode.
  name: Shuffle Manual Mode API
  slug: addshuffle-com-manual-mode-api
- baseURL: https://www.textshuffle.com
  baseurl_source: declared
  description: The Utilities API from Shuffle — 1 operation(s) for utilities.
  name: Shuffle Utilities API
  slug: addshuffle-com-utilities-api
- baseURL: https://www.textshuffle.com
  baseurl_source: declared
  description: The Video Chain API from Shuffle — 4 operation(s) for video chain.
  name: Shuffle Video Chain API
  slug: addshuffle-com-video-chain-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/addshuffle-com/agentic-access/addshuffle-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/addshuffle-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/addshuffle-com/plans/addshuffle-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/addshuffle-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/addshuffle-com/rules/addshuffle-com-rules.yml
  title: ''
  type: Spectral
  url: rules/addshuffle-com-rules.yml
- group: design
  href: https://artifacts.apis.io/addshuffle-com/json-ld/addshuffle-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/addshuffle-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/addshuffle-com/vocabulary/addshuffle-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/addshuffle-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/addshuffle-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/addshuffle-com/data-model/addshuffle-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/addshuffle-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/addshuffle-com/errors/addshuffle-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/addshuffle-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/addshuffle-com/conformance/addshuffle-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/addshuffle-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/addshuffle-com/llms/addshuffle-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/addshuffle-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/addshuffle-com/well-known/addshuffle-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/addshuffle-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/addshuffle-com/hosts/addshuffle-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/addshuffle-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/addshuffle-com/vendors/addshuffle-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/addshuffle-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.textshuffle.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.textshuffle.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.textshuffle.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.textshuffle.com/plans
- group: auth
  href: https://artifacts.apis.io/addshuffle-com/security/addshuffle-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/addshuffle-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.textshuffle.com/
created: '2026-10-31'
description: Shuffle is an AI‑powered social media manager that creates, schedules, and publishes posts across multiple platforms, answers customer inquiries, and lets users approve content via text or a web interface. Positioned as a social media manager for AI agents, it helps brands automate their online presence while retaining human oversight, enabling efficient, AI‑driven engagement with audiences.
image: https://www.textshuffle.com/showcase/selected-1.webp
json_schemas:
- name: ChainSettings
  property_count: 6
  slug: addshuffle-com-chain-settings
- name: CreditBalance
  property_count: 4
  slug: addshuffle-com-credit-balance
- name: CreditTransaction
  property_count: 6
  slug: addshuffle-com-credit-transaction
- name: L402Offer
  property_count: 8
  slug: addshuffle-com-l402-offer
- name: Progress
  property_count: 5
  slug: addshuffle-com-progress
jsonld:
- class_count: 6
  name: Addshuffle Com Context
  property_count: 25
  slug: addshuffle-com-context
layout: provider
modified: '2026-10-31'
name: Shuffle
nav: Providers
network: true
overview: 'Shuffle publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Credits API, L402 API, Manual Mode API, and 2 more. Tagged areas include Artificial Intelligence, Social Media, Automation, Marketing, and Software-as-a-Service.


  The Shuffle catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Shuffle''s developer surface includes support, pricing, and 17 more developer resources.'
plans:
- name: Addshuffle Com Plans Pricing
  plan_count: 4
  slug: addshuffle-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Addshuffle Com Rate Limits
  slug: addshuffle-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Shuffle API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: addshuffle-com-rules
scopes:
- name: Addshuffle Com Scopes
  scope_count: 0
  slug: addshuffle-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 29
    catalog_earned: 74.0
    catalog_earned_first_party: 12.0
    catalog_gap: 41.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 47.4
    contract_governance: 19.7
    contract_quality: 59.4
    developer_ergonomics: 17.1
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 44.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Addshuffle Com Authentication
  slug: addshuffle-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Addshuffle Com Domain Security
  slug: addshuffle-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 4
skills:
- name: cancel-video-chain
  slug: cancel-video-chain
- name: create-video-chain
  slug: create-video-chain
- name: get-video-chain-status
  slug: get-video-chain-status
- name: retry-step
  slug: retry-step
slug: addshuffle-com
tags:
- Artificial Intelligence
- Social Media
- Automation
- Marketing
- Software-as-a-Service
website: https://www.textshuffle.com/
---
