---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: OAuth2 (authorization code + PKCE) API for Bitmoji for Developers, providing access to a connected user's avatar ID, sticker packs, and sticker search. Served from bitmoji.api.snapchat.com/direct with
  name: Bitmoji Direct API
  slug: bitmoji-direct-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitstrips-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bitmoji.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Bitmoji/BitmojiForDevelopers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bitmoji
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitstrips-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bitstrips-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitstrips-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bitstrips-well-known.yml
created: '2026-07-17'
description: 'Bitstrips was a Toronto-based consumer software company, founded in 2007 by Jacob "Ba" Blackstock, that created the personalized comic platform Bitstrips and the personal-avatar app Bitmoji. Snap Inc. acquired Bitstrips in March 2016, retired the original Bitstrips comic product, and now operates the technology as Bitmoji. The public developer surface today is the Bitmoji Direct API (Bitmoji for Developers): an OAuth2 authorization-code-with-PKCE flow via www.bitmoji.com/connect that grants third-party apps access to a user''s avatar ID, sticker packs, and sticker search, served from bitmoji.api.snapchat.com/direct. Note that Snap has deprecated the "Bitmoji For Identity" product; the standalone stickers and search integrations remain documented. This profile was surfaced as a Kleiner Perkins portfolio company and enriched from the public Bitmoji developer documentation.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitstrips.png
layout: provider
modified: '2026-07-18'
name: Bitstrips
nav: Providers
network: true
overview: 'Bitstrips publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Avatars, Stickers, and Bitmoji.


  Bitstrips'' developer surface includes documentation, authentication, and 6 more developer resources.'
random_paper: 68
score:
  band: emerging
  composite: 15.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 15.2
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitstrips/refs/heads/main/screenshots/bitstrips-2026-07-25T203209.png
security:
- kind: authentication
  name: Bitstrips Authentication
  slug: bitstrips-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Bitstrips Domain Security
  slug: bitstrips-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitstrips
tags:
- Company
- Consumer
- Avatars
- Stickers
- Bitmoji
- Messaging
- Images
- OAuth
- Social
website: https://www.bitmoji.com
---
