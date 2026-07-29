---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 173
  human_in_the_loop: 2
  name: Avito Agentic Access
  operation_count: 248
  slug: avito-agentic-access
  summary_line: 248 operations · 173 acting · 2 human-in-the-loop
api_count: 51
apis:
- description: Для работы с API от своего лица необходимо получить токен авторизации — отдельный для каждой учетной записи на Авито. 1. Получаем **client_id** и **client_secret** в [личном кабинете](https://www.avit
  name: Avito Access API
  slug: avito-access-api
- description: The Ads API from Avito — 23 operation(s) for ads.
  name: Avito Ads API
  slug: avito-ads-api
- description: Для работы с API приложений от лица пользователя есть возможность получить токен через Authorization Code механизм протокола OAuth2. Для этого в первую очередь нужно зарегистрировать приложение на htt
  name: Avito ApplicationAccess API
  slug: avito-applicationaccess-api
- description: The Auction API from Avito — 1 operation(s) for auction.
  name: Avito Auction API
  slug: avito-auction-api
- description: The Authorization API from Avito — 1 operation(s) for authorization.
  name: Avito Authorization API
  slug: avito-authorization-api
- description: Методы API для получения информации об автозагрузке объявлений
  name: Avito Autoload API
  slug: avito-autoload-api
- description: API для работы с автостратегией в категории
  name: Avito Autostrategy API
  slug: avito-autostrategy-api
- description: 'С помощью API данного раздела вы можете получить информацию о балансе средств агентства и всех операций с ним. ### Типы авторизации Для использования данного API запрос должен быть авторизован. API Ав'
  name: Avito balance API
  slug: avito-balance-api
- description: The Call API from Avito — 4 operation(s) for call.
  name: Avito Call API
  slug: avito-call-api
- description: The Calltracking API from Avito — 3 operation(s) for calltracking.
  name: Avito Calltracking API
  slug: avito-calltracking-api
- description: The Chat API from Avito — 4 operation(s) for chat.
  name: Avito Chat API
  slug: avito-chat-api
- description: The CheckAhUserV1 API from Avito — 1 operation(s) for checkahuserv1.
  name: Avito CheckAhUserV1 API
  slug: avito-checkahuserv1-api
- description: The CheckAhUserV2 API from Avito — 1 operation(s) for checkahuserv2.
  name: Avito CheckAhUserV2 API
  slug: avito-checkahuserv2-api
- description: The Core API from Avito — 1 operation(s) for core.
  name: Avito Core API
  slug: avito-core-api
- description: '# Методы для работы с сервисом CPA Описание API произведено в формате [**Swagger 3.0**](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md). Вы можете использовать данный файл '
  name: Avito Cpa API
  slug: avito-cpa-api
- description: The Cpxpromo API from Avito — 5 operation(s) for cpxpromo.
  name: Avito Cpxpromo API
  slug: avito-cpxpromo-api
- description: The DeliverySandbox API from Avito — 9 operation(s) for deliverysandbox.
  name: Avito DeliverySandbox API
  slug: avito-deliverysandbox-api
- description: The DeliveryTariffication API from Avito — 3 operation(s) for deliverytariffication.
  name: Avito DeliveryTariffication API
  slug: avito-deliverytariffication-api
- description: The Evaluation API from Avito — 5 operation(s) for evaluation.
  name: Avito Evaluation API
  slug: avito-evaluation-api
- description: The GetAhInfoV1 API from Avito — 1 operation(s) for getahinfov1.
  name: Avito GetAhInfoV1 API
  slug: avito-getahinfov1-api
- description: The GetEmployeesV1 API from Avito — 1 operation(s) for getemployeesv1.
  name: Avito GetEmployeesV1 API
  slug: avito-getemployeesv1-api
- description: С помощью API данного раздела вы можете приглашать в агентство новых клиентов. [Отправьте](#operation/agencyUsersInviteSend) приглашение новому клиенту и получите идентификатор приглашения. Затем по и
  name: Avito invite API
  slug: avito-invite-api
- description: Общие методы API для работы с объявлениями на Авито Описание API произведено в формате [**Swagger 3.0**](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md). Вы можете использо
  name: Avito Item API
  slug: avito-item-api
- description: API для размещения, редактирования и снятия с публикации вакансии Авито Работа Описание API произведено в формате [**Swagger 3.0**](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.
  name: Avito Job API
  slug: avito-job-api
- description: The LinkItemsV1 API from Avito — 1 operation(s) for linkitemsv1.
  name: Avito LinkItemsV1 API
  slug: avito-linkitemsv1-api
- description: The ListCompanyPhonesV1 API from Avito — 1 operation(s) for listcompanyphonesv1.
  name: Avito ListCompanyPhonesV1 API
  slug: avito-listcompanyphonesv1-api
- description: The ListItemsByEmployeeIdV1 API from Avito — 1 operation(s) for listitemsbyemployeeidv1.
  name: Avito ListItemsByEmployeeIdV1 API
  slug: avito-listitemsbyemployeeidv1-api
- description: API для интеграции между мессенджером Авито и сторонней системой в обе стороны.
  name: Avito Messenger API
  slug: avito-messenger-api
- description: The OfflineMonitoring API from Avito — 4 operation(s) for offlinemonitoring.
  name: Avito OfflineMonitoring API
  slug: avito-offlinemonitoring-api
- description: The Order Management API from Avito — 12 operation(s) for order management.
  name: Avito Order Management API
  slug: avito-order-management-api
- description: The ParcelProcessing API from Avito — 9 operation(s) for parcelprocessing.
  name: Avito ParcelProcessing API
  slug: avito-parcelprocessing-api
- description: 'С помощью API данного раздела вы можете получать актуальную информацию о клиентах агентства. ### Типы авторизации Для использования данного API запрос должен быть авторизован. API Авито Promo использу'
  name: Avito profile API
  slug: avito-profile-api
- description: Общее API для чтения информации об услугах продвижения.
  name: Avito Promotion API
  slug: avito-promotion-api
- description: API для управления услугой "Продвижение с прогнозом".
  name: Avito Promotion_BBIP API
  slug: avito-promotion-bbip-api
- description: API для работы с рейтингами и отзывами
  name: Avito Ratings API
  slug: avito-ratings-api
- description: The Realty API from Avito — 7 operation(s) for realty.
  name: Avito Realty API
  slug: avito-realty-api
- description: The ReferenceData API from Avito — 2 operation(s) for referencedata.
  name: Avito ReferenceData API
  slug: avito-referencedata-api
- description: The Report API from Avito — 10 operation(s) for report.
  name: Avito Report API
  slug: avito-report-api
- description: The RisksAssessment API from Avito — 2 operation(s) for risksassessment.
  name: Avito RisksAssessment API
  slug: avito-risksassessment-api
- description: The Signal API from Avito — 1 operation(s) for signal.
  name: Avito Signal API
  slug: avito-signal-api
- description: The SpecialOffers API from Avito — 5 operation(s) for specialoffers.
  name: Avito SpecialOffers API
  slug: avito-specialoffers-api
- description: 'С помощью API данного раздела вы можете получать статистику по объявлениям и расходам клиентов. ### Типы авторизации Для использования данного API запрос должен быть авторизован. API Авито Promo испол'
  name: Avito statistics API
  slug: avito-statistics-api
- description: The Stock Management API from Avito — 2 operation(s) for stock management.
  name: Avito Stock Management API
  slug: avito-stock-management-api
- description: С помощью API данного раздела вы можете узнать статус клиентов, проверив их ИНН. За клиентов в статусе «Новый» или «Аплифт» агентству выплачивается комиссия. Подробные правила указаны в соглашении о п
  name: Avito targeting API
  slug: avito-targeting-api
- description: API для работы с Тарифами
  name: Avito Tariff API
  slug: avito-tariff-api
- description: The Teaser API from Avito — 2 operation(s) for teaser.
  name: Avito Teaser API
  slug: avito-teaser-api
- description: The TerminalManagement API from Avito — 3 operation(s) for terminalmanagement.
  name: Avito TerminalManagement API
  slug: avito-terminalmanagement-api
- description: С помощью API данного раздела вы можете выполнять переводы средств клиентам и отслеживать транзакции. [Выполните](#operation/agencyBalance) перевод средств на счёт клиента и получите идентификатор тра
  name: Avito transactions API
  slug: avito-transactions-api
- description: The Trx Promo API from Avito — 3 operation(s) for trx promo.
  name: Avito Trx Promo API
  slug: avito-trx-promo-api
- description: '# API для получения баланса кошелька пользователя, истории операций и инфорации об авторизованном пользователе Описание API произведено в формате [**Swagger 3.0**](https://github.com/OAI/OpenAPI-Speci'
  name: Avito User API
  slug: avito-user-api
- description: The XDelivery API from Avito — 7 operation(s) for xdelivery.
  name: Avito XDelivery API
  slug: avito-xdelivery-api
artifact_total: 57
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avito-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/avito-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/avito-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/avito-authentication.yml
- group: company
  title: ''
  type: Website
  url: http://www.avito.ru
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.avito.ru/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.avito.ru/api-catalog
- group: docs
  title: ''
  type: APIReference
  url: https://developers.avito.ru/api-catalog
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.avito.ru/about-api
- group: auth
  title: ''
  type: Authorization
  url: https://developers.avito.ru/api-catalog/auth/documentation
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.avito.ru/api-updates
- group: operate
  title: ''
  type: Support
  url: https://support.avito.ru/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avito.ru/legal/pro_tools/public-api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avito.ru/safety/personal/company
- group: start
  title: ''
  type: SignUp
  url: https://developers.avito.ru/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/avito-tech
- group: other
  title: ''
  type: Business
  url: https://www.avito.ru/business
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/avito-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/avito-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/avito-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/avito-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/avito-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/avito-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/avito-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avito-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/avito-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/avito-manage-listings.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/avito-respond-in-messenger.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/avito-autoload-feed.md
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-accounts-hierarchy-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-ads-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-auction-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-auth-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-autoload-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-autostrategy-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-autoteka-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-calltracking-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-cpa-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-cpxpromo-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-delivery-sandbox-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-item-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-job-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-messenger-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-order-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-promo-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-promotion-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-ratings-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-realty-reports-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-sbc-gateway-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-stock-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-str-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-tariff-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-trxpromo-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avito-user-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: openapi/avito-messenger-openapi.json
created: '2026-07-17'
description: Avito is Russia's largest online classifieds platform (avito.ru), founded in 2007, where individuals and businesses buy and sell across goods, vehicles, real estate, jobs and services. For business sellers and integrators Avito publishes a public Developer Portal (developers.avito.ru) exposing 25 OpenAPI 3.0.0 REST APIs on api.avito.ru covering item/listing management, autoload feed ingestion, the buyer-seller messenger, delivery, order and stock management, ratings and reviews, advertising and CPA/promotion campaigns, short-term rental, jobs (Avito.Rabota), and Autoteka vehicle history. All APIs use OAuth 2.0 (authorization_code for acting on behalf of users, client_credentials for a business's own account) with scoped access and per-minute rate limiting.
image: https://m.avito.ru/icons/open-graph-default.svg
layout: provider
mcp_servers:
- description: ''
  name: avito-mcp.yml
  slug: avito-mcpyml
modified: '2026-07-18'
name: Avito
nav: Providers
network: true
overview: 'Avito publishes 51 APIs on the [APIs.io](https://apis.io/) network, including Access API, Ads API, ApplicationAccess API, and 48 more. Tagged areas include Company, Consumer, Classifieds, Marketplace, and E-commerce.


  Avito''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, support, signup flow, and 49 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 1
  name: Avito Rate Limits
  slug: avito-rate-limits
scopes:
- name: Avito Scopes
  scope_count: 26
  slug: avito-scopes
  summary_line: 26 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 50.4
  delta: 1.5
  facets:
    commercial_clarity: 34.2
    contract_quality: 59.9
    developer_ergonomics: 53.8
    discoverability: 74.1
    governance: 20.8
    operational_transparency: 50.0
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: unknown
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 51
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 58.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/avito/refs/heads/main/screenshots/avito-2026-07-25T201949.png
security:
- kind: authentication
  name: Avito Authentication
  slug: avito-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Avito Domain Security
  slug: avito-domain-security
  summary_line: TLSv1.3 · DMARC
slug: avito
tags:
- Company
- Consumer
- Classifieds
- Marketplace
- E-commerce
- Real Estate
- Automotive
- Jobs
- Advertising
- Messaging
- Delivery
- Russia
website: http://www.avito.ru
---
