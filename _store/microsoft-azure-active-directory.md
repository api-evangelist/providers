---
aid: microsoft-azure-active-directory
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-active-directory/refs/heads/main/apis.yml
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
  - type: SDKs
    url: https://docs.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/active-directory/
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/graph/use-the-api
  - type: Explorer
    url: https://developer.microsoft.com/en-us/graph/graph-explorer
  - type: ChangeLog
    url: https://learn.microsoft.com/en-us/graph/changelog
  - type: BetaDocumentation
    url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-beta
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
  - type: ConditionalAccessDocumentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccesspolicy?view=graph-rest-1.0
  - type: IdentityGovernanceDocumentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-overview?view=graph-rest-1.0
  - type: DeveloperGuide
    url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-conditional-access-dev-guide
  - type: OpenAPI
    url: openapi/microsoft-graph-identity-api.yml
  - type: JSONSchema
    url: json-schema/azure-active-directory-user-schema.json
  - type: JSON-LD
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
  - type: Migration Guide
    url: https://docs.microsoft.com/en-us/graph/migrate-azure-ad-graph-overview
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
  - type: GitHub
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
  - type: GitHub
    url: https://github.com/AzureAD/microsoft-authentication-library-for-js
  - type: Samples
    url: https://docs.microsoft.com/en-us/azure/active-directory/develop/sample-v2-code
  - type: GitHubDotNet
    url: https://github.com/AzureAD/microsoft-authentication-library-for-dotnet
  - type: GitHubPython
    url: https://github.com/AzureAD/microsoft-authentication-library-for-python
  - type: GitHubJava
    url: https://github.com/AzureAD/microsoft-authentication-library-for-java
  - type: GitHubiOS
    url: https://github.com/AzureAD/microsoft-authentication-library-for-objc
  - type: MSALDocumentation
    url: https://learn.microsoft.com/en-us/entra/msal/
  - type: DotNetDocumentation
    url: https://learn.microsoft.com/en-us/entra/msal/dotnet/
  - type: PythonDocumentation
    url: https://learn.microsoft.com/en-us/entra/msal/python/
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
  - type: OAuthDocumentation
    url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols
  - type: OpenIDConnectDocumentation
    url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc
  - type: AuthorizationCodeFlowDocumentation
    url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow
  - type: AppRegistrationGuide
    url: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
  - type: ScopesAndPermissions
    url: https://learn.microsoft.com/en-us/entra/identity-platform/scopes-oidc
  - type: ApplicationTypes
    url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-app-types
  - type: Samples
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
  - type: AdminAPIDocumentation
    url: https://learn.microsoft.com/en-us/entra/verified-id/admin-api
  - type: NetworkAPIDocumentation
    url: https://learn.microsoft.com/en-us/entra/verified-id/vc-network-api
  - type: Overview
    url: https://learn.microsoft.com/en-us/entra/verified-id/decentralized-identifier-overview
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/entra/verified-id/verifiable-credentials-configure-tenant
  - type: ProductPage
    url: https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-verified-id
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
  - type: GraphAPIDocumentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-overview?view=graph-rest-1.0
  - type: AccessReviewsDocumentation
    url: https://learn.microsoft.com/en-us/entra/id-governance/deploy-access-reviews
  - type: LifecycleWorkflowsDocumentation
    url: https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflows-deployment
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
  - type: ArchitectureGuide
    url: https://learn.microsoft.com/en-us/entra/architecture/sync-scim
  - type: GitHub
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
  - type: Installation
    url: https://learn.microsoft.com/en-us/powershell/entra-powershell/installation?view=entra-powershell
  - type: GitHub
    url: https://github.com/microsoftgraph/entra-powershell
  - type: GraphPowerShellDocumentation
    url: https://learn.microsoft.com/en-us/powershell/microsoftgraph/?view=graph-powershell-1.0
name: Azure Active Directory
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
type: Contract
image: https://docs.microsoft.com/azure/media/index/active-directory.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Azure Active Directory (Azure AD), now Microsoft Entra ID, is Microsoft's cloud-based identity and access management service, which helps employees sign in and access resources.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

