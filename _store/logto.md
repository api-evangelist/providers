---
aid: logto
name: Logto
description: Logto is an open source identity infrastructure platform with authentication, authorization, user management, and multi-tenancy supporting OIDC, OAuth, and SAML.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Authorization
  - Identity
  - OIDC
  - OAuth
  - SAML
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/logto/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: logto:logto-api
    name: Logto API
    description: The Logto Management API provides full programmatic access to applications, users, roles, organizations, connectors, sign-in experiences, and tenant configuration. The OpenAPI specification covers Logto Cloud; Logto OSS instances expose the same surface via /api/swagger.json.
    humanURL: https://docs.logto.io
    tags:
      - Authentication
      - Identity
      - User Management
    properties:
      - type: Documentation
        url: https://docs.logto.io
      - type: GitHub Repository
        url: https://github.com/logto-io/logto
      - type: OpenAPI
        url: openapi/logto-openapi-original.yml
common:
  - type: Website
    url: https://logto.io
  - type: Documentation
    url: https://docs.logto.io
  - type: OpenAPI
    url: https://openapi.logto.io/source.yaml
  - type: GitHub Organization
    url: https://github.com/logto-io
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
