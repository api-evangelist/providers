---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Pulsoid Agentic Access
  operation_count: 15
  slug: pulsoid-agentic-access
  summary_line: 15 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://dev.pulsoid.net
  baseurl_source: declared
  description: The Features API from Pulsoid — 1 operation(s) for features.
  name: Pulsoid Features API
  slug: pulsoid-features-api
- baseURL: https://dev.pulsoid.net
  baseurl_source: declared
  description: The Geometry Dash API from Pulsoid — 1 operation(s) for geometry dash.
  name: Pulsoid Geometry Dash API
  slug: pulsoid-geometry-dash-api
- baseURL: https://dev.pulsoid.net
  baseurl_source: declared
  description: The Heart Rate API from Pulsoid — 2 operation(s) for heart rate.
  name: Pulsoid Heart Rate API
  slug: pulsoid-heart-rate-api
- baseURL: https://dev.pulsoid.net
  baseurl_source: declared
  description: The OAuth2 API from Pulsoid — 4 operation(s) for oauth2.
  name: Pulsoid OAuth2 API
  slug: pulsoid-oauth2-api
- baseURL: https://dev.pulsoid.net
  baseurl_source: declared
  description: The Profile API from Pulsoid — 1 operation(s) for profile.
  name: Pulsoid Profile API
  slug: pulsoid-profile-api
- baseURL: https://dev.pulsoid.net
  baseurl_source: declared
  description: The Statistics API from Pulsoid — 1 operation(s) for statistics.
  name: Pulsoid Statistics API
  slug: pulsoid-statistics-api
- baseURL: https://dev.pulsoid.net
  baseurl_source: declared
  description: The Token API from Pulsoid — 1 operation(s) for token.
  name: Pulsoid Token API
  slug: pulsoid-token-api
- baseURL: https://dev.pulsoid.net
  baseurl_source: declared
  description: The Widgets API from Pulsoid — 2 operation(s) for widgets.
  name: Pulsoid Widgets API
  slug: pulsoid-widgets-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pulsoid Features API
  slug: open-pulsoid-features-api
- collection_type: open
  name: Pulsoid Features Geometry Dash API
  slug: open-pulsoid-geometry-dash-api
- collection_type: open
  name: Pulsoid Features Heart Rate API
  slug: open-pulsoid-heart-rate-api
- collection_type: open
  name: Pulsoid Features OAuth2 API
  slug: open-pulsoid-oauth2-api
- collection_type: open
  name: Pulsoid Features Profile API
  slug: open-pulsoid-profile-api
- collection_type: open
  name: Pulsoid Features Statistics API
  slug: open-pulsoid-statistics-api
- collection_type: open
  name: Pulsoid Features Token API
  slug: open-pulsoid-token-api
- collection_type: open
  name: Pulsoid Features Widgets API
  slug: open-pulsoid-widgets-api
- collection_type: open
  name: Pulsoid API
  slug: open-pulsoid
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pulsoid-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pulsoid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pulsoid-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pulsoid-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pulsoid
- group: company
  title: ''
  type: Website
  url: https://pulsoid.net/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pulsoid.net/
- group: start
  title: ''
  type: Signup
  url: https://pulsoid.net/auth/sign_up
- group: start
  title: ''
  type: Login
  url: https://pulsoid.net/auth/sign_in
- group: auth
  title: ''
  type: Authentication
  url: https://docs.pulsoid.net/access-token-and-authentication/about-access-token
- group: auth
  title: ''
  type: OAuth
  url: https://docs.pulsoid.net/access-token-and-authentication/oauth-authorization-code-grant
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pulsoid
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.pulsoid.net/llms.txt
created: '2025-02-17'
description: Pulsoid enables real-time heart rate data transmission from peripherals (BLE heart rate monitors, smartwatches, etc.) to clients. The Pulsoid API allows reading and writing real-time heart rate data, accessing statistics, and managing widgets and profile.
finops:
- name: Pulsoid Finops
  service_category: API
  slug: pulsoid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pulsoid.png
layout: provider
modified: '2026-05-19'
name: Pulsoid
nav: Providers
network: true
overview: 'Pulsoid publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Features API, Geometry Dash API, Heart Rate API, and 5 more. Tagged areas include Heart Rate, Health, Wearables, Real-Time, and Streaming.


  Pulsoid''s developer surface includes authentication, documentation, signup flow, and 10 more developer resources.'
plans:
- name: Pulsoid Plans Pricing
  plan_count: 3
  slug: pulsoid-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Pulsoid Rate Limits
  slug: pulsoid-rate-limits
scopes:
- name: Pulsoid Scopes
  scope_count: 9
  slug: pulsoid-scopes
  summary_line: 9 scopes · implicit/authorizationCode
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 49.8
    developer_ergonomics: 9.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 36.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pulsoid/refs/heads/main/screenshots/pulsoid-2026-06-20T192309.png
security:
- kind: authentication
  name: Pulsoid Authentication
  slug: pulsoid-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Pulsoid Domain Security
  slug: pulsoid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pulsoid
tags:
- Heart Rate
- Health
- Wearables
- Real-Time
- Streaming
- WebSocket
- Authentication
website: https://pulsoid.net/
---
