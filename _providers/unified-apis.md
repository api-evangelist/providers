---
agent_readiness:
  band: human-only
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 4
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unified-apis/refs/heads/main/json-ld/unified-apis-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/unified-apis-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unified-apis/refs/heads/main/vocabulary/unified-apis-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/unified-apis-vocabulary.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/unified-apis/refs/heads/main/json-schema/unified-apis-connector-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-apis-connector-schema.json
created: '2026-03-27'
description: This is the index of unified API service and tooling repos being tracked by the API Evangelist network. Unified APIs (also called integration hubs, API aggregators, or universal connectors) abstract multiple third-party APIs behind a single standardized interface, enabling software teams to build one integration instead of many. The market has grown to 23+ vendors in 2026, covering HR, accounting, CRM, file storage, ATS, e-commerce, and data pipeline use cases.
examples:
- key_count: 15
  name: Unified Apis Connector Example
  slug: unified-apis-connector-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: Unified API Connector
  property_count: 14
  slug: unified-apis-connector
json_structures:
- name: Unified Apis Connector Structure
  property_count: 0
  slug: unified-apis-connector-structure
jsonld:
- class_count: 6
  name: Unified Apis Context
  property_count: 11
  slug: unified-apis-context
layout: provider
modified: '2026-05-03'
name: Unified APIs
nav: Providers
network: true
overview: 'Unified APIs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Aggregation, Normalization, Unified API, Integration, and Software-as-a-Service.


  The Unified APIs catalog on APIs.io includes 1 JSON-LD context.'
random_paper: 4
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 14.7
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: unified-apis
tags:
- Aggregation
- Normalization
- Unified API
- Integration
- Software-as-a-Service
- iPaaS
---
