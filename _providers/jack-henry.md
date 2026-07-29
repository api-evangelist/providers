---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Jack Henry Agentic Access
  operation_count: 52
  slug: jack-henry-agentic-access
  summary_line: 52 operations · 19 acting
api_count: 42
apis:
- description: 'Real-time, pub/sub-based event streaming surface. Lets institutions and partners react to events emitted across Jack Henry''s platform (account events, transaction events, alert events, user-lifecycle '
  name: Enterprise Event System
  slug: enterprise-event-system
- description: Translation surface for the Symitar credit-union core. Query member accounts, post transactions, and execute PowerOn scripts.
  name: SymXchange
  slug: symxchange
- description: Customized bulk-data query interface for institution data. Sits alongside Data Hub for deeper analytics access.
  name: Operational Data Integration (ODI)
  slug: operational-data-integration-odi
- description: Provides deeper access to financial institution data for partners building analytics, BI, and personalization solutions on top of Jack Henry core systems.
  name: Data Hub
  slug: data-hub
- description: Cloud-native core banking platform — the next-generation successor surface alongside SilverLake, CIF 20/20, and Symitar. Targets modern API-first deployments for de novo banks and modernization progra
  name: Digital Core
  slug: digital-core
- description: Institution feature-flag map.
  name: Jack Henry & Associates Abilities API
  slug: jack-henry-abilities-api
- description: Deposit, loan, line-of-credit, and investment accounts.
  name: Jack Henry & Associates Accounts API
  slug: jack-henry-accounts-api
- description: ACH credit and debit origination.
  name: Jack Henry & Associates ACH Origination API
  slug: jack-henry-ach-origination-api
- description: Account and security alerts.
  name: Jack Henry & Associates Alerts API
  slug: jack-henry-alerts-api
- description: OAuth authorization endpoint.
  name: Jack Henry & Associates Authorization API
  slug: jack-henry-authorization-api
- description: Bill-payment payees and payments.
  name: Jack Henry & Associates Bill Pay API
  slug: jack-henry-bill-pay-api
- description: Consumer and small-business bill pay.
  name: Jack Henry & Associates Bill Payments API
  slug: jack-henry-bill-payments-api
- description: Debit and credit card management.
  name: Jack Henry & Associates Cards API
  slug: jack-henry-cards-api
- description: Consumer account administration.
  name: Jack Henry & Associates Consumers API
  slug: jack-henry-consumers-api
- description: Customer (CIF) records.
  name: Jack Henry & Associates Customers API
  slug: jack-henry-customers-api
- description: DDA/savings/CD deposit accounts.
  name: Jack Henry & Associates Deposit Accounts API
  slug: jack-henry-deposit-accounts-api
- description: OpenID Connect discovery and JWKS.
  name: Jack Henry & Associates Discovery API
  slug: jack-henry-discovery-api
- description: GL account inquiry.
  name: Jack Henry & Associates General Ledger API
  slug: jack-henry-general-ledger-api
- description: Sensitive operations requiring elevated authorization.
  name: Jack Henry & Associates High Risk Actions API
  slug: jack-henry-high-risk-actions-api
- description: Audit and activity history.
  name: Jack Henry & Associates History API
  slug: jack-henry-history-api
- description: Drive scheduled or emergency offline modes.
  name: Jack Henry & Associates Institution Offline Status API
  slug: jack-henry-institution-offline-status-api
- description: Public institution profile lookup.
  name: Jack Henry & Associates Institutions API
  slug: jack-henry-institutions-api
- description: Consumer and commercial loans.
  name: Jack Henry & Associates Loan Accounts API
  slug: jack-henry-loan-accounts-api
- description: Configure marketing/ad cards in the dashboard.
  name: Jack Henry & Associates Marketing Ads API
  slug: jack-henry-marketing-ads-api
- description: Two-way secure messaging with the institution.
  name: Jack Henry & Associates Messages API
  slug: jack-henry-messages-api
- description: Cross-rail routing and virtual accounts.
  name: Jack Henry & Associates Payments Orchestrator API
  slug: jack-henry-payments-orchestrator-api
- description: P2P transfers via partner networks.
  name: Jack Henry & Associates Peer To Peer API
  slug: jack-henry-peer-to-peer-api
- description: Bridge handshake and lifecycle.
  name: Jack Henry & Associates Plugin Bridge API
  slug: jack-henry-plugin-bridge-api
- description: Plugin metadata published by the host.
  name: Jack Henry & Associates Plugin Configuration API
  slug: jack-henry-plugin-configuration-api
