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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1055
  human_in_the_loop: 31
  name: Akeda Ru Agentic Access
  operation_count: 1844
  slug: akeda-ru-agentic-access
  summary_line: 1844 operations · 1055 acting · 31 human-in-the-loop
api_count: 1
apis:
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: 'Внешний контур: маршруты, которые зовёт САМА установка приложения своим краткосрочным токеном. Предъявитель здесь не человек, кабинет берётся из токена, а не из адреса, и доступ решает пересечение сог'
  name: Akeda App runtime API
  slug: akeda-ru-app-runtime-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Личные разговоры и подписные сводки встроенного помощника
  name: Akeda Assistant API
  slug: akeda-ru-assistant-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Манифест возможностей автоматизаций «когда → если → то»
  name: Akeda Automation API
  slug: akeda-ru-automation-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль calendar (события, занятость и внешняя синхронизация)
  name: Akeda Calendar API
  slug: akeda-ru-calendar-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль chat (чаты и рабочие обсуждения)
  name: Akeda Chat API
  slug: akeda-ru-chat-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники) — валюта, аналитические разрезы и закрытие периода
  name: Akeda Core accounting API
  slug: akeda-ru-core-accounting-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники) — единые статьи ДДС и ОПиУ
  name: Akeda Core accounting items API
  slug: akeda-ru-core-accounting-items-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники) — контрагенты и их роли покупателя/поставщика
  name: Akeda Core contacts API
  slug: akeda-ru-core-contacts-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники) — история, источники и обновление курсов валют
  name: Akeda Core currency rates API
  slug: akeda-ru-core-currency-rates-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники) — единый каталог, конструктор справочников и папки
  name: Akeda Core directories API
  slug: akeda-ru-core-directories-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники) — типы документов, журнал, проведение, связи и блокировки
  name: Akeda Core documents API
  slug: akeda-ru-core-documents-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники) — шаблоны приёма и увольнения, выданное имущество
  name: Akeda Core employee operations API
  slug: akeda-ru-core-employee-operations-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники) — сотрудники, оргструктура и фотографии
  name: Akeda Core employees API
  slug: akeda-ru-core-employees-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники) — соответствия внешних объектов, ручной разбор и автоматч контрагентов
  name: Akeda Core external refs API
  slug: akeda-ru-core-external-refs-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники) — разбор ОСВ 1С для предзаполнения начальных остатков
  name: Akeda Core GL opening imports API
  slug: akeda-ru-core-gl-opening-imports-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники) — план счетов, схема проводок и оборотно-сальдовая ведомость
  name: Akeda Core ledger API
  slug: akeda-ru-core-ledger-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: The Core orders API from Akeda — 3 operation(s) for core orders.
  name: Akeda Core orders API
  slug: akeda-ru-core-orders-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники) — общие настройки кабинета и персональное состояние интерфейса
  name: Akeda Core preferences API
  slug: akeda-ru-core-preferences-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники) — шаблоны, управляемый импорт и экспорт номенклатуры
  name: Akeda Core product transfers API
  slug: akeda-ru-core-product-transfers-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники) — товары, услуги, семейства, варианты и внешние идентификаторы
  name: Akeda Core products API
  slug: akeda-ru-core-products-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники) — публичный слой ссылок, каталог справочников, значения по ключу и разрешение ссылок
  name: Akeda Core reference API
  slug: akeda-ru-core-reference-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники) — определения регистров, остатки, обороты и движения
  name: Akeda Core registers API
  slug: akeda-ru-core-registers-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль core (справочники, документы и проведение) — продажи и поставщикам, статусы кабинета и загрузка
  name: Akeda Core trade API
  slug: akeda-ru-core-trade-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль crm — сводка менеджера и аналитика продаж
  name: Akeda CRM analytics API
  slug: akeda-ru-crm-analytics-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль crm — правила автоматизации, запуски и журнал действий
  name: Akeda CRM automation API
  slug: akeda-ru-crm-automation-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль crm — собственная база клиентов и перенос в справочник контрагентов ERP
  name: Akeda CRM customers API
  slug: akeda-ru-crm-customers-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль crm — сделки, доска, история стадий и причины отказа
  name: Akeda CRM deals API
  slug: akeda-ru-crm-deals-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль crm — перенос клиентов, лидов и сделок из чужих CRM и файлов
  name: Akeda CRM import API
  slug: akeda-ru-crm-import-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль crm — каналы, диалоги, переписка и шаблоны ответов
  name: Akeda CRM inbox API
  slug: akeda-ru-crm-inbox-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль crm — заявки, квалификация и перевод в сделку
  name: Akeda CRM leads API
  slug: akeda-ru-crm-leads-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль crm — заметки и связи записей с задачами, событиями и встречами
  name: Akeda CRM links API
  slug: akeda-ru-crm-links-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль crm — воронки, стадии, нормативы SLA и порядок этапов
  name: Akeda CRM pipelines API
  slug: akeda-ru-crm-pipelines-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль crm — сохранённые представления списков лидов, сделок и клиентов
  name: Akeda CRM views API
  slug: akeda-ru-crm-views-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: The Dashboard metrics API from Akeda — 3 operation(s) for dashboard metrics.
  name: Akeda Dashboard metrics API
  slug: akeda-ru-dashboard-metrics-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: 'Личный контур внешнего разработчика Akeda Apps: самостоятельная регистрация, вход по одноразовой ссылке и заявка на имя издателя. Предъявитель здесь не сотрудник кабинета и не установка приложения, а '
  name: Akeda Developer account API
  slug: akeda-ru-developer-account-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: 'Модуль docflow (документы) — действия над пакетом у оператора: подтвердить и отклонить документ, очередь этапов и аннулирование по соглашению сторон. Все операции раздела меняют состояние в боевом ЭДО'
  name: Akeda Docflow actions API
  slug: akeda-ru-docflow-actions-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: 'Модуль docflow (документы) — согласование как САМОСТОЯТЕЛЬНАЯ сущность: лист больше не часть карточки. Предмет назван нейтральной тройкой «модуль — вид — идентификатор», и внешнего ключа на него нет в'
  name: Akeda Docflow approvals API
  slug: akeda-ru-docflow-approvals-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: 'Модуль docflow (документы) — подключения юрлиц кабинета к операторам ЭДО. Учётные данные оператора не возвращаются ни одной операцией: снаружи виден только признак их наличия'
  name: Akeda Docflow connections API
  slug: akeda-ru-docflow-connections-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: 'Модуль docflow (документы) — связь бумаги с учётом: ручные связи с документами модулей финансов и склада, создание плановой операции и приёмка акта. Записывает всегда владелец через свой порт — крыло '
  name: Akeda Docflow flow accounting API
  slug: akeda-ru-docflow-flow-accounting-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: 'Модуль docflow (документы) — внутренний документооборот кабинета: карточки договоров, спецификаций и актов, их неизменяемые редакции, файлы и связи между документами. Учётного факта это крыло не созда'
  name: Akeda Docflow flow API
  slug: akeda-ru-docflow-flow-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: 'Модуль docflow (документы) — приёмка входящего формализованного документа к учёту: разбор титула продавца из вложений пакета, предложение по контрагенту и номенклатуре и подтверждение человека, из кот'
  name: Akeda Docflow intake API
  slug: akeda-ru-docflow-intake-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль docflow (документы) — зеркало документов оператора, его обновление и выдача файлов. Отправки документа контрагенту здесь нет ни одной операции
  name: Akeda Docflow mirror API
  slug: akeda-ru-docflow-mirror-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: 'Модуль docflow (документы) — исходящий формализованный документ: титул продавца по учётному документу кабинета и ответный титул покупателя на входящий пакет. Предполётная проверка ничего не меняет и н'
  name: Akeda Docflow outgoing API
  slug: akeda-ru-docflow-outgoing-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: 'Модуль docflow (документы) — заявка на оплату как документ: автор заводит её и отправляет по маршруту согласования, согласованная уходит в модуль finance (счета, выписки и расчёты) в платёжный календа'
  name: Akeda Docflow payment requests API
  slug: akeda-ru-docflow-payment-requests-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: 'Модуль docflow (документы) — раздел «Налоговая»: требования, письма и рассылки госорганов и статусы сданной отчётности из ленты отчётности оператора. Только чтение и одна локальная отметка «ответ дан»'
  name: Akeda Docflow tax API
  slug: akeda-ru-docflow-tax-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: 'Модуль docflow (документы: бумаги, ЭДО, согласование) — заказы сайта на Яндекс KIT: итог опроса API KIT и связь заказа сайта с заказом покупателя. Двери экрана «Настройки → Подключения → Яндекс KIT».'
  name: Akeda Docflow Yandex KIT API
  slug: akeda-ru-docflow-yandex-kit-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Права на папки файлового хранилища
  name: Akeda Files access API
  slug: akeda-ru-files-access-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль files (файловое хранилище кабинета)
  name: Akeda Files API
  slug: akeda-ru-files-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Скачивание файлов и выгрузка папок архивом
  name: Akeda Files content API
  slug: akeda-ru-files-content-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Внешние ссылки на файлы и папки
  name: Akeda Files shares API
  slug: akeda-ru-files-shares-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Докачиваемая загрузка файлов частями
  name: Akeda Files uploads API
  slug: akeda-ru-files-uploads-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — банковские счета и входящие остатки
  name: Akeda Finance accounts API
  slug: akeda-ru-finance-accounts-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — сверка эквайринга — деньги в пути по оплатам картой, выплаты эквайера, реестры провайдера и эквайеры юрлиц
  name: Akeda Finance acquiring API
  slug: akeda-ru-finance-acquiring-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — счета провайдера, синхронизация и журнал запусков
  name: Akeda Finance connector sync API
  slug: akeda-ru-finance-connector-sync-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — безопасное управление подключениями к банкам
  name: Akeda Finance connectors API
  slug: akeda-ru-finance-connectors-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — версионируемые коммерческие условия и позиция контрагента
  name: Akeda Finance counterparty terms API
  slug: akeda-ru-finance-counterparty-terms-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: The Finance dividends API from Akeda — 11 operation(s) for finance dividends.
  name: Akeda Finance dividends API
  slug: akeda-ru-finance-dividends-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — идемпотентный журнал обмена с внешними учётными системами
  name: Akeda Finance exchange API
  slug: akeda-ru-finance-exchange-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — управляемый импорт банковских и кассовых операций
  name: Akeda Finance imports API
  slug: akeda-ru-finance-imports-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: The Finance operations API from Akeda — 10 operation(s) for finance operations.
  name: Akeda Finance operations API
  slug: akeda-ru-finance-operations-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — форма и строки отчёта ОПиУ
  name: Akeda Finance P&L layouts API
  slug: akeda-ru-finance-p-l-layouts-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — планы, факты и прогноз движения денег
  name: Akeda Finance payment calendar API
  slug: akeda-ru-finance-payment-calendar-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — зарплатные документы, реестры выплат и загрузка ведомости
  name: Akeda Finance payroll API
  slug: akeda-ru-finance-payroll-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — пересинхронизация и сверка учётных регистров
  name: Akeda Finance registers API
  slug: akeda-ru-finance-registers-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — ДДС, ОПиУ, баланс и проверки периода
  name: Akeda Finance reports API
  slug: akeda-ru-finance-reports-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — проверка владельца, БИК и номера счёта
  name: Akeda Finance requisites API
  slug: akeda-ru-finance-requisites-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — документы долгов, авансов, продаж, закупок и распределения оплат
  name: Akeda Finance settlements API
  slug: akeda-ru-finance-settlements-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — ручные и загруженные выписки
  name: Akeda Finance statements API
  slug: akeda-ru-finance-statements-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — журнал продаж и закупок, свободные авансы
  name: Akeda Finance trade API
  slug: akeda-ru-finance-trade-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль finance (счета и выписки) — операции, категоризация и очередь сверки
  name: Akeda Finance transactions API
  slug: akeda-ru-finance-transactions-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль invitations (приглашения) — одноразовые ссылки в кабинет по почте с ролью
  name: Akeda Invitations API
  slug: akeda-ru-invitations-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль knowledge (база знаний) — состав участников пространства и страницы
  name: Akeda Knowledge access API
  slug: akeda-ru-knowledge-access-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль knowledge (база знаний) — файлы страницы и их содержимое
  name: Akeda Knowledge files API
  slug: akeda-ru-knowledge-files-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль knowledge (база знаний) — страницы, редакции, согласование, публикация и корзина
  name: Akeda Knowledge pages API
  slug: akeda-ru-knowledge-pages-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль knowledge (база знаний) — поиск по материалам и ответ с цитатами
  name: Akeda Knowledge search API
  slug: akeda-ru-knowledge-search-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль knowledge (база знаний) — пространства и дерево страниц
  name: Akeda Knowledge spaces API
  slug: akeda-ru-knowledge-spaces-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: 'Модуль mail (почта сотрудника) — подключение ящиков по IMAP и SMTP, подсказки провайдеров, папки ящика и синхронизация по требованию. Пароль подключения не возвращает ни одна операция: о нём говорит т'
  name: Akeda Mail accounts API
  slug: akeda-ru-mail-accounts-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: The Mail API from Akeda — 3 operation(s) for mail.
  name: Akeda Mail API
  slug: akeda-ru-mail-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль mail (почта сотрудника) — письма и переписки, отметки прочтения, важности и спама, перенос между папками, вложения, очередь отправки и составление письма. Письмо без признака save_as_draft вста
  name: Akeda Mail messages API
  slug: akeda-ru-mail-messages-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: 'Модуль mail (почта сотрудника) — правила разбора входящей почты и их применение к уже накопившимся письмам. Набор полей и операторов закрытый: правило исполняется на сервере над чужой перепиской'
  name: Akeda Mail rules API
  slug: akeda-ru-mail-rules-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marketplace (торговые площадки) — юрлицо магазина, источник себестоимости и передача недельного отчёта в учёт
  name: Akeda Marketplace accounting API
  slug: akeda-ru-marketplace-accounting-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marketplace (торговые площадки) — загрузка каталога магазина в номенклатуру кабинета и сопоставление его карточек с товарами
  name: Akeda Marketplace catalog API
  slug: akeda-ru-marketplace-catalog-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marketplace (торговые площадки) — витрины Ozon и расчёт юнит-экономики
  name: Akeda Marketplace Ozon API
  slug: akeda-ru-marketplace-ozon-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marketplace (торговые площадки) — группы товаров Ozon и Wildberries
  name: Akeda Marketplace product groups API
  slug: akeda-ru-marketplace-product-groups-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marketplace (торговые площадки) — магазины Ozon, Wildberries и Яндекс.Маркета
  name: Akeda Marketplace stores API
  slug: akeda-ru-marketplace-stores-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marketplace (торговые площадки) — отгрузки на маркетплейс и расхождения приёмки поставок
  name: Akeda Marketplace supplies API
  slug: akeda-ru-marketplace-supplies-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marketplace (торговые площадки) — время в разделах по кабинету — порядок и доля плиток листа «Площадки», сводка использования разделов
  name: Akeda Marketplace usage API
  slug: akeda-ru-marketplace-usage-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marketplace (торговые площадки) — витрины Wildberries и карточка товара
  name: Akeda Marketplace Wildberries API
  slug: akeda-ru-marketplace-wildberries-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marketplace (торговые площадки) — витрины Яндекс.Маркета
  name: Akeda Marketplace Yandex API
  slug: akeda-ru-marketplace-yandex-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marking (маркировка «Честный знак») — короба (КИТУ, SSCC) — сборка, этикетка, отчёты агрегации и состав
  name: Akeda Marking boxes API
  slug: akeda-ru-marking-boxes-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marking (маркировка «Честный знак») — реестр кодов, их разбор и проверка в ГИС МТ
  name: Akeda Marking codes API
  slug: akeda-ru-marking-codes-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marking (маркировка «Честный знак») — подключение юрлиц к ГИС МТ и СУЗ, баланс и места деятельности
  name: Akeda Marking connections API
  slug: akeda-ru-marking-connections-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marking (маркировка «Честный знак») — входящие документы ГИС МТ, черновики и исходящие
  name: Akeda Marking GIS MT documents API
  slug: akeda-ru-marking-gis-mt-documents-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marking (маркировка «Честный знак») — печать этикеток и шаблоны
  name: Akeda Marking labels API
  slug: akeda-ru-marking-labels-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marking (маркировка «Честный знак») — заказы кодов в СУЗ
  name: Akeda Marking orders API
  slug: akeda-ru-marking-orders-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marking (маркировка «Честный знак») — профиль маркировки товара
  name: Akeda Marking products API
  slug: akeda-ru-marking-products-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marking (маркировка «Честный знак») — товарные группы юрлиц и настройки маркировки юрлица
  name: Akeda Marking settings API
  slug: akeda-ru-marking-settings-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль marking (маркировка «Честный знак») — коды маркировки в складских документах
  name: Akeda Marking stock documents API
  slug: akeda-ru-marking-stock-documents-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль settings (участники, роли, юрлица) — юрлица кабинета, метод учёта и ставки НДС
  name: Akeda Settings companies API
  slug: akeda-ru-settings-companies-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль settings (участники, роли, юрлица) — дополнительные поля карточек
  name: Akeda Settings fields API
  slug: akeda-ru-settings-fields-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: 'Модуль settings (настройки кабинета) — подключения к торговым платформам и службам доставки, которые не маркетплейсы (Яндекс KIT, Ozon Retail, СДЭК): проверка ключей у платформы, включённость и настро'
  name: Akeda Settings integrations API
  slug: akeda-ru-settings-integrations-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль settings (участники, роли, юрлица) — участники кабинета
  name: Akeda Settings members API
  slug: akeda-ru-settings-members-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль settings (участники, роли, юрлица) — роли, их носители и перенос носителей
  name: Akeda Settings roles API
  slug: akeda-ru-settings-roles-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль stock (склад) — версионируемый состав изделия для комплектации и разукомплектации
  name: Akeda Stock assembly specs API
  slug: akeda-ru-stock-assembly-specs-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль stock (склад) — партии
  name: Akeda Stock batches API
  slug: akeda-ru-stock-batches-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль stock (склад) — журнал складских документов, проведение, отмена, связи и блокировки
  name: Akeda Stock documents API
  slug: akeda-ru-stock-documents-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль stock (склад) — выгрузка данных файлом
  name: Akeda Stock exports API
  slug: akeda-ru-stock-exports-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль stock (склад) — физические единицы хранения, их состояние и подсказки размещения
  name: Akeda Stock handling units API
  slug: akeda-ru-stock-handling-units-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль stock (склад) — загрузка данных файлом, разбор, соответствие колонок, предпросмотр и применение
  name: Akeda Stock imports API
  slug: akeda-ru-stock-imports-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль stock (склад) — инвентаризация, снимок остатков, ведомость пересчёта и производные акты
  name: Akeda Stock inventory API
  slug: akeda-ru-stock-inventory-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль stock (склад) — единицы измерения товара и их пересчёт
  name: Akeda Stock product units API
  slug: akeda-ru-stock-product-units-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль stock (склад) — закупки
  name: Akeda Stock purchasing API
  slug: akeda-ru-stock-purchasing-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль stock (склад) — справочные выборки склада, юрлица кабинета и поставщики
  name: Akeda Stock references API
  slug: akeda-ru-stock-references-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль stock (склад) — правила пополнения
  name: Akeda Stock reorder rules API
  slug: akeda-ru-stock-reorder-rules-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль stock (склад) — отчёты по остаткам, закупкам и резервам
  name: Akeda Stock reports API
  slug: akeda-ru-stock-reports-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль stock (склад) — настройки склада и учётные политики юрлиц
  name: Akeda Stock settings API
  slug: akeda-ru-stock-settings-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль stock (склад) — расчёт себестоимости, предпросмотр и асинхронный пересчёт
  name: Akeda Stock valuation API
  slug: akeda-ru-stock-valuation-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль stock (склад) — склады, их активность и блокировки деактивации
  name: Akeda Stock warehouses API
  slug: akeda-ru-stock-warehouses-api
