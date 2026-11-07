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
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: BuyWise Agent API provides trust signals about brands and product listings for shopping agents.
  name: BuyWise Agent API
  slug: buywise-agent-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/buywise-fyi/rules/buywise-fyi-rules.yml
  title: ''
  type: Spectral
  url: rules/buywise-fyi-rules.yml
- group: design
  href: https://artifacts.apis.io/buywise-fyi/json-ld/buywise-fyi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buywise-fyi-context.jsonld
- group: design
  href: https://artifacts.apis.io/buywise-fyi/vocabulary/buywise-fyi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buywise-fyi-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/buywise-fyi/conformance/buywise-fyi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buywise-fyi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buywise-fyi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/buywise-fyi/data-model/buywise-fyi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buywise-fyi-data-model.yml
- group: design
  href: https://artifacts.apis.io/buywise-fyi/errors/buywise-fyi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/buywise-fyi-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/buywise-fyi/llms/buywise-fyi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buywise-fyi-llms.txt
- group: agent
  href: https://artifacts.apis.io/buywise-fyi/well-known/buywise-fyi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buywise-fyi-well-known.yml
- group: other
  href: https://artifacts.apis.io/buywise-fyi/hosts/buywise-fyi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buywise-fyi-hosts.yml
- group: other
  href: https://artifacts.apis.io/buywise-fyi/vendors/buywise-fyi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buywise-fyi-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buywise.fyi/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buywise.fyi/privacy
- group: auth
  href: https://artifacts.apis.io/buywise-fyi/security/buywise-fyi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buywise-fyi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buywise.fyi/
created: '2026-11-03'
description: BuyWise provides a free Chrome extension that instantly evaluates product pages, delivering odds on authenticity, quality, pricing fairness, and review credibility. It aggregates checks like brand authenticity, product quality, price analysis, discount verification, review authenticity, and pressure‑tactic detection, helping shoppers make informed decisions.
jsonld:
- class_count: 15
  name: Buywise Fyi Context
  property_count: 43
  slug: buywise-fyi-context
layout: provider
modified: '2026-11-03'
name: BuyWise
nav: Providers
network: true
overview: 'BuyWise publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shopping, Chrome Extension, ProductAnalysis, and Consumer Protection.


  The BuyWise catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: BuyWise API Rules
  rule_count: 61
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 1
  slug: buywise-fyi-rules
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 1.8
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buywise Fyi Domain Security
  slug: buywise-fyi-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: buywise-fyi-check-product-listings
  slug: buywise-fyi-check-product-listings
slug: buywise-fyi
tags:
- Company
- Shopping
- Chrome Extension
- ProductAnalysis
- Consumer Protection
website: https://buywise.fyi/
---
