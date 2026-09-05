---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Splitit Agentic Access
  operation_count: 18
  slug: splitit-agentic-access
  summary_line: 18 operations · 13 acting
api_count: 2
apis:
- description: The updated version of the Splitit Installments API offering enhanced capabilities for creating and managing credit card installment plans with improvements over the v3 API.
  name: Splitit Installments API v4
  slug: splitit-installments-api-v4
- description: API for onboarding and managing sub-merchants on the Splitit platform. Enables payment facilitators and marketplace operators to add merchant partners, upload compliance documents, send onboarding inv
  name: Splitit Account Management System API
  slug: splitit-account-management-system-api
- description: API for retrieving merchant-level reporting data including transaction history, installment plan summaries, funding reports, and reconciliation data for merchants operating on the Splitit platform.
  name: Splitit Merchant Reports API
  slug: splitit-merchant-reports-api
- description: API for creating and managing encryption keys used to secure payment data during Splitit integrations. Supports cryptographic key management for secure card data handling in compliance with PCI DSS re
  name: Splitit Key Exchange Server API
  slug: splitit-key-exchange-server-api
- description: API for handling and managing chargebacks on Splitit installment plans. Enables merchants to respond to, track, and resolve chargeback disputes for installment transactions processed through the Split
  name: Splitit Chargebacks API
  slug: splitit-chargebacks-api
- description: API enabling merchants to initiate Splitit installment payment flows via SMS, email, and QR codes as part of the Splitit Go product. Allows sending payment links to shoppers through non-traditional ch
  name: Splitit Text-to-Pay API
  slug: splitit-text-to-pay-api
- baseURL: https://webapi.production.splitit.com
  baseurl_source: declared
  description: Obtain access tokens
  name: Splitit Authentication API
  slug: splitit-authentication-api
- baseURL: https://webapi.production.splitit.com
  baseurl_source: declared
  description: Check shopper eligibility for installment plans
  name: Splitit Eligibility API
  slug: splitit-eligibility-api
- baseURL: https://webapi.production.splitit.com
  baseurl_source: declared
  description: Create, initiate, fetch, update, refund, and cancel installment plans
  name: Splitit Installment Plans API
  slug: splitit-installment-plans-api
- baseURL: https://webapi.production.splitit.com
  baseurl_source: declared
  description: Onboard and manage merchant partners
  name: Splitit Merchant Management API
  slug: splitit-merchant-management-api
artifact_total: 32
collections:
- collection_type: postman
  name: Splitit Account Management System Authentication API
  slug: postman-splitit-authentication-api
- collection_type: postman
  name: Splitit Account Management System Authentication Eligibility API
  slug: postman-splitit-eligibility-api
- collection_type: postman
  name: Splitit Account Management System Authentication Installment Plans API
  slug: postman-splitit-installment-plans-api
- collection_type: postman
  name: Splitit Account Management System Authentication Merchant Management API
  slug: postman-splitit-merchant-management-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Splitit Account Management System Authentication API
  slug: open-splitit-authentication-api
- collection_type: open
  name: Splitit Account Management System Authentication Eligibility API
  slug: open-splitit-eligibility-api
- collection_type: open
  name: Splitit Account Management System Authentication Installment Plans API
  slug: open-splitit-installment-plans-api
- collection_type: open
  name: Splitit Account Management System Authentication Merchant Management API
  slug: open-splitit-merchant-management-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/splitit/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/splitit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/splitit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/splitit-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.splitit.com/
- group: start
  title: ''
  type: Signup
  url: https://register-developer.sandbox.splitit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.splitit.com/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.splitit.com/direct-api/quickstart/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/splitit
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/Splitit/Python-SDK
- group: build
  title: ''
  type: TypeScript SDK
  url: https://github.com/Splitit/TypeScript-SDK
- group: build
  title: ''
  type: Go SDK
  url: https://github.com/Splitit/Go-SDK
- group: build
  title: ''
  type: Java SDK
  url: https://github.com/Splitit/Java-SDK
- group: build
  title: ''
  type: DotNet SDK
  url: https://github.com/Splitit/.NET-C-SDK
- group: build
  title: ''
  type: PHP SDK
  url: https://github.com/Splitit/PHP-SDK
- group: design
  title: ''
  type: Webhooks
  url: https://developers.splitit.com/category/direct-api-implementations/
- group: build
  title: ''
  type: Plugins
  url: https://developers.splitit.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.splitit.com/business/pricing-plans/
- group: auth
  title: ''
  type: Trust
  url: https://trust.splitit.com
- group: operate
  title: ''
  type: Contact
  url: https://www.splitit.com/contact-sales/
- group: start
  title: ''
  type: Merchant Portal
  url: https://merchant.splitit.com
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/splitit/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/splitit/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/splitit/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Splitit is a credit card installment platform that enables merchants to offer shoppers the ability to split existing credit card purchases into monthly installments without requiring new credit applications, additional interest charges, or third-party redirects. The platform operates directly on shoppers' existing credit cards, leveraging available credit to create installment plans while merchants receive full payment upfront. Splitit provides REST APIs for installment plan creation, eligibility checking, refunds, chargebacks, and merchant onboarding, along with plugins for major e-commerce platforms.
examples:
- key_count: 7
  name: Check Eligibility
  slug: check-eligibility
- key_count: 7
  name: Create Installment Plan
  slug: create-installment-plan
- key_count: 7
  name: Initiate Installment Plan
  slug: initiate-installment-plan
- key_count: 7
  name: Refund Plan
  slug: refund-plan
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/splitit.png
json_schemas:
- name: Splitit Installment Plan
  property_count: 9
  slug: installment-plan
jsonld:
- class_count: 33
  name: Splitit Context
  property_count: 20
  slug: splitit-context
layout: provider
modified: '2026-06-13'
name: Splitit
nav: Providers
network: true
overview: 'Splitit publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Eligibility API, Installment Plans API, and 1 more. Tagged areas include Payments, Installments, Buy Now Pay Later, Credit Card, and Fintech.


  The Splitit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Splitit''s developer surface includes authentication, developer portal, signup flow, documentation, getting-started guide, pricing, and 18 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 0
rate_limits:
- limit_count: 4
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Splitit API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: splitit-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 78.3
    catalog_earned_first_party: 0.0
    catalog_gap: 36.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 9.8
    contract_quality: 64.7
    developer_ergonomics: 60.7
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 39.5
  previous_composite: 56.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/splitit/refs/heads/main/screenshots/splitit-2026-06-20T194331.png
security:
- kind: authentication
  name: Splitit Authentication
  slug: splitit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Splitit Domain Security
  slug: splitit-domain-security
  summary_line: TLSv1.3 · DMARC
slug: splitit
tags:
- Payments
- Installments
- Buy Now Pay Later
- Credit Card
- Fintech
- E-Commerce
website: https://developers.splitit.com/
---
