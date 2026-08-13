---
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
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/second-dinner-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/second-dinner-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.seconddinner.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seconddinner
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.seconddinner.com/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://www.seconddinner.com/careers/
- group: other
  title: ''
  type: Product
  url: https://www.marvelsnap.com/
- group: company
  title: ''
  type: Blog
  url: https://marvelsnap.com/news/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/second-dinner_stock/
coverage:
  checked: '2026-08-05'
  detail: Second Dinner ships consumer games only — MARVEL SNAP has a player web shop and a leaderboard page but no developer surface, and contract discovery across seconddinner.com, marvelsnap.com and shop.marvelsnap.com found no OpenAPI, no /.well-known/ document, no llms.txt, no /developers page, and no first-party package on npm, PyPI or NuGet; api.seconddinner.com and api.marvelsnap.com do not resolve in DNS.
  evidence:
  - status: 404
    url: https://marvelsnap.com/openapi.json
  - status: 404
    url: https://marvelsnap.com/developers
  - status: 404
    url: https://marvelsnap.com/.well-known/agent-card.json
  - status: 404
    url: https://shop.marvelsnap.com/.well-known/api-catalog
  - status: 403
    url: https://www.seconddinner.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: 'Second Dinner is an independent, remote-first video game studio headquartered in Irvine, California, founded in 2018 by a group of former Blizzard Hearthstone developers including Hamilton Chu, Ben Brode, Yong Woo, Jomaro Kindred and Michael Schweitzer. Its debut title, MARVEL SNAP, is a fast-paced digital collectible card game built in Unity that won Mobile Game of the Year at both The Game Awards and the DICE Awards along with an Apple Design Award, and the studio has since been reported to be building its next title on the Godot engine. Second Dinner raised a $100M Series B led by Griffin Gaming Partners in January 2024. The studio ships consumer games rather than developer platforms: it publishes no public API, SDK, developer portal, or machine-readable specification, and its public engineering footprint is a small GitHub organization of Unity build and test tooling forks.'
image: https://images.ctfassets.net/jgt5qzadk2ry/d1Hv9qzoyC47v1cIxEgDP/b7e1885f3299fc74d073ddfa206e7c93/ico-6.png
layout: provider
modified: '2026-08-05'
name: Second Dinner
nav: Providers
network: true
overview: 'Second Dinner is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video Games, Game Development, Gaming, and Entertainment.


  Second Dinner''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 10.0
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Second Dinner Domain Security
  slug: second-dinner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: second-dinner
tags:
- Company
- Video Games
- Game Development
- Gaming
- Entertainment
- Mobile Games
- Card Games
- Unity
website: https://www.seconddinner.com/
---
