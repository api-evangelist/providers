---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Microsoft Azure Active Directory Agentic Access
  operation_count: 24
  slug: microsoft-azure-active-directory-agentic-access
  summary_line: 24 operations · 13 acting
api_count: 12
apis:
- description: Legacy API for accessing Azure AD (deprecated in favor of Microsoft Graph).
  name: Azure AD Graph API (Deprecated)
  slug: azure-ad-graph-api-deprecated
- description: Authentication library for Azure AD (being replaced by MSAL).
  name: Azure AD Authentication Library (ADAL)
  slug: azure-ad-authentication-library-adal
- description: Modern authentication library for Microsoft identity platform.
  name: Microsoft Authentication Library (MSAL)
  slug: microsoft-authentication-library-msal
- description: 'The Microsoft identity platform provides authentication and authorization services using standards-compliant implementations of OAuth 2.0 and OpenID Connect, enabling developers to build applications '
  name: Microsoft Identity Platform
  slug: microsoft-identity-platform
- description: Microsoft Entra Verified ID is a managed verifiable credentials service that enables organizations to issue, manage, and verify decentralized identity credentials based on W3C standards.
  name: Microsoft Entra Verified ID API
  slug: microsoft-entra-verified-id-api
- description: Microsoft Entra ID Governance APIs in Microsoft Graph enable automated access reviews, entitlement management, lifecycle workflows, and privileged identity management for identity governance scenarios
  name: Microsoft Entra ID Governance API
  slug: microsoft-entra-id-governance-api
- description: Microsoft Entra ID supports SCIM 2.0 protocol for automatic user and group provisioning to cloud applications, enabling automated identity lifecycle management through standardized REST APIs.
  name: Microsoft Entra SCIM Provisioning API
  slug: microsoft-entra-scim-provisioning-api
- description: The Microsoft Entra PowerShell module provides cmdlets for managing Microsoft Entra resources programmatically, built on the Microsoft Graph PowerShell SDK.
  name: Microsoft Entra PowerShell
  slug: microsoft-entra-powershell
- description: Manage application registrations in Azure Active Directory. An application object is the global representation of an application across all tenants, defining the app identity, access configuration, an
  name: Microsoft Azure Active Directory Applications API
  slug: microsoft-azure-active-directory-applications-api
- description: Manage groups in Azure Active Directory. Groups can be security groups, Microsoft 365 groups, or mail-enabled security groups. They provide shared access to resources for a collection of users and oth
  name: Microsoft Azure Active Directory Groups API
  slug: microsoft-azure-active-directory-groups-api
- description: Manage service principals in Azure Active Directory. A service principal is the local representation of an application in a specific tenant. It defines what the application can do in the tenant, who c
  name: Microsoft Azure Active Directory Service Principals API
  slug: microsoft-azure-active-directory-service-principals-api
- description: Manage user accounts in Azure Active Directory. Users are the core identity objects representing people in an organization. Each user has a profile with attributes such as display name, email, job tit
  name: Microsoft Azure Active Directory Users API
  slug: microsoft-azure-active-directory-users-api
artifact_total: 175
collections:
- collection_type: open
  name: Microsoft Graph Identity API
  slug: open-microsoft-graph-identity-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-active-directory-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-active-directory-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-active-directory-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-active-directory-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/azure-active-directory/bg-p/Azure-Active-Directory
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/active-directory/
- group: learn
  title: ''
  type: Training
  url: https://docs.microsoft.com/en-us/learn/azure/
- group: start
  title: Entra Admin Center
  type: Portal
  url: https://entra.microsoft.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/graph
- group: company
  title: Identity Developer Blog
  type: Blog
  url: https://devblogs.microsoft.com/identity/
- group: company
  title: ''
  type: BlogRSS
  url: https://devblogs.microsoft.com/identity/feed/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new
- group: docs
  title: Entra Documentation
  type: Documentation
  url: https://learn.microsoft.com/en-us/entra/identity/
