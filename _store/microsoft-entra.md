---
aid: microsoft-entra
name: Microsoft Entra
description: Microsoft Entra (formerly Azure Active Directory) provides identity and access management services including authentication, authorization, and directory services.
url: https://raw.githubusercontent.com/api-evangelist/microsoft-entra/refs/heads/main/apis.yml
image: https://www.microsoft.com/en-us/security/content/dam/microsoft/final/security/includes/microsoft-entra-logo.svg
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
type: Index
access: 3rd-Party
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
apis:
  - aid: microsoft-entra:graph-identity
    name: Microsoft Entra ID (Azure AD) API
    description: Core identity and access management API for user authentication, authorization, and directory management.
    image: https://www.microsoft.com/en-us/security/content/dam/microsoft/final/security/includes/microsoft-entra-logo.svg
    humanURL: https://learn.microsoft.com/en-us/graph/azuread-identity-access-management-concept-overview
    baseURL: https://graph.microsoft.com/v1.0
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
      - type: SDK
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: Pricing
        url: https://www.microsoft.com/en-us/security/business/microsoft-entra-pricing
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/tutorial-applications-basics
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/identity-network-access-overview
  - aid: microsoft-entra:id-protection
    name: Microsoft Entra ID Protection API
    description: API for identity risk detection, investigation, and remediation.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/identityprotection-overview
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Identity Protection
      - Risk Detection
      - Security
      - Threat Protection
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/id-protection/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/identityprotectionroot
  - aid: microsoft-entra:conditional-access
    name: Microsoft Entra Conditional Access API
    description: API for managing conditional access policies and controls.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccessroot
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Access Control
      - Conditional Access
      - Policies
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/identity/conditional-access/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccessroot
  - aid: microsoft-entra:pim
    name: Microsoft Entra Privileged Identity Management API
    description: API for managing privileged access and just-in-time administration.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/privilegedidentitymanagementv3-overview
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Just-In-Time
      - PIM
      - Privileged Access
      - Role Management
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/privilegedidentitymanagementv3-overview
  - aid: microsoft-entra:verified-id
    name: Microsoft Entra Verified ID API
    description: API for issuing and verifying decentralized identity credentials.
    humanURL: https://learn.microsoft.com/en-us/entra/verified-id/
    baseURL: https://verifiedid.did.msidentity.com/v1.0
    tags:
      - Decentralized Identity
      - DID
      - SSI
      - Verifiable Credentials
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/verified-id/verifiable-credentials-configure-tenant
      - type: APIReference
        url: https://learn.microsoft.com/en-us/entra/verified-id/get-started-request-api
  - aid: microsoft-entra:external-id
    name: Microsoft Entra External ID API
    description: API for managing customer and partner identity and access management.
    humanURL: https://learn.microsoft.com/en-us/entra/external-id/
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - B2B
      - B2C
      - Customer Identity
      - External Identities
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/external-id/external-identities-overview
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/identity-network-access-overview
  - aid: microsoft-entra:id-governance
    name: Microsoft Entra ID Governance API
    description: API for managing identity governance including access reviews, entitlement management, and lifecycle workflows to ensure the right people have the right access at the right time.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-overview
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Access Reviews
      - Compliance
      - Entitlement Management
      - Identity Governance
      - Lifecycle Workflows
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-overview
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/tutorial-access-package-api
  - aid: microsoft-entra:application-management
    name: Microsoft Entra Application Management API
    description: API for registering, configuring, and managing applications and service principals in Microsoft Entra ID.
    humanURL: https://learn.microsoft.com/en-us/graph/applications-concept-overview
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - App Registration
      - Applications
      - Credentials
      - OAuth
      - Service Principals
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/applications-api-overview
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/applications-api-overview
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/tutorial-applications-basics
  - aid: microsoft-entra:authentication-methods
    name: Microsoft Entra Authentication Methods API
    description: API for managing user authentication methods including FIDO2 security keys, passwordless phone sign-in, Microsoft Authenticator, and MFA registration.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/authenticationmethods-overview
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Authentication Methods
      - FIDO2
      - MFA
      - Passkeys
      - Passwordless
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/authenticationmethods-overview
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/authenticationmethods-get-started
  - aid: microsoft-entra:workload-id
    name: Microsoft Entra Workload ID API
    description: API for managing and securing identities for software workloads such as applications, services, scripts, and containers.
    humanURL: https://learn.microsoft.com/en-us/entra/workload-id/
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Managed Identities
      - Service Principals
      - Workload Identities
      - Workload Identity Federation
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview
  - aid: microsoft-entra:provisioning
    name: Microsoft Entra Provisioning API
    description: API for automating user provisioning and deprovisioning using SCIM protocol, including API-driven inbound provisioning from any system of record.
    humanURL: https://learn.microsoft.com/en-us/entra/identity/app-provisioning/inbound-provisioning-api-concepts
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Inbound Provisioning
      - Provisioning
      - SCIM
      - Synchronization
      - User Lifecycle
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/identity/app-provisioning/how-provisioning-works
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/synchronization-overview
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/entra/identity/app-provisioning/inbound-provisioning-api-configure-app
  - aid: microsoft-entra:global-secure-access
    name: Microsoft Entra Global Secure Access API
    description: API for managing Microsoft Entra Internet Access and Microsoft Entra Private Access, providing identity-centric secure web gateway and zero-trust network access.
    humanURL: https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access
    baseURL: https://graph.microsoft.com/beta
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
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/networkaccess-global-secure-access-api-overview
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/tutorial-entra-private-access
  - aid: microsoft-entra:identity-platform
    name: Microsoft Identity Platform API
    description: API endpoints for OAuth 2.0, OpenID Connect, and SAML authentication protocols enabling application integration with Microsoft Entra ID.
    humanURL: https://learn.microsoft.com/en-us/entra/identity-platform/
    baseURL: https://login.microsoftonline.com
    tags:
      - Identity Platform
      - OAuth 2.0
      - OpenID Connect
      - SAML
      - Token Service
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/identity-platform/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols
  - aid: microsoft-entra:agent-id
    name: Microsoft Entra Agent ID API
    description: API for creating, securing, and monitoring AI agent identities, providing authentication, authorization, and lifecycle management for AI agents.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/agentid-platform-overview
    baseURL: https://graph.microsoft.com/beta
    tags:
      - Agent Identity
      - Agent Registry
      - AI Agents
      - Machine Identity
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/agentid-platform-overview
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/interactive-agent-request-user-tokens
common:
  - type: Portal
    url: https://entra.microsoft.com/
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/entra/fundamentals/
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/microsoft-entra-azure-ad-blog/bg-p/Identity
  - type: Support
    url: https://learn.microsoft.com/en-us/entra/fundamentals/how-to-get-support
  - type: StatusPage
    url: https://status.azure.com/
  - type: TermsOfService
    url: https://www.microsoft.com/licensing/terms/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/
  - type: ChangeLog
    url: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new
  - type: SDK
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: GitHubOrganization
    url: https://github.com/microsoftgraph
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: Pricing
    url: https://www.microsoft.com/en-us/security/business/microsoft-entra-pricing
  - type: JSONLD
    url: json-ld/microsoft-entra-context.jsonld
  - type: JSONSchema
    url: json-schema/microsoft-entra-user-schema.json
  - type: JSONSchema
    url: json-schema/microsoft-entra-application-schema.json
  - type: NaftikoCapability
    url: capabilities/shared/graph-identity.yaml
    title: Graph Identity API Shared Definition
  - type: NaftikoCapability
    url: capabilities/identity-and-access.yaml
    title: Identity and Access Management Workflow
  - type: Features
    data:
      - name: Identity and Access Management
        description: Manage user identities, authentication, and authorization across cloud and hybrid environments with single sign-on.
      - name: Conditional Access
        description: Enforce adaptive access policies based on user, device, location, and risk signals for zero trust security.
      - name: Identity Governance
        description: Automate access reviews, entitlement management, and lifecycle workflows to ensure proper access controls.
      - name: Privileged Identity Management
        description: Manage, control, and monitor privileged access with just-in-time and approval-based activation.
      - name: Verified ID
        description: Issue and verify decentralized identity credentials using open standards for portable, self-sovereign identity.
      - name: External Identities
        description: Enable secure collaboration with external partners and customers through B2B and B2C identity management.
      - name: Global Secure Access
        description: Provide identity-centric secure web gateway and zero-trust network access for internet and private resources.
      - name: Workload Identities
        description: Secure and manage identities for applications, services, scripts, and containers running as software workloads.
  - type: UseCases
    data:
      - name: Zero Trust Implementation
        description: Implement zero trust architecture with identity-based access controls, conditional access policies, and continuous verification.
      - name: Hybrid Identity Management
        description: Synchronize and manage identities across on-premises Active Directory and cloud environments.
      - name: Application Single Sign-On
        description: Enable SSO for thousands of SaaS and on-premises applications with SAML, OIDC, and password-based authentication.
      - name: Automated User Provisioning
        description: Automate user lifecycle management with SCIM-based provisioning and deprovisioning across integrated applications.
      - name: AI Agent Identity Management
        description: Create, secure, and monitor identities for AI agents with authentication, authorization, and lifecycle management.
  - type: Integrations
    data:
      - name: Microsoft 365
        description: Deep integration for identity and access management across all Microsoft 365 applications and services.
      - name: Azure Services
        description: Native identity provider for Azure resources including VMs, databases, storage, and managed identities.
      - name: Active Directory
        description: Hybrid identity synchronization with on-premises Active Directory using Azure AD Connect.
      - name: Salesforce
        description: SAML and SCIM integration for single sign-on and automated user provisioning with Salesforce.
      - name: ServiceNow
        description: SSO and automated provisioning integration with ServiceNow ITSM platform.
      - name: Workday
        description: Inbound provisioning from Workday HR to automate user lifecycle management.
      - name: SAP
        description: SSO and provisioning integration with SAP applications and S/4HANA.
      - name: Okta
        description: Cross-platform identity federation and migration support with Okta identity provider.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com/
---
