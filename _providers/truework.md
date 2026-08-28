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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Truework Agentic Access
  operation_count: 16
  slug: truework-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 5
apis:
- description: Truework.js is the client-side JavaScript library that powers Truework Direct, the borrower-driven (consumer-permissioned) verification flow. The host page loads `https://js.truework.com/v1` and initi
  name: Truework.js (Truework Direct)
  slug: truework-js
- description: The subpackage_orders API from Truework — 8 operation(s) for subpackage_orders.
  name: Truework subpackage_orders API
  slug: truework-subpackage-orders-api
- description: The subpackage_qualificationChecks API from Truework — 3 operation(s) for subpackage_qualificationchecks.
  name: Truework subpackage_qualificationChecks API
  slug: truework-subpackage-qualificationchecks-api
- description: The subpackage_reports API from Truework — 1 operation(s) for subpackage_reports.
  name: Truework subpackage_reports API
  slug: truework-subpackage-reports-api
- description: The subpackage_tenantProperties API from Truework — 2 operation(s) for subpackage_tenantproperties.
  name: Truework subpackage_tenantProperties API
  slug: truework-subpackage-tenantproperties-api
artifact_total: 45
collections:
- collection_type: postman
  name: Truework Qualifications & Tenant Properties API (Beta) subpackage_orders API
  slug: postman-truework-subpackage-orders-api
- collection_type: postman
  name: Truework Qualifications & Tenant Properties API (Beta) subpackage_orders subpackage_qualificationChecks API
  slug: postman-truework-subpackage-qualificationchecks-api
- collection_type: postman
  name: Truework Qualifications & Tenant Properties API (Beta) subpackage_orders subpackage_reports API
  slug: postman-truework-subpackage-reports-api
- collection_type: postman
  name: Truework Qualifications & Tenant Properties API (Beta) subpackage_orders subpackage_tenantProperties API
  slug: postman-truework-subpackage-tenantproperties-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Truework Qualifications & Tenant Properties API (Beta)
  slug: open-truework-beta
- collection_type: open
  name: Truework Qualifications & Tenant Properties API (Beta) subpackage_orders API
  slug: open-truework-subpackage-orders-api
- collection_type: open
  name: Truework Qualifications & Tenant Properties API (Beta) subpackage_orders subpackage_qualificationChecks API
  slug: open-truework-subpackage-qualificationchecks-api
- collection_type: open
  name: Truework Qualifications & Tenant Properties API (Beta) subpackage_orders subpackage_reports API
  slug: open-truework-subpackage-reports-api
- collection_type: open
  name: Truework Qualifications & Tenant Properties API (Beta) subpackage_orders subpackage_tenantProperties API
  slug: open-truework-subpackage-tenantproperties-api
- collection_type: open
  name: Truework Verifications API
  slug: open-truework-verifications-orders
- collection_type: open
  name: Truework Webhooks
  slug: open-truework-webhooks
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/truework/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/truework-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truework-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/truework-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.truework.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.truework.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.truework.com/docs/api-reference
- group: docs
  title: ''
  type: Documentation
  url: https://www.truework.com/docs/api-reference/versions/2023-10-30
- group: docs
  title: ''
  type: Documentation
  url: https://www.truework.com/docs/api-reference/versions
- group: design
  title: ''
  type: Versioning
  url: https://www.truework.com/docs/api-reference/versions
- group: auth
  title: ''
  type: Authentication
  url: https://www.truework.com/docs/api-reference/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://www.truework.com/docs/api-reference/limits
- group: design
  title: ''
  type: ErrorCodes
  url: https://www.truework.com/docs/api-reference/versions/2023-10-30
- group: start
  title: ''
  type: Sandbox
  url: https://www.truework.com/docs/api-reference/sandbox
- group: docs
  title: ''
  type: Documentation
  url: https://www.truework.com/docs/api-reference/sandbox/test-cases
- group: docs
  title: ''
  type: Documentation
  url: https://www.truework.com/docs/api-reference/monitoring
- group: design
  title: ''
  type: Webhooks
  url: https://www.truework.com/docs/api-reference/webhooks
- group: docs
  title: ''
  type: Documentation
  url: https://www.truework.com/docs/api-reference/webhooks/security
- group: docs
  title: ''
  type: Documentation
  url: https://www.truework.com/docs/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://www.truework.com/docs/guides/api/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://www.truework.com/docs/guides/methods
- group: docs
  title: ''
  type: Documentation
  url: https://www.truework.com/docs/guides/workflows
- group: docs
  title: ''
  type: Documentation
  url: https://www.truework.com/docs/guides/truework-direct/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://www.truework.com/docs/guides/truework-direct/truework-js-reference
- group: docs
  title: ''
  type: Documentation
  url: https://www.truework.com/docs/guides/mortgage/mortgage-intro
- group: docs
  title: ''
  type: Documentation
  url: https://www.truework.com/docs/guides/mortgage/mortgage-los
