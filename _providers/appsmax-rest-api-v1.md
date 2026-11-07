---
access_model:
  confidence: high
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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Appsmax Rest Api V1 Agentic Access
  operation_count: 21
  slug: appsmax-rest-api-v1-agentic-access
  summary_line: 21 operations · 6 acting
api_count: 1
apis:
- baseURL: https://telegram.appsmax.ru/api/v1
  baseurl_source: declared
  description: Проверка токена и контекста организации.
  name: AppsMax Access API
  slug: appsmax-rest-api-v1-access-api
- baseURL: https://telegram.appsmax.ru/api/v1
  baseurl_source: declared
  description: Заявки и их теги.
  name: AppsMax Applications API
  slug: appsmax-rest-api-v1-applications-api
- baseURL: https://telegram.appsmax.ru/api/v1
  baseurl_source: declared
  description: Боты и их безопасные сведения о подключении без секретов.
  name: AppsMax Bots API
  slug: appsmax-rest-api-v1-bots-api
- baseURL: https://telegram.appsmax.ru/api/v1
  baseurl_source: declared
  description: Рассылки и их запуск.
  name: AppsMax Campaigns API
  slug: appsmax-rest-api-v1-campaigns-api
- baseURL: https://telegram.appsmax.ru/api/v1
  baseurl_source: declared
  description: Сценарии и воронки ботов.
  name: AppsMax Funnels API
  slug: appsmax-rest-api-v1-funnels-api
- baseURL: https://telegram.appsmax.ru/api/v1
  baseurl_source: declared
  description: Элементы интерактивного меню ботов.
  name: AppsMax Interactive menu API
  slug: appsmax-rest-api-v1-interactive-menu-api
- baseURL: https://telegram.appsmax.ru/api/v1
  baseurl_source: declared
  description: Мини-приложения организации.
  name: AppsMax Miniapps API
  slug: appsmax-rest-api-v1-miniapps-api
- baseURL: https://telegram.appsmax.ru/api/v1
  baseurl_source: declared
  description: Организация, к которой привязан токен.
  name: AppsMax Organizations API
  slug: appsmax-rest-api-v1-organizations-api
- baseURL: https://telegram.appsmax.ru/api/v1
  baseurl_source: declared
  description: Подписчики и их сегментационные теги.
  name: AppsMax Subscribers API
  slug: appsmax-rest-api-v1-subscribers-api
artifact_total: 32
collections:
- collection_type: postman
  name: AppsMax REST API v1 — Quickstart
  slug: postman-appsmax-rest-api-v1-quickstart
- collection_type: open
  name: AppsMax REST Access API
  slug: open-appsmax-rest-api-v1-access-api
- collection_type: open
  name: AppsMax REST Applications API
  slug: open-appsmax-rest-api-v1-applications-api
- collection_type: open
  name: AppsMax REST Bots API
  slug: open-appsmax-rest-api-v1-bots-api
- collection_type: open
  name: AppsMax REST Campaigns API
  slug: open-appsmax-rest-api-v1-campaigns-api
- collection_type: open
  name: AppsMax REST Funnels API
  slug: open-appsmax-rest-api-v1-funnels-api
- collection_type: open
  name: AppsMax REST Interactive menu API
  slug: open-appsmax-rest-api-v1-interactive-menu-api
- collection_type: open
  name: AppsMax REST Miniapps API
  slug: open-appsmax-rest-api-v1-miniapps-api
- collection_type: open
  name: AppsMax REST Organizations API
  slug: open-appsmax-rest-api-v1-organizations-api
- collection_type: open
  name: AppsMax REST Subscribers API
  slug: open-appsmax-rest-api-v1-subscribers-api
common:
- group: agent
  href: https://artifacts.apis.io/appsmax-rest-api-v1/mcp/appsmax-rest-api-v1-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/appsmax-rest-api-v1-mcp.yml
- group: agent
  href: https://artifacts.apis.io/appsmax-rest-api-v1/agentic-access/appsmax-rest-api-v1-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/appsmax-rest-api-v1-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/appsmax-rest-api-v1/security/appsmax-rest-api-v1-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appsmax-rest-api-v1-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/appsmax-rest-api-v1/authentication/appsmax-rest-api-v1-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appsmax-rest-api-v1-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://appsmax.ru/
- group: other
  title: ''
  type: APIsJSON
  url: https://appsmax.ru/apis.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://appsmax.ru/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://appsmax.ru/developers/#methods
- group: company
  title: ''
  type: Blog
  url: https://appsmax.ru/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://appsmax.ru/news/feed/
- group: start
  title: ''
  type: SignUp
  url: https://telegram.appsmax.ru/register
- group: start
  title: ''
  type: Login
  url: https://telegram.appsmax.ru/login
- group: operate
  title: ''
  type: HelpCenter
  url: https://appsmax.ru/kb/
- group: operate
  title: ''
  type: FAQ
  url: https://appsmax.ru/faq/
- group: build
  title: ''
  type: SourceCode
  url: https://gitverse.ru/appsmax/appsmax-api-reference
- group: build
  title: ''
  type: Postman
  url: https://gitverse.ru/appsmax/appsmax-api-reference
- group: design
  href: https://artifacts.apis.io/appsmax-rest-api-v1/conventions/appsmax-rest-api-v1-conventions.yml
  title: ''
  type: Conventions
  url: conventions/appsmax-rest-api-v1-conventions.yml
- group: design
  href: https://artifacts.apis.io/appsmax-rest-api-v1/conventions/appsmax-rest-api-v1-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/appsmax-rest-api-v1-conventions.yml
- group: design
  href: https://artifacts.apis.io/appsmax-rest-api-v1/errors/appsmax-rest-api-v1-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/appsmax-rest-api-v1-problem-types.yml