- group: start
  title: Graph Explorer
  type: Console
  url: https://developer.microsoft.com/en-us/graph/graph-explorer
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AzureAD
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/microsoft-graph-identity-api.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/azure-active-directory-user-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/azure-active-directory-context.jsonld
created: '2024-01-15'
description: Microsoft Azure Active Directory (Azure AD), now Microsoft Entra ID, is Microsoft's cloud-based identity and access management service, which helps employees sign in and access resources.
examples:
- key_count: 6
  name: Microsoft Azure Active Directory Addgroupmember Example
  slug: microsoft-azure-active-directory-addgroupmember-example
- key_count: 6
  name: Microsoft Azure Active Directory Createapplication Example
  slug: microsoft-azure-active-directory-createapplication-example
- key_count: 6
  name: Microsoft Azure Active Directory Creategroup Example
  slug: microsoft-azure-active-directory-creategroup-example
- key_count: 6
  name: Microsoft Azure Active Directory Createserviceprincipal Example
  slug: microsoft-azure-active-directory-createserviceprincipal-example
- key_count: 6
  name: Microsoft Azure Active Directory Createuser Example
  slug: microsoft-azure-active-directory-createuser-example
- key_count: 6
  name: Microsoft Azure Active Directory Getapplication Example
  slug: microsoft-azure-active-directory-getapplication-example
- key_count: 6
  name: Microsoft Azure Active Directory Getgroup Example
  slug: microsoft-azure-active-directory-getgroup-example
- key_count: 6
  name: Microsoft Azure Active Directory Getserviceprincipal Example
  slug: microsoft-azure-active-directory-getserviceprincipal-example
- key_count: 6
  name: Microsoft Azure Active Directory Getuser Example
  slug: microsoft-azure-active-directory-getuser-example
- key_count: 6
  name: Microsoft Azure Active Directory Listapplications Example
  slug: microsoft-azure-active-directory-listapplications-example
- key_count: 6
  name: Microsoft Azure Active Directory Listgroupmembers Example
  slug: microsoft-azure-active-directory-listgroupmembers-example
- key_count: 6
  name: Microsoft Azure Active Directory Listgroups Example
  slug: microsoft-azure-active-directory-listgroups-example
- key_count: 6
  name: Microsoft Azure Active Directory Listserviceprincipalapproleassignments Example
  slug: microsoft-azure-active-directory-listserviceprincipalapproleassignments-example
- key_count: 6
  name: Microsoft Azure Active Directory Listserviceprincipals Example
  slug: microsoft-azure-active-directory-listserviceprincipals-example
- key_count: 6
  name: Microsoft Azure Active Directory Listusermemberof Example
  slug: microsoft-azure-active-directory-listusermemberof-example
- key_count: 6
  name: Microsoft Azure Active Directory Listusers Example
  slug: microsoft-azure-active-directory-listusers-example
- key_count: 6
  name: Microsoft Azure Active Directory Updateapplication Example
  slug: microsoft-azure-active-directory-updateapplication-example
- key_count: 6
  name: Microsoft Azure Active Directory Updategroup Example
  slug: microsoft-azure-active-directory-updategroup-example
- key_count: 6
  name: Microsoft Azure Active Directory Updateserviceprincipal Example
  slug: microsoft-azure-active-directory-updateserviceprincipal-example
- key_count: 6
  name: Microsoft Azure Active Directory Updateuser Example
  slug: microsoft-azure-active-directory-updateuser-example
- key_count: 5
  name: Microsoft Graph Identity Api Application Example
  slug: microsoft-graph-identity-api-application-example
- key_count: 8
  name: Microsoft Graph Identity App Role Assignment Example
  slug: microsoft-graph-identity-app-role-assignment-example
- key_count: 6
  name: Microsoft Graph Identity App Role Example
  slug: microsoft-graph-identity-app-role-example
- key_count: 7
  name: Microsoft Graph Identity Application Create Example
  slug: microsoft-graph-identity-application-create-example
- key_count: 12
  name: Microsoft Graph Identity Application Example
  slug: microsoft-graph-identity-application-example
- key_count: 7
  name: Microsoft Graph Identity Application Update Example
  slug: microsoft-graph-identity-application-update-example
- key_count: 2
  name: Microsoft Graph Identity Assigned License Example
  slug: microsoft-graph-identity-assigned-license-example
- key_count: 4
  name: Microsoft Graph Identity Assigned Plan Example
  slug: microsoft-graph-identity-assigned-plan-example
