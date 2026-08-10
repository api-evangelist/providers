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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Enterprise REST API for the Storyclash influencer marketing platform. Token-based authentication over HTTPS returning structured JSON, with real-time webhooks for campaign updates and creator import s
  name: Storyclash API
  slug: storyclash-api
artifact_total: 4
asyncapis:
- description: ''
  name: Storyclash Webhooks
  slug: storyclash-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.storyclash.com/integrations/api-integration
- group: docs
  title: ''
  type: Documentation
  url: https://storyclash.notion.site/Storyclash-API-Documentation-1266dc2ddd0880a79cf9e3d34c19fa01
- group: commercial
  title: ''
  type: Pricing
  url: https://www.storyclash.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.storyclash.com/blog/en
- group: start
  title: ''
  type: Login
  url: https://app.storyclash.com/login
- group: operate
  title: ''
  type: Support
  url: https://help.storyclash.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.storyclash.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.storyclash.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.storyclash.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/storyclash-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/storyclash-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/storyclash-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/storyclash-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/storyclash-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/storyclash-domain-security.yml
created: '2026-07-17'
description: Storyclash is an AI-powered influencer marketing software platform used by brands and agencies to discover creators, analyze brand and competitor strategies, manage collaborations in a purpose-built CRM, and measure campaign performance and revenue ROI across Instagram, TikTok, YouTube, and Facebook. Its AI-driven creator discovery includes neural visual search over 120M+ creators, letting teams match on a reference image or product URL rather than keywords alone. Storyclash exposes an enterprise REST API with token-based authentication and real-time webhooks that streams campaign KPIs (50+ metrics per campaign), creator profiles, content performance, and revenue attribution as structured JSON into BI tools such as Power BI, Tableau, and Looker Studio. The company, headquartered in Linz, Austria, was surfaced as a portfolio company of Speedinvest and has since been acquired by Kolsquare.
image: https://www.storyclash.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: Storyclash
nav: Providers
network: true
overview: 'Storyclash publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Influencer Marketing, Creator Economy, Social Media Analytics, and Marketing Analytics.


  The Storyclash catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Storyclash''s developer surface includes documentation, pricing, engineering blog, support, authentication, and 10 more developer resources.'
random_paper: 56
score:
  band: thin
  composite: 40.6
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 34.8
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 40.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Storyclash Authentication
  slug: storyclash-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Storyclash Domain Security
  slug: storyclash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: storyclash
tags:
- Company
- Influencer Marketing
- Creator Economy
- Social Media Analytics
- Marketing Analytics
- Campaign Management
- Business Intelligence
- REST API
- Webhooks
website: https://www.storyclash.com/integrations/api-integration
---
