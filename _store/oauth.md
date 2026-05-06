---
aid: oauth
name: OAuth
description: OAuth is an open authorization framework that enables third-party applications to access user resources without exposing credentials. It provides a secure, token-based delegation mechanism widely used across the web for granting limited access to APIs and services on behalf of users.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Access Control
  - Authorization
  - OAuth
  - Security
  - Tokens
url: https://raw.githubusercontent.com/api-evangelist/oauth/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: oauth:oauth-2-authorization-server
    name: OAuth 2.0 Authorization Server API
    description: API specification for an OAuth 2.0 authorization server implementing the authorization endpoint, token endpoint, and token revocation endpoint as defined in RFC 6749, RFC 6750, and RFC 7009.
    humanURL: https://oauth.net/2/
    tags:
      - Authorization
      - OAuth 2.0
    properties:
      - type: Documentation
        url: https://oauth.net/2/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/oauth/refs/heads/main/openapi/oauth-token-endpoint.yml
      - type: JSON Schema
        url: https://raw.githubusercontent.com/api-evangelist/oauth/refs/heads/main/json-schema/oauth-authorization-request.json
      - type: JSON Schema
        url: https://raw.githubusercontent.com/api-evangelist/oauth/refs/heads/main/json-schema/oauth-token-response.json
      - type: JSON Schema
        url: https://raw.githubusercontent.com/api-evangelist/oauth/refs/heads/main/json-schema/oauth-error-response.json
      - type: JSON-LD Context
        url: https://raw.githubusercontent.com/api-evangelist/oauth/refs/heads/main/json-ld/oauth-context.jsonld
common:
  - type: Website
    url: https://oauth.net/
  - type: Documentation
    url: https://oauth.net/2/
  - type: Reference
    url: https://datatracker.ietf.org/doc/html/rfc6749
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
