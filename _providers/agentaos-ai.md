---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 44
  human_in_the_loop: 4
  name: Agentaos Ai Agentic Access
  operation_count: 88
  slug: agentaos-ai-agentic-access
  summary_line: 88 operations · 44 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.agentaos.ai/api/v1
  baseurl_source: declared
  description: 'Where payouts go: the bank accounts of a business, as thin references (holder, last four digits, the name-check result), never the account number. For a platform: with the `AgentaOS-Account` header th'
  name: AgentaOS Bank Accounts API
  slug: agentaos-ai-bank-accounts-api
- baseURL: https://api.agentaos.ai/api/v1
  baseurl_source: declared
  description: 'For platforms: the businesses you manage, a client''s business or another app of your own company. To act as one of them on any other endpoint, send its id in the `AgentaOS-Account` header. Every field'
  name: AgentaOS Businesses API
  slug: agentaos-ai-businesses-api
- baseURL: https://api.agentaos.ai/api/v1
  baseurl_source: declared
  description: One attempt to collect one payment, standalone or built from a payment link. Wire path is `/gateway/sessions`; the SDK and CLI call this resource "checkout".
  name: AgentaOS Checkouts API
  slug: agentaos-ai-checkouts-api
- baseURL: https://api.agentaos.ai/api/v1
  baseurl_source: declared
  description: 'Read-only surface: everyone who has paid you or been sent an invoice.'
  name: AgentaOS Customers API
  slug: agentaos-ai-customers-api
- baseURL: https://api.agentaos.ai/api/v1
  baseurl_source: declared
  description: The Discount Codes API from AgentaOS — 3 operation(s) for discount codes.
  name: AgentaOS Discount Codes API
  slug: agentaos-ai-discount-codes-api
- baseURL: https://api.agentaos.ai/api/v1
  baseurl_source: declared
  description: Every checkout issues an invoice. List, retrieve, void, export, and download PDFs/receipts.
  name: AgentaOS Invoices API
  slug: agentaos-ai-invoices-api
- baseURL: https://api.agentaos.ai/api/v1
  baseurl_source: declared
  description: 'Reusable, shareable payment products: a fixed amount and description behind one URL.'
  name: AgentaOS Payment Links API
  slug: agentaos-ai-payment-links-api
- baseURL: https://api.agentaos.ai/api/v1
  baseurl_source: declared
  description: 'Merchant-side read and management surface for recurring plans. Created automatically when a buyer pays a `type: subscription` payment link.'
  name: AgentaOS Subscriptions API
  slug: agentaos-ai-subscriptions-api
- baseURL: https://api.agentaos.ai/api/v1
  baseurl_source: declared
  description: 'The unified activity feed: every inbound payment and outbound send, across every rail, in one list.'
  name: AgentaOS Transactions API
  slug: agentaos-ai-transactions-api
artifact_total: 57
asyncapis:
- description: ''
  name: Agentaos Ai Webhooks
  slug: agentaos-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/agentaos-ai/agentic-access/agentaos-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentaos-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/agentaos-ai/plans/agentaos-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentaos-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentaos-ai/rules/agentaos-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/agentaos-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/agentaos-ai/json-ld/agentaos-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentaos-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentaos-ai/vocabulary/agentaos-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentaos-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentaos-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentaos-ai/asyncapi/agentaos-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agentaos-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/agentaos-ai/data-model/agentaos-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentaos-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/agentaos-ai/changelog/agentaos-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agentaos-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/agentaos-ai/conventions/agentaos-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agentaos-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentaos-ai/conventions/agentaos-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentaos-ai-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://agentaos.ai/security
- group: auth
  href: https://artifacts.apis.io/agentaos-ai/authentication/agentaos-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentaos-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentaos-ai/errors/agentaos-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentaos-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentaos-ai/conformance/agentaos-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentaos-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentaos-ai/llms/agentaos-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentaos-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/agentaos-ai/a2a/agentaos-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentaos-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentaos-ai/well-known/agentaos-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentaos-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentaos-ai/hosts/agentaos-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentaos-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentaos-ai/vendors/agentaos-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentaos-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://agentaos.ai/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.agentaos.ai/changelog/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agentaos.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/agentaos-ai/security/agentaos-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/agentaos-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/agentaos-ai/security/agentaos-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentaos-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentaos-ai/security/agentaos-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentaos-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentaos.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agentaos.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://agentaos.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentaos.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentaos.ai/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://agentaos.ai/about
created: '2026-10-31'
description: AgentaOS provides borderless billing and payment processing for freelancers, agencies, and SaaS companies in the AI era. It acts as the official seller on every transaction, handling tax, invoices, and chargebacks across 190+ countries, without requiring the seller to have a registered company. Built by Aristokrates OÜ in Estonia, the platform offers flexible pricing, payout calculators, and compliance tools, aiming to simplify global commerce for AI-driven businesses.
image: https://agentaos.ai/og-image.png?v=20261003d
json_schemas:
- name: BankAccountRequirements
  property_count: 2
  slug: agentaos-ai-bank-account-requirements
- name: BankAccount
  property_count: 10
  slug: agentaos-ai-bank-account
- name: BusinessCreateRequest
  property_count: 5
  slug: agentaos-ai-business-create-request
