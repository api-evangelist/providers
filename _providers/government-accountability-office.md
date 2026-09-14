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
- group: company
  title: ''
  type: Website
  url: https://www.gao.gov/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/government-accountability-office-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-government
- group: other
  title: ''
  type: Reports
  url: https://www.gao.gov/reports-testimonies
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gao.gov/copyright
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gao.gov/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.gao.gov/about/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.gao.gov/blog
- group: company
  title: ''
  type: BlogFeeds
  url: https://www.gao.gov/rss/reports.xml
- group: company
  title: ''
  type: Press
  url: https://www.gao.gov/press-center
- group: other
  title: ''
  type: Podcast
  url: https://www.gao.gov/podcast
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/government-accountability-office-llms.txt
coverage:
  checked: '2026-09-12'
  detail: GAO publishes no API and no developer program of any kind — its entire machine-readable public surface is a catalog of ~40 RSS 2.0 feeds, while the Recommendations Database, bid-protest docket and appropriations-law decisions are browser-only search applications whose query strings robots.txt disallows.
  evidence:
  - status: 404
    url: https://www.gao.gov/openapi.json
  - status: 404
    url: https://www.gao.gov/.well-known/api-catalog
  - status: 404
    url: https://www.gao.gov/about/what-gao-does/data-tools
  - status: 200
    url: https://www.gao.gov/rss/reports.xml
  reason: no-developer-program
  state: none
created: '2024-12-25'
description: The Government Accountability Office (GAO) is the United States government's supreme audit institution. It provides Congress with auditing, evaluation, and investigative services, and publishes reports, testimonies, and other products examining federal programs and policies.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/government-accountability-office.png
layout: provider
modified: '2026-09-12'
name: Government Accountability Office
nav: Providers
network: true
overview: 'Government Accountability Office is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Accountability, Auditing, Federal-Government, Government, and United States.


  Government Accountability Office''s developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 5
screenshot: https://raw.githubusercontent.com/api-evangelist/government-accountability-office/refs/heads/main/screenshots/government-accountability-office-2026-06-20T182302.png
security:
- kind: domain-security
  name: Government Accountability Office Domain Security
  slug: government-accountability-office-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: government-accountability-office
tags:
- Accountability
- Auditing
- Federal-Government
- Government
- United States
website: https://www.gao.gov/
---
