---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Total System Services Agentic Access
  operation_count: 23
  slug: total-system-services-agentic-access
  summary_line: 23 operations · 13 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://issuing.api.tsys.com/v1
  baseurl_source: spec
  description: Cardholder account management
  name: Total System Services Accounts API
  slug: total-system-services-accounts-api
- baseURL: https://api.tsys.com/v1
  baseurl_source: spec
  description: Authorize card payments
  name: Total System Services Authorization API
  slug: total-system-services-authorization-api
- baseURL: https://api.tsys.com/v1
  baseurl_source: spec
  description: Capture authorized transactions
  name: Total System Services Capture API
  slug: total-system-services-capture-api
- baseURL: https://issuing.api.tsys.com/v1
  baseurl_source: spec
  description: Card lifecycle management
  name: Total System Services Cards API
  slug: total-system-services-cards-api
- baseURL: https://issuing.api.tsys.com/v1
  baseurl_source: spec
  description: Spending controls and limits
  name: Total System Services Controls API
  slug: total-system-services-controls-api
- baseURL: https://issuing.api.tsys.com/v1
  baseurl_source: spec
  description: Transaction dispute management
  name: Total System Services Disputes API
  slug: total-system-services-disputes-api
- baseURL: https://api.tsys.com/v1
  baseurl_source: spec
  description: Look up transaction status
  name: Total System Services Inquiries API
  slug: total-system-services-inquiries-api
- baseURL: https://api.tsys.com/v1
  baseurl_source: spec
  description: Process refunds and credits
  name: Total System Services Refunds API
  slug: total-system-services-refunds-api
- baseURL: https://issuing.api.tsys.com/v1
  baseurl_source: spec
  description: Card transaction history
  name: Total System Services Transactions API
  slug: total-system-services-transactions-api
- baseURL: https://api.tsys.com/v1
  baseurl_source: spec
  description: Void pending transactions
  name: Total System Services Voids API
  slug: total-system-services-voids-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TSYS Issuing Platform Accounts API
  slug: open-total-system-services-accounts-api
- collection_type: open
  name: TSYS Issuing Platform Accounts Authorization API
  slug: open-total-system-services-authorization-api
- collection_type: open
  name: TSYS Issuing Platform Accounts Capture API
  slug: open-total-system-services-capture-api
- collection_type: open
  name: TSYS Issuing Platform Accounts Cards API
  slug: open-total-system-services-cards-api
- collection_type: open
  name: TSYS Issuing Platform Accounts Controls API
  slug: open-total-system-services-controls-api
- collection_type: open
  name: TSYS Issuing Platform Accounts Disputes API
  slug: open-total-system-services-disputes-api
- collection_type: open
  name: TSYS Issuing Platform Accounts Inquiries API
  slug: open-total-system-services-inquiries-api
- collection_type: open
  name: TSYS Issuing Platform Accounts Refunds API
  slug: open-total-system-services-refunds-api
- collection_type: open
  name: TSYS Issuing Platform Accounts Transactions API
  slug: open-total-system-services-transactions-api
- collection_type: open
  name: TSYS Issuing Platform Accounts Voids API
  slug: open-total-system-services-voids-api
- collection_type: open
  name: TSYS Issuing Platform
  slug: open-tsys-issuing
- collection_type: open
  name: TSYS Payment Gateway
  slug: open-tsys-payment-gateway
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/total-system-services-capability-edges.yml
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


  Total System Services'' developer surface includes authentication, documentation, and 10 more developer resources.'
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
random_paper: 20
rate_limits:
- limit_count: 1
  name: Total System Services Rate Limits
  slug: total-system-services-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Total System Services API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: total-system-services-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Total System Services API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: total-system-services-spectral-rules
- effective_rule_count: 10
  extends: []
  name: Total System Services API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: tsys-spectral-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 56.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 59.1
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 31.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 60.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
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
- Financial-Services
- Fortune 1000
website: https://www.tsys.com/
---
