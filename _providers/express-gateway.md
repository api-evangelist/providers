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
- acting_count: 16
  human_in_the_loop: 0
  name: Express Gateway Agentic Access
  operation_count: 25
  slug: express-gateway-agentic-access
  summary_line: 25 operations · 16 acting
api_count: 5
apis:
- description: Express Gateway is an API gateway built on Express.js for managing and securing microservices and APIs.
  name: Express Gateway
  slug: express-gateway
- description: The Apps API from Express Gateway — 3 operation(s) for apps.
  name: Express Gateway Apps API
  slug: express-gateway-apps-api
- description: The Credentials API from Express Gateway — 6 operation(s) for credentials.
  name: Express Gateway Credentials API
  slug: express-gateway-credentials-api
- description: The Scopes API from Express Gateway — 2 operation(s) for scopes.
  name: Express Gateway Scopes API
  slug: express-gateway-scopes-api
- description: The Users API from Express Gateway — 3 operation(s) for users.
  name: Express Gateway Users API
  slug: express-gateway-users-api
artifact_total: 12
collections:
- collection_type: open
  name: Express Gateway Admin API
  slug: open-express-gateway
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/express-gateway-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/express-gateway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/express-gateway-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.express-gateway.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.express-gateway.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ExpressGateway
created: '2026-03-27'
description: Express Gateway is an API gateway built on Express.js for managing and securing microservices and APIs.
finops:
- name: Express Gateway Finops
  service_category: API
  slug: express-gateway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/express-gateway.png
layout: provider
modified: '2026-04-28'
name: Express Gateway
nav: Providers
network: true
overview: 'Express Gateway publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Credentials API, Scopes API, and 1 more. Tagged areas include API Composition, API Gateway, and BFF.


  Express Gateway''s developer surface includes authentication, documentation, and 4 more developer resources.'
plans:
- name: Express Gateway Plans Pricing
  plan_count: 3
  slug: express-gateway-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Express Gateway Rate Limits
  slug: express-gateway-rate-limits
score:
  band: thin
  composite: 32.9
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 46.6
    developer_ergonomics: 19.6
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/express-gateway/refs/heads/main/screenshots/express-gateway-2026-06-20T180941.png
security:
- kind: authentication
  name: Express Gateway Authentication
  slug: express-gateway-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Express Gateway Domain Security
  slug: express-gateway-domain-security
  summary_line: TLSv1.3 · HSTS
slug: express-gateway
tags:
- API Composition
- API Gateway
- BFF
website: https://www.express-gateway.io/
---
