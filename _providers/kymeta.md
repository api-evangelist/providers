---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
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
    error_semantics: false
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
  score: 13.3
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Kymeta's first-party API host for the Kymeta Connect service platform, which backs the Kymeta Access app and the Kymeta Access Portal. The host answers unauthenticated on three operational endpoints o
  name: Kymeta Connect Platform API
  slug: kymeta-connect-platform-api
- description: Kymeta's own OAuth 2.0 / OpenID Connect authorization server (issuer https://access.kymeta.io), the single sign-on point for the Kymeta Access Portal, Kymeta Academy and Grapevine. It publishes a live
  name: Kymeta Access Identity
  slug: kymeta-access-identity
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kymeta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kymetacorp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.kymetacorp.com/support/resources
- group: operate
  title: ''
  type: Support
  url: https://www.kymetacorp.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.kymetacorp.com/about/news-insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kymetacorp.com/legal?q=terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kymetacorp.com/legal?q=privacy-policy
- group: start
  title: ''
  type: Login
  url: https://access.kymeta.io/
- group: learn
  title: ''
  type: Training
  url: https://www.kymetacorp.com/support/training
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kymeta-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kymeta-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kymeta-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kymeta-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kymeta-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kymeta-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kymeta-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kymeta-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kymeta-rate-limits.yml
coverage:
  checked: '2026-08-23'
  detail: Kymeta runs a live first-party API host at api.kymeta.io that answers /health, /version and /status unauthenticated and 404s every specification path, while its own support site states "You must have a Kymeta Access Portal account to access the notices" — so the contract, reference and release notes for the Kymeta Connect platform all sit behind a customer tenant rather than being unpublished.
  evidence:
  - status: 200
    url: https://api.kymeta.io/status
  - status: 404
    url: https://api.kymeta.io/openapi.json
  - status: 200
    url: https://www.kymetacorp.com/support/product-and-software-updates
  - status: 200
    url: https://access.kymeta.io/.well-known/openid-configuration
  reason: customer-only-docs
  state: gated
created: '2026-08-23'
description: Kymeta Corporation is a Redmond, Washington satellite communications company that builds electronically steered, flat-panel metamaterial antennas and the connectivity service that runs behind them. Spun out of Intellectual Ventures in 2012 from metamaterials research begun at Duke University, Kymeta ships the u8 terminal family — Osprey u8, Goshawk u8, Peregrine u8, Hawk u8 and the compact Kestrel u5 — for military and government, maritime, land-mobile, energy and humanitarian users who need multi-orbit GEO/LEO connectivity on the move. The hardware is paired with Kymeta Connect, a software-defined service platform reached through the Kymeta Access app and the Kymeta Access Portal, which handles terminal management, subscriptions, usage metrics and remote monitoring. Kymeta operates a first-party API host and its own OAuth 2.0 / OpenID Connect identity provider, but publishes no public developer program, API reference or machine-readable contract; product documentation and release
  notices require a Kymeta Access Portal account.
image: https://www.kymetacorp.com/dist/img/meta/logo-mark.svg
layout: provider
modified: '2026-08-23'
name: Kymeta
nav: Providers
network: true
overview: 'Kymeta publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Satellite, Satellite Communications, Connectivity, Telecommunications, and Networking.


  Kymeta''s developer surface includes documentation, support, engineering blog, training material, authentication, and 13 more developer resources.'
plans:
- name: Kymeta Plans Pricing
  plan_count: 0
  slug: kymeta-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Kymeta Rate Limits
  slug: kymeta-rate-limits
scopes:
- name: Kymeta Scopes
  scope_count: 11
  slug: kymeta-scopes
  summary_line: 11 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 24.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 58.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kymeta/refs/heads/main/screenshots/kymeta-2026-09-02T150227.png
security:
- kind: authentication
  name: Kymeta Authentication
  slug: kymeta-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Kymeta Domain Security
  slug: kymeta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kymeta
tags:
- Satellite
- Satellite Communications
- Connectivity
- Telecommunications
- Networking
- Antennas
- Metamaterials
- Aerospace and Defense
- Maritime
- Remote Monitoring
- Hardware
website: https://www.kymetacorp.com/
---
