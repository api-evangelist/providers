---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: Access Bloomberg TV and Radio content including video clips, interview segments, market coverage segments, and audio content for licensed distribution to enterprise clients and media partners.
  name: Bloomberg Media Content API
  slug: bloomberg-media-content-api
- description: Embed or access Bloomberg TV live stream for licensed digital distribution on websites, apps, and digital platforms. Includes live market coverage, news programming, and special event coverage.
  name: Bloomberg Live Streaming API
  slug: bloomberg-live-stream
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-television-and-radio-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bloomberg.com/media-distribution/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
created: '2024-01-01'
description: Bloomberg Television is a 24-hour global business and financial news television network, while Bloomberg Radio provides all-news financial radio coverage. Bloomberg TV and Radio deliver breaking market news, interviews with business leaders, economic analysis, and market commentary. Content is distributed via cable, satellite, streaming, and digital platforms globally.
features:
- description: Round-the-clock global financial and business news coverage.
  name: 24/7 Financial News
- description: Live coverage of major market open and close events.
  name: Market Open and Close Coverage
- description: In-depth interviews with business leaders, economists, and policymakers.
  name: Executive Interviews
- description: All-news audio coverage for on-the-go financial news consumption.
  name: Bloomberg Radio
- description: Access archived Bloomberg TV segments and interviews on demand.
  name: On-Demand Content
- description: Regional Bloomberg TV channels covering Asia, Europe, and US markets.
  name: International Coverage
finops:
- name: Bloomberg Television And Radio Finops
  service_category: API
  slug: bloomberg-television-and-radio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-television-and-radio.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Television and Radio
nav: Providers
network: true
overview: 'Bloomberg Television and Radio publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Television, Radio, Financial News, Media, and Streaming.


  Bloomberg Television and Radio''s developer surface includes developer portal, documentation, support, and 3 more developer resources.'
plans:
- name: Bloomberg Television And Radio Plans Pricing
  plan_count: 3
  slug: bloomberg-television-and-radio-plans-pricing
random_paper: 112
rate_limits:
- limit_count: 5
  name: Bloomberg Television And Radio Rate Limits
  slug: bloomberg-television-and-radio-rate-limits
score:
  band: emerging
  composite: 27.4
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 27.4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-television-and-radio/refs/heads/main/screenshots/bloomberg-television-and-radio-2026-07-25T203405.png
security:
- kind: domain-security
  name: Bloomberg Television And Radio Domain Security
  slug: bloomberg-television-and-radio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-television-and-radio
tags:
- Television
- Radio
- Financial News
- Media
- Streaming
- Bloomberg TV
- Bloomberg Radio
use_cases:
- description: Monitor financial markets and breaking news through live TV coverage.
  name: Market Monitoring
- description: Distribute Bloomberg TV to trading floors and enterprise environments.
  name: Enterprise TV Integration
- description: License Bloomberg TV content for redistribution on third-party platforms.
  name: Content Licensing
- description: Access Bloomberg TV content archives for media and financial research.
  name: Media Research
website: https://www.bloomberg.com/professional/
---
