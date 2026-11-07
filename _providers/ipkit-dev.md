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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'IPKit API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: IPKit API
  slug: ipkit-dev-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/ipkit-dev/rules/ipkit-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/ipkit-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/ipkit-dev/json-ld/ipkit-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ipkit-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/ipkit-dev/vocabulary/ipkit-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ipkit-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ipkit-dev/data-model/ipkit-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ipkit-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/ipkit-dev/conformance/ipkit-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ipkit-dev-conformance.yml
- group: other
  href: https://artifacts.apis.io/ipkit-dev/hosts/ipkit-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ipkit-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/ipkit-dev/vendors/ipkit-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ipkit-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ipkit-dev/security/ipkit-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ipkit-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ipkit.dev
- group: docs
  title: ''
  type: APIReference
  url: https://ipkit.dev
created: '2026-10-22'
description: IPKit provides a simple API to retrieve IP address information. The service returns JSON data about the queried IP, including geolocation, ISP, and security details, wrapping data from the ipregistry service. It is designed for developers needing quick IP lookups without authentication, supporting public access via the root endpoint. IPKit aims to offer reliable, low-latency IP data for integration into applications, analytics, and security tools.
image: https://ipkit.dev/og.png
json_schemas:
- name: GetApiMyIpResponse
  property_count: 7
  slug: ipkit-dev-get-api-my-ip-response
- name: Get2001486048608888Response
  property_count: 7
  slug: ipkit-dev-get2001486048608888-response
- name: Get8888Response
  property_count: 7
  slug: ipkit-dev-get8888-response
jsonld:
- class_count: 3
  name: Ipkit Dev Context
  property_count: 6
  slug: ipkit-dev-context
layout: provider
modified: '2026-10-22'
name: IPKit
nav: Providers
network: true
overview: 'IPKit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IP, Geolocation, and Data.


  The IPKit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  IPKit''s developer surface includes API reference and 9 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: IPKit API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: ipkit-dev-rules
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 53.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.8
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
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/ipkit-dev/ipkit-dev-2026-11-03T134023.png
security:
- kind: domain-security
  name: Ipkit Dev Domain Security
  slug: ipkit-dev-domain-security
  summary_line: TLSv1.3
slug: ipkit-dev
tags:
- Company
- IP
- Geolocation
- Data
website: https://ipkit.dev
---
