---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://8sec.games
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/8sec
- group: company
  title: ''
  type: Twitter
  url: https://x.com/8sec_games
- group: company
  title: ''
  type: Careers
  url: https://8sec.teamtailor.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/8sec-domain-security.yml
coverage:
  checked: '2026-08-17'
  detail: 8SEC closed in October 2025 after ten years and roughly 90 mobile games, and its own site is gone with it — 8sec.games now resolves to an OVHcloud "Site not installed" 404 behind a certificate issued to cluster103.hosting.ovh.net, so a verifying client cannot even complete the TLS handshake; only a leftover Netlify deploy of the marketing site still serves 8SEC content, and it answers every path with the same HTML homepage.
  evidence:
  - status: 404
    url: https://8sec.games/
  - status: 404
    url: https://8sec.games/.well-known/security.txt
  - status: 404
    url: https://8sec.games/openapi.json
  - status: 404
    url: https://8sec.teamtailor.com/
  - status: 200
    url: https://mobilegamer.biz/french-hybridcasual-studio-8sec-is-closing/
  reason: defunct
  state: none
created: '2026-07-17'
description: 8SEC is a hybrid-casual and hyper-casual mobile game studio based in Lyon, France, founded in 2015 by serial entrepreneur and investor Jeremie Berrebi. The studio rapidly prototypes and ships engaging free-to-play mobile games for iOS and Android, with titles such as Jump Race!, Turbo Taxi, Trivia.io, Untie!, and Human Puzzle that have collectively driven over 50 million downloads. 8SEC positions itself as a full-stack studio spanning game design, development, and publishing. It is a portfolio company of 500 Global, surfaced into the API Evangelist network via VC portfolio mapping. The company operates as a game producer and does not currently publish a public developer API, SDK, or documentation surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/8sec.png
layout: provider
modified: '2026-07-17'
name: 8sec
nav: Providers
network: true
overview: 8sec is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Games, Mobile Games, Game Studio, and Hyper-Casual.
random_paper: 73
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: 8Sec Domain Security
  slug: 8sec-domain-security
  summary_line: no transport/DNS hardening detected
slug: 8sec
tags:
- Company
- Games
- Mobile Games
- Game Studio
- Hyper-Casual
- Gaming
- France
website: https://8sec.games
---
