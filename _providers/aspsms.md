---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 12.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://webapi.aspsms.com
  baseurl_source: declared
  description: 'ASPSMS API as documented publicly: 52 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: ASPSMS API
  slug: aspsms-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/aspsms/rules/aspsms-rules.yml
  title: ''
  type: Spectral
  url: rules/aspsms-rules.yml
- group: design
  href: https://artifacts.apis.io/aspsms/json-ld/aspsms-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aspsms-context.jsonld
- group: design
  href: https://artifacts.apis.io/aspsms/vocabulary/aspsms-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aspsms-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aspsms/data-model/aspsms-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aspsms-data-model.yml
- group: operate
  href: https://artifacts.apis.io/aspsms/changelog/aspsms-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aspsms-changelog.yml
- group: design
  href: https://artifacts.apis.io/aspsms/conformance/aspsms-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aspsms-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aspsms/llms/aspsms-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aspsms-llms.txt
- group: other
  href: https://artifacts.apis.io/aspsms/hosts/aspsms-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aspsms-hosts.yml
- group: build
  href: https://artifacts.apis.io/aspsms/packages/aspsms-packages.yml
  title: ''
  type: SDKs
  url: packages/aspsms-packages.yml
- group: build
  href: https://artifacts.apis.io/aspsms/packages/aspsms-packages.yml
  title: ''
  type: Packages
  url: packages/aspsms-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aspsms.com/en/privacy/
- group: start
  title: ''
  type: Login
  url: https://www.aspsms.com/en/login/
- group: auth
  href: https://artifacts.apis.io/aspsms/security/aspsms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aspsms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aspsms.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.aspsms.com/en/documentation/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aspsms.com/en/prices/
- group: company
  title: ''
  type: Blog
  url: https://www.aspsms.com/en/Blog/
- group: operate
  title: ''
  type: Support
  url: https://www.aspsms.com/en/support/
coverage:
  checked: '2026-10-26'
  detail: API documentation pages return 403 HTML blocks, preventing access to machine‑readable specs.
  evidence:
  - status: 403
    url: https://www.aspsms.com/en/json/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: ASPSMS provides a global SMS gateway service for businesses, offering multiple integration options including JSON REST, SOAP, HTTP POST, SMTP, and email‑to‑SMS. The platform supports two‑factor authentication, bulk messaging, and two‑way SMS, with no licence, setup, or monthly fees. Documentation, pricing, and developer resources are available in several languages, and the service includes a web portal for managing credits and messages.
json_schemas:
- name: PostAspsmsdeactivatependingsmswithtransactionreferencenumber
  property_count: 1
  slug: aspsms-post-aspsmsdeactivatependingsmswithtransactionreferencenumber
- name: PostAspsmsestimatecreditconsumptionRequest
  property_count: 1
  slug: aspsms-post-aspsmsestimatecreditconsumption-request
- name: PostAspsmssendsmsRequest
  property_count: 1
  slug: aspsms-post-aspsmssendsms-request
- name: PostMsisdndlrstatignorelistaddPostRequest
  property_count: 1
  slug: aspsms-post-msisdndlrstatignorelistadd-post-request
- name: PostMsisdndlrstatignorelistremovePostRequest
  property_count: 1
  slug: aspsms-post-msisdndlrstatignorelistremove-post-request
- name: PostPhonenumbersAddRequest
  property_count: 1
  slug: aspsms-post-phonenumbers-add-request
jsonld:
- class_count: 8
  name: Aspsms Context
  property_count: 6
  slug: aspsms-context
layout: provider
modified: '2026-10-26'
name: ASPSMS
nav: Providers
network: true
overview: 'ASPSMS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SMS, Messaging, API, Communications, and Business.


  The ASPSMS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ASPSMS''s developer surface includes changelog, documentation, pricing, engineering blog, support, and 13 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: ASPSMS API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: aspsms-rules
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 23.7
    developer_ergonomics: 23.8
    discoverability: 62.5
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 33
      marker_coverage: 100.0
      total: 33
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aspsms Domain Security
  slug: aspsms-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: aspsms
tags:
- SMS
- Messaging
- API
- Communications
- Business
website: https://www.aspsms.com/
---
