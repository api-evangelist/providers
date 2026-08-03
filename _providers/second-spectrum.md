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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: Customer-facing platform delivering Second Spectrum tracking data, visualizations, and clips to club analysts and coaching staff. Access is gated by Auth0-backed login under the Genius Sports Performa
  name: Performance Studio
  slug: performance-studio
- description: Skeletal and optical tracking data feed produced from in-venue computer vision systems for football and basketball. Delivered to leagues, clubs, and broadcasters under enterprise agreement; the Premie
  name: Second Spectrum Tracking Data
  slug: tracking-data
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/second-spectrum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.secondspectrum.com/
- group: other
  title: Genius Sports (parent company)
  type: Parent
  url: https://geniussports.com/
- group: start
  title: ''
  type: Portal
  url: https://performancestudio.geniussports.com/
- group: company
  title: ''
  type: Newsroom
  url: https://geniussports.com/news/
- group: company
  title: ''
  type: Careers
  url: https://geniussports.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/second-spectrum
- group: operate
  title: ''
  type: Contact
  url: https://geniussports.com/contact-us/
created: '2026-05-23'
description: Second Spectrum is a Los Angeles–based computer vision and AI sports tracking company, acquired by Genius Sports in 2021 for roughly $200M. It supplies skeletal and optical tracking, machine-learning analytics, and augmented broadcast products to major leagues, clubs, and broadcasters — most notably the NBA (official tracking partner from 2017 to 2023), the Premier League (official tracking partner via Football DataCo), and MLS. The customer-facing offering is the Performance Studio platform, used by club analysts and coaching staff to access tracking data, visualizations, and tagged clips. There is no public developer portal, no published OpenAPI, and no self-serve API keys; data and integration access are delivered exclusively under enterprise agreement with Genius Sports. The product surface is effectively a sales-led, league/club-tier offering rather than a developer API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/second-spectrum.png
layout: provider
modified: '2026-05-25'
name: Second Spectrum (Genius Sports)
nav: Providers
network: true
overview: 'Second Spectrum (Genius Sports) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Sports Tracking, Computer Vision, AI, Broadcast, and NBA.


  Second Spectrum (Genius Sports)''s developer surface includes developer portal and 7 more developer resources.'
random_paper: 44
score:
  band: minimal
  composite: 8.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/second-spectrum/refs/heads/main/screenshots/second-spectrum-2026-06-20T193622.png
security:
- kind: domain-security
  name: Second Spectrum Domain Security
  slug: second-spectrum-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: second-spectrum
tags:
- Sports Tracking
- Computer Vision
- AI
- Broadcast
- NBA
- Premier League
- Genius Sports
- Performance Studio
- Skeletal Tracking
- Optical Tracking
- Augmented Broadcast
website: https://www.secondspectrum.com/
---
