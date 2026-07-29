---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.8
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Live audience and traffic data updated every three seconds — top pages, referrers, geographies, engaged time, loyalty, and live concurrent visitors — the data behind the Real-Time Dashboard. HTTP GET,
  name: Chartbeat Real-Time API
  slug: chartbeat-real-time-api
- description: Summary historical traffic data for a site over custom date ranges, via an asynchronous submit / status / results job model. Supports one-time and recurring queries with configurable metrics, dimensio
  name: Chartbeat Historical API (Advanced Queries)
  slug: chartbeat-historical-api-advanced-queries
- description: Programmatic access to headline testing data — raw variant-level data, summary reports, and variant reports for headline tests run over a custom time range.
  name: Chartbeat Headline Testing API
  slug: chartbeat-headline-testing-api
- description: Retrieve the top articles that drove a given conversion event for a specified host and date range, with counts attributed per path.
  name: Chartbeat Conversion API
  slug: chartbeat-conversion-api
- description: Programmatic access to Chartbeat Data Lab datasets for deeper custom analysis of audience and content performance.
  name: Chartbeat Data Lab API
  slug: chartbeat-data-lab-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://chartbeat.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.chartbeat.com/cbp
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chartbeat.com/cbp
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chartbeat.com/cbp/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.chartbeat.com/cbp/api/real-time-apis/getting-started-with-our-real-time-api
- group: other
  title: ''
  type: APIExplorer
  url: https://chartbeat.com/docs/api/explore/
- group: operate
  title: ''
  type: Support
  url: https://help.chartbeat.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.chartbeat.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chartbeat.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chartbeat-labs
- group: commercial
  title: ''
  type: Pricing
  url: https://chartbeat.com/product/chartbeat-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://chartbeat.com/signin/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chartbeat.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chartbeat.com/privacy/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.chartbeat.com/llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/chartbeat-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chartbeat-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chartbeat-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chartbeat-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/chartbeat-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/chartbeat-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chartbeat-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/chartbeat-well-known.yml
created: '2026-07-17'
description: 'Chartbeat is a real-time content analytics and audience-engagement platform built for digital publishers, media brands, and editorial teams. It measures how audiences read, watch, and engage with content the moment it is published, reporting live traffic, engaged time, loyalty, video engagement, and headline performance. Beyond its dashboards, Chartbeat exposes public HTTP APIs: a Real-Time API for live traffic and video data updated every three seconds, a Historical (Advanced Queries) API for summary traffic reporting, and Headline Testing, Conversion, and Data Lab APIs, plus JavaScript, iOS, Android, and React Native tracking SDKs for data collection. Authentication is via an account API key sent in the X-CB-AK header.'
image: https://chartbeat.com/wp-content/uploads/2024/04/Chartbeat-logo-Navy-300ppi@2x.png
layout: provider
modified: '2026-07-18'
name: Chartbeat
nav: Providers
network: true
overview: 'Chartbeat publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SaaS, Analytics, Content Analytics, and Real-Time Analytics.


  Chartbeat''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 73
rate_limits:
- limit_count: 0
  name: Chartbeat Rate Limits
  slug: chartbeat-rate-limits
score:
  band: thin
  composite: 32.7
  delta: -0.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 92.6
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chartbeat/refs/heads/main/screenshots/chartbeat-2026-07-25T205108.png
security:
- kind: authentication
  name: Chartbeat Authentication
  slug: chartbeat-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Chartbeat Domain Security
  slug: chartbeat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chartbeat
tags:
- Company
- SaaS
- Analytics
- Content Analytics
- Real-Time Analytics
- Audience Engagement
- Publishing
- Media
- Web Analytics
- Video Analytics
website: https://chartbeat.com/
---
