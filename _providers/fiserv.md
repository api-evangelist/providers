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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 28.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Fiserv Agentic Access
  operation_count: 42
  slug: fiserv-agentic-access
  summary_line: 42 operations · 27 acting
api_count: 4
apis:
- description: Fiserv provides webhook-based event notifications across the payments lifecycle. Merchants can subscribe to webhooks to receive real-time notifications for key events including transaction status chan
  name: Fiserv Payment Events
  slug: payment-events
- description: Manage 3-D Secure authentication flows for cardholder verification.
  name: Fiserv 3-D Secure API
  slug: fiserv-3-d-secure-api
- description: Create, retrieve, update, and manage deposit and loan accounts.
  name: Fiserv Accounts API
  slug: fiserv-accounts-api
- description: Authorize payment transactions against a cardholder account.
  name: Fiserv Authorization API
  slug: fiserv-authorization-api
- description: Create and manage transaction authorizations.
  name: Fiserv Authorizations API
  slug: fiserv-authorizations-api
- description: Look up Bank Identification Number (BIN) data for cards.
  name: Fiserv BIN API
  slug: fiserv-bin-api
- description: Cancel or void previously authorized transactions.
  name: Fiserv Cancels API
  slug: fiserv-cancels-api
- description: Capture previously authorized transactions for settlement.
  name: Fiserv Capture API
  slug: fiserv-capture-api
- description: Capture previously authorized transactions for settlement.
  name: Fiserv Captures API
  slug: fiserv-captures-api
- description: Issue, activate, manage, and retrieve card details.
  name: Fiserv Cards API
  slug: fiserv-cards-api
- description: Process payment charges including authorizations, sales, and pre-authorizations.
  name: Fiserv Charges API
  slug: fiserv-charges-api
- description: Retrieve funding information for settled transactions.
  name: Fiserv Funding API
  slug: fiserv-funding-api
- description: Inquire about the status of transactions and merchant information.
  name: Fiserv Inquire API
  slug: fiserv-inquire-api
- description: Manage credit, temporary credit, and cash limits.
  name: Fiserv Limits API
  slug: fiserv-limits-api
- description: Manage customer and party information including personal details and contact information.
  name: Fiserv Parties API
  slug: fiserv-parties-api
- description: Process payment transactions including credits, debits, and bill payments.
  name: Fiserv Payments API
  slug: fiserv-payments-api
- description: Manage stored customer payment profiles for recurring or future transactions.
  name: Fiserv Profile API
  slug: fiserv-profile-api
- description: Refund previously captured and settled transactions.
  name: Fiserv Refund API
  slug: fiserv-refund-api
- description: Process refunds against previously captured transactions.
  name: Fiserv Refunds API
  slug: fiserv-refunds-api
- description: Retrieve settlement status for processed transactions.
  name: Fiserv Settlement API
  slug: fiserv-settlement-api
- description: Submit signature capture data for completed transactions.
  name: Fiserv Signature Capture API
  slug: fiserv-signature-capture-api
- description: Retrieve account statements and statement transactions.
  name: Fiserv Statements API
  slug: fiserv-statements-api
- description: Create, manage, and use payment tokens for secure storage of payment credentials.
  name: Fiserv Tokens API
  slug: fiserv-tokens-api
- description: Retrieve and manage account transaction history and details.
  name: Fiserv Transactions API
  slug: fiserv-transactions-api
- description: Initiate and manage fund transfers between accounts.
  name: Fiserv Transfers API
  slug: fiserv-transfers-api
- description: Verify payment cards or tokens before processing a transaction.
  name: Fiserv Verifications API
  slug: fiserv-verifications-api
- description: Void previously authorized transactions before settlement.
  name: Fiserv Void API
  slug: fiserv-void-api
artifact_total: 73
asyncapis:
- description: Fiserv provides webhook-based event notifications across the payments lifecycle. Merchants can subscribe to webhooks to receive real-time notifications for key events including transaction status chan
  name: Fiserv Payment Events
  slug: fiserv-payment-events-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fiserv BankingHub 3-D Secure API
  slug: open-fiserv-3-d-secure-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Accounts API
  slug: open-fiserv-accounts-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Authorization API
  slug: open-fiserv-authorization-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Authorizations API
  slug: open-fiserv-authorizations-api
- collection_type: open
  name: Fiserv BankingHub API
  slug: open-fiserv-bankinghub
- collection_type: open
  name: Fiserv BankingHub 3-D Secure BIN API
  slug: open-fiserv-bin-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Cancels API
  slug: open-fiserv-cancels-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Capture API
  slug: open-fiserv-capture-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Captures API
  slug: open-fiserv-captures-api