- baseURL: https://erp.akeda.ru
  baseurl_source: declared
  description: Модуль tasks (задачник)
  name: Akeda Tasks API
  slug: akeda-ru-tasks-api
artifact_total: 132
asyncapis:
- description: ''
  name: Akeda Ru Webhooks
  slug: akeda-ru-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/akeda-ru/agentic-access/akeda-ru-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/akeda-ru-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/akeda-ru/rules/akeda-ru-rules.yml
  title: ''
  type: Spectral
  url: rules/akeda-ru-rules.yml
- group: design
  href: https://artifacts.apis.io/akeda-ru/json-ld/akeda-ru-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/akeda-ru-context.jsonld
- group: design
  href: https://artifacts.apis.io/akeda-ru/vocabulary/akeda-ru-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/akeda-ru-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/akeda-ru/asyncapi/akeda-ru-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/akeda-ru-webhooks.yml
- group: design
  href: https://artifacts.apis.io/akeda-ru/data-model/akeda-ru-data-model.yml
  title: ''
  type: DataModel
  url: data-model/akeda-ru-data-model.yml
- group: design
  href: https://artifacts.apis.io/akeda-ru/conventions/akeda-ru-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/akeda-ru-conventions.yml
- group: design
  href: https://artifacts.apis.io/akeda-ru/conventions/akeda-ru-conventions.yml
  title: ''
  type: Conventions
  url: conventions/akeda-ru-conventions.yml
