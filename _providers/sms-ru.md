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
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: ''
  name: SMS.ru API
  slug: sms-ru-api-2
- description: 'SMS.ru API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: SMS.ru API
  slug: sms-ru-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/sms-ru/rules/sms-ru-rules.yml
  title: ''
  type: Spectral
  url: rules/sms-ru-rules.yml
- group: design
  href: https://artifacts.apis.io/sms-ru/json-ld/sms-ru-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sms-ru-context.jsonld
- group: design
  href: https://artifacts.apis.io/sms-ru/vocabulary/sms-ru-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sms-ru-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/sms-ru/data-model/sms-ru-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sms-ru-data-model.yml
- group: design
  href: https://artifacts.apis.io/sms-ru/conformance/sms-ru-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sms-ru-conformance.yml
- group: other
  href: https://artifacts.apis.io/sms-ru/hosts/sms-ru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sms-ru-hosts.yml
- group: auth
  href: https://artifacts.apis.io/sms-ru/security/sms-ru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sms-ru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sms.ru/
- group: docs
  title: ''
  type: Documentation
  url: https://sms.ru/docs
- group: docs
  title: ''
  type: APIReference
  url: https://sms.ru/api
- group: commercial
  title: ''
  type: Pricing
  url: https://sms.ru/price
- group: operate
  title: ''
  type: Support
  url: https://sms.ru/contacts
- group: company
  title: ''
  type: Blog
  url: https://sms.ru/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sms.ru/oferta
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sms.ru/
coverage:
  checked: '2026-10-28'
  detail: API documentation is HTML only and does not provide a machine‑readable OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 200
    url: https://sms.ru/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: SMS.ru provides a mass SMS sending service across Russia, offering a personal account and an HTTP/SMTP API for sending SMS messages. Users can launch campaigns within 15 minutes, view transparent operator‑based pricing, and register an alphanumeric sender name. The platform supports bulk messaging, authentication via calls, balance checks, and cost estimation, catering to businesses needing reliable communication.
image: https://sms.ru/i/logo-blue-big.png
json_schemas:
- name: GetCallbackGetResponse
  property_count: 3
  slug: sms-ru-get-callback-get-response
- name: GetMyLimitResponse
  property_count: 4
  slug: sms-ru-get-my-limit-response
- name: GetSmsCostResponse
  property_count: 5
  slug: sms-ru-get-sms-cost-response
- name: GetSmsSendResponse
  property_count: 4
  slug: sms-ru-get-sms-send-response
- name: GetSmsStatusResponse
  property_count: 4
  slug: sms-ru-get-sms-status-response
- name: GetStoplistGetResponse
  property_count: 3
  slug: sms-ru-get-stoplist-get-response
jsonld:
- class_count: 10
  name: Sms Ru Context
  property_count: 10
  slug: sms-ru-context
layout: provider
modified: '2026-10-28'
name: SMS.ru
nav: Providers
network: true
overview: 'SMS.ru is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SMS, Messaging, API, and Russia.


  The SMS.ru catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SMS.ru''s developer surface includes documentation, API reference, pricing, support, engineering blog, and 10 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 0
  name: Sms Ru Rate Limits
  slug: sms-ru-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: SMS.ru API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: sms-ru-rules
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 23.8
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 15.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sms Ru Domain Security
  slug: sms-ru-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sms-ru
tags:
- Company
- SMS
- Messaging
- API
- Russia
website: https://sms.ru/
---
