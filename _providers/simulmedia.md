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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.4
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: In-game rewarded-video ad API. A game server exchanges client credentials for a Bearer token, then requests ad opportunities for a player and reports the playback lifecycle (start, progress, complete,
  name: PlayerWON API
  slug: playerwon-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simulmedia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://simulmedia.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/simulmedia-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Simulmedia
- group: company
  title: ''
  type: Blog
  url: https://simulmedia.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.simulmedia.com/auth/signup
- group: start
  title: ''
  type: Login
  url: https://platform.simulmedia.com/sign-in
- group: operate
  title: ''
  type: Support
  url: https://simulmedia.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://simulmedia.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://simulmedia.com/terms
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/simulmedia-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/simulmedia-plans-pricing.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.playerwon.com/developers
created: '2026-07-17'
description: Simulmedia is a technology-driven television advertising company that helps advertisers, agencies, and growth marketers plan, buy, and measure campaigns across linear TV, connected TV (CTV), and games. Its products include the Performance TV media-buying service, the AI-powered TV+ media-buying platform, and Simulmedia Self-Serve. Through PlayerWON, Simulmedia operates an in-game rewarded-video engagement and monetization platform for free-to-play console and PC games, exposed to game developers through the PlayerWON API and a first-party Unity/Unreal SDK. Simulmedia is a portfolio company of Union Square Ventures. This profile was enriched by the API Evangelist pipeline from the company's public developer surface and the open-source PlayerWON SDK.
image: https://logo.clearbit.com/simulmedia.com
layout: provider
mcp_servers:
- description: ''
  name: Simulmedia MCP Server
  slug: simulmedia-mcp-server
modified: '2026-08-13'
name: Simulmedia
nav: Providers
network: true
overview: 'Simulmedia publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Television, Connected TV, and Games.


  Simulmedia''s developer surface includes engineering blog, signup flow, support, changelog, and 9 more developer resources.'
plans:
- name: Simulmedia Plans Pricing
  plan_count: 0
  slug: simulmedia-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Simulmedia Rate Limits
  slug: simulmedia-rate-limits
score:
  band: emerging
  composite: 22.1
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 22.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Simulmedia Authentication
  slug: simulmedia-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Simulmedia Domain Security
  slug: simulmedia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: simulmedia
tags:
- Company
- Advertising
- Television
- Connected TV
- Games
- AdTech
- Rewarded Video
- Media Buying
website: https://simulmedia.com
---
