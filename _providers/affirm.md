---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.4
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Affirm Agentic Access
  operation_count: 29
  slug: affirm-agentic-access
  summary_line: 29 operations · 18 acting
api_count: 11
apis:
- description: Initialize and authorize Affirm checkout flows for online merchants.
  name: Affirm Checkout API
  slug: affirm-checkout-api
- description: Capture, void, and refund Affirm charges; read transaction details.
  name: Affirm Charges API
  slug: affirm-charges-api
- description: Read transactions, settlements, and disputes.
  name: Affirm Transactions API
  slug: affirm-transactions-api
- description: Server-side operations for authorizing Affirm transactions after a customer completes the checkout flow and a checkout token is returned.
  name: Affirm Authorization API
  slug: affirm-authorization-api
- description: Operations for managing virtual card numbers (VCN) issued via the Affirm Lite integration pattern.
  name: Affirm Cards API
  slug: affirm-cards-api
- description: Operations for creating, retrieving, updating, and resending Affirm checkout sessions.
  name: Affirm Checkouts API
  slug: affirm-checkouts-api
- description: Operations for listing, retrieving, contesting, and closing payment disputes initiated by customers.
  name: Affirm Disputes API
  slug: affirm-disputes-api
- description: Operations for retrieving dynamic promotional messaging and financing term information to display on merchant web pages.
  name: Affirm Promos API
  slug: affirm-promos-api
- description: Operations for listing settlement events and summaries that track disbursement activity.
  name: Affirm Settlement Events API
  slug: affirm-settlement-events-api
- description: Operations for listing transaction event records associated with transaction lifecycle changes.
  name: Affirm Transaction Events API
  slug: affirm-transaction-events-api
- description: Post-authorization transaction management operations including capture, void, and refund.
  name: Affirm Transactions API
  slug: affirm-transactions-api
artifact_total: 124
asyncapis:
- description: Affirm uses webhooks to notify merchant endpoints in real time when events occur during the customer checkout and prequalification flows. Webhooks are available to Key and Enterprise merchants. Affirm
  name: Affirm Webhooks
  slug: affirm-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Affirm Checkout Authorization API
  slug: open-affirm-authorization-api
- collection_type: open
  name: Affirm Checkout Authorization Cards API
  slug: open-affirm-cards-api
- collection_type: open
  name: Affirm Checkout API
  slug: open-affirm-checkout
- collection_type: open
  name: Affirm Checkout Authorization Checkouts API
  slug: open-affirm-checkouts-api
- collection_type: open
  name: Affirm Direct API
  slug: open-affirm-direct-api
- collection_type: open
  name: Affirm Checkout Authorization Disputes API
  slug: open-affirm-disputes-api
- collection_type: open
  name: Affirm Disputes API
  slug: open-affirm-disputes
- collection_type: open
  name: Affirm Checkout Authorization Promos API
  slug: open-affirm-promos-api
- collection_type: open
  name: Affirm Promos API
  slug: open-affirm-promos
- collection_type: open
  name: Affirm Checkout Authorization Settlement Events API
  slug: open-affirm-settlement-events-api
- collection_type: open
  name: Affirm Checkout Authorization Transaction Events API
  slug: open-affirm-transaction-events-api
- collection_type: open
  name: Affirm Checkout Authorization Transactions API
  slug: open-affirm-transactions-api
- collection_type: open
  name: Affirm Transactions API
  slug: open-affirm-transactions
common:
- group: docs
  title: ''
  type: Documentation
  url: https://www.affirm.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.affirm.com/affirm-developers/changelog
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/affirm-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/affirm-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/affirm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/affirm-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Affirm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/affirm
- group: company
  title: ''
  type: Website
  url: https://www.affirm.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/affirm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/affirm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/affirm-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.affirm.com/llms.txt
created: '2026-05-08'
description: Affirm is a buy-now-pay-later platform offering installment loans at point-of-sale via merchant SDKs and direct APIs. Public Series A through F-funded company.
examples:
- key_count: 22
  name: Affirm Checkout Example
  slug: affirm-checkout-example
- key_count: 12
  name: Affirm Dispute Example
  slug: affirm-dispute-example
- key_count: 13
  name: Affirm Transaction Example
  slug: affirm-transaction-example
- key_count: 6
  name: Checkout Address Object Example
  slug: checkout-address-object-example
- key_count: 18
  name: Checkout Checkout Example
  slug: checkout-checkout-example
- key_count: 15
  name: Checkout Checkout Request Example
  slug: checkout-checkout-request-example
- key_count: 4
  name: Checkout Contact Object Example
  slug: checkout-contact-object-example
