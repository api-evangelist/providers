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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Strongly-typed GraphQL API to query and mutate the Rad TV platform — catalog (features, series, seasons, episodes, streams, miniseries), content management, uploads (TUS resumable), transcoding with A
  name: Rad TV GraphQL API
  slug: rad-tv-graphql-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://rad.live/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.rad.live/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.rad.live/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.rad.live/docs/graphql/types
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.rad.live/docs/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://developers.rad.live/docs/getting-started/quickstart
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rad-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rad-well-known.yml
- group: start
  title: ''
  type: SignUp
  url: https://rad.live/signup
- group: start
  title: ''
  type: Login
  url: https://rad.live/login
- group: commercial
  title: ''
  type: Pricing
  url: https://rad.live/premium
- group: commercial
  title: ''
  type: TermsOfService
  url: https://business.rad.live/terms
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rad-domain-security.yml
created: '2026-07-17'
description: Rad TV (Rad.) is a two-sided subscription video platform connecting content creators with consumers. For creators it offers AI-powered content enhancement tools — video upscaling to 4K/8K (Real-ESRGAN/ESPCN), stereo-to-surround audio upmixing, multilingual AI subtitling in 40+ languages, and viral thumbnail/title prediction with actionable recommendations — plus multi-platform monetization. For consumers it provides streaming plus private cloud storage with sideloading to PS5/PSVR2, DLNA/uPnP, RSS, and Plex/Jellyfin compatibility across web, iOS, Android, Android TV, Apple TV, and PlayStation. Developers build on the platform through a strongly-typed GraphQL API (api.rad.live/graphql), a Model Context Protocol (MCP) server exposing 34 agent tools, Bearer-token/API-key auth and OAuth 2.1 (PKCE), TUS resumable uploads, and a full published documentation site.
image: https://rad.live/rad-new-seo.jpg
layout: provider
mcp_servers:
- description: ''
  name: rad-mcp.yml
  slug: rad-mcpyml
modified: '2026-07-20'
name: Rad.
nav: Providers
network: true
overview: 'Rad. publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, Streaming, Creator Economy, and Artificial Intelligence.


  Rad.''s developer surface includes documentation, API reference, getting-started guide, quickstart, signup flow, pricing, and 8 more developer resources.'
random_paper: 3
scopes:
- name: Rad Scopes
  scope_count: 1
  slug: rad-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 35.1
  delta: 10.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 43.2
    developer_ergonomics: 36.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 24.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Rad Authentication
  slug: rad-authentication
  summary_line: http-bearer/apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Rad Domain Security
  slug: rad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rad
tags:
- Company
- Video
- Streaming
- Creator Economy
- Artificial Intelligence
- Media
- Monetization
- GraphQL
- MCP
website: https://rad.live/
---
