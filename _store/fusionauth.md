---
aid: fusionauth
name: FusionAuth
type: Index
description: FusionAuth is a developer-focused customer identity and access management (CIAM) platform that delivers authentication, authorization, registration, multi-factor authentication, single sign-on, OAuth2 and OpenID Connect, and user management capabilities through a comprehensive REST API and self-hostable identity service.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Authorization
  - Identity
  - CIAM
  - OAuth
  - OpenID Connect
  - Single Sign-On
  - Multi-Factor Authentication
created: '2024-09-26'
modified: '2026-04-28'
position: Consumer
access: 3rd-Party
url: https://raw.githubusercontent.com/api-evangelist/fusionauth/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: fusionauth:fusionauth
    name: FusionAuth API
    description: The FusionAuth API exposes the platform's complete authentication, authorization, user management, OAuth2/OIDC, multi-factor, tenant, application, and administrative surface as a REST API. An upstream OpenAPI 3.0 specification is published and maintained by FusionAuth.
    humanURL: https://fusionauth.io/docs/
    baseURL: https://sandbox.fusionauth.io
    tags:
      - Authentication
      - Authorization
      - Identity
      - CIAM
      - OAuth
      - OpenID Connect
    properties:
      - type: Documentation
        url: https://fusionauth.io/docs/apis/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/FusionAuth/fusionauth-openapi/main/openapi.yaml
      - type: SDKs
        url: https://fusionauth.io/docs/sdks/
common:
  - type: Getting Started
    url: https://fusionauth.io/docs/get-started/
  - type: SDKs
    url: https://fusionauth.io/docs/sdks/
  - type: Change Log
    url: https://fusionauth.io/docs/release-notes/
  - type: Blog
    url: https://fusionauth.io/blog/
  - type: Login
    url: https://login.fusionauth.io/oauth2/authorize
  - type: Sign Up
    url: https://login.fusionauth.io/oauth2/register
  - type: Privacy Policy
    url: https://fusionauth.io/privacy-policy
  - type: GitHub Organization
    url: https://github.com/fusionauth
  - type: Pricing
    url: https://fusionauth.io/pricing
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