- key_count: 2
  name: Checkout Discount Object Example
  slug: checkout-discount-object-example
- key_count: 7
  name: Checkout Item Object Example
  slug: checkout-item-object-example
- key_count: 5
  name: Checkout Merchant Object Example
  slug: checkout-merchant-object-example
- key_count: 3
  name: Checkout Name Object Example
  slug: checkout-name-object-example
- key_count: 2
  name: Checkout Store Object Example
  slug: checkout-store-object-example
- key_count: 10
  name: Direct Api Card Example
  slug: direct-api-card-example
- key_count: 6
  name: Direct Api File Object Example
  slug: direct-api-file-object-example
- key_count: 9
  name: Direct Api Transaction Example
  slug: direct-api-transaction-example
- key_count: 12
  name: Disputes Dispute Example
  slug: disputes-dispute-example
- key_count: 4
  name: Disputes Evidence Item Example
  slug: disputes-evidence-item-example
- key_count: 6
  name: Disputes Evidence Request Example
  slug: disputes-evidence-request-example
- key_count: 7
  name: Promos Financing Term Example
  slug: promos-financing-term-example
- key_count: 3
  name: Promos Offer Content Example
  slug: promos-offer-content-example
- key_count: 7
  name: Promos Promo Config Example
  slug: promos-promo-config-example
- key_count: 8
  name: Promos Promo Content Example
  slug: promos-promo-content-example
- key_count: 2
  name: Promos Promo Response Example
  slug: promos-promo-response-example
- key_count: 7
  name: Transactions Settlement Event Example
  slug: transactions-settlement-event-example
- key_count: 5
  name: Transactions Settlement Event Summary Example
  slug: transactions-settlement-event-summary-example
- key_count: 8
  name: Transactions Transaction Event Example
  slug: transactions-transaction-event-example
- key_count: 13
  name: Transactions Transaction Example
  slug: transactions-transaction-example
finops:
- name: Affirm Finops
  service_category: Fintech
  slug: affirm-finops
graphqls:
- description: This document describes the conceptual GraphQL schema for the Affirm Buy Now Pay Later (BNPL) platform. Affirm's production API is REST-based; this schema models the same domain objects and operations
  name: Affirm GraphQL Schema
  slug: affirm-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/affirm.png
json_schemas:
- name: Affirm Checkout
  property_count: 22
  slug: affirm-checkout
- name: Affirm Dispute
  property_count: 12
  slug: affirm-dispute
- name: Affirm Transaction
  property_count: 13
  slug: affirm-transaction
- name: AddressObject
  property_count: 6
  slug: checkout-address-object
- name: CheckoutRequest
  property_count: 15
  slug: checkout-checkout-request
- name: Checkout
  property_count: 18
  slug: checkout-checkout
- name: ContactObject
  property_count: 4
  slug: checkout-contact-object
- name: DiscountObject
  property_count: 2
  slug: checkout-discount-object
- name: ItemObject
  property_count: 7
  slug: checkout-item-object
- name: MerchantObject
  property_count: 5
  slug: checkout-merchant-object
- name: NameObject
  property_count: 3
  slug: checkout-name-object
- name: StoreObject
  property_count: 2
  slug: checkout-store-object
- name: Card
  property_count: 10
  slug: direct-api-card
- name: FileObject
  property_count: 6
  slug: direct-api-file-object
- name: Transaction
  property_count: 9
  slug: direct-api-transaction
- name: Dispute
  property_count: 12
  slug: disputes-dispute
- name: EvidenceItem
  property_count: 4
  slug: disputes-evidence-item
- name: EvidenceRequest
  property_count: 6
  slug: disputes-evidence-request
- name: FinancingTerm
  property_count: 7
  slug: promos-financing-term
- name: OfferContent
  property_count: 3
  slug: promos-offer-content
- name: PromoConfig
  property_count: 7
  slug: promos-promo-config
- name: PromoContent
  property_count: 8
  slug: promos-promo-content
- name: PromoResponse
  property_count: 2
  slug: promos-promo-response
- name: SettlementEvent
  property_count: 7
  slug: transactions-settlement-event
- name: SettlementEventSummary
  property_count: 5
  slug: transactions-settlement-event-summary
- name: TransactionEvent
  property_count: 8
  slug: transactions-transaction-event
- name: Transaction
  property_count: 13
  slug: transactions-transaction
json_structures:
- name: Affirm Checkout Structure
  property_count: 22
  slug: affirm-checkout-structure
- name: Affirm Dispute Structure
  property_count: 12
  slug: affirm-dispute-structure
- name: Affirm Transaction Structure
  property_count: 13
  slug: affirm-transaction-structure
