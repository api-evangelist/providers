---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 25
  human_in_the_loop: 1
  name: Tink Com Agentic Access
  operation_count: 63
  slug: tink-com-agentic-access
  summary_line: 63 operations · 25 acting · 1 human-in-the-loop
api_count: 25
apis:
- description: User bank accounts and balances.
  name: Tink Accounts API
  slug: tink-com-accounts-api
- description: Account ownership verification reports.
  name: Tink AccountVerificationReports API
  slug: tink-com-accountverificationreports-api
- description: On-demand balance refresh.
  name: Tink BalanceRefresh API
  slug: tink-com-balancerefresh-api
- description: Personal and business budgets.
  name: Tink Budgets API
  slug: tink-com-budgets-api
- description: Business account ownership verification reports.
  name: Tink BusinessAccountVerificationReports API
  slug: tink-com-businessaccountverificationreports-api
- description: Cash flow summaries.
  name: Tink CashFlow API
  slug: tink-com-cashflow-api
- description: Tink categorisation taxonomy.
  name: Tink Categories API
  slug: tink-com-categories-api
- description: Partner-ingested accounts.
  name: Tink ConnectorAccounts API
  slug: tink-com-connectoraccounts-api
- description: Partner-ingested transactions.
  name: Tink ConnectorTransactions API
  slug: tink-com-connectortransactions-api
- description: Categorised and merchant-enriched transactions.
  name: Tink EnrichedTransactions API
  slug: tink-com-enrichedtransactions-api
- description: Expense verification reports.
  name: Tink ExpenseChecks API
  slug: tink-com-expensechecks-api
- description: Financial calendar events and reconciliations.
  name: Tink FinancialCalendar API
  slug: tink-com-financialcalendar-api
- description: Account holder identities returned by the bank.
  name: Tink Identities API
  slug: tink-com-identities-api
- description: Income verification reports.
  name: Tink IncomeChecks API
  slug: tink-com-incomechecks-api
- description: Investment accounts and holdings.
  name: Tink Investments API
  slug: tink-com-investments-api
- description: Loan accounts.
  name: Tink Loans API
  slug: tink-com-loans-api
- description: Recurring payment mandates.
  name: Tink Mandates API
  slug: tink-com-mandates-api
- description: Token, authorization, and delegated grant endpoints.
  name: Tink OAuth API
  slug: tink-com-oauth-api
- description: Payment initiation, status, cancel, and refund.
  name: Tink Payments API
  slug: tink-com-payments-api
- description: Recurring transaction detection and prediction.
  name: Tink RecurringTransactions API
  slug: tink-com-recurringtransactions-api
- description: Risk categorisation reports.
  name: Tink RiskCategorisation API
  slug: tink-com-riskcategorisation-api
- description: Risk decisioning reports.
  name: Tink RiskInsights API
  slug: tink-com-riskinsights-api
- description: User bank transactions.
  name: Tink Transactions API
  slug: tink-com-transactions-api
- description: Permanent user lifecycle management.
  name: Tink User API
  slug: tink-com-user-api
- description: Webhook endpoint management.
  name: Tink WebhookEndpoints API
  slug: tink-com-webhookendpoints-api
arazzos:
- description: List a user's accounts, read the balances of a chosen account, then list its transactions.
  name: Tink Account And Transactions Overview
  slug: tink-com-account-transactions-overview-workflow
- description: Create a Tink Link session pre-loaded with identity, then retrieve the resulting Account Check report as JSON and PDF.
  name: Tink Account Check Verification And Report Retrieval
  slug: tink-com-account-verification-report-workflow
- description: Trigger an on-demand balance refresh for a credentials object, then poll until it finishes, then read fresh balances.
  name: Tink Trigger A Balance Refresh And Poll It
  slug: tink-com-balance-refresh-poll-workflow
- description: Initiate a Pay by Bank payment, then poll the payment until it reaches a terminal status.
  name: Tink Initiate A Payment And Poll Its Status
  slug: tink-com-initiate-payment-poll-status-workflow
- description: Create a recurring payment mandate for a user, then read it back to confirm it is active.
  name: Tink Create A Payment Mandate And Confirm It
  slug: tink-com-mandate-setup-workflow
- description: Confirm a payment is executed, initiate a refund, then poll the refund until it reaches a terminal status.
  name: Tink Refund An Executed Payment And Poll The Refund
  slug: tink-com-payment-refund-poll-workflow
- description: List a user's provider consents and credentials, then delete the credentials object to revoke the underlying bank consent.
  name: Tink Review And Revoke A Bank Consent
  slug: tink-com-provider-consent-cleanup-workflow
- description: Read a user's confirmed recurring transactions and category taxonomy, create a business budget around them, then read the budget's progress.
  name: Tink Build A Budget From Recurring Spend
  slug: tink-com-recurring-spend-budget-workflow
