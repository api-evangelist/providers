---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
- description: Best for personal diet management and food service professionals. Type your ingredients in natural language and get instant, comprehensive nutritional analysis with 26 nutrients.
  name: Nutrition Analysis API
  slug: nutrition-analysis-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/nutridatax/plans/nutridatax-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nutridatax-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/nutridatax/llms/nutridatax-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nutridatax-llms.txt
- group: other
  href: https://artifacts.apis.io/nutridatax/hosts/nutridatax-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nutridatax-hosts.yml
- group: other
  href: https://artifacts.apis.io/nutridatax/vendors/nutridatax-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nutridatax-vendors.yml
- group: auth
  href: https://artifacts.apis.io/nutridatax/security/nutridatax-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nutridatax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nutridatax.com/
- group: docs
  title: ''
  type: Documentation
  url: https://nutridatax.com/products/nutrition-analysis
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nutridatax.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://nutridatax.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://nutridatax.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://nutridatax.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nutridatax.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nutridatax.com/privacy
coverage:
  checked: '2026-10-18'
  detail: Documentation pages render as a JavaScript shell with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://nutridatax.com/products/nutrition-analysis
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-17'
description: NutriDataX provides AI‑powered nutrition data services, including recipe analysis, meal‑plan generation, ingredient breakdowns, and food‑intelligence tools for both home cooks and professional developers. Their platform offers eight distinct APIs covering nutrition analysis, ingredient search, diet recommendations, grocery list creation, food‑label parsing, recipe suggestions, meal‑planning optimization, and health‑impact scoring, all accessible via REST with robust authentication and rate‑limit controls.
image: https://nutridatax.com/__l5e/assets-v1/493aac31-3c83-4c35-b594-39e575123e9c/nutridatax-og-share.jpg
layout: provider
modified: '2026-10-17'
name: NutriDataX
nav: Providers
network: true
overview: 'NutriDataX is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nutrition, Food Data, and Artificial Intelligence.


  NutriDataX''s developer surface includes documentation, pricing, engineering blog, signup flow, and 9 more developer resources.'
plans:
- name: Nutridatax Plans Pricing
  plan_count: 2
  slug: nutridatax-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 22.6
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nutridatax/nutridatax-2026-11-03T140353.png
security:
- kind: domain-security
  name: Nutridatax Domain Security
  slug: nutridatax-domain-security
  summary_line: TLSv1.3 · HSTS
slug: nutridatax
tags:
- Company
- Nutrition
- Food Data
- Artificial Intelligence
website: https://nutridatax.com/
---
