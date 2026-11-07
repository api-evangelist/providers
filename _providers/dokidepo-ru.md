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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/dokidepo-ru/plans/dokidepo-ru-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dokidepo-ru-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dokidepo-ru/llms/dokidepo-ru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dokidepo-ru-llms.txt
- group: other
  href: https://artifacts.apis.io/dokidepo-ru/hosts/dokidepo-ru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dokidepo-ru-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://dokidepo.ru/support/
- group: auth
  href: https://artifacts.apis.io/dokidepo-ru/security/dokidepo-ru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dokidepo-ru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dokidepo.ru/
- group: docs
  title: ''
  type: Documentation
  url: https://dokidepo.ru/tools/
- group: start
  title: ''
  type: GettingStarted
  url: https://dokidepo.ru/free-warehouse/
- group: commercial
  title: ''
  type: Pricing
  url: https://dokidepo.ru/pricing/
- group: docs
  title: ''
  type: APIReference
  url: https://dokidepo.ru/tools/catalog.json
coverage:
  checked: '2026-11-06'
  detail: Documentation pages exist but no machine‑readable OpenAPI/AsyncAPI/GraphQL contract was found.
  evidence:
  - status: 200
    url: https://dokidepo.ru/guides/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: 'ДокиДепо – это онлайн‑склад с интерактивной картой, позволяющий бесплатно печатать ценники, этикетки, сравнивать таблицы и рассчитывать закупки. Сервис предлагает набор бесплатных бизнес‑инструментов: генератор артикулов, баланс склада, публикацию товаров и интеграцию с поставщиками. Всё без регистрации, доступно в веб‑интерфейсе и через публичный API, описанный в каталоге открытых инструментов.'
layout: provider
modified: '2026-11-06'
name: ДокиДепо
nav: Providers
network: true
overview: 'ДокиДепо is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Warehouse, BusinessTools, and Free.


  ДокиДепо''s developer surface includes support, documentation, getting-started guide, pricing, API reference, and 5 more developer resources.'
plans:
- name: Dokidepo Ru Plans Pricing
  plan_count: 1
  slug: dokidepo-ru-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 28.0
    catalog_earned_first_party: 8.0
    catalog_gap: 87.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dokidepo Ru Domain Security
  slug: dokidepo-ru-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dokidepo-ru
tags:
- Company
- Warehouse
- BusinessTools
- Free
website: https://dokidepo.ru/
---
