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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: JSON ad-request endpoint (mobile.mng-ads.com) that returns a single ad (banner, interstitial, native) for a given placement, device User-Agent, SDK version and consent signal. GET or POST.
  name: Madvertise Ad Request API
  slug: madvertise-ad-request-api
- description: OpenRTB 2.5 bid-request endpoint (mobile.mng-ads.com/bidrequest/{placement}) for programmatic in-app demand. POST JSON with x-openrtb-version 2.5; returns bid markup in the adm field, 204 when no bid,
  name: Madvertise OpenRTB Bid Request API
  slug: madvertise-openrtb-bid-request-api
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bluestack.app/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bluestack.app/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.bluestack.app/adserving/
- group: company
  title: ''
  type: Blog
  url: https://developers.bluestack.app/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.bluestack.app/releases
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/azerion
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developers.bluestack.app/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://madvertise.com/en
- group: build
  title: ''
  type: Packages
  url: packages/madvertise-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/madvertise-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/madvertise-error-codes.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/madvertise-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/madvertise-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/madvertise-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/madvertise-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/madvertise-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.bluestack.app/releases
- group: auth
  title: ''
  type: DomainSecurity
  url: security/madvertise-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/madvertise-llms.txt
created: '2026-07-17'
description: Madvertise is a mobile advertising and monetization brand now operating within Azerion as the "BlueStack" (Improve Digital InApp) mobile SDK suite and the mng-ads.com ad-serving platform. It lets mobile publishers monetize in-app inventory with banner, interstitial, native, rewarded-video and App Open ad formats through first-party SDKs for Android, iOS, Unity, React Native, Flutter and .NET MAUI, and connects programmatic demand through an OpenRTB 2.5 bid-request API, a JSON ad-request API, VAST video, and a Prebid Server adapter. The platform advertises IAB TCF, IAB Open Measurement, GDPR and COPPA compliance. Originally a Munich-founded mobile ad network backed by Point Nine Capital, Madvertise's technology now ships under Azerion / Improve Digital.
image: https://www.azerion.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: Madvertise
nav: Providers
network: true
overview: 'Madvertise publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Mobile, and Monetization.


  Madvertise''s developer surface includes documentation, API reference, engineering blog, changelog, authentication, and 14 more developer resources.'
random_paper: 36
score:
  band: emerging
  composite: 23.6
  delta: -0.2
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 23.8
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/madvertise/refs/heads/main/screenshots/madvertise-2026-07-25T225832.png
security:
- kind: authentication
  name: Madvertise Authentication
  slug: madvertise-authentication
  summary_line: placement-code/app-id · 2 schemes
- kind: domain-security
  name: Madvertise Domain Security
  slug: madvertise-domain-security
  summary_line: TLSv1.3
slug: madvertise
tags:
- Company
- Advertising
- AdTech
- Mobile
- Monetization
- Programmatic
- OpenRTB
- SDK
- Publishers
website: https://madvertise.com/en
---
