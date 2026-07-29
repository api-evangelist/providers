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
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Carrier-grade SMS API for sending and receiving A2P and P2A SMS at scale on the Rakuten Mobile network, with delivery receipts pushed to caller-configured webhooks. UTF-8 encoded, JWT-authenticated RE
  name: Rakuten CPaaS SMS / Messaging API
  slug: rakuten-cpaas-sms-api
- description: One-time PIN delivery and verification API for two-factor authentication and transaction confirmation, with SMS and Voice channel support, lifecycle operations for request / validate / resend / cancel
  name: Rakuten CPaaS Confirm (OTP) API
  slug: rakuten-cpaas-confirm-api
- description: Link shortening and analytics API for CPaaS campaigns. Supports create / retrieve / update / list / delete operations on short URLs, with JWT bearer authentication, UTC timestamps, JSON over HTTPS, an
  name: Rakuten CPaaS Short URL API
  slug: rakuten-cpaas-shorturl-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rakuten-mobile-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rakuten-mobile-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://network.mobile.rakuten.co.jp/
- group: company
  title: ''
  type: Website
  url: https://corp.mobile.rakuten.co.jp/
- group: other
  title: ''
  type: Symphony
  url: https://symphony.rakuten.com/
- group: other
  title: ''
  type: SymworldPlatform
  url: https://symphony.rakuten.com/symworld/a-new-kind-of-operating-platform
- group: other
  title: ''
  type: OpenRAN
  url: https://symphony.rakuten.com/open-ran
- group: other
  title: ''
  type: Cloud
  url: https://symphony.rakuten.com/cloud
- group: other
  title: ''
  type: OSS
  url: https://symphony.rakuten.com/oss
- group: other
  title: ''
  type: SiteManagement
  url: https://symphony.rakuten.com/site-management
- group: other
  title: ''
  type: CPaaS
  url: https://symphony.rakuten.com/cpaas/en
- group: docs
  title: ''
  type: DeveloperDocs
  url: https://docs.cpaas.symphony.rakuten.net/
- group: start
  title: ''
  type: Portal
  url: https://portal.cpaas.symphony.rakuten.net/
- group: other
  title: ''
  type: Symworld
  url: https://symworld.rakuten.com/
- group: company
  title: ''
  type: Newsroom
  url: https://symphony.rakuten.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://symphony.rakuten.com/blog
- group: other
  title: ''
  type: ParentCompany
  url: https://global.rakuten.com/corp/
- group: company
  title: ''
  type: GroupNewsroom
  url: https://global.rakuten.com/corp/news/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rakuten-mobile/
- group: company
  title: ''
  type: LinkedInSymphony
  url: https://www.linkedin.com/company/rakuten-symphony/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@RakutenMobile
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/RakutenMobile_R
- group: company
  title: ''
  type: TwitterSymphony
  url: https://twitter.com/RakutenSymphony
created: '2026-05-25'
description: Rakuten Mobile is the Japanese mobile network operator (MNO) of Rakuten Group, headquartered in Setagaya, Tokyo, and Japan's fourth nationwide carrier alongside NTT Docomo, KDDI, and SoftBank. Commercially launched in April 2020 and surpassing 10 million subscribers in December 2025, Rakuten Mobile built and operates the world's first fully cloud-native, end-to-end virtualized mobile network on Open RAN, with 4G population coverage of 99.9% and expanding 5G plus 700 MHz Platinum Band rollout. The same engineering effort spun out into Rakuten Symphony, a B2B business that productizes the Rakuten Mobile playbook as the Symworld platform — a cloud-native operating platform for telcos covering Open RAN (CU/DU/RIC, Symware distributed unit appliance), Symworld Cloud (Kubernetes-based hyperconverged telco cloud / CNP), OSS/BSS, site management, and a marketplace of pre-integrated cloud-native network functions from 50+ vendor partners. Symphony also offers Rakuten CPaaS (carrier-grade
  SMS, Confirm/OTP, and Short URL APIs running on the Rakuten Mobile network with JWT-authenticated REST endpoints at api.cpaas.symphony.rakuten.net) and Rakuten Communications Platform (RCP) for enterprise private 5G. Public, developer-accessible APIs are concentrated in the CPaaS suite; the Symworld platform APIs themselves are TM Forum-aligned but exposed under commercial engagement rather than a public developer signup.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rakuten-mobile.png
layout: provider
modified: '2026-05-25'
name: Rakuten Mobile
nav: Providers
network: true
overview: 'Rakuten Mobile publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Mobile Network Operator, Carrier, 5G, and 4G LTE.


  Rakuten Mobile''s developer surface includes developer portal, engineering blog, YouTube channel, and 20 more developer resources.'
random_paper: 53
score:
  band: minimal
  composite: 10.7
  delta: -1.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rakuten-mobile/refs/heads/main/screenshots/rakuten-mobile-2026-06-20T192543.png
security:
- kind: domain-security
  name: Rakuten Mobile Domain Security
  slug: rakuten-mobile-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rakuten Mobile Vulnerability Disclosure
  slug: rakuten-mobile-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: rakuten-mobile
tags:
- Telecommunications
- Mobile Network Operator
- Carrier
- 5G
- 4G LTE
- Open RAN
- Cloud Native
- Symworld
- Symphony
- CPaaS
- SMS
- OTP
- Short URL
- Messaging
- OSS
- BSS
- RIC
- Kubernetes
- Edge
- Private 5G
- Japan
website: https://network.mobile.rakuten.co.jp/
---