- name: BusinessInvitation
  property_count: 2
  slug: agentaos-ai-business-invitation
- name: Business
  property_count: 11
  slug: agentaos-ai-business
- name: CheckoutCreateRequest
  property_count: 21
  slug: agentaos-ai-checkout-create-request
- name: CheckoutDetail
  property_count: 28
  slug: agentaos-ai-checkout-detail
- name: CheckoutListResponse
  property_count: 3
  slug: agentaos-ai-checkout-list-response
- name: Checkout
  property_count: 22
  slug: agentaos-ai-checkout
- name: CreateBankAccountParams
  property_count: 5
  slug: agentaos-ai-create-bank-account-params
- name: CreateDiscountCodeRequest
  property_count: 7
  slug: agentaos-ai-create-discount-code-request
- name: CreatedBusiness
  property_count: 3
  slug: agentaos-ai-created-business
- name: CustomerListResponse
  property_count: 3
  slug: agentaos-ai-customer-list-response
- name: DiscountCodeDetail
  property_count: 11
  slug: agentaos-ai-discount-code-detail
- name: DiscountCodeListResponse
  property_count: 3
  slug: agentaos-ai-discount-code-list-response
- name: DiscountCode
  property_count: 8
  slug: agentaos-ai-discount-code
- name: GrantCreditRequest
  property_count: 2
  slug: agentaos-ai-grant-credit-request
- name: InvoiceDetail
  property_count: 27
  slug: agentaos-ai-invoice-detail
- name: InvoiceListResponse
  property_count: 3
  slug: agentaos-ai-invoice-list-response
- name: PaymentLinkCreateRequest
  property_count: 18
  slug: agentaos-ai-payment-link-create-request
- name: PaymentLinkDetail
  property_count: 31
  slug: agentaos-ai-payment-link-detail
- name: PaymentLinkListResponse
  property_count: 3
  slug: agentaos-ai-payment-link-list-response
- name: PaymentLink
  property_count: 30
  slug: agentaos-ai-payment-link
- name: PaymentLinkUpdateRequest
  property_count: 8
  slug: agentaos-ai-payment-link-update-request
- name: PlanChangePreview
  property_count: 9
  slug: agentaos-ai-plan-change-preview
- name: PlanChangeResponse
  property_count: 0
  slug: agentaos-ai-plan-change-response
- name: RefundRequest
  property_count: 5
  slug: agentaos-ai-refund-request
- name: ResendInvitationRequest
  property_count: 1
  slug: agentaos-ai-resend-invitation-request
- name: SendReceiptResponse
  property_count: 2
  slug: agentaos-ai-send-receipt-response
- name: SubscriptionCreditListResponse
  property_count: 3
  slug: agentaos-ai-subscription-credit-list-response
- name: SubscriptionCredit
  property_count: 10
  slug: agentaos-ai-subscription-credit
- name: SubscriptionInvoice
  property_count: 7
  slug: agentaos-ai-subscription-invoice
- name: SuccessResponse
  property_count: 1
  slug: agentaos-ai-success-response
- name: TransactionListResponse
  property_count: 3
  slug: agentaos-ai-transaction-list-response
- name: VerificationLink
  property_count: 2
  slug: agentaos-ai-verification-link
jsonld:
- class_count: 44
  name: Agentaos Ai Context
  property_count: 183
  slug: agentaos-ai-context
layout: provider
modified: '2026-10-31'
name: AgentaOS
nav: Providers
network: true
overview: 'AgentaOS publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bank Accounts API, Businesses API, Checkouts API, and 6 more. Tagged areas include Payments, Billing, Software-as-a-Service, Freelancers, and Artificial Intelligence.


  The AgentaOS catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  AgentaOS''s developer surface includes changelog, authentication, API reference, documentation, pricing, getting-started guide, and 26 more developer resources.'
plans:
- name: Agentaos Ai Plans Pricing
  plan_count: 6
  slug: agentaos-ai-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 111
  extends:
  - spectral:oas
  name: AgentaOS API Rules
  rule_count: 70
  severity_counts:
    error: 59
    hint: 0
    info: 4
    warn: 7
  slug: agentaos-ai-rules
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 74.9
    developer_ergonomics: 28.0
    discoverability: 57.1
    operational_transparency: 21.1
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentaos Ai Authentication
  slug: agentaos-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentaos Ai Domain Security
  slug: agentaos-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agentaos Ai Vulnerability Disclosure
  slug: agentaos-ai-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Agentaos Ai Trust Center
  slug: agentaos-ai-trust-center
  summary_line: PCI DSS, GDPR
skill_count: 4
skills:
- name: agentaos-ai-change-subscription-plan
  slug: agentaos-ai-change-subscription-plan
- name: agentaos-ai-create-and-retrieve-business
  slug: agentaos-ai-create-and-retrieve-business
- name: agentaos-ai-download-invoice-pdf
  slug: agentaos-ai-download-invoice-pdf
- name: agentaos-ai-refund-transaction
  slug: agentaos-ai-refund-transaction
slug: agentaos-ai
tags:
- Payments
- Billing
- Software-as-a-Service
- Freelancers
- Artificial Intelligence
website: https://agentaos.ai/
---
