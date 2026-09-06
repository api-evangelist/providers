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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 72
  human_in_the_loop: 2
  name: Fat Zebra Agentic Access
  operation_count: 133
  slug: fat-zebra-agentic-access
  summary_line: 133 operations · 72 acting · 2 human-in-the-loop
api_count: 4
apis:
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: A merchant's connections to acquirers — board, list, update, enable/disable.
  name: Fat Zebra Acquirer connections API
  slug: fat-zebra-acquirer-connections-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The acquirer catalogue this partner may board onto.
  name: Fat Zebra Acquirers API
  slug: fat-zebra-acquirers-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Applicable Surcharge API from Fat Zebra — 1 operation(s) for applicable surcharge.
  name: Fat Zebra Applicable Surcharge API
  slug: fat-zebra-applicable-surcharge-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Authenticate API from Fat Zebra — 3 operation(s) for authenticate.
  name: Fat Zebra Authenticate API
  slug: fat-zebra-authenticate-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Bank Accounts API from Fat Zebra — 2 operation(s) for bank accounts.
  name: Fat Zebra Bank Accounts API
  slug: fat-zebra-bank-accounts-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Batches API from Fat Zebra — 4 operation(s) for batches.
  name: Fat Zebra Batches API
  slug: fat-zebra-batches-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Chargebacks API from Fat Zebra — 4 operation(s) for chargebacks.
  name: Fat Zebra Chargebacks API
  slug: fat-zebra-chargebacks-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Credit Cards API from Fat Zebra — 3 operation(s) for credit cards.
  name: Fat Zebra Credit Cards API
  slug: fat-zebra-credit-cards-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Customers API from Fat Zebra — 3 operation(s) for customers.
  name: Fat Zebra Customers API
  slug: fat-zebra-customers-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Direct Credits API from Fat Zebra — 3 operation(s) for direct credits.
  name: Fat Zebra Direct Credits API
  slug: fat-zebra-direct-credits-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Direct Debits API from Fat Zebra — 3 operation(s) for direct debits.
  name: Fat Zebra Direct Debits API
  slug: fat-zebra-direct-debits-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Disputes API from Fat Zebra — 1 operation(s) for disputes.
  name: Fat Zebra Disputes API
  slug: fat-zebra-disputes-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Fat Zebra Billing API from Fat Zebra — 1 operation(s) for fat zebra billing.
  name: Fat Zebra Fat Zebra Billing API
  slug: fat-zebra-fat-zebra-billing-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Health API from Fat Zebra — 2 operation(s) for health.
  name: Fat Zebra Health API
  slug: fat-zebra-health-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Invoice Imports API from Fat Zebra — 1 operation(s) for invoice imports.
  name: Fat Zebra Invoice Imports API
  slug: fat-zebra-invoice-imports-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Invoices API from Fat Zebra — 2 operation(s) for invoices.
  name: Fat Zebra Invoices API
  slug: fat-zebra-invoices-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Merchants API from Fat Zebra — 7 operation(s) for merchants.
  name: Fat Zebra Merchants API
  slug: fat-zebra-merchants-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Oauth Clients API from Fat Zebra — 1 operation(s) for oauth clients.
  name: Fat Zebra Oauth Clients API
  slug: fat-zebra-oauth-clients-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The authenticated partner (self).
  name: Fat Zebra Partner API
  slug: fat-zebra-partner-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Payment Plans API from Fat Zebra — 2 operation(s) for payment plans.
  name: Fat Zebra Payment Plans API
  slug: fat-zebra-payment-plans-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Paypal API from Fat Zebra — 15 operation(s) for paypal.
  name: Fat Zebra Paypal API
  slug: fat-zebra-paypal-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Purchases API from Fat Zebra — 11 operation(s) for purchases.
  name: Fat Zebra Purchases API
  slug: fat-zebra-purchases-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Refunds API from Fat Zebra — 3 operation(s) for refunds.
  name: Fat Zebra Refunds API
  slug: fat-zebra-refunds-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Reports API from Fat Zebra — 2 operation(s) for reports.
  name: Fat Zebra Reports API
  slug: fat-zebra-reports-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Settlement API from Fat Zebra — 1 operation(s) for settlement.
  name: Fat Zebra Settlement API
  slug: fat-zebra-settlement-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: Partner SSO enforcement — read state, enforce, disable.
  name: Fat Zebra SSO API
  slug: fat-zebra-sso-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Transactions API from Fat Zebra — 2 operation(s) for transactions.
  name: Fat Zebra Transactions API
  slug: fat-zebra-transactions-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: Partner dashboard users — CRUD plus deactivate/reactivate.
  name: Fat Zebra Users API
  slug: fat-zebra-users-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Utilities API from Fat Zebra — 3 operation(s) for utilities.
  name: Fat Zebra Utilities API
  slug: fat-zebra-utilities-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Utlities API from Fat Zebra — 1 operation(s) for utlities.
  name: Fat Zebra Utlities API
  slug: fat-zebra-utlities-api
