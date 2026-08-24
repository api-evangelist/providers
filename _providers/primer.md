---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Primer Agentic Access
  operation_count: 20
  slug: primer-agentic-access
  summary_line: 20 operations · 16 acting
api_count: 5
apis:
- description: The Client Session API API from Primer — 1 operation(s) for client session api.
  name: Primer Client Session API API
  slug: primer-client-session-api-api
- description: The Dispute & Chargebacks Webhooks API from Primer — 2 operation(s) for dispute & chargebacks webhooks.
  name: Primer Dispute & Chargebacks Webhooks API
  slug: primer-dispute-chargebacks-webhooks-api
- description: The Payment Methods API API from Primer — 4 operation(s) for payment methods api.
  name: Primer Payment Methods API API
  slug: primer-payment-methods-api-api
- description: The Payment Webhooks API from Primer — 2 operation(s) for payment webhooks.
  name: Primer Payment Webhooks API
  slug: primer-payment-webhooks-api
- description: The Payments API API from Primer — 8 operation(s) for payments api.
  name: Primer Payments API API
  slug: primer-payments-api-api
artifact_total: 53
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Primer Client Session API API
  slug: open-primer-client-session-api-api
- collection_type: open
  name: Primer Client Session API Dispute & Chargebacks Webhooks API
  slug: open-primer-dispute-chargebacks-webhooks-api
- collection_type: open
  name: Primer Client Session API Payment Methods API API
  slug: open-primer-payment-methods-api-api
- collection_type: open
  name: Primer Client Session API Payment Webhooks API
  slug: open-primer-payment-webhooks-api
- collection_type: open
  name: Primer Client Session API Payments API API
  slug: open-primer-payments-api-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/primer-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/primer-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/primer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/primer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/primer-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://primer.io/
- group: docs
  title: ''
  type: Documentation
  url: https://primer.io/docs/api-reference/get-started/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/primer-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/primerapi/
- group: other
  title: ''
  type: X
  url: https://x.com/primer_io
- group: company
  title: ''
  type: Blog
  url: https://primer.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://primer.io/blog/primer-launches-primer-for-growth
- group: operate
  title: ''
  type: StatusPage
  url: https://status.primer.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://primer.io/docs/changelogs/android-sdk
- group: commercial
  title: ''
  type: Plans
  url: plans/primer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/primer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/primer-finops.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/primer-clientsession.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/primer-paymentcreation.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/primer-payment.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/primer-paymentrefund.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/primer-paymentcapture.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/primer-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/primer-context.jsonld
created: 2026-06-12
description: Primer is a payment orchestration platform that enables merchants to build flexible payment flows across multiple processors through a single REST API integration. The platform provides intelligent routing, automatic fallback logic, fraud detection integrations, and a no-code Workflows builder for managing payment rules without engineering effort. Primer supports 60+ payment methods including cards, digital wallets, and regional alternatives such as iDEAL, Klarna, and Alipay. The platform delivers unified observability, reconciliation, and analytics across all connected payment providers, and processes billions of dollars monthly with 99.99% uptime.
examples:
- key_count: 1
  name: Primer Patch Client Session Response 400 Clientsessionvalidationerror
  slug: primer-patch-client-session-response-400-clientsessionvalidationerror
- key_count: 1
  name: Primer Patch Client Session Response 400 Metadatacontainsemptykey
  slug: primer-patch-client-session-response-400-metadatacontainsemptykey
- key_count: 1
  name: Primer Post Client Session Response 400 Clientsessionvalidationerror
  slug: primer-post-client-session-response-400-clientsessionvalidationerror
- key_count: 1
  name: Primer Post Client Session Response 400 Metadatacontainsemptykey
  slug: primer-post-client-session-response-400-metadatacontainsemptykey
- key_count: 1
  name: Primer Post Payments Id Adjust Authorization Response 400 Adjustauthorizationnoncardpayment
  slug: primer-post-payments-id-adjust-authorization-response-400-adjustauthorizationnoncardpayment
- key_count: 1
  name: Primer Post Payments Id Adjust Authorization Response 400 Adjustauthorizationnotsupported
  slug: primer-post-payments-id-adjust-authorization-response-400-adjustauthorizationnotsupported
- key_count: 1
  name: Primer Post Payments Id Adjust Authorization Response 400 Incorrectpaymentauthorizationtype
  slug: primer-post-payments-id-adjust-authorization-response-400-incorrectpaymentauthorizationtype
- key_count: 1
  name: Primer Post Payments Id Adjust Authorization Response 400 Paymentisnotauthorized
  slug: primer-post-payments-id-adjust-authorization-response-400-paymentisnotauthorized
- key_count: 1
  name: Primer Post Payments Id Authorize Response 400 Invalidpaymentstatus
  slug: primer-post-payments-id-authorize-response-400-invalidpaymentstatus
