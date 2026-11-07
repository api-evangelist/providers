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
api_count: 1
apis:
- description: Amo provides social networking features across its apps.
  name: Amo API
  slug: amo-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/amo/well-known/amo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amo-well-known.yml
- group: other
  href: https://artifacts.apis.io/amo/hosts/amo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amo-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.amo.co/
- group: auth
  href: https://artifacts.apis.io/amo/security/amo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amo.co/
coverage:
  checked: '2026-10-25'
  detail: Home page renders via JavaScript, no machine‑readable API spec discovered.
  evidence:
  - status: 200
    url: https://amo.co/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Amo is a social networking company focused on fostering friendships through multiple apps. Their flagship apps include ID, a collaborative social profile board, Bump, a map for friends, and Sugar, an unlimited canvas chat. The company believes friendship deserves a dedicated online space and builds tools to bring friends closer together, emphasizing community, shared experiences, and innovative social features.
image: https://amo.co/og/amo.png
layout: provider
modified: '2026-10-25'
name: Amo
nav: Providers
network: true
overview: 'Amo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, Networking, Application, and Friendship.


  Amo''s developer surface includes documentation and 4 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.8
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.1
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/amo/amo-2026-11-03T120835.png
security:
- kind: domain-security
  name: Amo Domain Security
  slug: amo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: amo
tags:
- Company
- Social
- Networking
- Application
- Friendship
website: https://www.amo.co/
---
