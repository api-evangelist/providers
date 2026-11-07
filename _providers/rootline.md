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
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: Rootline Payment API providing endpoints for payments, accounts, webhooks, and more.
  name: Rootline API
  slug: rootline-api
- baseURL: https://payment-api.staging.rootline.com
  baseurl_source: declared
  description: 'Rootline core API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Rootline core API
  slug: core-api
- baseURL: https://payment-api.staging.rootline.com
  baseurl_source: declared
  description: 'Rootline in person payments API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Rootline in person payments API
  slug: in-person-payments-api
- baseURL: https://payment-api.staging.rootline.com
  baseurl_source: declared
  description: 'Rootline payments API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Rootline payments API
  slug: payments-api
artifact_total: 25
common:
- group: design
  href: https://artifacts.apis.io/rootline/rules/rootline-rules.yml
  title: ''
  type: Spectral
  url: rules/rootline-rules.yml
- group: design
  href: https://artifacts.apis.io/rootline/json-ld/rootline-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rootline-context.jsonld
- group: design
  href: https://artifacts.apis.io/rootline/vocabulary/rootline-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rootline-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/rootline/data-model/rootline-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rootline-data-model.yml
- group: operate
  href: https://artifacts.apis.io/rootline/changelog/rootline-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/rootline-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://rootline.com/legal/responsible-disclosure-policy
- group: auth
  href: https://artifacts.apis.io/rootline/authentication/rootline-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rootline-authentication.yml
- group: design
  href: https://artifacts.apis.io/rootline/lifecycle/rootline-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rootline-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/rootline/errors/rootline-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/rootline-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/rootline/errors/rootline-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rootline-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rootline/conformance/rootline-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rootline-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rootline/llms/rootline-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rootline-llms.txt
- group: auth
  href: https://artifacts.apis.io/rootline/well-known/rootline-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rootline-security.txt
- group: agent
  href: https://artifacts.apis.io/rootline/well-known/rootline-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rootline-well-known.yml
- group: other
  href: https://artifacts.apis.io/rootline/hosts/rootline-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rootline-hosts.yml
- group: other
  href: https://artifacts.apis.io/rootline/vendors/rootline-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rootline-vendors.yml
- group: build
  href: https://artifacts.apis.io/rootline/packages/rootline-packages.yml
  title: ''
  type: SDKs
  url: packages/rootline-packages.yml
- group: build
  href: https://artifacts.apis.io/rootline/packages/rootline-packages.yml
  title: ''
  type: Packages
  url: packages/rootline-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rootline.com/legal/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rootline.com/
- group: start
  title: ''
  type: SignUp
  url: https://rootline.com/old/meetups/signup/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rootline.com/legal/privacy-statement
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rootline.com/guides/get-started/quick-start
- group: auth
  href: https://artifacts.apis.io/rootline/security/rootline-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/rootline-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/rootline/security/rootline-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rootline-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rootline.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rootline.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rootline.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rootline.com/api
- group: company
  title: ''
  type: Blog
  url: https://rootline.com/blog
- group: operate
  title: ''
  type: Support
  url: https://rootline.com/contact/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rootline
coverage:
  checked: '2026-10-29'
  detail: Public documentation provides endpoint information but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://docs.rootline.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Rootline provides an embedded payments platform that enables businesses to integrate online and in-person payment processing, fee configuration, fund routing, and real-time reconciliation through a single API. The solution supports multiple payment methods, dynamic fee structures, multi-entity payouts, and offers a developer portal with comprehensive documentation and API reference.
image: https://framerusercontent.com/images/3LNDLzE6Qeqjxj5QokF5OuQsiU.png
json_schemas:
- name: DeleteV1PaymentDevicesPaymentdeviceidAppsPaymentdeviceappidR
  property_count: 1
  slug: rootline-delete-v1-payment-devices-paymentdeviceid-apps-paymentdeviceappid-r
- name: GetPaymentsPaymentidResponse
  property_count: 11
  slug: rootline-get-payments-paymentid-response
- name: GetV1AccountsAccountidResponse
  property_count: 10
  slug: rootline-get-v1-accounts-accountid-response
- name: GetV1CustomersCustomeridPaymentTokensResponse
  property_count: 5
  slug: rootline-get-v1-customers-customerid-payment-tokens-response
- name: GetV1PaymentTokensIdResponse
  property_count: 5
  slug: rootline-get-v1-payment-tokens-id-response
- name: GetV1PaymentsPaymentidAbortResponse
  property_count: 4
  slug: rootline-get-v1-payments-paymentid-abort-response
- name: PatchPaymentsIdRequest
  property_count: 1
  slug: rootline-patch-payments-id-request
- name: PatchPaymentsIdResponse
  property_count: 2
  slug: rootline-patch-payments-id-response
- name: PatchV1PaymentDevicesPaymentdeviceidAppsPaymentdeviceappidRe
  property_count: 1
  slug: rootline-patch-v1-payment-devices-paymentdeviceid-apps-paymentdeviceappid-re
- name: PostV1AppsAppidAppVersionsRequest
  property_count: 2
  slug: rootline-post-v1-apps-appid-app-versions-request
- name: PostV1AppsRequest
  property_count: 2
  slug: rootline-post-v1-apps-request
- name: PostV1CustomersRequest
  property_count: 6
  slug: rootline-post-v1-customers-request
- name: PostV1CustomersResponse
  property_count: 7
  slug: rootline-post-v1-customers-response
- name: PostV1PaymentDevicesPaymentdeviceidAppsRequest
  property_count: 1
  slug: rootline-post-v1-payment-devices-paymentdeviceid-apps-request
- name: PostV1PaymentsRequest
  property_count: 5
  slug: rootline-post-v1-payments-request
- name: PostV1PaymentsResponse
  property_count: 4
  slug: rootline-post-v1-payments-response
jsonld:
- class_count: 22
  name: Rootline Context
  property_count: 48
  slug: rootline-context
layout: provider
modified: '2026-10-29'
name: Rootline
nav: Providers
network: true
overview: 'Rootline is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including core API, in person payments API, payments API, and 1 more. Tagged areas include Payments, Fintech, Embedded Payments, and Platform.


  The Rootline catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Rootline''s developer surface includes changelog, authentication, signup flow, getting-started guide, documentation, API reference, engineering blog, and 25 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Rootline API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: rootline-rules
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.5
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 25.9
    developer_ergonomics: 41.7
    discoverability: 69.6
    operational_transparency: 31.6
  previous_composite: 43.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/rootline/rootline-2026-11-03T142406.png
security:
- kind: authentication
  name: Rootline Authentication
  slug: rootline-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Rootline Domain Security
  slug: rootline-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Rootline Vulnerability Disclosure
  slug: rootline-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: rootline
tags:
- Payments
- Fintech
- Embedded Payments
- Platform
website: https://rootline.com/
---
