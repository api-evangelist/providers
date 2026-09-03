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
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The App.net Stream API — a RESTful, OAuth 2.0-secured social API covering posts, users, follows, channels/messages, files, filters, and a real-time streaming surface. Responses use a uniform {data, me
  name: App.net Stream API
  slug: appnet-stream-api
artifact_total: 4
common:
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
  title: ''
  type: Authentication
  url: authentication/appnet-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/appnet-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/appnet-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/appnet-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/appnet-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/appnet-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/appnet-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/appnet-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/appnet-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appnet-llms.txt
created: '2026-07-17'
description: 'App.net (ADN) was a paid, ad-free real-time social networking and microblogging platform launched in 2012 by Dalton Caldwell''s Mixed Media Labs after a public crowdfunding campaign. It was explicitly developer-first: the App.net Stream API exposed posts, users, follows, files, channels, private messaging, filters and a real-time streaming/subscription surface, all governed by OAuth 2.0 bearer tokens and a consistent data/meta response envelope. Third-party clients (Alpha, and many community apps) were built entirely on the public API. App.net announced in 2016 that it would not renew and the service was shut down on 2017-03-14; the live API hosts (api.app.net, developers.app.net) no longer resolve and the app.net domain is now operated by an unrelated apps directory. The API documentation (appdotnet/api-spec), terms of service, and official SDKs remain publicly preserved on the appdotnet GitHub organization, which is the basis for this profile.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appnet.png
layout: provider
modified: '2026-07-18'
name: App.net
nav: Providers
network: true
overview: 'App.net publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, Microblogging, Messaging, and Real-Time.


  App.net''s developer surface includes documentation, authentication, and 11 more developer resources.'
random_paper: 18
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
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 22.0
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
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
---
