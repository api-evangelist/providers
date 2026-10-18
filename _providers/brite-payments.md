---
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
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-10-17'
api_count: 7
apis:
- description: API documentation for Brite Payments offering Pay by Bank integration.
  name: Brite Payments API
  slug: brite-payments-api-2
- baseURL: https://sandbox.britepaymentgroup.com
  baseurl_source: declared
  description: The Assets API from Brite Payments — 2 operation(s) for assets.
  name: Brite Payments Assets API
  slug: brite-payments-assets-api
- baseURL: https://sandbox.britepaymentgroup.com
  baseurl_source: declared
  description: The Bank Account API from Brite Payments — 1 operation(s) for bank account.
  name: Brite Payments Bank Account API
  slug: brite-payments-bank-account-api
- baseURL: https://sandbox.britepaymentgroup.com
  baseurl_source: declared
  description: The Brite Payments API API from Brite Payments — 1 operation(s) for brite payments api.
  name: Brite Payments Brite Payments API
  slug: brite-payments-brite-payments-api-api
- baseURL: https://sandbox.britepaymentgroup.com
  baseurl_source: declared
  description: The Callback API from Brite Payments — 1 operation(s) for callback.
  name: Brite Payments Callback API
  slug: brite-payments-callback-api
- baseURL: https://sandbox.britepaymentgroup.com
  baseurl_source: declared
  description: The Session API from Brite Payments — 1 operation(s) for session.
  name: Brite Payments Session API
  slug: brite-payments-session-api
- baseURL: https://sandbox.britepaymentgroup.com
  baseurl_source: declared
  description: The Transaction API from Brite Payments — 2 operation(s) for transaction.
  name: Brite Payments Transaction API
  slug: brite-payments-transaction-api
artifact_total: 16
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brite-payments/refs/heads/main/rules/brite-payments-rules.yml
  title: ''
  type: Spectral
  url: rules/brite-payments-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brite-payments/refs/heads/main/json-ld/brite-payments-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/brite-payments-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brite-payments/refs/heads/main/vocabulary/brite-payments-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/brite-payments-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brite-payments/refs/heads/main/data-model/brite-payments-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brite-payments-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brite-payments/refs/heads/main/conformance/brite-payments-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brite-payments-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brite-payments/refs/heads/main/llms/brite-payments-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brite-payments-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brite-payments/refs/heads/main/well-known/brite-payments-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brite-payments-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brite-payments/refs/heads/main/hosts/brite-payments-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brite-payments-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brite-payments/refs/heads/main/vendors/brite-payments-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brite-payments-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://britepayments.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://britepayments.com/privacy-notice/
- group: company
  title: ''
  type: Newsroom
  url: https://britepayments.com/resources/press/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brite-payments/refs/heads/main/security/brite-payments-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brite-payments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://britepayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.britepayments.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.britepayments.com/api-documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://britepayments.com/about/
- group: operate
  title: ''
  type: Support
  url: https://britepayments.com/support/
- group: company
  title: ''
  type: Blog
  url: https://britepayments.com/blog/
coverage:
  checked: '2026-10-15'
  detail: API documentation page returns HTML but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files were found.
  evidence:
  - status: 200
    url: https://docs.britepayments.com/api-documentation/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Brite Payments is a European payment institution offering instant, secure, and free-to-use online payments by connecting directly to thousands of banks across Europe. It enables merchants to accept “Pay by Bank” payments, providing instant checkout, refunds, and payouts without requiring card details. Brite serves both personal and business customers, supporting e‑commerce, charities, travel, utilities, and gaming, and emphasizes strong security, regulatory compliance, and a seamless user experience.
image: https://britepayments.com/wp-content/uploads/2026/02/home-hero-1024x576.webp
json_schemas:
- name: GetV1AssetsResponse
  property_count: 5
  slug: brite-payments-get-v1-assets-response
- name: PostApiApiidRequest
  property_count: 10
  slug: brite-payments-post-api-apiid-request
- name: PostApiApiidResponse
  property_count: 3
  slug: brite-payments-post-api-apiid-response
- name: PostBankAccountCreateResponse
  property_count: 1
  slug: brite-payments-post-bank-account-create-response
- name: PostTransactionCreateWithdrawalRequest
  property_count: 5
  slug: brite-payments-post-transaction-create-withdrawal-request
- name: PostTransactionCreateWithdrawalResponse
  property_count: 2
  slug: brite-payments-post-transaction-create-withdrawal-response
jsonld:
- class_count: 6
  name: Brite Payments Context
  property_count: 21
  slug: brite-payments-context
layout: provider
modified: '2026-10-15'
name: Brite Payments
nav: Providers
network: true
overview: 'Brite Payments is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Bank Account API, Brite Payments API, and 4 more. Tagged areas include Company, Payments, Fintech, Europe, and OnlinePayments.


  The Brite Payments catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Brite Payments'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 14 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Brite Payments API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: brite-payments-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 35.7
    discoverability: 71.4
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
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
    score: 0.0
security:
- kind: domain-security
  name: Brite Payments Domain Security
  slug: brite-payments-domain-security
  summary_line: TLSv1.3 · DMARC
slug: brite-payments
tags:
- Company
- Payments
- Fintech
- Europe
- OnlinePayments
website: https://britepayments.com/
---
