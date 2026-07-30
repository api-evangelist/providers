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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: HeadSpin's v0 REST API for authentication, real-device management, capture sessions, app (APK/IPA) instrumentation, biometrics, and audio/video capture. Authenticates with a HeadSpin API token as an H
  name: HeadSpin REST API (v0)
  slug: headspin-rest-api-v0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.headspin.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.headspin.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.headspin.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.headspin.io/docs
- group: company
  title: ''
  type: Blog
  url: https://www.headspin.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.headspin.io/pricing
- group: start
  title: ''
  type: Login
  url: https://ui.headspin.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.headspin.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.headspin.io/terms/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/headspinio
- group: auth
  title: ''
  type: Authentication
  url: authentication/headspin-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/headspin-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/headspin-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/headspin-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/headspin-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/headspin-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/headspin-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/headspin-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/headspin-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/headspin-domain-security.yml
created: '2026-07-17'
description: HeadSpin is a real-device digital-experience, functional, and performance testing platform for mobile, web, and OTT applications. Teams test, monitor, and optimize app behavior on real devices and real SIMs across 60+ locations in 50+ countries, running manual and automated tests through frameworks such as Appium and Selenium while capturing 130+ performance KPIs across app, device, browser, audio-video, and network layers. HeadSpin exposes a v0 REST API (Bearer API-token auth) for authentication, device management, capture sessions, app instrumentation, biometrics, and audio/video capture, plus an official `hs` command-line interface and a family of open-source Appium drivers for Roku, LG WebOS, and Samsung Tizen TV.
image: https://cdn.prod.website-files.com/619e15d781b212391a206fb2/67c6baa984aae71625255247_home-headspin.jpg
layout: provider
mcp_servers:
- description: ''
  name: headspin-mcp.yml
  slug: headspin-mcpyml
modified: '2026-07-19'
name: HeadSpin
nav: Providers
network: true
overview: 'HeadSpin publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Testing, Mobile, Performance, and Real Device Testing.


  HeadSpin''s developer surface includes documentation, API reference, engineering blog, pricing, authentication, CLI, and 14 more developer resources.'
random_paper: 24
score:
  band: thin
  composite: 28.0
  delta: -2.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 30.6
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/headspin/refs/heads/main/screenshots/headspin-2026-07-25T220825.png
security:
- kind: authentication
  name: Headspin Authentication
  slug: headspin-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Headspin Domain Security
  slug: headspin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: headspin
tags:
- Company
- Testing
- Mobile
- Performance
- Real Device Testing
- Automation
- Appium
- OTT
- Quality Assurance
- Monitoring
website: https://www.headspin.io
---
