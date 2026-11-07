---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Meal Planner Online Agentic Access
  operation_count: 3
  slug: meal-planner-online-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Read-only subscriber API for accessing meal plans.
  name: Meal Planner Read-only API
  slug: meal-planner-read-only-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/meal-planner-online/agentic-access/meal-planner-online-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/meal-planner-online-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/meal-planner-online/plans/meal-planner-online-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/meal-planner-online-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/meal-planner-online/rules/meal-planner-online-rules.yml
  title: ''
  type: Spectral
  url: rules/meal-planner-online-rules.yml
- group: design
  href: https://artifacts.apis.io/meal-planner-online/json-ld/meal-planner-online-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/meal-planner-online-context.jsonld
- group: design
  href: https://artifacts.apis.io/meal-planner-online/vocabulary/meal-planner-online-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/meal-planner-online-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/meal-planner-online/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/meal-planner-online/data-model/meal-planner-online-data-model.yml
  title: ''
  type: DataModel
  url: data-model/meal-planner-online-data-model.yml
- group: design
  href: https://artifacts.apis.io/meal-planner-online/errors/meal-planner-online-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/meal-planner-online-problem-types.yml
- group: design
  href: https://artifacts.apis.io/meal-planner-online/conformance/meal-planner-online-conformance.yml
  title: ''
  type: Conformance
  url: conformance/meal-planner-online-conformance.yml
- group: agent
  href: https://artifacts.apis.io/meal-planner-online/llms/meal-planner-online-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/meal-planner-online-llms.txt
- group: other
  href: https://artifacts.apis.io/meal-planner-online/hosts/meal-planner-online-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meal-planner-online-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://www.meal-planner.online/login/?redirect_to=https%3A%2F%2Fwww.meal-planner.online%2Fmy-plan%2F
- group: auth
  href: https://artifacts.apis.io/meal-planner-online/authentication/meal-planner-online-authentication.yml
  title: ''
  type: Authentication
  url: authentication/meal-planner-online-authentication.yml
- group: auth
  href: https://artifacts.apis.io/meal-planner-online/security/meal-planner-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meal-planner-online-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.meal-planner.online/
- group: docs
  title: ''
  type: Documentation
  url: https://www.meal-planner.online/meal-planner-api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.meal-planner.online/meal-planner-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.meal-planner.online/weekly-meal-plan/
- group: operate
  title: ''
  type: Support
  url: https://www.meal-planner.online/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.meal-planner.online/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meal-planner.online/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meal-planner.online/privacy-policy/
created: '2026-10-30'
description: Meal Planner Online provides a family‑focused meal planning service that generates weekly dinner plans, grocery lists, and recipe suggestions. Users can access a free tier with basic plans or upgrade to a paid Plus subscription for personalized menus, Instacart grocery handoff, and additional features. The platform is built in Canada and targets real‑life cooking needs, offering multilingual support and a public API for integrations.
image: https://www.meal-planner.online/wp-content/uploads/2026/10/meal-planner-week-20261026-public.jpg
jsonld:
- class_count: 7
  name: Meal Planner Online Context
  property_count: 28
  slug: meal-planner-online-context
layout: provider
modified: '2026-10-30'
name: meal-planner-online
nav: Providers
network: true
overview: 'meal-planner-online is listed with 1 API on the [APIs.io](https://apis.io/) network: Meal Planner Read-only API. Tagged areas include Meal Planning, Family, Canada, Subscription, and Cooking.


  The meal-planner-online catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  meal-planner-online''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 16 more developer resources.'
plans:
- name: Meal Planner Online Plans Pricing
  plan_count: 3
  slug: meal-planner-online-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: meal-planner-online API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: meal-planner-online-rules
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 20.6
    developer_ergonomics: 35.0
    discoverability: 73.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/meal-planner-online/meal-planner-online-2026-11-03T135414.png
security:
- kind: authentication
  name: Meal Planner Online Authentication
  slug: meal-planner-online-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Meal Planner Online Domain Security
  slug: meal-planner-online-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: meal-planner-online-main
  slug: meal-planner-online-main
slug: meal-planner-online
tags:
- Meal Planning
- Family
- Canada
- Subscription
- Cooking
website: https://www.meal-planner.online/
---
