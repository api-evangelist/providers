---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 204
  human_in_the_loop: 12
  name: Marqeta Agentic Access
  operation_count: 436
  slug: marqeta-agentic-access
  summary_line: 436 operations · 204 acting · 12 human-in-the-loop
api_count: 81
apis:
- description: Outbound HTTP webhook delivery for card events, authorization requests, advice messages, transactions, and account events.
  name: Marqeta Webhooks
  slug: webhooks
- description: Synchronous webhook-style HTTP endpoint customers expose for Marqeta to call during card authorization for approve/decline decisions.
  name: Marqeta Risk Controller / Real-Time Decisioning
  slug: risk-controller
- description: The accepted countries API from Marqeta — 2 operation(s) for accepted countries.
  name: Marqeta accepted countries API
  slug: marqeta-accepted-countries-api
- description: The Account API from Marqeta — 2 operation(s) for account.
  name: Marqeta Account API
  slug: marqeta-account-api
- description: The Account Bundle Transitions API from Marqeta — 2 operation(s) for account bundle transitions.
  name: Marqeta Account Bundle Transitions API
  slug: marqeta-account-bundle-transitions-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the account cards endpoints to create and retrieve credit cards that can access the credit line
  name: Marqeta Account Cards API
  slug: marqeta-account-cards-api
- description: The Account Documents API from Marqeta — 3 operation(s) for account documents.
  name: Marqeta Account Documents API
  slug: marqeta-account-documents-api
- description: The account holder groups API from Marqeta — 2 operation(s) for account holder groups.
  name: Marqeta account holder groups API
  slug: marqeta-account-holder-groups-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the account refunds endpoints to create and retrieve account refunds on Marqeta's credit platfo
  name: Marqeta Account Refunds API
  slug: marqeta-account-refunds-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the `/credit/accounts/{account_token}/rewards` endpoint to create a one-time reward on a <</cor
  name: Marqeta Account Rewards API
  slug: marqeta-account-rewards-api
- description: The Account Signup Bonus API from Marqeta — 1 operation(s) for account signup bonus.
  name: Marqeta Account Signup Bonus API
  slug: marqeta-account-signup-bonus-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the account transitions endpoints to create and retrieve account transitions on Marqeta's credi
  name: Marqeta Account Transitions API
  slug: marqeta-account-transitions-api
- description: The Accounts API from Marqeta — 1 operation(s) for accounts.
  name: Marqeta Accounts API
  slug: marqeta-accounts-api
- description: The AccountUsers API from Marqeta — 1 operation(s) for accountusers.
  name: Marqeta AccountUsers API
  slug: marqeta-accountusers-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the adjustments endpoints to create and retrieve account adjustments on Marqeta's credit platfo
  name: Marqeta Adjustments API
  slug: marqeta-adjustments-api
- description: The Admin API from Marqeta — 5 operation(s) for admin.
  name: Marqeta Admin API
  slug: marqeta-admin-api
- description: The auth controls API from Marqeta — 4 operation(s) for auth controls.
  name: Marqeta auth controls API
  slug: marqeta-auth-controls-api
- description: The auto reloads API from Marqeta — 2 operation(s) for auto reloads.
  name: Marqeta auto reloads API
  slug: marqeta-auto-reloads-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the credit balance refunds endpoint to issue a credit balance refund on <</core-api/credit-acco
  name: Marqeta Balance Refunds API
  slug: marqeta-balance-refunds-api
- description: The bank transfers API from Marqeta — 4 operation(s) for bank transfers.
  name: Marqeta bank transfers API
  slug: marqeta-bank-transfers-api
- description: The bulk issuances API from Marqeta — 2 operation(s) for bulk issuances.
  name: Marqeta bulk issuances API
  slug: marqeta-bulk-issuances-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] The bundles feature on Marqeta's credit platform enables you to create and manage bundles by choosi
  name: Marqeta Bundles API
  slug: marqeta-bundles-api
- description: The business transitions API from Marqeta — 3 operation(s) for business transitions.
  name: Marqeta business transitions API
  slug: marqeta-business-transitions-api
- description: The businesses API from Marqeta — 10 operation(s) for businesses.
  name: Marqeta businesses API
  slug: marqeta-businesses-api
