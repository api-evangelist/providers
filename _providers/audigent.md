---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-10'
api_count: 4
apis:
- description: Public, anonymous identity-resolution endpoint that returns Audigent's cookieless Hadron ID (plus hadronIdv2 and the legacy haloId) for the calling browser. Called by the Prebid.js hadronIdSystem user
  name: Hadron ID API
  slug: hadron-id-api
- description: Segment and real-time-data endpoint returning an OpenRTB ortb2 fragment used to enrich a Prebid auction with Audigent audience segments and contextual signals. Backed by the hadronRtdProvider Prebid.j
  name: Hadron Real-Time Data (RTD) API
  slug: hadron-real-time-data-rtd-api
- description: Analytics collection endpoint for the hadronAnalyticsAdapter Prebid.js analytics adapter. Receives auction lifecycle events (auctionInit, auctionEnd, bidWon and related) keyed to an Audigent partnerId
  name: Hadron Analytics API
  slug: hadron-analytics-api
- description: Authenticated platform API behind the Audigent admin console. The host is live (gunicorn/Django) but every anonymous request 302s to the admin.audigent.com login, and no public reference, OpenAPI or d
  name: Audigent Platform API
  slug: audigent-platform-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://audigent.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.prebid.org/dev-docs/modules/hadronRtdProvider.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.prebid.org/dev-docs/modules/userid-submodules/hadron.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.prebid.org/dev-docs/modules/userid-submodules/hadron.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AuDigent
- group: company
  title: ''
  type: Blog
  url: https://audigent.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://audigent.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://admin.audigent.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://audigent.com/privacypolicy/
- group: commercial
  title: ''
  type: PlatformPrivacyPolicy
  url: https://audigent.com/platform-privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://audigent.com/cookie-policy/
- group: commercial
  title: ''
  type: PrivacyCenter
  url: https://audigent.com/privacy-center/
- group: auth
  title: ''
  type: Authentication
  url: authentication/audigent-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/audigent-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/audigent-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/audigent-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/audigent-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/audigent-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/audigent-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/audigent-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/audigent-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/audigent_stock/
created: '2026-08-06'
description: 'Audigent is a data activation, curation and identity platform for digital advertising, acquired by Experian in December 2024 and now operated as part of Experian Marketing Services. Its products include the Hadron ID cookieless identifier, the SmartPMP, ContextualPMP and CognitivePMP private-marketplace suites, a first-party data platform for publishers and advertisers, and the 1st Unit rich-media format. Audigent''s public technical surface is not a documented REST developer program: it is a set of live ad-tech identity, segment and analytics endpoints on the ad.gt and hadronid.net domains, reached through first-party open-source Prebid.js modules (hadronIdSystem, hadronRtdProvider, hadronAnalyticsAdapter) that Audigent authors and maintains upstream in the Prebid.js project. Audigent is IAB Europe TCF Global Vendor List vendor 561 and publishes a machine-readable device-storage disclosure.'
image: https://avatars.githubusercontent.com/u/16336664?v=4
layout: provider
modified: '2026-08-06'
name: Audigent
nav: Providers
network: true
overview: 'Audigent publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Data, and Identity.


  Audigent''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 16 more developer resources.'
random_paper: 37
score:
  band: emerging
  composite: 27.5
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 13.2
  previous_composite: 27.5
  provenance:
    conformance: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/audigent/refs/heads/main/screenshots/audigent-2026-08-07T161917.png
security:
- kind: authentication
  name: Audigent Authentication
  slug: audigent-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Audigent Domain Security
  slug: audigent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: audigent
tags:
- Company
- Advertising
- AdTech
- Data
- Identity
- Programmatic
- Audience
- Marketing
- Privacy
- Prebid
- Header Bidding
- Data Curation
website: https://audigent.com/
---
