---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The single first-party API behind the Adgager platform and the dash.adgager.com client dashboard. A Laravel Lighthouse GraphQL endpoint exposing 118 queries and 141 mutations over the platform''s core '
  name: Adgager GraphQL API
  slug: adgager-graphql
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/adgager/rate-limits/adgager-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adgager-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://www.adgager.com/
- group: start
  title: ''
  type: Login
  url: https://dash.adgager.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://dash.adgager.com/en/adq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adgager.com/en/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adgager.com/en/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.adgager.com/en/contact/
- group: company
  title: ''
  type: Blog
  url: https://blog.adgager.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.adgager.com/feed/
- group: agent
  href: https://artifacts.apis.io/adgager/llms/adgager-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adgager-llms.txt
- group: commercial
  href: https://artifacts.apis.io/adgager/plans/adgager-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adgager-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/adgager/lifecycle/adgager-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/adgager-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/adgager/security/adgager-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adgager-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/adgager/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/adgager/packages/adgager-packages.yml
  title: ''
  type: Packages
  url: packages/adgager-packages.yml
created: '2026-09-07'
description: Adgager is an Istanbul-based market research platform founded in 2016 with support from Istanbul Technical University (ITU). It runs end-to-end research studies for brands over a verified member community ("Gagers"), combining survey, mobile-community (ADTEAMS), neuroscience and ethnographic methods with an AI-assisted analysis stack. Its AdQ product scores advertising effectiveness across traditional and digital channels and benchmarks a brand against category, competitor and market averages. Clients run projects, target groups, question groups and reports through the dashboard at dash.adgager.com, which is backed by a single first-party GraphQL API at api.adgager.com/graphql (Laravel Lighthouse, Sanctum bearer auth). Adgager reports serving 200+ brands including L'Oreal, Nestle, Bioderma, ING Bank, Reckitt Benckiser and Oriflame.
image: https://www.adgager.com/wp-content/uploads/2023/09/adgager-logo-1.png
layout: provider
modified: '2026-09-07'
name: Adgager
nav: Providers
network: true
overview: 'Adgager is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Market Research, Consumer Insights, Surveys, and Advertising.


  Adgager''s developer surface includes pricing, support, engineering blog, and 12 more developer resources.'
plans:
- name: Adgager Plans Pricing
  plan_count: 8
  slug: adgager-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Adgager Rate Limits
  slug: adgager-rate-limits
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 69.7
    contract_governance: 4.5
    contract_quality: 35.1
    developer_ergonomics: 20.8
    discoverability: 73.2
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - turkey
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 38.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/adgager/adgager-2026-10-11T092756.png
security:
- kind: authentication
  name: Adgager Authentication
  slug: adgager-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Adgager Domain Security
  slug: adgager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: adgager-read-adq-scores
  slug: adgager-read-adq-scores
- name: adgager-run-a-research-project
  slug: adgager-run-a-research-project
slug: adgager
tags:
- Company
- Market Research
- Consumer Insights
- Surveys
- Advertising
- Advertising Effectiveness
- Brand Measurement
- Panel
- GraphQL
- Turkey
website: https://www.adgager.com/
---
