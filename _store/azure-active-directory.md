---
aid: microsoft-azure-active-directory
name: Microsoft Azure Active Directory
description: Microsoft Azure Active Directory (Azure AD), now Microsoft Entra ID, is Microsoft's cloud-based identity and access management service, which helps employees sign in and access resources.
type: Index
image: https://docs.microsoft.com/azure/media/index/active-directory.svg
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-active-directory/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Authentication
  - Authorization
  - Identity
  - Microsoft
  - Microsoft Entra
  - OAuth
  - OpenID Connect
  - SAML
  - SCIM
  - Single Sign-On
  - Zero Trust
apis:
  - name: Microsoft Graph API
    description: The Microsoft Graph API offers a single endpoint to access Azure AD data and other Microsoft 365 services.
    image: https://docs.microsoft.com/graph/images/microsoft-graph.png
    humanURL: https://docs.microsoft.com/en-us/graph/overview
    baseURL: https://graph.microsoft.com
    tags:
      - Graph
      - Groups
      - Identity
      - Users
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/graph/api/overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
      - type: OpenAPI
        url: openapi/microsoft-graph-identity-api.yml
      - type: Authentication
        url: https://docs.microsoft.com/en-us/graph/auth/
      - type: SDK
        url: https://docs.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/active-directory/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/use-the-api
      - type: Console
        url: https://developer.microsoft.com/en-us/graph/graph-explorer
        title: Graph Explorer
      - type: ChangeLog
        url: https://learn.microsoft.com/en-us/graph/changelog
  - name: Microsoft Graph Identity and Access API
    description: Microsoft Graph APIs for managing Microsoft Entra identity and network access capabilities, including user management, group management, application registration, conditional access policies, authentication methods, and identity governance.
    humanURL: https://learn.microsoft.com/en-us/graph/identity-network-access-overview
    baseURL: https://graph.microsoft.com
    tags:
      - Access Management
      - Authentication Methods
      - Conditional Access
      - Identity
      - Identity Governance
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/identity-network-access-overview?view=graph-rest-1.0
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccesspolicy?view=graph-rest-1.0
        title: Conditional Access Documentation
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-overview?view=graph-rest-1.0
        title: Identity Governance Documentation
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-conditional-access-dev-guide
        title: Developer Guide
      - type: OpenAPI
        url: openapi/microsoft-graph-identity-api.yml
      - type: JSONSchema
        url: json-schema/azure-active-directory-user-schema.json
      - type: JSONLD
        url: json-ld/azure-active-directory-context.jsonld
  - name: Azure AD Graph API (Deprecated)
    description: Legacy API for accessing Azure AD (deprecated in favor of Microsoft Graph).
    humanURL: https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-graph-api
    baseURL: https://graph.windows.net
    tags:
      - Deprecated
      - Identity
      - Legacy
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/previous-versions/azure/ad/graph/api/api-catalog
      - type: Documentation
        url: https://docs.microsoft.com/en-us/graph/migrate-azure-ad-graph-overview
        title: Migration Guide
  - name: Azure AD Authentication Library (ADAL)
    description: Authentication library for Azure AD (being replaced by MSAL).
    humanURL: https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-authentication-libraries
    tags:
      - Authentication
      - Legacy
      - Library
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-authentication-libraries
      - type: GitHubRepository
        url: https://github.com/AzureAD/azure-activedirectory-library-for-dotnet
  - name: Microsoft Authentication Library (MSAL)
    description: Modern authentication library for Microsoft identity platform.
    humanURL: https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-overview
    tags:
      - Authentication
      - Library
      - OAuth
      - OpenID Connect
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-overview
      - type: GitHubRepository
        url: https://github.com/AzureAD/microsoft-authentication-library-for-js
        title: JavaScript SDK
      - type: CodeExamples
        url: https://docs.microsoft.com/en-us/azure/active-directory/develop/sample-v2-code
      - type: GitHubRepository
        url: https://github.com/AzureAD/microsoft-authentication-library-for-dotnet
        title: .NET SDK
      - type: GitHubRepository
        url: https://github.com/AzureAD/microsoft-authentication-library-for-python
        title: Python SDK
      - type: GitHubRepository
        url: https://github.com/AzureAD/microsoft-authentication-library-for-java
        title: Java SDK
      - type: GitHubRepository
        url: https://github.com/AzureAD/microsoft-authentication-library-for-objc
        title: iOS SDK
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/msal/
        title: MSAL Documentation
  - name: Microsoft Identity Platform
    description: The Microsoft identity platform provides authentication and authorization services using standards-compliant implementations of OAuth 2.0 and OpenID Connect, enabling developers to build applications that sign in users and access secured APIs.
    humanURL: https://learn.microsoft.com/en-us/entra/identity-platform/
    baseURL: https://login.microsoftonline.com
    tags:
      - App Registration
      - Authentication
      - Authorization
      - OAuth
      - OpenID Connect
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/identity-platform/
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols
        title: OAuth Documentation
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc
        title: OpenID Connect Documentation
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow
        title: Authorization Code Flow
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
        title: App Registration Guide
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/identity-platform/scopes-oidc
        title: Scopes and Permissions
      - type: CodeExamples
        url: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-web-app-sign-in
  - name: Microsoft Entra Verified ID API
    description: Microsoft Entra Verified ID is a managed verifiable credentials service that enables organizations to issue, manage, and verify decentralized identity credentials based on W3C standards.
    humanURL: https://learn.microsoft.com/en-us/entra/verified-id/
    baseURL: https://verifiedid.did.msidentity.com
    tags:
      - Decentralized Identity
      - Identity Verification
      - Verifiable Credentials
      - W3C
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/verified-id/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/entra/verified-id/admin-api
        title: Admin API
      - type: APIReference
        url: https://learn.microsoft.com/en-us/entra/verified-id/vc-network-api
        title: Network API
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/verified-id/decentralized-identifier-overview
        title: Overview
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/entra/verified-id/verifiable-credentials-configure-tenant
  - name: Microsoft Entra ID Governance API
    description: Microsoft Entra ID Governance APIs in Microsoft Graph enable automated access reviews, entitlement management, lifecycle workflows, and privileged identity management for identity governance scenarios.
    humanURL: https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview
    baseURL: https://graph.microsoft.com
    tags:
      - Access Reviews
      - Entitlement Management
      - Governance
      - Lifecycle Workflows
      - Privileged Identity Management
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-overview?view=graph-rest-1.0
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/id-governance/deploy-access-reviews
        title: Access Reviews
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflows-deployment
        title: Lifecycle Workflows
      - type: Pricing
        url: https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals
  - name: Microsoft Entra SCIM Provisioning API
    description: Microsoft Entra ID supports SCIM 2.0 protocol for automatic user and group provisioning to cloud applications, enabling automated identity lifecycle management through standardized REST APIs.
    humanURL: https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups
    tags:
      - Automation
      - Group Management
      - Provisioning
      - SCIM
      - User Management
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups
      - type: Documentation
        url: https://learn.microsoft.com/en-us/entra/architecture/sync-scim
        title: Architecture Guide
      - type: GitHubRepository
        url: https://github.com/azure-ad-b2c/rest-api
  - name: Microsoft Entra PowerShell
    description: The Microsoft Entra PowerShell module provides cmdlets for managing Microsoft Entra resources programmatically, built on the Microsoft Graph PowerShell SDK.
    humanURL: https://learn.microsoft.com/en-us/powershell/entra-powershell/overview?view=entra-powershell
    tags:
      - Automation
      - CLI
      - PowerShell
      - Scripting
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/powershell/entra-powershell/?view=entra-powershell
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/powershell/entra-powershell/installation?view=entra-powershell
        title: Installation
      - type: GitHubRepository
        url: https://github.com/microsoftgraph/entra-powershell