- group: design
  href: https://artifacts.apis.io/appsmax-rest-api-v1/lifecycle/appsmax-rest-api-v1-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/appsmax-rest-api-v1-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/appsmax-rest-api-v1/scopes/appsmax-rest-api-v1-scopes.yml
  title: ''
  type: Scopes
  url: scopes/appsmax-rest-api-v1-scopes.yml
- group: design
  href: https://artifacts.apis.io/appsmax-rest-api-v1/conformance/appsmax-rest-api-v1-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appsmax-rest-api-v1-conformance.yml
- group: design
  href: https://artifacts.apis.io/appsmax-rest-api-v1/data-model/appsmax-rest-api-v1-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appsmax-rest-api-v1-data-model.yml
- group: build
  href: https://artifacts.apis.io/appsmax-rest-api-v1/packages/appsmax-rest-api-v1-packages.yml
  title: ''
  type: Packages
  url: packages/appsmax-rest-api-v1-packages.yml
- group: agent
  href: https://artifacts.apis.io/appsmax-rest-api-v1/well-known/appsmax-rest-api-v1-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appsmax-rest-api-v1-well-known.yml
- group: agent
  href: https://artifacts.apis.io/appsmax-rest-api-v1/llms/appsmax-rest-api-v1-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appsmax-rest-api-v1-llms.txt
- group: other
  href: https://artifacts.apis.io/appsmax-rest-api-v1/overlays/appsmax-rest-api-v1-rest-api-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appsmax-rest-api-v1-rest-api-v1-overlay.yaml
- group: build
  href: https://artifacts.apis.io/appsmax-rest-api-v1/examples/_index.yml
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  href: https://artifacts.apis.io/appsmax-rest-api-v1/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/appsmax-rest-api-v1/rate-limits/appsmax-rest-api-v1-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/appsmax-rest-api-v1-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/appsmax-rest-api-v1/plans/appsmax-rest-api-v1-plans.yml
  title: ''
  type: Plans
  url: plans/appsmax-rest-api-v1-plans.yml
- group: auth
  href: https://artifacts.apis.io/appsmax-rest-api-v1/security/appsmax-rest-api-v1-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/appsmax-rest-api-v1-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://gitverse.ru/appsmax/appsmax-api-reference
created: '2026-07-31'
description: AppsMax.ru is a Russian-language SaaS platform for small business, communities and integrators, used to run customer requests, online booking, orders, mini apps, groups, channels, permitted messaging, GigaChat and integrations inside MAX and Telegram. Its developer surface is a single server-to-server REST API (v1) with a published OpenAPI 3.0.3 contract, an APIs.json index, an API Onboarding Descriptor and an llms.txt. AppsMax is not a product of, nor an official representative of, MAX, Telegram or GigaChat.
finops:
- has_sources: true
  method: derived
  name: Appsmax Rest Api V1 Finops
  primary_unit: subscription
  service_category: ''
  slug: appsmax-rest-api-v1-finops
  template: false
image: https://appsmax.ru/wp-content/themes/appsmax-site/assets/img/logo-appsmax.svg
layout: provider
modified: '2026-08-09'
name: AppsMax
nav: Providers
network: true
overview: 'AppsMax publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access API, Applications API, Bots API, and 6 more. Tagged areas include Company, Software-as-a-Service, Messaging, Business Automation, and Chatbots.


  The AppsMax catalog on APIs.io includes 1 Spectral governance ruleset.


  AppsMax''s developer surface includes authentication, API reference, engineering blog, signup flow, FAQ, code examples, and 27 more developer resources.'
plans:
- name: Appsmax Rest Api V1 Plans
  plan_count: 5
  slug: appsmax-rest-api-v1-plans
random_paper: 0
rate_limits:
- limit_count: 3
  name: Appsmax Rest Api V1 Rate Limits
  slug: appsmax-rest-api-v1-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: AppsMax API Rules
  rule_count: 65
  severity_counts:
    error: 61
    hint: 0
    info: 3
    warn: 1
  slug: appsmax-rest-api-v1-rules
scopes:
- name: Appsmax Rest Api V1 Scopes
  scope_count: 12
  slug: appsmax-rest-api-v1-scopes
  summary_line: 12 scopes
score:
  band: strong
  composite: 65.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 53.3
    developer_ergonomics: 63.7
    discoverability: 73.2
    operational_transparency: 47.4
  previous_composite: 63.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/appsmax-rest-api-v1/appsmax-rest-api-v1-2026-08-17T080613.png
security:
- kind: authentication
  name: Appsmax Rest Api V1 Authentication
  slug: appsmax-rest-api-v1-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Appsmax Rest Api V1 Domain Security
  slug: appsmax-rest-api-v1-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Appsmax Rest Api V1 Vulnerability Disclosure
  slug: appsmax-rest-api-v1-vulnerability-disclosure
  summary_line: Hackerone · contact published
skill_count: 4
skills:
- name: Capture a customer request into AppsMax
  slug: appsmax-rest-api-v1-capture-customer-request
- name: Draft and launch an AppsMax campaign
  slug: appsmax-rest-api-v1-draft-and-launch-campaign
- name: Inventory an AppsMax bot estate
  slug: appsmax-rest-api-v1-inventory-bot-estate
- name: Sync subscribers into AppsMax
  slug: appsmax-rest-api-v1-sync-subscribers
slug: appsmax-rest-api-v1
tags:
- Company
- Software-as-a-Service
- Messaging
- Business Automation
- Chatbots
- Mini Apps
- Customer Requests
- Workflow Automation
- MAX
- Telegram
- Russian Language
website: https://appsmax.ru/
---
