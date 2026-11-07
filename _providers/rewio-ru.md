---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Rewio Ru Agentic Access
  operation_count: 53
  slug: rewio-ru-agentic-access
  summary_line: 53 operations · 28 acting
api_count: 1
apis:
- baseURL: https://api.rewio.ru
  baseurl_source: declared
  description: 'Агрегированная аналитика по отзывам объекта: сводка и динамика.'
  name: rewio-ru Analytics API
  slug: rewio-ru-analytics-api
- baseURL: https://api.rewio.ru
  baseurl_source: declared
  description: 'Жалобы на отзывы: форма площадки, подача и итог. Отзыв называете вы, форму – площадка (Яндекс – текст, 2ГИС – категория и текст, Google – категория).'
  name: rewio-ru Complaints API
  slug: rewio-ru-complaints-api
- baseURL: https://api.rewio.ru
  baseurl_source: declared
  description: Папки объектов. Позволяют запросить отзывы сразу по нескольким объектам одним параметром `folder_id` – см. `GET /v3/reviews` и `GET /v3/analytics`.
  name: rewio-ru Folders API
  slug: rewio-ru-folders-api
- baseURL: https://api.rewio.ru
  baseurl_source: declared
  description: 'Доступность API. Ключ не нужен: оба метода отвечают и без заголовка `X-API-Key`, поэтому им удобно отделять проблему с сетью от проблемы с ключом.'
  name: rewio-ru Health API
  slug: rewio-ru-health-api
- baseURL: https://api.rewio.ru
  baseurl_source: declared
  description: Скрытие ненужных и закрепление нужных отзывов внутри объекта; сами отзывы не меняются.
  name: rewio-ru hidden & pinned API
  slug: rewio-ru-hidden-pinned-api
- baseURL: https://api.rewio.ru
  baseurl_source: declared
  description: Ссылки внутри объекта – страницы объекта на площадках, по одной на площадку. Добавление, изменение и удаление ссылок, статус сбора отзывов.
  name: rewio-ru Links API
  slug: rewio-ru-links-api
- baseURL: https://api.rewio.ru
  baseurl_source: declared
  description: Объекты – единицы бизнеса, отзывы по которым собираются (филиал, клиника, конкретный специалист). Создание, просмотр, изменение и удаление объектов.
  name: rewio-ru Objects API
  slug: rewio-ru-objects-api
- baseURL: https://api.rewio.ru
  baseurl_source: declared
  description: 'Ответы на отзывы от лица организации: публикация, замена и удаление. Форма запроса одна для всех площадок.'
  name: rewio-ru Replies API
  slug: rewio-ru-replies-api
- baseURL: https://api.rewio.ru
  baseurl_source: declared
  description: Нормализованные отзывы объекта с фильтрацией, сортировкой и пагинацией.
  name: rewio-ru Reviews API
  slug: rewio-ru-reviews-api
- baseURL: https://api.rewio.ru
  baseurl_source: declared
  description: Список поддерживаемых площадок отзывов.
  name: rewio-ru Sources API
  slug: rewio-ru-sources-api
- baseURL: https://api.rewio.ru
  baseurl_source: declared
  description: 'Написать в поддержку: вопрос по API, ошибка, просьба. Работает с любым ключом, включая `read_only`. Номер аккаунта, почта и тариф подставляются сами – писать их в тексте не нужно.'
  name: rewio-ru Support API
  slug: rewio-ru-support-api
- baseURL: https://api.rewio.ru
  baseurl_source: declared
  description: 'Вебхуки: уведомления о новых отзывах, новых ответах и завершении сбора. **Быстрый старт:** 1. `POST /v3/webhooks` с `{"target": "https://...", "event_types": ["reviews.new"]}` – создать вебхук. 2. `PO'
  name: rewio-ru Webhooks API
  slug: rewio-ru-webhooks-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/rewio-ru/agentic-access/rewio-ru-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rewio-ru-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/rewio-ru/rules/rewio-ru-rules.yml
  title: ''
  type: Spectral
  url: rules/rewio-ru-rules.yml
- group: design
  href: https://artifacts.apis.io/rewio-ru/json-ld/rewio-ru-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rewio-ru-context.jsonld
- group: design
  href: https://artifacts.apis.io/rewio-ru/vocabulary/rewio-ru-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rewio-ru-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/rewio-ru/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/rewio-ru/data-model/rewio-ru-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rewio-ru-data-model.yml
- group: auth
  href: https://artifacts.apis.io/rewio-ru/authentication/rewio-ru-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rewio-ru-authentication.yml
- group: design
  href: https://artifacts.apis.io/rewio-ru/errors/rewio-ru-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rewio-ru-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rewio-ru/conformance/rewio-ru-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rewio-ru-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rewio-ru/llms/rewio-ru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rewio-ru-llms.txt
- group: other
  href: https://artifacts.apis.io/rewio-ru/hosts/rewio-ru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rewio-ru-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rewio.ru/
- group: start
  title: ''
  type: Login
  url: https://app.rewio.ru/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rewio.ru**\n\n
- group: auth
  href: https://artifacts.apis.io/rewio-ru/security/rewio-ru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rewio-ru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rewio.ru/
- group: docs
  title: ''
  type: Documentation
  url: https://api.rewio.ru/v2/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.rewio.ru/v2/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://rewio.ru/api-otzyvov/
- group: commercial
  title: ''
  type: Pricing
  url: https://rewio.ru/#pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rewio.ru/privacy.html
- group: operate
  title: ''
  type: Support
  url: mailto:info@rewio.ru
created: '2026-10-31'
description: Rewio provides a review aggregation service and API for collecting reviews from Yandex Maps, 2GIS, Google and over 35 other platforms. It gathers reviews multiple times per day, offers response publishing, complaint handling, and analytics. Pricing starts from 48 RUB per object per month.
image: https://rewio.ru/logo.png
json_schemas:
- name: ComplaintV3
  property_count: 11
  slug: rewio-ru-complaint-v3
- name: FolderWriteV3
  property_count: 10
  slug: rewio-ru-folder-write-v3
- name: ObjectRefreshV3
  property_count: 11
  slug: rewio-ru-object-refresh-v3
- name: ObjectV3
  property_count: 9
  slug: rewio-ru-object-v3
- name: ReplyStateV3
  property_count: 5
  slug: rewio-ru-reply-state-v3
- name: ReviewV3
  property_count: 28
  slug: rewio-ru-review-v3
jsonld:
- class_count: 80
  name: Rewio Ru Context
  property_count: 158
  slug: rewio-ru-context
layout: provider
modified: '2026-10-31'
name: rewio-ru
nav: Providers
network: true
overview: 'rewio-ru publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Complaints API, Folders API, and 9 more. Tagged areas include Reviews, Aggregation, Russian, and Maps.


  The rewio-ru catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  rewio-ru''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, support, and 16 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: rewio-ru API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: rewio-ru-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 58.3
    developer_ergonomics: 42.1
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rewio-ru/rewio-ru-2026-11-03T142345.png
security:
- kind: authentication
  name: Rewio Ru Authentication
  slug: rewio-ru-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Rewio Ru Domain Security
  slug: rewio-ru-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: create-object
  slug: rewio-ru-create-object
- name: get-reviews
  slug: rewio-ru-get-reviews
slug: rewio-ru
tags:
- Reviews
- Aggregation
- Russian
- Maps
website: https://rewio.ru/
---