- description: The Card Group API from Marqeta — 2 operation(s) for card group.
  name: Marqeta Card Group API
  slug: marqeta-card-group-api
- description: The card products API from Marqeta — 2 operation(s) for card products.
  name: Marqeta card products API
  slug: marqeta-card-products-api
- description: The card transitions API from Marqeta — 3 operation(s) for card transitions.
  name: Marqeta card transitions API
  slug: marqeta-card-transitions-api
- description: The cardholder balances API from Marqeta — 3 operation(s) for cardholder balances.
  name: Marqeta cardholder balances API
  slug: marqeta-cardholder-balances-api
- description: The cards API from Marqeta — 11 operation(s) for cards.
  name: Marqeta cards API
  slug: marqeta-cards-api
- description: The chargebacks API from Marqeta — 9 operation(s) for chargebacks.
  name: Marqeta chargebacks API
  slug: marqeta-chargebacks-api
- description: The commando modes API from Marqeta — 4 operation(s) for commando modes.
  name: Marqeta commando modes API
  slug: marqeta-commando-modes-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the credit account disputes endpoints to create and manage disputes on a <</core-api/credit-acc
  name: Marqeta Credit Account Disputes API
  slug: marqeta-credit-account-disputes-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the credit accounts endpoints to create and manage accounts on Marqeta's credit platform. A cre
  name: Marqeta Credit Accounts API
  slug: marqeta-credit-accounts-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] [IMPORTANT] This feature is deprecated and replaced by credit product policies, which is part of th
  name: Marqeta Credit Products API
  slug: marqeta-credit-products-api
- description: '// Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Credit substatuses can be applied to credit accounts or credit account holders. Substatuses should '
  name: Marqeta Credit Substatuses API
  slug: marqeta-credit-substatuses-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the delinquency endpoints to retrieve details on a credit account's delinquency state and trans
  name: Marqeta Delinquency API
  slug: marqeta-delinquency-api
- description: The Depositaccounts API from Marqeta — 1 operation(s) for depositaccounts.
  name: Marqeta Depositaccounts API
  slug: marqeta-depositaccounts-api
- description: '// Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] The Marqeta platform facilitates the use of digital wallets for storing tokenized cards and making '
  name: Marqeta Digital Wallets Management API
  slug: marqeta-digital-wallets-management-api
- description: The direct deposit accounts API from Marqeta — 9 operation(s) for direct deposit accounts.
  name: Marqeta direct deposit accounts API
  slug: marqeta-direct-deposit-accounts-api
- description: The direct deposits API from Marqeta — 5 operation(s) for direct deposits.
  name: Marqeta direct deposits API
  slug: marqeta-direct-deposits-api
- description: The fee charges API from Marqeta — 3 operation(s) for fee charges.
  name: Marqeta fee charges API
  slug: marqeta-fee-charges-api
- description: The fee refunds API from Marqeta — 1 operation(s) for fee refunds.
  name: Marqeta fee refunds API
  slug: marqeta-fee-refunds-api
- description: The Feedback API from Marqeta — 1 operation(s) for feedback.
  name: Marqeta Feedback API
  slug: marqeta-feedback-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] // This source file is used by InfoDev to generate API reference documentation. File location in Gi
  name: Marqeta Fees API
  slug: marqeta-fees-api
- description: The funding sources API from Marqeta — 20 operation(s) for funding sources.
  name: Marqeta funding sources API
  slug: marqeta-funding-sources-api
- description: The gpa orders API from Marqeta — 4 operation(s) for gpa orders.
  name: Marqeta gpa orders API
  slug: marqeta-gpa-orders-api
- description: The Internal - BIN Pools API from Marqeta — 2 operation(s) for internal - bin pools.
  name: Marqeta Internal - BIN Pools API
  slug: marqeta-internal-bin-pools-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the journal entries endpoints to retrieve journal entries made on an <</core-api/credit-account
  name: Marqeta Journal Entries API
  slug: marqeta-journal-entries-api
- description: The kyc API from Marqeta — 4 operation(s) for kyc.
  name: Marqeta kyc API
  slug: marqeta-kyc-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] [IMPORTANT] ==== This feature is deprecated and replaced by journal entries. &#160; + For documenta
  name: Marqeta Ledger Entries API
  slug: marqeta-ledger-entries-api