- description: Create a permanent Tink user, delegate bank authorization, exchange the code for a user token, and list their accounts.
  name: Tink Onboard A User And Access Their Bank Data
  slug: tink-com-user-data-access-workflow
- description: Register a webhook endpoint for selected event types, read it back to capture its signing secret, then confirm it is enabled in the endpoint list.
  name: Tink Register And Verify A Webhook Endpoint
  slug: tink-com-webhook-endpoint-setup-workflow
artifact_total: 99
collections:
- collection_type: postman
  name: Tink Account Check API
  slug: postman-tink-account-check-api
- collection_type: postman
  name: Tink Connector API
  slug: postman-tink-connector-api
- collection_type: postman
  name: Tink Data API
  slug: postman-tink-data-api
- collection_type: postman
  name: Tink Data Enrichment API
  slug: postman-tink-data-enrichment-api
- collection_type: postman
  name: Tink Money Manager API
  slug: postman-tink-money-manager-api
- collection_type: postman
  name: Tink OAuth and Authorization API
  slug: postman-tink-oauth-api
- collection_type: postman
  name: Tink Payments API
  slug: postman-tink-payments-api
- collection_type: postman
  name: Tink Risk and Reports API
  slug: postman-tink-risk-reports-api
- collection_type: postman
  name: Tink Webhooks API
  slug: postman-tink-webhooks-api
- collection_type: open
  name: Tink Account Check API
  slug: open-tink-account-check-api
- collection_type: open
  name: Tink Connector API
  slug: open-tink-connector-api
- collection_type: open
  name: Tink Data API
  slug: open-tink-data-api
- collection_type: open
  name: Tink Data Enrichment API
  slug: open-tink-data-enrichment-api
- collection_type: open
  name: Tink Money Manager API
  slug: open-tink-money-manager-api
- collection_type: open
  name: Tink OAuth and Authorization API
  slug: open-tink-oauth-api
- collection_type: open
  name: Tink Payments API
  slug: open-tink-payments-api
- collection_type: open
  name: Tink Risk and Reports API
  slug: open-tink-risk-reports-api
- collection_type: open
  name: Tink Webhooks API
  slug: open-tink-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tink-com-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tink-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tink-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tink-com-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tink/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tink-com-account-transactions-overview-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tink-com-account-verification-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tink-com-balance-refresh-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tink-com-initiate-payment-poll-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tink-com-mandate-setup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tink-com-payment-refund-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tink-com-provider-consent-cleanup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tink-com-recurring-spend-budget-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tink-com-user-data-access-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tink-com-webhook-endpoint-setup-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://tink.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tink.com/
- group: start
  title: ''
  type: Console
  url: https://console.tink.com/
- group: start
  title: ''
  type: Signup
  url: https://tink.com/contact-sales/
- group: commercial
  title: ''
  type: Pricing
  url: https://tink.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tink.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.tink.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://tink.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tink.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tink.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://tink.com/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tink-ab
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tink-ab/
- group: build
  title: ''
  type: Postman
  url: https://github.com/tink-ab/tink-postman
- group: build
  title: ''
  type: Postman
  url: https://github.com/tink-ab/tink-postman-us
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tink-ab/tink-link-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tink-ab/tink-link-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tink-ab/tink-money-manager-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tink-ab/tink-money-manager-ios
- group: build
  title: ''
  type: Tools
  url: https://github.com/tink-ab/terraform-provider-buildkite
- group: design
  title: ''
  type: SpectralRules
  url: rules/tink-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tink-com-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tink-com-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/tink-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tink-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tink-com-finops.yml
created: '2026-05-25'
description: Tink, a Visa solution acquired in 2022, is a European Open Banking platform with 6,000+ bank connections across Europe and a US Pay by Bank stack. Tink exposes a single API for PSD2-aggregated bank data (Accounts, Transactions, Balances, Identities, Investments, Loans), value-added risk reports (Account Check, Business Account Check, Income Check, Expense Check, Risk Insights, Risk Categorisation), Money Manager BFM, Data Enrichment, and PSD2 Payment Initiation Services (Pay by Bank, Auto Payments, Variable Recurring Payments, Mandates, Refunds, Payouts). Authentication is OAuth 2.0 with delegated user consent through the Tink Link hosted flow.
examples:
- key_count: 7
  name: Tink Account Verification Report Example
  slug: tink-account-verification-report-example
- key_count: 11
  name: Tink Payment Example
  slug: tink-payment-example
- key_count: 9
  name: Tink Transaction Example
  slug: tink-transaction-example
features:
- description: PSD2 and non-PSD2 connectivity across the Nordics, UK, DACH, Benelux, France, Iberia, Italy, Ireland, and Poland.
  name: 6,000+ Bank Connections
- description: Single API for one-off payments, Variable Recurring Payments, Auto Payments, payouts, refunds, and mandates.
  name: PSD2 Payment Initiation
- description: Verified account ownership for individuals and businesses with optional identity match (name, DOB, address).
  name: Account Check and Business Account Check
