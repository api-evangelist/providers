---
aid: authelia
name: Authelia
description: |
  Authelia is an open source authentication and authorization server providing multi-factor authentication and single sign-on for applications behind a reverse proxy. It supports OpenID Connect 1.0, OAuth 2.0, TOTP, WebAuthn, and Duo Push as authentication methods. Authelia exposes a REST API documented with an OpenAPI specification and integrates with nginx, Traefik, Caddy, and other reverse proxies.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Authorization
  - LDAP
  - MFA
  - Open Source
  - OpenID Connect
  - Self-Hosted
  - SSO
url: https://raw.githubusercontent.com/api-evangelist/authelia/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: authelia:authelia-rest-api
    name: Authelia REST API
    description: |
      The Authelia REST API provides endpoints for authentication flows including first-factor login, MFA challenges, password reset, session management, and authorization verification for reverse proxy integration.
    humanURL: https://www.authelia.com/reference/
    baseURL: https://your-authelia-instance.example.com/api
    tags:
      - Authentication
      - Authorization
      - MFA
      - REST
      - SSO
    properties:
      - type: Documentation
        url: https://www.authelia.com/reference/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/authelia/authelia/master/api/openapi.yml
      - type: GitHubRepository
        url: https://github.com/authelia/authelia
  - aid: authelia:authelia-oidc-provider
    name: Authelia OpenID Connect 1.0 Provider
    description: |
      Authelia acts as an OpenID Certified OpenID Connect 1.0 Provider supporting Authorization Code, Implicit, and Hybrid flows with PKCE, PAR, and various token endpoint authentication methods.
    humanURL: https://www.authelia.com/configuration/identity-providers/openid-connect/provider/
    baseURL: https://your-authelia-instance.example.com
    tags:
      - Authentication
      - OAuth
      - OIDC
      - OpenID Connect
    properties:
      - type: Documentation
        url: https://www.authelia.com/configuration/identity-providers/openid-connect/provider/
common:
  - type: Website
    url: https://www.authelia.com
  - type: Documentation
    url: https://www.authelia.com/configuration/prologue/introduction/
  - type: GitHubOrganization
    url: https://github.com/authelia
  - type: GitHubRepository
    url: https://github.com/authelia/authelia
  - type: ChangeLog
    url: https://github.com/authelia/authelia/releases
  - type: Support
    url: https://github.com/authelia/authelia/discussions
  - type: Community
    url: https://discord.gg/authelia
  - type: Features
    data:
      - name: Multi-Factor Authentication
        description: Supports TOTP, WebAuthn/FIDO2, Duo Push, and mobile authenticator apps as second factors.
      - name: OpenID Connect 1.0 Provider
        description: OpenID Certified identity provider supporting Authorization Code, Implicit, and Hybrid flows.
      - name: Single Sign-On
        description: Session-based SSO across all applications behind the reverse proxy with configurable session lifetime.
      - name: LDAP/Active Directory Integration
        description: User authentication against LDAP, Active Directory, and OpenLDAP directories with group-based access control.
      - name: Access Control Rules
        description: Fine-grained access control policies based on domain, path, user, group, and network for precise authorization.
      - name: Reverse Proxy Integration
        description: Native integration with nginx, Traefik, Caddy, HAProxy, Envoy, and Skipper via forward-auth and ExtAuthz endpoints.
      - name: Passwordless Authentication
        description: Support for WebAuthn/FIDO2 passwordless login using hardware security keys and platform authenticators.
  - type: UseCases
    data:
      - name: Self-Hosted SSO
        description: Deploy a self-hosted SSO solution for internal web applications and services without relying on cloud identity providers.
      - name: Homelab Security
        description: Protect self-hosted homelab applications with MFA and access control without exposing them to the internet unprotected.
      - name: Small Business Identity
        description: Provide centralized authentication for small business web applications using LDAP and access control policies.
      - name: OIDC Provider
        description: Act as an OpenID Connect provider for applications requiring OAuth 2.0 and OIDC-based authentication flows.
  - type: Integrations
    data:
      - name: Nginx
        description: Integration with nginx-based proxies including nginx, nginx-proxy-manager, and Swag via auth_request module.
      - name: Traefik
        description: Native Traefik middleware integration via ForwardAuth for seamless authentication in Docker and Kubernetes environments.
      - name: Caddy
        description: Caddy forward-auth integration for protecting applications behind the Caddy web server.
      - name: LDAP/Active Directory
        description: User directory integration with LDAP, Active Directory, and FreeIPA for enterprise user management.
      - name: Helm
        description: Official Helm chart available at the authelia/chartrepo GitHub repository for Kubernetes deployment.
  - type: Solutions
    data:
      - name: Self-Hosted Identity
        description: Complete self-hosted identity and access management solution for privacy-conscious deployments.
      - name: Zero Trust Security
        description: Enforce zero trust network access policies for internal applications with per-request authentication verification.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
