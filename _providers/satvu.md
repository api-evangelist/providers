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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.satellitevu.com
  baseurl_source: declared
  description: 'SatVu API as documented publicly: 42 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: SatVu API
  slug: satvu-api
artifact_total: 11
asyncapis:
- description: ''
  name: Satvu Webhooks
  slug: satvu-webhooks
common:
- group: design
  href: https://artifacts.apis.io/satvu/rules/satvu-rules.yml
  title: ''
  type: Spectral
  url: rules/satvu-rules.yml
- group: design
  href: https://artifacts.apis.io/satvu/json-ld/satvu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/satvu-context.jsonld
- group: design
  href: https://artifacts.apis.io/satvu/vocabulary/satvu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/satvu-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/satvu/asyncapi/satvu-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/satvu-webhooks.yml
- group: design
  href: https://artifacts.apis.io/satvu/data-model/satvu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/satvu-data-model.yml
- group: design
  href: https://artifacts.apis.io/satvu/conformance/satvu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/satvu-conformance.yml
- group: other
  href: https://artifacts.apis.io/satvu/hosts/satvu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/satvu-hosts.yml
- group: other
  href: https://artifacts.apis.io/satvu/vendors/satvu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/satvu-vendors.yml
- group: build
  href: https://artifacts.apis.io/satvu/packages/satvu-packages.yml
  title: ''
  type: SDKs
  url: packages/satvu-packages.yml
- group: build
  href: https://artifacts.apis.io/satvu/packages/satvu-packages.yml
  title: ''
  type: Packages
  url: packages/satvu-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.satellitevu.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.satellitevu.com/insights/press
- group: company
  title: ''
  type: Blog
  url: https://www.satellitevu.com/insights/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.satellitevu.com/developers/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.satellitevu.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SatelliteVu
- group: auth
  href: https://artifacts.apis.io/satvu/security/satvu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/satvu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.satellitevu.com
coverage:
  checked: '2026-10-21'
  detail: The website provides only static HTML with no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.satellitevu.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: SatVu supplies high‑resolution (up to 3.5 m) thermal infrared imagery captured from its satellite constellation. The data can be delivered as still images or video up to 60 seconds and is marketed for use in national security, economic monitoring and climate‑resilience applications, including urban heat monitoring and activity detection inside structures day or night.
image: https://cdn.prod.website-files.com/664e1cfdaf0f190ac9bb6e1e/66ec4c58732e9d9d26af1114_SatVu-Open-Graph-Image.png
json_schemas:
- name: PostContractidTaskingSeriesResponse
  property_count: 7
  slug: satvu-post-contractid-tasking-series-response
- name: PostOtmV2ContractIdTaskingFeasibilitiesResponse
  property_count: 6
  slug: satvu-post-otm-v2-contract-id-tasking-feasibilities-response
- name: PostOtmV2ContractIdTaskingOrdersRequest
  property_count: 3
  slug: satvu-post-otm-v2-contract-id-tasking-orders-request
- name: PostOtmV2ContractIdTaskingSeriesPriceRequest
  property_count: 3
  slug: satvu-post-otm-v2-contract-id-tasking-series-price-request
- name: PostOtmV2ContractIdTaskingSeriesRequest
  property_count: 3
  slug: satvu-post-otm-v2-contract-id-tasking-series-request
- name: PostPolicyV1ContractsResponse
  property_count: 9
  slug: satvu-post-policy-v1-contracts-response
jsonld:
- class_count: 24
  name: Satvu Context
  property_count: 27
  slug: satvu-context
layout: provider
modified: '2026-10-21'
name: SatVu
nav: Providers
network: true
overview: 'SatVu is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Thermal imagery, Satellite data, National security, Economic monitoring, and Climate resilience.


  The SatVu catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  SatVu''s developer surface includes engineering blog, getting-started guide, API reference, and 15 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: SatVu API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: satvu-rules
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 36.1
    developer_ergonomics: 28.6
    discoverability: 67.9
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Satvu Domain Security
  slug: satvu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: satvu
tags:
- Thermal imagery
- Satellite data
- National security
- Economic monitoring
- Climate resilience
website: https://www.satellitevu.com
---