- key_count: 3
  name: Microsoft Graph Identity Directory Object Example
  slug: microsoft-graph-identity-directory-object-example
- key_count: 10
  name: Microsoft Graph Identity Group Create Example
  slug: microsoft-graph-identity-group-create-example
- key_count: 21
  name: Microsoft Graph Identity Group Example
  slug: microsoft-graph-identity-group-example
- key_count: 8
  name: Microsoft Graph Identity Group Update Example
  slug: microsoft-graph-identity-group-update-example
- key_count: 8
  name: Microsoft Graph Identity Key Credential Example
  slug: microsoft-graph-identity-key-credential-example
- key_count: 1
  name: Microsoft Graph Identity O Data Error Example
  slug: microsoft-graph-identity-o-data-error-example
- key_count: 7
  name: Microsoft Graph Identity Password Credential Example
  slug: microsoft-graph-identity-password-credential-example
- key_count: 3
  name: Microsoft Graph Identity Password Profile Example
  slug: microsoft-graph-identity-password-profile-example
- key_count: 8
  name: Microsoft Graph Identity Permission Scope Example
  slug: microsoft-graph-identity-permission-scope-example
- key_count: 1
  name: Microsoft Graph Identity Public Client Application Example
  slug: microsoft-graph-identity-public-client-application-example
- key_count: 2
  name: Microsoft Graph Identity Required Resource Access Example
  slug: microsoft-graph-identity-required-resource-access-example
- key_count: 6
  name: Microsoft Graph Identity Service Principal Create Example
  slug: microsoft-graph-identity-service-principal-create-example
- key_count: 21
  name: Microsoft Graph Identity Service Principal Example
  slug: microsoft-graph-identity-service-principal-example
- key_count: 9
  name: Microsoft Graph Identity Service Principal Update Example
  slug: microsoft-graph-identity-service-principal-update-example
- key_count: 1
  name: Microsoft Graph Identity Spa Application Example
  slug: microsoft-graph-identity-spa-application-example
- key_count: 13
  name: Microsoft Graph Identity User Create Example
  slug: microsoft-graph-identity-user-create-example
- key_count: 35
  name: Microsoft Graph Identity User Example
  slug: microsoft-graph-identity-user-example
- key_count: 20
  name: Microsoft Graph Identity User Update Example
  slug: microsoft-graph-identity-user-update-example
- key_count: 4
  name: Microsoft Graph Identity Web Application Example
  slug: microsoft-graph-identity-web-application-example
features:
- description: Enable users to sign in once and access all connected applications without re-authenticating.
  name: Single Sign-On
- description: Enforce granular access policies based on user, device, location, and risk signals for zero trust security.
  name: Conditional Access
- description: Add a second layer of security with phone, app, or hardware token verification for identity protection.
  name: Multi-Factor Authentication
- description: Automate user and group lifecycle management across cloud applications using SCIM 2.0 standard.
  name: SCIM User Provisioning
- description: Issue and verify decentralized identity credentials based on W3C standards for privacy-preserving identity verification.
  name: Verifiable Credentials
- description: Automate access reviews, entitlement management, and lifecycle workflows for identity governance at scale.
  name: Identity Governance
- description: Publish on-premises web applications externally with secure remote access without VPN infrastructure.
  name: Application Proxy
finops:
- name: Azure Active Directory Finops
  service_category: Identity
  slug: azure-active-directory-finops
- name: Microsoft Azure Active Directory Finops
  service_category: Identity
  slug: microsoft-azure-active-directory-finops
image: https://docs.microsoft.com/azure/media/index/active-directory.svg
integrations:
- description: Native identity provider for all Microsoft 365 applications including Teams, Outlook, SharePoint, and OneDrive.
  name: Microsoft 365
- description: Single sign-on and automated user provisioning for Salesforce CRM using SAML and SCIM protocols.
  name: Salesforce
- description: Federated authentication and automated user lifecycle management for ServiceNow ITSM platform.
  name: ServiceNow
- description: Cross-cloud identity federation enabling Azure AD users to access AWS resources with single sign-on.
  name: AWS
