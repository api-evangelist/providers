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
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST/JSON API providing programmatic read-only access to AdMob account data, apps, ad units, mediation configuration, and network/mediation performance reports. Authorized with Google OAuth 2.0.
  name: AdMob API
  slug: admob-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/admob-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://g.co/vrp
- group: auth
  title: ''
  type: DomainSecurity
  url: security/admob-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/admob-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cloud.google.com/security/compliance
- group: agent
  title: ''
  type: WellKnown
  url: well-known/admob-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/admob-security.txt
- group: company
  title: ''
  type: Website
  url: https://admob.google.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.google.com/admob/api
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/admob/api/v1/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/admob/api/rest
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/admob/api/v1/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/admob
- group: company
  title: ''
  type: Blog
  url: https://ads-developers.googleblog.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleads
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.google.com/admob/api/release-notes
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://admob.google.com/home/get-started/
- group: auth
  title: ''
  type: Authentication
  url: authentication/admob-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/admob-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/admob-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/admob-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/admob-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/admob-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/admob-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/admob-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/admob-llms.txt
created: '2026-07-17'
description: AdMob is Google's mobile app advertising and monetization platform, letting app publishers earn revenue through in-app ads (banner, interstitial, rewarded, rewarded interstitial, native, and app open formats), maximize fill rate and eCPM with AdMob Mediation and open bidding across many ad networks, and understand performance through reporting and user metrics. The AdMob API (admob.googleapis.com, v1) provides programmatic, read-only access to AdMob account data, apps, ad units, mediation configuration, and network/mediation performance reports over REST/JSON, authorized with Google OAuth 2.0 using the admob.readonly and admob.report scopes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/admob.png
layout: provider
modified: '2026-07-17'
name: AdMob
nav: Providers
network: true
overview: 'AdMob publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Mobile, Monetization, and Ads.


  AdMob''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, signup flow, and 21 more developer resources.'
random_paper: 35
scopes:
- name: Admob Scopes
  scope_count: 2
  slug: admob-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 35.6
  delta: -0.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 36.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/screenshots/admob-2026-07-25T181651.png
security:
- kind: authentication
  name: Admob Authentication
  slug: admob-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Admob Domain Security
  slug: admob-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Admob Vulnerability Disclosure
  slug: admob-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Admob Trust Center
  slug: admob-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018, SOC 2, SOC 3, PCI DSS
slug: admob
tags:
- Company
- Advertising
- Mobile
- Monetization
- Ads
- Google
- Reporting
- Mediation
- AdTech
website: https://admob.google.com
---
