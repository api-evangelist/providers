---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://jumprampgames.com'', ''status'': 301, ''note'': ''declared website redirects to https://mobilityware.com/ — a different registrable domain (jumprampgames.com -> mobilityware.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jump-ramp-games-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jumprampgames.com
coverage:
  checked: '2026-08-12'
  detail: Jump Ramp Games was acquired by MobilityWare in September 2019 and fully absorbed; jumprampgames.com and the Lucktastic product domain both now answer HTTP 301 to https://mobilityware.com/, so there is no Jump Ramp surface left to profile — no developer site, no spec, no GitHub org (all four candidate org names 404).
  evidence:
  - status: 301
    url: https://jumprampgames.com/
  - status: 404
    url: https://lucktastic.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/jumprampgames
  reason: defunct
  state: none
created: '2026-07-17'
description: Jump Ramp Games was a New York City casual mobile gaming company best known for Lucktastic, a free scratch-card, rewards, and instant-win app that launched on Android in 2014 and grew to roughly 10 million US installs across Android and iOS, consistently ranking near the top of the lifestyle category. Founded by Alex Betancur and Tony Vartanian and backed by Bullpen Capital, the company paired free-to-play casual gaming with performance-marketing and rewards technology. Jump Ramp Games was acquired by MobilityWare in September 2019, which took over the Lucktastic franchise; the jumprampgames.com domain now redirects to mobilityware.com. The company exposes no public developer, API, or documentation surface, so this profile is maintained as a company record in the API Evangelist network rather than an API provider.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jump-ramp-games.png
layout: provider
modified: '2026-08-12'
name: Jump Ramp Games
nav: Providers
network: true
overview: Jump Ramp Games is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobile Games, Casual Gaming, Rewards, and Consumer.
random_paper: 0
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 3
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jump-ramp-games/refs/heads/main/screenshots/jump-ramp-games-2026-07-25T223317.png
security:
- kind: domain-security
  name: Jump Ramp Games Domain Security
  slug: jump-ramp-games-domain-security
  summary_line: TLSv1.2
slug: jump-ramp-games
tags:
- Company
- Mobile Games
- Casual Gaming
- Rewards
- Consumer
- Advertising Technology
- New York
website: https://jumprampgames.com
---
