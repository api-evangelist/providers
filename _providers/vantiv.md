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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Vantiv Agentic Access
  operation_count: 16
  slug: vantiv-agentic-access
  summary_line: 16 operations · 13 acting
api_count: 10
apis:
- description: Card authorization and fund verification
  name: Vantiv Authorizations API
  slug: vantiv-authorizations-api
- description: Capture previously authorized transactions for settlement
  name: Vantiv Captures API
  slug: vantiv-captures-api
- description: Chargeback dispute retrieval and response management
  name: Vantiv Chargebacks API
  slug: vantiv-chargebacks-api
- description: Refunds and credits to cardholder accounts
  name: Vantiv Credits API
  slug: vantiv-credits-api
- description: Evidence document upload and management for chargebacks
  name: Vantiv Documents API
  slug: vantiv-documents-api
- description: ACH and electronic check payment processing
  name: Vantiv eCheck API
  slug: vantiv-echeck-api
- description: Recurring and subscription billing
  name: Vantiv Recurring API
  slug: vantiv-recurring-api
- description: Combined authorization and capture transactions
  name: Vantiv Sales API
  slug: vantiv-sales-api
- description: Card data tokenization via Vantiv Vault
  name: Vantiv Tokenization API
  slug: vantiv-tokenization-api
- description: Cancel pending unsettled transactions
  name: Vantiv Voids API
  slug: vantiv-voids-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vantiv Chargeback Authorizations API
  slug: open-vantiv-authorizations-api
- collection_type: open
  name: Vantiv Chargeback Authorizations Captures API
  slug: open-vantiv-captures-api
- collection_type: open
  name: Vantiv Chargeback API
  slug: open-vantiv-chargeback
- collection_type: open
  name: Vantiv Chargeback Authorizations Chargebacks API
  slug: open-vantiv-chargebacks-api
- collection_type: open
  name: Vantiv CNP API
  slug: open-vantiv-cnp
- collection_type: open
  name: Vantiv Chargeback Authorizations Credits API
  slug: open-vantiv-credits-api
- collection_type: open
  name: Vantiv Chargeback Authorizations Documents API
  slug: open-vantiv-documents-api
- collection_type: open
  name: Vantiv Chargeback Authorizations eCheck API
  slug: open-vantiv-echeck-api
- collection_type: open
  name: Vantiv Chargeback Authorizations Recurring API
  slug: open-vantiv-recurring-api
- collection_type: open
  name: Vantiv Chargeback Authorizations Sales API
  slug: open-vantiv-sales-api
- collection_type: open
  name: Vantiv Chargeback Authorizations Tokenization API
  slug: open-vantiv-tokenization-api
- collection_type: open
  name: Vantiv Chargeback Authorizations Voids API
  slug: open-vantiv-voids-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vantiv-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vantiv-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vantiv-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vantiv
- group: start
  title: ''
  type: Portal
  url: https://developer.vantiv.com/community/ecommerce
- group: build
  title: ''
  type: SDKs
  url: https://developer.vantiv.com/community/ecommerce/pages/sdks
- group: start
  title: ''
  type: Sandbox
  url: https://developer.vantiv.com/docs/DOC-1347
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vantiv
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vantiv/cnp-sdk-for-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vantiv/vantiv-sdk-for-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vantiv/cnp-sdk-for-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vantiv/cnp-sdk-for-dotnet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vantiv/cnp-sdk-for-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vantiv/cnp-chargeback-sdk-java
- group: docs
  title: ''
  type: Documentation
  url: https://developer.worldpay.com
- group: company
  title: ''
  type: Website
  url: https://www.vantiv.com
created: '2026-05-03'
description: Vantiv was a leading American payment processing and technology provider that merged with Worldpay in 2018, forming Worldpay from FIS. Vantiv provided integrated payment processing solutions for merchants, financial institutions, and businesses across eCommerce, in-store, and omni-channel payment scenarios. Their cnpAPI (formerly litleAPI) supported credit card authorizations, captures, sales, refunds, voids, tokenization, chargebacks, and recurring billing.
examples:
- key_count: 2
  name: Vantiv Create Sale Example
  slug: vantiv-create-sale-example
- key_count: 2
  name: Vantiv Register Token Example
  slug: vantiv-register-token-example
finops:
- name: Vantiv Finops
  service_category: Payments
  slug: vantiv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vantiv.png
json_schemas:
- name: Vantiv Transaction
  property_count: 11
  slug: vantiv-transaction
json_structures:
- name: Vantiv Transaction Structure
  property_count: 0
  slug: vantiv-transaction-structure
jsonld:
- class_count: 17
  name: Vantiv Context
  property_count: 13
  slug: vantiv-context
layout: provider
modified: '2026-05-19'
name: Vantiv
nav: Providers
network: true
overview: 'Vantiv publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authorizations API, Captures API, Chargebacks API, and 7 more. Tagged areas include Payments, Payment Processing, eCommerce, Finance, and FinTech.


  The Vantiv catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vantiv''s developer surface includes authentication, developer portal, sandbox, documentation, and 12 more developer resources.'
plans:
- name: Vantiv Plans Pricing
  plan_count: 2
  slug: vantiv-plans-pricing
press:
- date: '2026-05-25'
  title: Investments
  url: https://www.adventinternational.com/investments/
- date: '2026-05-25'
  title: Vantiv News & Media
  url: https://www.atmmarketplace.com/companies/vantiv/media/
- date: '2026-05-25'
  title: IDEMIA/WORLDPAY | Business Wire
  url: https://via.ritzau.dk/pressemeddelelse/13061997/idemiaworldpay?publisherId=90456
- date: '2026-05-25'
  title: Vantiv Embraces Apple Pay on Web, Lures Its Developers
  url: https://www.americanbanker.com/payments/news/vantiv-embraces-apple-pay-on-web-lures-its-developers
- date: '2026-05-25'
  title: Vantiv and Worldpay Complete Combination to Form ...
  url: https://www.prnewswire.com/news-releases/vantiv-and-worldpay-complete-combination-to-form-worldpay-inc-300583008.html
random_paper: 68
rate_limits:
- limit_count: 1
  name: Vantiv Rate Limits
  slug: vantiv-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Vantiv API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vantiv-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Vantiv API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: vantiv-rules
score:
  band: thin
  composite: 37.9
  delta: -4.7
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 67.5
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 42.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Vantiv Authentication
  slug: vantiv-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vantiv Domain Security
  slug: vantiv-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vantiv
tags:
- Payments
- Payment Processing
- eCommerce
- Finance
- FinTech
- Fortune 1000
website: https://www.vantiv.com
---
