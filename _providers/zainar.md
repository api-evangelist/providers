---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- description: Private, credential-gated REST API for the ZaiNar Wi-Fi location cloud. Clients authenticate with a username/password to obtain a bearer token, then trigger and manage locates against tracker and anch
  name: ZaiNar Location Platform API
  slug: zainar-location-platform-api
artifact_total: 4
asyncapis:
- description: ''
  name: Zainar Event Surface
  slug: zainar-event-surface
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/zainar/locate-latency-measurement-script/issues
- group: company
  title: ''
  type: Website
  url: https://zainartech.com/
- group: company
  title: ''
  type: Blog
  url: https://zainartech.com/news
- group: operate
  title: ''
  type: Support
  url: https://zps.support.zainartech.com/servicedesk/customer/portals
- group: operate
  title: ''
  type: Contact
  url: https://zainartech.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zainar
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zainar
- group: company
  title: ''
  type: Twitter
  url: https://x.com/zainartech
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/zainar_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/zainar-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zainar-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zainar-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zainar-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zainar-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/zainar-packages.yml
- group: other
  title: ''
  type: StreamingEndpoint
  url: asyncapi/zainar-event-surface.yml
created: '2026-08-02'
description: ZaiNar is a Positioning, Navigation and Timing (PNT) company that turns existing wireless networks into a sensing system. Its patented digital signal processing achieves sub-nanosecond time synchronization across commodity radios, which yields sub-meter 3D positioning for any device that emits a radio signal — indoors, outdoors, through walls and around corners — with no reliance on GPS/GNSS, cameras or additional device power. ZaiNar works across frequencies and known wireless protocols (Wi-Fi, 5G/SRS, IoT radios) and is deployed today in healthcare equipment tracking, construction site and safety-zone monitoring, and coordinated autonomous operations. The company emerged from nine years of stealth in February 2026 with more than $100M raised and a $1B+ valuation, and opened a Tokyo office in April 2026. Location data is delivered to customers through a private, credential-gated REST and real-time WebSocket platform; ZaiNar publishes no public developer portal, OpenAPI definition
  or SDKs as of this profiling pass.
image: https://zainartech.com/zainar-logo.png
layout: provider
modified: '2026-08-02'
name: ZaiNar
nav: Providers
network: true
overview: 'ZaiNar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Location, Positioning, Navigation, and Timing.


  The ZaiNar catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ZaiNar''s developer surface includes engineering blog, support, authentication, and 13 more developer resources.'
random_paper: 15
screenshot: https://raw.githubusercontent.com/api-evangelist/zainar/refs/heads/main/screenshots/zainar-2026-09-02T171438.png
security:
- kind: authentication
  name: Zainar Authentication
  slug: zainar-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Zainar Domain Security
  slug: zainar-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: zainar
tags:
- Company
- Location
- Positioning
- Navigation
- Timing
- Wireless
- Real-Time Location
- Asset Tracking
- IoT
- Physical AI
website: https://zainartech.com/
---
