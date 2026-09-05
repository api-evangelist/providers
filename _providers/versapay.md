---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 54
  human_in_the_loop: 2
  name: Versapay Agentic Access
  operation_count: 106
  slug: versapay-agentic-access
  summary_line: 106 operations · 54 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: The Agreements API from Versapay — 7 operation(s) for agreements.
  name: Versapay Agreements API
  slug: versapay-agreements-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: 'Visit your account settings in `UAT` (https://uat.versapay.com/account) or `Production` (https://secure.versapay.com/account) to setup API credentials needed for authentication as well as webhooks to '
  name: Versapay Authentication API
  slug: versapay-authentication-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: Autopays are a digital analog to paper pre-authorized debit agreements that businesses could use, for instance, for monthly billing.
  name: Versapay Autopay API
  slug: versapay-autopay-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: Card Present EMV payment transactions require a Versapay certified point-of-sale terminal. Contact support@versapay.com for support & setup for POS/CP EMV enablement.
  name: Versapay Card Present EMV API
  slug: versapay-card-present-emv-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: As a supplier your customers collaborate with you through comments about invoices and/or payments.
  name: Versapay Collaboration API
  slug: versapay-collaboration-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: 'As a supplier your customers are the entities that are invoiced. ## Webhooks When using Webhooks, your application will be notified when key events are triggered for a customer.'
  name: Versapay Customers API
  slug: versapay-customers-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: Operations available to developers
  name: Versapay Developers API
  slug: versapay-developers-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: As a supplier divisions are used to group your invoices.
  name: Versapay Divisions API
  slug: versapay-divisions-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: As a supplier you can upload customer, invoice, and payment data in CSV file formats.
  name: Versapay File Imports API
  slug: versapay-file-imports-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: The Fund Sources API from Versapay — 2 operation(s) for fund sources.
  name: Versapay Fund Sources API
  slug: versapay-fund-sources-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: Provisioned gift cards can be activated/enabled (or deactivated/disabled) as well as have their balances loaded/re-loaded with an amount. Contact support@versapay.com for support & setup for Gift Card
  name: Versapay Gift Cards API
  slug: versapay-gift-cards-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: Operations intended only to the iframe front end
  name: Versapay Internal API
  slug: versapay-internal-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: 'As a supplier invoices are your receivables. ## Webhooks When using Webhooks, your application will be notified when key events are triggered for an invoice.'
  name: Versapay Invoices API
  slug: versapay-invoices-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: 'As a supplier a payments are made by customers for invoices issued to them. ## Webhooks When using Webhooks, your application will be notified when key events are triggered for a payment.'
  name: Versapay Invoicing Payments API
  slug: versapay-invoicing-payments-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: As a supplier you can notify customers about their invoices.
  name: Versapay Notifications API
  slug: versapay-notifications-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: Onboarding supports the automated process of applying for merchant services. Contact support@versapay.com for support & setup of supplier onboarding partner credentials.
  name: Versapay Onboarding API
  slug: versapay-onboarding-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: Order-based card/ACH and card present EMV payment transactions include verify, authorize, capture, sale, void, return refund, and return credit transaction types. If participating in a gift card progr
  name: Versapay Order Transactions API
  slug: versapay-order-transactions-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: The Order entity represents the sales document in the ERP system. The fields in the ERP system should be aligned as closely as possible with the fields in the order entity, as the gateway will use the
  name: Versapay Orders API
  slug: versapay-orders-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: For convenience purposes only, Versapay can supply third party reference data to its partners and users. This data can be used to implement client-side tooling (e.g., fraud mitigation services), but i
  name: Versapay Reference Data API
  slug: versapay-reference-data-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: Settlement Reporting includes retrieval of monthly statements, daily deposit amounts (including fee information), transaction exceptions (ACH reject/return & CC chargeback), and transaction details. C
  name: Versapay Settlement Reporting API
  slug: versapay-settlement-reporting-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: The Transactions API from Versapay — 4 operation(s) for transactions.
  name: Versapay Transactions API
  slug: versapay-transactions-api
- baseURL: https://secure.versapay.com
  baseurl_source: declared
  description: The Wallet entity holds vaulted & secured payment methods owned by a customer (buyer/payor) that can be used to make payments via Collaborative AR (online Portals, AutoPay, Pay Now), Order Transaction
  name: Versapay Wallets API
  slug: versapay-wallets-api
artifact_total: 29
asyncapis:
- description: ''
  name: Versapay Webhooks
  slug: versapay-webhooks
collections:
- collection_type: open
  name: Versapay API Reference
  slug: open-versapay-api-reference
- collection_type: open
  name: Versapay Ecommerce API
  slug: open-versapay-ecommerce-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/versapay-api-reference-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/versapay-ecommerce-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/versapay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/versapay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/versapay-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/versapay-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/versapay-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/versapay-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/versapay-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/versapay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/versapay-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/versapay-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/versapay-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/versapay-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/versapay-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://versapay.com/security
- group: start
  title: ''
  type: Sandbox
  url: sandbox/versapay-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/versapay-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/versapay-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/versapay-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://versapay.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.versapay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.versapay.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.versapay.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.versapay.com
- group: company
  title: ''
  type: Blog
  url: https://versapay.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://secure.versapay.com/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://versapay.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://versapay.com/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://versapay.com/security
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/versapay
created: '2026-07-24'
description: 'Versapay is a Toronto, Canada based B2B payments company focused on accounts receivable (AR) automation and integrated payment acceptance for suppliers and their buyers. Its "Collaborative AR" platform combines electronic invoicing, customer collaboration, cash application, and embedded payment processing so businesses can invoice, get paid, and reconcile inside one workflow, with ERP-adjacent integrations for order-to-cash. Versapay serves the North American mid-market and enterprise segment and, unlike consumer money-movement players in Canada''s Interac-dominated market, sits in the API-native B2B acquiring and AR/AP money-movement layer. Its API posture is genuinely public and honest: developers.versapay.com hosts a Redocly-rendered reference for a broad REST platform API (onboarding, wallets, orders, order transactions, gift cards, card-present EMV, settlement reporting, autopay, customers, invoices, divisions, notifications, and webhooks) plus a separate hosted-iframe
  Ecommerce API for PCI-reduced payment sessions. Authentication is HTTPS Basic access authentication using an API Token and Key issued from the account console, with a UAT sandbox alongside production and a documented webhook event model.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Versapay
nav: Providers
network: true
overview: 'Versapay publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Agreements API, Authentication API, Autopay API, and 19 more. Tagged areas include Payments, Canada, Accounts Receivable, AR Automation, and Order-to-Cash.


  The Versapay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Versapay''s developer surface includes authentication, sandbox, documentation, API reference, engineering blog, signup flow, and 26 more developer resources.'
random_paper: 14
scopes:
- name: Versapay Scopes
  scope_count: 5
  slug: versapay-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials/password
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 57.2
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 75.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/versapay/refs/heads/main/screenshots/versapay-2026-08-17T082740.png
security:
- kind: authentication
  name: Versapay Authentication
  slug: versapay-authentication
  summary_line: http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Versapay Domain Security
  slug: versapay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: versapay
tags:
- Payments
- Canada
- Accounts Receivable
- AR Automation
- Order-to-Cash
- Payment Acceptance
- Payment Processing
- B2B Payments
- Invoicing
- E-Commerce
- Card Present
- Webhook
website: https://versapay.com
---