- baseURL: https://gateway.pmnts.io/v1.0
  baseurl_source: declared
  description: The Web Hooks API from Fat Zebra — 2 operation(s) for web hooks.
  name: Fat Zebra Web Hooks API
  slug: fat-zebra-web-hooks-api
artifact_total: 40
asyncapis:
- description: ''
  name: Fat Zebra Webhooks
  slug: fat-zebra-webhooks
collections:
- collection_type: open
  name: Fat Zebra Billing
  slug: open-fat-zebra-billing
- collection_type: open
  name: FDMS TPP Merchant Onboarding
  slug: open-fat-zebra-fdms-tpp-merchant-onboarding
- collection_type: open
  name: gateway
  slug: open-fat-zebra-gateway
- collection_type: open
  name: Fat Zebra Partner API
  slug: open-fat-zebra-partner
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/fat-zebra-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fat-zebra-gateway-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fat-zebra-partner-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fat-zebra-billing-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fat-zebra-fdms-tpp-merchant-onboarding-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fat-zebra-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fat-zebra-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fat-zebra-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fat-zebra-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.fatzebra.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.fatzebra.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fatzebra.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fatzebra.com/reference/purchases
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fatzebra.com/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.fatzebra.com/changelog/welcome-to-pmnts
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fatzebra
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fatzebra.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fatzebra.com/platform/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.fatzebra.com/company/news
- group: operate
  title: ''
  type: Support
  url: https://www.fatzebra.com/contact/support
- group: auth
  title: ''
  type: Security
  url: https://www.fatzebra.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fatzebra.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/fat-zebra-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fat-zebra-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fat-zebra-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fat-zebra-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/fat-zebra-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fat-zebra-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/fat-zebra-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.fatzebra.com/docs/pci-certification
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fat-zebra-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/fat-zebra-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fat-zebra-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.fatzebra.com/changelog/welcome-to-pmnts
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fat-zebra-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fat-zebra-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/fat-zebra-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/fat-zebra-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fat-zebra-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fat-zebra-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/fat-zebra-accept-a-card-payment.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/fat-zebra-authorize-and-capture.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/fat-zebra-tokenize-and-charge.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/fat-zebra-board-a-submerchant.md
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fat-zebra-changelog.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.fatzebra.com/contact/sales
created: '2026-07-24'
description: Fat Zebra is an Australian payments company (founded 2012, Sydney) providing a card-present and card-not-present payment gateway and processing platform for merchants, ISOs, and software platforms across Australia and New Zealand. Its API-first Gateway handles Visa, Mastercard, and Amex purchases, authorizations and captures, refunds and voids, card tokenization, 3D Secure, recurring payment plans, direct debits and direct credits over local bank rails, chargeback handling, batch processing, and hosted payment pages (PayNow), alongside wallet acceptance for Apple Pay, Google Pay, and Click to Pay. A separate Partner API lets platforms and ISOs create and board their own sub-merchants onto acquirer connections programmatically. The developer surface is a genuine, well-documented ReadMe hub at docs.fatzebra.com with four downloadable OpenAPI definitions, and the runtime platform is branded pmnts (gateway.pmnts.io). Authentication is HTTP Basic using a username and API token.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Fat Zebra
nav: Providers
network: true
overview: 'Fat Zebra publishes 31 APIs on the [APIs.io](https://apis.io/) network, including Acquirer connections API, Acquirers API, Applicable Surcharge API, and 28 more. Tagged areas include Payments, Australia, Payment Gateway, Payment Processing, and Acquiring.


  The Fat Zebra catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fat Zebra''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, pricing, engineering blog, and 39 more developer resources.'
random_paper: 10
score:
  band: strong
  composite: 56.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 65.8
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 43.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 56.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 58.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fat-zebra/refs/heads/main/screenshots/fat-zebra-2026-07-25T214245.png
security:
- kind: authentication
  name: Fat Zebra Authentication
  slug: fat-zebra-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fat Zebra Domain Security
  slug: fat-zebra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fat Zebra Trust Center
  slug: fat-zebra-trust-center
  summary_line: PCI DSS
slug: fat-zebra
tags:
- Payments
- Australia
- Payment Gateway
- Payment Processing
- Acquiring
- Card Payments
- Tokenization
- Recurring Billing
- Direct Debit
- Hosted Payment Pages
- Merchant Onboarding
website: https://www.fatzebra.com/
---
