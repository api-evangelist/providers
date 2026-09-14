---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/9count-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getwinkapp.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/9count
- group: company
  title: ''
  type: Blog
  url: https://blog.getwinkapp.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getwinkapp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getwinkapp.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/9-count-inc
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/9count-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 9 Count ships only end-user mobile apps — its corporate domain www.9count.co 301-redirects every path to the Wink consumer marketing site, its GitHub org holds 25 repositories of which 23 are forks of third-party vendor SDKs (Stream Chat, mParticle, OneSignal, RevenueCat) and none is an API contract, and api./developer./docs. subdomains do not resolve on any domain it owns.
  evidence:
  - status: 404
    url: https://www.getwinkapp.com/openapi.json
  - status: 404
    url: https://www.getwinkapp.com/llms.txt
  - status: 404
    url: https://www.getwinkapp.com/.well-known/api-catalog
  - status: 404
    url: https://www.lex.lgbt/.well-known/agent-card.json
  - status: 200
    url: https://github.com/9count
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: '9 Count, Inc. is a Los Angeles (Venice, CA) consumer mobile app studio founded in 2018 by Alex Hofmann, the former CEO of musical.ly, and Joe Viola. The company builds, tests and cross-promotes a portfolio of social-connection applications rather than a single product, iterating on each with usage data and customer feedback. Its flagship is Wink, an AI-assisted friend-making and dating app that matches on personality, stated intent and real-world interests instead of swipe-first selection, and it acquired the LGBTQ+ social and personals app Lex in September 2024. Earlier titles include the dating app Summer, social arcade app Juju and the creator-fan app Popstream. 9 Count has raised roughly $27.5M across three rounds. It is a business-to-consumer studio: its products ship as end-user mobile applications through the App Store and Google Play, and as of a 2026-09-05 probe it publishes no public API, SDK, webhook surface, developer portal or machine-readable specification of
  any kind.'
image: https://avatars.githubusercontent.com/u/45574631?v=4
layout: provider
modified: '2026-09-05'
name: 9 Count
nav: Providers
network: true
overview: '9 Count is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Apps, Social Networking, Dating, and Mobile Applications.


  9 Count''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 1
security:
- kind: domain-security
  name: 9Count Domain Security
  slug: 9count-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 9count
tags:
- Company
- Consumer Apps
- Social Networking
- Dating
- Mobile Applications
- Social Discovery
- Consumer Internet
- Media and Entertainment
website: https://www.getwinkapp.com/
---
