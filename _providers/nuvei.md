---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 23
  human_in_the_loop: 1
  name: Nuvei Agentic Access
  operation_count: 23
  slug: nuvei-agentic-access
  summary_line: 23 operations · 23 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: Server-to-server REST API for processing card and APM transactions through Nuvei. Includes openOrder for session setup, payment for end-to-end transactions, settleTransaction for capturing pre-authori
  name: Nuvei Payments API
  slug: nuvei-payments-api
- description: Pushes funds out to consumers and counterparties via card, bank account, and a wide set of local APMs. The payout endpoint supports referenced (relatedTransactionId) and unreferenced (account number /
  name: Nuvei Payouts API
  slug: nuvei-payouts-api
- description: Manages stored payment instruments (User Payment Options / UPOs) including card and APM tokenization. Supports addUPOCreditCard, addUPOAPM, editUPOCreditCard, editUPOAPM, deleteUPO, getUserUPOs, and e
  name: Nuvei User Payment Options API
  slug: nuvei-user-payment-options-api
- description: 3D Secure 2 authentication endpoints. getCard3DDetails returns DS information and challenge requirements for a card; authenticate3d completes the authentication flow returning CAVV and ECI. Designed t
  name: Nuvei 3DS API
  slug: nuvei-3ds-api
- description: Dynamic Currency Conversion. getDccDetails computes the converted amount and markup rate for a card BIN and currency pair so merchants can present a localized currency offer at checkout.
  name: Nuvei DCC API
  slug: nuvei-dcc-api
- description: 'Asynchronous webhook notifications sent from Nuvei to a merchant endpoint to communicate the final status of payments, payouts, refunds, voids, settles, and Control Panel events. Payment DMNs include '
  name: Nuvei Direct Merchant Notifications (DMN)
  slug: nuvei-webhooks-dmn
- description: Settle, void, and refund operations.
  name: Nuvei Financial Operations API
  slug: nuvei-financial-operations-api
- description: The Merchant API from Nuvei — 2 operation(s) for merchant.
  name: Nuvei Merchant API
  slug: nuvei-merchant-api
- description: The Orders API from Nuvei — 2 operation(s) for orders.
  name: Nuvei Orders API
  slug: nuvei-orders-api
- description: The Sessions API from Nuvei — 1 operation(s) for sessions.
  name: Nuvei Sessions API
  slug: nuvei-sessions-api
- description: Read-only transaction state.
  name: Nuvei Status API
  slug: nuvei-status-api
artifact_total: 43
asyncapis:
- description: Asynchronous webhook notifications delivered from Nuvei to a merchant-configured notificationUrl when payments, payouts, refunds, voids, settles, or Control Panel events reach their final state. Payme
  name: Nuvei Direct Merchant Notifications (DMN)
  slug: nuvei-dmn-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nuvei 3DS API
  slug: open-nuvei-3ds-api
- collection_type: open
  name: Nuvei 3DS DCC API
  slug: open-nuvei-dcc-api
- collection_type: open
  name: Nuvei 3DS Financial Operations API
  slug: open-nuvei-financial-operations-api
- collection_type: open
  name: Nuvei 3DS Merchant API
  slug: open-nuvei-merchant-api
- collection_type: open
  name: Nuvei Merchant Configuration API
  slug: open-nuvei-merchant-config-api
- collection_type: open
  name: Nuvei Order API
  slug: open-nuvei-order-api
- collection_type: open
  name: Nuvei 3DS Orders API
  slug: open-nuvei-orders-api
- collection_type: open
  name: Nuvei 3DS Payments API
  slug: open-nuvei-payments-api
- collection_type: open
  name: Nuvei 3DS Payouts API
  slug: open-nuvei-payouts-api
- collection_type: open
  name: Nuvei Session API
  slug: open-nuvei-session-api
- collection_type: open
  name: Nuvei 3DS Sessions API
  slug: open-nuvei-sessions-api
- collection_type: open
  name: Nuvei 3DS Status API
  slug: open-nuvei-status-api
- collection_type: open
  name: Nuvei 3DS User Payment Options API
  slug: open-nuvei-user-payment-options-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nuvei-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuvei-domain-security.yml
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Nuvei/nuvei-server-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Nuvei/nuvei-server-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Nuvei/nuvei-server-java-2.0
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Nuvei/nuvei-server-nodejs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Nuvei/nuvei-mobile-sdk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Nuvei/nuvei-mobile-sdk-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Nuvei/nuvei-react-native-mobile-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Nuvei/nuvei-mobile-cashier-helper-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Nuvei/nuvei-mobile-cashier-helper-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Nuvei/nuvei-cashier-helper-react-for-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Nuvei/nuvei-mobile-pods
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Nuvei/nuvei-maven-android
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Nuvei/nuvei-plugin-magento-2
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Nuvei/nuvei-plugin-woocommerce
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Nuvei/nuvei-plugin-prestashop
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Nuvei/nuvei-plugin-opencart-3
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Nuvei/nuvei-plugin-opencart-4
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Nuvei/nuvei-plugin-shopware-5
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Nuvei/nuvei-plugin-shopware-6
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Nuvei/nuvei-plugin-salesforce-commerce-cloud
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Nuvei/nuvei-plugin-sap-commerce
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Nuvei/nuvei-plugin-commerce-tools-backend
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Nuvei/nuvei-plugin-commerce-tools-frontend
created: '2026-05-24'
description: Nuvei is a global payment technology company headquartered in Montreal, Canada, providing a single platform for online card acquiring, alternative payment methods (700+ APMs), payouts, currency management across 150+ currencies, risk and fraud, and payment orchestration. Nuvei serves merchants in 200+ markets with local acquiring in 52 markets across eCommerce, iGaming, sports betting, travel, retail, B2B, and financial services. Originally listed on Nasdaq and TSX as NVEI, Nuvei was taken private by Advent International in 2024.
examples:
- key_count: 2
  name: Nuvei Open Order Example
  slug: nuvei-open-order-example
- key_count: 2
  name: Nuvei Payment Dmn Example
  slug: nuvei-payment-dmn-example
- key_count: 2
  name: Nuvei Payment Example
  slug: nuvei-payment-example
- key_count: 2
  name: Nuvei Refund Example
  slug: nuvei-refund-example
finops:
- name: Nuvei Finops
  service_category: Payments
  slug: nuvei-finops
graphqls:
- description: Nuvei is a global payment technology company. The API covers payment processing, payment methods, refunds, payouts, subscriptions, fraud management, 3DS authentication, and transaction reporting acros
  name: Nuvei GraphQL API
  slug: nuvei-graphql
image: https://nuvei.com/wp-content/uploads/2023/01/Nuvei_Logo_2C_RGB.svg
json_schemas:
- name: NuveiPayment
  property_count: 17
  slug: nuvei-payment
- name: NuveiTransaction
  property_count: 19
  slug: nuvei-transaction
json_structures:
- name: Nuvei Payment Structure
  property_count: 9
  slug: nuvei-payment-structure
jsonld:
- class_count: 32
  name: Nuvei Context
  property_count: 2
  slug: nuvei-context
layout: provider
modified: '2026-05-24'
name: Nuvei
nav: Providers
network: true
overview: 'Nuvei publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Payments API, Payouts API, User Payment Options API, and 8 more. Tagged areas include Payments, Payment Processing, Payment Gateway, Acquiring, and Payouts.


  The Nuvei catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.'
plans:
- name: Nuvei Plans Pricing
  plan_count: 1
  slug: nuvei-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Nuvei Rate Limits
  slug: nuvei-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Nuvei API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: nuvei-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Nuvei API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: nuvei-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Nuvei API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: nuvei-rules
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 46.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 66.9
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 0.0
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nuvei/refs/heads/main/screenshots/nuvei-2026-06-20T190542.png
security:
- kind: domain-security
  name: Nuvei Domain Security
  slug: nuvei-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nuvei
tags:
- Payments
- Payment Processing
- Payment Gateway
- Acquiring
- Payouts
- Alternative Payment Methods
- Fraud
- Risk
- Currency Conversion
- iGaming
- E-Commerce
- Fintech
---
