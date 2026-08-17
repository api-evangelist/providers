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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Oauth2 Proxy Agentic Access
  operation_count: 12
  slug: oauth2-proxy-agentic-access
  summary_line: 12 operations
api_count: 7
apis:
- description: oauth2-proxy is an open-source reverse proxy that provides authentication with Google, Azure, OpenID Connect, and many more identity providers.
  name: Oauth2-Proxy
  slug: oauth2-proxy
- description: The Metrics API from Oauth2-Proxy — 1 operation(s) for metrics.
  name: Oauth2-Proxy Metrics API
  slug: oauth2-proxy-metrics-api
- description: The Oauth2 API from Oauth2-Proxy — 7 operation(s) for oauth2.
  name: Oauth2-Proxy Oauth2 API
  slug: oauth2-proxy-oauth2-api
- description: The OAuth2 Proxy Endpoints API from Oauth2-Proxy — 1 operation(s) for oauth2 proxy endpoints.
  name: Oauth2-Proxy OAuth2 Proxy Endpoints API
  slug: oauth2-proxy-oauth2-proxy-endpoints-api
- description: The Ping API from Oauth2-Proxy — 1 operation(s) for ping.
  name: Oauth2-Proxy Ping API
  slug: oauth2-proxy-ping-api
- description: The Ready API from Oauth2-Proxy — 1 operation(s) for ready.
  name: Oauth2-Proxy Ready API
  slug: oauth2-proxy-ready-api
- description: The Robots.txt API from Oauth2-Proxy — 1 operation(s) for robots.txt.
  name: Oauth2-Proxy Robots.txt API
  slug: oauth2-proxy-robots-txt-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OAuth2 Proxy Endpoints Metrics API
  slug: open-oauth2-proxy-metrics-api
- collection_type: open
  name: Proxy Endpoints Metrics Oauth2 API
  slug: open-oauth2-proxy-oauth2-api
- collection_type: open
  name: Metrics OAuth2 Proxy Endpoints API
  slug: open-oauth2-proxy-oauth2-proxy-endpoints-api
- collection_type: open
  name: OAuth2 Proxy Endpoints Metrics Ping API
  slug: open-oauth2-proxy-ping-api
- collection_type: open
  name: OAuth2 Proxy Endpoints Metrics Ready API
  slug: open-oauth2-proxy-ready-api
- collection_type: open
  name: OAuth2 Proxy Endpoints Metrics Robots.txt API
  slug: open-oauth2-proxy-robots-txt-api
- collection_type: open
  name: OAuth2 Proxy Endpoints
  slug: open-oauth2-proxy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oauth2-proxy-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oauth2-proxy-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://oauth2-proxy.github.io/oauth2-proxy/
- group: docs
  title: ''
  type: Documentation
  url: https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oauth2-proxy/oauth2-proxy
created: '2026-03-27'
description: oauth2-proxy is an open-source reverse proxy that provides authentication with Google, Azure, OpenID Connect, and many more identity providers.
finops:
- name: Oauth2 Proxy Finops
  service_category: API
  slug: oauth2-proxy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oauth2-proxy.png
layout: provider
modified: '2026-03-27'
name: Oauth2-Proxy
nav: Providers
network: true
overview: 'Oauth2-Proxy publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Metrics API, Oauth2 API, OAuth2 Proxy Endpoints API, and 3 more. Tagged areas include Authentication Proxy and Proxy.


  Oauth2-Proxy''s developer surface includes authentication, documentation, and 3 more developer resources.'
plans:
- name: Oauth2 Proxy Plans Pricing
  plan_count: 3
  slug: oauth2-proxy-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 5
  name: Oauth2 Proxy Rate Limits
  slug: oauth2-proxy-rate-limits
score:
  band: emerging
  composite: 24.2
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 43.0
    developer_ergonomics: 19.6
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 24.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oauth2-proxy/refs/heads/main/screenshots/oauth2-proxy-2026-06-20T190551.png
security:
- kind: authentication
  name: Oauth2 Proxy Authentication
  slug: oauth2-proxy-authentication
  summary_line: apiKey · 1 scheme
slug: oauth2-proxy
tags:
- Authentication Proxy
- Proxy
website: https://oauth2-proxy.github.io/oauth2-proxy/
---
