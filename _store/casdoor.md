---
aid: casdoor
name: Casdoor
description: Casdoor is an open-source, AI-first identity and access management (IAM) and MCP gateway authentication server with a web UI. Built in Go (Beego) with a React frontend, Casdoor supports OAuth 2.0, OIDC, SAML 2.0, CAS, LDAP, Kerberos/SPNEGO, WebAuthn / Passkeys, TOTP / MFA, SCIM 2.0 provisioning, social login, multi-tenant organizations, role-based access control, and an MCP Gateway plus A2A Protocol for agent-to-agent communication. The platform exposes a RESTful API documented via Swagger and ships SDKs for Go, Java, Python, Node.js, C#, C++, PHP, Ruby, JavaScript, Lua, and Haskell. Released under the Apache License 2.0.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Authorization
  - IAM
  - Identity
  - LDAP
  - MCP
  - MFA
  - OAuth
  - OIDC
  - Open Source
  - Passkeys
  - SAML
  - SCIM
  - Single Sign-On
  - SSO
  - WebAuthn
url: https://raw.githubusercontent.com/api-evangelist/casdoor/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: casdoor:casdoor-rest-api
    name: Casdoor REST API
    description: The Casdoor REST API provides programmatic access to the IAM platform's core resources including users, organizations, applications, roles, groups, permissions, identity providers, tokens, sessions, certificates, adapters, syncers, webhooks, products, payments, MFA enrollments, and enforcers. The API follows RESTful conventions with JSON payloads and is documented via a hosted Swagger UI.
    humanURL: https://casdoor.ai/docs/basic/api
    baseURL: https://door.casdoor.com
    tags:
      - Applications
      - IAM
      - Organizations
      - REST
      - Roles
      - Sessions
      - Tokens
      - Users
    properties:
      - type: Documentation
        url: https://casdoor.ai/docs/basic/api
      - type: Swagger
        url: https://door.casdoor.com/swagger/
      - type: GitHub Repository
        url: https://github.com/casdoor/casdoor
      - type: Authentication
        url: https://casdoor.ai/docs/basic/core-concepts
  - aid: casdoor:casdoor-oauth-oidc
    name: Casdoor OAuth 2.0 / OIDC Provider
    description: Casdoor implements an OAuth 2.0 authorization server and OpenID Connect identity provider, exposing the standard authorization, token, userinfo, revocation, introspection, JWKS, and OIDC discovery endpoints used by web, mobile, native, and machine-to-machine clients to obtain ID tokens and access tokens.
    humanURL: https://casdoor.ai/docs/how-to-connect/oauth
    tags:
      - Authentication
      - JWT
      - OAuth
      - OIDC
      - SSO
      - Tokens
    properties:
      - type: Documentation
        url: https://casdoor.ai/docs/how-to-connect/oauth
      - type: Discovery
        url: https://door.casdoor.com/.well-known/openid-configuration
      - type: Specification
        url: https://datatracker.ietf.org/doc/html/rfc6749
  - aid: casdoor:casdoor-saml
    name: Casdoor SAML 2.0 Identity Provider
    description: SAML 2.0 identity provider endpoints in Casdoor that issue SAML assertions to enterprise service providers, supporting SSO scenarios for legacy and enterprise SaaS applications via standard SAML metadata, ACS, and SLO bindings.
    humanURL: https://casdoor.ai/docs/how-to-connect/saml
    tags:
      - Enterprise SSO
      - Federation
      - SAML
      - SSO
    properties:
      - type: Documentation
        url: https://casdoor.ai/docs/how-to-connect/saml
      - type: Specification
        url: http://docs.oasis-open.org/security/saml/v2.0/
  - aid: casdoor:casdoor-cas
    name: Casdoor CAS Server
    description: Casdoor exposes a CAS (Central Authentication Service) server compatible with CAS protocol versions 1.0, 2.0, and 3.0, providing single sign-on to applications that integrate via the CAS ticket-validation flow.
    humanURL: https://casdoor.ai/docs/how-to-connect/cas
    tags:
      - Authentication
      - CAS
      - SSO
    properties:
      - type: Documentation
        url: https://casdoor.ai/docs/how-to-connect/cas
  - aid: casdoor:casdoor-ldap
    name: Casdoor LDAP Server
    description: Casdoor provides an LDAP server interface so that legacy applications and infrastructure components requiring LDAP authentication can bind against Casdoor users and groups, and a sync engine that imports users from external LDAP directories.
    humanURL: https://casdoor.ai/docs/ldap/overview
    tags:
      - Directory
      - LDAP
      - Sync
    properties:
      - type: Documentation
        url: https://casdoor.ai/docs/ldap/overview
  - aid: casdoor:casdoor-scim
    name: Casdoor SCIM 2.0 API
    description: SCIM 2.0 (System for Cross-domain Identity Management) endpoints for automated user and group provisioning between Casdoor and downstream identity-aware systems.
    humanURL: https://casdoor.ai/docs/scim/overview
    tags:
      - Identity
      - Provisioning
      - SCIM
    properties:
      - type: Documentation
        url: https://casdoor.ai/docs/scim/overview
      - type: Specification
        url: https://datatracker.ietf.org/doc/html/rfc7644
  - aid: casdoor:casdoor-mcp-gateway
    name: Casdoor MCP Gateway
    description: Casdoor's MCP (Model Context Protocol) gateway and A2A (Agent-to-Agent) protocol surface, designed to broker authentication and authorization for AI agents and MCP-aware tooling using Casdoor as the identity provider.
    humanURL: https://casdoor.ai/docs/mcp/overview
    tags:
      - A2A
      - Agents
      - AI
      - MCP
    properties:
      - type: Documentation
        url: https://casdoor.ai/docs/mcp/overview
  - aid: casdoor:casdoor-webhooks
    name: Casdoor Webhooks
    description: Outbound webhook events that notify external systems of identity events such as user signup, login, logout, profile changes, password resets, and MFA enrollments.
    humanURL: https://casdoor.ai/docs/integration/webhook
    tags:
      - Events
      - Integration
      - Webhooks
    properties:
      - type: Documentation
        url: https://casdoor.ai/docs/integration/webhook
