---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 6
apis:
- description: Endpoints for authenticating end-users and obtaining authorization grants.
  name: OIDC Authentication API
  slug: oidc-authentication-api
- description: OpenID Connect Discovery endpoints for provider metadata.
  name: OIDC Discovery API
  slug: oidc-discovery-api
- description: JSON Web Key Set endpoint for token signature verification.
  name: OIDC JWKS API
  slug: oidc-jwks-api
- description: Session management endpoints including logout.
  name: OIDC Session API
  slug: oidc-session-api
- description: Token endpoint for exchanging authorization codes for tokens.
  name: OIDC Token API
  slug: oidc-token-api
- description: Endpoint for retrieving claims about the authenticated end-user.
  name: OIDC User Info API
  slug: oidc-user-info-api
artifact_total: 8
common:
- group: other
  href: https://artifacts.apis.io/openid-connect/capabilities/openid-connect-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/openid-connect-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/openid-connect/security/openid-connect-domain-security.yml
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
overview: 'OpenID Connect publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including OIDC Authentication API, OIDC Discovery API, OIDC JWKS API, and 3 more. Tagged areas include Authentication, Identity, JWT, OAuth, and OpenID Connect.


  The OpenID Connect catalog on APIs.io includes 1 Spectral governance ruleset.


  OpenID Connect''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: OpenID Connect API Rules
  rule_count: 62
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 1
  slug: openid-connect-rules
screenshot: https://apis.io/screenshots/openid-connect/openid-connect-2026-06-20T191005.png
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
