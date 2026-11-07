---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API reference for Amazon Payment Services covering payment processing, hosted checkout, tokenization, and related operations.
  name: Amazon Payment Services API
  slug: amazon-payment-services-api-2
- description: 'Amazon Payment Services API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Amazon Payment Services API
  slug: amazon-payment-services-api
artifact_total: 13
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.amazon.com/terms-and-agreements
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paymentservices.amazon.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AmazonAppDev
- group: start
  title: ''
  type: GettingStarted
  url: https://paymentservices.amazon.com/docs/getting-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.amazon.com/
- group: design
  href: https://artifacts.apis.io/amazon-payment-services/rules/amazon-payment-services-rules.yml
  title: ''
  type: Spectral
  url: rules/amazon-payment-services-rules.yml
- group: design
  href: https://artifacts.apis.io/amazon-payment-services/json-ld/amazon-payment-services-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-payment-services-context.jsonld
- group: design
  href: https://artifacts.apis.io/amazon-payment-services/vocabulary/amazon-payment-services-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-payment-services-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/amazon-payment-services/data-model/amazon-payment-services-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amazon-payment-services-data-model.yml
- group: start
  href: https://artifacts.apis.io/amazon-payment-services/sandbox/amazon-payment-services-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/amazon-payment-services-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/amazonvrp
- group: auth
  href: https://artifacts.apis.io/amazon-payment-services/authentication/amazon-payment-services-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-payment-services-authentication.yml
- group: design
  href: https://artifacts.apis.io/amazon-payment-services/conformance/amazon-payment-services-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amazon-payment-services-conformance.yml
- group: agent
  href: https://artifacts.apis.io/amazon-payment-services/llms/amazon-payment-services-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amazon-payment-services-llms.txt
- group: auth
  href: https://artifacts.apis.io/amazon-payment-services/well-known/amazon-payment-services-aws-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amazon-payment-services-aws-security.txt
- group: agent
  href: https://artifacts.apis.io/amazon-payment-services/well-known/amazon-payment-services-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazon-payment-services-well-known.yml
- group: other
  href: https://artifacts.apis.io/amazon-payment-services/hosts/amazon-payment-services-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amazon-payment-services-hosts.yml
- group: other
  href: https://artifacts.apis.io/amazon-payment-services/vendors/amazon-payment-services-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amazon-payment-services-vendors.yml
- group: build
  href: https://artifacts.apis.io/amazon-payment-services/packages/amazon-payment-services-packages.yml
  title: ''
  type: SDKs
  url: packages/amazon-payment-services-packages.yml
- group: build
  href: https://artifacts.apis.io/amazon-payment-services/packages/amazon-payment-services-packages.yml
  title: ''
  type: Packages
  url: packages/amazon-payment-services-packages.yml
- group: auth
  href: https://artifacts.apis.io/amazon-payment-services/security/amazon-payment-services-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-payment-services-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-payment-services/security/amazon-payment-services-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-payment-services-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://paymentservices.amazon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://paymentservices.amazon.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://paymentservices.amazon.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://paymentservices.amazon.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://paymentservices.amazon.com/blog
- group: other
  title: ''
  type: GetStarted
  url: https://paymentservices.amazon.com/get-started/dashboard
coverage:
  checked: '2026-10-27'
  detail: API documentation is rendered via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://paymentservices.amazon.com/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Amazon Payment Services provides payment processing solutions that enable merchants to accept online payments across multiple channels, including credit cards, debit cards, and alternative payment methods. Leveraging Amazon’s global infrastructure, the service offers secure, scalable, and compliant transaction handling, fraud detection, and settlement capabilities for businesses of all sizes. It integrates with e‑commerce platforms, mobile apps, and point‑of‑sale systems, delivering a seamless checkout experience while adhering to PCI DSS standards and regional regulatory requirements.
image: https://m.media-amazon.com/images/G/01/APS/website/Amazon-Payment-Services-Launched-in-MENA-1-1440x564_c1.png
json_schemas:
- name: GetFortapiPaymentapiResponse
  property_count: 11
  slug: amazon-payment-services-get-fortapi-paymentapi-response
- name: PostFortapiBatchapiResponse
  property_count: 11
  slug: amazon-payment-services-post-fortapi-batchapi-response
- name: PostFortapiPaymentapiRequest
  property_count: 9
  slug: amazon-payment-services-post-fortapi-paymentapi-request
- name: PostFortapiPaymentapiResponse
  property_count: 18
  slug: amazon-payment-services-post-fortapi-paymentapi-response
- name: PostFortapiUploadResponse
  property_count: 10
  slug: amazon-payment-services-post-fortapi-upload-response
- name: PostIntegrationBatchBatchapiResponse
  property_count: 10
  slug: amazon-payment-services-post-integration-batch-batchapi-response
jsonld:
- class_count: 7
  name: Amazon Payment Services Context
  property_count: 23
  slug: amazon-payment-services-context
layout: provider
modified: '2026-10-27'
name: Amazon Payment Services
nav: Providers
network: true
overview: 'Amazon Payment Services is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, E-Commerce, and PaymentsGateway.


  The Amazon Payment Services catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Amazon Payment Services'' developer surface includes getting-started guide, sandbox, authentication, documentation, API reference, pricing, engineering blog, and 21 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: Amazon Payment Services API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: amazon-payment-services-rules
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.8
  facets:
    access_clarity: 26.3
    contract_governance: 35.6
    contract_quality: 23.9
    developer_ergonomics: 52.4
    discoverability: 64.3
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 31.6
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/amazon-payment-services/amazon-payment-services-2026-11-03T120803.png
security:
- kind: authentication
  name: Amazon Payment Services Authentication
  slug: amazon-payment-services-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Amazon Payment Services Domain Security
  slug: amazon-payment-services-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Payment Services Vulnerability Disclosure
  slug: amazon-payment-services-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: amazon-payment-services
tags:
- Company
- Payments
- Fintech
- E-Commerce
- PaymentsGateway
website: https://paymentservices.amazon.com/
---
