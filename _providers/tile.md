---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.thetileapp.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.life360.com/ — a different registrable domain (thetileapp.com -> life360.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 2
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/life360/
- group: company
  title: ''
  type: Website
  url: https://www.thetileapp.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tile-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tile-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tile-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tile-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/life360
created: '2026-07-17'
description: Tile is a consumer-electronics company known for its Bluetooth tracker devices, used to locate everyday items such as keys, wallets, bags, and phones through a companion mobile app and a crowd-sourced Find network. Tile was acquired by Life360 in 2021; its former site thetileapp.com now 301-redirects to life360.com. Surfaced as a portfolio company of Bessemer Venture Partners, Tile publishes no public developer API — this profile captures its security posture (security.txt, a HackerOne responsible-disclosure program, and probed domain security).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tile.png
layout: provider
modified: '2026-07-21'
name: Tile
nav: Providers
network: true
overview: Tile is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Consumer Electronics, Bluetooth, and Tracking.
random_paper: 10
screenshot: https://raw.githubusercontent.com/api-evangelist/tile/refs/heads/main/screenshots/tile-2026-09-02T163740.png
security:
- kind: domain-security
  name: Tile Domain Security
  slug: tile-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tile Vulnerability Disclosure
  slug: tile-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: tile
tags:
- Company
- Consumer
- Consumer Electronics
- Bluetooth
- Tracking
- Location
- IoT
- Hardware
website: https://www.thetileapp.com/
---
