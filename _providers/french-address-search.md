---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://geo.api.gouv.fr/adresse'', ''status'': 301, ''note'': ''declared website redirects to https://adresse.data.gouv.fr/outils/api-doc/adresse — a different registrable domain (api.gouv.fr -> data.gouv.fr), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- description: Address search via the French Government
  name: French Address Search
  slug: french-address-search
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/french-address-search-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://geo.api.gouv.fr/adresse
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://ghost.adresse.data.gouv.fr/rss/
created: '2026-05-28'
description: Address search via the French Government
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/french-address-search.png
layout: provider
modified: '2026-05-28'
name: French Address Search
nav: Providers
network: true
overview: 'French Address Search publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data and Public APIs.


  French Address Search''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 13
screenshot: https://raw.githubusercontent.com/api-evangelist/french-address-search/refs/heads/main/screenshots/french-address-search-2026-06-20T181536.png
security:
- kind: domain-security
  name: French Address Search Domain Security
  slug: french-address-search-domain-security
  summary_line: TLSv1.3 · DMARC
slug: french-address-search
tags:
- Open Data
- Public APIs
website: https://geo.api.gouv.fr/adresse
---