- description: HR-driven identity provisioning with automated user creation and attribute synchronization from Workday.
  name: Workday
json_schemas:
- name: Azure Active Directory User
  property_count: 64
  slug: azure-active-directory-user
- name: ApiApplication
  property_count: 5
  slug: microsoft-azure-active-directory-apiapplication
- name: Application
  property_count: 16
  slug: microsoft-azure-active-directory-application
- name: ApplicationCreate
  property_count: 11
  slug: microsoft-azure-active-directory-applicationcreate
- name: ApplicationUpdate
  property_count: 11
  slug: microsoft-azure-active-directory-applicationupdate
- name: AppRole
  property_count: 6
  slug: microsoft-azure-active-directory-approle
- name: AppRoleAssignment
  property_count: 8
  slug: microsoft-azure-active-directory-approleassignment
- name: AssignedLicense
  property_count: 2
  slug: microsoft-azure-active-directory-assignedlicense
- name: AssignedPlan
  property_count: 4
  slug: microsoft-azure-active-directory-assignedplan
- name: DirectoryObject
  property_count: 3
  slug: microsoft-azure-active-directory-directoryobject
- name: Group
  property_count: 21
  slug: microsoft-azure-active-directory-group
- name: GroupCreate
  property_count: 10
  slug: microsoft-azure-active-directory-groupcreate
- name: GroupUpdate
  property_count: 8
  slug: microsoft-azure-active-directory-groupupdate
- name: KeyCredential
  property_count: 8
  slug: microsoft-azure-active-directory-keycredential
- name: ODataError
  property_count: 1
  slug: microsoft-azure-active-directory-odataerror
- name: PasswordCredential
  property_count: 7
  slug: microsoft-azure-active-directory-passwordcredential
- name: PasswordProfile
  property_count: 3
  slug: microsoft-azure-active-directory-passwordprofile
- name: PermissionScope
  property_count: 8
  slug: microsoft-azure-active-directory-permissionscope
- name: PublicClientApplication
  property_count: 1
  slug: microsoft-azure-active-directory-publicclientapplication
- name: RequiredResourceAccess
  property_count: 2
  slug: microsoft-azure-active-directory-requiredresourceaccess
- name: ServicePrincipal
  property_count: 21
  slug: microsoft-azure-active-directory-serviceprincipal
- name: ServicePrincipalCreate
  property_count: 6
  slug: microsoft-azure-active-directory-serviceprincipalcreate
- name: ServicePrincipalUpdate
  property_count: 9
  slug: microsoft-azure-active-directory-serviceprincipalupdate
- name: SpaApplication
  property_count: 1
  slug: microsoft-azure-active-directory-spaapplication
- name: User
  property_count: 35
  slug: microsoft-azure-active-directory-user
- name: UserCreate
  property_count: 14
  slug: microsoft-azure-active-directory-usercreate
- name: UserUpdate
  property_count: 21
  slug: microsoft-azure-active-directory-userupdate
- name: WebApplication
  property_count: 4
  slug: microsoft-azure-active-directory-webapplication
- name: ApiApplication
  property_count: 5
  slug: microsoft-graph-identity-api-application
- name: AppRoleAssignment
  property_count: 8
  slug: microsoft-graph-identity-app-role-assignment
- name: AppRole
  property_count: 6
  slug: microsoft-graph-identity-app-role
- name: ApplicationCreate
  property_count: 7
  slug: microsoft-graph-identity-application-create
- name: Application
  property_count: 12
  slug: microsoft-graph-identity-application
- name: ApplicationUpdate
  property_count: 7
  slug: microsoft-graph-identity-application-update
- name: AssignedLicense
  property_count: 2
  slug: microsoft-graph-identity-assigned-license
- name: AssignedPlan
  property_count: 4
  slug: microsoft-graph-identity-assigned-plan
- name: DirectoryObject
  property_count: 3
  slug: microsoft-graph-identity-directory-object
- name: GroupCreate
  property_count: 10
  slug: microsoft-graph-identity-group-create
- name: Group
  property_count: 21
  slug: microsoft-graph-identity-group
- name: GroupUpdate
  property_count: 8
  slug: microsoft-graph-identity-group-update
