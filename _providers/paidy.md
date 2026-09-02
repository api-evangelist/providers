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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Paidy Agentic Access
  operation_count: 11
  slug: paidy-agentic-access
  summary_line: 11 operations · 8 acting
api_count: 1
apis:
- description: 'JavaScript-based checkout integration that enables consumers to authenticate with Paidy and authorize payments or create recurring payment tokens directly from the merchant checkout page. Handles the '
  name: Paidy Checkout
  slug: paidy-checkout
- description: Manage payment authorizations, captures, refunds, updates, and closures.
  name: Paidy Payments API
  slug: paidy-payments-api
- description: Manage recurring payment tokens for subscription billing.
  name: Paidy Tokens API
  slug: paidy-tokens-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Paidy Payments API
  slug: open-paidy-payments-api
- collection_type: open
  name: Paidy Payments Tokens API
  slug: open-paidy-tokens-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paidy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paidy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paidy-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://paidy.com/docs/en/
- group: docs
  title: ''
  type: APIReference
  url: https://paidy.com/docs/api/en/
- group: other
  title: ''
  type: Merchant Dashboard
  url: https://merchant.paidy.com/
- group: design
  title: ''
  type: Webhooks
  url: https://paidy.com/docs/en/webhook.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://paidy.com/docs/en/updates.html
- group: design
  title: ''
  type: Testing
  url: https://paidy.com/docs/en/testing.html
- group: operate
  title: ''
  type: Status
  url: https://paidy.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paidy.com/merchant/
created: '2026-06-13'
description: Paidy is a Japanese buy now, pay later (BNPL) and digital payment service that enables Japanese consumers to make purchases and pay later via monthly consolidated billing. Merchants integrate Paidy Checkout (JavaScript) and the Paidy REST API to accept deferred payments, manage authorizations, capture funds, issue refunds, and handle recurring payments via stored tokens.
examples:
- key_count: 1
  name: Capture Payment
  slug: capture-payment
- key_count: 8
  name: Create Payment
  slug: create-payment
- key_count: 16
  name: Payment Response
  slug: payment-response
- key_count: 4
  name: Refund Payment
  slug: refund-payment
- key_count: 2
  name: Suspend Token
  slug: suspend-token
- key_count: 16
  name: Token Response
  slug: token-response
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paidy.png
json_schemas:
- name: Payment
  property_count: 16
  slug: payment
- name: Token
  property_count: 16
  slug: token
jsonld:
- class_count: 55
  name: context Context
  property_count: 6
  slug: context
layout: provider
modified: '2026-06-13'
name: Paidy
nav: Providers
network: true
overview: 'Paidy publishes 2 APIs on the [APIs.io](https://apis.io/) network: Payments API and Tokens API. Tagged areas include Buy Now Pay Later, BNPL, Payments, Japan, and Checkout.


  The Paidy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Paidy''s developer surface includes authentication, documentation, API reference, changelog, status page, and 6 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 10
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Paidy API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: paidy-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 55.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 64.1
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paidy/refs/heads/main/screenshots/paidy-2026-06-20T191326.png
security:
- kind: authentication
  name: Paidy Authentication
  slug: paidy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Paidy Domain Security
  slug: paidy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paidy
tags:
- Buy Now Pay Later
- BNPL
- Payments
- Japan
- Checkout
- Deferred Payments
- Recurring Payments
- Tokens
---
