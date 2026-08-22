---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openid-connect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openid.net/
- group: docs
  title: ''
  type: Documentation
  url: https://openid.net/developers/specs/
- group: docs
  title: ''
  type: Reference
  url: https://openid.net/specs/openid-connect-core-1_0.html
- group: agent
  title: ''
  type: LlmsText
  url: https://openid.net/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://openid.net/feed/
created: '2025-01-01'
description: OpenID Connect (OIDC) is an identity authentication protocol that is an extension of OAuth 2.0. It enables clients to verify the identity of end-users and obtain basic profile information in a secure, standardized way using JSON Web Tokens (JWT).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openid-connect.png
layout: provider
modified: '2026-04-28'
name: OpenID Connect
nav: Providers
network: true
overview: 'OpenID Connect is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Authentication, Identity, JWT, OAuth, and OpenID Connect.


  OpenID Connect''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 9.5
  delta: 0.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openid-connect/refs/heads/main/screenshots/openid-connect-2026-06-20T191005.png
security:
- kind: domain-security
  name: Openid Connect Domain Security
  slug: openid-connect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openid-connect
tags:
- Authentication
- Identity
- JWT
- OAuth
- OpenID Connect
website: https://openid.net/
---
