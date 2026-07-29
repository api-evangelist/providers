---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Xiaoe's Open API (开放API) for integrating store data and operations — users, products, orders, refunds, live broadcasts, learning/course data, marketing (coupons, group-buy, promoters) and points — int
  name: Xiaoe Open API
  slug: xiaoe-open-api
artifact_total: 5
asyncapis:
- description: ''
  name: Sem Message Push Webhooks
  slug: sem-message-push-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.xiaoe-tech.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.xiaoe-tech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-doc.xiaoe-tech.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-doc.xiaoe-tech.com/api_list.html
- group: start
  title: ''
  type: GettingStarted
  url: https://api-doc.xiaoe-tech.com/read_before/access_guide.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://api-doc.xiaoe-tech.com/log.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sem-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sem-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sem-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sem-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sem-message-push-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/sem-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sem-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sem-rate-limits.yml
created: '2026-07-17'
description: Xiaoe (小鹅通), operated by Shenzhen Xiaoe Network Technology Co., Ltd., is a Chinese private-domain (私域) marketing and content-commerce SaaS platform that helps businesses convert public-channel audiences into owned WeChat-based channels. Its product suite spans knowledge/course delivery, live-streaming e-commerce, a mini-program mall, enterprise SCRM, training academies, community circles, points/loyalty, and promoter (affiliate) programs across 20+ industries. Xiaoe exposes an Open API (开放API) at api.xiaoe-tech.com covering users, products, orders, payments, live broadcasts, learning data, marketing and points, using access_token authentication, a code/msg/data response envelope, and an encrypted message-push (webhook) event system. The "sem" subdomain is Xiaoe's search-marketing landing surface; the company was surfaced as a portfolio company of Qiming Venture Partners.
image: https://www.xiaoe-tech.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: Xiaoe (小鹅通)
nav: Providers
network: true
overview: 'Xiaoe (小鹅通) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SaaS, Private Domain, Content Commerce, and Live Streaming.


  The Xiaoe (小鹅通) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Xiaoe (小鹅通)''s developer surface includes documentation, API reference, getting-started guide, changelog, authentication, and 10 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 1
  name: Sem Rate Limits
  slug: sem-rate-limits
score:
  band: thin
  composite: 36.0
  delta: 4.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.6
    developer_ergonomics: 52.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 31.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Sem Authentication
  slug: sem-authentication
  summary_line: access_token · 0 schemes
- kind: domain-security
  name: Sem Domain Security
  slug: sem-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sem
tags:
- Company
- SaaS
- Private Domain
- Content Commerce
- Live Streaming
- Education
- E-Commerce
- Marketing
- WeChat
- China
website: https://www.xiaoe-tech.com
---
