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
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Static read‑only API providing prostitution law data for 196 countries in JSON, CSV and Markdown. No authentication required.
  name: Prostitution Laws Data API
  slug: prostitution-laws-data-api
- baseURL: https://prostitutionlaws.org
  baseurl_source: declared
  description: 'Static, read-only files: no key, no sign-up, no rate plan; `Access-Control-Allow-Origin: *`. Regenerated on every release of the site.'
  name: Prostitution Laws data API API
  slug: prostitution-laws-data-api-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/prostitutionlaws/rules/prostitutionlaws-rules.yml
  title: ''
  type: Spectral
  url: rules/prostitutionlaws-rules.yml
- group: design
  href: https://artifacts.apis.io/prostitutionlaws/json-ld/prostitutionlaws-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/prostitutionlaws-context.jsonld
- group: design
  href: https://artifacts.apis.io/prostitutionlaws/vocabulary/prostitutionlaws-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/prostitutionlaws-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/prostitutionlaws/conformance/prostitutionlaws-conformance.yml
  title: ''
  type: Conformance
  url: conformance/prostitutionlaws-conformance.yml
- group: design
  href: https://artifacts.apis.io/prostitutionlaws/data-model/prostitutionlaws-data-model.yml
  title: ''
  type: DataModel
  url: data-model/prostitutionlaws-data-model.yml
- group: design
  href: https://artifacts.apis.io/prostitutionlaws/errors/prostitutionlaws-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/prostitutionlaws-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/prostitutionlaws/llms/prostitutionlaws-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/prostitutionlaws-llms.txt
- group: agent
  href: https://artifacts.apis.io/prostitutionlaws/well-known/prostitutionlaws-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/prostitutionlaws-well-known.yml
- group: other
  href: https://artifacts.apis.io/prostitutionlaws/hosts/prostitutionlaws-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prostitutionlaws-hosts.yml
- group: other
  href: https://artifacts.apis.io/prostitutionlaws/vendors/prostitutionlaws-vendors.yml
  title: ''
  type: Vendors
  url: vendors/prostitutionlaws-vendors.yml
- group: auth
  href: https://artifacts.apis.io/prostitutionlaws/security/prostitutionlaws-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prostitutionlaws-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prostitutionlaws.org/
- group: docs
  title: ''
  type: Documentation
  url: https://prostitutionlaws.org/developers/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://prostitutionlaws.org/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://prostitutionlaws.org/openapi.json
- group: agent
  title: ''
  type: llms.txt
  url: https://prostitutionlaws.org/llms.txt
- group: agent
  title: ''
  type: MCP
  url: https://prostitutionlaws.org/.well-known/mcp.json
- group: other
  title: ''
  type: AgentCard
  url: https://prostitutionlaws.org/.well-known/agent-card.json
created: '2026-11-02'
description: Prostitution Laws provides a comprehensive, country‑by‑country reference of prostitution legislation worldwide. The site maps legal models across 196 nations, detailing whether selling, buying, brothel operation, and advertising are permitted, regulated, or prohibited. Data is regularly updated, with methodology notes and sources for each statute, offering researchers, policymakers, and the public clear insight into global sex‑work laws.
image: https://prostitutionlaws.org/cards/world-og.png?v=mvy1b23x
json_schemas:
- name: AllCountries
  property_count: 5
  slug: prostitutionlaws-all-countries
- name: CountryDocument
  property_count: 6
  slug: prostitutionlaws-country-document
- name: IndexDocument
  property_count: 7
  slug: prostitutionlaws-index-document
jsonld:
- class_count: 5
  name: Prostitutionlaws Context
  property_count: 31
  slug: prostitutionlaws-context
layout: provider
modified: '2026-11-02'
name: Prostitution Laws
nav: Providers
network: true
overview: 'Prostitution Laws publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including data API API, and 1 more. Tagged areas include Company, Law, Data, Research, and Global.


  The Prostitution Laws catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Prostitution Laws'' developer surface includes documentation, API reference, and 16 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Prostitution Laws API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: prostitutionlaws-rules
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 56.7
    developer_ergonomics: 13.1
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Prostitutionlaws Domain Security
  slug: prostitutionlaws-domain-security
  summary_line: TLSv1.3
slug: prostitutionlaws
tags:
- Company
- Law
- Data
- Research
- Global
website: https://prostitutionlaws.org/
---
