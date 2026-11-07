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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/fork-and-good/well-known/fork-and-good-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fork-and-good-well-known.yml
- group: other
  href: https://artifacts.apis.io/fork-and-good/hosts/fork-and-good-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fork-and-good-hosts.yml
- group: other
  href: https://artifacts.apis.io/fork-and-good/vendors/fork-and-good-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fork-and-good-vendors.yml
- group: auth
  href: https://artifacts.apis.io/fork-and-good/security/fork-and-good-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fork-and-good-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forkandgood.com
coverage:
  checked: '2026-10-24'
  detail: The website renders most content via JavaScript, and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://forkandgood.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Fork & Good is pioneering a new way of raising and producing meat by dramatically reducing the environmental impact of meat production while delivering the highest quality product. The company combines sustainable farming practices with advanced biotechnology to create a future where everyone can enjoy premium meat responsibly. Their mission focuses on climate‑friendly protein, animal welfare, and innovative supply chains, positioning Fork & Good at the forefront of the food‑tech industry.
image: https://dccn0e8z.cdn.imgeng.in/wp-content/uploads/2022/11/dummy-2-scaled-1-1024x548.jpg
layout: provider
modified: '2026-10-24'
name: Fork & Good
nav: Providers
network: true
overview: Fork & Good is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Food Tech, Sustainable, Biotechnology, MeatProduction, and Climate Impact.
random_paper: 8
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
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
  previous_composite: 4.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fork-and-good/fork-and-good-2026-11-03T132230.png
security:
- kind: domain-security
  name: Fork And Good Domain Security
  slug: fork-and-good-domain-security
  summary_line: TLSv1.3 · HSTS
slug: fork-and-good
tags:
- Food Tech
- Sustainable
- Biotechnology
- MeatProduction
- Climate Impact
- Company
website: https://forkandgood.com
---