- description: Lender-grade affordability and risk-decisioning reports built on aggregated bank data.
  name: Risk Insights and Risk Categorisation
- description: Verified income streams and categorised expenses for underwriting and KYC.
  name: Income Check and Expense Check
- description: Cash-flow summaries, budgets, financial calendar, and reconciliations for SMB and personal apps.
  name: Money Manager
- description: Tink categorisation taxonomy, merchant identification, and recurring-transaction detection and prediction.
  name: Data Enrichment
- description: Push partner-collected data into the Tink platform for downstream enrichment and reporting.
  name: Connector API
- description: Hosted bank-consent UX handling SCA and bank app-to-app redirects on mobile.
  name: Tink Link
- description: Asynchronous notifications for report completion, payment and refund status, and credentials updates.
  name: Webhooks
- description: Single PSD2 licensed integration removes the need for customers to obtain their own PSD2 authorisation.
  name: SOC 2 Type II and PSD2 Licence
finops:
- name: Tink Com Finops
  service_category: Open Banking
  slug: tink-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tink-com.png
integrations:
- description: Tink is a Visa solution following the 2022 acquisition; integrates with Visa's payment and risk products.
  name: Visa
- description: Pay by Bank rails for Adyen merchants.
  name: Adyen
- description: Open Banking data and payments connectivity for Revolut.
  name: Revolut
- description: Risk decisioning powered by Tink for the European consumer lender.
  name: Younited
- description: Account aggregation and risk reports for the Nordic digital bank.
  name: Bank Norwegian
- description: Payment Initiation Services for the Nordic communications and logistics group.
  name: PostNord Strålfors
json_schemas:
- name: Tink Account Verification Report
  property_count: 7
  slug: tink-account-verification-report
- name: Tink Payment
  property_count: 11
  slug: tink-payment
- name: Tink Transaction
  property_count: 9
  slug: tink-transaction
jsonld:
- class_count: 52
  name: Tink Com Context
  property_count: 0
  slug: tink-com-context
layout: provider
modified: '2026-05-25'
name: Tink
nav: Providers
network: true
overview: 'Tink publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, AccountVerificationReports API, BalanceRefresh API, and 22 more. Tagged areas include Open Banking, PSD2, Payment Initiation, Account Aggregation, and Risk Decisioning.


  The Tink catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tink''s developer surface includes authentication, developer portal, documentation, developer console, signup flow, pricing, changelog, and 34 more developer resources.'
plans:
- name: Tink Com Plans Pricing
  plan_count: 2
  slug: tink-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Tink Com Rate Limits
  slug: tink-com-rate-limits
rules:
- name: Tink API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: tink-com-jsonschema-spectral-rules
- name: Tink API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 3
  slug: tink-rules
score:
  band: strong
  composite: 64.4
  delta: -7.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 74.4
    developer_ergonomics: 56.5
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 78.9
  previous_composite: 71.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 44.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/tink-com/refs/heads/main/screenshots/tink-com-2026-06-20T195409.png
security:
- kind: authentication
  name: Tink Com Authentication
  slug: tink-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tink Com Domain Security
  slug: tink-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tink Com Vulnerability Disclosure
  slug: tink-com-vulnerability-disclosure
  summary_line: security.txt
slug: tink-com
solutions:
- description: Aggregation, money management, and PIS for retail and business banking platforms.
  name: Banking
- description: Income, expense, risk, and account verification for credit underwriting.
  name: Lending
- description: Pay by Bank, VRP, mandates, refunds, and payouts for ecommerce, billers, and PSPs.
  name: Payments
- description: Holdings, loans, and balance aggregation for wealth-management and PFM apps.
  name: Wealth and Investments
- description: Money Manager BFM, business budgets, cash-flow, and Business Account Check for SMB platforms.
  name: SMB
tags:
- Open Banking
- PSD2
- Payment Initiation
- Account Aggregation
- Risk Decisioning
- Pay by Bank
- Finance
- Banking
- Europe
- Visa
use_cases:
- description: Verify bank ownership and identity match in seconds with Account Check.
  name: Onboarding and KYC
- description: Risk Insights, Income Check, and Expense Check inform consumer and SMB lending decisions.
  name: Affordability and Underwriting
- description: Initiate account-to-account payments at checkout with one-off PIS or Auto Payments.
  name: Pay by Bank Checkout
- description: Sweeping Variable Recurring Payments collect recurring charges directly from the customer's bank.
  name: Subscription Billing
- description: Embed Money Manager dashboards in SMB banking and accounting apps.
  name: Business Financial Management
- description: Power personal finance experiences with categorised transactions and recurring detection.
  name: PFM and Personal Banking
- description: Disburse funds back to a verified bank account using PIS payouts.
  name: Payouts
- description: Stitch PSD2 data with partner-collected data via Connector API for a unified view.
  name: Open Finance Composition
website: https://tink.com/
---
