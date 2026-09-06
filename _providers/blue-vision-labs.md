---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bluevisionlabs
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blue-vision-labs-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blue-vision-labs-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blue-vision-labs-llms.txt
created: '2026-07-17'
description: 'Blue Vision Labs was a London-based computer-vision company that built the first city-scale augmented reality cloud — crowdsourcing centimetre-accurate 3D maps of entire cities from images captured by car-mounted smartphone cameras, then letting developers use visual positioning to place shared and persistent AR content that every device sees in the same real-world spot. It emerged from stealth in March 2018 with a $14.5M round led by GV, alongside Accel and Horizons Ventures, and offered invite-only early access to iOS and Android SDKs covering San Francisco, New York City and London. Lyft acquired the company in October 2018 and made it the UK hub of its Level 5 self-driving division. The developer platform is retired: bluevisionlabs.com no longer resolves to a web host, the documentation and SDK downloads are offline, and no public API surface remains.'
image: https://avatars.githubusercontent.com/u/19323859?v=4
layout: provider
modified: '2026-07-20'
name: Blue Vision Labs
nav: Providers
network: true
overview: Blue Vision Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Frontier Tech, Augmented Reality, Computer-Vision, and Mapping.
random_paper: 0
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 6.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blue-vision-labs/refs/heads/main/screenshots/blue-vision-labs-2026-07-25T203444.png
security:
- kind: domain-security
  name: Blue Vision Labs Domain Security
  slug: blue-vision-labs-domain-security
  summary_line: no transport/DNS hardening detected
slug: blue-vision-labs
tags:
- Company
- Frontier Tech
- Augmented Reality
- Computer-Vision
- Mapping
- Localization
- Spatial Computing
- Acquired
- Retired
---
