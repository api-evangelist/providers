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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'Sunyur''s enterprise procurement open integration platform ("聚贤阁"). Exposes an accessToken-authenticated API base at https://open.sunyur.com/api that connects buyers to mainstream e-commerce platforms '
  name: Sunyur Open Platform
  slug: sunyur-open-platform
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.sunyur.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.sunyur.com
- group: docs
  title: ''
  type: Documentation
  url: https://open.sunyur.com/front/#/docs
- group: auth
  title: ''
  type: Authentication
  url: authentication/sunyur-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sunyur-error-codes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sunyur-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sunyur-well-known.yml
created: '2026-07-17'
description: Sunyur (商越科技 / Beijing Sunyur Network Technology Co., Ltd, 北京商越网络科技有限公司) is a Chinese enterprise procurement digitalization company providing AI-driven procurement solutions for large and medium enterprises. Its products include an intelligent procurement middle-platform (采购中台), an SRM supplier relationship management system, an e-procurement SaaS platform, and a procurement mall (采购商城), helping each customer build a dedicated online, digital, and intelligent enterprise procurement platform to raise efficiency and lower cost. Sunyur operates an open integration platform ("聚贤阁", open.sunyur.com) that connects enterprises to 30+ mainstream e-commerce platforms and 10+ third-party applications through a single accessToken-authenticated API surface. Sunyur is backed by Qiming Venture Partners.
image: https://img.sunyur.com/158313907762748503.png
layout: provider
modified: '2026-07-21'
name: Sunyur
nav: Providers
network: true
overview: 'Sunyur publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Procurement, SRM, E-Procurement, and Supplier Management.


  Sunyur''s developer surface includes documentation, authentication, and 5 more developer resources.'
random_paper: 98
score:
  band: minimal
  composite: 12.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Sunyur Authentication
  slug: sunyur-authentication
  summary_line: accessToken · 1 scheme
- kind: domain-security
  name: Sunyur Domain Security
  slug: sunyur-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: sunyur
tags:
- Company
- Procurement
- SRM
- E-Procurement
- Supplier Management
- Digital Procurement
- Enterprise Software
- SaaS
- B2B
- China
- AI
website: https://www.sunyur.com
---
