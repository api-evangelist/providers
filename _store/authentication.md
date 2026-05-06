---
aid: authentication
name: Authentication
description: |
  A curated index of services, tooling, and open source solutions for API authentication, authorization, identity management, and secrets management. This collection covers identity providers, SSO platforms, privileged access management, MFA, open source identity servers, and authentication standards including OAuth 2.0, OpenID Connect, SAML 2.0, FIDO2/WebAuthn, and SCIM.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Authorization
  - Identity
  - MFA
  - OAuth
  - OpenID Connect
  - SAML
  - Security
  - SSO
url: https://raw.githubusercontent.com/api-evangelist/authentication/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-19'
specificationVersion: '0.19'
network:
  - name: Amazon Cognito
    url: https://raw.githubusercontent.com/api-evangelist/aws-cognito/refs/heads/main/apis.yml
  - name: Auth0
    url: https://raw.githubusercontent.com/api-evangelist/auth0/refs/heads/main/apis.yml
  - name: Authelia
    url: https://raw.githubusercontent.com/api-evangelist/authelia/refs/heads/main/apis.yml
  - name: Authentik
    url: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/apis.yml
  - name: Casdoor
    url: https://raw.githubusercontent.com/api-evangelist/casdoor/refs/heads/main/apis.yml
  - name: Cerbos
    url: https://raw.githubusercontent.com/api-evangelist/cerbos/refs/heads/main/apis.yml
  - name: CyberArk
    url: https://raw.githubusercontent.com/api-evangelist/cyberark/refs/heads/main/apis.yml
  - name: Duo Security
    url: https://raw.githubusercontent.com/api-evangelist/duo-security/refs/heads/main/apis.yml
  - name: ForgeRock
    url: https://raw.githubusercontent.com/api-evangelist/forgerock/refs/heads/main/apis.yml
  - name: HashiCorp Vault
    url: https://raw.githubusercontent.com/api-evangelist/hashicorp-vault/refs/heads/main/apis.yml
  - name: Keycloak
    url: https://raw.githubusercontent.com/api-evangelist/keycloak/refs/heads/main/apis.yml
  - name: Logto
    url: https://raw.githubusercontent.com/api-evangelist/logto/refs/heads/main/apis.yml
  - name: Microsoft Entra ID
    url: https://raw.githubusercontent.com/api-evangelist/microsoft-entra-id/refs/heads/main/apis.yml
  - name: Okta
    url: https://raw.githubusercontent.com/api-evangelist/okta/refs/heads/main/apis.yml
  - name: OneLogin
    url: https://raw.githubusercontent.com/api-evangelist/onelogin/refs/heads/main/apis.yml
  - name: Ory
    url: https://raw.githubusercontent.com/api-evangelist/ory/refs/heads/main/apis.yml
  - name: Ping Identity
    url: https://raw.githubusercontent.com/api-evangelist/ping-identity/refs/heads/main/apis.yml
  - name: SailPoint
    url: https://raw.githubusercontent.com/api-evangelist/sailpoint/refs/heads/main/apis.yml
  - name: SuperTokens
    url: https://raw.githubusercontent.com/api-evangelist/supertokens/refs/heads/main/apis.yml
  - name: WorkOS
    url: https://raw.githubusercontent.com/api-evangelist/workos/refs/heads/main/apis.yml
  - name: Zitadel
    url: https://raw.githubusercontent.com/api-evangelist/zitadel/refs/heads/main/apis.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Features
    data:
      - name: OAuth 2.0 Protocol Coverage
        description: Comprehensive coverage of OAuth 2.0 authorization framework implementations from cloud providers, open source projects, and commercial platforms.
      - name: OpenID Connect Providers
        description: Index of OpenID Connect certified identity providers and implementations spanning cloud, on-premises, and self-hosted deployments.
      - name: Multi-Factor Authentication
        description: Coverage of MFA solutions including TOTP, SMS, push notification, WebAuthn/FIDO2, and hardware token implementations.
      - name: Self-Hosted Identity Solutions
        description: Open source identity servers that can be self-hosted including Keycloak, Authelia, Authentik, Zitadel, and Casdoor.
      - name: Enterprise Identity Providers
        description: Commercial enterprise IAM platforms including Okta, Auth0, ForgeRock, Ping Identity, and Microsoft Entra ID.
      - name: Secrets and PAM
        description: Privileged access management and secrets management tools including HashiCorp Vault and CyberArk for secure credential storage.
  - type: UseCases
    data:
      - name: Identity Provider Selection
        description: Compare authentication platforms across self-hosted, cloud, and enterprise tiers to select the right identity provider.
      - name: SSO Implementation
        description: Find SSO platforms and libraries for implementing single sign-on across applications and services.
      - name: API Security Research
        description: Research authentication standards, security patterns, and best practices for securing REST, GraphQL, and gRPC APIs.
      - name: Zero Trust Architecture
        description: Discover identity verification services for zero trust network access and continuous authentication architectures.
  - type: Integrations
    data:
      - name: OAuth 2.0 Standard
        description: The foundational authorization framework implemented by every provider in this collection.
      - name: OpenID Connect Standard
        description: Identity layer on top of OAuth 2.0 providing standardized user info, ID tokens, and discovery endpoints.
      - name: SAML 2.0 Standard
        description: XML-based authentication standard widely used for enterprise SSO and federation scenarios.
      - name: SCIM 2.0 Standard
        description: System for Cross-domain Identity Management for automated user provisioning and deprovisioning.
      - name: FIDO2/WebAuthn Standard
        description: Web Authentication standard for passwordless and hardware-backed authentication.
---
