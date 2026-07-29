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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 21
  human_in_the_loop: 1
  name: Onelogin Agentic Access
  operation_count: 31
  slug: onelogin-agentic-access
  summary_line: 31 operations · 21 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: Application management
  name: OneLogin Apps API
  slug: onelogin-apps-api
- description: Multi-Factor Authentication
  name: OneLogin MFA API
  slug: onelogin-mfa-api
- description: OAuth 2.0 token generation and revocation
  name: OneLogin OAuth API
  slug: onelogin-oauth-api
- description: Role management
  name: OneLogin Roles API
  slug: onelogin-roles-api
- description: SAML assertion generation
  name: OneLogin SAML API
  slug: onelogin-saml-api
- description: User management
  name: OneLogin Users API
  slug: onelogin-users-api
artifact_total: 13
collections:
- collection_type: open
  name: OneLogin API
  slug: open-onelogin
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/onelogin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onelogin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/onelogin-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onelogin
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onelogin
- group: company
  title: ''
  type: Website
  url: https://www.onelogin.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.onelogin.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.onelogin.com
- group: company
  title: ''
  type: Blog
  url: https://www.onelogin.com/blog/feed
created: '2025-01-08'
description: OneLogin is an identity and access management platform providing single sign-on (SSO), multi-factor authentication, user provisioning, and a RESTful API for managing users, roles, applications, MFA, branding, connectors, reports, SAML assertions, smart hooks, and Vigilance AI.
finops:
- name: Onelogin Finops
  service_category: API
  slug: onelogin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onelogin.png
layout: provider
modified: '2026-05-19'
name: OneLogin
nav: Providers
network: true
overview: 'OneLogin publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Apps API, MFA API, OAuth API, and 3 more. Tagged areas include Identity, Access Management, Single Sign-On, Multi-Factor Authentication, and SAML.


  OneLogin''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Onelogin Plans Pricing
  plan_count: 3
  slug: onelogin-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 5
  name: Onelogin Rate Limits
  slug: onelogin-rate-limits
score:
  band: thin
  composite: 39.2
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.0
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onelogin/refs/heads/main/screenshots/onelogin-2026-06-20T190716.png
security:
- kind: authentication
  name: Onelogin Authentication
  slug: onelogin-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Onelogin Domain Security
  slug: onelogin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: onelogin
tags:
- Identity
- Access Management
- Single Sign-On
- Multi-Factor Authentication
- SAML
- OAuth
website: https://www.onelogin.com
---
