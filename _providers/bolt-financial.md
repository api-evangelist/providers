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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.1
  scored_at: '2026-09-05'
api_count: 4
apis:
- description: 'Bolt exposes two Model Context Protocol surfaces: a hosted documentation MCP server advertised at help.boltapp.com/mcp with search_docs, get_doc_page and list_doc_sections tools, and a Speakeasy-gener'
  name: Bolt MCP Servers
  slug: mcp
- baseURL: https://api.boltapp.com
  baseurl_source: declared
  description: Use the Account endpoint to view and manage customer accounts. Perform actions such as creating an account, updating an address, or adding a payment method. This endpoint is for merchants using the Ac
  name: Bolt Financial Account API
  slug: bolt-financial-account-api
- baseURL: https://api.boltapp.com
  baseurl_source: declared
  description: Implement Callback endpoints on your servers to power Bolt experiences. Different Bolt packages require different callbacks to be implemented. Consult your relevant product documentation for a list of
  name: Bolt Financial Callbacks API
  slug: bolt-financial-callbacks-api
- baseURL: https://api.boltapp.com
  baseurl_source: declared
  description: Use this resource to retrieve and set Merchant Callback URLs. Bolt uses these URLs to exchange information with your commerce server. See our related guide [About the Merchant Callback API](https://he
  name: Bolt Financial Configuration API
  slug: bolt-financial-configuration-api
- baseURL: https://api.boltapp.com
  baseurl_source: declared
  description: Use this endpoint to retrieve an OAuth token. Use the token to allow your ecommerce server to make calls to the Account endpoint and create a one-click checkout experience for shoppers. See related gu
  name: Bolt Financial O Auth API
  slug: bolt-financial-oauth-api
- baseURL: https://api.boltapp.com
  baseurl_source: declared
  description: Use the Orders API to interact with the customer's cart throughout the checkout process. Pre-checkout, perform actions such as validating inventory, verifying discounts, and calculating taxes. Post-ch
  name: Bolt Financial Orders API
  slug: bolt-financial-orders-api
- baseURL: https://api.boltapp.com
  baseurl_source: declared
  description: Use the Payments API to process credit card and alternative payment methods with Bolt.
  name: Bolt Financial Payments API
  slug: bolt-financial-payments-api
- baseURL: https://api.boltapp.com
  baseurl_source: declared
  description: '[Statements](/merchants/references/financials/statements/) are available in the Merchant Dashboard for merchants who use Bolt Payments as their processor. Merchants using other processors do not recei'
  name: Bolt Financial Statements API
  slug: bolt-financial-statements-api
- baseURL: https://api.boltapp.com
  baseurl_source: declared
  description: 'Use the Subscriptions endpoint to manage merchant-side recurring subscriptions created through Bolt Charge: list and retrieve subscriptions, cancel or pause/unpause them, view generated orders, and co'
  name: Bolt Financial Subscriptions API
  slug: bolt-financial-subscriptions-api
- baseURL: https://api.boltapp.com
  baseurl_source: declared
  description: The testing endpoint allows you to test various functionality within Bolt. Create a test credit card to process a test payment in your store. You can also simulate tracking an order’s shipment and pro
  name: Bolt Financial Testing API
  slug: bolt-financial-testing-api
- baseURL: https://api.boltapp.com
  baseurl_source: declared
  description: The Tokenizer API from Bolt Financial — 2 operation(s) for tokenizer.
  name: Bolt Financial Tokenizer API
  slug: bolt-financial-tokenizer-api
- baseURL: https://api.boltapp.com
  baseurl_source: declared
  description: Use the Transactions endpoint to authorize payments when the shopper checks out and handle post authorization actions such as captures and refunds. You can use a shopper's existing saved payment infor
  name: Bolt Financial Transactions API
  slug: bolt-financial-transactions-api
- baseURL: https://api.boltapp.com
  baseurl_source: declared
  description: Set up webhooks to notify your backend of events within Bolt. These webhooks can communicate with your OMS or other systems to keep them up to date with Bolt. See our related guide on [Webhooks](https
  name: Bolt Financial Webhooks API
  slug: bolt-financial-webhooks-api
artifact_total: 22
asyncapis:
- description: ''
  name: Bolt Financial Webhooks
  slug: bolt-financial-webhooks
collections:
- collection_type: open
  name: Bolt API Reference
  slug: open-bolt-financial-bolt-api
- collection_type: open
  name: Embedded API Reference
  slug: open-bolt-financial-embeddable-checkout-v1
- collection_type: open
  name: Bolt API Reference
  slug: open-bolt-financial-embeddable-checkout-v3
- collection_type: open
  name: Tokenizer Endpoint
  slug: open-bolt-financial-tokenizer
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/bolt-financial-bolt-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/bolt-financial-embeddable-checkout-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/bolt-financial-embeddable-checkout-v3-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/bolt-financial-tokenizer-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bolt-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bolt.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.boltapp.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://help.boltapp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.boltapp.com/api-bolt/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.boltapp.com/getting-started/introduction/
- group: operate
  title: ''
  type: Support
  url: https://help.boltapp.com/support
- group: company
  title: ''
  type: Blog
  url: https://boltapp.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BoltApp
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/bolt-inc/bolt-public
- group: commercial
  title: ''
  type: Pricing
  url: https://help.boltapp.com/dashboard/billing/fees/
- group: start
  title: ''
  type: SignUp
  url: https://merchant.boltapp.com/onboarding
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boltapp.com/end-user-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boltapp.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bolt.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bolt-financial-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/bolt-financial-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bolt-financial-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bolt-financial-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bolt-financial-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/bolt-financial-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bolt-financial-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/bolt-financial-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/bolt-financial-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bolt-financial-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bolt-financial-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bolt-financial-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bolt-financial-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/bolt-financial-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bolt-financial-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/bolt-financial-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bolt-financial-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bolt-financial-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-31'
description: 'Bolt Financial, Inc. is an American commerce technology company that gives retailers a one-click, identity-powered checkout backed by a shopper account network, payments processing, tokenization and fraud protection. Merchants integrate Bolt either through platform plugins (Adobe Commerce/Magento, BigCommerce, Salesforce Commerce Cloud, Shopify, WooCommerce) or directly against a REST API surface that covers shopper accounts, order tokens, transaction authorize/capture/refund/void, subscriptions, product catalog, merchant statements, webhooks and a hosted card tokenizer. Bolt publishes OpenAPI 3.0 definitions for its Bolt API, Embeddable Checkout v1 and v3, and Tokenizer endpoints, ships first-party SDKs for TypeScript, Python, C#, Go, PHP, iOS/Swift, Android/Kotlin, React Native, Unity and Unreal, and maintains an explicit agent-facing surface: an llms.txt index, a hosted documentation MCP server and two published agent skills.'
image: https://kinlane-productions2.s3.amazonaws.com/api-evangelist-site/company-images/bolt-financial.png
layout: provider
mcp_servers:
- description: ''
  name: Bolt Financial MCP Server
  slug: bolt-financial-mcp-server
modified: '2026-07-31'
name: Bolt Financial
nav: Providers
network: true
overview: 'Bolt Financial publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Account API, Callbacks API, Configuration API, and 9 more. Tagged areas include Company, Payments, Checkout, E-Commerce, and Fintech.


  The Bolt Financial catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bolt Financial''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
random_paper: 4
scopes:
- name: Bolt Financial Scopes
  scope_count: 4
  slug: bolt-financial-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 63.0
    developer_ergonomics: 79.8
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 59.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 78.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bolt-financial/refs/heads/main/screenshots/bolt-financial-2026-08-07T162709.png
security:
- kind: authentication
  name: Bolt Financial Authentication
  slug: bolt-financial-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Bolt Financial Domain Security
  slug: bolt-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bolt-financial
tags:
- Company
- Payments
- Checkout
- E-Commerce
- Fintech
- Subscription
- Tokenization
- Fraud
- Identity
- Webhook
website: https://www.bolt.com
---
