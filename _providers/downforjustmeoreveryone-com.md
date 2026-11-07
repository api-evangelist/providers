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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'downforjustmeoreveryone-com API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: downforjustmeoreveryone-com API
  slug: downforjustmeoreveryone-com-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/downforjustmeoreveryone-com/vendors/downforjustmeoreveryone-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/downforjustmeoreveryone-com-vendors.yml
- group: design
  href: https://artifacts.apis.io/downforjustmeoreveryone-com/rules/downforjustmeoreveryone-com-rules.yml
  title: ''
  type: Spectral
  url: rules/downforjustmeoreveryone-com-rules.yml
- group: design
  href: https://artifacts.apis.io/downforjustmeoreveryone-com/json-ld/downforjustmeoreveryone-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/downforjustmeoreveryone-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/downforjustmeoreveryone-com/vocabulary/downforjustmeoreveryone-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/downforjustmeoreveryone-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/downforjustmeoreveryone-com/data-model/downforjustmeoreveryone-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/downforjustmeoreveryone-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/downforjustmeoreveryone-com/conformance/downforjustmeoreveryone-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/downforjustmeoreveryone-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/downforjustmeoreveryone-com/hosts/downforjustmeoreveryone-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/downforjustmeoreveryone-com-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://downforjustmeoreveryone.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://downforjustmeoreveryone.com/postman.com/outages
- group: company
  title: ''
  type: Newsroom
  url: https://downforjustmeoreveryone.com/category/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://downforjustmeoreveryone.com/category/developer
- group: auth
  href: https://artifacts.apis.io/downforjustmeoreveryone-com/security/downforjustmeoreveryone-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/downforjustmeoreveryone-com-domain-security.yml
coverage:
  checked: '2026-11-06'
  detail: No machine‑readable API specification (OpenAPI/GraphQL/AsyncAPI) is published; the developer portal provides only human‑readable pages.
  evidence:
  - status: 200
    url: https://downforjustmeoreveryone.com/category/developer
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: 'downforjustmeoreveryone-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://downforjustmeoreveryone.com/og/home.png
json_schemas:
- name: GetApiCertResponse
  property_count: 2
  slug: downforjustmeoreveryone-com-get-api-cert-response
- name: GetMcpResponse
  property_count: 1
  slug: downforjustmeoreveryone-com-get-mcp-response
jsonld:
- class_count: 2
  name: Downforjustmeoreveryone Com Context
  property_count: 3
  slug: downforjustmeoreveryone-com-context
layout: provider
modified: '2026-11-05'
name: downforjustmeoreveryone-com
nav: Providers
network: true
overview: 'downforjustmeoreveryone-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Uptime Monitoring and Website Status.


  The downforjustmeoreveryone-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: downforjustmeoreveryone-com API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: downforjustmeoreveryone-com-rules
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 41.8
    catalog_earned_first_party: 0.0
    catalog_gap: 73.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 19.9
    developer_ergonomics: 14.3
    discoverability: 41.1
    operational_transparency: 0.0
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Downforjustmeoreveryone Com Domain Security
  slug: downforjustmeoreveryone-com-domain-security
  summary_line: TLSv1.3
slug: downforjustmeoreveryone-com
tags:
- Uptime Monitoring
- Website Status
website: https://downforjustmeoreveryone.com/category/developer
---
