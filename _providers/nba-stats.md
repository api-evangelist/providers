---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://any-api.com/nba_com/nba_com/docs/API_Description'', ''status'': 301, ''note'': ''declared website redirects to https://marketplace.apilayer.com/?utm_source=any-api&utm_medium=any-api-redirection&utm_campaign=any-api-redirection — a different registrable domain (any-api.com -> apilayer.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- description: Current and historical NBA Statistics
  name: NBA Stats
  slug: nba-stats
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nba-stats-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://any-api.com/nba_com/nba_com/docs/API_Description
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Current and historical NBA Statistics
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nba-stats.png
layout: provider
modified: '2026-05-28'
name: NBA Stats
nav: Providers
network: true
overview: NBA Stats publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sports And Fitness and Public APIs.
random_paper: 6
screenshot: https://raw.githubusercontent.com/api-evangelist/nba-stats/refs/heads/main/screenshots/nba-stats-2026-06-20T190110.png
security:
- kind: domain-security
  name: Nba Stats Domain Security
  slug: nba-stats-domain-security
  summary_line: TLSv1.3 · HSTS
slug: nba-stats
tags:
- Sports And Fitness
- Public APIs
website: https://any-api.com/nba_com/nba_com/docs/API_Description
---
