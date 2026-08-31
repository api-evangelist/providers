---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Breaking Bad Agentic Access
  operation_count: 11
  slug: breaking-bad-agentic-access
  summary_line: 11 operations
api_count: 4
apis:
- description: Characters from the Breaking Bad and Better Call Saul universe.
  name: Breaking Bad Characters API
  slug: breaking-bad-characters-api
- description: On-screen deaths catalogued across the series.
  name: Breaking Bad Deaths API
  slug: breaking-bad-deaths-api
- description: Episodes from the Breaking Bad and Better Call Saul series.
  name: Breaking Bad Episodes API
  slug: breaking-bad-episodes-api
- description: Memorable quotes attributed to characters.
  name: Breaking Bad Quotes API
  slug: breaking-bad-quotes-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Breaking Bad Characters API
  slug: open-breaking-bad-characters-api
- collection_type: open
  name: Breaking Bad Characters Deaths API
  slug: open-breaking-bad-deaths-api
- collection_type: open
  name: Breaking Bad Characters Episodes API
  slug: open-breaking-bad-episodes-api
- collection_type: open
  name: Breaking Bad Characters Quotes API
  slug: open-breaking-bad-quotes-api
- collection_type: open
  name: Breaking Bad API
  slug: open-breaking-bad
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/timbiles/Breaking-Bad--API/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/breaking-bad-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/timbiles/Breaking-Bad--API
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/timbiles/Breaking-Bad--API
- group: commercial
  title: ''
  type: License
  url: https://github.com/timbiles/Breaking-Bad--API/blob/master/LICENSE.rst
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: commercial
  title: Free / Anonymous
  type: Plans
  url: https://github.com/timbiles/Breaking-Bad--API#readme
- group: operate
  title: 10,000 Requests Per Day
  type: RateLimits
  url: https://github.com/timbiles/Breaking-Bad--API#readme
- group: design
  title: ''
  type: JSONLD
  url: json-ld/breaking-bad-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/breaking-bad-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/breaking-bad-rules.yml
created: '2026-05-28'
description: Community-built REST API exposing characters, quotes, episodes, and on-screen deaths from the Breaking Bad and Better Call Saul television universe. The original hosted service at breakingbadapi.com is no longer reachable as of 2026-05-29 (DNS does not resolve). The canonical source code remains at github.com/timbiles/Breaking-Bad--API under BSD-3-Clause and is the basis for the historical OpenAPI and capability artifacts in this repo.
examples:
- key_count: 8
  name: Breaking Bad Getrandomdeath Example
  slug: breaking-bad-getrandomdeath-example
image: https://github.com/timbiles/Breaking-Bad--API/raw/master/public/favicon.ico
json_schemas:
- name: Character
  property_count: 11
  slug: breaking-bad-character
- name: Death
  property_count: 8
  slug: breaking-bad-death
- name: Episode
  property_count: 7
  slug: breaking-bad-episode
- name: Quote
  property_count: 4
  slug: breaking-bad-quote
json_structures:
- name: Breaking Bad Character Structure
  property_count: 11
  slug: breaking-bad-character-structure
- name: Breaking Bad Death Structure
  property_count: 8
  slug: breaking-bad-death-structure
- name: Breaking Bad Episode Structure
  property_count: 7
  slug: breaking-bad-episode-structure
- name: Breaking Bad Quote Structure
  property_count: 4
  slug: breaking-bad-quote-structure
jsonld:
- class_count: 4
  name: Breaking Bad Context
  property_count: 27
  slug: breaking-bad-context
layout: provider
modified: '2026-05-29'
name: Breaking Bad
nav: Providers
network: true
overview: 'Breaking Bad publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Characters API, Deaths API, Episodes API, and 1 more. Tagged areas include Video, Television, Public APIs, Open-Source, and Breaking Bad.


  The Breaking Bad catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
random_paper: 20
rules:
- effective_rule_count: 5
  extends: []
  name: Breaking Bad API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: breaking-bad-jsonschema-spectral-rules
- effective_rule_count: 73
  extends:
  - spectral:oas
  name: Breaking Bad API Rules
  rule_count: 32
  severity_counts:
    error: 10
    hint: 0
    info: 9
    warn: 13
  slug: breaking-bad-rules
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 47.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 27.7
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 20.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/breaking-bad/refs/heads/main/screenshots/breaking-bad-2026-06-20T173647.png
slug: breaking-bad
tags:
- Video
- Television
- Public APIs
- Open-Source
- Breaking Bad
- Better Call Saul
- Pop Culture
- Deprecated
---