- group: design
  href: https://artifacts.apis.io/akeda-ru/errors/akeda-ru-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/akeda-ru-problem-types.yml
- group: design
  href: https://artifacts.apis.io/akeda-ru/conformance/akeda-ru-conformance.yml
  title: ''
  type: Conformance
  url: conformance/akeda-ru-conformance.yml
- group: agent
  href: https://artifacts.apis.io/akeda-ru/llms/akeda-ru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/akeda-ru-llms.txt
- group: agent
  href: https://artifacts.apis.io/akeda-ru/well-known/akeda-ru-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/akeda-ru-well-known.yml
- group: other
  href: https://artifacts.apis.io/akeda-ru/hosts/akeda-ru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/akeda-ru-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://app.akeda.ru/security
- group: start
  title: ''
  type: Login
  url: https://app.akeda.ru/auth/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.akeda.ru/
- group: auth
  href: https://artifacts.apis.io/akeda-ru/scopes/akeda-ru-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/akeda-ru-scopes.yml
- group: auth
  href: https://artifacts.apis.io/akeda-ru/authentication/akeda-ru-authentication.yml
  title: ''
  type: Authentication
  url: authentication/akeda-ru-authentication.yml
- group: auth
  href: https://artifacts.apis.io/akeda-ru/security/akeda-ru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/akeda-ru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://akeda.ru/
