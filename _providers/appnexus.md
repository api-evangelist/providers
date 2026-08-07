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
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: RESTful JSON API for the AppNexus/Xandr programmatic advertising platform - manage advertisers, campaigns, line items, creatives, placements, inventory, deals, and pull reporting. Token authentication
  name: Digital Platform API
  slug: digital-platform-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.appnexus.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.microsoft.com/xandr/digital-platform-api/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/xandr/digital-platform-api/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/xandr/digital-platform-api/api-services
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/xandr/digital-platform-api/api-onboarding-process
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appnexus
- group: auth
  title: ''
  type: Authentication
  url: authentication/appnexus-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/appnexus-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/appnexus-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/appnexus-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/xandr/digital-platform-api/breaking-changes
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/xandr/digital-platform-api/api-release-notes
- group: start
  title: ''
  type: Sandbox
  url: sandbox/appnexus-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/appnexus-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/appnexus-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/appnexus-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appnexus-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appnexus-llms.txt
created: '2026-07-17'
description: AppNexus was a New York-based programmatic advertising technology company that ran one of the largest independent real-time online ad exchanges alongside a cloud-based buy-side and sell-side platform for advertisers, agencies, and publishers. AT&T acquired AppNexus in 2018 and rebranded it Xandr; it is now part of Microsoft. Its developer surface lives on as the Xandr Digital Platform API (host api.appnexus.com) - a RESTful JSON API for campaign, creative, inventory, deal, and reporting operations - plus the first-party AppNexus mobile advertising SDKs for Android and iOS. This profile was enriched by the API Evangelist pipeline from the public developer documentation.
image: https://raw.githubusercontent.com/api-evangelist/appnexus/refs/heads/main/apis.yml
layout: provider
modified: '2026-07-17'
name: AppNexus
nav: Providers
network: true
overview: 'AppNexus publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Adtech, Advertising, Programmatic, and Ad Exchange.


  AppNexus'' developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, and 12 more developer resources.'
random_paper: 93
score:
  band: emerging
  composite: 23.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 23.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appnexus/refs/heads/main/screenshots/appnexus-2026-07-25T200821.png
security:
- kind: authentication
  name: Appnexus Authentication
  slug: appnexus-authentication
  summary_line: token · 1 scheme
- kind: domain-security
  name: Appnexus Domain Security
  slug: appnexus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appnexus
tags:
- Company
- Adtech
- Advertising
- Programmatic
- Ad Exchange
- DSP
- SSP
- Mobile SDK
- Marketing
website: https://www.appnexus.com
---
