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
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
api_count: 3
apis:
- description: The Ad Serving API from LoopMe — 1 operation(s) for ad serving.
  name: LoopMe Ad Serving API
  slug: loopme-ad-serving-api
- description: The Advertiser Reporting API from LoopMe — 1 operation(s) for advertiser reporting.
  name: LoopMe Advertiser Reporting API
  slug: loopme-advertiser-reporting-api
- description: The Publisher Reporting API from LoopMe — 1 operation(s) for publisher reporting.
  name: LoopMe Publisher Reporting API
  slug: loopme-publisher-reporting-api
artifact_total: 6
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wiki.loopme.cool/
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.loopme.cool/
- group: docs
  title: ''
  type: APIReference
  url: https://wiki.loopme.cool/publishers/reporting-api
- group: company
  title: ''
  type: Blog
  url: https://loopme.ai/news-blog/
- group: operate
  title: ''
  type: Support
  url: https://www.loopme.io/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/loopme
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.loopme.com/privacy-center
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.loopme.com/legal-centre/terms-of-use
- group: build
  title: ''
  type: SDKs
  url: packages/loopme-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/loopme-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loopme-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/loopme-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/loopme-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/loopme-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/loopme-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/loopme-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loopme-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/loopme-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/loopme-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loopme-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: LoopMe is a global brand-performance advertising platform that uses AI to bring brands into mobile and CTV apps. Its products span an AI-powered intelligent marketplace, PurchaseLoop outcome-based brand advertising, the Chartboost in-app monetization platform, and an Audience & Measurement Platform (AMP). For developers, LoopMe exposes a REST Reporting API for publisher (app/site) and advertiser (campaign) statistics, a server-to-server (S2S) ad request API, first-party United SDKs for Android and iOS, and a Prebid.js header-bidding adapter. LoopMe is backed by HV Capital and headquartered in the UK.
image: https://loopme.ai/wp-content/themes/loopme/assets/images/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: loopme-mcp.yml
  slug: loopme-mcpyml
modified: '2026-07-20'
name: LoopMe
nav: Providers
network: true
overview: 'LoopMe publishes 3 APIs on the [APIs.io](https://apis.io/) network: Ad Serving API, Advertiser Reporting API, and Publisher Reporting API. Tagged areas include Company, Advertising, AdTech, Mobile Advertising, and CTV.


  LoopMe''s developer surface includes documentation, API reference, engineering blog, support, authentication, changelog, and 15 more developer resources.'
random_paper: 40
score:
  band: developing
  composite: 45.0
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 61.9
    developer_ergonomics: 63.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 45.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loopme/refs/heads/main/screenshots/loopme-2026-07-25T225535.png
security:
- kind: authentication
  name: Loopme Authentication
  slug: loopme-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Loopme Domain Security
  slug: loopme-domain-security
  summary_line: TLSv1.3 · DMARC
slug: loopme
tags:
- Company
- Advertising
- AdTech
- Mobile Advertising
- CTV
- Reporting
- Programmatic
- Ai Enterprise Software
- SDK
website: https://wiki.loopme.cool/
---
