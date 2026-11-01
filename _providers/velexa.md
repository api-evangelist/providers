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
api_count: 2
apis:
- description: API for Velexa platform (no public contract discovered)
  name: Velexa API
  slug: velexa-api-2
- baseURL: https://api-live.velexa.com
  baseurl_source: declared
  description: 'Velexa API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: Velexa API
  slug: velexa-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/velexa/rules/velexa-rules.yml
  title: ''
  type: Spectral
  url: rules/velexa-rules.yml
- group: design
  href: https://artifacts.apis.io/velexa/json-ld/velexa-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/velexa-context.jsonld
- group: design
  href: https://artifacts.apis.io/velexa/vocabulary/velexa-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/velexa-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/velexa/data-model/velexa-data-model.yml
  title: ''
  type: DataModel
  url: data-model/velexa-data-model.yml
- group: design
  href: https://artifacts.apis.io/velexa/conformance/velexa-conformance.yml
  title: ''
  type: Conformance
  url: conformance/velexa-conformance.yml
- group: other
  href: https://artifacts.apis.io/velexa/hosts/velexa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/velexa-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.velexa.com/
- group: auth
  href: https://artifacts.apis.io/velexa/security/velexa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/velexa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://velexa.com/
created: '2026-10-21'
description: Velexa provides WealthTech solutions for institutions serving next‑generation investors. The platform offers a fully customisable investing‑as‑a‑service model with access to all markets through a single integration. Velexa consolidates integration and support functions under its partner EXANTE, offering white‑label and API solutions to scale financial businesses. It aims to deliver seamless, end‑to‑end wealth management capabilities, supporting institutions in delivering modern investment experiences to their clients.
json_schemas:
- name: PostMd30SymbolsAaplNasdaqRequest
  property_count: 6
  slug: velexa-post-md30-symbols-aapl-nasdaq-request
- name: PostMd30SymbolsAaplNasdaqResponse
  property_count: 12
  slug: velexa-post-md30-symbols-aapl-nasdaq-response
- name: PostTrade30OrdersRequest
  property_count: 6
  slug: velexa-post-trade30-orders-request
- name: PostTrade30OrdersResponse
  property_count: 7
  slug: velexa-post-trade30-orders-response
jsonld:
- class_count: 4
  name: Velexa Context
  property_count: 23
  slug: velexa-context
layout: provider
modified: '2026-10-21'
name: Velexa
nav: Providers
network: true
overview: 'Velexa is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, WealthTech, Financial Services, API Platform, and Institutional Investing.


  The Velexa catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Velexa''s developer surface includes support and 8 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Velexa API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: velexa-rules
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 22.6
    developer_ergonomics: 4.8
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Velexa Domain Security
  slug: velexa-domain-security
  summary_line: TLSv1.3 · DMARC
slug: velexa
tags:
- Company
- WealthTech
- Financial Services
- API Platform
- Institutional Investing
website: https://velexa.com/
---