common:
  - type: Website
    url: https://casdoor.org
  - type: Documentation
    url: https://casdoor.ai/docs/overview
  - type: GettingStarted
    url: https://casdoor.ai/docs/basic/server-installation
  - type: Authentication
    url: https://casdoor.ai/docs/basic/core-concepts
  - type: Swagger
    url: https://door.casdoor.com/swagger/
  - type: GitHub
    url: https://github.com/casdoor/casdoor
  - type: GitHubOrganization
    url: https://github.com/casdoor
  - type: SourceCode
    url: https://github.com/casdoor/casdoor
  - type: IssueTracker
    url: https://github.com/casdoor/casdoor/issues
  - type: Blog
    url: https://casdoor.org/blog
  - type: Community
    url: https://casdoor.ai/docs/community/forum
  - type: Discord
    url: https://discord.gg/5rPsrAzK7S
  - type: License
    url: https://github.com/casdoor/casdoor/blob/master/LICENSE
  - type: DockerHub
    url: https://hub.docker.com/r/casbin/casdoor
  - type: Demo
    url: https://door.casdoor.com
  - type: PrivacyPolicy
    url: https://casdoor.org/privacy
  - type: Pricing
    url: https://casdoor.com/pricing
  - name: Features
    type: Features
    data:
      - name: OAuth 2.0 Server
      - name: OIDC Provider
      - name: SAML 2.0 IdP
      - name: CAS Server
      - name: LDAP Server
      - name: SCIM 2.0 Provisioning
      - name: WebAuthn / Passkeys
      - name: TOTP MFA
      - name: Face ID Biometrics
      - name: Social Login
      - name: RBAC
      - name: ABAC
      - name: ACL
      - name: Multi-Tenancy
      - name: Organizations
      - name: Audit Logs
      - name: Webhooks
      - name: Identity Provider Federation
      - name: MCP Gateway
      - name: A2A Protocol
      - name: Self-Hosted
      - name: Apache 2.0 License
  - name: UseCases
    type: UseCases
    data:
      - name: Single Sign-On
      - name: Customer Identity (CIAM)
      - name: Workforce Identity
      - name: Passwordless Login
      - name: Multi-Factor Authentication
      - name: Enterprise SSO via SAML
      - name: API Authorization
      - name: Identity Provider for AI Agents
      - name: User Provisioning Automation
      - name: Self-Hosted Auth Server
  - name: Integrations
    type: Integrations
    data:
      - name: GitHub
      - name: Google
      - name: Azure AD
      - name: WeChat
      - name: QQ
      - name: MySQL
      - name: PostgreSQL
      - name: SQL Server
      - name: Redis
      - name: Beego
      - name: React
      - name: Casbin
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
