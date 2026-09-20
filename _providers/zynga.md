---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-19'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zynga/refs/heads/main/security/zynga-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zynga-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zynga/refs/heads/main/security/zynga-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zynga-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zynga.com/
- group: company
  title: ''
  type: Blog
  url: https://www.zynga.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.zynga.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zynga
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.take2games.com/legal/en-US/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.take2games.com/privacy/en-US/
- group: auth
  title: ''
  type: Security
  url: https://www.zynga.com/security/rdp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zynga/refs/heads/main/llms/zynga-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zynga-llms.txt
coverage:
  checked: '2026-09-13'
  detail: Zynga ships games as end-user products only; developers.zynga.com has no address records, www.zynga.com/developers is a 404 and the live api.zynga.com is an internal game-client router that answers every path with HTTP 400 "Failed to extract service name" under a robots.txt Disallow.
  evidence:
  - status: 404
    url: https://www.zynga.com/developers
  - status: 400
    url: https://api.zynga.com/openapi.json
  - status: 200
    url: https://api.zynga.com/robots.txt
  - status: 404
    url: https://www.zynga.com/llms.txt
  - status: 403
    url: https://www.zynga.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-13'
description: 'Zynga is a mobile and social game developer and publisher, founded in 2007 in San Francisco and a wholly owned subsidiary of Take-Two Interactive since May 2022. It operates a portfolio of free-to-play franchises including FarmVille, Zynga Poker, Words With Friends, CSR Racing, Empires & Puzzles, Toon Blast, Merge Dragons, Harry Potter: Puzzles & Spells, Top Eleven and Golf Rival, built across studios such as NaturalMotion, Peak, Rollic, Socialpoint, Small Giant Games, Gram Games, Nordeus and StarLark. Zynga publishes a corporate website, an engineering blog, a player support center and a responsible disclosure program, but as of September 2026 it operates no public developer program: there is no developer portal, no API reference, and no machine-readable contract on any Zynga-controlled host. The third-party "Zynga API" announced at Zynga Unleashed in 2011-2012 was retired with the zynga.com third-party publishing platform, and developers.zynga.com no longer resolves.'
image: https://www.zynga.com/storage/2018/09/logo.png
layout: provider
modified: '2026-09-13'
name: Zynga
nav: Providers
network: true
overview: 'Zynga is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Video Games, Mobile Games, and Social Games.


  Zynga''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 13.2
  previous_composite: 12.4
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Zynga Domain Security
  slug: zynga-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zynga Vulnerability Disclosure
  slug: zynga-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: zynga
tags:
- Company
- Gaming
- Video Games
- Mobile Games
- Social Games
- Entertainment
- Game Development
- Free-to-Play
- Consumer
website: https://www.zynga.com/
---
