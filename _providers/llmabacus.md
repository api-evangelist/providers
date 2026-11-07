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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'LLM Abacus API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: LLM Abacus API
  slug: llmabacus-api
artifact_total: 4
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.llmabacus.com/api/prices
- group: design
  href: https://artifacts.apis.io/llmabacus/rules/llmabacus-rules.yml
  title: ''
  type: Spectral
  url: rules/llmabacus-rules.yml
- group: design
  href: https://artifacts.apis.io/llmabacus/vocabulary/llmabacus-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/llmabacus-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/llmabacus/changelog/llmabacus-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/llmabacus-changelog.yml
- group: design
  href: https://artifacts.apis.io/llmabacus/conformance/llmabacus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/llmabacus-conformance.yml
- group: agent
  href: https://artifacts.apis.io/llmabacus/llms/llmabacus-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/llmabacus-llms.txt
- group: other
  href: https://artifacts.apis.io/llmabacus/hosts/llmabacus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/llmabacus-hosts.yml
- group: other
  href: https://artifacts.apis.io/llmabacus/vendors/llmabacus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/llmabacus-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.llmabacus.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.llmabacus.com/media
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.llmabacus.com/changelog
- group: auth
  href: https://artifacts.apis.io/llmabacus/security/llmabacus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/llmabacus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.llmabacus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.llmabacus.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://www.llmabacus.com/en/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://llmabacus.com/
  reason: no-developer-program
  state: none
created: '2026-10-18'
description: LLM Abacus provides a comprehensive comparison and pricing guide for large language model APIs, aggregating data on models such as GPT‑5.5, Claude, Gemini, DeepSeek, and many others. The site offers detailed tables of token costs, latency, and feature sets, along with tools for estimating usage, exploring model capabilities, and accessing multilingual pricing information. It serves developers and businesses seeking to evaluate and select LLM providers based on cost, performance, and regional availability.
image: https://www.llmabacus.com/opengraph-image?43beca158235bb56
layout: provider
modified: '2026-10-18'
name: LLM Abacus
nav: Providers
network: true
overview: 'LLM Abacus is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, LLM, Pricing, and Comparison.


  The LLM Abacus catalog on APIs.io includes 1 Spectral governance ruleset.


  LLM Abacus'' developer surface includes pricing, changelog, documentation, API reference, and 11 more developer resources.'
plans:
- name: Llmabacus Plans Pricing
  plan_count: 0
  slug: llmabacus-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: LLM Abacus API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: llmabacus-rules
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 32.8
    catalog_earned_first_party: 0.0
    catalog_gap: 82.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 10.5
    contract_governance: 35.6
    contract_quality: 9.4
    developer_ergonomics: 8.3
    discoverability: 56.3
    operational_transparency: 7.9
  previous_composite: 21.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/llmabacus/llmabacus-2026-11-03T134949.png
security:
- kind: domain-security
  name: Llmabacus Domain Security
  slug: llmabacus-domain-security
  summary_line: TLSv1.3 · HSTS
slug: llmabacus
tags:
- Company
- LLM
- Pricing
- Comparison
website: https://www.llmabacus.com/
---
