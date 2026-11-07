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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Free public API providing static JSON files of Matter product catalog.
  name: MatterCatalog API
  slug: mattercatalog-api-2
- description: 'MatterCatalog API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: MatterCatalog API
  slug: mattercatalog-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/mattercatalog/rules/mattercatalog-rules.yml
  title: ''
  type: Spectral
  url: rules/mattercatalog-rules.yml
- group: design
  href: https://artifacts.apis.io/mattercatalog/json-ld/mattercatalog-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mattercatalog-context.jsonld
- group: design
  href: https://artifacts.apis.io/mattercatalog/vocabulary/mattercatalog-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mattercatalog-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mattercatalog/data-model/mattercatalog-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mattercatalog-data-model.yml
- group: operate
  href: https://artifacts.apis.io/mattercatalog/changelog/mattercatalog-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mattercatalog-changelog.yml
- group: design
  href: https://artifacts.apis.io/mattercatalog/conformance/mattercatalog-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mattercatalog-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mattercatalog/llms/mattercatalog-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mattercatalog-llms.txt
- group: other
  href: https://artifacts.apis.io/mattercatalog/hosts/mattercatalog-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mattercatalog-hosts.yml
- group: other
  href: https://artifacts.apis.io/mattercatalog/vendors/mattercatalog-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mattercatalog-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://mattercatalog.com/guides/matter-setup-code
- group: auth
  href: https://artifacts.apis.io/mattercatalog/security/mattercatalog-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mattercatalog-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mattercatalog.com
- group: docs
  title: ''
  type: Documentation
  url: https://mattercatalog.com/developers
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mattercatalog.com/developers
- group: operate
  title: ''
  type: Support
  url: https://mattercatalog.com/contact
- group: company
  title: ''
  type: Blog
  url: https://mattercatalog.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mattercatalog.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mattercatalog.com/privacy
coverage:
  checked: '2026-11-02'
  detail: Developer docs describe a free public API serving static JSON files, but no OpenAPI or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://mattercatalog.com/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: MatterCatalog is an independent US catalog of Matter smart home devices. It lists over 1,100 products sold in the United States, indicating each model’s CSA certification status, Thread or Wi‑Fi connectivity, and provides verified store links. The site also offers an affiliate disclosure and a free public API for accessing device data.
image: https://mattercatalog.com/og-image.jpg
json_schemas:
- name: GetApiProductsIdJsonResponse
  property_count: 20
  slug: mattercatalog-get-api-products-id-json-response
- name: GetApiProductsJsonResponse
  property_count: 2
  slug: mattercatalog-get-api-products-json-response
- name: GetApiStatsJsonResponse
  property_count: 1
  slug: mattercatalog-get-api-stats-json-response
jsonld:
- class_count: 3
  name: Mattercatalog Context
  property_count: 17
  slug: mattercatalog-context
layout: provider
modified: '2026-11-02'
name: MatterCatalog
nav: Providers
network: true
overview: 'MatterCatalog is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Matter, Smart Home, IoT, Certification, and Directory.


  The MatterCatalog catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MatterCatalog''s developer surface includes changelog, getting-started guide, documentation, support, engineering blog, and 13 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: MatterCatalog API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: mattercatalog-rules
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 21.3
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mattercatalog Domain Security
  slug: mattercatalog-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mattercatalog
tags:
- Matter
- Smart Home
- IoT
- Certification
- Directory
website: https://mattercatalog.com
---
