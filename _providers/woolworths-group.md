---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 68.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Woolworths Group Agentic Access
  operation_count: 50
  slug: woolworths-group-agentic-access
  summary_line: 50 operations · 21 acting
api_count: 5
apis:
- description: Wpay digital acceptance platform documentation (Build with Wpay) for accepting online payments; its OpenAPI files at integration.wpay.com.au/openapi.v1.json self-identify as the Gr4vy API (servers api
  name: Wpay Digital Acceptance
  slug: wpay-digital-acceptance
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: Account Status Inquiry (ASI) or account verification is a type of authorisation that is done to check the validity of the card. From the perspective of the merchant, the only difference between a stan
  name: Woolworths Group Account Status Inquiry API
  slug: woolworths-group-accountstatusinquiry-api
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: The Activating Physical Gift Cards API from Woolworths Group — 1 operation(s) for activating physical gift cards.
  name: Woolworths Group Activating Physical Gift Cards API
  slug: woolworths-group-activating-physical-gift-cards-api
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: An authorization involves the bank’s approval of transactions that fall under a particular payment scheme. When you use a credit or scheme based debit card, the transaction request is sent to the card
  name: Woolworths Group Authorization API
  slug: woolworths-group-authorization-api
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: Captures are sent after an authorization. This request finalizes the transaction, and on approval the reserved funds are transferred from the cardholder’s account to the merchant’s account.
  name: Woolworths Group Capture API
  slug: woolworths-group-capture-api
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: Gifting Catalogue APIs
  name: Woolworths Group Gifting Catalogue API
  slug: woolworths-group-gifting-catalogue-api
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: The Health check API from Woolworths Group — 1 operation(s) for health check.
  name: Woolworths Group Health check API
  slug: woolworths-group-health-check-api
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: The Instruments API from Woolworths Group — 4 operation(s) for instruments.
  name: Woolworths Group Instruments API
  slug: woolworths-group-instruments-api
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: Create and manage API keys.
  name: Woolworths Group Key Management API
  slug: woolworths-group-key-management-api
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: The Order API from Woolworths Group — 4 operation(s) for order.
  name: Woolworths Group Order API
  slug: woolworths-group-order-api
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: The Ordering Digital Gift Cards API from Woolworths Group — 3 operation(s) for ordering digital gift cards.
  name: Woolworths Group Ordering Digital Gift Cards API
  slug: woolworths-group-ordering-digital-gift-cards-api
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: The Payments API from Woolworths Group — 5 operation(s) for payments.
  name: Woolworths Group Payments API
  slug: woolworths-group-payments-api
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: Refunds are submitted on approved capture transactions. Refunds credit a cardholder’s account.
  name: Woolworths Group Refund API
  slug: woolworths-group-refund-api
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: The Refunds API from Woolworths Group — 2 operation(s) for refunds.
  name: Woolworths Group Refunds API
  slug: woolworths-group-refunds-api
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: The Support API from Woolworths Group — 1 operation(s) for support.
  name: Woolworths Group Support API
  slug: woolworths-group-support-api
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: The transaction search utility allows consumers to view previously submitted transactions.
  name: Woolworths Group Transaction API
  slug: woolworths-group-transaction-api
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: A void reverses an un-captured authorization. The action informs the issuing bank to release the lock of funds that was created by an authorization request.
  name: Woolworths Group Void API
  slug: woolworths-group-void-api
- baseURL: https://pt-api.wpay.com.au/gifting
  baseurl_source: declared
  description: The Wallet Services API from Woolworths Group — 1 operation(s) for wallet services.
  name: Woolworths Group Wallet Services API
  slug: woolworths-group-wallet-services-api
artifact_total: 61
asyncapis:
- description: ''
  name: Woolworths Group Webhooks
  slug: woolworths-group-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/woolworths-group/agentic-access/woolworths-group-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/woolworths-group-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/woolworths-group/rules/woolworths-group-rules.yml
  title: ''
  type: Spectral
  url: rules/woolworths-group-rules.yml
- group: design
  href: https://artifacts.apis.io/woolworths-group/json-ld/woolworths-group-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/woolworths-group-context.jsonld
- group: design
  href: https://artifacts.apis.io/woolworths-group/vocabulary/woolworths-group-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/woolworths-group-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/woolworths-group/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/woolworths-group/asyncapi/woolworths-group-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/woolworths-group-webhooks.yml
- group: design
  href: https://artifacts.apis.io/woolworths-group/data-model/woolworths-group-data-model.yml
  title: ''
  type: DataModel
  url: data-model/woolworths-group-data-model.yml
- group: operate
  href: https://artifacts.apis.io/woolworths-group/changelog/woolworths-group-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/woolworths-group-changelog.yml
- group: design
  href: https://artifacts.apis.io/woolworths-group/conventions/woolworths-group-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/woolworths-group-conventions.yml
- group: design
  href: https://artifacts.apis.io/woolworths-group/conventions/woolworths-group-conventions.yml
  title: ''
  type: Conventions
  url: conventions/woolworths-group-conventions.yml
- group: start
  href: https://artifacts.apis.io/woolworths-group/sandbox/woolworths-group-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/woolworths-group-sandbox.yml
- group: design
  href: https://artifacts.apis.io/woolworths-group/lifecycle/woolworths-group-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/woolworths-group-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/woolworths-group/errors/woolworths-group-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/woolworths-group-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/woolworths-group/errors/woolworths-group-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/woolworths-group-error-codes.yml
- group: design
  href: https://artifacts.apis.io/woolworths-group/errors/woolworths-group-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/woolworths-group-problem-types.yml
- group: design
  href: https://artifacts.apis.io/woolworths-group/conformance/woolworths-group-conformance.yml
  title: ''
  type: Conformance
  url: conformance/woolworths-group-conformance.yml
- group: other
  href: https://artifacts.apis.io/woolworths-group/overlays/woolworths-group-wpay-cards-connect-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/woolworths-group-wpay-cards-connect-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/woolworths-group/llms/woolworths-group-giftingservices-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/woolworths-group-giftingservices-llms.txt
- group: other
  href: https://artifacts.apis.io/woolworths-group/a2a/woolworths-group-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/woolworths-group-a2a.yml
- group: build
  href: https://artifacts.apis.io/woolworths-group/mcp/woolworths-group-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/woolworths-group-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/woolworths-group/mcp/woolworths-group-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/woolworths-group-mcp.yml
- group: agent
  href: https://artifacts.apis.io/woolworths-group/well-known/woolworths-group-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/woolworths-group-well-known.yml
- group: other
  href: https://artifacts.apis.io/woolworths-group/hosts/woolworths-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/woolworths-group-hosts.yml
- group: other
  href: https://artifacts.apis.io/woolworths-group/vendors/woolworths-group-vendors.yml
  title: ''
  type: Vendors
  url: vendors/woolworths-group-vendors.yml
- group: auth
  href: https://artifacts.apis.io/woolworths-group/authentication/woolworths-group-authentication.yml
  title: ''
  type: Authentication
  url: authentication/woolworths-group-authentication.yml
- group: auth
  href: https://artifacts.apis.io/woolworths-group/security/woolworths-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/woolworths-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.woolworthsgroup.com.au/
- group: company
  title: ''
  type: Blog
  url: https://www.woolworthsgroup.com.au/au/en/our-newsroom.html
- group: operate
  title: ''
  type: Support
  url: https://www.woolworthsgroup.com.au/au/en/contact-us.html
- group: company
  title: ''
  type: Careers
  url: https://careers.woolworthsgroup.com.au/
- group: company
  title: ''
  type: Investors
  url: https://www.woolworthsgroup.com.au/au/en/investors.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/woolworths-group/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.woolworthsgroup.com.au/au/en/privacy/policy-documents/terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.woolworthsgroup.com.au/au/en/privacy/policy-documents/privacy-policy.html
created: '2026-10-22'
description: Woolworths Group Limited is an Australian retail group (ASX-listed) whose corporate site describes it as made up of some of the most recognisable and trusted brands in retailing, serving millions of customers every day with great choice, low prices and excellent quality. Its businesses span supermarkets in Australia and New Zealand (Woolworths), BIG W and related retail brands. The corporate site woolworthsgroup.com.au publishes investor, newsroom, sustainability, careers and policy content; its payments business Wpay publishes a developer hub (developerhub.wpay.com.au) documenting gifting, Cards Connect and PayTo APIs.
image: https://www.woolworthsgroup.com.au/content/dam/wwg/wwg-assets/logo.svg
json_schemas:
- name: AccountStatusInquiryRequest
  property_count: 7
  slug: woolworths-group-account-status-inquiry-request
- name: AccountStatusInquiryResponse
  property_count: 13
  slug: woolworths-group-account-status-inquiry-response
- name: ActivatedCardsResponse
  property_count: 5
  slug: woolworths-group-activated-cards-response
- name: ApiKeyDetails
  property_count: 3
  slug: woolworths-group-api-key-details
- name: CancelRequest
  property_count: 27
  slug: woolworths-group-cancel-request
- name: CancelResponse
  property_count: 15
  slug: woolworths-group-cancel-response
- name: CategoryDto
  property_count: 4
  slug: woolworths-group-category-dto
- name: CnpAuthorizationRequest
  property_count: 18
  slug: woolworths-group-cnp-authorization-request
- name: CnpRefundsResponse
  property_count: 5
  slug: woolworths-group-cnp-refunds-response
- name: CnpTransactionDetailResponse
  property_count: 19
  slug: woolworths-group-cnp-transaction-detail-response
- name: CnpVoidsResponse
  property_count: 5
  slug: woolworths-group-cnp-voids-response
- name: CreateKeyResponse
  property_count: 4
  slug: woolworths-group-create-key-response
- name: DigitalOrderRequest
  property_count: 5
  slug: woolworths-group-digital-order-request
- name: InitiatePayment
  property_count: 8
  slug: woolworths-group-merchant-api-application-commands-merchant-initiate-payment-merchant-initiate-payment-command
- name: Merchant.API.Application.Queries.ViewModels.MerchantSessionViewModel
  property_count: 12
  slug: woolworths-group-merchant-api-application-queries-view-models-merchant-session-view-model
- name: Merchant.API.Application.Queries.ViewModels.PaymentDetailsByPaymentIdViewModel
  property_count: 13
  slug: woolworths-group-merchant-api-application-queries-view-models-payment-details-by-payment-id-view-model
- name: PaymentDetailsViewModel
  property_count: 13
  slug: woolworths-group-merchant-api-application-queries-view-models-payment-details-view-model
- name: Merchant.API.Application.Queries.ViewModels.RefundDetailsByRefundIdViewModel
  property_count: 12
  slug: woolworths-group-merchant-api-application-queries-view-models-refund-details-by-refund-id-view-model
- name: RefundDetailsViewModel
  property_count: 12
  slug: woolworths-group-merchant-api-application-queries-view-models-refund-details-view-model
- name: OrderDataDto
  property_count: 8
  slug: woolworths-group-order-data-dto
- name: OrderDigitalCardsResponse
  property_count: 8
  slug: woolworths-group-order-digital-cards-response
- name: OrderInfoDto
  property_count: 13
  slug: woolworths-group-order-info-dto
- name: OrderProcessingResponse
  property_count: 6
  slug: woolworths-group-order-processing-response
- name: OrderStatusResponse
  property_count: 4
  slug: woolworths-group-order-status-response
- name: PhysicalOrderRequest
  property_count: 6
  slug: woolworths-group-physical-order-request
- name: ProductDtoPagedResponse
  property_count: 6
  slug: woolworths-group-product-dto-paged-response
- name: ProductDto
  property_count: 18
  slug: woolworths-group-product-dto
- name: ProgramDto
  property_count: 8
  slug: woolworths-group-program-dto
- name: TransactionRequest
  property_count: 30
  slug: woolworths-group-transaction-request
- name: TransactionResponse
  property_count: 15
  slug: woolworths-group-transaction-response
jsonld:
- class_count: 120
  name: Woolworths Group Context
  property_count: 234
  slug: woolworths-group-context
layout: provider
mcp_servers:
- description: Remote MCP server at integration.wpay.com.au; 3 tools listed.
  name: Wpay
  slug: wpay
modified: '2026-10-22'
name: Woolworths Group
nav: Providers
network: true
overview: 'Woolworths Group publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Status Inquiry API, Activating Physical Gift Cards API, Authorization API, and 15 more. Tagged areas include Company, Retail, Supermarkets, Grocery, and Australia.


  The Woolworths Group catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Woolworths Group''s developer surface includes changelog, sandbox, authentication, engineering blog, support, and 29 more developer resources.'
plans:
- name: Woolworths Group Plans Pricing
  plan_count: 0
  slug: woolworths-group-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Woolworths Group Rate Limits
  slug: woolworths-group-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Woolworths Group API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: woolworths-group-rules
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 10.5
    contract_governance: 35.6
    contract_quality: 69.7
    developer_ergonomics: 29.2
    discoverability: 71.7
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    - new-zealand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 58.8
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Woolworths Group Authentication
  slug: woolworths-group-authentication
  summary_line: apiKey/http/signed-request · 5 schemes
- kind: domain-security
  name: Woolworths Group Domain Security
  slug: woolworths-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: cards-connect-authorize-capture
  slug: woolworths-group-cards-connect-authorize-capture
- name: order-digital-gift-cards
  slug: woolworths-group-order-digital-gift-cards
- name: partner-gift-card-orders
  slug: woolworths-group-partner-gift-card-orders
- name: payment-transaction
  slug: woolworths-group-payment-transaction
slug: woolworths-group
tags:
- Company
- Retail
- Supermarkets
- Grocery
- Australia
- New Zealand
- E-Commerce
website: https://www.woolworthsgroup.com.au/
---
