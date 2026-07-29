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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dice-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://dice.fm/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dice-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dice-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dice-security.txt
- group: company
  title: ''
  type: Website
  url: https://dice.fm/
- group: company
  title: ''
  type: Blog
  url: https://dice.fm/blog
- group: operate
  title: ''
  type: Support
  url: https://dice.fm/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dice.fm/terms_and_conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dice.fm/privacy_policy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dicefm
created: '2026-07-17'
description: DICE is a mobile-first live events discovery and ticketing platform founded in London in 2014 by Phil Hutcheon. Through the DICE app (iOS and Android) and dice.fm, fans discover concerts, club nights, festivals, tours and livestreams, buy fee-transparent tickets that live securely in-app, join waiting lists for sold-out shows, and resell tickets at face value to curb touting. DICE also runs a partner business serving venues, promoters, artists and festivals with tools to reach fans, sell tickets and grow their audiences, and owns the Boiler Room brand. Backed by SoftBank Vision Fund, DICE operates across the UK, Europe and the US. DICE publishes no public developer API; this profile captures the company's public web, security and legal surface.
image: https://dice.fm/static/images/dice-fan-social.png
layout: provider
modified: '2026-07-19'
name: DICE
nav: Providers
network: true
overview: 'DICE is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Live Events, Ticketing, and Music.


  DICE''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 13.7
  delta: -0.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 14.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dice/refs/heads/main/screenshots/dice-2026-07-25T211933.png
security:
- kind: domain-security
  name: Dice Domain Security
  slug: dice-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dice Vulnerability Disclosure
  slug: dice-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: dice
tags:
- Company
- Consumer
- Live Events
- Ticketing
- Music
- Events
- Entertainment
- Mobile
- Marketplace
- Discovery
website: https://dice.fm/
---
