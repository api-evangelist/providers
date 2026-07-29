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
- acting_count: 42
  human_in_the_loop: 4
  name: Unkey Dev Agentic Access
  operation_count: 42
  slug: unkey-dev-agentic-access
  summary_line: 42 operations · 42 acting · 4 human-in-the-loop
api_count: 8
apis:
- description: Key-verification analytics query operations.
  name: Unkey analytics API
  slug: unkey-dev-analytics-api
- description: API (namespace) management operations.
  name: Unkey apis API
  slug: unkey-dev-apis-api
- description: Deployment operations.
  name: Unkey deploy API
  slug: unkey-dev-deploy-api
- description: Identity (tenant / user) management operations.
  name: Unkey identities API
  slug: unkey-dev-identities-api
- description: API key management operations.
  name: Unkey keys API
  slug: unkey-dev-keys-api
- description: Health check operations.
  name: Unkey liveness API
  slug: unkey-dev-liveness-api
- description: Permission and role (RBAC) management operations.
  name: Unkey permissions API
  slug: unkey-dev-permissions-api
- description: Standalone rate limiting and override operations.
  name: Unkey ratelimit API
  slug: unkey-dev-ratelimit-api
artifact_total: 15
collections:
- collection_type: open
  name: Unkey API
  slug: open-unkey-dev
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unkey-dev-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unkey-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unkey-dev-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unkeyed
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unkeyed
- group: company
  title: ''
  type: Website
  url: https://www.unkey.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.unkey.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/unkey-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unkey-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unkey-dev-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.unkey.com/blog
created: '2026-07-02'
description: Unkey is an open-source developer platform for modern APIs, providing globally distributed API key management, authentication, and rate limiting. The platform lets API providers issue, verify, update, reroll, and revoke keys with metadata, expiration, usage credits, permissions, and roles, plus standalone rate limiting, identities, RBAC, and key-verification analytics. Unkey exposes an RPC-style REST API (all POST) with a stable v2 at api.unkey.com and a legacy v1 at api.unkey.dev, authenticated with Bearer root keys.
finops:
- name: Unkey Dev Finops
  service_category: Identity and Access Management
  slug: unkey-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unkey-dev.png
layout: provider
modified: '2026-07-02'
name: Unkey
nav: Providers
network: true
overview: 'Unkey publishes 8 APIs on the [APIs.io](https://apis.io/) network, including analytics API, apis API, deploy API, and 5 more. Tagged areas include API Keys, Rate Limiting, Authentication, Access Control, and Identity.


  Unkey''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Unkey Dev Plans Pricing
  plan_count: 7
  slug: unkey-dev-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Unkey Dev Rate Limits
  slug: unkey-dev-rate-limits
score:
  band: thin
  composite: 39.8
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Unkey Dev Authentication
  slug: unkey-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Unkey Dev Domain Security
  slug: unkey-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unkey-dev
tags:
- API Keys
- Rate Limiting
- Authentication
- Access Control
- Identity
- RBAC
- Analytics
- Open Source
website: https://www.unkey.com
---
