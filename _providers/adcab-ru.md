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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation for AdCab advertising connector
  name: AdCab API
  slug: adcab-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/adcab-ru/plans/adcab-ru-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adcab-ru-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/adcab-ru/authentication/adcab-ru-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adcab-ru-authentication.yml
- group: agent
  href: https://artifacts.apis.io/adcab-ru/llms/adcab-ru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adcab-ru-llms.txt
- group: agent
  href: https://artifacts.apis.io/adcab-ru/well-known/adcab-ru-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adcab-ru-well-known.yml
- group: other
  href: https://artifacts.apis.io/adcab-ru/hosts/adcab-ru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adcab-ru-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adcab.ru/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://adcab.ru/pricing
- group: start
  title: ''
  type: Login
  url: https://adcab.ru/login
- group: docs
  title: ''
  type: Documentation
  url: https://adcab.ru/docs
- group: company
  title: ''
  type: Blog
  url: https://adcab.ru/blog
- group: auth
  href: https://artifacts.apis.io/adcab-ru/security/adcab-ru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adcab-ru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adcab.ru/
coverage:
  checked: '2026-10-31'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://adcab.ru/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 'AdCab (Адкаб) — коннектор MCP: подключите рекламные кабинеты Яндекс Директа, VK и Авито к Claude или ChatGPT. Сбор семантики, запуск кампаний, статистика и чистка площадок РСЯ прямо в чате. Любое изменение применяется только после вашего подтверждения.'
image: https://adcab.ru/og.png
layout: provider
modified: '2026-10-31'
name: AdCab
nav: Providers
network: true
overview: 'AdCab is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Artificial Intelligence, Marketing, Russian, and Integration.


  AdCab''s developer surface includes authentication, pricing, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Adcab Ru Plans Pricing
  plan_count: 4
  slug: adcab-ru-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 23.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adcab Ru Authentication
  slug: adcab-ru-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adcab Ru Domain Security
  slug: adcab-ru-domain-security
  summary_line: TLSv1.3
slug: adcab-ru
tags:
- Advertising
- Artificial Intelligence
- Marketing
- Russian
- Integration
website: https://adcab.ru/
---
