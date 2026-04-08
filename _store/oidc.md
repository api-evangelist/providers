---
aid: oidc
url: https://raw.githubusercontent.com/api-evangelist/oidc/refs/heads/main/apis.yml
apis:
- aid: oidc:openid-connect
  name: OpenID Connect API
  description: Core OpenID Connect API endpoints for authentication and identity, including discovery, authorization, token exchange, and user information.
  humanURL: https://openid.net/specs/openid-connect-core-1_0.html
  tags:
  - Authentication
  - Identity
  - OIDC
  properties:
  - type: Documentation
    url: https://openid.net/specs/openid-connect-core-1_0.html
  - type: OpenAPI
    url: openapi/oidc.yml
name: OIDC
tags:
- Authentication
- Identity
- JWT
- OAuth
- OIDC
- OpenID Connect
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: OpenID Connect (OIDC) is an identity layer built on top of OAuth 2.0 that enables clients to verify the identity of end-users based on authentication performed by an authorization server. It provides a standardized way to obtain basic profile information about users through RESTful endpoints including discovery, authorization, token, userinfo, and JWKS.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

