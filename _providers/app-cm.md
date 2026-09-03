---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/app-cm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://app-cm.co.jp
- group: operate
  title: ''
  type: Support
  url: https://www.app-cm.co.jp/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.app-cm.co.jp/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.app-cm.co.jp/privacy/
- group: build
  title: ''
  type: Packages
  url: packages/app-cm-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/app-cm-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/app-cm-llms.txt
coverage:
  checked: '2026-08-12'
  detail: App-CM markets an iOS/Android publisher SDK — the FAQ states publishers integrate the video ad unit via SDK — but the only documented way to obtain it is the contact form, after which a sales rep opens an account; there is no developer portal, no download, no reference, and no package in npm/PyPI/CocoaPods/Maven Central.
  evidence:
  - status: 200
    url: https://www.app-cm.co.jp/faq/
  - status: 200
    url: https://www.app-cm.co.jp/contact/
  - status: 404
    url: https://app-cm.co.jp/openapi.json
  - status: 404
    url: https://app-cm.co.jp/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: 'App-CM, Inc. (株式会社アップシーエム) is a Tokyo-based technology company that operates a proprietary video-advertising delivery platform for smartphones, using in-house compression, delivery, and targeting-algorithm technology to serve video ads smoothly in mobile environments. App-CM also develops and publishes consumer mobile apps including FriendQuiz, SunQ, and Shakin. The company is backed by 500 Global and is profiled in the API Evangelist network. It ships a publisher-side iOS/Android video ad SDK, but distributes it only through a sales conversation: there is no public API, developer portal, SDK download, package-registry release, or machine-readable specification, and every /.well-known/ discovery path returns 404. This profile captures its identity, commercial model, and security posture.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/app-cm.png
layout: provider
modified: '2026-08-12'
name: App-CM
nav: Providers
network: true
overview: 'App-CM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Video Advertising, AdTech, and Mobile.


  App-CM''s developer surface includes support and 7 more developer resources.'
plans:
- name: App Cm Plans Pricing
  plan_count: 0
  slug: app-cm-plans-pricing
random_paper: 7
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/app-cm/refs/heads/main/screenshots/app-cm-2026-07-25T200700.png
security:
- kind: domain-security
  name: App Cm Domain Security
  slug: app-cm-domain-security
  summary_line: TLSv1.3
slug: app-cm
tags:
- Company
- Advertising
- Video Advertising
- AdTech
- Mobile
- Consumer Apps
- Platform
- Japan
website: https://app-cm.co.jp
---
