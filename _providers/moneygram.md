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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.9
  scored_at: '2026-10-17'
api_count: 9
apis:
- baseURL: https://sandboxapi.moneygram.com
  baseurl_source: declared
  description: The Accounts API from MoneyGram — 1 operation(s) for accounts.
  name: MoneyGram Accounts API
  slug: moneygram-accounts-api
- baseURL: https://sandboxapi.moneygram.com
  baseurl_source: declared
  description: The Amend API from MoneyGram — 1 operation(s) for amend.
  name: MoneyGram Amend API
  slug: moneygram-amend-api
- baseURL: https://sandboxapi.moneygram.com
  baseurl_source: declared
  description: The Fx Rate API from MoneyGram — 1 operation(s) for fx rate.
  name: MoneyGram Fx Rate API
  slug: moneygram-fx-rate-api
- baseURL: https://sandboxapi.moneygram.com
  baseurl_source: declared
  description: The Oauth API from MoneyGram — 1 operation(s) for oauth.
  name: MoneyGram OAuth API
  slug: moneygram-oauth-api
- baseURL: https://sandboxapi.moneygram.com
  baseurl_source: declared
  description: The Partnerconnect API from MoneyGram — 1 operation(s) for partnerconnect.
  name: MoneyGram Partnerconnect API
  slug: moneygram-partnerconnect-api
- baseURL: https://sandboxapi.moneygram.com
  baseurl_source: declared
  description: The Reference Data API from MoneyGram — 2 operation(s) for reference data.
  name: MoneyGram Reference Data API
  slug: moneygram-reference-data-api
- baseURL: https://sandboxapi.moneygram.com
  baseurl_source: declared
  description: The Transactions API from MoneyGram — 1 operation(s) for transactions.
  name: MoneyGram Transactions API
  slug: moneygram-transactions-api
- baseURL: https://sandboxapi.moneygram.com
  baseurl_source: declared
  description: The Transfer API from MoneyGram — 3 operation(s) for transfer.
  name: MoneyGram Transfer API
  slug: moneygram-transfer-api
- baseURL: https://sandboxapi.moneygram.com
  baseurl_source: declared
  description: The Transfers API from MoneyGram — 1 operation(s) for transfers.
  name: MoneyGram Transfers API
  slug: moneygram-transfers-api
artifact_total: 19
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moneygram/refs/heads/main/rules/moneygram-rules.yml
  title: ''
  type: Spectral
  url: rules/moneygram-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moneygram/refs/heads/main/json-ld/moneygram-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/moneygram-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moneygram/refs/heads/main/vocabulary/moneygram-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/moneygram-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moneygram/refs/heads/main/data-model/moneygram-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moneygram-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moneygram/refs/heads/main/authentication/moneygram-authentication.yml
  title: ''
  type: Authentication
  url: authentication/moneygram-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/moneygram/refs/heads/main/lifecycle/moneygram-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/moneygram-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moneygram/refs/heads/main/lifecycle/moneygram-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/moneygram-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moneygram/refs/heads/main/conformance/moneygram-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moneygram-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moneygram/refs/heads/main/well-known/moneygram-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/moneygram-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moneygram/refs/heads/main/hosts/moneygram-hosts.yml
  title: ''
  type: Hosts
  url: hosts/moneygram-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moneygram/refs/heads/main/vendors/moneygram-vendors.yml
  title: ''
  type: Vendors
  url: vendors/moneygram-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.moneygram.com/
- group: company
  title: ''
  type: Newsroom
  url: https://corporate.moneygram.com/news
- group: start
  title: ''
  type: Login
  url: https://www.moneygram.com/gb/en/log-in
- group: other
  title: ''
  type: Leadership
  url: https://corporate.moneygram.com/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moneygram/refs/heads/main/security/moneygram-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moneygram-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.moneygram.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.moneygram.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.moneygram.com/moneygram-developer/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.moneygram.com/moneygram-developer/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.moneygram.com/moneygram-developer/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.moneygram.com/us/en/help-center
- group: company
  title: ''
  type: Blog
  url: https://www.moneygram.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moneygram.com/us/en/help-center/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moneygram.com/us/en/privacy-center
coverage:
  checked: '2026-10-15'
  detail: Developer portal pages render only via JavaScript, no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://www.moneygram.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: MoneyGram is a global money transfer and payment services company, enabling individuals and businesses to send and receive funds across more than 200 countries and territories. Founded in 1940, MoneyGram offers online, in‑app, and in‑person transfer options, with a network of agents and retail locations worldwide. The platform emphasizes security, competitive exchange rates, and multiple payout methods, including bank deposits, cash pickup, and digital wallets.
image: https://images.ctfassets.net/toryt1tt0roy/7MomRYb1LV2WMrv0u49W3u/78ea6116322787a764201f68e3802091/MoneyGram_Social_Share_Glyph_New.png
json_schemas:
- name: GetOauthOauthidResponse
  property_count: 14
  slug: moneygram-get-oauth-oauthid-response
- name: GetReferenceDataV1V1IdResponse
  property_count: 11
  slug: moneygram-get-reference-data-v1-v1-id-response
- name: PostV1AccountsValidateRequest
  property_count: 14
  slug: moneygram-post-v1-accounts-validate-request
- name: PostV1AccountsValidateResponse
  property_count: 9
  slug: moneygram-post-v1-accounts-validate-response
- name: PostV1TransfersRequest
  property_count: 16
  slug: moneygram-post-v1-transfers-request
- name: PutTransactionsMgitransactionidStatusRequest
  property_count: 3
  slug: moneygram-put-transactions-mgitransactionid-status-request
jsonld:
- class_count: 11
  name: Moneygram Context
  property_count: 70
  slug: moneygram-context
layout: provider
modified: '2026-10-14'
name: MoneyGram
nav: Providers
network: true
overview: 'MoneyGram is listed with 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Amend API, Fx Rate API, and 6 more. Tagged areas include Money, Payments, Transfer, Fintech, and Global.


  The MoneyGram catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MoneyGram''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 19 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: MoneyGram API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: moneygram-rules
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 65.0
    catalog_earned_first_party: 0.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 19.7
    contract_quality: 25.6
    developer_ergonomics: 57.1
    discoverability: 75.0
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Moneygram Authentication
  slug: moneygram-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Moneygram Domain Security
  slug: moneygram-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moneygram
tags:
- Money
- Payments
- Transfer
- Fintech
- Global
website: https://www.moneygram.com
---
