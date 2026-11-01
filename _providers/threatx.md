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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'ThreatX API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: ThreatX API
  slug: threatx-api
artifact_total: 10
common:
- group: auth
  href: https://artifacts.apis.io/threatx/well-known/threatx-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/threatx-status-security.txt
- group: agent
  href: https://artifacts.apis.io/threatx/well-known/threatx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/threatx-well-known.yml
- group: other
  href: https://artifacts.apis.io/threatx/vendors/threatx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/threatx-vendors.yml
- group: design
  href: https://artifacts.apis.io/threatx/rules/threatx-rules.yml
  title: ''
  type: Spectral
  url: rules/threatx-rules.yml
- group: design
  href: https://artifacts.apis.io/threatx/json-ld/threatx-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/threatx-context.jsonld
- group: design
  href: https://artifacts.apis.io/threatx/vocabulary/threatx-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/threatx-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/threatx/data-model/threatx-data-model.yml
  title: ''
  type: DataModel
  url: data-model/threatx-data-model.yml
- group: operate
  href: https://artifacts.apis.io/threatx/changelog/threatx-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/threatx-changelog.yml
- group: design
  href: https://artifacts.apis.io/threatx/conformance/threatx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/threatx-conformance.yml
- group: other
  href: https://artifacts.apis.io/threatx/hosts/threatx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/threatx-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.threatx.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.threatx.com/news/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.threatx.com/documentation/whats-new/
- group: auth
  href: https://artifacts.apis.io/threatx/security/threatx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/threatx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.threatx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.threatx.com/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.threatx.com/documentation/using-threatx/
- group: operate
  title: ''
  type: Support
  url: https://www.threatx.com/security
- group: company
  title: ''
  type: Blog
  url: https://www.threatx.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.threatx.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.threatx.com/privacy-policy/
coverage:
  checked: '2026-10-21'
  detail: Documentation pages exist but provide no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.threatx.com/documentation/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: ThreatX, now part of A10 Networks, provides API and application security solutions including API protection, bot management, DDoS mitigation, and risk‑based blocking. Their platform secures modern cloud‑native applications and APIs across multi‑cloud environments, offering managed services and on‑premise deployments for enterprises.
json_schemas:
- name: PostTxApiV1ChannelsHRequest
  property_count: 2
  slug: threatx-post-tx-api-v1-channels-hrequest
- name: PostTxApiV1ChannelsHResponse
  property_count: 1
  slug: threatx-post-tx-api-v1-channels-hresponse
- name: PostTxApiV1CustomersRequest
  property_count: 2
  slug: threatx-post-tx-api-v1-customers-request
- name: PostTxApiV1ListsRequest
  property_count: 4
  slug: threatx-post-tx-api-v1-lists-request
- name: PostTxApiV1LoginRequest
  property_count: 2
  slug: threatx-post-tx-api-v1-login-request
- name: PostTxApiV2LogsRequest
  property_count: 4
  slug: threatx-post-tx-api-v2-logs-request
jsonld:
- class_count: 9
  name: Threatx Context
  property_count: 7
  slug: threatx-context
layout: provider
modified: '2026-10-21'
name: ThreatX
nav: Providers
network: true
overview: 'ThreatX is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, API Protection, Bot Management, DDoS Mitigation, and Cloud Security.


  The ThreatX catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ThreatX''s developer surface includes changelog, documentation, getting-started guide, support, engineering blog, and 16 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: ThreatX API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: threatx-rules
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 35.6
    contract_quality: 22.0
    developer_ergonomics: 28.6
    discoverability: 55.4
    operational_transparency: 42.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Threatx Domain Security
  slug: threatx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: threatx
tags:
- Security
- API Protection
- Bot Management
- DDoS Mitigation
- Cloud Security
website: https://www.threatx.com/
---
