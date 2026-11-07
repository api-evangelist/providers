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
  href: https://artifacts.apis.io/barbaropizza-com/hosts/barbaropizza-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/barbaropizza-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/barbaropizza-com/vendors/barbaropizza-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/barbaropizza-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/barbaropizza-com/security/barbaropizza-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/barbaropizza-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://barbaropizza.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://barbaropizza.com/Privacy
coverage:
  checked: '2026-11-02'
  detail: Barbaropizza.com is a restaurant with no public API surface.
  evidence:
  - status: 200
    url: https://barbaropizza.com/
  reason: not-a-software-company
  state: none
created: '2026-11-02'
description: Barbaro. Sourdough pizza shaped by time, fire, and craft. El Dorado Hills, California. Start with any Barbaro pizza or build from scratch. Choose your ingredients and watch the balance shift in real time. Our sourdough recipe, as a working calculator. Make the amount you need, change the hydration or the flours, or bring your own recipe. El Dorado Hills, CA. Riff on a Barbaro pizza. Sounds like a mistake. Tastes like a decision. Every pizza on the menu is a place to start. The Builder takes it from there. The dough, your way. Start with our house recipe or bring your own. Explore flours, hydration, preferments, and fermentation schedules. Keep your versions and see what changes.
image: https://barbaropizza.com/images/barbaro/og-barbaro-real-quiet-cover-20260930.jpeg
layout: provider
modified: '2026-11-02'
name: Barbaro
nav: Providers
network: true
overview: Barbaro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pizza, Sourdough, Food, and Restaurant.
random_paper: 19
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 7
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
security:
- kind: domain-security
  name: Barbaropizza Com Domain Security
  slug: barbaropizza-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: barbaropizza-com
tags:
- Company
- Pizza
- Sourdough
- Food
- Restaurant
- Ordering
website: https://barbaropizza.com/
---
