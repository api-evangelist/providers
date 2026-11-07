---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Free REST API for product discovery.
  name: AppBoard API
  slug: appboard-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/appboard-pro/plans/appboard-pro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appboard-pro-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/appboard-pro/llms/appboard-pro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appboard-pro-llms.txt
- group: other
  href: https://artifacts.apis.io/appboard-pro/hosts/appboard-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appboard-pro-hosts.yml
- group: other
  href: https://artifacts.apis.io/appboard-pro/vendors/appboard-pro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appboard-pro-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appboard.pro/terms/
- group: operate
  title: ''
  type: Support
  url: https://appboard.pro/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appboard.pro/privacy/
- group: start
  title: ''
  type: Login
  url: https://appboard.pro/login/
- group: auth
  href: https://artifacts.apis.io/appboard-pro/security/appboard-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appboard-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appboard.pro/
- group: docs
  title: ''
  type: Documentation
  url: https://appboard.pro/api-docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://appboard.pro/pricing/
coverage:
  checked: '2026-11-01'
  detail: API documentation page renders via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://appboard.pro/api-docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AppBoard is a free product discovery platform that helps creators launch, rank, and grow their software through community engagement. It offers a REST API for product discovery, allowing searches, trending data, and category vocabularies. The service provides free API keys, rate limits, and aims to surface great software without gatekeepers.
image: https://appboard.pro/og.png
layout: provider
modified: '2026-11-01'
name: AppBoard
nav: Providers
network: true
overview: 'AppBoard is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Product Discovery, Free, and Community.


  AppBoard''s developer surface includes support, documentation, pricing, and 9 more developer resources.'
plans:
- name: Appboard Pro Plans Pricing
  plan_count: 4
  slug: appboard-pro-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 23.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appboard Pro Domain Security
  slug: appboard-pro-domain-security
  summary_line: TLSv1.3 · DMARC
slug: appboard-pro
tags:
- Company
- Product Discovery
- Free
- Community
website: https://appboard.pro/
---