- name: Checkout Address Object Structure
  property_count: 6
  slug: checkout-address-object-structure
- name: Checkout Checkout Request Structure
  property_count: 15
  slug: checkout-checkout-request-structure
- name: Checkout Checkout Structure
  property_count: 18
  slug: checkout-checkout-structure
- name: Checkout Contact Object Structure
  property_count: 4
  slug: checkout-contact-object-structure
- name: Checkout Discount Object Structure
  property_count: 2
  slug: checkout-discount-object-structure
- name: Checkout Item Object Structure
  property_count: 7
  slug: checkout-item-object-structure
- name: Checkout Merchant Object Structure
  property_count: 5
  slug: checkout-merchant-object-structure
- name: Checkout Name Object Structure
  property_count: 3
  slug: checkout-name-object-structure
- name: Checkout Store Object Structure
  property_count: 2
  slug: checkout-store-object-structure
- name: Direct Api Card Structure
  property_count: 10
  slug: direct-api-card-structure
- name: Direct Api File Object Structure
  property_count: 6
  slug: direct-api-file-object-structure
- name: Direct Api Transaction Structure
  property_count: 9
  slug: direct-api-transaction-structure
- name: Disputes Dispute Structure
  property_count: 12
  slug: disputes-dispute-structure
- name: Disputes Evidence Item Structure
  property_count: 4
  slug: disputes-evidence-item-structure
- name: Disputes Evidence Request Structure
  property_count: 6
  slug: disputes-evidence-request-structure
- name: Promos Financing Term Structure
  property_count: 7
  slug: promos-financing-term-structure
- name: Promos Offer Content Structure
  property_count: 3
  slug: promos-offer-content-structure
- name: Promos Promo Config Structure
  property_count: 7
  slug: promos-promo-config-structure
- name: Promos Promo Content Structure
  property_count: 8
  slug: promos-promo-content-structure
- name: Promos Promo Response Structure
  property_count: 2
  slug: promos-promo-response-structure
- name: Transactions Settlement Event Structure
  property_count: 7
  slug: transactions-settlement-event-structure
- name: Transactions Settlement Event Summary Structure
  property_count: 5
  slug: transactions-settlement-event-summary-structure
- name: Transactions Transaction Event Structure
  property_count: 8
  slug: transactions-transaction-event-structure
- name: Transactions Transaction Structure
  property_count: 13
  slug: transactions-transaction-structure
jsonld:
- class_count: 11
  name: Affirm Checkout Context
  property_count: 50
  slug: affirm-checkout-context
- class_count: 0
  name: Affirm Context
  property_count: 9
  slug: affirm-context
- class_count: 3
  name: Affirm Direct Context
  property_count: 23
  slug: affirm-direct-context
- class_count: 3
  name: Affirm Disputes Context
  property_count: 21
  slug: affirm-disputes-context
- class_count: 6
  name: Affirm Promos Context
  property_count: 30
  slug: affirm-promos-context
- class_count: 4
  name: Affirm Transactions Context
  property_count: 22
  slug: affirm-transactions-context
layout: provider
modified: '2026-05-08'
name: Affirm
nav: Providers
network: true
overview: 'Affirm publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Transactions API, Authorization API, Cards API, and 6 more. Tagged areas include Fintech, BNPL, Lending, Payments, and Consumer.


  The Affirm catalog on APIs.io includes 1 event-driven AsyncAPI specification, 6 JSON-LD contexts, and 3 Spectral governance rulesets.


  Affirm''s developer surface includes documentation, changelog, authentication, and 10 more developer resources.'
plans:
- name: Affirm Plans Pricing
  plan_count: 1
  slug: affirm-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Affirm Rate Limits
  slug: affirm-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Affirm API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: affirm-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Affirm API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: affirm-jsonschema-spectral-rules
- effective_rule_count: 83
  extends:
  - spectral:oas
  name: Affirm API Rules
  rule_count: 42
  severity_counts:
    error: 16
    hint: 0
    info: 2
    warn: 24
  slug: affirm-spectral-rules
score:
  band: thin
  composite: 38.1
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 13.6
    contract_quality: 80.7
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/affirm/refs/heads/main/screenshots/affirm-2026-06-20T165638.png
security:
- kind: authentication
  name: Affirm Authentication
  slug: affirm-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Affirm Domain Security
  slug: affirm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Affirm Trust Center
  slug: affirm-trust-center
  summary_line: SOC 2, PCI DSS
slug: affirm
tags:
- Fintech
- BNPL
- Lending
- Payments
- Consumer
website: https://www.affirm.com/
---
