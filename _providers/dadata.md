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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-10-31'
api_count: 4
apis:
- description: Поиск адреса от региона до дома или по индексу. Поиск компаний по ИНН, адресу и руководителю. Подбор банков, ФИО и email.
  name: DaData API
  slug: dadata-api
- baseURL: https://suggestions.dadata.ru
  baseurl_source: declared
  description: 'DaData API-методы API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: DaData API-методы API
  slug: clean-api
- baseURL: https://suggestions.dadata.ru
  baseurl_source: declared
  description: 'DaData core API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: DaData core API
  slug: core-api
- baseURL: https://suggestions.dadata.ru
  baseurl_source: declared
  description: 'DaData API-методы API as documented publicly: 35 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: DaData API-методы API
  slug: suggest-api
artifact_total: 23
common:
- group: design
  href: https://artifacts.apis.io/dadata/rules/dadata-rules.yml
  title: ''
  type: Spectral
  url: rules/dadata-rules.yml
- group: design
  href: https://artifacts.apis.io/dadata/json-ld/dadata-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dadata-context.jsonld
- group: design
  href: https://artifacts.apis.io/dadata/vocabulary/dadata-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dadata-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dadata/data-model/dadata-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dadata-data-model.yml
- group: auth
  href: https://artifacts.apis.io/dadata/authentication/dadata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dadata-authentication.yml
- group: design
  href: https://artifacts.apis.io/dadata/conformance/dadata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dadata-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dadata/llms/dadata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dadata-llms.txt
- group: other
  href: https://artifacts.apis.io/dadata/hosts/dadata-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dadata-hosts.yml
- group: other
  href: https://artifacts.apis.io/dadata/vendors/dadata-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dadata-vendors.yml
- group: build
  href: https://artifacts.apis.io/dadata/packages/dadata-packages.yml
  title: ''
  type: SDKs
  url: packages/dadata-packages.yml
- group: build
  href: https://artifacts.apis.io/dadata/packages/dadata-packages.yml
  title: ''
  type: Packages
  url: packages/dadata-packages.yml
- group: auth
  href: https://artifacts.apis.io/dadata/security/dadata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dadata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dadata.ru/
- group: docs
  title: ''
  type: Documentation
  url: https://dadata.ru/api/
- group: docs
  title: ''
  type: APIReference
  url: https://dadata.ru/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://dadata.ru/api/
- group: operate
  title: ''
  type: Support
  url: https://dadata.ru/support/
- group: company
  title: ''
  type: Blog
  url: https://dadata.ru/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://dadata.ru/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dadata.ru/offer/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dadata.ru/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dadata.ru/
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are HTML/SPA and no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract is published.
  evidence:
  - status: 200
    url: https://dadata.ru/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: DaData provides a suite of APIs for data validation, standardization, and enrichment, primarily targeting Russian business data. Its services include address standardization, company information lookup by INN/KPP/OGRN, phone and email validation, bank data retrieval, and document extraction. The platform offers both free and paid tiers, supporting developers in building reliable data pipelines for CRM, e‑commerce, and analytics applications. By leveraging DaData, businesses can reduce errors, improve data quality, and accelerate onboarding processes.
image: https://dadata.ru/img/covers/dadata.ru.png
json_schemas:
- name: PostSuggestionsApi41RsFindaffiliatedPartyRequest
  property_count: 1
  slug: dadata-post-suggestions-api41-rs-findaffiliated-party-request
- name: PostSuggestionsApi41RsFindbyemailCompanyRequest
  property_count: 1
  slug: dadata-post-suggestions-api41-rs-findbyemail-company-request
- name: PostSuggestionsApi41RsFindbyidAddressRequest
  property_count: 1
  slug: dadata-post-suggestions-api41-rs-findbyid-address-request
- name: PostSuggestionsApi41RsFindbyidCarBrandRequest
  property_count: 1
  slug: dadata-post-suggestions-api41-rs-findbyid-car-brand-request
- name: PostSuggestionsApi41RsFindbyidCountryRequest
  property_count: 1
  slug: dadata-post-suggestions-api41-rs-findbyid-country-request
- name: PostSuggestionsApi41RsFindbyidCourtRequest
  property_count: 1
  slug: dadata-post-suggestions-api41-rs-findbyid-court-request
- name: PostSuggestionsApi41RsFindbyidCurrencyRequest
  property_count: 1
  slug: dadata-post-suggestions-api41-rs-findbyid-currency-request
- name: PostSuggestionsApi41RsFindbyidFnsUnitRequest
  property_count: 1
  slug: dadata-post-suggestions-api41-rs-findbyid-fns-unit-request
- name: PostSuggestionsApi41RsGeolocateAddressRequest
  property_count: 2
  slug: dadata-post-suggestions-api41-rs-geolocate-address-request
- name: PostSuggestionsApi41RsGeolocatePostalUnitRequest
  property_count: 3
  slug: dadata-post-suggestions-api41-rs-geolocate-postal-unit-request
- name: PostSuggestionsApi41RsIplocateAddressRequest
  property_count: 3
  slug: dadata-post-suggestions-api41-rs-iplocate-address-request
- name: PostSuggestionsApi41RsIplocateAddressResponse
  property_count: 21
  slug: dadata-post-suggestions-api41-rs-iplocate-address-response
jsonld:
- class_count: 44
  name: Dadata Context
  property_count: 28
  slug: dadata-context
layout: provider
modified: '2026-10-28'
name: DaData
nav: Providers
network: true
overview: 'DaData is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including API-методы API, core API, and 2 more. Tagged areas include Data, API, Russian, DataEnrichment, and AddressStandardization.


  The DaData catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DaData''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Dadata Plans Pricing
  plan_count: 0
  slug: dadata-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Dadata Rate Limits
  slug: dadata-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: DaData API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: dadata-rules
scopes:
- name: Dadata Scopes
  scope_count: 0
  slug: dadata-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 65.0
    catalog_earned_first_party: 0.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 19.7
    contract_quality: 25.3
    developer_ergonomics: 54.8
    discoverability: 71.4
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dadata Authentication
  slug: dadata-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dadata Domain Security
  slug: dadata-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dadata
tags:
- Data
- API
- Russian
- DataEnrichment
- AddressStandardization
website: https://dadata.ru/
---