- description: Retrieve funding load transaction data at a specified aggregation level. Covers all load types including ACH, push-to-card, and program transfers.
  name: Marqeta Loads API
  slug: marqeta-loads-api
- description: The mcc groups API from Marqeta — 2 operation(s) for mcc groups.
  name: Marqeta mcc groups API
  slug: marqeta-mcc-groups-api
- description: The merchantgroups API from Marqeta — 2 operation(s) for merchantgroups.
  name: Marqeta merchantgroups API
  slug: marqeta-merchantgroups-api
- description: The Migrations API from Marqeta — 3 operation(s) for migrations.
  name: Marqeta Migrations API
  slug: marqeta-migrations-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the payment schedule endpoints to create and retrieve payment schedules and payment schedule tr
  name: Marqeta Payment Schedules API
  slug: marqeta-payment-schedules-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the payment sources endpoint to link an external payment source to an <</core-api/credit-accoun
  name: Marqeta Payment Sources API
  slug: marqeta-payment-sources-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the payments endpoints to create and retrieve payments made on a <</core-api/credit-accounts, c
  name: Marqeta Payments API
  slug: marqeta-payments-api
- description: The peer transfers API from Marqeta — 5 operation(s) for peer transfers.
  name: Marqeta peer transfers API
  slug: marqeta-peer-transfers-api
- description: The ping API from Marqeta — 1 operation(s) for ping.
  name: Marqeta ping API
  slug: marqeta-ping-api
- description: '// Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the `/pins` endpoint to create, update, or reveal a personal identification number (PIN) for a '
  name: Marqeta PINs API
  slug: marqeta-pins-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] The Marqeta credit platform's policies feature enables you to customize the configurations of polic
  name: Marqeta Policies API
  slug: marqeta-policies-api
- description: Retrieve program funding balance data for financial reconciliation. Includes beginning and ending bank balances, amounts to send, and settlement details aggregated over configurable time periods.
  name: Marqeta Program Balances API
  slug: marqeta-program-balances-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the Credit Program Gateways endpoints to create, retrieve, and update Program Gateways for your
  name: Marqeta Program Gateways API
  slug: marqeta-program-gateways-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the Program Reserve API to retrieve program reserve account balances and transactions.
  name: Marqeta Program Reserve API
  slug: marqeta-program-reserve-api
- description: '// Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] A program transfer moves funds from an account holder''s general purpose account (GPA) to a program '
  name: Marqeta Program Transfers API
  slug: marqeta-program-transfers-api
- description: The ProgramFunding API from Marqeta — 2 operation(s) for programfunding.
  name: Marqeta ProgramFunding API
  slug: marqeta-programfunding-api
- description: The push to card API from Marqeta — 4 operation(s) for push to card.
  name: Marqeta push to card API
  slug: marqeta-push-to-card-api
- description: Marqeta enables you to assess fees in real time through the use of real-time fee groups. A real-time fee group is a collection of fees associated with an account holder group (and thereby associated w
  name: Marqeta Real-Time Fee Groups API
  slug: marqeta-real-time-fee-groups-api
- description: The Refunds API from Marqeta — 1 operation(s) for refunds.
  name: Marqeta Refunds API
  slug: marqeta-refunds-api
- description: The Rewards API from Marqeta — 1 operation(s) for rewards.
  name: Marqeta Rewards API
  slug: marqeta-rewards-api
- description: The simulate API from Marqeta — 10 operation(s) for simulate.
  name: Marqeta simulate API
  slug: marqeta-simulate-api
- description: The Spaces API from Marqeta — 3 operation(s) for spaces.
  name: Marqeta Spaces API
  slug: marqeta-spaces-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Use the statements endpoints to retrieve statement information or statement files for a <</core-api
  name: Marqeta Statements API
  slug: marqeta-statements-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] // This source file is used by InfoDev to generate API reference documentation. // File location in
  name: Marqeta Transactions API
  slug: marqeta-transactions-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] // This source file is used by InfoDev to generate API reference documentation. // File location in
  name: Marqeta User Transitions API
  slug: marqeta-user-transitions-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] // This source file is used by InfoDev to generate API reference documentation. // File location in
  name: Marqeta Users API
  slug: marqeta-users-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] A velocity control limits how much users can spend. You can configure velocity controls to limit ho
  name: Marqeta Velocity Controls API
  slug: marqeta-velocity-controls-api
