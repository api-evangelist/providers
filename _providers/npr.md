---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 12
  human_in_the_loop: 2
  name: Npr Agentic Access
  operation_count: 18
  slug: npr-agentic-access
  summary_line: 18 operations · 12 acting · 2 human-in-the-loop
api_count: 4
apis:
- description: Audio recommendations tailored to a user's preferences.
  name: NPR Listening
  slug: listening
- description: The Authorization API from NPR — 4 operation(s) for authorization.
  name: NPR Authorization API
  slug: npr-authorization-api
- description: The Identity API from NPR — 3 operation(s) for identity.
  name: NPR Identity API
  slug: npr-identity-api
- description: The Stationfinder API from NPR — 2 operation(s) for stationfinder.
  name: NPR Stationfinder API
  slug: npr-stationfinder-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/npr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/npr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/npr-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/npr-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/npr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/npr
- group: company
  title: ''
  type: Website
  url: https://www.npr.org/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.npr.org/
created: '2024-04-14'
description: National Public Radio (NPR) APIs. The APIs support station finding, authentication, user management, and listening with audio recommendations tailored to a user's preferences.
finops:
- name: Npr Finops
  service_category: Media / Public Broadcasting
  slug: npr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/npr.png
layout: provider
modified: '2026-05-19'
name: NPR
nav: Providers
network: true
overview: 'NPR publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Listening, Authorization API, Identity API, and 1 more. Tagged areas include Media, News, and Radio.


  NPR''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Npr Plans Pricing
  plan_count: 1
  slug: npr-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 1
  name: Npr Rate Limits
  slug: npr-rate-limits
scopes:
- name: Npr Scopes
  scope_count: 5
  slug: npr-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 33.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.6
    developer_ergonomics: 19.6
    discoverability: 75.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 33.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/npr/refs/heads/main/screenshots/npr-2026-06-20T190453.png
security:
- kind: authentication
  name: Npr Authentication
  slug: npr-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Npr Domain Security
  slug: npr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: npr
tags:
- Media
- News
- Radio
website: https://www.npr.org/
---
