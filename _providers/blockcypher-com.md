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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://blockcypher.com
created: '2026-10-25'
description: 'MommaZoo is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by 500-global) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-25'
name: MommaZoo
nav: Providers
network: true
overview: MommaZoo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
plans:
- name: Blockcypher Com Plans Pricing
  plan_count: 3
  slug: blockcypher-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 6
  name: Blockcypher Com Rate Limits
  slug: blockcypher-com-rate-limits
scopes:
- name: Blockcypher Com Scopes
  scope_count: 0
  slug: blockcypher-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 39.0
    catalog_earned_first_party: 24.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blockcypher Com Authentication
  slug: blockcypher-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Blockcypher Com Domain Security
  slug: blockcypher-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blockcypher-com
tags:
- Company
website: https://blockcypher.com
---