- description: Configure external applications and plugins.
  name: Jack Henry & Associates Plugin Management API
  slug: jack-henry-plugin-management-api
- description: Consumer and commercial RDC.
  name: Jack Henry & Associates Remote Deposit Capture API
  slug: jack-henry-remote-deposit-capture-api
- description: Operational and audit reports.
  name: Jack Henry & Associates Reports API
  slug: jack-henry-reports-api
- description: Routing number validation.
  name: Jack Henry & Associates Routing Numbers API
  slug: jack-henry-routing-numbers-api
- description: User segments for targeted experiences.
  name: Jack Henry & Associates Segments API
  slug: jack-henry-segments-api
- description: OAuth token exchange.
  name: Jack Henry & Associates Token API
  slug: jack-henry-token-api
- description: Posted and pending transactions per account.
  name: Jack Henry & Associates Transactions API
  slug: jack-henry-transactions-api
- description: Account-to-account and external transfers.
  name: Jack Henry & Associates Transfers API
  slug: jack-henry-transfers-api
- description: Profile and identity of the authenticated user.
  name: Jack Henry & Associates User API
  slug: jack-henry-user-api
- description: Authenticated user/account context surfaced to a plugin.
  name: Jack Henry & Associates User Context API
  slug: jack-henry-user-context-api
- description: OpenID Connect UserInfo endpoint.
  name: Jack Henry & Associates UserInfo API
  slug: jack-henry-userinfo-api
- description: Outbound wire requests.
  name: Jack Henry & Associates Wire Transfers API
  slug: jack-henry-wire-transfers-api
- description: Zelle peer-to-peer payments.
  name: Jack Henry & Associates Zelle API
  slug: jack-henry-zelle-api
artifact_total: 82
asyncapis:
- description: Real-time, pub/sub-based event system for Jack Henry platform events. Lets partners and institutions subscribe to account events, transaction events, alert events, and user-lifecycle events without po
  name: Jack Henry Enterprise Event System
  slug: enterprise-event-system-asyncapi
collections:
- collection_type: open
  name: Banno Admin API
  slug: open-banno-admin-api
- collection_type: open
  name: Banno Authentication Framework
  slug: open-banno-authentication-framework
- collection_type: open
  name: Banno Consumer API
  slug: open-banno-consumer-api
- collection_type: open
  name: Banno Plugin Framework
  slug: open-banno-plugin-framework
- collection_type: open
  name: Jack Henry Payments
  slug: open-jack-henry-payments
- collection_type: open
  name: jXchange REST
  slug: open-jxchange-rest
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jack-henry-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jack-henry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jack-henry-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.jackhenry.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://jackhenry.dev/
- group: build
  title: ''
  type: DigitalToolkit
  url: https://jackhenry.dev/digital-toolkit/
- group: docs
  title: ''
  type: Documentation
  url: https://banno.github.io/open-api-docs/
- group: company
  title: ''
  type: Blog
  url: https://www.jackhenry.com/fintalk
- group: operate
  title: ''
  type: PressReleases
  url: https://ir.jackhenry.com/news-releases
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.jackhenry.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Banno
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/banno-digital-toolkit
- group: operate
  title: ''
  type: Support
  url: https://jackhenry.dev/support/
- group: operate
  title: ''
  type: Status
  url: https://status.banno.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jackhenry.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jackhenry.com/legal/privacy
- group: company
  title: ''
  type: Careers
  url: https://www.jackhenry.com/who-we-are/careers
- group: company
  title: ''
  type: TwitterX
  url: https://x.com/JackHenryAssoc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jack-henry-associates/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/JackHenryAssociates
created: '2026-05-23'
description: 'Jack Henry & Associates (Nasdaq: JKHY) is an S&P 500 financial technology company that provides core banking, payments, lending, digital banking, and fraud-prevention technology to community and regional financial institutions in the United States. Approximately 7,400 client institutions and ~7,240 associates as of fiscal year-end June 30, 2025. The developer surface centers on the Banno Digital Toolkit (Plugin Framework, Consumer API, Admin API, Authentication Framework), the jXchange and SymXchange core banking translation APIs, the Payments Orchestrator + rails (ACH, A2A/Wire, Bill Pay, RDC, Cards, Zelle), the Enterprise Event System, Operational Data Integration (ODI), and the Digital Core. Banno''s developer documentation site at jackhenry.dev is mirrored at banno.github.io/open-api-docs.'
examples:
- key_count: 13
  name: Banno Admin Institution Abilities Response Example
  slug: banno-admin-institution-abilities-response-example
