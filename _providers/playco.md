---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/playco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.play.co/
- group: company
  title: ''
  type: About
  url: https://www.play.co/about
- group: operate
  title: ''
  type: Support
  url: http://support.play.co/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.play.co/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.play.co/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/play-co
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/playco
- group: company
  title: ''
  type: Press
  url: https://www.play.co/news
- group: build
  title: ''
  type: Packages
  url: packages/playco-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/playco-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/playco-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/playco-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Playco is a consumer instant-games studio with no developer program at all — the play.co navigation is About / Games / Tech / Career / Discover, api.play.co, developer.play.co and docs.play.co do not resolve, and the three technologies it markets to developers (GCInstant, Replicant, Odie3D) ship as internal client-side game tooling that is not published to any package registry.
  evidence:
  - status: 404
    url: https://www.play.co/developers
  - status: 404
    url: https://www.play.co/openapi.json
  - status: <no response>
    url: https://api.play.co/
  - status: 404
    url: https://www.play.co/.well-known/agent-card.json
  - status: 200
    url: https://www.play.co/tech
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Playco is an instant-play gaming company founded in 2020 by Justin Waldron, Michael Carter, Takeshi Otsuka and Teddy Cross, headquartered in Tokyo with teams worldwide. It builds HTML5 games that run inside social and communication platforms without an app install — EverWing on Facebook, Snake Squad on Snap Games, Heads Up! for Zoom, Sway Stories on TikTok and Trip Royale on LINE — and reached unicorn status on a $100M Series A. Its technology stack, described on play.co/tech, is developer tooling rather than a public web API: PixiJS (the open-source HTML5 rendering/creation engine it acquired with Goodboy Digital in 2021), Odie3D (a 3D extension framework), GCInstant (a client-side JavaScript library wrapping platform SDKs and analytics) and Replicant (a backend-as-a-service state manager for instant games). Playco publishes no developer portal, no API reference and no machine-readable contract; its public code surface is the play-co GitHub organization, which is the renamed
  Game Closure organization and carries the legacy devkit HTML5 game platform, js.io and ff.'
image: https://cdn.prod.website-files.com/5ef5b52561b705cdd979275e/5f6bf7aa03bbe535e0b56505_Open%20Graph%20Image.png
layout: provider
modified: '2026-08-26'
name: Playco
nav: Providers
network: true
overview: 'Playco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Games, Instant Games, and HTML5.


  Playco''s developer surface includes support and 12 more developer resources.'
plans:
- name: Playco Plans Pricing
  plan_count: 0
  slug: playco-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Playco Rate Limits
  slug: playco-rate-limits
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/playco/refs/heads/main/screenshots/playco-2026-09-02T151446.png
security:
- kind: domain-security
  name: Playco Domain Security
  slug: playco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: playco
tags:
- Company
- Gaming
- Games
- Instant Games
- HTML5
- Game Engine
- Mobile Games
- Social Gaming
- Developer Tools
- Open-Source
website: https://www.play.co/
---