- key_count: 1
  name: Primer Post Payments Id Authorize Response 400 Merchantaccountconflict
  slug: primer-post-payments-id-authorize-response-400-merchantaccountconflict
- key_count: 1
  name: Primer Post Payments Id Authorize Response 400 Merchantaccountnotfound
  slug: primer-post-payments-id-authorize-response-400-merchantaccountnotfound
- key_count: 1
  name: Primer Post Payments Id Authorize Response 400 Paymentalreadyauthorized
  slug: primer-post-payments-id-authorize-response-400-paymentalreadyauthorized
- key_count: 1
  name: Primer Post Payments Id Capture Request Basic
  slug: primer-post-payments-id-capture-request-basic
- key_count: 2
  name: Primer Post Payments Id Capture Request Final Capture
  slug: primer-post-payments-id-capture-request-final-capture
- key_count: 2
  name: Primer Post Payments Id Capture Request Using Expand
  slug: primer-post-payments-id-capture-request-using-expand
- key_count: 2
  name: Primer Post Payments Id Capture Request Using Metadata
  slug: primer-post-payments-id-capture-request-using-metadata
- key_count: 0
  name: Primer Post Payments Id Refund Request Full Refund
  slug: primer-post-payments-id-refund-request-full-refund
- key_count: 1
  name: Primer Post Payments Id Refund Request Partial Refund With Transaction Event
  slug: primer-post-payments-id-refund-request-partial-refund-with-transaction-event
- key_count: 1
  name: Primer Post Payments Id Refund Request Partial Refund
  slug: primer-post-payments-id-refund-request-partial-refund
- key_count: 1
  name: Primer Post Payments Id Refund Request Using Expand
  slug: primer-post-payments-id-refund-request-using-expand
- key_count: 1
  name: Primer Post Payments Id Refund Response 409 Idempotencykeyalreadyexists
  slug: primer-post-payments-id-refund-response-409-idempotencykeyalreadyexists
- key_count: 1
  name: Primer Post Payments Id Refund Response 409 Paymentalreadyrefunded
  slug: primer-post-payments-id-refund-response-409-paymentalreadyrefunded
- key_count: 1
  name: Primer Post Payments Id Refund Response 422 Requestvalidationerror
  slug: primer-post-payments-id-refund-response-422-requestvalidationerror
- key_count: 1
  name: Primer Post Payments Id Refund Response 422 Unprocessablerefundamount
  slug: primer-post-payments-id-refund-response-422-unprocessablerefundamount
- key_count: 1
  name: Primer Post Payments Response 400 Genericerror
  slug: primer-post-payments-response-400-genericerror
- key_count: 1
  name: Primer Post Payments Response 400 Idempotencyerror
  slug: primer-post-payments-response-400-idempotencyerror
- key_count: 1
  name: Primer Post Payments Response 400 Metadatacontainsemptykey
  slug: primer-post-payments-response-400-metadatacontainsemptykey
finops:
- name: Primer Finops
  service_category: ''
  slug: primer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/primer.png
json_schemas:
- name: ClientSessionAPIRequest
  property_count: 8
  slug: primer-clientsession
- name: PaymentAPIResponse
  property_count: 18
  slug: primer-payment
- name: PaymentCaptureAPIRequest
  property_count: 5
  slug: primer-paymentcapture
- name: PaymentCreationAPIRequest
  property_count: 10
  slug: primer-paymentcreation
- name: PaymentRefundAPIRequest
  property_count: 5
  slug: primer-paymentrefund
jsonld:
- class_count: 16
  name: Primer Context
  property_count: 27
  slug: primer-context
layout: provider
modified: 2026-06-12
name: Primer
nav: Providers
network: true
overview: 'Primer publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Client Session API API, Dispute & Chargebacks Webhooks API, Payment Methods API API, and 2 more. Tagged areas include Payments, Payment Orchestration, Payment Processing, Fintech, and Fraud Detection.


  The Primer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Primer''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 19 more developer resources.'
plans:
- name: Primer Plans Pricing
  plan_count: 2
  slug: primer-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Primer Rate Limits
  slug: primer-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Primer API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: primer-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.9
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 25.0
    contract_quality: 64.1
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 65.8
  previous_composite: 50.9
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
    regime: Payments
    regime_id: payments
    score: 43.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/primer/refs/heads/main/screenshots/primer-2026-06-20T192104.png
security:
- kind: authentication
  name: Primer Authentication
  slug: primer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Primer Domain Security
  slug: primer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Primer Vulnerability Disclosure
  slug: primer-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Primer Trust Center
  slug: primer-trust-center
  summary_line: SOC 2, ISO 27001
slug: primer
tags:
- Payments
- Payment Orchestration
- Payment Processing
- Fintech
- Fraud Detection
- Smart Routing
- Checkout
- Payment Methods
- Reconciliation
- Webhook
website: https://primer.io/
---
