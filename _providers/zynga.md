---
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zynga-vulnerability-disclosure.yml
- group: auth
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
random_paper: 7
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
