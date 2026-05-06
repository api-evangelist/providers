---
aid: google-identity-platform
name: Google Identity Platform
description: Google Identity Platform provides authentication and identity management APIs that enable developers to add sign-in, user management, and multi-tenancy capabilities to applications using industry-standard protocols including OAuth 2.0, OpenID Connect, and SAML.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-identity-platform/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Authentication
  - Google Cloud
  - Identity
  - Multi-Tenancy
  - OAuth
  - OpenID Connect
  - SAML
apis:
  - name: Identity Toolkit API
    description: The Identity Toolkit API (v3) provides REST endpoints for managing user authentication in Google Identity Platform. It supports creating and signing in users with email/password, phone, and federated identity providers. The API handles token verification, password resets, email verification, account linking, and multi-factor authentication enrollment and sign-in.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/identity-platform/docs/reference/rest
    baseURL: https://identitytoolkit.googleapis.com
    tags:
      - Authentication
      - Identity
      - Sign-In
      - Users
    properties:
      - type: Documentation
        url: https://cloud.google.com/identity-platform/docs/reference/rest
      - type: OpenAPI
        url: openapi/identity-toolkit-openapi.yml
      - type: JSONSchema
        url: json-schema/google-identity-platform-user-schema.json
  - name: Identity Platform Tenant Management API
    description: The Tenant Management API enables developers to create and manage tenants for multi-tenant Identity Platform configurations. Each tenant can have its own set of identity providers, authentication settings, and user pools, allowing SaaS applications to isolate authentication for different customers or organizational units.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/identity-platform/docs/multi-tenancy
    baseURL: https://identitytoolkit.googleapis.com
    tags:
      - Multi-Tenancy
      - SaaS
      - Tenant Management
    properties:
      - type: Documentation
        url: https://cloud.google.com/identity-platform/docs/multi-tenancy
  - name: Identity Platform OAuth Configuration API
    description: The OAuth Configuration API allows developers to programmatically manage OAuth identity provider configurations for Identity Platform projects. It supports configuring Google, Facebook, Apple, Microsoft, Twitter, GitHub, and other OIDC and SAML providers for federated authentication.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/identity-platform/docs/federated-login
    baseURL: https://identitytoolkit.googleapis.com
    tags:
      - Federation
      - Identity Providers
      - OAuth
    properties:
      - type: Documentation
        url: https://cloud.google.com/identity-platform/docs/reference/rest/v2/projects.defaultSupportedIdpConfigs
common:
  - type: GettingStarted
    url: https://cloud.google.com/identity-platform/docs/quickstarts
  - type: Pricing
    url: https://cloud.google.com/identity-platform/pricing
  - type: Authentication
    url: https://cloud.google.com/identity-platform/docs/concepts
  - type: Console
    url: https://console.cloud.google.com/customer-identity
  - type: SDKs
    url: https://cloud.google.com/identity-platform/docs/reference/libraries
  - type: Support
    url: https://cloud.google.com/identity-platform/docs/support
  - type: Status
    url: https://status.cloud.google.com
  - type: JSON-LD
    url: json-ld/google-identity-platform-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
