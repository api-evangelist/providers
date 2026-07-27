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
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 28.8
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Retrieve campaign spend data for the authenticated customer via a keyed GET request, filterable by date range, campaign, bundle, platform, and country.
  name: App Samurai Campaign Spend API
  slug: app-samurai-campaign-spend-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://appsamurai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.appsamurai.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://help.appsamurai.com/en/articles/11105087-appsamurai-campaign-spend-api
- group: operate
  title: ''
  type: Support
  url: https://help.appsamurai.com/en/
- group: company
  title: ''
  type: Blog
  url: https://appsamurai.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Netvent
- group: start
  title: ''
  type: Login
  url: https://dashboard.appsamurai.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appsamurai.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appsamurai.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.storyly.io/
- group: build
  title: ''
  type: Packages
  url: packages/app-samurai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/app-samurai-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/app-samurai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/app-samurai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/app-samurai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/app-samurai-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/app-samurai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/app-samurai-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/app-samurai-domain-security.yml
created: '2026-07-17'
description: App Samurai is an AI-powered mobile app growth and user-acquisition platform that helps app and game publishers acquire, re-engage, and monetize users at scale. Its products span rewarded user-acquisition campaigns, a programmatic demand-side platform (DSP) for UA and retargeting across premium mobile inventory, OEM and on-device app discovery, and rewarded-playtime monetization, alongside the Storyly in-app stories product. Developers integrate through first-party mobile SDKs for App Samurai Ads, AS attribution, Appsprize playtime, and Storyly (iOS, Android, Unity, React Native), and can pull reporting programmatically via the Campaign Spend REST API. App Samurai is a Techstars-backed company reaching billions of devices worldwide.
image: https://appsamurai.com/og-default.png
layout: provider
mcp_servers:
- description: ''
  name: app-samurai-mcp.yml
  slug: app-samurai-mcpyml
modified: '2026-07-17'
name: App Samurai
nav: Providers
network: true
overview: 'App Samurai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobile, Advertising, User Acquisition, and App Marketing.


  App Samurai''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 14 more developer resources.'
random_paper: 32
score:
  band: emerging
  composite: 28.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 28.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/app-samurai/refs/heads/main/screenshots/app-samurai-2026-07-25T200710.png
security:
- kind: authentication
  name: App Samurai Authentication
  slug: app-samurai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: App Samurai Domain Security
  slug: app-samurai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: app-samurai
tags:
- Company
- Mobile
- Advertising
- User Acquisition
- App Marketing
- Attribution
- Monetization
- Mobile SDK
- Programmatic
website: https://appsamurai.com/
---
