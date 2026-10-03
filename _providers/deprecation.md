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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Rules, capabilities, vocabulary, and linked-data description for managing API deprecation and retirement.
  name: API Deprecation Practice
  slug: practice
artifact_total: 6
common:
- group: docs
  title: ''
  type: Reference
  url: https://www.rfc-editor.org/rfc/rfc8594.html
- group: docs
  title: ''
  type: Reference
  url: https://datatracker.ietf.org/doc/draft-ietf-httpapi-deprecation-header/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-03-29'
description: API deprecation, sunset headers, end-of-life management, and API retirement practices, including RFC 8594 Sunset, the Deprecation header, OpenAPI deprecation flags, and consumer migration patterns.
finops:
- name: Deprecation Finops
  service_category: API
  slug: deprecation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
jsonld:
- class_count: 0
  name: Deprecation Context
  property_count: 0
  slug: deprecation
layout: provider
modified: '2026-04-28'
name: Deprecation
nav: Providers
network: true
overview: 'Deprecation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Retirement, Deprecation, End of Life, Sunset, and Lifecycle.


  The Deprecation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Deprecation Plans Pricing
  plan_count: 3
  slug: deprecation-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Deprecation Rate Limits
  slug: deprecation-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Deprecation API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: deprecation-rules
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 56.1
    catalog_earned_first_party: 0.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.3
    contract_governance: 13.6
    contract_quality: 6.7
    developer_ergonomics: 7.1
    discoverability: 39.3
    operational_transparency: 33.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
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
slug: deprecation
tags:
- API Retirement
- Deprecation
- End of Life
- Sunset
- Lifecycle
- Migration
---
