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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://lunchflow.app
  baseurl_source: declared
  description: 'Lunch Flow API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Lunch Flow API
  slug: lunch-flow-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/lunch-flow/plans/lunch-flow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lunch-flow-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/lunch-flow/rules/lunch-flow-rules.yml
  title: ''
  type: Spectral
  url: rules/lunch-flow-rules.yml
- group: design
  href: https://artifacts.apis.io/lunch-flow/json-ld/lunch-flow-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lunch-flow-context.jsonld
- group: design
  href: https://artifacts.apis.io/lunch-flow/vocabulary/lunch-flow-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lunch-flow-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/lunch-flow/data-model/lunch-flow-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lunch-flow-data-model.yml
- group: auth
  href: https://artifacts.apis.io/lunch-flow/authentication/lunch-flow-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lunch-flow-authentication.yml
- group: design
  href: https://artifacts.apis.io/lunch-flow/conformance/lunch-flow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lunch-flow-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lunch-flow/llms/lunch-flow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lunch-flow-llms.txt
- group: agent
  href: https://artifacts.apis.io/lunch-flow/well-known/lunch-flow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lunch-flow-well-known.yml
- group: other
  href: https://artifacts.apis.io/lunch-flow/hosts/lunch-flow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lunch-flow-hosts.yml
- group: other
  href: https://artifacts.apis.io/lunch-flow/vendors/lunch-flow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lunch-flow-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.lunchflow.app/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lunchflow
- group: auth
  href: https://artifacts.apis.io/lunch-flow/security/lunch-flow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lunch-flow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lunchflow.app/
- group: docs
  title: ''
  type: Documentation
  url: https://www.lunchflow.app/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.lunchflow.app/docs/api/platform-api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.lunchflow.app/docs/guides/get-started/welcome
- group: operate
  title: ''
  type: Support
  url: https://www.lunchflow.app/docs/guides/account/security-privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lunchflow.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lunchflow.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lunchflow.app/privacy
coverage:
  checked: '2026-10-27'
  detail: Documentation pages are rendered via JavaScript and provide no machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.lunchflow.app/docs/guides/get-started/welcome
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Lunch Flow provides a unified API platform that connects bank accounts, investment accounts, and financial data across 30+ countries. It enables developers to embed financial data into their applications, offering personal and platform APIs for account transactions, balances, holdings, and user management. The service supports OAuth, Basic Auth, and detailed raw data access, targeting fintech integrations, budgeting tools, and investment tracking solutions.
json_schemas:
- name: GetApiPlatformV1AccountsStringBalanceResponse
  property_count: 1
  slug: lunch-flow-get-api-platform-v1-accounts-string-balance-response
- name: GetApiPlatformV1AccountsStringHoldingsResponse
  property_count: 3
  slug: lunch-flow-get-api-platform-v1-accounts-string-holdings-response
- name: GetApiV1AccountsStringHoldingsResponse
  property_count: 3
  slug: lunch-flow-get-api-v1-accounts-string-holdings-response
- name: PostApiPlatformOauthTokenRequest
  property_count: 4
  slug: lunch-flow-post-api-platform-oauth-token-request
- name: PutApiPlatformV1UsersStringRequest
  property_count: 1
  slug: lunch-flow-put-api-platform-v1-users-string-request
- name: PutApiPlatformV1UsersStringResponse
  property_count: 1
  slug: lunch-flow-put-api-platform-v1-users-string-response
jsonld:
- class_count: 8
  name: Lunch Flow Context
  property_count: 11
  slug: lunch-flow-context
layout: provider
modified: '2026-10-27'
name: Lunch Flow
nav: Providers
network: true
overview: 'Lunch Flow is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, API, Banking, Integration, and OpenAPI.


  The Lunch Flow catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lunch Flow''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, pricing, and 15 more developer resources.'
plans:
- name: Lunch Flow Plans Pricing
  plan_count: 6
  slug: lunch-flow-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Lunch Flow API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: lunch-flow-rules
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 26.2
    developer_ergonomics: 45.2
    discoverability: 62.5
    operational_transparency: 21.1
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
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 19.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Lunch Flow Authentication
  slug: lunch-flow-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Lunch Flow Domain Security
  slug: lunch-flow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lunch-flow
tags:
- Fintech
- API
- Banking
- Integration
- OpenAPI
- Developer
website: https://www.lunchflow.app/
---
