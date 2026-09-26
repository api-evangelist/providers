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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: The App.net Stream API — a RESTful, OAuth 2.0-secured social API covering posts, users, follows, channels/messages, files, filters, and a real-time streaming surface. Responses use a uniform {data, me
  name: App.net Stream API
  slug: appnet-stream-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://app.net
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appdotnet
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/appdotnet/api-spec
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/appdotnet/terms-of-service
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appnet/refs/heads/main/authentication/appnet-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appnet-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appnet/refs/heads/main/scopes/appnet-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/appnet-scopes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appnet/refs/heads/main/packages/appnet-packages.yml
  title: ''
  type: Packages
  url: packages/appnet-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appnet/refs/heads/main/packages/appnet-packages.yml
  title: ''
  type: SDKs
  url: packages/appnet-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appnet/refs/heads/main/conventions/appnet-conventions.yml
  title: ''
  type: Conventions
  url: conventions/appnet-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appnet/refs/heads/main/errors/appnet-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/appnet-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appnet/refs/heads/main/conformance/appnet-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appnet-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appnet/refs/heads/main/lifecycle/appnet-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/appnet-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/appnet/refs/heads/main/rate-limits/appnet-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/appnet-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appnet/refs/heads/main/llms/appnet-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appnet-llms.txt
created: '2026-07-17'
description: 'App.net (ADN) was a paid, ad-free real-time social networking and microblogging platform launched in 2012 by Dalton Caldwell''s Mixed Media Labs after a public crowdfunding campaign. It was explicitly developer-first: the App.net Stream API exposed posts, users, follows, files, channels, private messaging, filters and a real-time streaming/subscription surface, all governed by OAuth 2.0 bearer tokens and a consistent data/meta response envelope. Third-party clients (Alpha, and many community apps) were built entirely on the public API. App.net announced in 2016 that it would not renew and the service was shut down on 2017-03-14; the live API hosts (api.app.net, developers.app.net) no longer resolve and the app.net domain is now operated by an unrelated apps directory. The API documentation (appdotnet/api-spec), terms of service, and official SDKs remain publicly preserved on the appdotnet GitHub organization, which is the basis for this profile.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appnet.png
layout: provider
modified: '2026-09-16'
name: App.net
nav: Providers
network: true
overview: 'App.net publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, Microblogging, Messaging, and Real-Time.


  App.net''s developer surface includes documentation, authentication, and 12 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 3
  name: Appnet Rate Limits
  slug: appnet-rate-limits
scopes:
- name: Appnet Scopes
  scope_count: 9
  slug: appnet-scopes
  summary_line: 9 scopes · authorizationCode/implicit/password
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/appnet/refs/heads/main/screenshots/appnet-2026-07-25T200825.png
security:
- kind: authentication
  name: Appnet Authentication
  slug: appnet-authentication
  summary_line: oauth2 · 1 scheme
slug: appnet
tags:
- Company
- Social
- Microblogging
- Messaging
- Real-Time
- Streaming
- Developer Platform
- Authentication
- Defunct
website: https://app.net
---
