---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: platform
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 69
  human_in_the_loop: 0
  name: Nmi Agentic Access
  operation_count: 108
  slug: nmi-agentic-access
  summary_line: 108 operations · 69 acting
api_count: 9
apis:
- description: The NMI Three Step Redirect API keeps merchants outside the scope of transmitting sensitive payment data by routing cardholder information directly to NMI servers. Supports transaction, recurring bill
  name: NMI Three Step Redirect API
  slug: nmi-three-step-redirect-api
- description: The NMI Customer-Present Cloud API enables browser-based point-of-sale payment processing without software installation. Supports cloud device registration and control, payment requests on connected d
  name: NMI Customer-Present Cloud API
  slug: nmi-customer-present-cloud-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: Here you can find information about webhook events
  name: NMI Webhook Events API
  slug: nmi-payments-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: The Affiliates API from NMI — 1 operation(s) for affiliates.
  name: NMI Affiliates API
  slug: nmi-affiliates-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: Here you can find information about endpoints that are related to Apple Pay.
  name: NMI Apple Pay API
  slug: nmi-apple-pay-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: Manage merchant applications
  name: NMI Applications API
  slug: nmi-applications-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: The Authorization endpoint allows clients to securely authenticate and obtain an access token for making requests to the API.
  name: NMI Authentication API
  slug: nmi-authentication-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: 'Authvia TXT2PAY® allows your merchants to request payments by text, with no download required. With NMI’s seamless Authvia integration, you can enable your merchants to create new text conversations, '
  name: NMI Authvia TXT2PAY API
  slug: nmi-authvia-txt2pay-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: The Billing & Commission API from NMI — 2 operation(s) for billing & commission.
  name: NMI Billing & Commission API
  slug: nmi-billing-commission-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: The Component Sessions API from NMI — 1 operation(s) for component sessions.
  name: NMI Component Sessions API
  slug: nmi-component-sessions-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: Customer vault management endpoints
  name: NMI Customers API
  slug: nmi-customers-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: Query API (query.php) for retrieving transaction, subscription, and invoice data. Intended for existing Classic integrations.
  name: NMI Data and Transaction Reporting API
  slug: nmi-data-and-transaction-reporting-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: Cloud device management and payment request endpoints
  name: NMI Devices API
  slug: nmi-devices-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: The Fee Schedule API from NMI — 2 operation(s) for fee schedule.
  name: NMI Fee Schedule API
  slug: nmi-fee-schedule-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: Gateway Features
  name: NMI Gateway Features API
  slug: nmi-gateway-features-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: Invoice management endpoints
  name: NMI Invoicing API
  slug: nmi-invoicing-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: The Marketplace App API from NMI — 1 operation(s) for marketplace app.
  name: NMI Marketplace App API
  slug: nmi-marketplace-app-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: The Merchants API from NMI — 4 operation(s) for merchants.
  name: NMI Merchants API
  slug: nmi-merchants-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: Get all the information required for application submissions
  name: NMI Packages API
  slug: nmi-packages-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: Recurring payment plan management endpoints
  name: NMI Plans API
  slug: nmi-plans-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: Here you can find information about endpoints that provide general services that are useful across a variety workflows.
  name: NMI Processors and Services API
  slug: nmi-processors-and-services-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: Product management endpoints for the Product Manager
  name: NMI Products API
  slug: nmi-products-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: The Settlement Time API from NMI — 1 operation(s) for settlement time.
  name: NMI Settlement Time API
  slug: nmi-settlement-time-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: Subscription management endpoints
  name: NMI Subscriptions API
  slug: nmi-subscriptions-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: Core payment processing operations including credit card, ACH, and cash transactions
  name: NMI Transactions API
  slug: nmi-transactions-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: The Users API from NMI — 2 operation(s) for users.
  name: NMI Users API
  slug: nmi-users-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: Here you can find information about webhook events
  name: NMI Webhook Events API
  slug: nmi-webhook-events-api
- baseURL: https://secure.networkmerchants.com
  baseurl_source: declared
  description: Manage Webhook Subscriptions
  name: NMI Webhook Subscriptions API
  slug: nmi-webhook-subscriptions-api
artifact_total: 63
asyncapis:
- description: ''
  name: Nmi Webhooks
  slug: nmi-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/agentic-access/nmi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nmi-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/rules/nmi-rules.yml
  title: ''
  type: Spectral
  url: rules/nmi-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/json-ld/nmi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nmi-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/vocabulary/nmi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nmi-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/asyncapi/nmi-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/nmi-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/data-model/nmi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nmi-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/conventions/nmi-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/nmi-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/conventions/nmi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nmi-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/errors/nmi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nmi-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/conformance/nmi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nmi-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/llms/nmi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nmi-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/mcp/nmi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/nmi-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/well-known/nmi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nmi-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/hosts/nmi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nmi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/vendors/nmi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nmi-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nmi.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nmi.com/policy/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.nmi.com/about-us/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.nmi.com/about-us/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/scopes/nmi-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/nmi-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/authentication/nmi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nmi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://nmi.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/security/nmi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nmi-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://docs.nmi.com
