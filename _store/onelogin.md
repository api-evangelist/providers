---
aid: onelogin
name: OneLogin
description: OneLogin is an identity and access management platform providing single sign-on (SSO), multi-factor authentication, user provisioning, and a RESTful API for managing users, roles, applications, MFA, branding, connectors, reports, SAML assertions, smart hooks, and Vigilance AI.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Identity
  - Access Management
  - Single Sign-On
  - Multi-Factor Authentication
  - SAML
  - OAuth
created: '2025-01-08'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/onelogin/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: onelogin:onelogin
    name: OneLogin API
    description: OneLogin REST API for identity and access management. The API follows RESTful principles, is secured by OAuth 2.0, and provides JSON messages with search, pagination, sorting, and filtering. Resources include Users, Roles, Apps, App Rules, Branding, Connectors, MFA, Reports, SAML Assertions, Smart Hooks, Smart MFA, User Mappings, Self- Registration, and Vigilance AI.
    humanURL: https://developers.onelogin.com/api-docs/2/getting-started/dev-overview
    baseURL: https://<subdomain>.onelogin.com
    tags:
      - Identity
      - Access Management
      - Users
      - Roles
      - Apps
      - SAML
      - OAuth
    properties:
      - type: Documentation
        url: https://developers.onelogin.com/api-docs/2/getting-started/dev-overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/onelogin/refs/heads/main/openapi/onelogin-openapi.yml
      - type: Getting Started
        url: https://developers.onelogin.com/api-docs/2/getting-started/working-with-api-credentials
      - type: Authentication
        url: https://developers.onelogin.com/api-docs/2/oauth20-tokens/generate-tokens-2
common:
  - type: Website
    url: https://www.onelogin.com
  - type: Documentation
    url: https://developers.onelogin.com
  - type: Developer Portal
    url: https://developers.onelogin.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
