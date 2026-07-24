---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pg And E Agentic Access
  operation_count: 5
  slug: pg-and-e-agentic-access
  summary_line: 5 operations
api_count: 3
apis:
- description: OAuth 2.0 authorization for customer data access.
  name: pg-and-e Authorization API
  slug: pg-and-e-authorization-api
- description: Manage data subscriptions for customer accounts.
  name: pg-and-e Subscriptions API
  slug: pg-and-e-subscriptions-api
- description: Retrieve energy usage interval data.
  name: pg-and-e Usage API
  slug: pg-and-e-usage-api
artifact_total: 11
collections:
- collection_type: open
  name: PG&E Share My Data API
  slug: open-pg-and-e-share-my-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pg-and-e-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pg-and-e-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pg-and-e-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pg-and-e-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pgetech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pacificgasandelectric
- group: other
  title: ''
  type: Share My Data
  url: https://www.pge.com/en/save-energy-and-money/energy-usage-and-tips/understand-my-usage/share-my-data.html
- group: company
  title: ''
  type: Website
  url: https://www.pge.com/
description: Pacific Gas and Electric Company (PG&E) is one of the largest combined natural gas and electric energy companies in the United States, serving approximately 16 million people in northern and central California. PG&E offers the Share My Data API, a Green Button Connect My Data implementation providing customer- authorized access to energy usage interval data for both electricity and gas through RESTful web services.
finops:
- name: Pg And E Finops
  service_category: Utilities Data
  slug: pg-and-e-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pg-and-e.png
layout: provider
modified: '2026-05-19'
name: pg-and-e
nav: Providers
network: true
overview: 'pg-and-e publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authorization API, Subscriptions API, and Usage API.


  pg-and-e''s developer surface includes authentication and 7 more developer resources.'
plans:
- name: Pg And E Plans Pricing
  plan_count: 1
  slug: pg-and-e-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 1
  name: Pg And E Rate Limits
  slug: pg-and-e-rate-limits
scopes:
- name: Pg And E Scopes
  scope_count: 1
  slug: pg-and-e-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 29.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.4
    developer_ergonomics: 10.9
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 29.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/screenshots/pg-and-e-2026-06-20T191630.png
security:
- kind: authentication
  name: Pg And E Authentication
  slug: pg-and-e-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Pg And E Domain Security
  slug: pg-and-e-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pg-and-e
website: https://www.pge.com/
---
