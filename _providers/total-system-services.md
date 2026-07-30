---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Total System Services Agentic Access
  operation_count: 23
  slug: total-system-services-agentic-access
  summary_line: 23 operations · 13 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: Cardholder account management
  name: Total System Services Accounts API
  slug: total-system-services-accounts-api
- description: Authorize card payments
  name: Total System Services Authorization API
  slug: total-system-services-authorization-api
- description: Capture authorized transactions
  name: Total System Services Capture API
  slug: total-system-services-capture-api
- description: Card lifecycle management
  name: Total System Services Cards API
  slug: total-system-services-cards-api
- description: Spending controls and limits
  name: Total System Services Controls API
  slug: total-system-services-controls-api
- description: Transaction dispute management
  name: Total System Services Disputes API
  slug: total-system-services-disputes-api
- description: Look up transaction status
  name: Total System Services Inquiries API
  slug: total-system-services-inquiries-api
- description: Process refunds and credits
  name: Total System Services Refunds API
  slug: total-system-services-refunds-api
- description: Card transaction history
  name: Total System Services Transactions API
  slug: total-system-services-transactions-api
- description: Void pending transactions
  name: Total System Services Voids API
  slug: total-system-services-voids-api
artifact_total: 25
collections:
- collection_type: open
  name: TSYS Issuing Platform
  slug: open-tsys-issuing
- collection_type: open
  name: TSYS Payment Gateway
  slug: open-tsys-payment-gateway
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/total-system-services-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/total-system-services-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/total-system-services-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TSYS-Merchant
- group: company
  title: ''
  type: Website
  url: https://www.tsys.com/
- group: other
  title: ''
  type: Developer
  url: https://developers.tsys.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tsysmerchant.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tsys
- group: design
  title: ''
  type: Rules
  url: rules/tsys-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/total-system-services-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/total-system-services-context.jsonld
created: '2026-03-24'
description: Total System Services (TSYS) was a leading global payment solutions provider offering payment processing services to financial and nonfinancial institutions before merging with Global Payments in 2019. TSYS provides an end-to-end payment stack spanning payment gateway services for merchants, card issuing for banks and fintechs, merchant acquiring and boarding, virtual card programs, and comprehensive reporting. The TSYS developer portal provides APIs for transaction processing, cardholder management, merchant services, and commercial virtual solutions.
examples:
- key_count: 2
  name: Tsys Process Sale Example
  slug: tsys-process-sale-example
finops:
- name: Total System Services Finops
  service_category: Payments Processing
  slug: total-system-services-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/total-system-services.png
json_schemas:
- name: Transaction
  property_count: 13
  slug: tsys-transaction
json_structures:
- name: Tsys Transaction Structure
  property_count: 0
  slug: tsys-transaction-structure
jsonld:
- class_count: 45
  name: Total System Services Context
  property_count: 0
  slug: total-system-services-context
layout: provider
modified: '2026-05-19'
name: Total System Services
nav: Providers
network: true
overview: 'Total System Services publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authorization API, Capture API, and 7 more. Tagged areas include Payments, Payment Processing, Card Issuing, Merchant Services, and Fintech.


  The Total System Services catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Total System Services'' developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Total System Services Plans Pricing
  plan_count: 1
  slug: total-system-services-plans-pricing
press:
- date: '2026-05-25'
  title: TSYS, Global Payments Merger Finalized In 'Landmark ...
  url: https://www.pymnts.com/news/partnerships-acquisitions/2019/global-payments-tsys-merger-finalized-in-landmark-transaction/
- date: '2026-05-25'
  title: Global Payments to buy TSYS for $21.5 billion in latest ...
  url: https://www.reuters.com/article/business/global-payments-to-buy-tsys-for-215-billion-in-latest-fintech-deal-idUSKCN1SY142/
- date: '2026-05-25'
  title: TSYS Unit Signs Security-Services Deal
  url: https://www.americanbanker.com/payments/news/tsys-unit-signs-security-services-deal
- date: '2026-05-25'
  title: TSYS Acquired by FIS | SRM Blog
  url: https://srmcorp.com/fis-announces-acquisition-of-tsys-from-global-payments-a-strategic-pivot-to-reinforce-issuer-services/
- date: '2026-05-25'
  title: Global Payments to acquire TSYS in $21.5B merger
  url: https://www.atmmarketplace.com/articles/global-payments-to-acquire-tsys-in-215b-merger/
random_paper: 51
rate_limits:
- limit_count: 1
  name: Total System Services Rate Limits
  slug: total-system-services-rate-limits
rules:
- name: Total System Services API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: total-system-services-jsonschema-spectral-rules
- name: Total System Services API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: total-system-services-spectral-rules
- name: Total System Services API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: tsys-spectral-rules
score:
  band: thin
  composite: 41.7
  delta: -5.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 65.9
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 46.7
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Total System Services Authentication
  slug: total-system-services-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Total System Services Domain Security
  slug: total-system-services-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: total-system-services
tags:
- Payments
- Payment Processing
- Card Issuing
- Merchant Services
- Fintech
- Financial Services
- Fortune 1000
website: https://www.tsys.com/
---
