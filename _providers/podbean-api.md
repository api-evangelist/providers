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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Podbean Api Agentic Access
  operation_count: 8
  slug: podbean-api-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 6
apis:
- description: This is for third-party apps to connect to Podbean in order to manage a user's podcast. To manage your own podcast via API, please use Client Credentials and Get Multiple Podcasts Tokens. Provides OAu
  name: Podbean API
  slug: podbean-api
- description: Per-podcast analytics and report downloads.
  name: Podbean API Analytics API
  slug: podbean-api-analytics-api
- description: List and inspect episodes.
  name: Podbean API Episodes API
  slug: podbean-api-episodes-api
- description: Token issuance endpoints.
  name: Podbean API OAuth API
  slug: podbean-api-oauth-api
- description: List podcasts in the account.
  name: Podbean API Podcasts API
  slug: podbean-api-podcasts-api
- description: Manage private podcast members.
  name: Podbean API PrivateMembers API
  slug: podbean-api-privatemembers-api
artifact_total: 14
collections:
- collection_type: open
  name: Podbean API
  slug: open-podbean-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/podbean-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/podbean-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/podbean-api-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/podbean-api-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.podbean.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/podbean
- group: company
  title: ''
  type: Website
  url: https://www.podbean.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.podbean.com/podbean-api-docs/
created: '2025-05-02'
description: This is for third-party apps to connect to Podbean in order to manage a user's podcast. To manage your own podcast via API, please use Client Credentials and Get Multiple Podcasts Tokens. The Podbean API supports OAuth 2.0 authentication and provides programmatic access to podcasts, episodes, analytics, and account management resources.
finops:
- name: Podbean Api Finops
  service_category: API
  slug: podbean-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/podbean-api.png
layout: provider
modified: '2026-04-28'
name: Podbean API
nav: Providers
network: true
overview: 'Podbean API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Episodes API, OAuth API, and 2 more. Tagged areas include Podcasts, Podcasting, Audio, Media, and OAuth.


  Podbean API''s developer surface includes authentication, engineering blog, documentation, and 5 more developer resources.'
plans:
- name: Podbean Api Plans Pricing
  plan_count: 3
  slug: podbean-api-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Podbean Api Rate Limits
  slug: podbean-api-rate-limits
scopes:
- name: Podbean Api Scopes
  scope_count: 5
  slug: podbean-api-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: thin
  composite: 38.1
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/podbean-api/refs/heads/main/screenshots/podbean-api-2026-06-20T191831.png
security:
- kind: authentication
  name: Podbean Api Authentication
  slug: podbean-api-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Podbean Api Domain Security
  slug: podbean-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: podbean-api
tags:
- Podcasts
- Podcasting
- Audio
- Media
- OAuth
- Episodes
website: https://www.podbean.com
---
