---
aid: dex
name: Dex
description: A federated OpenID Connect provider that connects to other identity providers through connectors, enabling authentication for applications without handling passwords directly. Dex acts as a portal to other identity providers through connectors, making it easy to implement SSO across multiple providers. Dex is a single Go binary with pluggable storage and ships with a gRPC management API (api/v2/api.proto) for managing OAuth2 clients, passwords, connectors, and refresh tokens, alongside the standard set of OIDC endpoints.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
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
url: https://dexidp.io/
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: dex:grpc-api
    name: Dex gRPC API
    description: gRPC management API for Dex covering OAuth2 client lifecycle (Create, Get, Update, Delete, List), password management (Create, Update, Delete, List, Verify), identity provider connector management (Create, Update, Delete, List), refresh token listing and revocation, OpenID Connect discovery retrieval, and version reporting. The canonical schema lives in api/v2/api.proto in the dexidp/dex repository.
    humanURL: https://dexidp.io/docs/configuration/api/
    baseURL: https://dexidp.io
    tags:
      - Authentication
      - gRPC
      - Identity
      - Management API
      - OIDC
    properties:
      - type: Documentation
        url: https://dexidp.io/docs/configuration/api/
      - type: SourceCode
        url: https://github.com/dexidp/dex/blob/master/api/v2/api.proto
      - type: Repository
        url: https://github.com/dexidp/dex
common:
  - type: Website
    url: https://dexidp.io/
  - type: Documentation
    url: https://dexidp.io/docs/
  - type: GitHub Organization
    url: https://github.com/dexidp
  - type: Repository
    url: https://github.com/dexidp/dex
  - type: License
    url: https://github.com/dexidp/dex/blob/master/LICENSE
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
