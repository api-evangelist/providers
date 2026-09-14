---
api_count: 0
artifact_total: 1
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/4info
- group: auth
  title: ''
  type: DomainSecurity
  url: security/4info-domain-security.yml
coverage:
  checked: '2026-09-05'
  detail: 4INFO was fully absorbed into Cadent in January 2020 and its domain is now mail-only — 4info.com and www.4info.com publish no A or AAAA record at all, so every HTTP and /.well-known probe fails at DNS resolution rather than returning a page, and the last Internet Archive capture of the site (2023-02) is followed by a 404.
  evidence:
  - status: 0
    url: https://4info.com/
  - status: 0
    url: https://www.4info.com/
  - status: 0
    url: https://4info.com/.well-known/api-catalog
  - status: 404
    url: https://web.archive.org/web/20230528013343/https://4INFO.com/
  - status: 200
    url: https://apitracker.io/a/4info
  - status: 200
    url: https://github.com/4info
  reason: defunct
  state: none
created: '2026-09-05'
description: '4INFO, Inc. was a San Mateo (originally Palo Alto) California advertising-technology company founded in 2004 by Pankaj Shah and Zaw Thet. It began as an SMS content and alerting service — Nielsen called it the largest business-to-consumer SMS content provider in North America in 2008 — then pivoted in 2010 into mobile display advertising with the AdHaven platform, a mobile ad server, audience data-management and analytics stack sold to publishers, aggregators and national advertisers. Its later product was an identity graph: patented technology ("Systems and methods for statistically associating mobile devices to households") that statistically resolved mobile devices, set-top boxes and connected TVs back to a single household so brands could target and measure across screens. mBlox bought the legacy SMS business in 2015, and Cadent acquired the remaining company in January 2020, folding the identity and cross-screen targeting technology into Cadent''s advanced-TV platform.
  4INFO no longer operates as an independent company: 4info.com is retained for email only and publishes no A or AAAA record, so there is no website, developer portal, API reference or machine-readable contract of any kind on any 4Info host, live or archived.'
layout: provider
modified: '2026-09-05'
name: 4Info
nav: Providers
network: true
overview: 4Info is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Mobile Advertising, and Advanced TV.
random_paper: 18
security:
- kind: domain-security
  name: 4Info Domain Security
  slug: 4info-domain-security
  summary_line: no transport/DNS hardening detected
slug: 4info
tags:
- Company
- Advertising
- AdTech
- Mobile Advertising
- Advanced TV
- Identity Resolution
- Audience Targeting
- Data
- Acquired
- Defunct
---
