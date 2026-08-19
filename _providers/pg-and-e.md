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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
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
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PG&E Share My Data Authorization API
  slug: open-pg-and-e-authorization-api
- collection_type: open
  name: PG&E Share My Data API
  slug: open-pg-and-e-share-my-data-api
- collection_type: open
  name: PG&E Share My Data Authorization Subscriptions API
  slug: open-pg-and-e-subscriptions-api
- collection_type: open
  name: PG&E Share My Data Authorization Usage API
  slug: open-pg-and-e-usage-api
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
random_paper: 117
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
  composite: 24.7
  delta: -1.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 25.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
