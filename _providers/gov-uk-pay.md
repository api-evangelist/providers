---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Gov Uk Pay Agentic Access
  operation_count: 16
  slug: gov-uk-pay-agentic-access
  summary_line: 16 operations · 7 acting
api_count: 5
apis:
- description: The Agreements API from GOV.UK Pay — 3 operation(s) for agreements.
  name: GOV.UK Pay Agreements API
  slug: gov-uk-pay-agreements-api
- description: The Authorise card payments API from GOV.UK Pay — 1 operation(s) for authorise card payments.
  name: GOV.UK Pay Authorise card payments API
  slug: gov-uk-pay-authorise-card-payments-api
- description: The Card payments API from GOV.UK Pay — 5 operation(s) for card payments.
  name: GOV.UK Pay Card payments API
  slug: gov-uk-pay-card-payments-api
- description: The Disputes API from GOV.UK Pay — 1 operation(s) for disputes.
  name: GOV.UK Pay Disputes API
  slug: gov-uk-pay-disputes-api
- description: The Refunding card payments API from GOV.UK Pay — 3 operation(s) for refunding card payments.
  name: GOV.UK Pay Refunding card payments API
  slug: gov-uk-pay-refunding-card-payments-api
artifact_total: 60
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gov-uk-pay-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gov-uk-pay-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gov-uk-pay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gov-uk-pay-authentication.yml
created: '2026-06-13'
description: UK government digital payment service providing a REST API for accepting card payments, managing payment links, and processing refunds for government digital services. Built and operated by the Government Digital Service (GDS), GOV.UK Pay enables over 1,500 public sector organisations to take payments securely without managing their own PCI DSS compliance.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://www.payments.service.gov.uk/assets/images/govuk-pay-logo.png
json_schemas:
- name: Address
  property_count: 5
  slug: Address
- name: Agreement
  property_count: 8
  slug: Agreement
- name: AgreementSearchResults
  property_count: 5
  slug: AgreementSearchResults
- name: AuthorisationRequest
  property_count: 5
  slug: AuthorisationRequest
- name: AuthorisationSummary
  property_count: 1
  slug: AuthorisationSummary
- name: CardDetails
  property_count: 8
  slug: CardDetails
- name: CardDetailsFromResponse
  property_count: 7
  slug: CardDetailsFromResponse
- name: CreateAgreementRequest
  property_count: 3
  slug: CreateAgreementRequest
- name: CreateCardPaymentRequest
  property_count: 14
  slug: CreateCardPaymentRequest
- name: CreatePaymentResult
  property_count: 18
  slug: CreatePaymentResult
- name: DisputeDetailForSearch
  property_count: 11
  slug: DisputeDetailForSearch
- name: DisputeLinksForSearch
  property_count: 1
  slug: DisputeLinksForSearch
- name: DisputesSearchResults
  property_count: 5
  slug: DisputesSearchResults
- name: EmbeddedRefunds
  property_count: 1
  slug: EmbeddedRefunds
- name: ErrorResponse
  property_count: 2
  slug: ErrorResponse
- name: Exemption
  property_count: 3
  slug: Exemption
- name: ExternalMetadata
  property_count: 1
  slug: ExternalMetadata
- name: Link
  property_count: 2
  slug: Link
- name: Outcome
  property_count: 1
  slug: Outcome
- name: PaymentDetailForSearch
  property_count: 27
  slug: PaymentDetailForSearch
- name: PaymentEvent
  property_count: 4
  slug: PaymentEvent
- name: PaymentEventLink
  property_count: 1
  slug: PaymentEventLink
- name: PaymentEvents
  property_count: 3
  slug: PaymentEvents
- name: PaymentInstrument
  property_count: 3
  slug: PaymentInstrument
- name: PaymentLinks
  property_count: 8
  slug: PaymentLinks
- name: PaymentLinksForEvents
  property_count: 1
  slug: PaymentLinksForEvents
- name: PaymentLinksForSearch
  property_count: 5
  slug: PaymentLinksForSearch
- name: PaymentRefundRequest
  property_count: 2
  slug: PaymentRefundRequest
- name: PaymentSearchResults
  property_count: 5
  slug: PaymentSearchResults
- name: PaymentSettlementSummary
  property_count: 3
  slug: PaymentSettlementSummary
- name: PaymentState
  property_count: 5
  slug: PaymentState
- name: PaymentWithAllLinks
  property_count: 27
  slug: PaymentWithAllLinks
- name: PostLink
  property_count: 4
  slug: PostLink
- name: PrefilledCardholderDetails
  property_count: 2
  slug: PrefilledCardholderDetails
- name: Refund
  property_count: 7
  slug: Refund
- name: RefundDetailForSearch
  property_count: 7
  slug: RefundDetailForSearch
- name: RefundForSearchResult
  property_count: 3
  slug: RefundForSearchResult
- name: RefundLinksForSearch
  property_count: 2
  slug: RefundLinksForSearch
- name: RefundSearchResults
  property_count: 5
  slug: RefundSearchResults
- name: RefundSettlementSummary
  property_count: 1
  slug: RefundSettlementSummary
- name: RefundSummary
  property_count: 3
  slug: RefundSummary
- name: RefundsResponse
  property_count: 2
  slug: RefundsResponse
- name: RequestError
  property_count: 4
  slug: RequestError
- name: SearchNavigationLinks
  property_count: 5
  slug: SearchNavigationLinks
- name: SettlementSummary
  property_count: 1
  slug: SettlementSummary
- name: ThreeDSecure
  property_count: 1
  slug: ThreeDSecure
jsonld:
- class_count: 0
  name: Api Context
  property_count: 0
  slug: api
- class_count: 0
  name: context Context
  property_count: 64
  slug: context
layout: provider
modified: '2026-06-13'
name: GOV.UK Pay
nav: Providers
network: true
overview: 'GOV.UK Pay publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agreements API, Authorise card payments API, Card payments API, and 2 more. Tagged areas include Payments, Government, UK, Public Sector, and REST.


  The GOV.UK Pay catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  GOV.UK Pay''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 28
rules:
- name: GOV.UK Pay API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: gov-uk-pay-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.2
  delta: -4.9
  facets:
    commercial_clarity: 36.8
    contract_quality: 64.6
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 40.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gov-uk-pay/refs/heads/main/screenshots/gov-uk-pay-2026-06-20T182258.png
security:
- kind: authentication
  name: Gov Uk Pay Authentication
  slug: gov-uk-pay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gov Uk Pay Domain Security
  slug: gov-uk-pay-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Gov Uk Pay Trust Center
  slug: gov-uk-pay-trust-center
  summary_line: PCI DSS
slug: gov-uk-pay
tags:
- Payments
- Government
- UK
- Public Sector
- REST
- PCI DSS
- Refunds
- Recurring Payments
- Webhooks
---
