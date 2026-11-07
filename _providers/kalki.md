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
  href: https://artifacts.apis.io/kalki/hosts/kalki-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kalki-hosts.yml
- group: other
  href: https://artifacts.apis.io/kalki/vendors/kalki-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kalki-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getkalki.com/privacy
- group: other
  title: ''
  type: Leadership
  url: https://getkalki.com/team
- group: auth
  href: https://artifacts.apis.io/kalki/security/kalki-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kalki-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getkalki.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://getkalki.com/mcp
  - status: 403
    url: https://app.getkalki.com/mcp
  - status: 403
    url: https://console.getkalki.com/mcp
  - status: 403
    url: https://invest.getkalki.com/mcp
  - status: 200
    url: https://getkalki.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Kalki is a platform that transforms millions of everyday opinions into collective intelligence, allowing users to share their views, build credibility, earn rewards, and influence future outcomes. By aggregating diverse perspectives, Kalki creates a data-driven community where participants can see real-time sentiment on topics, engage in discussions, and contribute to shaping a brighter future through informed decision-making.
image: https://getkalki.com/og-default.png
layout: provider
modified: '2026-10-24'
name: Kalki
nav: Providers
network: true
overview: Kalki is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Opinion, Community, Rewards, and Data.
random_paper: 20
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.3
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
screenshot: https://apis.io/screenshots/kalki/kalki-2026-11-03T134302.png
security:
- kind: domain-security
  name: Kalki Domain Security
  slug: kalki-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kalki
tags:
- Company
- Opinion
- Community
- Rewards
- Data
website: https://getkalki.com/
---
