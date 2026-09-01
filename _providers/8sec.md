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
  scored_at: '2026-09-01'
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
description: 8SEC was a hybrid-casual and hyper-casual mobile game studio based in Lyon, France, founded in 2015 and later opening a second office in Paris. Over a ten-year run it published more than 90 free-to-play mobile games for iOS and Android — Jump Race!, Turbo Taxi, Trivia.io, Untie! and Human Puzzle among them — collectively driving roughly 50 million downloads, and positioned itself as a full-stack studio spanning game design, development and publishing. UK publisher Kwalee invested EUR 1.5 million in January 2024 and took over publishing duties across the entire 8SEC catalogue. THE STUDIO IS NOW CLOSED — the shutdown was reported in October 2025, with all seven staff, including cofounders Louis Croquet and Louis Giraud, seeking new roles. The company's own site at 8sec.games is no longer deployed — the domain resolves to OVHcloud shared hosting serving a "Site not installed" 404 behind a certificate that does not cover the hostname — and the Teamtailor careers page returns 404.
  8SEC was surfaced into the API Evangelist network as a 500 Global portfolio lead; it never published a public developer API, SDK, machine-readable specification or documentation surface, and it no longer exists to publish one.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/8sec.png
layout: provider
modified: '2026-08-17'
name: 8sec
nav: Providers
network: true
overview: 8sec is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Games, Mobile Games, Game Studio, and Hyper-Casual.
random_paper: 14
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Hybrid-Casual
- Free-to-Play
- Gaming
- France
website: https://8sec.games
---
