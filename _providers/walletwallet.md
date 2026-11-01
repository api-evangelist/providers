---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for creating and managing digital wallet passes.
  name: WalletWallet API
  slug: walletwallet-api-2
- baseURL: https://api.walletwallet.dev
  baseurl_source: declared
  description: 'WalletWallet API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: WalletWallet API
  slug: walletwallet-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/walletwallet/plans/walletwallet-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/walletwallet-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/walletwallet/rules/walletwallet-rules.yml
  title: ''
  type: Spectral
  url: rules/walletwallet-rules.yml
- group: design
  href: https://artifacts.apis.io/walletwallet/json-ld/walletwallet-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/walletwallet-context.jsonld
- group: design
  href: https://artifacts.apis.io/walletwallet/vocabulary/walletwallet-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/walletwallet-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/walletwallet/data-model/walletwallet-data-model.yml
  title: ''
  type: DataModel
  url: data-model/walletwallet-data-model.yml
- group: operate
  href: https://artifacts.apis.io/walletwallet/changelog/walletwallet-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/walletwallet-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.walletwallet.dev/trust/
- group: design
  href: https://artifacts.apis.io/walletwallet/conformance/walletwallet-conformance.yml
  title: ''
  type: Conformance
  url: conformance/walletwallet-conformance.yml
- group: agent
  href: https://artifacts.apis.io/walletwallet/llms/walletwallet-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/walletwallet-llms.txt
- group: agent
  href: https://artifacts.apis.io/walletwallet/well-known/walletwallet-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/walletwallet-well-known.yml
- group: other
  href: https://artifacts.apis.io/walletwallet/hosts/walletwallet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/walletwallet-hosts.yml
- group: other
  href: https://artifacts.apis.io/walletwallet/vendors/walletwallet-vendors.yml
  title: ''
  type: Vendors
  url: vendors/walletwallet-vendors.yml
- group: auth
  href: https://artifacts.apis.io/walletwallet/security/walletwallet-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/walletwallet-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/walletwallet/security/walletwallet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/walletwallet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.walletwallet.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.walletwallet.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://www.walletwallet.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.walletwallet.dev/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.walletwallet.dev/signup/
- group: operate
  title: ''
  type: Support
  url: https://www.walletwallet.dev/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.walletwallet.dev/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.walletwallet.dev/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.walletwallet.dev/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.walletwallet.dev/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.walletwallet.dev/llms.txt
coverage:
  detail: API documentation is served as HTML with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://www.walletwallet.dev/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: WalletWallet provides an API for creating, managing, and distributing digital wallet passes for Apple Wallet and Google Wallet. Their platform enables developers to generate passes, update them in real time, and host install pages, supporting use cases such as loyalty cards, event tickets, and membership cards. The service offers a free tier for up to 1,000 passes per month and integrates with various tools and frameworks.
json_schemas:
- name: DeleteApiPassesSerialResponse
  property_count: 5
  slug: walletwallet-delete-api-passes-serial-response
- name: GetApiAuthUsageResponse
  property_count: 5
  slug: walletwallet-get-api-auth-usage-response
- name: PostApiCredentialsRequest
  property_count: 2
  slug: walletwallet-post-api-credentials-request
- name: PostApiPassesRequest
  property_count: 5
  slug: walletwallet-post-api-passes-request
- name: PostApiPkpassResponse
  property_count: 4
  slug: walletwallet-post-api-pkpass-response
- name: PutApiPassesSerialRequest
  property_count: 4
  slug: walletwallet-put-api-passes-serial-request
jsonld:
- class_count: 10
  name: Walletwallet Context
  property_count: 24
  slug: walletwallet-context
layout: provider
modified: '2026-10-19'
name: WalletWallet
nav: Providers
network: true
overview: 'WalletWallet is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wallets, Passes, and Digital.


  The WalletWallet catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  WalletWallet''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Walletwallet Plans Pricing
  plan_count: 4
  slug: walletwallet-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: WalletWallet API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: walletwallet-rules
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 12.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 35.6
    contract_quality: 26.0
    developer_ergonomics: 50.0
    discoverability: 44.6
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Walletwallet Domain Security
  slug: walletwallet-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Walletwallet Trust Center
  slug: walletwallet-trust-center
  summary_line: GDPR
slug: walletwallet
tags:
- Company
- Wallets
- Passes
- Digital
website: https://www.walletwallet.dev/
---
