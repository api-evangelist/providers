---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API details listed on the Intelsat Developer Portal
  name: Intelsat API
  slug: intelsat-api-2
- description: The Alarms API from Intelsat — 1 operation(s) for alarms.
  name: Intelsat Alarms API
  slug: intelsat-alarms-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Blog
  url: https://www.ses.com/insights
- group: design
  href: https://artifacts.apis.io/intelsat/rules/intelsat-rules.yml
  title: ''
  type: Spectral
  url: rules/intelsat-rules.yml
- group: design
  href: https://artifacts.apis.io/intelsat/json-ld/intelsat-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/intelsat-context.jsonld
- group: design
  href: https://artifacts.apis.io/intelsat/vocabulary/intelsat-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/intelsat-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/intelsat/data-model/intelsat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/intelsat-data-model.yml
- group: design
  href: https://artifacts.apis.io/intelsat/conformance/intelsat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/intelsat-conformance.yml
- group: other
  href: https://artifacts.apis.io/intelsat/hosts/intelsat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/intelsat-hosts.yml
- group: other
  href: https://artifacts.apis.io/intelsat/vendors/intelsat-vendors.yml
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
  href: https://artifacts.apis.io/intelsat/security/intelsat-domain-security.yml
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
modified: '2026-10-06'
name: Intelsat
nav: Providers
network: true
overview: 'Intelsat is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Alarms API, and 1 more. Tagged areas include Satellite, Communications, Connectivity, Enterprise, and Media.


  The Intelsat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Intelsat''s developer surface includes engineering blog, documentation, and 13 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 52
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
  composite: 20.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 51.2
    catalog_earned_first_party: 0.0
    catalog_gap: 48.9
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 28.6
    contract_governance: 22.0
    contract_quality: 18.5
    developer_ergonomics: 7.1
    discoverability: 58.0
    operational_transparency: 5.3
  previous_composite: 28.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/intelsat/intelsat-2026-10-11T105807.png
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
