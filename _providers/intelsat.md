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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-09-25'
api_count: 2
apis:
- description: API details listed on the Intelsat Developer Portal
  name: Intelsat API
  slug: intelsat-api-2
- description: 'Intelsat API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-09-22); not the provider''s own document.'
  name: Intelsat API
  slug: intelsat-api
artifact_total: 6
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intelsat/refs/heads/main/rules/intelsat-rules.yml
  title: ''
  type: Spectral
  url: rules/intelsat-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intelsat/refs/heads/main/json-ld/intelsat-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/intelsat-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intelsat/refs/heads/main/vocabulary/intelsat-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/intelsat-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intelsat/refs/heads/main/data-model/intelsat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/intelsat-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intelsat/refs/heads/main/conformance/intelsat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/intelsat-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/intelsat/refs/heads/main/hosts/intelsat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/intelsat-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/intelsat/refs/heads/main/vendors/intelsat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/intelsat-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ses.com/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://www.ses.com/network-and-technology/technology-enablers/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ses.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.ses.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://developer.intelsat.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/intelsat/refs/heads/main/security/intelsat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intelsat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://intelsat.com/
coverage:
  checked: 2026-09-22
  detail: Developer portal pages are rendered via JavaScript and return no machine‑readable OpenAPI spec.
  evidence:
  - status: 404
    url: https://developer.intelsat.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-22'
description: Intelsat, now part of SES, is a leading satellite operator providing global communications services. It offers a portfolio of satellite capacity, managed services, and connectivity solutions across aviation, government, enterprise, and media sectors. The company leverages a fleet of geostationary and medium Earth orbit satellites to deliver reliable, high‑throughput connectivity worldwide, supporting critical applications such as broadband internet, broadcast, and IoT.
image: https://www.ses.com/social-share-default.jpg
json_schemas:
- name: GetApiAlarmsResponse
  property_count: 10
  slug: intelsat-get-api-alarms-response
jsonld:
- class_count: 1
  name: Intelsat Context
  property_count: 10
  slug: intelsat-context
layout: provider
modified: '2026-09-22'
name: Intelsat
nav: Providers
network: true
overview: 'Intelsat publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Satellite, Communications, Connectivity, Enterprise, and Media.


  The Intelsat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Intelsat''s developer surface includes documentation and 13 more developer resources.'
random_paper: 10
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Intelsat API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: intelsat-rules
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 51.2
    catalog_earned_first_party: 0.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 18.5
    developer_ergonomics: 9.5
    discoverability: 58.9
    operational_transparency: 10.5
  previous_composite: 20.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Intelsat Domain Security
  slug: intelsat-domain-security
  summary_line: TLSv1.3 · DMARC
slug: intelsat
tags:
- Satellite
- Communications
- Connectivity
- Enterprise
- Media
website: https://intelsat.com/
---
