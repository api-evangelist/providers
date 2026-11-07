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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Stainless API as documented publicly: 24 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Stainless API
  slug: stainlessapi-com-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/stainlessapi-com/well-known/stainlessapi-com-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stainlessapi-com-www-security.txt
- group: design
  href: https://artifacts.apis.io/stainlessapi-com/rules/stainlessapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/stainlessapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/stainlessapi-com/json-ld/stainlessapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/stainlessapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/stainlessapi-com/vocabulary/stainlessapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/stainlessapi-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/stainlessapi-com/data-model/stainlessapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stainlessapi-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/stainlessapi-com/conformance/stainlessapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stainlessapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/stainlessapi-com/well-known/stainlessapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stainlessapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/stainlessapi-com/hosts/stainlessapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stainlessapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/stainlessapi-com/vendors/stainlessapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stainlessapi-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.stainless.com/docs/quickstart-studio
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stainlessapi.com/
- group: auth
  href: https://artifacts.apis.io/stainlessapi-com/security/stainlessapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stainlessapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stainlessapi.com/
created: '2026-10-23'
description: 'Stainless is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by sequoia-capital) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: GetAccountsAccountidFriendsResponse
  property_count: 3
  slug: stainlessapi-com-get-accounts-accountid-friends-response
- name: GetStatusResponse
  property_count: 1
  slug: stainlessapi-com-get-status-response
jsonld:
- class_count: 2
  name: Stainlessapi Com Context
  property_count: 4
  slug: stainlessapi-com-context
layout: provider
modified: '2026-10-23'
name: Stainless
nav: Providers
network: true
overview: 'Stainless is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Stainless catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Stainless'' developer surface includes getting-started guide, documentation, and 11 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: Stainless API Rules
  rule_count: 40
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 3
  slug: stainlessapi-com-rules
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 39.8
    catalog_earned_first_party: 0.0
    catalog_gap: 75.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 10.7
    discoverability: 35.7
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.5
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/stainlessapi-com/stainlessapi-com-2026-11-03T143719.png
security:
- kind: domain-security
  name: Stainlessapi Com Domain Security
  slug: stainlessapi-com-domain-security
  summary_line: DMARC
slug: stainlessapi-com
tags:
- Company
website: https://www.stainlessapi.com/
---
