---
access_model:
  confidence: high
  label: Freemium, self-serve — REST API gated to the paid Profi plan
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - https://appsmax.ru/pricing/
  - https://appsmax.ru/.well-known/api-onboarding
  trial: true
  try_now: false
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-09-05'
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
artifact_total: 27
collections:
- collection_type: postman
  name: AppsMax REST API v1 — Quickstart
  slug: postman-appsmax-rest-api-v1-quickstart
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: X-MCPServerCandidate
  url: mcp/appsmax-rest-api-v1-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/appsmax-rest-api-v1-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appsmax-rest-api-v1-domain-security.yml
- group: auth
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
  title: ''
  type: Conventions
  url: conventions/appsmax-rest-api-v1-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/appsmax-rest-api-v1-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/appsmax-rest-api-v1-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/appsmax-rest-api-v1-lifecycle.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/appsmax-rest-api-v1-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/appsmax-rest-api-v1-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/appsmax-rest-api-v1-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/appsmax-rest-api-v1-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/appsmax-rest-api-v1-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appsmax-rest-api-v1-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/appsmax-rest-api-v1-rest-api-v1-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/appsmax-rest-api-v1-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/appsmax-rest-api-v1-plans.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/appsmax-rest-api-v1-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://gitverse.ru/appsmax/appsmax-api-reference
created: '2026-07-31'
description: AppsMax.ru is a Russian-language SaaS platform for small business, communities and integrators, used to run customer requests, online booking, orders, mini apps, groups, channels, permitted messaging, GigaChat and integrations inside MAX and Telegram. Its developer surface is a single server-to-server REST API (v1) with a published OpenAPI 3.0.3 contract, an APIs.json index, an API Onboarding Descriptor and an llms.txt. AppsMax is not a product of, nor an official representative of, MAX, Telegram or GigaChat.
image: https://appsmax.ru/wp-content/themes/appsmax-site/assets/img/logo-appsmax.svg
layout: provider
modified: '2026-08-09'
name: AppsMax
nav: Providers
network: true
overview: 'AppsMax publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Access API, Applications API, Bots API, and 6 more. Tagged areas include Company, Software-as-a-Service, Messaging, Business Automation, and Chatbots.


  AppsMax''s developer surface includes authentication, API reference, engineering blog, signup flow, FAQ, code examples, and 27 more developer resources.'
plans:
- name: Appsmax Rest Api V1 Plans
  plan_count: 5
  slug: appsmax-rest-api-v1-plans
random_paper: 18
rate_limits:
- limit_count: 3
  name: Appsmax Rest Api V1 Rate Limits
  slug: appsmax-rest-api-v1-rate-limits
scopes:
- name: Appsmax Rest Api V1 Scopes
  scope_count: 12
  slug: appsmax-rest-api-v1-scopes
  summary_line: 12 scopes
score:
  band: strong
  composite: 56.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 56.7
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 47.4
  previous_composite: 56.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appsmax-rest-api-v1/refs/heads/main/screenshots/appsmax-rest-api-v1-2026-08-17T080613.png
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
slug: appsmax-rest-api-v1
tags:
- Company
- Software-as-a-Service
- Messaging
- Business Automation
- Chatbots
- Mini Apps
- Customer Requests
- Workflow-Automation
- MAX
- Telegram
- Russian Language
website: https://appsmax.ru/
---
