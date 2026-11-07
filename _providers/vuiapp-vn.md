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
    auth_clarity: bearer
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://auth.sandbox.vuiapp.vn
  baseurl_source: declared
  description: 'Nano API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-23); not the provider''s own document.'
  name: Nano API
  slug: vuiapp-vn-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/vuiapp-vn/vendors/vuiapp-vn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vuiapp-vn-vendors.yml
- group: design
  href: https://artifacts.apis.io/vuiapp-vn/rules/vuiapp-vn-rules.yml
  title: ''
  type: Spectral
  url: rules/vuiapp-vn-rules.yml
- group: design
  href: https://artifacts.apis.io/vuiapp-vn/json-ld/vuiapp-vn-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vuiapp-vn-context.jsonld
- group: design
  href: https://artifacts.apis.io/vuiapp-vn/vocabulary/vuiapp-vn-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vuiapp-vn-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/vuiapp-vn/data-model/vuiapp-vn-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vuiapp-vn-data-model.yml
- group: design
  href: https://artifacts.apis.io/vuiapp-vn/conformance/vuiapp-vn-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vuiapp-vn-conformance.yml
- group: other
  href: https://artifacts.apis.io/vuiapp-vn/hosts/vuiapp-vn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vuiapp-vn-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: http://vuiapp.vn/privacy-policy
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/Redocly/redoc
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.vuiapp.vn/
- group: auth
  href: https://artifacts.apis.io/vuiapp-vn/security/vuiapp-vn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vuiapp-vn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vuiapp.vn/
created: '2026-10-23'
description: 'Nano is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by partech) and added to the network as a stub for full-pipeline profiling.'
image: http://cdn.vuiapp.vn/cdn/ff/b33XxXb7d4av7xzy5GQQGJHZR6Mm4js7QrWgMHqdVf8/1722190048/public/2021-12/Nguye%CC%82%CC%83n%20Hoa%CC%80ng%20Ye%CC%82%CC%81n%2C%201999%2C%20nha%CC%82n%20vie%CC%82n%20ba%CC%81n%20ha%CC%80ng.jpg
json_schemas:
- name: GetV1AdvancesResponse
  property_count: 2
  slug: vuiapp-vn-get-v1-advances-response
- name: PostAuthRealmsVuiappProtocolOpenidConnectTokenResponse
  property_count: 2
  slug: vuiapp-vn-post-auth-realms-vuiapp-protocol-openid-connect-token-response
jsonld:
- class_count: 2
  name: Vuiapp Vn Context
  property_count: 2
  slug: vuiapp-vn-context
layout: provider
modified: '2026-10-23'
name: Nano
nav: Providers
network: true
overview: 'Nano is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Nano catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Nano''s developer surface includes API reference, documentation, and 10 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Nano API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: vuiapp-vn-rules
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 68.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 22.1
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/vuiapp-vn/vuiapp-vn-2026-11-03T145941.png
security:
- kind: domain-security
  name: Vuiapp Vn Domain Security
  slug: vuiapp-vn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vuiapp-vn
tags:
- Company
website: https://vuiapp.vn/
---
