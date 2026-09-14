---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://api.youneedabudget.com/'', ''status'': 301, ''note'': ''declared website redirects to https://api.ynab.com/ — a different registrable domain (youneedabudget.com -> ynab.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- description: Budgeting & Planning
  name: YNAB
  slug: ynab
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ynab-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ynab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.youneedabudget.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ynab.com/blog/rss.xml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Budgeting & Planning
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ynab.png
layout: provider
modified: '2026-05-28'
name: YNAB
nav: Providers
network: true
overview: 'YNAB publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance and Public APIs.


  YNAB''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 6
screenshot: https://raw.githubusercontent.com/api-evangelist/ynab/refs/heads/main/screenshots/ynab-2026-06-20T201741.png
security:
- kind: domain-security
  name: Ynab Domain Security
  slug: ynab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ynab Vulnerability Disclosure
  slug: ynab-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: ynab
tags:
- Finance
- Public APIs
website: https://api.youneedabudget.com/
---
