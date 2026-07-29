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
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: verified
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 65.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 73
  human_in_the_loop: 0
  name: Curlec Agentic Access
  operation_count: 136
  slug: curlec-agentic-access
  summary_line: 136 operations · 73 acting
api_count: 30
apis:
- description: Razorpay Billme digital receipts and bills for retail, food & beverage, events, and ecommerce.
  name: Curlec Bills API
  slug: curlec-bills-api
- description: Customer profiles store contact information for recurring billing, saved cards, and personalised checkout. Each email+contact combination must be unique.
  name: Curlec Customers API
  slug: curlec-customers-api
- description: Disputes (chargebacks) are raised by customers via their bank. You can accept (lose) or contest (challenge with evidence) each dispute. Monitor respond_by timestamp — missing the deadline forfeits the
  name: Curlec Disputes API
  slug: curlec-disputes-api
- description: Document uploads for dispute evidence. Upload JPEG, PNG, or PDF files and receive a document ID to reference in dispute contest submissions.
  name: Curlec Documents API
  slug: curlec-documents-api
- description: 'On-demand settlements let you transfer your available Razorpay balance to your bank account immediately, outside the normal settlement cycle. Fees apply. Requires Instant Settlements to be enabled on '
  name: Curlec Instant Settlements API
  slug: curlec-instant-settlements-api
- description: 'Invoices and payment pages for one-time or partial-payment collection. Create in draft, issue to the customer, and track payment status. Cannot be used for GST invoices (use the Dashboard for those). '
  name: Curlec Invoices API
  slug: curlec-invoices-api
- description: Reusable catalog items that can be referenced in invoice line items. Defining items once avoids repeating price and description on each invoice.
  name: Curlec Items API
  slug: curlec-items-api
- description: Sub-merchant accounts (Linked Accounts) created under a Route marketplace. Includes account creation, stakeholder KYC, and Route product activation. Uses /v2/ API base path. Only one stakeholder is al
  name: Curlec Linked Accounts API
  slug: curlec-linked-accounts-api
- description: Orders are the starting point for accepting a payment. Create an order with the amount and currency, pass the order_id to Razorpay Checkout, then verify the payment signature after success.
  name: Curlec Orders API
  slug: curlec-orders-api
- description: Sub-merchant account lifecycle management via Partners API (Aggregator/Platform model). Uses OAuth access_token authentication.
  name: Curlec Partner Accounts API
  slug: curlec-partner-accounts-api
- description: Upload and fetch KYC documents for sub-merchant accounts and their stakeholders.
  name: Curlec Partner Documents API
  slug: curlec-partner-documents-api
- description: Manage stakeholders (directors/executives) for sub-merchant accounts. Multiple stakeholders allowed per account.
  name: Curlec Partner Stakeholders API
  slug: curlec-partner-stakeholders-api
- description: Configure webhooks for sub-merchant accounts to receive payment events. Maximum 30 per account.
  name: Curlec Partner Webhooks API
  slug: curlec-partner-webhooks-api
- description: Scheduled and live downtime information for card, netbanking, and UPI. Poll or subscribe to payment.downtime webhooks to detect degraded methods and adjust your checkout UI.
  name: Curlec Payment Downtimes API
  slug: curlec-payment-downtimes-api
- description: Payment Links are shareable URLs to collect payments without a website. Share via SMS, email, or any channel. Supports partial payments, expiry, reminders, UPI-only mode, offers, and transfers to link
  name: Curlec Payment Links API
  slug: curlec-payment-links-api
- description: A payment is created when a customer completes checkout. Payments can be auto-captured or manually captured. Fetch payment details to reconcile and diagnose failures.
  name: Curlec Payments API
  slug: curlec-payments-api
- description: Billing plan definitions for recurring subscriptions. A plan sets the billing period, interval, and per-cycle charge. Plans are reusable across multiple subscriptions and cannot be modified after crea
  name: Curlec Plans API
  slug: curlec-plans-api
- description: QR Codes enable offline and digital payment collection. Customers scan with any UPI or card app. Supports fixed-amount and variable-amount codes, single-use and multiple-use modes.
  name: Curlec QR Codes API
  slug: curlec-qr-codes-api
- description: Refunds return captured payment amounts to customers. Normal refunds take 5-7 business days. Instant (optimum) refunds settle immediately but may fall back to normal. Use X-Refund-Idempotency header t
  name: Curlec Refunds API
  slug: curlec-refunds-api