- group: docs
  title: ''
  type: Documentation
  url: https://akeda.ru/docs/akeda-erp/
- group: commercial
  title: ''
  type: Pricing
  url: https://akeda.ru/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://akeda.ru/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://akeda.ru/privacy/
- group: company
  title: ''
  type: Blog
  url: https://akeda.ru/articles/
created: '2026-11-01'
description: Akeda — российская IT‑компания, разрабатывающая ERP‑системы и AI‑решения для автоматизации бизнеса. Компания предлагает модульную ERP‑платформу Akeda ERP, интеграцию с 1С, CRM, BI‑дашбордами и более 100 AI‑моделей через единый REST‑API и MCP. Основана в августе 2026 года, обслуживает клиентов в России и странах СНГ, предоставляя решения для производства, финансового учёта, управления процессами и клиентских порталов.
image: https://akeda.ru/assets/akeda-social-card.png
json_schemas:
- name: CoreSalesChannel
  property_count: 43
  slug: akeda-ru-core-sales-channel
- name: CRMInboxLineInput
  property_count: 40
  slug: akeda-ru-crminbox-line-input
- name: CRMInboxLine
  property_count: 43
  slug: akeda-ru-crminbox-line
- name: DocflowMessage
  property_count: 51
  slug: akeda-ru-docflow-message
