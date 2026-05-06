---
aid: stytch
url: https://raw.githubusercontent.com/api-evangelist/stytch/refs/heads/main/apis.yml
apis:
  - aid: stytch:stytch-consumer-api
    name: Stytch Consumer Authentication API
    tags:
      - Authentication
      - Passwordless
      - Magic Links
      - OTP
      - Consumer
    humanURL: https://stytch.com/docs/api
    properties:
      - url: https://stytch.com/docs/api
        type: Documentation
      - url: https://stytch.com/docs/api/reference/library/overview
        type: API Reference
      - url: openapi/stytch-consumer-openapi.yml
        type: OpenAPI
    description: Stytch's Consumer API provides passwordless and password-based authentication for consumer-facing applications. Supports magic links, SMS/email OTP, OAuth social login, TOTP (authenticator apps), WebAuthn (biometrics/passkeys), and session management.
  - aid: stytch:stytch-b2b-api
    name: Stytch B2B Authentication API
    tags:
      - Authentication
      - B2B
      - SSO
      - Multi-Tenant
      - Organizations
    humanURL: https://stytch.com/docs/b2b
    properties:
      - url: https://stytch.com/docs/b2b
        type: Documentation
      - url: https://stytch.com/docs/b2b/api/overview
        type: API Reference
      - url: openapi/stytch-b2b-openapi.yml
        type: OpenAPI
    description: Stytch's B2B API provides authentication and identity management for organization-based SaaS applications. Supports multi-tenancy with Organizations and Members, SSO via SAML and OIDC, magic links, OTP, OAuth, and organization discovery flows.
name: Stytch
tags:
  - Authentication
  - Identity
  - Passwordless
  - Security
  - Developer Tools
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-15'
modified: '2026-05-04'
position: Consuming
description: Stytch is a company that specializes in providing secure and seamless authentication solutions for businesses. Their platform allows companies to integrate passwordless authentication methods such as magic links, SMS and email OTP, OAuth, TOTP, WebAuthn, and biometrics. Stytch offers both a Consumer API for end-user authentication and a B2B API for multi-tenant SaaS applications with organization management, SSO, and role-based access control.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - url: https://stytch.com
    type: Website
  - url: https://stytch.com/docs
    type: Documentation
  - url: https://stytch.com/docs/api
    type: API Reference
  - url: https://app.stytch.com/register
    type: Sign Up
  - url: https://app.stytch.com
    type: Portal
  - url: https://stytch.com/docs/guides/authentication
    type: Authentication
  - url: https://stytch.com/docs/guides/sessions
    type: Sessions
  - url: https://stytch.com/docs/sdks
    type: SDKs
  - url: https://stytch.com/pricing
    type: Pricing
  - url: https://stytch.com/privacy
    type: Privacy Policy
  - url: https://stytch.com/terms
    type: Terms of Service
  - url: https://stytch.com/docs/guides/webhooks
    type: Webhooks
  - url: https://github.com/stytchauth
    type: GitHub Organization
  - url: https://www.postman.com/stytch/stytch-public-workspace/overview
    type: Postman Workspace
  - url: https://github.com/stytchauth/stytch-node
    type: Node.js SDK
  - url: https://github.com/stytchauth/stytch-python
    type: Python SDK
  - url: https://github.com/stytchauth/stytch-java
    type: Java SDK
  - url: https://github.com/stytchauth/stytch-go
    type: Go SDK
  - url: https://github.com/stytchauth/stytch-ruby
    type: Ruby SDK
  - url: https://github.com/stytchauth/stytch-php
    type: PHP SDK
  - url: https://status.stytch.com
    type: Status
  - url: https://stytch.com/blog
    type: Blog
  - url: rules/stytch-rules.yml
    type: Spectral Rules
  - url: capabilities/passwordless-authentication.yaml
    type: Naftiko Capability
  - url: capabilities/b2b-identity-management.yaml
    type: Naftiko Capability
  - url: vocabulary/stytch-vocabulary.yml
    type: Vocabulary
  - url: json-schema/stytch-user-schema.json
    type: JSON Schema
  - url: json-schema/stytch-organization-schema.json
    type: JSON Schema
  - url: json-structure/stytch-session-structure.json
    type: JSON Structure
  - url: json-ld/stytch-context.jsonld
    type: JSON-LD Context
  - url: examples/stytch-send-magic-link-example.json
    type: Example
  - url: examples/stytch-create-organization-example.json
    type: Example
  - type: Features
    data:
      - Pay As You Go base $0; 10K MAUs included
      - 5 SSO/SCIM connections included; $125/mo per additional
      - 1K M2M tokens included
      - Fraud prevention 10K fingerprints free; $0.005 per additional
      - 'Brand customization + Stytch removal: $99 one-time'
      - 'Enterprise: 99.99% SLA, HIPAA/BAA, dedicated support'
      - 'Authentication: passwords, magic links, OAuth, biometrics, SSO'
      - B2B SaaS Authentication API (Organizations + RBAC)
      - Consumer Authentication API
      - 'Default API rate limit: 100 req/sec/project'
      - Webhooks for auth events
      - Bearer token + API keys (project-scoped)
      - OAuth 2.0 + OIDC + SAML
      - MFA (TOTP, SMS, biometric, security keys)
      - Device Fingerprinting for fraud prevention
      - M2M token issuance for service-to-service auth
    sources:
      - https://stytch.com/pricing
    updated: '2026-05-04'
---
