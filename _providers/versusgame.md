---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 120
  human_in_the_loop: 3
  name: Versusgame Agentic Access
  operation_count: 239
  slug: versusgame-agentic-access
  summary_line: 239 operations · 120 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: 'Production REST API for the Versus interactive gaming platform. 239 operations across 190 paths covering authentication (email/password plus Apple, Google, Facebook and Microsoft social login), games '
  name: Versusgame API
  slug: versusgame-api
artifact_total: 4
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/versusgame-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/versusgame-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/versusgame-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/versusgame-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/versusgame-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/versusgame-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/versusgame-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/versusgame-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/versusgame-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/versusgame-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/versusgame-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/versusgame-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/versusgame-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.versusgame.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.versusgame.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.versusgame.com/privacy
- group: operate
  title: ''
  type: Contact
  url: https://www.versusgame.com/forms/form-01
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VersusGame
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/versusgame
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/versusgame
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/versusgame_stock/
created: '2026-08-02'
description: VersusGame (branded "Versus") is an interactive gaming and audience-engagement company whose AI content-gamification engine turns publisher articles, live broadcasts and on-demand video into embeddable prediction games. Its flagship MiniGames product drops contextual, content-native games into partner sites via embed widgets, and its VersusLM AI system generates prediction games from arbitrary media. The platform layers real-time prediction, social competition, leaderboards, virtual wallets, coin/ticket economies, prize payouts and contextual "seamless ads" on top of partner content to drive longer sessions, repeat visits and incremental revenue. A single production REST API at api.versusgame.com exposes 239 operations across game creation, gameplays, gamesets, leaderboards, widgets, creators, playlists, wallets, ledger, payments/payouts and an autogame AI pipeline. Publicly named partners include ABC, Microsoft, Disney, BuzzFeed, Billboard, ESPN and UFC.
image: https://cdn.prod.website-files.com/661e9580f882ac357a892420/667c9c7ef8960c14de4190b9_Versus-Favicon-256.png
layout: provider
modified: '2026-08-02'
name: VersusGame
nav: Providers
network: true
overview: 'VersusGame publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, gaming, prediction-games, audience-engagement, and gamification.


  VersusGame''s developer surface includes authentication and 21 more developer resources.'
random_paper: 45
score:
  band: thin
  composite: 28.8
  facets:
    commercial_clarity: 21.1
    contract_quality: 38.0
    developer_ergonomics: 12.5
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Versusgame Authentication
  slug: versusgame-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Versusgame Domain Security
  slug: versusgame-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: versusgame
tags:
- Company
- gaming
- prediction-games
- audience-engagement
- gamification
- media-and-entertainment
- publishing
- widgets
- leaderboards
- creator-economy
- ai-content-generation
- payments
website: https://www.versusgame.com/
---