- collection_type: open
  name: Fiserv CardDeveloper API
  slug: open-fiserv-carddeveloper
- collection_type: open
  name: Fiserv CardPointe Gateway API
  slug: open-fiserv-cardpointe-gateway
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Cards API
  slug: open-fiserv-cards-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Charges API
  slug: open-fiserv-charges-api
- collection_type: open
  name: Fiserv CommerceHub API
  slug: open-fiserv-commercehub
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Funding API
  slug: open-fiserv-funding-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Inquire API
  slug: open-fiserv-inquire-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Limits API
  slug: open-fiserv-limits-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Parties API
  slug: open-fiserv-parties-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Payments API
  slug: open-fiserv-payments-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Profile API
  slug: open-fiserv-profile-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Refund API
  slug: open-fiserv-refund-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Refunds API
  slug: open-fiserv-refunds-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Settlement API
  slug: open-fiserv-settlement-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Signature Capture API
  slug: open-fiserv-signature-capture-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Statements API
  slug: open-fiserv-statements-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Tokens API
  slug: open-fiserv-tokens-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Transactions API
  slug: open-fiserv-transactions-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Transfers API
  slug: open-fiserv-transfers-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Verifications API
  slug: open-fiserv-verifications-api
- collection_type: open
  name: Fiserv BankingHub 3-D Secure Void API
  slug: open-fiserv-void-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/fiserv-capability-edges.yml
- group: operate
  title: ''
  type: Community
  url: https://www.fiserv.com/en/forum
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fiserv.com/en/about-fiserv/privacy-notice.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fiserv.com/en/about-fiserv/terms-of-use.html
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fiserv-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fiserv-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fiserv-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Fiserv
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fiserv
- group: company
  title: ''
  type: Website
  url: https://www.fiserv.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fiserv.com/
- group: start
  title: ''
  type: Signup
  url: https://developer.fiserv.com/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/fiserv-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fiserv-payment-transaction-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fiserv-account-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.fiserv.dev/llms.txt
created: '2025-02-17'
description: Fiserv is a global provider of financial services technology solutions, offering a wide range of products and services to help clients in the banking, payments, and wealth management industries.
features:
- 'Fiserv: API access via partner / B2B contracts only'
- No public API pricing published — contact enterprise sales
- Fiserv (Clover + Carat + First Data) APIs sold via commercial agreements.
finops:
- name: Fiserv Finops
  service_category: Payment Processing
  slug: fiserv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fiserv.png
json_schemas:
- name: Fiserv Account
  property_count: 13
  slug: fiserv-account
- name: Fiserv Payment Transaction
  property_count: 14
  slug: fiserv-payment-transaction
jsonld:
- class_count: 0
  name: Fiserv Context
  property_count: 8
  slug: fiserv-context
layout: provider
modified: '2026-05-19'
name: Fiserv
nav: Providers
network: true
overview: 'Fiserv publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Payment Events, 3-D Secure API, Accounts API, and 24 more. Tagged areas include Banking, Financial, Payments, Wealth Management, and Fortune 500.


  The Fiserv catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Fiserv''s developer surface includes authentication, documentation, signup flow, and 13 more developer resources.'
plans:
- name: Fiserv Plans Pricing
  plan_count: 1
  slug: fiserv-plans-pricing
press:
- date: '2026-05-25'
  title: 'Fiserv: Financial Services Technology, Mobile Banking ...'
  url: https://www.fiserv.com/en.html
- date: '2026-05-25'
  title: Fiserv (@fiserv) • Instagram photos and videos
  url: https://www.instagram.com/fiserv/?hl=en
- date: '2026-05-25'
  title: Fiserv, Inc. (FISV) Stock Price, News, Quote & History
  url: https://finance.yahoo.com/quote/FISV/
- date: '2026-05-25'
  title: Fiserv
  url: https://www.linkedin.com/company/fiserv
- date: '2026-05-25'
  title: Fiserv
  url: https://en.wikipedia.org/wiki/Fiserv
random_paper: 4
rate_limits:
- limit_count: 1
  name: Fiserv Rate Limits
  slug: fiserv-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Fiserv API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: fiserv-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Fiserv API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: fiserv-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 18
    catalog_gap: 68.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 13.6
    contract_quality: 67.7
    developer_ergonomics: 14.3
    discoverability: 63.0
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fiserv/refs/heads/main/screenshots/fiserv-2026-08-17T083418.png
security:
- kind: authentication
  name: Fiserv Authentication
  slug: fiserv-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Fiserv Domain Security
  slug: fiserv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fiserv
tags:
- Banking
- Financial
- Payments
- Wealth Management
- Fortune 500
website: https://www.fiserv.com/
---
