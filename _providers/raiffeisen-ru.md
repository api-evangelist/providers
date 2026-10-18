---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 193
  human_in_the_loop: 28
  name: Raiffeisen Ru Agentic Access
  operation_count: 449
  slug: raiffeisen-ru-agentic-access
  summary_line: 449 operations · 193 acting · 28 human-in-the-loop
api_count: 106
apis:
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: 'API для просмотра информации и управления счетами: * Получение баланса счёта, к которому привязаны карты * Получение списка счетов по номеру карты'
  name: Raiffeisenbank (Russia) Accounts Operation API
  slug: raiffeisen-ru-accounts-operation-api-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Агентский договора
  name: Raiffeisenbank (Russia) Agreement API
  slug: raiffeisen-ru-agreement-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Соглашения
  name: Raiffeisenbank (Russia) Agreements API
  slug: raiffeisen-ru-agreements-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Сумма договора Факторинга
  name: Raiffeisenbank (Russia) Agreement Sum API
  slug: raiffeisen-ru-agreementsum-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Информация о клиенте
  name: Raiffeisenbank (Russia) API - Client API
  slug: raiffeisen-ru-api-client-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The API - Fund API from Raiffeisenbank (Russia) — 1 operation(s) for api - fund.
  name: Raiffeisenbank (Russia) API - Fund API
  slug: raiffeisen-ru-api-fund-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The applications API from Raiffeisenbank (Russia) — 2 operation(s) for applications.
  name: Raiffeisenbank (Russia) Applications API
  slug: raiffeisen-ru-applications-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Работа с аудиторскими запросами
  name: Raiffeisenbank (Russia) Audits Controller API
  slug: raiffeisen-ru-auditscontroller-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Управление выставлением счетов на оплату
  name: Raiffeisenbank (Russia) Bills API
  slug: raiffeisen-ru-bills-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The brokerage-payment-orders API from Raiffeisenbank (Russia) — 2 operation(s) for brokerage-payment-orders.
  name: Raiffeisenbank (Russia) Brokerage Payment Orders API
  slug: raiffeisen-ru-brokerage-payment-orders-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The brokerage-reports API from Raiffeisenbank (Russia) — 4 operation(s) for brokerage-reports.
  name: Raiffeisenbank (Russia) Brokerage Reports API
  slug: raiffeisen-ru-brokerage-reports-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Покупатели
  name: Raiffeisenbank (Russia) Buyer API
  slug: raiffeisen-ru-buyer-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: 'Для информирования Компании о проведенных операциях по картам могут использоваться уведомления на адрес, указанный в настройках. В составе API имеется следующий функционал: * уведомление о блокировке '
  name: Raiffeisenbank (Russia) Callback API
  slug: raiffeisen-ru-callback-api-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Для информирования ТСП о проведенных платежах и возвратах могут использоваться HTTP-уведомления на адрес, указанный в его настройках. Адрес для уведомлений можно указать в [личном кабинете](https://ww
  name: Raiffeisenbank (Russia) Callback API
  slug: raiffeisen-ru-callback-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Методы позволяют получить список операций и итоговые суммы за определенный промежуток времени. Возможно использование методов для закрытия кассового периода.
  name: Raiffeisenbank (Russia) Cash Reconciliation API
  slug: raiffeisen-ru-cashreconciliation-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Клиенты
  name: Raiffeisenbank (Russia) Client API
  slug: raiffeisen-ru-client-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The Client settings API from Raiffeisenbank (Russia) — 1 operation(s) for client settings.
  name: Raiffeisenbank (Russia) Client settings API
  slug: raiffeisen-ru-client-settings-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The client-tariff-plan-change-correspond-controller API from Raiffeisenbank (Russia) — 1 operation(s) for client-tariff-plan-change-correspond-controller.
  name: Raiffeisenbank (Russia) Client Tariff Plan Change Correspond Controller API
  slug: raiffeisen-ru-client-tariff-plan-change-correspond-controller-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The client-tariff-plan-change-request-controller API from Raiffeisenbank (Russia) — 8 operation(s) for client-tariff-plan-change-request-controller.
  name: Raiffeisenbank (Russia) Client Tariff Plan Change Request Controller API
  slug: raiffeisen-ru-client-tariff-plan-change-request-controller-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The client-tariff-plan-change-request-dvr-controller API from Raiffeisenbank (Russia) — 1 operation(s) for client-tariff-plan-change-request-dvr-controller.
  name: Raiffeisenbank (Russia) Client Tariff Plan Change Request Dvr Controller API
  slug: raiffeisen-ru-client-tariff-plan-change-request-dvr-controller-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Управление закрывающими документами
  name: Raiffeisenbank (Russia) Closing Documents API
  slug: raiffeisen-ru-closingdocuments-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The code-blocking API from Raiffeisenbank (Russia) — 1 operation(s) for code-blocking.
  name: Raiffeisenbank (Russia) Code Blocking API
  slug: raiffeisen-ru-code-blocking-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The Codes API from Raiffeisenbank (Russia) — 2 operation(s) for codes.
  name: Raiffeisenbank (Russia) Codes API
  slug: raiffeisen-ru-codes-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Условия
  name: Raiffeisenbank (Russia) Condition API
  slug: raiffeisen-ru-condition-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The connection API from Raiffeisenbank (Russia) — 2 operation(s) for connection.
  name: Raiffeisenbank (Russia) Connection API
  slug: raiffeisen-ru-connection-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Контракт
  name: Raiffeisenbank (Russia) Contract API
  slug: raiffeisen-ru-contract-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Сведения о контракте
  name: Raiffeisenbank (Russia) Contract Details API
  slug: raiffeisen-ru-contract-details-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The Contracts API from Raiffeisenbank (Russia) — 2 operation(s) for contracts.
  name: Raiffeisenbank (Russia) Contracts API
  slug: raiffeisen-ru-contracts-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: 'Для реализации взаимодействия Райффайзенбанк предоставляет API: * запрос на создание карт с использованием HTTP; * получение информации о статусе запроса на создание карт'
  name: Raiffeisenbank (Russia) Corpcards API
  slug: raiffeisen-ru-corpcards-api-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Дополнительная информация для выпуска карт
  name: Raiffeisenbank (Russia) Corpcards Info API
  slug: raiffeisen-ru-corpcards-info-api-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: 'Для просмотра информации и управления картой Райффайзенбанк предоставляет API: * Просмотр списка карт * Подробная информация по карте * История действий * Список операций * Реквизиты карты * Установка'
  name: Raiffeisenbank (Russia) Corpcards Operation API
  slug: raiffeisen-ru-corpcards-operation-api-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Переписка
  name: Raiffeisenbank (Russia) Correspondences API
  slug: raiffeisen-ru-correspondences-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Кредитор
  name: Raiffeisenbank (Russia) Creditor API
  slug: raiffeisen-ru-creditor-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Сведения о валютных операциях
  name: Raiffeisenbank (Russia) Currency Transaction Certificate API
  slug: raiffeisen-ru-currency-transaction-certificate-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Операции с валютными переводами
  name: Raiffeisenbank (Russia) Currency Transfer API
  slug: raiffeisen-ru-currency-transfer-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The custody API from Raiffeisenbank (Russia) — 4 operation(s) for custody.
  name: Raiffeisenbank (Russia) Custody API
  slug: raiffeisen-ru-custody-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Рабочий день
  name: Raiffeisenbank (Russia) Day API
  slug: raiffeisen-ru-day-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Основные условия обслуживания поставщик-дебитор
  name: Raiffeisenbank (Russia) Deal Conditions API
  slug: raiffeisen-ru-dealconditions-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The Deals history API from Raiffeisenbank (Russia) — 3 operation(s) for deals history.
  name: Raiffeisenbank (Russia) Deals history API
  slug: raiffeisen-ru-deals-history-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Дебитор
  name: Raiffeisenbank (Russia) Debtor API
  slug: raiffeisen-ru-debtor-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Аутентификация пользователя и управление токенами OAuth2.
  name: Raiffeisenbank (Russia) Аутентификация API
  slug: raiffeisen-ru-default-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: 'Для получения информации о доставке карты Райффайзенбанк предоставляет API: * Информация о доставке карты'
  name: Raiffeisenbank (Russia) Delivery API
  slug: raiffeisen-ru-delivery-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The deprecated API from Raiffeisenbank (Russia) — 3 operation(s) for deprecated.
  name: Raiffeisenbank (Russia) Deprecated API
  slug: raiffeisen-ru-deprecated-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The dictionaries-v-1-controller API from Raiffeisenbank (Russia) — 1 operation(s) for dictionaries-v-1-controller.
  name: Raiffeisenbank (Russia) Dictionaries V 1 Controller API
  slug: raiffeisen-ru-dictionaries-v-1-controller-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: documents recognition
  name: Raiffeisenbank (Russia) Documents API
  slug: raiffeisen-ru-documents-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The domestic-payments API from Raiffeisenbank (Russia) — 15 operation(s) for domestic-payments.
  name: Raiffeisenbank (Russia) Domestic Payments API
  slug: raiffeisen-ru-domestic-payments-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Досрочное погашение
  name: Raiffeisenbank (Russia) Early Repayment API
  slug: raiffeisen-ru-earlyrepayment-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: 'API для управления категориями трат: * Получение категорий MCC * Создание и применение категорий трат по категориям и MCC * Получение сохраненных категорий трат'
  name: Raiffeisenbank (Russia) Expenses Categories API
  slug: raiffeisen-ru-expenses-categories-api-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Счета на оплату комиссий
  name: Raiffeisenbank (Russia) Fee Invoice API
  slug: raiffeisen-ru-feeinvoice-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Загрузка, проверка и скачивание вложений
  name: Raiffeisenbank (Russia) Files API
  slug: raiffeisen-ru-files-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Запрос на финансирование
  name: Raiffeisenbank (Russia) Financing Request API
  slug: raiffeisen-ru-financingrequest-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: 'Для фискализации чеков через партнёра Райффайзенбанк предоставляет API из следующих запросов: * Сохранение чека * Регистрация чека * Получение статуса чека Взаимодействие осуществляется по протоколу H'
  name: Raiffeisenbank (Russia) Fiscal Controller API
  slug: raiffeisen-ru-fiscal-controller-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The Forward API from Raiffeisenbank (Russia) — 3 operation(s) for forward.
  name: Raiffeisenbank (Russia) Forward API
  slug: raiffeisen-ru-forward-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Операции с распоряжениями о распределении валютной выручки
  name: Raiffeisenbank (Russia) Funds Distribution Order API
  slug: raiffeisen-ru-funds-distribution-order-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The future-client-tariff-plan-controller API from Raiffeisenbank (Russia) — 1 operation(s) for future-client-tariff-plan-controller.
  name: Raiffeisenbank (Russia) Future Client Tariff Plan Controller API
  slug: raiffeisen-ru-future-client-tariff-plan-controller-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Выпущенные гарантии в кабинете бенефициара
  name: Raiffeisenbank (Russia) Guarantee Beneficiary API
  slug: raiffeisen-ru-guarantee-beneficiary-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Отказы от прав
  name: Raiffeisenbank (Russia) Guarantee Renunciation API
  slug: raiffeisen-ru-guarantee-renunciation-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Печатные формы для отказов от прав
  name: Raiffeisenbank (Russia) Guarantee Renunciation Forms API
  slug: raiffeisen-ru-guarantee-renunciation-forms-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Схема сценария работы с выставлением счета со стороны Получателя. Применяется в тех случаях, когда нужно выставить счета с использование СБП B2B или Платежного поручения <a href='images/b2b-invoice.sv
  name: Raiffeisenbank (Russia) Invoice API
  slug: raiffeisen-ru-invoice-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Выпущенные гарантии
  name: Raiffeisenbank (Russia) Issued guarantees API
  slug: raiffeisen-ru-issued-guarantees-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Лимит
  name: Raiffeisenbank (Russia) Limit API
  slug: raiffeisen-ru-limit-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Транш
  name: Raiffeisenbank (Russia) Loan API
  slug: raiffeisen-ru-loan-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Письма
  name: Raiffeisenbank (Russia) Mails API
  slug: raiffeisen-ru-mails-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Конвертация MX и MT сообщений
  name: Raiffeisenbank (Russia) Конвертация MX и MT сообщений API
  slug: raiffeisen-ru-mx-mt-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Уведомление
  name: Raiffeisenbank (Russia) Notice API
  slug: raiffeisen-ru-notice-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The notification-external API from Raiffeisenbank (Russia) — 2 operation(s) for notification-external.
  name: Raiffeisenbank (Russia) Notification External API
  slug: raiffeisen-ru-notification-external-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The notification-settings-external API from Raiffeisenbank (Russia) — 2 operation(s) for notification-settings-external.
  name: Raiffeisenbank (Russia) Notification Settings External API
  slug: raiffeisen-ru-notification-settings-external-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Контекст факторингового предложения и доступности
  name: Raiffeisenbank (Russia) Offer API
  slug: raiffeisen-ru-offer-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The Option API from Raiffeisenbank (Russia) — 1 operation(s) for option.
  name: Raiffeisenbank (Russia) Option API
  slug: raiffeisen-ru-option-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Поручение
  name: Raiffeisenbank (Russia) Order API
  slug: raiffeisen-ru-order-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: 'Методы для работы с заказами: создание, получение списка, получение информации о заказе.'
  name: Raiffeisenbank (Russia) Orders API
  slug: raiffeisen-ru-orders-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Пакет поручений
  name: Raiffeisenbank (Russia) Packet API
  slug: raiffeisen-ru-packet-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Валидация PACS.009.01 и PACS.008.01 сообщений mx формата
  name: Raiffeisenbank (Russia) Валидация pacs сообщений API
  slug: raiffeisen-ru-pacs-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Парсер файлов реестров
  name: Raiffeisenbank (Russia) Parser API
  slug: raiffeisen-ru-parser-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: 'Для реализации взаимодействия с партнёром Райффайзенбанк предоставляет API для: * открытия платежной формы с использованием HTTP запросов; * получения информации о статусе заказа.'
  name: Raiffeisenbank (Russia) Pay Controller API
  slug: raiffeisen-ru-pay-controller-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The payer-email-change API from Raiffeisenbank (Russia) — 1 operation(s) for payer-email-change.
  name: Raiffeisenbank (Russia) Payer Email Change API
  slug: raiffeisen-ru-payer-email-change-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Простой способ для интеграции. Клиента необходимо перенаправить на платежную форму, передав параметры заказа.<br><br> [[Схема взаимодействия]](#section/Shema-raboty/Platezhnaya-forma-banka).
  name: Raiffeisenbank (Russia) Payform API
  slug: raiffeisen-ru-payform-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The payout-accounts API from Raiffeisenbank (Russia) — 1 operation(s) for payout-accounts.
  name: Raiffeisenbank (Russia) Payout Accounts API
  slug: raiffeisen-ru-payout-accounts-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: 'Для реализации взаимодействия с партнёром Райффайзенбанк предоставляет API из следующих запросов: * получение списка банков, принимающих выплаты по СБП, * запрос на проведение выплаты, * запрос на соз'
  name: Raiffeisenbank (Russia) Payout Controller API
  slug: raiffeisen-ru-payout-controller-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The payroll-statements-methods API from Raiffeisenbank (Russia) — 3 operation(s) for payroll-statements-methods.
  name: Raiffeisenbank (Russia) Payroll Statements Methods API
  slug: raiffeisen-ru-payroll-statements-methods-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Заявление на досрочное погашение основного долга
  name: Raiffeisenbank (Russia) Proposition API
  slug: raiffeisen-ru-proposition-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: 'Для реализации взаимодействия с партнёром Райффайзенбанк предоставляет API из следующих запросов: * отмена QR-кода, * получение данных по зарегистрированному QR-коду, * получение данных по платежу, * '
  name: Raiffeisenbank (Russia) QR API
  slug: raiffeisen-ru-qr-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The qr-sender API from Raiffeisenbank (Russia) — 5 operation(s) for qr-sender.
  name: Raiffeisenbank (Russia) Qr Sender API
  slug: raiffeisen-ru-qr-sender-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: 'Для реализации взаимодействия с кассовой ссылкой СБП (QRVariable) Райффайзенбанк предоставляет API из следующих запросов: * создание заказа * проведение возврата * получение статуса возврата * получен'
  name: Raiffeisenbank (Russia) QR Variable API
  slug: raiffeisen-ru-qrvariable-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: API курса валют ЦБ
  name: Raiffeisenbank (Russia) Rates API
  slug: raiffeisen-ru-rates-api-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Реестр поставок
  name: Raiffeisenbank (Russia) Registry API
  slug: raiffeisen-ru-registry-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Отчет
  name: Raiffeisenbank (Russia) Report API
  slug: raiffeisen-ru-report-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The Report V1 API from Raiffeisenbank (Russia) — 12 operation(s) for report v1.
  name: Raiffeisenbank (Russia) Report V1 API
  slug: raiffeisen-ru-report-v1-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The Report V1 Sync API from Raiffeisenbank (Russia) — 3 operation(s) for report v1 sync.
  name: Raiffeisenbank (Russia) Report V1 Sync API
  slug: raiffeisen-ru-report-v1-sync-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The Report V2 API from Raiffeisenbank (Russia) — 1 operation(s) for report v2.
  name: Raiffeisenbank (Russia) Report V2 API
  slug: raiffeisen-ru-report-v2-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The reports API from Raiffeisenbank (Russia) — 3 operation(s) for reports.
  name: Raiffeisenbank (Russia) Reports API
  slug: raiffeisen-ru-reports-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: 'Схема сценария работы с многоразовым Qr со стороны Получателя. Он удобен, когда транзакции носят повторяющийся характер или требуется обеспечить удобство для плательщика, позволяя использовать одну и '
  name: Raiffeisenbank (Russia) Reusable Payment Link API
  slug: raiffeisen-ru-reusable-payment-link-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The rp-accounting-account API from Raiffeisenbank (Russia) — 2 operation(s) for rp-accounting-account.
  name: Raiffeisenbank (Russia) Rp Accounting Account API
  slug: raiffeisen-ru-rp-accounting-account-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The rp-accounting API from Raiffeisenbank (Russia) — 2 operation(s) for rp-accounting.
  name: Raiffeisenbank (Russia) Rp Accounting API
  slug: raiffeisen-ru-rp-accounting-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: В данном разделе описаны методы, расширяющие сценарий проведения платежа.
  name: Raiffeisenbank (Russia) Scenario Expansion API
  slug: raiffeisen-ru-scenario-expansion-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Этот раздел позволяет вам удобно управлять распределением денег при получении денежных средств через СБП B2B. Вы можете создать заказ и указать, на какие счета и в каком объёме нужно зачислить получен
  name: Raiffeisenbank (Russia) Splits API
  slug: raiffeisen-ru-splits-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The Spot API from Raiffeisenbank (Russia) — 3 operation(s) for spot.
  name: Raiffeisenbank (Russia) Spot API
  slug: raiffeisen-ru-spot-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Сублимит - лимит на дебитора в рамках конкретного договора Факторинга
  name: Raiffeisenbank (Russia) Sublimit API
  slug: raiffeisen-ru-sublimit-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Для включения подписок необходима дополнительная настройка. Для этого заполните заявку в [Онлайн-банке](https://www.rbo.raiffeisen.ru/sign-form/subscription). Посмотреть клиентский путь можно с помощь
  name: Raiffeisenbank (Russia) Subscription API
  slug: raiffeisen-ru-subscription-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: В данном разделе описаны методы, с помощью которых можно провести списание по оформленной подписке, а также получить статус платежа. **API для данного сценария может быть расширяемым**.
  name: Raiffeisenbank (Russia) Subscriptions API
  slug: raiffeisen-ru-subscriptions-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Поставщик
  name: Raiffeisenbank (Russia) Supplier API
  slug: raiffeisen-ru-supplier-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Поставка
  name: Raiffeisenbank (Russia) Supply API
  slug: raiffeisen-ru-supply-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The tariff-plan-controller API from Raiffeisenbank (Russia) — 1 operation(s) for tariff-plan-controller.
  name: Raiffeisenbank (Russia) Tariff Plan Controller API
  slug: raiffeisen-ru-tariff-plan-controller-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Операции с документами тарифных планов
  name: Raiffeisenbank (Russia) Tariff plan documents API
  slug: raiffeisen-ru-tariff-plan-documents-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Тарифный план
  name: Raiffeisenbank (Russia) Tariff Plan API
  slug: raiffeisen-ru-tariffplan-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Для получения тестовых данных для интеграции напишите на ecom@raiffeisen.ru. В ответном письме мы отправим вам токен для авторизации в тестовой среде и два счёта для тестирования сервиса. Ниже предста
  name: Raiffeisenbank (Russia) Testing API
  slug: raiffeisen-ru-testing-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Темы переписок
  name: Raiffeisenbank (Russia) Topics API
  slug: raiffeisen-ru-topics-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: '**Методы в разработке** Методы позволяют создавать и проводить B2B-платежи двумя способами: - по QR-коду или платежной ссылке, - по банковским реквизитам получателя. Способ зависит от значения поля `t'
  name: Raiffeisenbank (Russia) Transfers V2 API
  slug: raiffeisen-ru-transfers-v2-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The ukep-controller API from Raiffeisenbank (Russia) — 3 operation(s) for ukep-controller.
  name: Raiffeisenbank (Russia) Ukep Controller API
  slug: raiffeisen-ru-ukep-controller-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The Пермиссии V1 API from Raiffeisenbank (Russia) — 2 operation(s) for пермиссии v1.
  name: Raiffeisenbank (Russia) Пермиссии V1 API
  slug: raiffeisen-ru-v1-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: The Пермиссии V2 API from Raiffeisenbank (Russia) — 3 operation(s) for пермиссии v2.
  name: Raiffeisenbank (Russia) Пермиссии V2 API
  slug: raiffeisen-ru-v2-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Для работы с карточными платежами с вашей формой, потребуется PCI DSS сертификация вашей организации. PCI DSS — стандарт информационной безопасности, принятый в индустрии платежных карт Visa и MasterC
  name: Raiffeisenbank (Russia) White Label API
  slug: raiffeisen-ru-white-label-api
- baseURL: https://api.raiffeisen.ru/raif-pay
  baseurl_source: declared
  description: Информация о клиенте
  name: Raiffeisenbank (Russia) Client Info API
  slug: raiffeisen-ru-client-info-api
artifact_total: 244
asyncapis:
- description: ''
  name: Raiffeisen Ru Webhooks
  slug: raiffeisen-ru-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/capabilities/raiffeisen-ru-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/raiffeisen-ru-capability-edges.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/asyncapi/raiffeisen-ru-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/raiffeisen-ru-webhooks.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/integrations/raiffeisen-ru-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/raiffeisen-ru-integration-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/agentic-access/raiffeisen-ru-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/raiffeisen-ru-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/rules/raiffeisen-ru-rules.yml
  title: ''
  type: Spectral
  url: rules/raiffeisen-ru-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/rules/raiffeisen-ru-rest-api-guide-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/raiffeisen-ru-rest-api-guide-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/json-ld/raiffeisen-ru-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/raiffeisen-ru-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/vocabulary/raiffeisen-ru-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/raiffeisen-ru-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/data-model/raiffeisen-ru-data-model.yml
  title: ''
  type: DataModel
  url: data-model/raiffeisen-ru-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/components/raiffeisen-ru-components.yml
  title: ''
  type: Components
  url: components/raiffeisen-ru-components.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/changelog/raiffeisen-ru-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/raiffeisen-ru-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/conventions/raiffeisen-ru-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/raiffeisen-ru-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/conventions/raiffeisen-ru-conventions.yml
  title: ''
  type: Conventions
  url: conventions/raiffeisen-ru-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/sandbox/raiffeisen-ru-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/raiffeisen-ru-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/scopes/raiffeisen-ru-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/raiffeisen-ru-scopes.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/lifecycle/raiffeisen-ru-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/raiffeisen-ru-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/lifecycle/raiffeisen-ru-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/raiffeisen-ru-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/errors/raiffeisen-ru-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/raiffeisen-ru-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/errors/raiffeisen-ru-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/raiffeisen-ru-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/errors/raiffeisen-ru-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/raiffeisen-ru-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/conformance/raiffeisen-ru-conformance.yml
  title: ''
  type: Conformance
  url: conformance/raiffeisen-ru-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/overlays/raiffeisen-ru-adm-deposit-codes-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/raiffeisen-ru-adm-deposit-codes-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/llms/raiffeisen-ru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/raiffeisen-ru-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/mcp/raiffeisen-ru-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/raiffeisen-ru-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/mcp/raiffeisen-ru-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/raiffeisen-ru-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/well-known/raiffeisen-ru-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/raiffeisen-ru-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/hosts/raiffeisen-ru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/raiffeisen-ru-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/packages/raiffeisen-ru-packages.yml
  title: ''
  type: SDKs
  url: packages/raiffeisen-ru-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/packages/raiffeisen-ru-packages.yml
  title: ''
  type: Packages
  url: packages/raiffeisen-ru-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.raiffeisen.ru/about/press/releases/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/authentication/raiffeisen-ru-authentication.yml
  title: ''
  type: Authentication
  url: authentication/raiffeisen-ru-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/security/raiffeisen-ru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/raiffeisen-ru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.raiffeisen.ru/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.raiffeisen.ru/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.raiffeisen.ru/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.raiffeisen.ru/docs/howToStart
- group: start
  title: ''
  type: Sandbox
  url: https://developer.raiffeisen.ru/docs/sandbox
- group: operate
  title: ''
  type: Support
  url: https://developer.raiffeisen.ru/docs/support
- group: company
  title: ''
  type: News
  url: https://developer.raiffeisen.ru/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pay.raif.ru/dev/
- group: start
  title: ''
  type: SignUp
  url: https://www.rbo.raiffeisen.ru/integrations/api/integrations
- group: start
  title: ''
  type: Login
  url: https://online.raiffeisen.ru/login/main
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Raiffeisen-DGTL
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.raiffeisen.ru/static/common/about/disclaimer/policy_processing_of_personal_data.pdf
- group: company
  title: ''
  type: Newsroom
  url: https://www.raiffeisen.ru/about/press/
- group: operate
  title: ''
  type: Contact
  url: https://www.raiffeisen.ru/about/feedback/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/Raiffeisen-DGTL/rest-api-guide/blob/b2afc8e0247d5ff43a3cb61b2c343752fd2f6ee6/spectral/base-ruleset.yaml
created: '2026-10-09'
description: Raiffeisenbank (AO Raiffeisenbank, Райффайзен Банк) is a Russian bank providing a full range of banking services to retail and corporate clients (mortgages, loans, deposits, business banking). Through its Raiffeisen API developer portal (developer.raiffeisen.ru) it publishes a catalog of public corporate banking APIs for payments, account statements, payroll, liquidity and FX, connectable directly from 1C or ERP systems, with OAuth 2.0 authentication, a sandbox and documentation; it also runs the separate Raif Pay API for merchant payments, and its Raiffeisen-DGTL GitHub organization publishes a REST API design guide with Spectral rules.
image: https://www.raiffeisen.ru/static/common/initial/opengraf.png
json_schemas:
- name: AccEmployeePermissionDTO
  property_count: 3
  slug: raiffeisen-ru-acc-employee-permission-dto
- name: AgreementResponse
  property_count: 11
  slug: raiffeisen-ru-agreement-response
- name: AgreementsFilterRequest
  property_count: 3
  slug: raiffeisen-ru-agreements-filter-request
- name: AgreementsResponse
  property_count: 1
  slug: raiffeisen-ru-agreements-response
- name: ApiProcessImportDto
  property_count: 8
  slug: raiffeisen-ru-api-process-import-dto
- name: ApiProcessImportFullDto
  property_count: 8
  slug: raiffeisen-ru-api-process-import-full-dto
- name: ApiShortProcessImportDto
  property_count: 1
  slug: raiffeisen-ru-api-short-process-import-dto
- name: AuditOrderResponse
  property_count: 11
  slug: raiffeisen-ru-audit-order-response
- name: AuditRequest
  property_count: 3
  slug: raiffeisen-ru-audit-request
- name: AvailableTariffPlansView
  property_count: 2
  slug: raiffeisen-ru-available-tariff-plans-view
- name: BillDetailsResponse
  property_count: 13
  slug: raiffeisen-ru-bill-details-response
- name: BillRequest
  property_count: 6
  slug: raiffeisen-ru-bill-request
- name: Buyer
  property_count: 0
  slug: raiffeisen-ru-buyer
- name: ClientInfoResponse
  property_count: 2
  slug: raiffeisen-ru-client-info-response
- name: ClientTariffPlanChangeRequestBodyView
  property_count: 4
  slug: raiffeisen-ru-client-tariff-plan-change-request-body-view
- name: ClientTariffPlanChangeRequestPreSignView
  property_count: 13
  slug: raiffeisen-ru-client-tariff-plan-change-request-pre-sign-view
- name: ClientTariffPlanChangeRequestStateHistoryView
  property_count: 2
  slug: raiffeisen-ru-client-tariff-plan-change-request-state-history-view
- name: ClosingDocumentDetailsResponse
  property_count: 5
  slug: raiffeisen-ru-closing-document-details-response
- name: ClosingDocumentListResponse
  property_count: 5
  slug: raiffeisen-ru-closing-document-list-response
- name: Code
  property_count: 6
  slug: raiffeisen-ru-code
- name: ColorResource
  property_count: 2
  slug: raiffeisen-ru-color-resource
- name: comparisonSummaryRep
  property_count: 2
  slug: raiffeisen-ru-comparison-summary-rep
- name: ConditionRequest
  property_count: 9
  slug: raiffeisen-ru-condition-request
- name: Condition
  property_count: 13
  slug: raiffeisen-ru-condition
- name: CreateAuditOrderResponse
  property_count: 9
  slug: raiffeisen-ru-create-audit-order-response
- name: CreateExcelReportRequest
  property_count: 12
  slug: raiffeisen-ru-create-excel-report-request
- name: CreateExternalCorrespondenceRequest
  property_count: 4
  slug: raiffeisen-ru-create-external-correspondence-request
- name: CreateExternalMailRequest
  property_count: 4
  slug: raiffeisen-ru-create-external-mail-request
- name: CreateMt940ReportRequest
  property_count: 13
  slug: raiffeisen-ru-create-mt940-report-request
- name: CreateMt942ReportRequest
  property_count: 12
  slug: raiffeisen-ru-create-mt942-report-request
- name: CreateNotificationRequest
  property_count: 3
  slug: raiffeisen-ru-create-notification-request
- name: CreateNotificationResponse
  property_count: 1
  slug: raiffeisen-ru-create-notification-response
- name: CreateNotificationSettingsRequest
  property_count: 1
  slug: raiffeisen-ru-create-notification-settings-request
- name: CreatePdfReportRequest
  property_count: 13
  slug: raiffeisen-ru-create-pdf-report-request
- name: CreateStatementRequest
  property_count: 3
  slug: raiffeisen-ru-create-statement-request
- name: CreateStatementResponse
  property_count: 1
  slug: raiffeisen-ru-create-statement-response
- name: Create1CReportRequest
  property_count: 12
  slug: raiffeisen-ru-create1-creport-request
- name: Create1CReportRequestV2
  property_count: 12
  slug: raiffeisen-ru-create1-creport-request-v2
- name: CurrencyContractRequest
  property_count: 0
  slug: raiffeisen-ru-currency-contract-request
- name: CurrencyContractResponse
  property_count: 0
  slug: raiffeisen-ru-currency-contract-response
- name: DeactivateCodeRequest
  property_count: 1
  slug: raiffeisen-ru-deactivate-code-request
- name: DeactivateCodeResponse
  property_count: 1
  slug: raiffeisen-ru-deactivate-code-response
- name: DeliverableConversionBlotterRequest
  property_count: 4
  slug: raiffeisen-ru-deliverable-conversion-blotter-request
- name: DeliverableConversionBlotterResponse
  property_count: 2
  slug: raiffeisen-ru-deliverable-conversion-blotter-response
- name: DigestResource
  property_count: 9
  slug: raiffeisen-ru-digest-resource
- name: DigestStatResource
  property_count: 2
  slug: raiffeisen-ru-digest-stat-resource
- name: DigestV2Resources
  property_count: 4
  slug: raiffeisen-ru-digest-v2-resources
- name: DocumentStatusResponse
  property_count: 2
  slug: raiffeisen-ru-document-status-response
- name: EligibleCompaniesResponse
  property_count: 4
  slug: raiffeisen-ru-eligible-companies-response
- name: EmployeeRoleRequest
  property_count: 2
  slug: raiffeisen-ru-employee-role-request
- name: EmployeeRoleResponse
  property_count: 3
  slug: raiffeisen-ru-employee-role-response
- name: ErrorPageDataDTO
  property_count: 2
  slug: raiffeisen-ru-error-page-data-dto
- name: FileMetadata
  property_count: 8
  slug: raiffeisen-ru-file-metadata
- name: FileUploadRequest
  property_count: 2
  slug: raiffeisen-ru-file-upload-request
- name: FileUploadResponse
  property_count: 0
  slug: raiffeisen-ru-file-upload-response
- name: ForeignTradeContract
  property_count: 29
  slug: raiffeisen-ru-foreign-trade-contract
- name: FundAccountResponse
  property_count: 5
  slug: raiffeisen-ru-fund-account-response
- name: FundInfoDto
  property_count: 2
  slug: raiffeisen-ru-fund-info-dto
- name: GetActivesByCnumRequest
  property_count: 1
  slug: raiffeisen-ru-get-actives-by-cnum-request
- name: GetCodeListResponse
  property_count: 4
  slug: raiffeisen-ru-get-code-list-response
- name: GetExternalCorrespondenceResponse
  property_count: 10
  slug: raiffeisen-ru-get-external-correspondence-response
- name: GetExternalCorrespondenceV2Response
  property_count: 11
  slug: raiffeisen-ru-get-external-correspondence-v2-response
- name: GuaranteeBeneficiaryDto
  property_count: 11
  slug: raiffeisen-ru-guarantee-beneficiary-dto
- name: GuaranteeBeneficiaryFilterRequest
  property_count: 3
  slug: raiffeisen-ru-guarantee-beneficiary-filter-request
- name: GuaranteeBeneficiaryResponse
  property_count: 1
  slug: raiffeisen-ru-guarantee-beneficiary-response
- name: GuaranteeChangeLogDto
  property_count: 11
  slug: raiffeisen-ru-guarantee-change-log-dto
- name: GuaranteeCommissionExcelRequest
  property_count: 4
  slug: raiffeisen-ru-guarantee-commission-excel-request
- name: GuaranteeFilterRequest
  property_count: 3
  slug: raiffeisen-ru-guarantee-filter-request
- name: GuaranteeRenunciationDto
  property_count: 16
  slug: raiffeisen-ru-guarantee-renunciation-dto
- name: GuaranteeShortDTO
  property_count: 2
  slug: raiffeisen-ru-guarantee-short-dto
- name: GuaranteesResponse
  property_count: 1
  slug: raiffeisen-ru-guarantees-response
- name: LoginStepRequestDTO
  property_count: 5
  slug: raiffeisen-ru-login-step-request-dto
- name: LoginViewDataDTO
  property_count: 3
  slug: raiffeisen-ru-login-view-data-dto
- name: NewsContentCounterResource
  property_count: 5
  slug: raiffeisen-ru-news-content-counter-resource
- name: Notice
  property_count: 6
  slug: raiffeisen-ru-notice
- name: NotificationSettingsResponse
  property_count: 0
  slug: raiffeisen-ru-notification-settings-response
- name: OperationDtoV2
  property_count: 4
  slug: raiffeisen-ru-operation-dto-v2
- name: OrderResponse
  property_count: 0
  slug: raiffeisen-ru-order-response
- name: PacketResponse
  property_count: 10
  slug: raiffeisen-ru-packet-response
- name: PageBillMiniResponse
  property_count: 12
  slug: raiffeisen-ru-page-bill-mini-response
- name: PageResponseClientTariffPlanChangeRequestListView
  property_count: 5
  slug: raiffeisen-ru-page-response-client-tariff-plan-change-request-list-view
- name: PageResponseFutureClientTariffPlanPublicView
  property_count: 5
  slug: raiffeisen-ru-page-response-future-client-tariff-plan-public-view
- name: PaymentOrderCreateRequest
  property_count: 5
  slug: raiffeisen-ru-payment-order-create-request
- name: PaymentOrder
  property_count: 8
  slug: raiffeisen-ru-payment-order
- name: PermissionsContextV1
  property_count: 3
  slug: raiffeisen-ru-permissions-context-v1
- name: ProductNewsV2Resource
  property_count: 10
  slug: raiffeisen-ru-product-news-v2-resource
- name: ProductNewsV2Resources
  property_count: 4
  slug: raiffeisen-ru-product-news-v2-resources
- name: PublicJwksResponseDTO
  property_count: 1
  slug: raiffeisen-ru-public-jwks-response-dto
- name: Rate
  property_count: 6
  slug: raiffeisen-ru-rate
- name: ReadStatusResource
  property_count: 1
  slug: raiffeisen-ru-read-status-resource
- name: reportPaymentCardResponse
  property_count: 10
  slug: raiffeisen-ru-report-payment-card-response
- name: reportPaymentSbpResponse
  property_count: 10
  slug: raiffeisen-ru-report-payment-sbp-response
- name: reportRefundCardResponse
  property_count: 10
  slug: raiffeisen-ru-report-refund-card-response
- name: reportRefundSbpResponse
  property_count: 10
  slug: raiffeisen-ru-report-refund-sbp-response
- name: ReportResponse
  property_count: 1
  slug: raiffeisen-ru-report-response
- name: ReportTaskCreateRequest
  property_count: 7
  slug: raiffeisen-ru-report-task-create-request
- name: ReportTask
  property_count: 14
  slug: raiffeisen-ru-report-task
- name: ReportTaskType
  property_count: 5
  slug: raiffeisen-ru-report-task-type
- name: SearchCorrespondencesRequest
  property_count: 3
  slug: raiffeisen-ru-search-correspondences-request
- name: StatResource
  property_count: 1
  slug: raiffeisen-ru-stat-resource
- name: StatementStatusResponse
  property_count: 5
  slug: raiffeisen-ru-statement-status-response
- name: StatementTransfersResponse
  property_count: 5
  slug: raiffeisen-ru-statement-transfers-response
- name: StatusHistoryResponse
  property_count: 1
  slug: raiffeisen-ru-status-history-response
- name: StreamingResponseBody
  property_count: 0
  slug: raiffeisen-ru-streaming-response-body
- name: SubmitExternalMailRequest
  property_count: 7
  slug: raiffeisen-ru-submit-external-mail-request
- name: SupplyList
  property_count: 0
  slug: raiffeisen-ru-supply-list
- name: Supply
  property_count: 16
  slug: raiffeisen-ru-supply
- name: TariffPlanDocumentPublicView
  property_count: 4
  slug: raiffeisen-ru-tariff-plan-document-public-view
- name: TaskCreateRequest
  property_count: 8
  slug: raiffeisen-ru-task-create-request
- name: TaskResponse
  property_count: 5
  slug: raiffeisen-ru-task-response
- name: TfoCounterResult
  property_count: 1
  slug: raiffeisen-ru-tfo-counter-result
- name: TokenRequestDTO
  property_count: 7
  slug: raiffeisen-ru-token-request-dto
- name: TokenRevocationRequestDTO
  property_count: 4
  slug: raiffeisen-ru-token-revocation-request-dto
- name: TreasuryReportsResponse
  property_count: 4
  slug: raiffeisen-ru-treasury-reports-response
- name: UiCountAgreementsResponse
  property_count: 2
  slug: raiffeisen-ru-ui-count-agreements-response
- name: UpdateCodeRequest
  property_count: 1
  slug: raiffeisen-ru-update-code-request
- name: UPDRequest
  property_count: 0
  slug: raiffeisen-ru-updrequest
- name: UserEligibleCompaniesResponse
  property_count: 4
  slug: raiffeisen-ru-user-eligible-companies-response
- name: WebinarV2Resource
  property_count: 14
  slug: raiffeisen-ru-webinar-v2-resource
- name: WebinarsV2Resources
  property_count: 4
  slug: raiffeisen-ru-webinars-v2-resources
jsonld:
- class_count: 120
  name: Raiffeisen Ru Context
  property_count: 196
  slug: raiffeisen-ru-context
layout: provider
mcp_servers:
- description: 'Official remote MCP server published by Raiffeisenbank (Russia) giving AI assistants access to the public developer portal (developer.raif.ru / developer.raiffeisen.ru): documentation in Russian and E'
  name: Raiffeisenbank (Russia) Developer Portal MCP Server
  slug: raiffeisenbank-russia-developer-portal-mcp-server
modified: '2026-10-09'
name: Raiffeisenbank (Russia)
nav: Providers
network: true
overview: 'Raiffeisenbank (Russia) publishes 113 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts Operation API, Agreement API, Agreements API, and 110 more. Tagged areas include Company, Banking, Financial Services, Corporate Banking, and Payments.


  The Raiffeisenbank (Russia) catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Raiffeisenbank (Russia)''s developer surface includes changelog, sandbox, authentication, documentation, getting-started guide, support, product news, and 41 more developer resources.'
plans:
- name: Raiffeisen Ru Plans Pricing
  plan_count: 0
  slug: raiffeisen-ru-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Raiffeisen Ru Rate Limits
  slug: raiffeisen-ru-rate-limits
rules:
- authorship: provider
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Raiffeisenbank (Russia) — rest api guide rules
  rule_count: 60
  severity_counts:
    error: 49
    hint: 0
    info: 4
    warn: 7
  slug: raiffeisen-ru-rest-api-guide-spectral-rules
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Raiffeisenbank (Russia) API Rules
  rule_count: 15
  severity_counts:
    error: 5
    hint: 0
    info: 4
    warn: 6
  slug: raiffeisen-ru-rules
scopes:
- name: Raiffeisen Ru Scopes
  scope_count: 4
  slug: raiffeisen-ru-scopes
  summary_line: 4 scopes
score:
  band: strong
  composite: 63.2
  coverage:
    artifact_dirs: 32
    catalog_earned: 79.3
    catalog_earned_first_party: 18.0
    catalog_gap: 35.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.3
  facets:
    access_clarity: 23.7
    contract_governance: 76.5
    contract_quality: 71.3
    developer_ergonomics: 63.7
    discoverability: 81.7
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - russia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 54.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 113
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 29.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/raiffeisen-ru/refs/heads/main/screenshots/raiffeisen-ru-2026-10-11T113117.png
security:
- kind: authentication
  name: Raiffeisen Ru Authentication
  slug: raiffeisen-ru-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Raiffeisen Ru Domain Security
  slug: raiffeisen-ru-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: raiffeisen-ru
tags:
- Company
- Banking
- Financial Services
- Corporate Banking
- Payments
- Open Banking
- Russia
website: https://www.raiffeisen.ru/
---