- description: 'Settlements represent batch transfers of collected payment funds to your bank account. Use the recon endpoint for transaction-level reconciliation reports mapping each payment, refund, and adjustment '
  name: Curlec Settlements API
  slug: curlec-settlements-api
- description: Recurring billing subscriptions. Customers must authorize a payment mandate (UPI Autopay, NACH, or card-on-file) via the short_url before charges begin. Supports pause/resume, plan changes, add-ons, a
  name: Curlec Subscriptions API
  slug: curlec-subscriptions-api
- description: Fund transfers from a merchant, payment, or order to a Linked Account (Route). Supports payment-based splits, direct on-demand transfers, settlement hold controls, and full/partial reversals. INR only
  name: Curlec Transfers API
  slug: curlec-transfers-api
- description: Virtual bank accounts and UPI VPAs that accept NEFT/RTGS/IMPS/UPI payments (Smart Collect). Each incoming payment creates a BankTransfer entity. Supports Third Party Validation (TPV) to restrict payer
  name: Curlec Virtual Accounts API
  slug: curlec-virtual-accounts-api
- description: Penny drop and reverse penny drop bank/VPA validation
  name: Curlec X Account Validation API
  slug: curlec-x-account-validation-api
- description: Fetch RazorpayX account balances
  name: Curlec X Banking Balances API
  slug: curlec-x-banking-balances-api
- description: RazorpayX payout recipients — create, fetch, update contacts
  name: Curlec X Contacts API
  slug: curlec-x-contacts-api
- description: Payout destination accounts (bank, VPA, card) linked to contacts
  name: Curlec X Fund Accounts API
  slug: curlec-x-fund-accounts-api
- description: Payout links for recipients without saved fund accounts
  name: Curlec X Payout Links API
  slug: curlec-x-payout-links-api
- description: Disbursements via NEFT, RTGS, IMPS, UPI, card — includes composite and approval flows
  name: Curlec X Payouts API
  slug: curlec-x-payouts-api
- description: Fetch RazorpayX transaction records — credits (bank_transfer inflows) and debits (payout outflows)
  name: Curlec X Transactions API
  slug: curlec-x-transactions-api
artifact_total: 66
asyncapis:
- description: ''
  name: Curlec Webhooks
  slug: curlec-webhooks
collections:
- collection_type: postman
  name: Razorpay Bills API
  slug: postman-curlec-bills-api
- collection_type: postman
  name: Razorpay Bills Customers API
  slug: postman-curlec-customers-api
- collection_type: postman
  name: Razorpay Bills Disputes API
  slug: postman-curlec-disputes-api
- collection_type: postman
  name: Razorpay Bills Documents API
  slug: postman-curlec-documents-api
- collection_type: postman
  name: Razorpay Bills Instant Settlements API
  slug: postman-curlec-instant-settlements-api
- collection_type: postman
  name: Razorpay Bills Invoices API
  slug: postman-curlec-invoices-api
- collection_type: postman
  name: Razorpay Bills Items API
  slug: postman-curlec-items-api
- collection_type: postman
  name: Razorpay Bills Linked Accounts API
  slug: postman-curlec-linked-accounts-api
- collection_type: postman
  name: Razorpay Bills Orders API
  slug: postman-curlec-orders-api
- collection_type: postman
  name: Razorpay Bills Partner Accounts API
  slug: postman-curlec-partner-accounts-api
- collection_type: postman
  name: Razorpay Bills Partner Documents API
  slug: postman-curlec-partner-documents-api
- collection_type: postman
  name: Razorpay Bills Partner Stakeholders API
  slug: postman-curlec-partner-stakeholders-api
- collection_type: postman
  name: Razorpay Bills Partner Webhooks API
  slug: postman-curlec-partner-webhooks-api
- collection_type: postman
  name: Razorpay Bills Payment Downtimes API
  slug: postman-curlec-payment-downtimes-api
- collection_type: postman
  name: Razorpay Bills Payment Links API
  slug: postman-curlec-payment-links-api
- collection_type: postman
  name: Razorpay Bills Payments API
  slug: postman-curlec-payments-api
- collection_type: postman
  name: Razorpay Bills Plans API
  slug: postman-curlec-plans-api
- collection_type: postman
  name: Razorpay Bills QR Codes API
  slug: postman-curlec-qr-codes-api
- collection_type: postman
  name: Razorpay Bills Refunds API
  slug: postman-curlec-refunds-api
- collection_type: postman
  name: Razorpay Bills Settlements API
  slug: postman-curlec-settlements-api
