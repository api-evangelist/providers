---
aid: microsoft-entra
url: https://raw.githubusercontent.com/api-evangelist/microsoft-entra/refs/heads/main/apis.yml
apis:
- name: Microsoft Entra ID (Azure AD) API
  description: Core identity and access management API for user authentication, authorization, and directory management.
  image: https://www.microsoft.com/en-us/security/content/dam/microsoft/final/security/includes/microsoft-entra-logo.svg
  humanUrl: https://learn.microsoft.com/en-us/graph/azuread-identity-access-management-concept-overview
  baseUrl: https://graph.microsoft.com/v1.0
  tags:
  - Authentication
  - Authorization
  - Directory
  - Groups
  - Identity
  - Users
  properties:
  - type: OpenAPI
    url: openapi/microsoft-entra-graph-identity-openapi.yml
  - type: Documentation
    url: https://learn.microsoft.com/en-us/entra/identity/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: SDKs
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: Pricing
    url: https://www.microsoft.com/en-us/security/business/microsoft-entra-pricing
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/graph/tutorial-applications-basics
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/identity-network-access-overview
- name: Microsoft Entra ID Protection API
  description: API for identity risk detection, investigation, and remediation.
  humanUrl: https://learn.microsoft.com/en-us/graph/api/resources/identityprotection-overview
  baseUrl: https://graph.microsoft.com/v1.0
  tags:
  - Identity Protection
  - Risk Detection
  - Security
  - Threat Protection
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/entra/id-protection/
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/identityprotectionroot
- name: Microsoft Entra Conditional Access API
  description: API for managing conditional access policies and controls.
  humanUrl: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccessroot
  baseUrl: https://graph.microsoft.com/v1.0
  tags:
  - Access Control
  - Conditional Access
  - Policies
  - Security
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/entra/identity/conditional-access/
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccessroot
- name: Microsoft Entra Privileged Identity Management API
  description: API for managing privileged access and just-in-time administration.
  humanUrl: https://learn.microsoft.com/en-us/graph/api/resources/privilegedidentitymanagementv3-overview
  baseUrl: https://graph.microsoft.com/v1.0
  tags:
  - Just-In-Time
  - PIM
  - Privileged Access
  - Role Management
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/privilegedidentitymanagementv3-overview
- name: Microsoft Entra Verified ID API
  description: API for issuing and verifying decentralized identity credentials.
  humanUrl: https://learn.microsoft.com/en-us/entra/verified-id/
  baseUrl: https://verifiedid.did.msidentity.com/v1.0
  tags:
  - Decentralized Identity
  - DID
  - SSI
  - Verifiable Credentials
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/entra/verified-id/verifiable-credentials-configure-tenant
  - type: API Reference
    url: https://learn.microsoft.com/en-us/entra/verified-id/get-started-request-api
  - type: Admin API Reference
    url: https://learn.microsoft.com/en-us/entra/verified-id/admin-api
- name: Microsoft Entra External ID API
  description: API for managing customer and partner identity and access management.
  humanUrl: https://learn.microsoft.com/en-us/entra/external-id/
  baseUrl: https://graph.microsoft.com/v1.0
  tags:
  - B2B
  - B2C
  - Customer Identity
  - External Identities
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/entra/external-id/external-identities-overview
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/identity-network-access-overview
  - type: Native Authentication API Reference
    url: https://learn.microsoft.com/en-us/entra/identity-platform/reference-native-authentication-api
- name: Microsoft Entra ID Governance API
  description: API for managing identity governance including access reviews, entitlement management, and lifecycle workflows to ensure the right people have the right access at the right time.
  humanUrl: https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-overview
  baseUrl: https://graph.microsoft.com/v1.0
  tags:
  - Access Reviews
  - Compliance
  - Entitlement Management
  - Identity Governance
  - Lifecycle Workflows
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-overview
  - type: Access Reviews API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/accessreviewsv2-overview
  - type: Entitlement Management API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/entitlementmanagement-overview
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/graph/tutorial-access-package-api
- name: Microsoft Entra Application Management API
  description: API for registering, configuring, and managing applications and service principals in Microsoft Entra ID.
  humanUrl: https://learn.microsoft.com/en-us/graph/applications-concept-overview
  baseUrl: https://graph.microsoft.com/v1.0
  tags:
  - App Registration
  - Applications
  - Credentials
  - OAuth
  - Service Principals
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/applications-api-overview
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/applications-api-overview
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/graph/tutorial-applications-basics
  - type: Policy API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/applicationauthenticationmethodpolicy