- group: docs
  title: ''
  type: Documentation
  url: https://www.truework.com/docs/guides/mortgage/mortgage-pos
- group: start
  title: ''
  type: Portal
  url: https://www.truework.com/products/api
- group: start
  title: ''
  type: Portal
  url: https://www.truework.com/products
- group: start
  title: ''
  type: Signup
  url: https://app.truework.com/requester/signup
- group: start
  title: ''
  type: Login
  url: https://app.truework.com/requester/login
- group: start
  title: ''
  type: Sandbox
  url: https://api.truework-sandbox.com
- group: operate
  title: ''
  type: StatusPage
  url: https://truework.statuspage.io
- group: operate
  title: ''
  type: Support
  url: https://help.truework.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.truework.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.truework.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/truework
- group: build
  title: ''
  type: SDKs
  url: https://github.com/truework/truework.js-examples
- group: build
  title: ''
  type: Tools
  url: https://github.com/truework/gretchen
- group: build
  title: ''
  type: Tools
  url: https://github.com/truework/mounty
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/truework
- group: company
  title: ''
  type: Blog
  url: https://www.truework.com/resource-center/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/truework-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/truework-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/truework-finops.yml
created: '2026-05-24T00:00:00.000Z'
description: Truework operates a unified income and employment verification platform for mortgage lenders, credit unions, and fintechs. The Truework API orchestrates six verification methods — Instant Data, Payroll Credentials, Bank Credentials, Tax Credentials, Smart Outreach, and Document Upload — behind a single REST surface (api.truework.com), asynchronous webhooks, and the Truework.js / Truework Direct widget for consumer-permissioned verifications. The platform claims coverage of more than 97% of U.S. workers and 75% completion rates versus a ~48% industry average. Core resources are Orders, Verification Requests, Reports, and Order Events, with beta surfaces for Qualification Checks and Tenant Properties.
features:
- Six verification methods orchestrated automatically — Instant Data, Payroll Credentials, Bank Credentials, Tax Credentials, Smart Outreach, Document Upload
- Coverage of over 97% of U.S. workers from a single platform
- Truework Direct (Truework.js) borrower-driven verification widget loaded from https://js.truework.com/v1
- Dated API versioning (current 2023-10-30) with per-key version pinning via the Accept header
- Bearer-token API keys, prefixed tw_sk_ (production) and tw_sk_test_ (sandbox)
- Publishable keys (tw_pk_, tw_pk_test_) for client-side Truework.js
- Sandbox environment at https://api.truework-sandbox.com with deterministic test SSN fixtures
- Webhook delivery with 48-hour retry and X-Truework-Token header authentication
- Up to 10 webhook destinations per account
- 10 req/s per source IP and 10 req/s per account rate envelope, with 429 on overage
- Order lifecycle states pending-approval, processing, action-required, completed, canceled, invalid
- Asynchronous target-employer orders plus synchronous employer-search orders
- Reverification endpoint POST /orders/reverification for refreshing prior reports
- Beta Qualification Checks for low-latency knockout decisioning on verified income/employment
- Beta Tenant Properties for tenant-scoped verification configuration
- GSE-ready unified reporting (Day 1 Certainty, AIM, GUS) for mortgage lenders
- LOS integrations (Encompass, Empower) and POS integrations (Blend, nCino)
- Public OpenAPI specs published from truework.docs.buildwithfern.com
finops:
- name: Truework Finops
  service_category: Identity and Verification
  slug: truework-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/truework.png
json_schemas:
- name: Truework Order
  property_count: 0
  slug: truework-order
- name: Truework Verification Report
  property_count: 0
  slug: truework-report
jsonld:
- class_count: 0
  name: Truework Context
  property_count: 8
  slug: truework-context
layout: provider
modified: '2026-05-24'
name: Truework
nav: Providers
network: true
overview: 'Truework publishes 4 APIs on the [APIs.io](https://apis.io/) network, including subpackage_orders API, subpackage_qualificationChecks API, subpackage_reports API, and 1 more. Tagged areas include Verification, Income Verification, Employment Verification, VOIE, and Mortgage.


  The Truework catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Truework''s developer surface includes authentication, developer portal, documentation, sandbox, getting-started guide, signup flow, support, and 38 more developer resources.'
plans:
- name: Truework Plans Pricing
  plan_count: 3
  slug: truework-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Truework Rate Limits
  slug: truework-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Truework API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: truework-jsonschema-spectral-rules
score:
  band: strong
  composite: 57.4
  delta: 0.8
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 9.8
    contract_quality: 70.7
    developer_ergonomics: 69.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 73.7
  previous_composite: 56.6
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
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/truework/refs/heads/main/screenshots/truework-2026-06-20T195901.png
security:
- kind: authentication
  name: Truework Authentication
  slug: truework-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Truework Domain Security
  slug: truework-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: truework
tags:
- Verification
- Income Verification
- Employment Verification
- VOIE
- Mortgage
- Lending
- Credit Unions
- Identity
- KYC
- Fintech
website: https://www.truework.com
---