- description: The Velocity Controls Card Group Balance API from Marqeta — 1 operation(s) for velocity controls card group balance.
  name: Marqeta Velocity Controls Card Group Balance API
  slug: marqeta-velocity-controls-card-group-balance-api
- description: View endpoints provide programmatic access to aggregated platform data derived from card program activity. Each view represents a specific dataset such as transactions, balances, or card states, aggre
  name: Marqeta Views API
  slug: marqeta-views-api
- description: The web push provisioning API from Marqeta — 1 operation(s) for web push provisioning.
  name: Marqeta web push provisioning API
  slug: marqeta-web-push-provisioning-api
- description: // Conditional snippet for beta or internal content include::../../maturity-admonition-banner.adoc[] Webhooks are notifications about API events, sent as they occur. The Marqeta platform sends these n
  name: Marqeta Webhooks API
  slug: marqeta-webhooks-api
artifact_total: 99
asyncapis:
- description: Marqeta delivers real-time event notifications to a developer-configured HTTPS endpoint when specific events occur within a card program. Each program supports up to five active webhook configurations
  name: Marqeta Webhooks
  slug: marqeta-webhooks-asyncapi
collections:
- collection_type: open
  name: Core API
  slug: open-marqeta-core-api
- collection_type: open
  name: Marqeta DiVA API
  slug: open-marqeta-diva-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/marqeta-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/marqeta-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/marqeta-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marqeta-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/marqeta-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/marqeta
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/marqeta
- group: company
  title: ''
  type: Website
  url: https://www.marqeta.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/marqeta-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/marqeta-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/marqeta-finops.yml
created: '2026-05-08'
description: Marqeta is a modern card-issuing and embedded-finance platform. The Core API is a large RESTful surface covering cards, users, businesses, GPA orders, KYC/KYB, fee transfer, transactions, real-time decisioning, MCC groups, programs, and webhooks. The Diva (Digital Wallets, Tokenization, 3DS) API extends the Core API.
finops:
- name: Marqeta Finops
  service_category: FinTech
  slug: marqeta-finops
graphqls:
- description: This conceptual GraphQL schema represents the Marqeta card-issuing and payment processing platform. Marqeta's Core API is a RESTful surface, and this schema captures an equivalent GraphQL model coveri
  name: Marqeta GraphQL Schema
  slug: marqeta-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marqeta.png
json_schemas:
- name: Marqeta Card
  property_count: 20
  slug: marqeta-card
- name: Marqeta Cardholder
  property_count: 26
  slug: marqeta-cardholder
- name: Marqeta Transaction
  property_count: 25
  slug: marqeta-transaction
jsonld:
- class_count: 0
  name: Marqeta Context
  property_count: 13
  slug: marqeta-context
layout: provider
modified: '2026-05-08'
name: Marqeta
nav: Providers
network: true
overview: 'Marqeta publishes 79 APIs on the [APIs.io](https://apis.io/) network, including accepted countries API, Account API, Account Bundle Transitions API, and 76 more. Tagged areas include FinTech, BaaS, Card Issuing, Payments, and Embedded Finance.


  The Marqeta catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Marqeta''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: Marqeta Plans Pricing
  plan_count: 2
  slug: marqeta-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 2
  name: Marqeta Rate Limits
  slug: marqeta-rate-limits
rules:
- name: Marqeta API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: marqeta-asyncapi-spectral-rules
- name: Marqeta API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: marqeta-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.3
  delta: -5.5
  facets:
    commercial_clarity: 36.8
    contract_quality: 73.7
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 41.7
    operational_transparency: 26.3
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 79
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 43.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/marqeta/refs/heads/main/screenshots/marqeta-2026-06-20T185001.png
security:
- kind: authentication
  name: Marqeta Authentication
  slug: marqeta-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Marqeta Domain Security
  slug: marqeta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Marqeta Vulnerability Disclosure
  slug: marqeta-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Marqeta Trust Center
  slug: marqeta-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: marqeta
tags:
- FinTech
- BaaS
- Card Issuing
- Payments
- Embedded Finance
website: https://www.marqeta.com/
---
