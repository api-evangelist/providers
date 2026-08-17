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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.8
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: RESTful JSON API for the AppNexus/Xandr programmatic advertising platform - manage advertisers, campaigns, line items, creatives, placements, inventory, deals, and pull reporting. Token authentication
  name: Digital Platform API
  slug: digital-platform-api
artifact_total: 6
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
  url: https://learn.microsoft.com/en-us/xandr/digital-platform-api/reference
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
  url: https://learn.microsoft.com/en-us/xandr/digital-platform-api/breaking-changes
- group: operate
  title: ''
  type: StatusPage
  url: https://status.xandr.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/xandr/monetize/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/appnexus-changelog.yml
- group: operate
  title: ''
  type: Support
  url: https://help.xandr.com
- group: start
  title: ''
  type: Login
  url: https://monetize.xandr.com/login
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
- group: build
  title: ''
  type: SDKs
  url: packages/appnexus-packages.yml
- group: design
  title: ''
  type: Components
  url: components/appnexus-components.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/appnexus-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/appnexus-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/appnexus-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/appnexus-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/appnexus-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appnexus-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/appnexus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/appnexus-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appnexus-llms.txt
created: '2026-07-17'
description: AppNexus was a New York-based programmatic advertising technology company that ran one of the largest independent real-time online ad exchanges alongside a cloud-based buy-side and sell-side platform for advertisers, agencies, and publishers. AT&T acquired AppNexus in 2018 and rebranded it Xandr; Microsoft acquired Xandr in 2022 and productized it as Microsoft Monetize (sell-side) and Microsoft Invest (buy-side). Its developer surface lives on as the Digital Platform API (host api.appnexus.com) - a RESTful JSON API of roughly 150 services covering advertisers, insertion orders, line items, campaigns, creatives, publishers, sites, placements, deals and reporting - plus the actively released AppNexus mobile advertising SDKs for Android and iOS. Microsoft is discontinuing the Invest DSP effective 28 February 2026; the Monetize sell-side platform and the API remain live, documented on Microsoft Learn. No OpenAPI, MCP server or agent card is published, and API access is restricted
  to contracted customers. This profile was enriched by the API Evangelist pipeline from the public developer documentation.
image: https://raw.githubusercontent.com/api-evangelist/appnexus/refs/heads/main/apis.yml
layout: provider
modified: '2026-08-12'
name: AppNexus
nav: Providers
network: true
overview: 'AppNexus publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Adtech, Advertising, Programmatic, and Ad Exchange.


  AppNexus'' developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, and 24 more developer resources.'
plans:
- name: Appnexus Plans Pricing
  plan_count: 0
  slug: appnexus-plans-pricing
random_paper: 139
rate_limits:
- limit_count: 4
  name: Appnexus Rate Limits
  slug: appnexus-rate-limits
score:
  band: thin
  composite: 37.6
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 86.8
  previous_composite: 37.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appnexus/refs/heads/main/screenshots/appnexus-2026-07-25T200821.png
security:
- kind: authentication
  name: Appnexus Authentication
  slug: appnexus-authentication
  summary_line: token · 2 schemes
- kind: domain-security
  name: Appnexus Domain Security
  slug: appnexus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Appnexus Vulnerability Disclosure
  slug: appnexus-vulnerability-disclosure
  summary_line: Hackerone
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
