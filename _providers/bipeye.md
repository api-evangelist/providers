---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.9
  scored_at: '2026-11-06'
api_count: 1
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/bipeye/security/bipeye-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bipeye-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bipeye.com/
created: '2026-10-20'
description: 'BIPEYE is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-20'
name: BIPEYE
nav: Providers
network: true
overview: BIPEYE publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
plans:
- name: Bipeye Plans Pricing
  plan_count: 4
  slug: bipeye-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Bipeye Rate Limits
  slug: bipeye-rate-limits
scopes:
- name: Bipeye Scopes
  scope_count: 0
  slug: bipeye-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 35.0
    catalog_earned_first_party: 20.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 38.3
    operational_transparency: 21.1
  previous_composite: 16.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bipeye/bipeye-2026-11-03T121738.png
security:
- kind: authentication
  name: Bipeye Authentication
  slug: bipeye-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bipeye Domain Security
  slug: bipeye-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: embed-link
  slug: bipeye-embed-link
slug: bipeye
tags:
- Company
website: https://bipeye.com/
---
