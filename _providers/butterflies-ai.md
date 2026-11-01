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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Butterflies AI API (no public documentation found; site requires payment).
  name: Butterflies AI API
  slug: butterflies-ai-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/butterflies-ai/hosts/butterflies-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/butterflies-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/butterflies-ai/vendors/butterflies-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/butterflies-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/butterflies-ai/security/butterflies-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/butterflies-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.butterflies.ai/landing
coverage:
  checked: '2026-10-25'
  detail: Landing page returns 402 Payment required, no API documentation accessible.
  evidence:
  - status: 402
    url: https://www.butterflies.ai/landing
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: 'Butterflies AI is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by coatue) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-25'
name: Butterflies AI
nav: Providers
network: true
overview: Butterflies AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 0
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Butterflies Ai Domain Security
  slug: butterflies-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: butterflies-ai
tags:
- Company
website: https://www.butterflies.ai/landing
---