- name: MarketplaceStore
  property_count: 36
  slug: akeda-ru-marketplace-store
- name: StockSettings
  property_count: 22
  slug: akeda-ru-stock-settings
jsonld:
- class_count: 120
  name: Akeda Ru Context
  property_count: 331
  slug: akeda-ru-context
layout: provider
modified: '2026-11-01'
name: Akeda
nav: Providers
network: true
overview: 'Akeda publishes 119 API contracts indexed on the [APIs.io](https://apis.io/) network, including App runtime API, Assistant API, Automation API, and 116 more. Tagged areas include ERP, Automation, Artificial Intelligence, Business, and Russia.


  The Akeda catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Akeda''s developer surface includes authentication, documentation, pricing, engineering blog, and 21 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Akeda API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 2
  slug: akeda-ru-rules
scopes:
- name: Akeda Ru Scopes
  scope_count: 1
  slug: akeda-ru-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 71.5
    developer_ergonomics: 22.6
    discoverability: 66.1
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - russia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 119
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Akeda Ru Authentication
  slug: akeda-ru-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Akeda Ru Domain Security
  slug: akeda-ru-domain-security
  summary_line: TLSv1.3 · DMARC
slug: akeda-ru
tags:
- ERP
- Automation
- Artificial Intelligence
- Business
- Russia
website: https://akeda.ru/
---
