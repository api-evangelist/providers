---
aid: authentik
name: Authentik
description: |
  Authentik is an open source identity provider with a comprehensive REST API for managing users, groups, flows, providers, sources, policies, and outposts. It supports OAuth2, OIDC, SAML, LDAP, SCIM, and RADIUS protocols with official client SDKs in TypeScript, Python, Go, Rust, Kotlin, and Swift.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Authorization
  - Identity Provider
  - LDAP
  - OAuth
  - Open Source
  - OpenID Connect
  - SAML
  - SCIM
  - Self-Hosted
url: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: authentik:authentik-rest-api
    name: Authentik REST API
    description: |
      The authentik REST API v3 provides complete management of the authentik identity platform including users, groups, tokens, flows, providers, sources, policies, outposts, events, and configuration. Every authentik instance includes a built-in API browser at /api/v3/.
    humanURL: https://api.goauthentik.io/
    baseURL: https://your-authentik-instance.example.com/api/v3
    tags:
      - Authentication
      - Identity
      - REST
      - Users
    properties:
      - type: Documentation
        url: https://docs.goauthentik.io/developer-docs/api/
      - type: OpenAPI
        url: https://api.goauthentik.io/#/Schema/schema_retrieve
      - type: APIReference
        url: https://api.goauthentik.io/
      - type: SDK
        url: https://pypi.org/project/authentik-client/
      - type: SDK
        url: https://www.npmjs.com/package/@goauthentik/api
      - type: GitHubRepository
        url: https://github.com/goauthentik/authentik
common:
  - type: Website
    url: https://goauthentik.io
  - type: Documentation
    url: https://docs.goauthentik.io
  - type: GitHubOrganization
    url: https://github.com/goauthentik
  - type: GitHubRepository
    url: https://github.com/goauthentik/authentik
  - type: ChangeLog
    url: https://github.com/goauthentik/authentik/releases
  - type: Support
    url: https://github.com/goauthentik/authentik/discussions
  - type: Community
    url: https://discord.gg/jg33eMhnj6
  - type: Pricing
    url: https://goauthentik.io/pricing
  - type: Features
    data:
      - name: Comprehensive REST API
        description: Full REST API covering all authentik features with built-in Swagger UI at /api/v3/ on every instance.
      - name: Multi-Protocol Support
        description: Native support for OAuth2, OIDC, SAML, LDAP, SCIM, RADIUS, and SSTP protocols for broad integration coverage.
      - name: Flow Engine
        description: Customizable authentication and enrollment flows with visual flow designer for configuring multi-step authentication processes.
      - name: Multi-Language SDKs
        description: Official API client SDKs in TypeScript, Python, Go, Rust, Kotlin, and Swift auto-generated from the OpenAPI schema.
      - name: Terraform Provider
        description: Official Terraform provider for infrastructure-as-code management of authentik resources.
      - name: Helm Deployment
        description: Official Helm chart for Kubernetes deployment with configurable replicas, persistence, and external database support.
      - name: RBAC
        description: Role-based access control for granular permission management across authentik resources and administrative functions.
  - type: UseCases
    data:
      - name: Self-Hosted Identity Provider
        description: Deploy a complete identity provider on-premises or in private cloud with full data sovereignty.
      - name: SSO Gateway
        description: Provide single sign-on for all internal applications using OIDC, SAML, or LDAP protocol support.
      - name: B2C Identity
        description: Build customer-facing registration and authentication flows with customizable enrollment and recovery processes.
      - name: Zero Trust Access
        description: Implement zero trust application access with forward auth proxy integration and per-application policies.
  - type: Integrations
    data:
      - name: Nginx/Traefik/Caddy
        description: Forward auth integration with major reverse proxies for transparent application authentication.
      - name: Kubernetes
        description: Native Kubernetes deployment via Helm chart with optional operator and RBAC integration.
      - name: LDAP Directory
        description: LDAP outpost that exposes authentik users to LDAP-compatible applications without a directory server.
      - name: Grafana
        description: Native OAuth2 integration with Grafana for unified authentication in monitoring stacks.
      - name: Nextcloud
        description: OIDC or SAML integration with Nextcloud for unified login in self-hosted file storage.
  - type: Solutions
    data:
      - name: Self-Hosted IAM
        description: Complete identity and access management platform deployable on any infrastructure with no vendor lock-in.
      - name: Application Gateway
        description: Secure and authenticate any application using forward auth with optional MFA and per-user access policies.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
