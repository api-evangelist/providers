---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Live Nation Entertainment Agentic Access
  operation_count: 7
  slug: live-nation-entertainment-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://app.ticketmaster.com/discovery/v2
  baseurl_source: declared
  description: Search and retrieve attraction information.
  name: live-nation-entertainment Attractions API
  slug: live-nation-entertainment-attractions-api
- baseURL: https://app.ticketmaster.com/discovery/v2
  baseurl_source: declared
  description: Search and retrieve classification/genre information.
  name: live-nation-entertainment Classifications API
  slug: live-nation-entertainment-classifications-api
- baseURL: https://app.ticketmaster.com/discovery/v2
  baseurl_source: declared
  description: Search and retrieve event information.
  name: live-nation-entertainment Events API
  slug: live-nation-entertainment-events-api
- baseURL: https://app.ticketmaster.com/discovery/v2
  baseurl_source: declared
  description: Search and retrieve venue information.
  name: live-nation-entertainment Venues API
  slug: live-nation-entertainment-venues-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ticketmaster Discovery Attractions API
  slug: open-live-nation-entertainment-attractions-api
- collection_type: open
  name: Ticketmaster Discovery Attractions Classifications API
  slug: open-live-nation-entertainment-classifications-api
- collection_type: open
  name: Ticketmaster Discovery Attractions Events API
  slug: open-live-nation-entertainment-events-api
- collection_type: open
  name: Ticketmaster Discovery API
  slug: open-live-nation-entertainment-ticketmaster-discovery-api
- collection_type: open
  name: Ticketmaster Discovery Attractions Venues API
  slug: open-live-nation-entertainment-venues-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/live-nation-entertainment-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/live-nation-entertainment-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/live-nation-entertainment-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ticketmaster
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/live-nation
- group: company
  title: ''
  type: Blog
  url: https://newsroom.livenation.com/feed
description: Tap into the Ticketmaster open developer network which gives you the flexibility and scale to bring unforgettable live events to fans. It’s our technology – ...
finops:
- name: Live Nation Entertainment Finops
  service_category: Ticketing / Events
  slug: live-nation-entertainment-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/live-nation-entertainment.png
layout: provider
modified: '2026-05-19'
name: Live Nation Entertainment
nav: Providers
network: true
overview: 'Live Nation Entertainment publishes 4 APIs on the [APIs.io](https://apis.io/) network, including live-nation-entertainment Attractions API, live-nation-entertainment Classifications API, live-nation-entertainment Events API, and 1 more. Tagged areas include Fortune 500.


  Live Nation Entertainment''s developer surface includes authentication, engineering blog, and 4 more developer resources.'
plans:
- name: Live Nation Entertainment Plans Pricing
  plan_count: 3
  slug: live-nation-entertainment-plans-pricing
press:
- date: '2026-05-25'
  title: Live Nation Entertainment, Inc. (LYV) Presents at J.P. ...
  url: https://seekingalpha.com/article/4907113-live-nation-entertainment-inc-lyv-presents-at-j-p-morgan-54th-annual-global-technology-media
- date: '2026-05-25'
  title: Live Nation Entertainment Q1 Earnings Call Highlights
  url: https://www.theglobeandmail.com/investing/markets/stocks/LYV/pressreleases/1873250/live-nation-entertainment-q1-earnings-call-highlights/
- date: '2026-05-25'
  title: Live Nation Entertainment, Inc. Stock (LYV) - Quote Nyse
  url: https://www.marketscreener.com/quote/stock/LIVE-NATION-ENTERTAINMENT-13449/
- date: '2026-05-25'
  title: LIVE NATION ENTERTAINMENT FULL YEAR AND ...
  url: https://www.prnewswire.com/news-releases/live-nation-entertainment-full-year-and-fourth-quarter-2025-results-302693023.html
- date: '2026-05-25'
  title: Live Nation Entertainment Full Year And Fourth Quarter ...
  url: https://newsroom.livenation.com/news/live-nation-entertainment-full-year-and-fourth-quarter-2025-results/
random_paper: 15
rate_limits:
- limit_count: 2
  name: Live Nation Entertainment Rate Limits
  slug: live-nation-entertainment-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/live-nation-entertainment/refs/heads/main/screenshots/live-nation-entertainment-2026-06-20T184616.png
security:
- kind: authentication
  name: Live Nation Entertainment Authentication
  slug: live-nation-entertainment-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Live Nation Entertainment Domain Security
  slug: live-nation-entertainment-domain-security
  summary_line: TLSv1.2 · DMARC
slug: live-nation-entertainment
tags:
- Fortune 500
---
