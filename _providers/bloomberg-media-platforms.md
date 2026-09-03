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
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Access Bloomberg's real-time financial news, market reports, and editorial content through Bloomberg's news data feeds. Available to Bloomberg Terminal subscribers and enterprise data license clients.
  name: Bloomberg News API
  slug: bloomberg-news-api
- description: Content distribution API for Bloomberg's editorial content including articles, video clips, and multimedia from Bloomberg.com, Bloomberg Businessweek, and other Bloomberg media properties.
  name: Bloomberg Media API
  slug: bloomberg-media-api
artifact_total: 16
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/bloomberg/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-media-platforms-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BloombergMedia
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bloomberg.com/professional/solution/news/
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
description: Bloomberg Media Platforms encompass Bloomberg's digital news and content distribution channels including Bloomberg.com, Bloomberg Businessweek, Bloomberg Markets, Bloomberg Technology, Bloomberg Opinion, and Bloomberg Quicktake. Bloomberg provides news APIs for distributing financial news, market data updates, and editorial content to institutional clients and media partners.
features:
- description: Real-time financial news and market updates from Bloomberg's newsroom.
  name: Real-Time News
- description: Search and filter Bloomberg news archives by company, topic, and date.
  name: News Search
- description: Original reporting and investigative journalism from Bloomberg journalists.
  name: Exclusive Reporting
- description: Columnist opinions and editorial analysis on financial and economic topics.
  name: Bloomberg Opinion
- description: Digital video and multimedia content for financial news consumption.
  name: Bloomberg Quicktake
- description: In-depth analysis of global financial markets and investment trends.
  name: Bloomberg Markets Magazine
finops:
- name: Bloomberg Media Platforms Finops
  service_category: API
  slug: bloomberg-media-platforms-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-media-platforms.png
layout: provider
modified: '2026-08-27'
name: Bloomberg Media Platforms
nav: Providers
network: true
overview: 'Bloomberg Media Platforms publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Media, News, Financial News, Digital Media, and Bloomberg.com.


  Bloomberg Media Platforms'' developer surface includes developer portal, documentation, support, and 5 more developer resources.'
plans:
- name: Bloomberg Media Platforms Plans Pricing
  plan_count: 3
  slug: bloomberg-media-platforms-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Bloomberg Media Platforms Rate Limits
  slug: bloomberg-media-platforms-rate-limits
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 19.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-media-platforms/refs/heads/main/screenshots/bloomberg-media-platforms-2026-07-25T203403.png
security:
- kind: domain-security
  name: Bloomberg Media Platforms Domain Security
  slug: bloomberg-media-platforms-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-media-platforms
tags:
- Media
- News
- Financial News
- Digital Media
- Bloomberg.com
- Bloomberg Businessweek
- Bloomberg
use_cases:
- description: Monitor breaking financial news and market-moving events in real time.
  name: News Monitoring
- description: Apply NLP to Bloomberg news for financial sentiment analysis.
  name: Sentiment Analysis
- description: Integrate Bloomberg news into research and analytics platforms.
  name: Research Integration
- description: License Bloomberg content for distribution on third-party platforms.
  name: Content Licensing
website: https://www.bloomberg.com/professional/
---
