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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 173
  human_in_the_loop: 2
  name: Avito Agentic Access
  operation_count: 248
  slug: avito-agentic-access
  summary_line: 248 operations · 173 acting · 2 human-in-the-loop
api_count: 25
apis:
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: Для работы с API от своего лица необходимо получить токен авторизации — отдельный для каждой учетной записи на Авито. 1. Получаем **client_id** и **client_secret** в [личном кабинете](https://www.avit
  name: Avito Access API
  slug: avito-access-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The Ads API from Avito — 23 operation(s) for ads.
  name: Avito Ads API
  slug: avito-ads-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: Для работы с API приложений от лица пользователя есть возможность получить токен через Authorization Code механизм протокола OAuth2. Для этого в первую очередь нужно зарегистрировать приложение на htt
  name: Avito ApplicationAccess API
  slug: avito-applicationaccess-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The Auction API from Avito — 1 operation(s) for auction.
  name: Avito Auction API
  slug: avito-auction-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The Authorization API from Avito — 1 operation(s) for authorization.
  name: Avito Authorization API
  slug: avito-authorization-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: Методы API для получения информации об автозагрузке объявлений
  name: Avito Autoload API
  slug: avito-autoload-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: API для работы с автостратегией в категории
  name: Avito Autostrategy API
  slug: avito-autostrategy-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: 'С помощью API данного раздела вы можете получить информацию о балансе средств агентства и всех операций с ним. ### Типы авторизации Для использования данного API запрос должен быть авторизован. API Ав'
  name: Avito balance API
  slug: avito-balance-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The Call API from Avito — 4 operation(s) for call.
  name: Avito Call API
  slug: avito-call-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The Calltracking API from Avito — 3 operation(s) for calltracking.
  name: Avito Calltracking API
  slug: avito-calltracking-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The Chat API from Avito — 4 operation(s) for chat.
  name: Avito Chat API
  slug: avito-chat-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The CheckAhUserV1 API from Avito — 1 operation(s) for checkahuserv1.
  name: Avito CheckAhUserV1 API
  slug: avito-checkahuserv1-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The CheckAhUserV2 API from Avito — 1 operation(s) for checkahuserv2.
  name: Avito CheckAhUserV2 API
  slug: avito-checkahuserv2-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The Core API from Avito — 1 operation(s) for core.
  name: Avito Core API
  slug: avito-core-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: '# Методы для работы с сервисом CPA Описание API произведено в формате [**Swagger 3.0**](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md). Вы можете использовать данный файл '
  name: Avito Cpa API
  slug: avito-cpa-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The Cpxpromo API from Avito — 5 operation(s) for cpxpromo.
  name: Avito Cpxpromo API
  slug: avito-cpxpromo-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The DeliverySandbox API from Avito — 9 operation(s) for deliverysandbox.
  name: Avito DeliverySandbox API
  slug: avito-deliverysandbox-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The DeliveryTariffication API from Avito — 3 operation(s) for deliverytariffication.
  name: Avito DeliveryTariffication API
  slug: avito-deliverytariffication-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The Evaluation API from Avito — 5 operation(s) for evaluation.
  name: Avito Evaluation API
  slug: avito-evaluation-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The GetAhInfoV1 API from Avito — 1 operation(s) for getahinfov1.
  name: Avito GetAhInfoV1 API
  slug: avito-getahinfov1-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The GetEmployeesV1 API from Avito — 1 operation(s) for getemployeesv1.
  name: Avito GetEmployeesV1 API
  slug: avito-getemployeesv1-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: С помощью API данного раздела вы можете приглашать в агентство новых клиентов. [Отправьте](#operation/agencyUsersInviteSend) приглашение новому клиенту и получите идентификатор приглашения. Затем по и
  name: Avito invite API
  slug: avito-invite-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: Общие методы API для работы с объявлениями на Авито Описание API произведено в формате [**Swagger 3.0**](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md). Вы можете использо
  name: Avito Item API
  slug: avito-item-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: API для размещения, редактирования и снятия с публикации вакансии Авито Работа Описание API произведено в формате [**Swagger 3.0**](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.
  name: Avito Job API
  slug: avito-job-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The LinkItemsV1 API from Avito — 1 operation(s) for linkitemsv1.
  name: Avito LinkItemsV1 API
  slug: avito-linkitemsv1-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The ListCompanyPhonesV1 API from Avito — 1 operation(s) for listcompanyphonesv1.
  name: Avito ListCompanyPhonesV1 API
  slug: avito-listcompanyphonesv1-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The ListItemsByEmployeeIdV1 API from Avito — 1 operation(s) for listitemsbyemployeeidv1.
  name: Avito ListItemsByEmployeeIdV1 API
  slug: avito-listitemsbyemployeeidv1-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: API для интеграции между мессенджером Авито и сторонней системой в обе стороны.
  name: Avito Messenger API
  slug: avito-messenger-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The OfflineMonitoring API from Avito — 4 operation(s) for offlinemonitoring.
  name: Avito OfflineMonitoring API
  slug: avito-offlinemonitoring-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The Order Management API from Avito — 12 operation(s) for order management.
  name: Avito Order Management API
  slug: avito-order-management-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The ParcelProcessing API from Avito — 9 operation(s) for parcelprocessing.
  name: Avito ParcelProcessing API
  slug: avito-parcelprocessing-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: 'С помощью API данного раздела вы можете получать актуальную информацию о клиентах агентства. ### Типы авторизации Для использования данного API запрос должен быть авторизован. API Авито Promo использу'
  name: Avito profile API
  slug: avito-profile-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: Общее API для чтения информации об услугах продвижения.
  name: Avito Promotion API
  slug: avito-promotion-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: API для управления услугой "Продвижение с прогнозом".
  name: Avito Promotion_BBIP API
  slug: avito-promotion-bbip-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: API для работы с рейтингами и отзывами
  name: Avito Ratings API
  slug: avito-ratings-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The Realty API from Avito — 7 operation(s) for realty.
  name: Avito Realty API
  slug: avito-realty-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The ReferenceData API from Avito — 2 operation(s) for referencedata.
  name: Avito ReferenceData API
  slug: avito-referencedata-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The Report API from Avito — 10 operation(s) for report.
  name: Avito Report API
  slug: avito-report-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The RisksAssessment API from Avito — 2 operation(s) for risksassessment.
  name: Avito RisksAssessment API
  slug: avito-risksassessment-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The Signal API from Avito — 1 operation(s) for signal.
  name: Avito Signal API
  slug: avito-signal-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The SpecialOffers API from Avito — 5 operation(s) for specialoffers.
  name: Avito SpecialOffers API
  slug: avito-specialoffers-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: 'С помощью API данного раздела вы можете получать статистику по объявлениям и расходам клиентов. ### Типы авторизации Для использования данного API запрос должен быть авторизован. API Авито Promo испол'
  name: Avito statistics API
  slug: avito-statistics-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The Stock Management API from Avito — 2 operation(s) for stock management.
  name: Avito Stock Management API
  slug: avito-stock-management-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: С помощью API данного раздела вы можете узнать статус клиентов, проверив их ИНН. За клиентов в статусе «Новый» или «Аплифт» агентству выплачивается комиссия. Подробные правила указаны в соглашении о п
  name: Avito targeting API
  slug: avito-targeting-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: API для работы с Тарифами
  name: Avito Tariff API
  slug: avito-tariff-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The Teaser API from Avito — 2 operation(s) for teaser.
  name: Avito Teaser API
  slug: avito-teaser-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The TerminalManagement API from Avito — 3 operation(s) for terminalmanagement.
  name: Avito TerminalManagement API
  slug: avito-terminalmanagement-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: С помощью API данного раздела вы можете выполнять переводы средств клиентам и отслеживать транзакции. [Выполните](#operation/agencyBalance) перевод средств на счёт клиента и получите идентификатор тра
  name: Avito transactions API
  slug: avito-transactions-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The Trx Promo API from Avito — 3 operation(s) for trx promo.
  name: Avito Trx Promo API
  slug: avito-trx-promo-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: '# API для получения баланса кошелька пользователя, истории операций и инфорации об авторизованном пользователе Описание API произведено в формате [**Swagger 3.0**](https://github.com/OAI/OpenAPI-Speci'
  name: Avito User API
  slug: avito-user-api
- baseURL: https://api.avito.ru/
  baseurl_source: declared
  description: The XDelivery API from Avito — 7 operation(s) for xdelivery.
  name: Avito XDelivery API
  slug: avito-xdelivery-api
artifact_total: 109
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Иерархия Аккаунтов Access API
  slug: open-avito-access-api
- collection_type: open
  name: Иерархия Аккаунтов Access Ads API
  slug: open-avito-ads-api
- collection_type: open
  name: Иерархия Аккаунтов Access ApplicationAccess API
  slug: open-avito-applicationaccess-api
- collection_type: open
  name: Иерархия Аккаунтов Access Auction API
  slug: open-avito-auction-api
- collection_type: open
  name: Иерархия Аккаунтов Access Authorization API
  slug: open-avito-authorization-api
- collection_type: open
  name: Иерархия Аккаунтов Access Autoload API
  slug: open-avito-autoload-api
- collection_type: open
  name: Иерархия Аккаунтов Access Autostrategy API
  slug: open-avito-autostrategy-api
- collection_type: open
  name: Иерархия Аккаунтов Access balance API
  slug: open-avito-balance-api
- collection_type: open
  name: Иерархия Аккаунтов Access Call API
  slug: open-avito-call-api
- collection_type: open
  name: Иерархия Аккаунтов Access Calltracking API
  slug: open-avito-calltracking-api
- collection_type: open
  name: Иерархия Аккаунтов Access Chat API
  slug: open-avito-chat-api
- collection_type: open
  name: Иерархия Аккаунтов Access CheckAhUserV1 API
  slug: open-avito-checkahuserv1-api
- collection_type: open
  name: Иерархия Аккаунтов Access CheckAhUserV2 API
  slug: open-avito-checkahuserv2-api
- collection_type: open
  name: Иерархия Аккаунтов Access Core API
  slug: open-avito-core-api
- collection_type: open
  name: Иерархия Аккаунтов Access Cpa API
  slug: open-avito-cpa-api
- collection_type: open
  name: Иерархия Аккаунтов Access Cpxpromo API
  slug: open-avito-cpxpromo-api
- collection_type: open
  name: Иерархия Аккаунтов Access DeliverySandbox API
  slug: open-avito-deliverysandbox-api
- collection_type: open
  name: Иерархия Аккаунтов Access DeliveryTariffication API
  slug: open-avito-deliverytariffication-api
- collection_type: open
  name: Иерархия Аккаунтов Access Evaluation API
  slug: open-avito-evaluation-api
- collection_type: open
  name: Иерархия Аккаунтов Access GetAhInfoV1 API
  slug: open-avito-getahinfov1-api
- collection_type: open
  name: Иерархия Аккаунтов Access GetEmployeesV1 API
  slug: open-avito-getemployeesv1-api
- collection_type: open
  name: Иерархия Аккаунтов Access invite API
  slug: open-avito-invite-api
- collection_type: open
  name: Иерархия Аккаунтов Access Item API
  slug: open-avito-item-api
- collection_type: open
  name: Иерархия Аккаунтов Access Job API
  slug: open-avito-job-api
- collection_type: open
  name: Иерархия Аккаунтов Access LinkItemsV1 API
  slug: open-avito-linkitemsv1-api
- collection_type: open
  name: Иерархия Аккаунтов Access ListCompanyPhonesV1 API
  slug: open-avito-listcompanyphonesv1-api
- collection_type: open
  name: Иерархия Аккаунтов Access ListItemsByEmployeeIdV1 API
  slug: open-avito-listitemsbyemployeeidv1-api
- collection_type: open
  name: Иерархия Аккаунтов Access Messenger API
  slug: open-avito-messenger-api
- collection_type: open
  name: Иерархия Аккаунтов Access OfflineMonitoring API
  slug: open-avito-offlinemonitoring-api
- collection_type: open
  name: Иерархия Аккаунтов Access Order Management API
  slug: open-avito-order-management-api
- collection_type: open
  name: Иерархия Аккаунтов Access ParcelProcessing API
  slug: open-avito-parcelprocessing-api
- collection_type: open
  name: Иерархия Аккаунтов Access profile API
  slug: open-avito-profile-api
- collection_type: open
  name: Иерархия Аккаунтов Access Promotion API
  slug: open-avito-promotion-api
- collection_type: open
  name: Иерархия Аккаунтов Access Promotion_BBIP API
  slug: open-avito-promotion-bbip-api
- collection_type: open
  name: Иерархия Аккаунтов Access Ratings API
  slug: open-avito-ratings-api
- collection_type: open
  name: Иерархия Аккаунтов Access Realty API
  slug: open-avito-realty-api
- collection_type: open
  name: Иерархия Аккаунтов Access ReferenceData API
  slug: open-avito-referencedata-api
- collection_type: open
  name: Иерархия Аккаунтов Access Report API
  slug: open-avito-report-api
- collection_type: open
  name: Иерархия Аккаунтов Access RisksAssessment API
  slug: open-avito-risksassessment-api
- collection_type: open
  name: Иерархия Аккаунтов Access Signal API
  slug: open-avito-signal-api
- collection_type: open
  name: Иерархия Аккаунтов Access SpecialOffers API
  slug: open-avito-specialoffers-api
- collection_type: open
  name: Иерархия Аккаунтов Access statistics API
  slug: open-avito-statistics-api
- collection_type: open
  name: Иерархия Аккаунтов Access Stock Management API
  slug: open-avito-stock-management-api
- collection_type: open
  name: Иерархия Аккаунтов Access targeting API
  slug: open-avito-targeting-api
- collection_type: open
  name: Иерархия Аккаунтов Access Tariff API
  slug: open-avito-tariff-api
- collection_type: open
  name: Иерархия Аккаунтов Access Teaser API
  slug: open-avito-teaser-api
- collection_type: open
  name: Иерархия Аккаунтов Access TerminalManagement API
  slug: open-avito-terminalmanagement-api
- collection_type: open
  name: Иерархия Аккаунтов Access transactions API
  slug: open-avito-transactions-api
- collection_type: open
  name: Иерархия Аккаунтов Access Trx Promo API
  slug: open-avito-trx-promo-api
- collection_type: open
  name: Иерархия Аккаунтов Access User API
  slug: open-avito-user-api
- collection_type: open
  name: Иерархия Аккаунтов Access XDelivery API
  slug: open-avito-xdelivery-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/avito-capability-edges.yml
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
  url: openapi/_original/avito-messenger-openapi.json
created: '2026-07-17'
description: Avito is Russia's largest online classifieds platform (avito.ru), founded in 2007, where individuals and businesses buy and sell across goods, vehicles, real estate, jobs and services. For business sellers and integrators Avito publishes a public Developer Portal (developers.avito.ru) exposing 25 OpenAPI 3.0.0 REST APIs on api.avito.ru covering item/listing management, autoload feed ingestion, the buyer-seller messenger, delivery, order and stock management, ratings and reviews, advertising and CPA/promotion campaigns, short-term rental, jobs (Avito.Rabota), and Autoteka vehicle history. All APIs use OAuth 2.0 (authorization_code for acting on behalf of users, client_credentials for a business's own account) with scoped access and per-minute rate limiting.
image: https://m.avito.ru/icons/open-graph-default.svg
layout: provider
mcp_servers:
- description: ''
  name: Avito MCP Server
  slug: avito-mcp-server
modified: '2026-07-18'
name: Avito
nav: Providers
network: true
overview: 'Avito publishes 51 APIs on the [APIs.io](https://apis.io/) network, including Access API, Ads API, ApplicationAccess API, and 48 more. Tagged areas include Company, Consumer, Classifieds, Marketplace, and E-Commerce.


  Avito''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, support, signup flow, and 50 more developer resources.'
random_paper: 1
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
  composite: 48.2
  coverage:
    artifact_dirs: 19
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 54.3
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 48.2
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- E-Commerce
- Real-Estate
- Automotive
- Job
- Advertising
- Messaging
- Delivery
- Russia
website: http://www.avito.ru
---
