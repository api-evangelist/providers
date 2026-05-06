---
aid: keycloak
name: Keycloak
description: Keycloak is an open source identity and access management solution for modern applications and services, providing single sign-on, identity brokering, user federation, and fine-grained authorization using OAuth 2.0 and OpenID Connect.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Authorization
  - Identity Management
  - OAuth
  - OpenID Connect
  - Security
  - SSO
url: https://raw.githubusercontent.com/api-evangelist/keycloak/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: keycloak:admin-rest-api
    name: Keycloak Admin REST API
    description: REST API for managing Keycloak realms, users, clients, roles, groups, and identity providers. Provides full administrative control over all aspects of a Keycloak deployment.
    humanURL: https://www.keycloak.org/docs-api/latest/rest-api/
    tags:
      - Access Management
      - Admin
      - Identity
    properties:
      - type: Documentation
        url: https://www.keycloak.org/docs-api/latest/rest-api/
      - type: Reference
        url: https://www.keycloak.org/docs/latest/server_admin/
      - type: OpenAPI
        url: openapi/keycloak-admin-rest-api-openapi.yml
      - type: JSONSchema
        url: json-schema/realm.yml
      - type: JSONSchema
        url: json-schema/client.yml
      - type: JSONSchema
        url: json-schema/user.yml
      - type: JSONLD
        url: json-ld/keycloak-context.yml
common:
  - type: Website
    url: https://www.keycloak.org/
  - type: Documentation
    url: https://www.keycloak.org/documentation
  - type: Getting Started
    url: https://www.keycloak.org/getting-started
  - type: GitHub Organization
    url: https://github.com/keycloak/keycloak
  - type: Blog
    url: https://www.keycloak.org/blog
  - type: Community
    url: https://www.keycloak.org/community
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