- name: KeyCredential
  property_count: 8
  slug: microsoft-graph-identity-key-credential
- name: ODataError
  property_count: 1
  slug: microsoft-graph-identity-o-data-error
- name: PasswordCredential
  property_count: 7
  slug: microsoft-graph-identity-password-credential
- name: PasswordProfile
  property_count: 3
  slug: microsoft-graph-identity-password-profile
- name: PermissionScope
  property_count: 8
  slug: microsoft-graph-identity-permission-scope
- name: PublicClientApplication
  property_count: 1
  slug: microsoft-graph-identity-public-client-application
- name: RequiredResourceAccess
  property_count: 2
  slug: microsoft-graph-identity-required-resource-access
- name: ServicePrincipalCreate
  property_count: 6
  slug: microsoft-graph-identity-service-principal-create
- name: ServicePrincipal
  property_count: 21
  slug: microsoft-graph-identity-service-principal
- name: ServicePrincipalUpdate
  property_count: 9
  slug: microsoft-graph-identity-service-principal-update
- name: SpaApplication
  property_count: 1
  slug: microsoft-graph-identity-spa-application
- name: UserCreate
  property_count: 13
  slug: microsoft-graph-identity-user-create
- name: User
  property_count: 35
  slug: microsoft-graph-identity-user
- name: UserUpdate
  property_count: 20
  slug: microsoft-graph-identity-user-update
- name: WebApplication
  property_count: 4
  slug: microsoft-graph-identity-web-application
json_structures:
- name: Microsoft Azure Active Directory Structure
  property_count: 0
  slug: microsoft-azure-active-directory-structure
- name: Microsoft Graph Identity Api Application Structure
  property_count: 5
  slug: microsoft-graph-identity-api-application-structure
- name: Microsoft Graph Identity App Role Assignment Structure
  property_count: 8
  slug: microsoft-graph-identity-app-role-assignment-structure
- name: Microsoft Graph Identity App Role Structure
  property_count: 6
  slug: microsoft-graph-identity-app-role-structure
- name: Microsoft Graph Identity Application Create Structure
  property_count: 7
  slug: microsoft-graph-identity-application-create-structure
- name: Microsoft Graph Identity Application Structure
  property_count: 12
  slug: microsoft-graph-identity-application-structure
- name: Microsoft Graph Identity Application Update Structure
  property_count: 7
  slug: microsoft-graph-identity-application-update-structure
- name: Microsoft Graph Identity Assigned License Structure
  property_count: 2
  slug: microsoft-graph-identity-assigned-license-structure
- name: Microsoft Graph Identity Assigned Plan Structure
  property_count: 4
  slug: microsoft-graph-identity-assigned-plan-structure
- name: Microsoft Graph Identity Directory Object Structure
  property_count: 3
  slug: microsoft-graph-identity-directory-object-structure
- name: Microsoft Graph Identity Group Create Structure
  property_count: 10
  slug: microsoft-graph-identity-group-create-structure
- name: Microsoft Graph Identity Group Structure
  property_count: 21
  slug: microsoft-graph-identity-group-structure
- name: Microsoft Graph Identity Group Update Structure
  property_count: 8
  slug: microsoft-graph-identity-group-update-structure
- name: Microsoft Graph Identity Key Credential Structure
  property_count: 8
  slug: microsoft-graph-identity-key-credential-structure
- name: Microsoft Graph Identity O Data Error Structure
  property_count: 1
  slug: microsoft-graph-identity-o-data-error-structure
- name: Microsoft Graph Identity Password Credential Structure
  property_count: 7
  slug: microsoft-graph-identity-password-credential-structure
- name: Microsoft Graph Identity Password Profile Structure
  property_count: 3
  slug: microsoft-graph-identity-password-profile-structure
- name: Microsoft Graph Identity Permission Scope Structure
  property_count: 8
  slug: microsoft-graph-identity-permission-scope-structure
- name: Microsoft Graph Identity Public Client Application Structure
  property_count: 1
  slug: microsoft-graph-identity-public-client-application-structure
- name: Microsoft Graph Identity Required Resource Access Structure
  property_count: 2
  slug: microsoft-graph-identity-required-resource-access-structure