- collection_type: postman
  name: Razorpay Bills Subscriptions API
  slug: postman-curlec-subscriptions-api
- collection_type: postman
  name: Razorpay Bills Transfers API
  slug: postman-curlec-transfers-api
- collection_type: postman
  name: Razorpay Bills Virtual Accounts API
  slug: postman-curlec-virtual-accounts-api
- collection_type: postman
  name: Razorpay Bills X Account Validation API
  slug: postman-curlec-x-account-validation-api
- collection_type: postman
  name: Razorpay Bills X Banking Balances API
  slug: postman-curlec-x-banking-balances-api
- collection_type: postman
  name: Razorpay Bills X Contacts API
  slug: postman-curlec-x-contacts-api
- collection_type: postman
  name: Razorpay Bills X Fund Accounts API
  slug: postman-curlec-x-fund-accounts-api
- collection_type: postman
  name: Razorpay Bills X Payout Links API
  slug: postman-curlec-x-payout-links-api
- collection_type: postman
  name: Razorpay Bills X Payouts API
  slug: postman-curlec-x-payouts-api
- collection_type: postman
  name: Razorpay Bills X Transactions API
  slug: postman-curlec-x-transactions-api
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/curlec-a2a.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/curlec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://curlec.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://curlec.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://curlec.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://curlec.com/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://curlec.com/docs/payments/
- group: auth
  title: ''
  type: Authentication
  url: https://curlec.com/docs/api/authentication/
- group: operate
  title: ''
  type: Support
  url: https://curlec.com/blog/knowledge-base/
- group: company
  title: ''
  type: Blog
  url: https://curlec.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/razorpay
- group: commercial
  title: ''
  type: Pricing
  url: https://curlec.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.curlec.com/
- group: start
  title: ''
  type: Login
  url: https://dashboard.curlec.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://curlec.com/blog/s/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://curlec.com/blog/s/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.razorpay.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://curlec.com/docs/api/changelog/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/razorpaydev/workspace/razorpay-public-workspace/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/curlec-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/curlec-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/curlec-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/curlec-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/curlec-packages.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/curlec-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/curlec-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/curlec-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/curlec-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/curlec-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/curlec-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/curlec-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/curlec-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/curlec-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/curlec-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/curlec-razorpay-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/curlec-llms.txt
- group: design
  title: ''
  type: Components
  url: components/curlec-components.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://curlec.com/docs/api/changelog/
created: '2026-07-17'
description: Curlec (Razorpay Curlec) is a Malaysian online payment solution and part of Razorpay, the RBI-authorised full-stack payment platform. Curlec lets businesses in Malaysia accept one-time and recurring payments through a Payment Gateway, Payment Links, Payment Pages, Payment Buttons, hosted Checkout, DuitNow real-time payments, FPX online banking, cards and e-wallets, plus Subscriptions and direct-debit recurring billing. It runs on the shared Razorpay REST API (https://api.razorpay.com/v1) — a RESTful, JSON, Basic-Auth API covering Orders, Payments, Refunds, Settlements, Disputes, Customers, Invoices, Plans, Subscriptions, Payment Links, QR Codes, Virtual Accounts, Transfers/Route, and the RazorpayX business-banking and payouts suite. Curlec exposes official server SDKs, webhooks, a sandbox test mode, a public Postman workspace, and an official hosted MCP server for AI-agent access.
image: https://curlec.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: curlec-mcp.yml
  slug: curlec-mcpyml
modified: '2026-07-18'
name: Curlec
nav: Providers
network: true
overview: 'Curlec publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Bills API, Customers API, Disputes API, and 27 more. Tagged areas include Company, Payments, Payment Gateway, Recurring Payments, and Subscriptions.


  The Curlec catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Curlec''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 32 more developer resources.'
random_paper: 6
scopes:
- name: Curlec Scopes
  scope_count: 1
  slug: curlec-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: strong
  composite: 64.6
  delta: -1.5
  facets:
    commercial_clarity: 52.6
    contract_quality: 70.5
    developer_ergonomics: 79.9
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 66.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 75.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/curlec/refs/heads/main/screenshots/curlec-2026-07-25T210942.png
security:
- kind: authentication
  name: Curlec Authentication
  slug: curlec-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Curlec Domain Security
  slug: curlec-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: curlec
tags:
- Company
- Payments
- Payment Gateway
- Recurring Payments
- Subscriptions
- Direct Debit
- FinTech
- Malaysia
- DuitNow
- FPX
- Webhooks
- Razorpay
website: https://curlec.com
---