- name: Microsoft Entra Authentication Methods API
  description: API for managing user authentication methods including FIDO2 security keys, passwordless phone sign-in, Microsoft Authenticator, and MFA registration.
  humanUrl: https://learn.microsoft.com/en-us/graph/api/resources/authenticationmethods-overview
  baseUrl: https://graph.microsoft.com/v1.0
  tags:
  - Authentication Methods
  - FIDO2
  - MFA
  - Passkeys
  - Passwordless
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/authenticationmethods-overview
  - type: Policy API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/authenticationmethodspolicies-overview
  - type: Authentication Strengths API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/authenticationstrengths-overview
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/graph/authenticationmethods-get-started
- name: Microsoft Entra Workload ID API
  description: API for managing and securing identities for software workloads such as applications, services, scripts, and containers.
  humanUrl: https://learn.microsoft.com/en-us/entra/workload-id/
  baseUrl: https://graph.microsoft.com/v1.0
  tags:
  - Managed Identities
  - Service Principals
  - Workload Identities
  - Workload Identity Federation
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview
  - type: Workload Identity Federation
    url: https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation
- name: Microsoft Entra Provisioning API
  description: API for automating user provisioning and deprovisioning using SCIM protocol, including API-driven inbound provisioning from any system of record.
  humanUrl: https://learn.microsoft.com/en-us/entra/identity/app-provisioning/inbound-provisioning-api-concepts
  baseUrl: https://graph.microsoft.com/v1.0
  tags:
  - Inbound Provisioning
  - Provisioning
  - SCIM
  - Synchronization
  - User Lifecycle
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/entra/identity/app-provisioning/how-provisioning-works
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/synchronization-overview
  - type: Inbound Provisioning API
    url: https://learn.microsoft.com/en-us/entra/identity/app-provisioning/inbound-provisioning-api-concepts
  - type: SCIM Reference
    url: https://learn.microsoft.com/en-us/entra/architecture/sync-scim
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/entra/identity/app-provisioning/inbound-provisioning-api-configure-app
- name: Microsoft Entra Global Secure Access API
  description: API for managing Microsoft Entra Internet Access and Microsoft Entra Private Access, providing identity-centric secure web gateway and zero-trust network access.
  humanUrl: https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access
  baseUrl: https://graph.microsoft.com/beta
  tags:
  - Internet Access
  - Network Security
  - Private Access
  - Secure Web Gateway
  - Zero Trust
  - ZTNA
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/entra/global-secure-access/
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/networkaccess-global-secure-access-api-overview
  - type: Private Access Documentation
    url: https://learn.microsoft.com/en-us/entra/global-secure-access/concept-private-access
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/graph/tutorial-entra-private-access
- name: Microsoft Identity Platform API
  description: API endpoints for OAuth 2.0, OpenID Connect, and SAML authentication protocols enabling application integration with Microsoft Entra ID.
  humanUrl: https://learn.microsoft.com/en-us/entra/identity-platform/
  baseUrl: https://login.microsoftonline.com
  tags:
  - Identity Platform
  - OAuth 2.0
  - OpenID Connect
  - SAML
  - Token Service
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/entra/identity-platform/
  - type: OAuth 2.0 Reference
    url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols
  - type: OpenID Connect Reference
    url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc
  - type: Authorization Code Flow
    url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow
  - type: On-Behalf-Of Flow
    url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow
- name: Microsoft Entra Agent ID API
  description: API for creating, securing, and monitoring AI agent identities, providing authentication, authorization, and lifecycle management for AI agents.
  humanUrl: https://learn.microsoft.com/en-us/graph/api/resources/agentid-platform-overview
  baseUrl: https://graph.microsoft.com/beta
  tags:
  - Agent Identity
  - Agent Registry
  - AI Agents
  - Machine Identity
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/agentid-platform-overview
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/interactive-agent-request-user-tokens
name: Microsoft Entra
tags:
- Access Management
- Authentication
- Azure AD
- Entra
- Identity
- Identity Governance
- Microsoft
- Network Security
- Security
- Zero Trust
type: Contract
image: https://www.microsoft.com/en-us/security/content/dam/microsoft/final/security/includes/microsoft-entra-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Entra (formerly Azure Active Directory) provides identity and access management services including authentication, authorization, and directory services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

