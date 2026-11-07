---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 18.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation is available but no machine‑readable contract (OpenAPI/GraphQL/AsyncAPI) was found.
  name: Dukon AI API
  slug: dukon-ai-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/dukonai-com/plans/dukonai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dukonai-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dukonai-com/well-known/dukonai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dukonai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dukonai-com/hosts/dukonai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dukonai-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dukonai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dukonai.com/privacy
- group: auth
  href: https://artifacts.apis.io/dukonai-com/security/dukonai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dukonai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dukonai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dukonai.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://dukonai.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://dukonai.com/docs#start
- group: operate
  title: ''
  type: Support
  url: https://dukonai.com/account
coverage:
  checked: '2026-11-06'
  detail: Documentation is publicly available at https://dukonai.com/docs but no machine‑readable API contract (OpenAPI, GraphQL, AsyncAPI) could be found.
  evidence:
  - status: 200
    url: https://dukonai.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: Dukon AI provides an AI-powered integration that connects your BILLZ accounting system to Claude and ChatGPT, enabling natural language queries for revenue, profit, inventory, and reports. It offers a free 20‑day trial with no credit card required, and multiple pricing plans in USD and UZS.
image: https://dukonai.com/assets/apple-touch-icon.png
layout: provider
modified: '2026-11-06'
name: Dukon AI
nav: Providers
network: true
overview: 'Dukon AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Dukon AI''s developer surface includes documentation, pricing, getting-started guide, support, and 7 more developer resources.'
plans:
- name: Dukonai Com Plans Pricing
  plan_count: 2
  slug: dukonai-com-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dukonai Com Domain Security
  slug: dukonai-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dukonai-com
tags:
- Company
website: https://dukonai.com/
---
