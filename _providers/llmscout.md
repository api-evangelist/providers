---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: LLM Scout provides an API for offline verification of LLM-powered system behavior, enabling safety, accuracy, and compliance checks.
  name: LLM Scout API
  slug: llm-scout-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/llmscout/plans/llmscout-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/llmscout-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/llmscout/hosts/llmscout-hosts.yml
  title: ''
  type: Hosts
  url: hosts/llmscout-hosts.yml
- group: auth
  href: https://artifacts.apis.io/llmscout/security/llmscout-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/llmscout-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://llmscout.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://llmscout.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://llmscout.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://llmscout.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://llmscout.com/release-notes
coverage:
  checked: '2026-10-18'
  detail: No OpenAPI, AsyncAPI, GraphQL, or gRPC spec found on api.llmscout.com despite probing common endpoints.
  evidence:
  - status: 0
    url: https://api.llmscout.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: LLM Scout provides offline-first verification of large language model (LLM) powered system behavior before production trust or deployment. It helps teams ensure AI outputs are safe, accurate, and aligned with expectations, offering tools to test prompts, monitor responses, and enforce compliance across the development lifecycle.
layout: provider
modified: '2026-10-18'
name: LLM Scout
nav: Providers
network: true
overview: 'LLM Scout is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Verification, Safety, and Compliance.


  LLM Scout''s developer surface includes pricing, changelog, and 6 more developer resources.'
plans:
- name: Llmscout Plans Pricing
  plan_count: 3
  slug: llmscout-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 7.9
  previous_composite: 19.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/llmscout/llmscout-2026-11-03T135005.png
security:
- kind: domain-security
  name: Llmscout Domain Security
  slug: llmscout-domain-security
  summary_line: TLSv1.3
slug: llmscout
tags:
- Company
- Artificial Intelligence
- Verification
- Safety
- Compliance
website: https://llmscout.com/
---
