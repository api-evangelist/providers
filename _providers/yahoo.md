---
access_model:
  confidence: high
  label: Application or Customer Gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - docs
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-09-03'
api_count: 5
apis:
- description: The Fantasy Sports APIs provide URIs used to access fantasy sports data, supporting retrieval of Fantasy Football, Baseball, Basketball and Hockey data including game, league, team, player, roster and
  name: Yahoo Fantasy Sports API
  slug: yahoo
- description: RESTful campaign-management API for the Yahoo demand-side platform. Exposes the full trafficking hierarchy - seats, account groups, advertisers, campaigns, packages, lines, ads and creatives - plus au
  name: Yahoo DSP Traffic API
  slug: dsp-traffic-api
- description: Asynchronous large-scale reporting API for Yahoo DSP campaign data. A Reporting object - composed of reportOption, limitSpec, filterOption, having and spec sub-objects plus account IDs, date type, int
  name: Yahoo DSP Reporting API
  slug: dsp-reporting-api
- description: 'Server-to-server conversion-event API (CAPI) for campaign measurement, attribution and optimization, positioned as the successor to browser-side Dot Pixel tracking. Two specifications are published - '
  name: Yahoo Conversion API
  slug: conversion-api
- description: Partner-facing data-exchange API for uploading and managing audience taxonomies, user and audience membership, fees and measurement feeds, plus a Real-Time API (specification v2.0), a Partner Match da
  name: Yahoo Ad Tech DataX API
  slug: datax-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.yahoo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.yahoo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.yahoo.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.yahoo.com/oauth2/guide/
- group: start
  title: ''
  type: SignUp
  url: https://developer.yahoo.com/apps/create/
- group: operate
  title: ''
  type: Support
  url: https://yahoo.uservoice.com/forums/182455-yahoo-developer-network
- group: company
  title: ''
  type: Blog
  url: https://developer.yahoo.com/blogs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.htm
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.yahoo.com/us/en/yahoo/privacy/products/developer/index.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/yahoodsp/workspace/public
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yahoo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yahoo
- group: auth
  title: ''
  type: Security
  url: security/yahoo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/yahoo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yahoo-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/yahoo-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/yahoo-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yahoo-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/yahoo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/yahoo-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yahoo-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/yahoo-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/yahoo-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yahoo-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/yahoo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/yahoo-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/yahoo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/yahoo-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/yahoo-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/yahoo-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/yahoo-components.yml
created: '2025-02-08'
description: Yahoo is a consumer internet and advertising-technology company operating Yahoo Mail, Yahoo Finance, Yahoo Sports and Yahoo Search alongside one of the largest independent demand-side platforms in programmatic advertising. Its public API surface splits cleanly in two. On the consumer side, the Yahoo Fantasy Sports API exposes fantasy football, baseball, basketball and hockey game, league, team, player, roster and transaction data over a composed URI tree at fantasysports.yahooapis.com, secured by a three-legged OAuth 2.0 flow against the Yahoo identity service, which itself publishes a full OpenID Connect discovery document. On the enterprise side, Yahoo Ad Tech ships the DSP Traffic API for programmatic campaign management, the DSP Reporting API for large-scale campaign measurement, the server-to-server Yahoo Conversion API, and the DataX API for audience and taxonomy exchange with data partners - all gated behind an existing DSP seat or a partner onboarding agreement and authenticated
  with a two-legged client-credentials JWT flow. Yahoo publishes no OpenAPI for any of these surfaces, distributing a public Postman collection and an llms.txt documentation index instead.
finops:
- name: Yahoo Finops
  service_category: API
  slug: yahoo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yahoo.png
layout: provider
modified: '2026-08-28'
name: Yahoo
nav: Providers
network: true
overview: 'Yahoo publishes 1 API on the [APIs.io](https://apis.io/) network: DSP Traffic API. Tagged areas include Advertising, Programmatic Advertising, Demand-Side Platform, Fantasy Sports, and Sports Data.


  Yahoo''s developer surface includes documentation, getting-started guide, signup flow, support, engineering blog, authentication, changelog, and 24 more developer resources.'
plans:
- name: Yahoo Plans Pricing
  plan_count: 0
  slug: yahoo-plans-pricing
press:
- date: '2026-05-25'
  title: Artificial intelligence
  url: https://finance.yahoo.com/topic/artificial-intelligence/
- date: '2026-05-25'
  title: AI News, Updates, Products and Reviews
  url: https://tech.yahoo.com/ai/
- date: '2026-05-25'
  title: Yahoo - The rapid growth of cloud computing and artificial ...
  url: https://www.facebook.com/yahoofinance/photos/the-rapid-growth-of-cloud-computing-and-artificial-intelligence-has-fueled-deman/1084123300249114/
- date: '2026-05-25'
  title: Introducing Yahoo Scout, a New AI Answer Engine
  url: https://www.yahooinc.com/press/introducing-yahoo-scout-a-new-ai-answer-engine
- date: '2026-05-25'
  title: How to Structure Press Releases for Maximum AI Visibility
  url: https://finance.yahoo.com/news/structure-press-releases-maximum-ai-091000311.html
random_paper: 19
rate_limits:
- limit_count: 17
  name: Yahoo Rate Limits
  slug: yahoo-rate-limits
scopes:
- name: Yahoo Scopes
  scope_count: 0
  slug: yahoo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 21
    catalog_gap: 60.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 68.4
  previous_composite: 39.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yahoo/refs/heads/main/screenshots/yahoo-2026-06-20T201726.png
security:
- kind: authentication
  name: Yahoo Authentication
  slug: yahoo-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Yahoo Domain Security
  slug: yahoo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Yahoo Vulnerability Disclosure
  slug: yahoo-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: yahoo
tags:
- Advertising
- Programmatic Advertising
- Demand-Side Platform
- Fantasy Sports
- Sports Data
- Identity
- OpenID Connect
- Authentication
- Audience Data
- Media
- Reporting
- Conversion Tracking
website: https://www.yahoo.com/
---
