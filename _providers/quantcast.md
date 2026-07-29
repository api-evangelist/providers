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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
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
  score: 9.0
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: 'The Quantcast Platform GraphQL API (v2) is the primary programmatic interface to the Quantcast advertising platform. It exposes queries and mutations for reporting, campaign and line item management, '
  name: Quantcast Platform GraphQL API
  slug: quantcast-platform-graphql-api
- description: The Quantcast Conversion API is a server-to-server integration that augments the browser-side Quantcast Live Tag. It accepts a JSON array of conversion events containing a conversion descriptor, a use
  name: Quantcast Conversion API
  slug: quantcast-conversion-api
- description: 'Quantcast Measure is the company''s free audience measurement product. Publishers and advertisers integrate the Quantcast Live Tag (Q Pixel) on web properties, or the Measure SDKs on iOS, Android, and '
  name: Quantcast Measure (Live Tag)
  slug: quantcast-measure-tag
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quantcast-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.quantcast.com
- group: other
  title: ''
  type: Platform
  url: https://www.quantcast.com/platform/
- group: other
  title: ''
  type: Measure
  url: https://www.quantcast.com/measure/
- group: other
  title: ''
  type: Developers
  url: https://developers.quantcast.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.quantcast.com/docs/graphql-api
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.quantcast.com
- group: auth
  title: ''
  type: Authentication
  url: https://developers.quantcast.com/docs/get-started/authentication/
- group: other
  title: ''
  type: Company
  url: https://www.quantcast.com/company/
- group: company
  title: ''
  type: Press
  url: https://www.quantcast.com/press/
- group: company
  title: ''
  type: Blog
  url: https://www.quantcast.com/blog/
- group: company
  title: ''
  type: Careers
  url: https://www.quantcast.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.quantcast.com/contact/
- group: commercial
  title: ''
  type: Privacy
  url: https://www.quantcast.com/privacy/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/quantcast
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quantcast
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/quantcast
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/Quantcast
- group: other
  title: ''
  type: Acquisition
  url: https://www.quantcast.com/press-release/inmobi-acquires-quantcast-choice-to-enhance-frictionless-consent-management-for-publishers/
created: '2026-05-25'
description: Quantcast is a San Francisco-headquartered digital advertising and audience intelligence company founded in 2006. Its flagship offering is the Quantcast Platform, an AI-driven demand-side platform (DSP) for programmatic display, video, CTV, audio, mobile, and native advertising, powered by the company's proprietary Audience Graph and Ara AI engine. Quantcast also operates Quantcast Measure, a free audience measurement product that has tagged millions of digital properties to produce demographic, psychographic, and cross-device audience insights. For programmatic access, Quantcast exposes a developer portal at developers.quantcast.com built around a GraphQL API (v2) for reporting, campaign management, and audience operations on the Quantcast Platform, secured via OAuth 2.0 client credentials. A server-to-server Conversion API augments the browser-side Live Tag for offline and signal-loss-resilient conversion tracking. Quantcast Choice, the company's IAB TCF v2-compliant Consent
  Management Platform, was acquired by InMobi in August 2023 and is now operated as part of InMobi CMP; legacy Quantcast Choice mobile SDKs remain published under the quantcast GitHub organization for reference. Quantcast also open-sources the Quantcast File System (QFS), a C++ distributed file system, and mobile/Roku measurement SDKs.
graphqls:
- description: 'The Quantcast Platform GraphQL API (v2) is the primary programmatic interface to the Quantcast advertising platform. It exposes queries and mutations for reporting, campaign and line item management, '
  name: Quantcast GraphQL API
  slug: quantcast-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quantcast.png
layout: provider
modified: '2026-05-25'
name: Quantcast
nav: Providers
network: true
overview: 'Quantcast publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, AdTech, Programmatic Advertising, Demand-Side Platform, and DSP.


  Quantcast''s developer surface includes documentation, authentication, engineering blog, privacy policy, GitHub presence, YouTube channel, and 13 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 14.5
  delta: -2.3
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 16.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quantcast/refs/heads/main/screenshots/quantcast-2026-06-20T192410.png
security:
- kind: domain-security
  name: Quantcast Domain Security
  slug: quantcast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: quantcast
tags:
- Advertising
- AdTech
- Programmatic Advertising
- Demand-Side Platform
- DSP
- Audience Measurement
- Audience Intelligence
- Consent Management
- CMP
- Privacy
- GraphQL
- Conversion Tracking
- CTV
- Video Advertising
- Display Advertising
- Artificial Intelligence
- Audience Graph
website: https://www.quantcast.com
---
