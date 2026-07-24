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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 17.3
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: 'Cuvva''s fleet of public single-purpose service APIs — auth (OAuth 2.0), vehicle lookup, MOT status, motor-coverage quotes/policies, billing, promo, profile, upload, terms, notification and more. Most '
  name: Cuvva Services API
  slug: cuvva-services-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.cuvva.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/cuvva/docs
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/cuvva/docs/tree/master/apis
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/cuvva/docs/tree/master/apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cuvva
- group: operate
  title: ''
  type: Support
  url: https://support.cuvva.com/en
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.cuvva.com/en
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cuvva.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.cuvva.com/en/articles/5907873-cuvva-s-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.cuvva.com/en/articles/5907862-cuvva-s-privacy-notice
- group: auth
  title: ''
  type: Authentication
  url: authentication/cuvva-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cuvva-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/cuvva-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cuvva-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cuvva-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cuvva-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cuvva-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cuvva-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cuvva-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cuvva-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/cuvva-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cuvva-llms.txt
created: '2026-07-17'
description: Cuvva is a UK insurtech that pioneered flexible, short-term car and van insurance sold entirely through its mobile apps. Founded in 2015 as the first app to sell temporary car insurance in the UK, it offers policies from one hour up to 28 days, learner-driver cover, drive-away cover for newly purchased vehicles, temporary van and motorhome insurance, and a rolling subscription product (formerly Flexi). Cuvva is FCA-authorised and has sold over 16 million policies to 1.7M+ drivers. Its engineering is built on a fleet of small single-purpose service APIs (auth, vehicle, MOT, motor-coverage, billing, promo, profile, upload, terms, notification and more), publicly documented on GitHub and secured with an in-house OAuth 2.0 implementation using JWT bearer tokens.
image: https://www.cuvva.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Cuvva
nav: Providers
network: true
overview: 'Cuvva publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Car Insurance, and Financial Services.


  Cuvva''s developer surface includes documentation, API reference, support, authentication, and 18 more developer resources.'
random_paper: 39
scopes:
- name: Cuvva Scopes
  scope_count: 1
  slug: cuvva-scopes
  summary_line: 1 scope · authorizationCode/refreshToken
score:
  band: thin
  composite: 36.1
  delta: 9.4
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 26.7
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 89.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: rising
security:
- kind: authentication
  name: Cuvva Authentication
  slug: cuvva-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Cuvva Domain Security
  slug: cuvva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cuvva Vulnerability Disclosure
  slug: cuvva-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: cuvva
tags:
- Company
- Insurance
- Insurtech
- Car Insurance
- Financial Services
- Mobile
- OAuth
- United Kingdom
website: https://www.cuvva.com
---
