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
  href: https://artifacts.apis.io/marine-snow/hosts/marine-snow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/marine-snow-hosts.yml
- group: other
  href: https://artifacts.apis.io/marine-snow/vendors/marine-snow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/marine-snow-vendors.yml
- group: auth
  href: https://artifacts.apis.io/marine-snow/security/marine-snow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/marine-snow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://marine-snow.co/vgux
coverage:
  checked: '2026-10-29'
  detail: Marine Snow's public website provides only a marketing page with no API documentation or developer resources.
  evidence:
  - status: 200
    url: https://marine-snow.co/vgux
  reason: not-a-software-company
  state: none
created: '2026-10-29'
description: Marine Snow is a venture‑backed company listed in the API Evangelist harvest backlog. The public website (https://marine-snow.co/vgux) is a minimal Squarespace page that provides only a title and an animated image, with no further details about the company's mission, products, or services. No API documentation, developer portal, or other informational pages are publicly available. The site does not expose any API endpoints, pricing information, terms of service, privacy policy, or support resources.
image: http://static1.squarespace.com/static/5e77c4dd917b85615be92a4c/t/5f9a2bd75f044f0fdc7bf256/1603727030146/Orbs-Animated-2.gif?format=1500w
layout: provider
modified: '2026-10-29'
name: Marine Snow
nav: Providers
network: true
overview: Marine Snow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Venture, Portfolio, and Placeholder.
random_paper: 8
score:
  band: minimal
  composite: 2.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 3.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/marine-snow/marine-snow-2026-11-03T135333.png
security:
- kind: domain-security
  name: Marine Snow Domain Security
  slug: marine-snow-domain-security
  summary_line: TLSv1.3 · HSTS
slug: marine-snow
tags:
- Company
- Venture
- Portfolio
- Placeholder
website: https://marine-snow.co/vgux
---
