---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: build
  title: ''
  type: Packages
  url: packages/ofo-packages.yml
coverage:
  checked: '2026-08-26'
  detail: Ofo stopped operating bikes by 2020 and its own host ofo.com now refuses TCP connections on both port 80 and port 443 despite still resolving, so every /.well-known/, /openapi.json and /llms.txt probe fails to connect rather than returning a status; the company never published a developer program in the first place, and the only surviving documentation of its endpoints is third-party reverse-engineering of the private mobile-app API at one.ofo.com.
  evidence:
  - status: 0
    url: https://ofo.com/
  - status: 0
    url: https://ofo.com/openapi.json
  - status: 0
    url: https://one.ofo.com/.well-known/agent-card.json
  - status: 0
    url: https://ofobike.com/
  - status: 404
    url: https://ofo.so/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/ofo
  - status: 403
    url: https://forgeglobal.com/ofo_stock/
  reason: defunct
  state: none
created: '2026-08-26'
description: 'Ofo (Chinese: 小黄车, "little yellow bike") was a Beijing dockless bicycle-sharing company founded in 2014 by Dai Wei and four classmates from the Peking University cycling club, and launched publicly on 7 September 2015. At its 2017 peak it had deployed more than 10 million bicycles across roughly 250 cities in 20 countries, reported over 60 million monthly active users, and was valued at around US$2 billion; in March 2018 it raised an $866M round led by Alibaba. Ofo''s bikes were unlocked exclusively through its own consumer iOS and Android app. The company never operated a developer portal, never published a machine-readable API contract, and never shipped official client SDKs — the only documentation of its endpoints is third-party reverse-engineering of the private mobile-app API at one.ofo.com. Ofo withdrew from most international markets in July 2018, collapsed under a deposit-refund backlog that left more than 10 million users queuing for refunds from December 2018, and
  had ceased bike-rental operations by 2020. ofo.com is still registered through Alibaba Cloud and still resolves, but its origin refuses connections on ports 80 and 443; the historic ofo.so host dropped and was re-registered by an unrelated party in April 2025 and now serves a parked arcade-game lander. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-08-26'
name: Ofo
nav: Providers
network: true
overview: Ofo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Transportation, Mobility, and Micromobility.
random_paper: 9
security:
- kind: domain-security
  name: Ofo Domain Security
  slug: ofo-domain-security
  summary_line: no transport/DNS hardening detected
slug: ofo
tags:
- Company
- Defunct
- Transportation
- Mobility
- Micromobility
- Bike Sharing
- Sharing Economy
- Consumer
- China
---
