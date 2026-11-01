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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: APIs for shipping, tracking, address validation and e‑commerce services as documented on the Bring developer portal.
  name: Bring API
  slug: bring-api-2
- baseURL: http://api.bring.com
  baseurl_source: declared
  description: 'Bring API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Bring API
  slug: bring-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/bring/rules/bring-rules.yml
  title: ''
  type: Spectral
  url: rules/bring-rules.yml
- group: design
  href: https://artifacts.apis.io/bring/json-ld/bring-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bring-context.jsonld
- group: design
  href: https://artifacts.apis.io/bring/vocabulary/bring-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bring-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bring/data-model/bring-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bring-data-model.yml
- group: auth
  href: https://artifacts.apis.io/bring/security/bring-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bring-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bring/authentication/bring-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bring-authentication.yml
- group: design
  href: https://artifacts.apis.io/bring/conformance/bring-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bring-conformance.yml
- group: auth
  href: https://artifacts.apis.io/bring/well-known/bring-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bring-security.txt
- group: auth
  href: https://artifacts.apis.io/bring/well-known/bring-bring-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bring-bring-security.txt
- group: auth
  href: https://artifacts.apis.io/bring/well-known/bring-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bring-api-security.txt
- group: agent
  href: https://artifacts.apis.io/bring/well-known/bring-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bring-well-known.yml
- group: other
  href: https://artifacts.apis.io/bring/hosts/bring-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bring-hosts.yml
- group: other
  href: https://artifacts.apis.io/bring/vendors/bring-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bring-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.bring.com/resources/mybring/register-your-company
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bring
- group: auth
  href: https://artifacts.apis.io/bring/security/bring-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bring-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bring/security/bring-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bring-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bring.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bring.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.bring.com/api/
- group: operate
  title: ''
  type: Support
  url: https://www.bring.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bring.com/privacy-policy
coverage:
  checked: '2026-10-27'
  detail: Developer portal pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://developer.bring.com/api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Bring is a Norwegian logistics company offering parcel, e‑commerce and shipping services across the Nordics. It provides a comprehensive set of APIs for developers to integrate shipping, tracking, address validation, customs handling, and e‑commerce checkout solutions. The APIs are documented on a dedicated developer portal and cover services such as Shipping Guide, Pickup Point, Address, Postal Code, Booking, Bulk Split, Customer Info, Customs, Tracking, Warehousing and more, enabling businesses to automate logistics and improve customer experience.
json_schemas:
- name: GetApiPickupOptionsResponse
  property_count: 7
  slug: bring-get-api-pickup-options-response
- name: GetPickupApiPickupOptionsResponse
  property_count: 7
  slug: bring-get-pickup-api-pickup-options-response
- name: PostApiCreateRequest
  property_count: 15
  slug: bring-post-api-create-request
- name: PostApiCreateResponse
  property_count: 5
  slug: bring-post-api-create-response
- name: PostPickupApiCreateRequest
  property_count: 15
  slug: bring-post-pickup-api-create-request
- name: PostPickupApiCreateResponse
  property_count: 5
  slug: bring-post-pickup-api-create-response
jsonld:
- class_count: 25
  name: Bring Context
  property_count: 40
  slug: bring-context
layout: provider
modified: '2026-10-27'
name: Bring
nav: Providers
network: true
overview: 'Bring is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Shipping, E‑commerce, API, and Norway.


  The Bring catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bring''s developer surface includes authentication, signup flow, documentation, getting-started guide, support, and 17 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Bring API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: bring-rules
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 38.1
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bring Authentication
  slug: bring-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Bring Domain Security
  slug: bring-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bring Vulnerability Disclosure
  slug: bring-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bring
tags:
- Logistics
- Shipping
- E‑commerce
- API
- Norway
website: https://bring.com/
---
