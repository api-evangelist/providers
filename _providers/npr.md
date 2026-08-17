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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-17'
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
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NPR Identity Service Authorization API
  slug: open-npr-authorization-api
- collection_type: open
  name: NPR Service Authorization Identity API
  slug: open-npr-identity-api
- collection_type: open
  name: NPR Identity Service Authorization Stationfinder API
  slug: open-npr-stationfinder-api
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
random_paper: 38
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
  band: emerging
  composite: 27.4
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 55.5
    developer_ergonomics: 19.6
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 27.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
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
