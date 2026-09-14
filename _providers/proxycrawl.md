---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://proxycrawl.com'', ''status'': 301, ''note'': ''declared website redirects to https://crawlbase.com/ — a different registrable domain (proxycrawl.com -> crawlbase.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- description: Scraping and crawling anticaptcha service
  name: ProxyCrawl
  slug: proxycrawl
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/proxycrawl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://proxycrawl.com
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://crawlbase.com/blog/
created: '2026-05-28'
description: Scraping and crawling anticaptcha service
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/proxycrawl.png
layout: provider
modified: '2026-05-28'
name: ProxyCrawl
nav: Providers
network: true
overview: 'ProxyCrawl publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Development and Public APIs.


  ProxyCrawl''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 2
screenshot: https://raw.githubusercontent.com/api-evangelist/proxycrawl/refs/heads/main/screenshots/proxycrawl-2026-06-20T192222.png
security:
- kind: domain-security
  name: Proxycrawl Domain Security
  slug: proxycrawl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: proxycrawl
tags:
- Development
- Public APIs
website: https://proxycrawl.com
---
