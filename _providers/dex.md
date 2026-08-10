---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: gRPC management API for Dex covering OAuth2 client lifecycle (Create, Get, Update, Delete, List), password management (Create, Update, Delete, List, Verify), identity provider connector management (Cr
  name: Dex gRPC API
  slug: grpc-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dexidp.io/
- group: docs
  title: ''
  type: Documentation
  url: https://dexidp.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dexidp
- group: other
  title: ''
  type: Repository
  url: https://github.com/dexidp/dex
- group: commercial
  title: ''
  type: License
  url: https://github.com/dexidp/dex/blob/master/LICENSE
created: '2025-01-01'
description: A federated OpenID Connect provider that connects to other identity providers through connectors, enabling authentication for applications without handling passwords directly. Dex acts as a portal to other identity providers through connectors, making it easy to implement SSO across multiple providers. Dex is a single Go binary with pluggable storage and ships with a gRPC management API (api/v2/api.proto) for managing OAuth2 clients, passwords, connectors, and refresh tokens, alongside the standard set of OIDC endpoints.
finops:
- name: Dex Finops
  service_category: API
  slug: dex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dex.png
layout: provider
modified: '2026-04-28'
name: Dex
nav: Providers
network: true
overview: 'Dex publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Authentication, Connectors, Federation, gRPC, and Identity Provider.


  Dex''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Dex Plans Pricing
  plan_count: 3
  slug: dex-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 5
  name: Dex Rate Limits
  slug: dex-rate-limits
score:
  band: emerging
  composite: 22.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 22.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dex/refs/heads/main/screenshots/dex-2026-06-20T175953.png
security:
- kind: domain-security
  name: Dex Domain Security
  slug: dex-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dex
tags:
- Authentication
- Connectors
- Federation
- gRPC
- Identity Provider
- LDAP
- OAuth 2.0
- OIDC
- OpenID Connect
- SAML
- Single Sign-On
- SSO
website: https://dexidp.io/
---