maintainers:
  - name: Microsoft
    email: azuread@microsoft.com
    url: https://azure.microsoft.com/en-us/services/active-directory/
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: StatusPage
    url: https://status.azure.com/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/azure-active-directory/bg-p/Azure-Active-Directory
  - type: TermsOfService
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/active-directory/
  - type: Training
    url: https://docs.microsoft.com/en-us/learn/azure/
  - type: Portal
    url: https://entra.microsoft.com
    title: Entra Admin Center
  - type: DeveloperPortal
    url: https://developer.microsoft.com/en-us/graph
  - type: Blog
    url: https://devblogs.microsoft.com/identity/
    title: Identity Developer Blog
  - type: ReleaseNotes
    url: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new
  - type: Documentation
    url: https://learn.microsoft.com/en-us/entra/identity/
    title: Entra Documentation
  - type: Console
    url: https://developer.microsoft.com/en-us/graph/graph-explorer
    title: Graph Explorer
  - type: GitHubOrganization
    url: https://github.com/AzureAD
  - type: OpenAPI
    url: openapi/microsoft-graph-identity-api.yml
  - type: JSONSchema
    url: json-schema/azure-active-directory-user-schema.json
  - type: JSONLD
    url: json-ld/azure-active-directory-context.jsonld
  - type: Features
    data:
      - name: Single Sign-On
        description: Enable users to sign in once and access all connected applications without re-authenticating.
      - name: Conditional Access
        description: Enforce granular access policies based on user, device, location, and risk signals for zero trust security.
      - name: Multi-Factor Authentication
        description: Add a second layer of security with phone, app, or hardware token verification for identity protection.
      - name: SCIM User Provisioning
        description: Automate user and group lifecycle management across cloud applications using SCIM 2.0 standard.
      - name: Verifiable Credentials
        description: Issue and verify decentralized identity credentials based on W3C standards for privacy-preserving identity verification.
      - name: Identity Governance
        description: Automate access reviews, entitlement management, and lifecycle workflows for identity governance at scale.
      - name: Application Proxy
        description: Publish on-premises web applications externally with secure remote access without VPN infrastructure.
  - type: UseCases
    data:
      - name: Enterprise SSO
        description: Implement single sign-on across SaaS and on-premises applications for seamless employee access management.
      - name: B2B Collaboration
        description: Enable secure collaboration with external partners and guests using Azure AD B2B identity federation.
      - name: Customer Identity
        description: Build customer-facing applications with self-service sign-up, social identity providers, and branded login experiences.
      - name: Zero Trust Security
        description: Implement zero trust architecture with conditional access policies, continuous access evaluation, and risk-based authentication.
      - name: Automated User Provisioning
        description: Automate user account creation, updates, and deprovisioning across connected SaaS applications using SCIM.
  - type: Integrations
    data:
      - name: Microsoft 365
        description: Native identity provider for all Microsoft 365 applications including Teams, Outlook, SharePoint, and OneDrive.
      - name: Salesforce
        description: Single sign-on and automated user provisioning for Salesforce CRM using SAML and SCIM protocols.
      - name: ServiceNow
        description: Federated authentication and automated user lifecycle management for ServiceNow ITSM platform.
      - name: AWS
        description: Cross-cloud identity federation enabling Azure AD users to access AWS resources with single sign-on.
      - name: Workday
        description: HR-driven identity provisioning with automated user creation and attribute synchronization from Workday.
include:
  - name: Microsoft Identity Platform
    url: https://docs.microsoft.com/en-us/azure/active-directory/develop/
  - name: Azure AD B2C
    url: https://azure.microsoft.com/en-us/services/active-directory/external-identities/b2c/
  - name: Azure AD B2B
    url: https://docs.microsoft.com/en-us/azure/active-directory/external-identities/
  - name: Microsoft Entra External ID
    url: https://learn.microsoft.com/en-us/entra/external-id/self-service-sign-up-secure-api-connector
  - name: Microsoft Entra ID Protection
    url: https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-graph-api
---
