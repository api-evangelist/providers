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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Real-time REST API exposing raw mobile app-store data — apps, publishers, parent companies, SDKs, download/revenue/usage estimates, ratings, top charts, and advertising intelligence across iTunes, Goo
  name: Apptopia Data API
  slug: apptopia-data-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://apptopia.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.apptopia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.apptopia.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.apptopia.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/apptopia-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://help.apptopia.com/knowledge
- group: commercial
  title: ''
  type: Pricing
  url: https://apptopia.com/en/pricing-investors/
- group: start
  title: ''
  type: Login
  url: https://apptopia.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apptopia.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apptopia.com/en/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://apptopia.com/en/our-compliance
- group: company
  title: ''
  type: Blog
  url: https://apptopia.com/en/insights/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apptopia
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apptopia-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apptopia-domain-security.yml
created: '2026-07-17'
description: Apptopia is a mobile app market-intelligence company that delivers investor-grade estimates of app downloads, revenue, usage, ratings, SDK adoption, and advertising activity across the iTunes App Store, Google Play, Tencent, Xiaomi, and Mobile 360 stores. Its data is derived from a real-user device panel and is trusted by financial institutions, ad-tech firms, and app publishers to track competitors, size markets, and validate investment theses. The Apptopia Data API exposes the raw dataset behind these estimates as JSON over HTTPS, organized into directory, discovery, time-series, entity-lookup, search, and data-export endpoints, authenticated with JSON Web Tokens.
image: https://apptopia.com/en/wp-content/uploads/2026/04/Group-10-1.png
layout: provider
mcp_servers:
- description: ''
  name: apptopia-mcp.yml
  slug: apptopia-mcpyml
modified: '2026-07-18'
name: Apptopia
nav: Providers
network: true
overview: 'Apptopia publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobile, App Store Intelligence, Market Intelligence, and Alternative Data.


  Apptopia''s developer surface includes documentation, API reference, authentication, support, pricing, engineering blog, and 9 more developer resources.'
random_paper: 46
rate_limits:
- limit_count: 0
  name: Apptopia Rate Limits
  slug: apptopia-rate-limits
score:
  band: emerging
  composite: 28.7
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apptopia/refs/heads/main/screenshots/apptopia-2026-07-25T200850.png
security:
- kind: authentication
  name: Apptopia Authentication
  slug: apptopia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apptopia Domain Security
  slug: apptopia-domain-security
  summary_line: TLSv1.2 · DMARC
slug: apptopia
tags:
- Company
- Mobile
- App Store Intelligence
- Market Intelligence
- Alternative Data
- Analytics
- Consumer Insights
- Advertising
website: https://apptopia.com
---