- key_count: 6
  name: Banno Consumer Create Transfer Request Example
  slug: banno-consumer-create-transfer-request-example
- key_count: 8
  name: Banno Consumer Create Transfer Response Example
  slug: banno-consumer-create-transfer-response-example
- key_count: 1
  name: Banno Consumer List Accounts Response Example
  slug: banno-consumer-list-accounts-response-example
- key_count: 2
  name: Banno Consumer List Transactions Response Example
  slug: banno-consumer-list-transactions-response-example
- key_count: 9
  name: Jxchange Customer Response Example
  slug: jxchange-customer-response-example
- key_count: 8
  name: Payments Ach Credit Request Example
  slug: payments-ach-credit-request-example
- key_count: 5
  name: Payments Ach Credit Response Example
  slug: payments-ach-credit-response-example
- key_count: 7
  name: Payments Orchestrator Route Request Example
  slug: payments-orchestrator-route-request-example
- key_count: 4
  name: Payments Orchestrator Route Response Example
  slug: payments-orchestrator-route-response-example
finops:
- name: Jack Henry Finops
  service_category: ''
  slug: jack-henry-finops
image: https://avatars.githubusercontent.com/u/1130370?s=200&v=4
json_schemas:
- name: Banno Account
  property_count: 14
  slug: banno-account
- name: Banno Institution Abilities Map
  property_count: 0
  slug: banno-institution-abilities
- name: Banno Transaction
  property_count: 13
  slug: banno-transaction
- name: Banno Transfer
  property_count: 8
  slug: banno-transfer
- name: jXchange Customer
  property_count: 9
  slug: jxchange-customer
- name: jXchange Loan Account
  property_count: 11
  slug: jxchange-loan-account
- name: Jack Henry Payments ACH Transaction
  property_count: 6
  slug: payments-ach-transaction
json_structures:
- name: Banno Account Structure
  property_count: 0
  slug: banno-account-structure
- name: Banno Transaction Structure
  property_count: 0
  slug: banno-transaction-structure
- name: Payments Orchestrator Request Structure
  property_count: 0
  slug: payments-orchestrator-request-structure
jsonld:
- class_count: 26
  name: Jack Henry Context
  property_count: 8
  slug: jack-henry-context
layout: provider
modified: '2026-05-23'
name: Jack Henry & Associates
nav: Providers
network: true
overview: 'Jack Henry & Associates publishes 38 APIs on the [APIs.io](https://apis.io/) network, including Enterprise Event System, Abilities API, Accounts API, and 35 more. Tagged areas include Financial Services, Banking, Core Banking, Digital Banking, and Payments.


  The Jack Henry & Associates catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 6 Spectral governance rulesets.


  Jack Henry & Associates'' developer surface includes authentication, documentation, engineering blog, GitHub presence, Stack Overflow tag, support, status page, and 13 more developer resources.'
plans:
- name: Jack Henry Plans Pricing
  plan_count: 2
  slug: jack-henry-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 0
  name: Jack Henry Rate Limits
  slug: jack-henry-rate-limits
rules:
- name: Jack Henry & Associates API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: banno-admin-api-rules
- name: Jack Henry & Associates API Rules
  rule_count: 5
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 1
  slug: banno-consumer-api-rules
- name: Jack Henry & Associates API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: jack-henry-asyncapi-spectral-rules
- name: Jack Henry & Associates API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: jack-henry-jsonschema-spectral-rules
- name: Jack Henry & Associates API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: jack-henry-payments-rules
- name: Jack Henry & Associates API Rules
  rule_count: 3
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 1
  slug: jxchange-rest-rules
score:
  band: thin
  composite: 41.7
  delta: -5.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.1
    developer_ergonomics: 34.8
    discoverability: 68.5
    governance: 20.8
    operational_transparency: 5.3
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 37
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/jack-henry/refs/heads/main/screenshots/jack-henry-2026-06-20T183648.png
security:
- kind: authentication
  name: Jack Henry Authentication
  slug: jack-henry-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Jack Henry Domain Security
  slug: jack-henry-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: jack-henry
tags:
- Financial Services
- Banking
- Core Banking
- Digital Banking
- Payments
- Lending
- Fraud
- Open Banking
- Community Banks
- Credit Unions
- Fintech
- OAuth
- OpenID Connect
website: https://www.jackhenry.com/
---
