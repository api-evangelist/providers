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
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 50.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The Campaign Spend API from Appsamurai — 1 operation(s) for campaign spend.
  name: Appsamurai Campaign Spend API
  slug: appsamurai-campaign-spend-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appsamurai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appsamurai.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.appsamurai.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://help.appsamurai.com/en/collections/12520260-campaign-spend-api-documentation
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.appsamurai.com/en/
- group: operate
  title: ''
  type: Support
  url: https://appsamurai.com/contact-us/
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
  type: SignUp
  url: https://dashboard.appsamurai.com/login
- group: start
  title: ''
  type: Login
  url: https://dashboard.appsamurai.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appsamurai.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appsamurai.com/terms-of-use/
- group: auth
  title: ''
  type: Compliance
  url: https://appsamurai.com/information-security-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/appsamurai-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appsamurai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/appsamurai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/appsamurai-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/appsamurai-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/appsamurai-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/appsamurai-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/appsamurai-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/appsamurai-conformance.yml
created: '2026-07-17'
description: AppSamurai (operated by Netvent) is a global, AI-powered mobile app growth platform founded in 2016. It offers user acquisition, retargeting, OEM / on-device app discovery, rewarded user acquisition, and monetization across one platform, plus the Storyly in-app stories product and the Interceptd ad fraud detection product. AppSamurai reaches over two billion users across more than 130 countries and works with mobile operators and device manufacturers such as Samsung, Xiaomi, Huawei, Oppo, and Lenovo. For developers and advertisers it publishes mobile ad and attribution SDKs and a Campaign Spend API that returns campaign spend reporting data via a keyed HTTP GET request. AppSamurai is ISO 27001 certified for information security. This profile was surfaced as a 500 Global portfolio company and enriched by the API Evangelist pipeline.
image: https://appsamurai.com/og-default.png
layout: provider
mcp_servers:
- description: ''
  name: appsamurai-mcp.yml
  slug: appsamurai-mcpyml
modified: '2026-07-18'
name: Appsamurai
nav: Providers
network: true
overview: 'Appsamurai publishes 1 API on the [APIs.io](https://apis.io/) network: Campaign Spend API. Tagged areas include Company, Mobile, Advertising, User Acquisition, and Marketing.


  Appsamurai''s developer surface includes documentation, support, engineering blog, signup flow, authentication, and 17 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 43.4
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 60.2
    developer_ergonomics: 50.0
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 43.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Appsamurai Authentication
  slug: appsamurai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Appsamurai Domain Security
  slug: appsamurai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appsamurai
tags:
- Company
- Mobile
- Advertising
- User Acquisition
- Marketing
- App Growth
- Attribution
- Analytics
- Mobile Marketing
- SDK
website: https://appsamurai.com
---
