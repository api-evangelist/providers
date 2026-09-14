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
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commission-of-fine-arts-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/commission-of-fine-arts-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cfa.gov/vulnerability-disclosure-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/commission-of-fine-arts-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/commission-of-fine-arts-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/commission-of-fine-arts-rate-limits.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/u-s-commission-of-fine-arts
- group: company
  title: ''
  type: Website
  url: https://www.cfa.gov
- group: other
  title: ''
  type: ProjectSearch
  url: https://www.cfa.gov/records-research/project-search
- group: other
  title: ''
  type: RecordsResearch
  url: https://www.cfa.gov/records-research
- group: other
  title: ''
  type: MeetingsAndAgendas
  url: https://www.cfa.gov/upcoming-meetings
- group: other
  title: ''
  type: OldGeorgetownBoard
  url: https://www.cfa.gov/project-review/old-georgetown
- group: other
  title: ''
  type: AccessingRecords
  url: https://www.cfa.gov/records-research/accessing-our-records
- group: operate
  title: ''
  type: ContactUs
  url: https://www.cfa.gov/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cfa.gov/website-policies
- group: company
  title: ''
  type: Blog
  url: https://www.cfa.gov/about-cfa/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.cfa.gov/rss/blog.xml
coverage:
  checked: '2026-09-05'
  detail: The CFA runs one Drupal 10 site whose ~19,500 project records are served only as HTML through a Search API view — /jsonapi, /api, /openapi.json, /data.json and /llms.txt all 404, no api./data./developer. subdomain resolves in DNS, and the agency has no developer portal, SDK or webhook surface of any kind.
  evidence:
  - status: 404
    url: https://www.cfa.gov/jsonapi
  - status: 404
    url: https://www.cfa.gov/openapi.json
  - status: 404
    url: https://www.cfa.gov/developer
  - status: 404
    url: https://www.cfa.gov/.well-known/api-catalog
  - status: 200
    url: https://www.cfa.gov/records-research/project-search
  reason: no-developer-program
  state: none
created: '2024-12-03'
description: The U.S. Commission of Fine Arts (CFA) is an independent federal agency established in 1910 that has review authority over the design and aesthetics of construction within Washington, D.C., and over coins, medals, and Federal commemorative works. The CFA also appoints the Old Georgetown Board which conducts design review for projects in the Georgetown Historic District. As of September 2026 the CFA publishes no public developer API, no OpenAPI specification and no developer program. Its roughly 19,500 project records are reachable only through a server-rendered Drupal Search API view at cfa.gov/records-research/project-search and through the records-and-research request process. The only machine-readable surfaces the agency serves are a sitemap.xml, a robots.txt and three RSS 2.0 feeds (blog, news, meetings). The CFA does publish a CISA-aligned Vulnerability Disclosure Policy with a security@cfa.gov contact and stated 3/7/90-day response targets.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/commission-of-fine-arts.png
layout: provider
modified: '2026-09-05'
name: Commission of Fine Arts
nav: Providers
network: true
overview: 'Commission of Fine Arts is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Architecture, Arts, Design Review, Federal-Government, and Washington DC.


  Commission of Fine Arts'' developer surface includes engineering blog and 16 more developer resources.'
plans:
- name: Commission Of Fine Arts Plans Pricing
  plan_count: 0
  slug: commission-of-fine-arts-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Commission Of Fine Arts Rate Limits
  slug: commission-of-fine-arts-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/commission-of-fine-arts/refs/heads/main/screenshots/commission-of-fine-arts-2026-06-20T174817.png
security:
- kind: domain-security
  name: Commission Of Fine Arts Domain Security
  slug: commission-of-fine-arts-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Commission Of Fine Arts Vulnerability Disclosure
  slug: commission-of-fine-arts-vulnerability-disclosure
  summary_line: contact published
slug: commission-of-fine-arts
tags:
- Architecture
- Arts
- Design Review
- Federal-Government
- Washington DC
website: https://www.cfa.gov
---
