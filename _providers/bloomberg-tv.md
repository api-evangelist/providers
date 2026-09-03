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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: Access Bloomberg TV video content, live stream, and on-demand clips for licensed distribution. Provides access to market coverage segments, interviews, and editorial content for enterprise and media p
  name: Bloomberg TV Content API
  slug: bloomberg-tv-api
- description: Embed Bloomberg TV live stream and video clips on licensed digital properties using Bloomberg's embed API. Supports customizable player integration for websites, apps, and digital publishing platforms
  name: Bloomberg TV Embed API
  slug: bloomberg-tv-embed
artifact_total: 16
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/bloomberg/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-tv-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bloombergtelevision
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bloomberg.com/live/
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
description: Bloomberg TV is a 24-hour global business and financial news television network delivering real-time market coverage, business news, executive interviews, and economic analysis. Bloomberg TV reaches a global audience through cable, satellite, digital streaming, and over-the-top (OTT) platforms. The network provides live market open and close coverage, special event programming, and on-demand content access.
features:
- description: Round-the-clock live financial news and market coverage.
  name: 24/7 Live Coverage
- description: Special programming covering US and international market open and close events.
  name: Market Open and Close
- description: In-depth interviews with C-suite executives, policymakers, and economists.
  name: Executive Interviews
- description: Access Bloomberg TV segments and interviews on demand.
  name: On-Demand Video
- description: Bloomberg TV channels covering Asia, Europe, Middle East, and Americas.
  name: Multi-Region Coverage
- description: OTT and digital streaming via Bloomberg.com, app, and partner platforms.
  name: Digital Streaming
finops:
- name: Bloomberg Tv Finops
  service_category: API
  slug: bloomberg-tv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-tv.png
layout: provider
modified: '2026-08-27'
name: Bloomberg TV
nav: Providers
network: true
overview: 'Bloomberg TV publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Bloomberg TV, Television, Financial News, Media, and Streaming.


  Bloomberg TV''s developer surface includes developer portal, documentation, support, and 5 more developer resources.'
plans:
- name: Bloomberg Tv Plans Pricing
  plan_count: 3
  slug: bloomberg-tv-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Bloomberg Tv Rate Limits
  slug: bloomberg-tv-rate-limits
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 20.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-tv/refs/heads/main/screenshots/bloomberg-tv-2026-07-25T203405.png
security:
- kind: domain-security
  name: Bloomberg Tv Domain Security
  slug: bloomberg-tv-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-tv
tags:
- Bloomberg TV
- Television
- Financial News
- Media
- Streaming
- Live Coverage
- Bloomberg
use_cases:
- description: Display Bloomberg TV live on trading floor screens for market monitoring.
  name: Trading Floor Displays
- description: Embed Bloomberg TV content on licensed financial news websites.
  name: Digital Publishing
- description: Deploy Bloomberg TV to corporate offices and financial institutions.
  name: Enterprise Deployment
- description: Monitor Bloomberg TV coverage for media analysis and research.
  name: Research and Media Monitoring
website: https://www.bloomberg.com/professional/
---
