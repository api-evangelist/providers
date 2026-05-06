---
aid: ory
name: Ory
description: Ory is an open source identity infrastructure platform providing OAuth2 and OpenID Connect (Hydra), identity and user management (Kratos), permissions and authorization (Keto), and a reverse proxy with policy enforcement (Oathkeeper).
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Authorization
  - Identity
  - OAuth2
  - OpenID Connect
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/ory/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: ory:hydra
    name: Ory Hydra
    description: Ory Hydra is an OAuth 2.0 and OpenID Connect server. It implements OAuth 2.0 authorization, OpenID Connect Core 1.0, and OpenID Connect Discovery for issuing and managing access tokens, refresh tokens, ID tokens, and OAuth2 clients.
    humanURL: https://www.ory.sh/hydra/
    tags:
      - OAuth2
      - OpenID Connect
      - Authentication
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/ory/refs/heads/main/openapi/ory-hydra-openapi.json
      - type: Documentation
        url: https://www.ory.sh/docs/hydra/
      - type: GitHub Repository
        url: https://github.com/ory/hydra
  - aid: ory:kratos
    name: Ory Kratos
    description: Ory Kratos is an identity and user management system. It handles registration, login, multi-factor authentication, account recovery, verification, profile management, and identity schemas with strong security defaults.
    humanURL: https://www.ory.sh/kratos/
    tags:
      - Identity
      - Authentication
      - User Management
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/ory/refs/heads/main/openapi/ory-kratos-openapi.json
      - type: Documentation
        url: https://www.ory.sh/docs/kratos/
      - type: GitHub Repository
        url: https://github.com/ory/kratos
  - aid: ory:keto
    name: Ory Keto
    description: Ory Keto is a permission and authorization server inspired by Google Zanzibar. It provides relationship-based access control (ReBAC), role-based access control (RBAC), and access control list (ACL) checks at scale.
    humanURL: https://www.ory.sh/keto/
    tags:
      - Authorization
      - Permissions
      - Access Control
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/ory/refs/heads/main/openapi/ory-keto-openapi.json
      - type: Documentation
        url: https://www.ory.sh/docs/keto/
      - type: GitHub Repository
        url: https://github.com/ory/keto
  - aid: ory:oathkeeper
    name: Ory Oathkeeper
    description: Ory Oathkeeper is an identity and access proxy that authenticates, authorizes, and mutates incoming HTTP(S) requests using configurable access rules backed by Hydra, Kratos, and Keto.
    humanURL: https://www.ory.sh/oathkeeper/
    tags:
      - Reverse Proxy
      - Authentication
      - Authorization
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/ory/refs/heads/main/openapi/ory-oathkeeper-openapi.json
      - type: Documentation
        url: https://www.ory.sh/docs/oathkeeper/
      - type: GitHub Repository
        url: https://github.com/ory/oathkeeper
common:
  - type: Website
    url: https://www.ory.sh
  - type: Documentation
    url: https://www.ory.sh/docs/
  - type: GitHub Organization
    url: https://github.com/ory
  - type: Blog
    url: https://www.ory.sh/blog/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
