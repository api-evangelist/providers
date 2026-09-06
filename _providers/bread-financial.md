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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-09-05'
api_count: 13
apis:
- description: Next-generation Bread Pay REST API for managing buyers, merchant accounts, personalized payment options and pricing, and the merchant transaction lifecycle (authorize, capture, cancel, refund). Secure
  name: BreadPay Platform API
  slug: breadpay-platform-api
- description: The Bread Pay API enables merchants to integrate installment financing options into online and in-store checkout flows. Supports creating financing applications, retrieving loan statuses, managing tra
  name: Bread Pay API
  slug: bread-pay-api
- description: SplitPay is a short-term financing alternative for retail merchants, enabling customers to split purchases into manageable payments and helping retailers attract price-sensitive customers while increa
  name: Bread SplitPay API
  slug: split-pay-api
- baseURL: https://api.platform.breadpayments.com
  baseurl_source: declared
  description: Checkout supports the buyer's shopping journey — starting and decisioning a financing application, returning personalized payment agreement options, completing checkout in-store or online, and issuing
  name: BreadPay Checkout API
  slug: bread-pay-api
- description: SplitPay is Bread's short-term, card-funded split-payment product for retail merchants. It is delivered through the same BreadPay Platform contracts and the same hosted SDK as installment financing ra
  name: Bread SplitPay
  slug: split-pay-api
- baseURL: https://api.platform.breadpayments.com
  baseurl_source: declared
  description: The merchant-facing transaction lifecycle — authorize, settle, refund, cancel, rescind, extend expiration — plus carts, fulfillment detail, and settlement/funding/targeting reporting exports. Transact
  name: BreadPay Merchant Operations API
  slug: merchant-operations-api
- baseURL: https://api.platform.breadpayments.com
  baseurl_source: declared
  description: The buyer's post-purchase journey — payment agreements, balances and ledger breakdowns, autopay enrollment, scheduled and ad-hoc payments, refunds, fee and principal waivers, product disputes, deferre
  name: BreadPay Servicing API
  slug: servicing-api
- baseURL: https://api.platform.breadpayments.com
  baseurl_source: declared
  description: Registration, lookup and management of buyers and their contacts, credit-report data, status and authorized third parties, with fraud-management capabilities around allow-listing and self cure. Handle
  name: BreadPay Buyer Management API
  slug: buyer-management-api
- baseURL: https://api.platform.breadpayments.com
  baseurl_source: declared
  description: Stored payment methods and their access and transient tokens, ACH account unblocking, network token retrieval, payment execution and audit, refunds and payment reversal. 21 operations.
  name: BreadPay Payments API
  slug: payments-api
- baseURL: https://api.platform.breadpayments.com
  baseurl_source: declared
  description: Platform foundations — service-account authorization (HTTP Basic client credentials exchanged for a bearer JWT), buyer login and token refresh, org-token exchange, one-time verification codes, org cod
  name: BreadPay Foundations API
  slug: foundations-api
- baseURL: https://api.platform.breadpayments.com
  baseurl_source: declared
  description: Self-service webhook subscription management — create, update and delete subscriptions with NONE, BASIC or static-bearer subscriber auth, list delivered events by status, replay failed events by id, f
  name: BreadPay Webhook API
  slug: webhook-api
- baseURL: https://api.platform.breadpayments.com
  baseurl_source: declared
  description: Management of public programs, payment products and the policies that determine system behaviour and execution. Only one operation is published (getPaymentProductEnrollmentByMerchantID) against 47 com
  name: BreadPay Program API
  slug: program-api
- baseURL: https://api.platform.breadpayments.com
  baseurl_source: declared
  description: Streamlines the upgrade / trade-in flow for the Apple program — upgrade elections, trade-in payments, and linking an upgradeable loan to a payment agreement. 6 operations.
  name: BreadPay Tradein API
  slug: tradein-api
artifact_total: 16
asyncapis:
- description: ''
  name: Bread Financial Webhooks
  slug: bread-financial-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.breadfinancial.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform-docs.breadpayments.com/bread-developers/docs
- group: docs
  title: ''
  type: Documentation
  url: https://platform-docs.breadpayments.com/bread-developers/docs
- group: docs
  title: ''
  type: APIReference
  url: https://platform-docs.breadpayments.com/bread-developers/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://platform-docs.breadpayments.com/bread-developers/docs/api-access
- group: operate
  title: ''
  type: Support
  url: https://platform-docs.breadpayments.com/bread-onboarding/docs/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bppub
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.breadfinancial.com/en/privacy-policy.html
- group: build
  title: ''
  type: Packages
  url: packages/bread-financial-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bread-financial-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bread-financial-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/bread-financial-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bread-financial-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bread-financial-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bread-financial-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bread-financial-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/bread-financial-components.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bread-financial-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bread-financial-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bread-financial-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bread-financial-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getbread
- group: docs
  title: ''
  type: Documentation
  url: https://developers.breadfinancial.com/
created: '2026-07-17'
description: 'Bread Financial (formerly Alliance Data Systems) is a US consumer financial services company providing branded and co-brand credit cards, private-label and general-purpose lending, and point-of-sale buy-now-pay-later financing under the Bread Pay brand. Its developer surface, Bread Pay, exposes a REST API platform for merchants to embed installment and revolving financing into online and in-store checkout: the next-generation BreadPay Platform API (api.platform.breadpayments.com) manages buyers, merchant accounts, payment options, pricing, and the transaction lifecycle (authorize, capture, cancel, refund), secured with OAuth 2.0 client-credentials and JWT access tokens; a legacy Bread Classic Merchant API manages checkout carts and transactions; and browser (JavaScript) plus native iOS and Android SDKs render placements, prequalification (RTPS), and the Bread checkout modal on merchant storefronts. Bread also ships e-commerce platform plugins (Shopify, Magento 2, BigCommerce,
  WooCommerce, Miva, Volusion, Salesforce Commerce Cloud) and a partner sandbox. This profile was surfaced as a portfolio company of Bessemer Venture Partners.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bread-financial.png
layout: provider
modified: '2026-07-18'
name: Bread Financial
nav: Providers
network: true
overview: 'Bread Financial publishes 9 APIs on the [APIs.io](https://apis.io/) network, including BreadPay Checkout API, BreadPay Merchant Operations API, BreadPay Servicing API, and 6 more. Tagged areas include Company, Fintech, Payments, Buy Now Pay Later, and Lending.


  The Bread Financial catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bread Financial''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 17 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 65.9
    developer_ergonomics: 57.1
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 30.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/bread-financial/refs/heads/main/screenshots/bread-financial-2026-07-25T203733.png
security:
- kind: authentication
  name: Bread Financial Authentication
  slug: bread-financial-authentication
  summary_line: oauth2/http/apiKey · 3 schemes
- kind: domain-security
  name: Bread Financial Domain Security
  slug: bread-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bread-financial
tags:
- Company
- Fintech
- Payments
- Buy Now Pay Later
- Lending
- Consumer Finance
- Point-of-Sale
- E-Commerce
website: https://www.breadfinancial.com
---