- group: other
  title: ''
  type: Developer Experience
  url: https://www.nmi.com/dev-experience/
- group: build
  title: ''
  type: SDKs
  url: https://www.nmi.com/payment-gateway-sdks-apis/
- group: start
  title: ''
  type: Integration Portal
  url: https://secure.networkmerchants.com/gw/merchants/resources/integration/integration_portal.php
- group: start
  title: ''
  type: Sandbox
  url: https://docs.nmi.com/docs/sandbox-testing
- group: operate
  title: ''
  type: Support
  url: https://support.nmi.com
- group: company
  title: ''
  type: Blog
  url: https://www.nmi.com/blog/
- group: operate
  title: ''
  type: Contact
  url: https://www.nmi.com/about-us/contact-us/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: NMI is a global embedded payments enablement platform providing full-stack payment technology with REST APIs for payment processing, tokenization, recurring billing, customer vault management, and payment facilitation across ecommerce, in-person, mobile, and unattended acquisition channels. With over 20 years of operation, NMI connects 1.2 million active merchants, 6,000 channel partners, and 150+ processor connections, processing over $502 billion in annual payments volume.
finops:
- has_sources: false
  method: generated
  name: Finops
  primary_unit: ''
  service_category: ''
  slug: finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nmi.png
json_schemas:
- name: ACH - Credit
  property_count: 0
  slug: nmi-achcredit-request
- name: ACH - Sale
  property_count: 0
  slug: nmi-achsale-request
- name: application-document
  property_count: 7
  slug: nmi-application-document
- name: Response
  property_count: 29
  slug: nmi-assign-fee-schedule-to-merchant-response
- name: ConversationAmountInput
  property_count: 0
  slug: nmi-conversation-amount-input
- name: ConversationCustomerPhoneWithDashes
  property_count: 0
  slug: nmi-conversation-customer-phone-with-dashes
- name: ConversationExpirationDateInput
  property_count: 0
  slug: nmi-conversation-expiration-date-input
- name: ConversationId
  property_count: 0
  slug: nmi-conversation-id
- name: ConversationInstructions
  property_count: 0
  slug: nmi-conversation-instructions
- name: Response
  property_count: 29
  slug: nmi-create-merchant-response
- name: Credit Card - Capture
  property_count: 0
  slug: nmi-credit-card-capture-request
- name: Credit Card - Complete Partial Payment in Full
  property_count: 0
  slug: nmi-credit-card-payment-in-full-partial-request
- name: Credit Card - Sale
  property_count: 0
  slug: nmi-credit-card-sale-request
- name: full-application
  property_count: 7
  slug: nmi-full-application
- name: Response
  property_count: 8
  slug: nmi-get-merchant-list-response
- name: Report Response
  property_count: 8
  slug: nmi-get-merchant-processors-and-value-added-services-details-response
- name: Response
  property_count: 27
  slug: nmi-get-specific-merchant-information-response
- name: Response
  property_count: 8
  slug: nmi-get-transaction-data-response
- name: NmiRecordId
  property_count: 0
  slug: nmi-nmi-record-id
- name: Collection of Fields
  property_count: 6
  slug: nmi-package-collection
- name: package-fields
  property_count: 0
  slug: nmi-package-fields
- name: pagination
  property_count: 4
  slug: nmi-pagination
- name: Response
  property_count: 19
  slug: nmi-response
- name: subscription
  property_count: 6
  slug: nmi-subscription
jsonld:
- class_count: 120
  name: Nmi Context
  property_count: 423
  slug: nmi-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.nmi.com over HTTP; 7 tools listed.
  name: NMI MCP Server
  slug: nmi
modified: '2026-09-16'
name: NMI
nav: Providers
network: true
overview: 'NMI publishes 28 API contracts indexed on the [APIs.io](https://apis.io/) network, including Webhook Events API, Affiliates API, Apple Pay API, and 25 more. Tagged areas include Payments, Payment Gateway, Payment Processing, Tokenization, and Recurring Billing.


  The NMI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  NMI''s developer surface includes authentication, developer portal, sandbox, support, engineering blog, and 29 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 16
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: NMI API Rules
  rule_count: 13
  severity_counts:
    error: 6
    hint: 0
    info: 2
    warn: 5
  slug: nmi-rules
scopes:
- name: Nmi Scopes
  scope_count: 6
  slug: nmi-scopes
  summary_line: 6 scopes · clientCredentials
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 68.8
    catalog_earned_first_party: 0.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 21.2
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 73.6
    developer_ergonomics: 48.8
    discoverability: 83.3
    operational_transparency: 7.9
  previous_composite: 25.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 26
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/screenshots/nmi-2026-06-20T190340.png
security:
- kind: authentication
  name: Nmi Authentication
  slug: nmi-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Nmi Domain Security
  slug: nmi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nmi
tags:
- Payments
- Payment Gateway
- Payment Processing
- Tokenization
- Recurring Billing
- Customer Vault
- Fintech
- Embedded Payments
- Payment Facilitation
website: https://nmi.com
---