- name: Microsoft Graph Identity Service Principal Create Structure
  property_count: 6
  slug: microsoft-graph-identity-service-principal-create-structure
- name: Microsoft Graph Identity Service Principal Structure
  property_count: 21
  slug: microsoft-graph-identity-service-principal-structure
- name: Microsoft Graph Identity Service Principal Update Structure
  property_count: 9
  slug: microsoft-graph-identity-service-principal-update-structure
- name: Microsoft Graph Identity Spa Application Structure
  property_count: 1
  slug: microsoft-graph-identity-spa-application-structure
- name: Microsoft Graph Identity User Create Structure
  property_count: 13
  slug: microsoft-graph-identity-user-create-structure
- name: Microsoft Graph Identity User Structure
  property_count: 35
  slug: microsoft-graph-identity-user-structure
- name: Microsoft Graph Identity User Update Structure
  property_count: 20
  slug: microsoft-graph-identity-user-update-structure
- name: Microsoft Graph Identity Web Application Structure
  property_count: 4
  slug: microsoft-graph-identity-web-application-structure
jsonld:
- class_count: 1
  name: Azure Active Directory Context
  property_count: 6
  slug: azure-active-directory-context
- class_count: 0
  name: Microsoft Graph Identity Context
  property_count: 0
  slug: microsoft-graph-identity-context
layout: provider
modified: '2026-05-19'
name: Microsoft Azure Active Directory
nav: Providers
network: true
overview: 'Microsoft Azure Active Directory publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Groups API, Service Principals API, and 1 more. Tagged areas include Authentication, Authorization, Identity, Microsoft, and Microsoft Entra.


  The Microsoft Azure Active Directory catalog on APIs.io includes 2 JSON-LD contexts and 3 Spectral governance rulesets.


  Microsoft Azure Active Directory''s developer surface includes authentication, developer portal, support, engineering blog, pricing, training material, release notes, and 16 more developer resources.'
plans:
- name: Azure Active Directory Plans Pricing
  plan_count: 6
  slug: azure-active-directory-plans-pricing
- name: Microsoft Azure Active Directory Plans Pricing
  plan_count: 9
  slug: microsoft-azure-active-directory-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 10
  name: Azure Active Directory Rate Limits
  slug: azure-active-directory-rate-limits
- limit_count: 6
  name: Microsoft Azure Active Directory Rate Limits
  slug: microsoft-azure-active-directory-rate-limits
rules:
- name: Microsoft Azure Active Directory API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: azure-active-directory-spectral-rules
- name: Microsoft Azure Active Directory API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-azure-active-directory-jsonschema-spectral-rules
- name: Microsoft Azure Active Directory API Rules
  rule_count: 11
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 9
  slug: microsoft-azure-active-directory-spectral-rules
scopes:
- name: Microsoft Azure Active Directory Scopes
  scope_count: 12
  slug: microsoft-azure-active-directory-scopes
  summary_line: 12 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 57.4
  delta: -2.4
  facets:
    commercial_clarity: 71.1
    contract_quality: 71.7
    developer_ergonomics: 41.3
    discoverability: 55.6
    governance: 20.8
    operational_transparency: 68.4
  previous_composite: 59.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-active-directory/refs/heads/main/screenshots/microsoft-azure-active-directory-2026-06-20T185351.png
security:
- kind: authentication
  name: Microsoft Azure Active Directory Authentication
  slug: microsoft-azure-active-directory-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Active Directory Domain Security
  slug: microsoft-azure-active-directory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-active-directory
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
use_cases:
- description: Implement single sign-on across SaaS and on-premises applications for seamless employee access management.
  name: Enterprise SSO
- description: Enable secure collaboration with external partners and guests using Azure AD B2B identity federation.
  name: B2B Collaboration
- description: Build customer-facing applications with self-service sign-up, social identity providers, and branded login experiences.
  name: Customer Identity
- description: Implement zero trust architecture with conditional access policies, continuous access evaluation, and risk-based authentication.
  name: Zero Trust Security
- description: Automate user account creation, updates, and deprovisioning across connected SaaS applications using SCIM.
  name: Automated User Provisioning
website: https://developer.microsoft.com/en-us/graph
---
