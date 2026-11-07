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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/chiral/hosts/chiral-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chiral-hosts.yml
- group: other
  href: https://artifacts.apis.io/chiral/vendors/chiral-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chiral-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chiralnano.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/chiral/security/chiral-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chiral-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chiralnano.com/
coverage:
  checked: '2026-10-24'
  detail: The provider's documentation site returns only JavaScript-rendered pages with no machine-readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.chiralnano.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Chiral develops semiconductor manufacturing equipment to fabricate electronic transistors with nanomaterials at industrial scale. It enables semiconductor manufacturers to produce next‑generation chips reliably, leveraging carbon nanotubes, TMDs, and hBN technologies for advanced nanoelectronics.
image: https://cdn.prod.website-files.com/65ad6036b8e90d97576de773/697a2de7b0a90aaecb0b950d_team%20picture%20home%20page.avif
layout: provider
modified: '2026-10-24'
name: Chiral
nav: Providers
network: true
overview: Chiral is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Manufacturing, Nanomaterials, and Equipment.
random_paper: 3
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chiral/chiral-2026-11-03T124054.png
security:
- kind: domain-security
  name: Chiral Domain Security
  slug: chiral-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chiral
tags:
- Company
- Semiconductors
- Manufacturing
- Nanomaterials
- Equipment
website: https://www.chiralnano.com/
---
