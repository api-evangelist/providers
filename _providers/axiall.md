---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axiall/refs/heads/main/security/axiall-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axiall-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/axiall-corporation
- group: other
  title: ''
  type: Successor
  url: https://www.westlake.com
coverage:
  checked: '2026-09-18'
  detail: Axiall was absorbed into Westlake Chemical on 2016-08-31; www.axiall.com and axiall.com resolve to 34.199.101.188 but nothing listens on 80 or 443 (every probe timed out, TCP connect refused), so there is no site, no docs and no contract to read.
  evidence:
  - status: 0
    url: https://www.axiall.com
  - status: 0
    url: https://axiall.com
  - status: 0
    url: https://www.axiall.com/.well-known/agent-card.json
  - status: 200
    url: https://www.westlake.com/westlake-chemical-completes-acquisition-axiall-corporation
  - status: 200
    url: https://www.linkedin.com/company/axiall-corporation
  reason: defunct
  state: none
created: '2026-03-23'
description: Axiall Corporation was a manufacturer and international marketer of chemicals and building products, including chlorovinyls (chlor-alkali, PVC resin and vinyl compounds) and aromatics, for use in industrial and consumer applications. Westlake Chemical completed its acquisition of Axiall on 2016-08-31 and the Axiall brand and website have been absorbed into Westlake; the company published no developer program or API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/axiall.png
layout: provider
modified: '2026-09-18'
name: Axiall
nav: Providers
network: true
overview: Axiall is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Chemicals, Manufacturing, Building Products, Chlor-Alkali, and PVC.
press:
- date: ''
  title: PPG and Georgia Gulf merger complete - Lake Charles
  url: https://www.kplctv.com/story/20718704/ppg-georgia-gulf-merger-nearly-complete/
- date: ''
  title: Axiall, Lotte Announce $3 Billion In Louisiana Chemical ...
  url: https://www.opportunitylouisiana.gov/news/axiall-lotte-announce-3-billion-in-louisiana-chemical-projects
- date: ''
  title: Axiall Corporation Adds Three Directors to Board | MarketScreener
  url: https://www.marketscreener.com/news/latest/Axiall-Corporation-Adds-Three-Directors-to-Board-15977336/
- date: ''
  title: 'Update: Chlorine leak at Proctor chemical plant investigated'
  url: https://www.wtap.com/content/news/Axiall-releases-statement-Chlorine-leak-sends-two-people-to-hospital--391494151.html
- date: ''
  title: Westlake Acquires Epoxy Business | News
  url: https://www.clearygottlieb.com/news-and-insights/news-listing/westlakes-acquisition-of-hexions-global-epoxy-business
random_paper: 19
security:
- kind: domain-security
  name: Axiall Domain Security
  slug: axiall-domain-security
  summary_line: DMARC
slug: axiall
tags:
- Chemicals
- Manufacturing
- Building Products
- Chlor-Alkali
- PVC
- Vinyls
- Defunct
- Acquired
---
