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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.deltastream.io/v2
  baseurl_source: declared
  description: 'DeltaStream API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-23); not the provider''s own document.'
  name: DeltaStream API
  slug: deltastream-api
artifact_total: 9
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.deltastream.io/getting-started/trial-quick-start
- group: design
  href: https://artifacts.apis.io/deltastream/rules/deltastream-rules.yml
  title: ''
  type: Spectral
  url: rules/deltastream-rules.yml
- group: design
  href: https://artifacts.apis.io/deltastream/json-ld/deltastream-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deltastream-context.jsonld
- group: design
  href: https://artifacts.apis.io/deltastream/vocabulary/deltastream-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deltastream-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/deltastream/data-model/deltastream-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deltastream-data-model.yml
- group: design
  href: https://artifacts.apis.io/deltastream/conformance/deltastream-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deltastream-conformance.yml
- group: agent
  href: https://artifacts.apis.io/deltastream/llms/deltastream-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deltastream-llms.txt
- group: agent
  href: https://artifacts.apis.io/deltastream/well-known/deltastream-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deltastream-well-known.yml
- group: other
  href: https://artifacts.apis.io/deltastream/hosts/deltastream-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deltastream-hosts.yml
- group: other
  href: https://artifacts.apis.io/deltastream/vendors/deltastream-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deltastream-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.deltastream.io/reference/metrics
- group: auth
  href: https://artifacts.apis.io/deltastream/security/deltastream-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deltastream-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.deltastream.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deltastream.io/
- group: operate
  title: ''
  type: Support
  url: https://www.deltastream.io/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.deltastream.io/blogs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deltastream.io/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.deltastream.io/security/
coverage:
  checked: '2026-10-23'
  detail: Docs are served via Gitbook which renders pages client‑side, no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://docs.deltastream.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: DeltaStream provides a real-time context engine for AI agents, enabling continuous data ingestion and processing to keep agents up-to-date every second. The platform offers data stores, materialized views, compute pools, and a REST API, supporting use cases across e‑commerce, fintech, cybersecurity, IoT, and manufacturing. It aims to simplify building autonomous agents that act on live data streams.
image: https://www.deltastream.io/wp-content/uploads/2026/01/ds-new-social-share.png
json_schemas:
- name: GetDownloadResourcetypeOrganizationidResourcenameResponse
  property_count: 7
  slug: deltastream-get-download-resourcetype-organizationid-resourcename-response
- name: GetStatementsStatementidResponse
  property_count: 8
  slug: deltastream-get-statements-statementid-response
- name: GetVersionResponse
  property_count: 4
  slug: deltastream-get-version-response
- name: PostStatementsRequest
  property_count: 2
  slug: deltastream-post-statements-request
- name: PostStatementsResponse
  property_count: 8
  slug: deltastream-post-statements-response
jsonld:
- class_count: 5
  name: Deltastream Context
  property_count: 2
  slug: deltastream-context
layout: provider
modified: '2026-10-22'
name: DeltaStream
nav: Providers
network: true
overview: 'DeltaStream is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Real-Time, Data Streaming, and Platform.


  The DeltaStream catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DeltaStream''s developer surface includes getting-started guide, API reference, documentation, support, engineering blog, and 13 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: DeltaStream API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: deltastream-rules
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 19.7
    contract_quality: 23.8
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deltastream Domain Security
  slug: deltastream-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: deltastream
tags:
- Company
- Artificial Intelligence
- Real-Time
- Data Streaming
- Platform
website: https://www.deltastream.io/
---
