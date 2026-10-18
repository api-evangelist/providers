---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.2
  scored_at: '2026-10-17'
api_count: 16
apis:
- description: API for Pinch payments and medical spa services
  name: Pinch API
  slug: pinch-api-2
- baseURL: https://api.getpinch.com.au
  baseurl_source: declared
  description: The Calculate Fees API from Pinch — 1 operation(s) for calculate fees.
  name: Pinch Calculate Fees API
  slug: pinch-calculate-fees-api
- baseURL: https://api.getpinch.com.au
  baseurl_source: declared
  description: The Connect API from Pinch — 1 operation(s) for connect.
  name: Pinch Connect API
  slug: pinch-connect-api
- baseURL: https://api.getpinch.com.au
  baseurl_source: declared
  description: The Fees API from Pinch — 1 operation(s) for fees.
  name: Pinch Fees API
  slug: pinch-fees-api
- baseURL: https://api.getpinch.com.au
  baseurl_source: declared
  description: The Merchants API from Pinch — 2 operation(s) for merchants.
  name: Pinch Merchants API
  slug: pinch-merchants-api
- baseURL: https://api.getpinch.com.au
  baseurl_source: declared
  description: The Payers API from Pinch — 2 operation(s) for payers.
  name: Pinch Payers API
  slug: pinch-payers-api
- baseURL: https://api.getpinch.com.au
  baseurl_source: declared
  description: The Payment Links API from Pinch — 1 operation(s) for payment links.
  name: Pinch Payment Links API
  slug: pinch-payment-links-api
- baseURL: https://api.getpinch.com.au
  baseurl_source: declared
  description: The Payments API from Pinch — 3 operation(s) for payments.
  name: Pinch Payments API
  slug: pinch-payments-api
- baseURL: https://api.getpinch.com.au
  baseurl_source: declared
  description: The Plans API from Pinch — 2 operation(s) for plans.
  name: Pinch Plans API
  slug: pinch-plans-api
- baseURL: https://api.getpinch.com.au
  baseurl_source: declared
  description: The Refund API from Pinch — 1 operation(s) for refund.
  name: Pinch Refund API
  slug: pinch-refund-api
- baseURL: https://api.getpinch.com.au
  baseurl_source: declared
  description: The Refunds API from Pinch — 2 operation(s) for refunds.
  name: Pinch Refunds API
  slug: pinch-refunds-api
- baseURL: https://api.getpinch.com.au
  baseurl_source: declared
  description: The Sources API from Pinch — 1 operation(s) for sources.
  name: Pinch Sources API
  slug: pinch-sources-api
- baseURL: https://api.getpinch.com.au
  baseurl_source: declared
  description: The Subscriptions API from Pinch — 3 operation(s) for subscriptions.
  name: Pinch Subscriptions API
  slug: pinch-subscriptions-api
- baseURL: https://api.getpinch.com.au
  baseurl_source: declared
  description: The Test API from Pinch — 11 operation(s) for test.
  name: Pinch Test API
  slug: pinch-test-api
- baseURL: https://api.getpinch.com.au
  baseurl_source: declared
  description: The Transfers API from Pinch — 3 operation(s) for transfers.
  name: Pinch Transfers API
  slug: pinch-transfers-api
- baseURL: https://api.getpinch.com.au
  baseurl_source: declared
  description: The Webhooks API from Pinch — 1 operation(s) for webhooks.
  name: Pinch Webhooks API
  slug: pinch-webhooks-api
artifact_total: 26
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pinch/refs/heads/main/rules/pinch-rules.yml
  title: ''
  type: Spectral
  url: rules/pinch-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pinch/refs/heads/main/json-ld/pinch-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pinch-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pinch/refs/heads/main/vocabulary/pinch-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pinch-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pinch/refs/heads/main/data-model/pinch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pinch-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pinch/refs/heads/main/changelog/pinch-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pinch-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pinch/refs/heads/main/conventions/pinch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pinch-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pinch/refs/heads/main/authentication/pinch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pinch-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pinch/refs/heads/main/lifecycle/pinch-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pinch-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pinch/refs/heads/main/conformance/pinch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pinch-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pinch/refs/heads/main/llms/pinch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pinch-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pinch/refs/heads/main/well-known/pinch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pinch-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pinch/refs/heads/main/hosts/pinch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pinch-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pinch/refs/heads/main/vendors/pinch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pinch-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pinch/refs/heads/main/security/pinch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pinch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bookpinch.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getpinch.com.au
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getpinch.com.au
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getpinch.com.au/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getpinch.com.au/docs/get-started-with-the-pinch-api
- group: operate
  title: ''
  type: Support
  url: https://helpdesk.getpinch.com.au
- group: company
  title: ''
  type: Blog
  url: https://blog.getpinch.com.au
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PinchPayments
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.getpinch.com.au/docs/plans-and-subscriptions
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bookpinch.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bookpinch.com/privacy-policy
coverage:
  checked: '2026-10-12'
  detail: Docs site returns HTTP 429 rate limit errors, preventing access to machine‑readable spec.
  evidence:
  - status: 429
    url: https://docs.getpinch.com.au/reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Pinch provides an at‑home medical spa experience combined with a payments platform that enables businesses to accept online payments for aesthetic treatments. The company offers a suite of APIs for managing customers, processing credit‑card and direct‑debit transactions, handling subscriptions, and integrating with third‑party services. Documentation includes guides, reference API specs, and SDKs for multiple languages, supporting developers to build seamless checkout flows for health‑and‑beauty services.
image: https://cdn.sanity.io/images/98lcnac0/production/0a4bcd959a4eab98b8cf8add62ab1244db0c6462-4000x2667.jpg
json_schemas:
- name: PostCalculateFeesResponse
  property_count: 4
  slug: pinch-post-calculate-fees-response
- name: PostMerchantsMerchantidRequest
  property_count: 6
  slug: pinch-post-merchants-merchantid-request
- name: PostPlansRequest
  property_count: 3
  slug: pinch-post-plans-request
- name: PostRefundsRequest
  property_count: 4
  slug: pinch-post-refunds-request
- name: PostRefundsResponse
  property_count: 2
  slug: pinch-post-refunds-response
- name: PostSubscriptionsRequest
  property_count: 6
  slug: pinch-post-subscriptions-request
jsonld:
- class_count: 25
  name: Pinch Context
  property_count: 41
  slug: pinch-context
layout: provider
modified: '2026-10-12'
name: Pinch
nav: Providers
network: true
overview: 'Pinch is listed with 16 APIs on the [APIs.io](https://apis.io/) network, including Calculate Fees API, Connect API, Fees API, and 13 more. Tagged areas include Company, Payments, MedicalSpa, and Health Tech.


  The Pinch catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Pinch''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 18 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Pinch API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: pinch-rules
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 57.1
    discoverability: 60.7
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 16
      marker_coverage: 100.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Pinch Authentication
  slug: pinch-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Pinch Domain Security
  slug: pinch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pinch
tags:
- Company
- Payments
- MedicalSpa
- Health Tech
website: https://bookpinch.com
---
