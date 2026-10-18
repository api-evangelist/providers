---
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-10-17'
api_count: 4
apis:
- baseURL: https://api.payplug.com
  baseurl_source: declared
  description: The Cards API from PayPlug — 1 operation(s) for cards.
  name: PayPlug Cards API
  slug: payplug-cards-api
- baseURL: https://api.payplug.com
  baseurl_source: declared
  description: The Installment Plans API from PayPlug — 1 operation(s) for installment plans.
  name: PayPlug Installment Plans API
  slug: payplug-installment-plans-api
- baseURL: https://api.payplug.com
  baseurl_source: declared
  description: The Payments API from PayPlug — 4 operation(s) for payments.
  name: PayPlug Payments API
  slug: payplug-payments-api
- baseURL: https://api.payplug.com
  baseurl_source: declared
  description: The PayPlug API API from PayPlug — 2 operation(s) for payplug api.
  name: PayPlug PayPlug API
  slug: payplug-payplug-api-api
artifact_total: 13
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payplug/refs/heads/main/rules/payplug-rules.yml
  title: ''
  type: Spectral
  url: rules/payplug-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payplug/refs/heads/main/json-ld/payplug-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/payplug-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payplug/refs/heads/main/vocabulary/payplug-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/payplug-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payplug/refs/heads/main/data-model/payplug-data-model.yml
  title: ''
  type: DataModel
  url: data-model/payplug-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/payplug/refs/heads/main/changelog/payplug-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/payplug-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payplug/refs/heads/main/lifecycle/payplug-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/payplug-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payplug/refs/heads/main/conformance/payplug-conformance.yml
  title: ''
  type: Conformance
  url: conformance/payplug-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/payplug/refs/heads/main/well-known/payplug-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/payplug-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/payplug/refs/heads/main/well-known/payplug-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/payplug-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/payplug/refs/heads/main/hosts/payplug-hosts.yml
  title: ''
  type: Hosts
  url: hosts/payplug-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/payplug/refs/heads/main/vendors/payplug-vendors.yml
  title: ''
  type: Vendors
  url: vendors/payplug-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/payplug/refs/heads/main/packages/payplug-packages.yml
  title: ''
  type: SDKs
  url: packages/payplug-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/payplug/refs/heads/main/packages/payplug-packages.yml
  title: ''
  type: Packages
  url: packages/payplug-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.payplug.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://help.payplug.com/hc/fr
- group: operate
  title: ''
  type: StatusPage
  url: https://status.payplug.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.payplug.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.payplug.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.payplug.com/press/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.payplug.com/
- group: company
  title: ''
  type: Blog
  url: https://www.payplug.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.payplug.com/api/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.payplug.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/payplug
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/payplug/refs/heads/main/security/payplug-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/payplug-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.payplug.com
coverage:
  checked: '2026-10-14'
  detail: Documentation at https://docs.payplug.com/api/ provides no machine‑readable OpenAPI, GraphQL, AsyncAPI or WSDL specifications.
  evidence:
  - status: 200
    url: https://docs.payplug.com/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: 'PayPlug is a company surfaced via the API Evangelist harvest backlog (source: tag-qc) and added to the network as a stub for full-pipeline profiling.'
image: https://www.payplug.com/wp-content/uploads/2023/02/visuel-payplug-1024x536-1.jpg
json_schemas:
- name: GetV1InstallmentPlansInstallmentplanidResponse
  property_count: 3
  slug: payplug-get-v1-installment-plans-installmentplanid-response
- name: GetV1PaymentsPaymentidRefundsRefundidResponse
  property_count: 3
  slug: payplug-get-v1-payments-paymentid-refunds-refundid-response
- name: GetV1PaymentsPaymentidResponse
  property_count: 9
  slug: payplug-get-v1-payments-paymentid-response
- name: PostV1PaymentsPaymentidRefundsResponse
  property_count: 3
  slug: payplug-post-v1-payments-paymentid-refunds-response
- name: PostV1V1IdRequest
  property_count: 9
  slug: payplug-post-v1-v1-id-request
- name: PostV1V1IdResponse
  property_count: 24
  slug: payplug-post-v1-v1-id-response
jsonld:
- class_count: 12
  name: Payplug Context
  property_count: 28
  slug: payplug-context
layout: provider
modified: '2026-10-14'
name: PayPlug
nav: Providers
network: true
overview: 'PayPlug is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Cards API, Installment Plans API, Payments API, and 1 more. Tagged areas include Company.


  The PayPlug catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PayPlug''s developer surface includes changelog, support, pricing, engineering blog, getting-started guide, documentation, and 20 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: PayPlug API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: payplug-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 45.2
    discoverability: 55.4
    operational_transparency: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Payplug Domain Security
  slug: payplug-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: payplug
tags:
- Company
website: https://www.payplug.com
---
