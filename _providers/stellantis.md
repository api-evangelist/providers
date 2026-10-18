---
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
    error_semantics: derived
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
  score: 16.2
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: Stellantis Connected Vehicle API
  name: Connected Vehicle API
  slug: connected-vehicle-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: Allows to organize the vehicles (of the owner) by group(s) according to functional criteria. Groups allow collective action on a set of vehicles, such as subscription to a monitor or a data stream (*r
  name: Stellantis Grouping API
  slug: stellantis-grouping-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: Describe the data stream feature allowing the publication of defined stream data on the associated output channel
  name: Stellantis Data Stream API
  slug: stellantis-data-stream-api
artifact_total: 10
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stellantis/refs/heads/main/errors/stellantis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/stellantis-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stellantis/refs/heads/main/rules/stellantis-rules.yml
  title: ''
  type: Spectral
  url: rules/stellantis-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stellantis/refs/heads/main/json-ld/stellantis-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/stellantis-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stellantis/refs/heads/main/vocabulary/stellantis-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/stellantis-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stellantis/refs/heads/main/conformance/stellantis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stellantis-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/stellantis/refs/heads/main/hosts/stellantis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stellantis-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/stellantis/refs/heads/main/vendors/stellantis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stellantis-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.stellantis.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stellantis
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stellantis/refs/heads/main/security/stellantis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stellantis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stellantis.com
created: '2026-10-13'
description: Stellantis is a global automotive manufacturing corporation formed in 2021 through the merger of Fiat Chrysler Automobiles and PSA Group. It designs, manufactures, and sells a wide range of vehicles under 14 iconic brands, including Abarth, Alfa Romeo, Chrysler, Citroën, Dodge, DS Automobiles, Fiat, Jeep, Lancia, Maserati, Opel, Peugeot, Ram, and Vauxhall. The company focuses on innovative mobility solutions, sustainability, and advanced technology platforms, operating worldwide with a strong presence in Europe, North America, and Latin America. Its corporate website provides extensive information on its strategy, governance, brand portfolio, and sustainability initiatives.
json_schemas:
- name: DataStream
  property_count: 3
  slug: stellantis-data-stream
- name: DataStreamStatusSetter
  property_count: 0
  slug: stellantis-data-stream-status-setter
- name: GroupMaintain
  property_count: 3
  slug: stellantis-group-maintain
- name: GroupObj
  property_count: 2
  slug: stellantis-group-obj
jsonld:
- class_count: 86
  name: Stellantis Context
  property_count: 135
  slug: stellantis-context
layout: provider
modified: '2026-10-13'
name: Stellantis
nav: Providers
network: true
overview: 'Stellantis publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Grouping API, Data Stream API, and 1 more. Tagged areas include Company, Automotive, Manufacturing, Mobility, and Sustainability.


  The Stellantis catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Stellantis'' developer surface includes documentation and 10 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Stellantis API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: stellantis-rules
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 56.8
    developer_ergonomics: 9.5
    discoverability: 62.5
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Stellantis Domain Security
  slug: stellantis-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: stellantis
tags:
- Company
- Automotive
- Manufacturing
- Mobility
- Sustainability
website: https://www.stellantis.com
---
