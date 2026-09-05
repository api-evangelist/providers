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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Microsoft Entra Agentic Access
  operation_count: 28
  slug: microsoft-entra-agentic-access
  summary_line: 28 operations · 17 acting
api_count: 1
apis:
- description: API for identity risk detection, investigation, and remediation.
  name: Microsoft Entra ID Protection API
  slug: id-protection
- description: API for managing conditional access policies and controls.
  name: Microsoft Entra Conditional Access API
  slug: conditional-access
- description: API for managing privileged access and just-in-time administration.
  name: Microsoft Entra Privileged Identity Management API
  slug: pim
- description: API for issuing and verifying decentralized identity credentials.
  name: Microsoft Entra Verified ID API
  slug: verified-id
- description: API for managing customer and partner identity and access management.
  name: Microsoft Entra External ID API
  slug: external-id
- description: API for managing identity governance including access reviews, entitlement management, and lifecycle workflows to ensure the right people have the right access at the right time.
  name: Microsoft Entra ID Governance API
  slug: id-governance
- description: API for registering, configuring, and managing applications and service principals in Microsoft Entra ID.
  name: Microsoft Entra Application Management API
  slug: application-management
- description: API for managing user authentication methods including FIDO2 security keys, passwordless phone sign-in, Microsoft Authenticator, and MFA registration.
  name: Microsoft Entra Authentication Methods API
  slug: authentication-methods
- description: API for managing and securing identities for software workloads such as applications, services, scripts, and containers.
  name: Microsoft Entra Workload ID API
  slug: workload-id
- description: API for automating user provisioning and deprovisioning using SCIM protocol, including API-driven inbound provisioning from any system of record.
  name: Microsoft Entra Provisioning API
  slug: provisioning
- description: API for managing Microsoft Entra Internet Access and Microsoft Entra Private Access, providing identity-centric secure web gateway and zero-trust network access.
  name: Microsoft Entra Global Secure Access API
  slug: global-secure-access
- description: API endpoints for OAuth 2.0, OpenID Connect, and SAML authentication protocols enabling application integration with Microsoft Entra ID.
  name: Microsoft Identity Platform API
  slug: identity-platform
- description: API for creating, securing, and monitoring AI agent identities, providing authentication, authorization, and lifecycle management for AI agents.
  name: Microsoft Entra Agent ID API
  slug: agent-id
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Register and manage application objects that define application configuration including credentials, permissions, and sign-in settings
  name: Microsoft Entra Applications API
  slug: microsoft-entra-applications-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Manage groups for organizing users, devices, and other principals including Microsoft 365 groups, security groups, and distribution lists
  name: Microsoft Entra Groups API
  slug: microsoft-entra-groups-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Manage service principal objects that represent application instances in a tenant for authentication and authorization
  name: Microsoft Entra ServicePrincipals API
  slug: microsoft-entra-serviceprincipals-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Manage user accounts in the directory including creation, updates, profile management, and lifecycle operations
  name: Microsoft Entra Users API
  slug: microsoft-entra-users-api
arazzos:
- description: Find a user by UPN, read its profile, and list its group memberships.
  name: Microsoft Entra Audit User Memberships
  slug: microsoft-entra-audit-user-memberships-workflow
- description: Create a security group, add a member, and list its members.
  name: Microsoft Entra Create Group With Member
  slug: microsoft-entra-create-group-with-member-workflow
- description: Create a Unified M365 group, add a member, and read the group back.
  name: Microsoft Entra Create Microsoft 365 Group With Member
  slug: microsoft-entra-create-m365-group-with-owner-member-workflow
- description: Find a service principal by appId, delete it, then delete the app.
  name: Microsoft Entra Decommission Application
  slug: microsoft-entra-decommission-application-workflow
- description: Disable a user account, then delete the user from the directory.
  name: Microsoft Entra Deprovision User
  slug: microsoft-entra-deprovision-user-workflow
- description: Find an app by appId, update its display name, and read it back.
  name: Microsoft Entra Find And Update Application
  slug: microsoft-entra-find-and-update-application-workflow
- description: Find a group by display name, update it, and read it back.
  name: Microsoft Entra Find And Update Group
  slug: microsoft-entra-find-and-update-group-workflow
- description: Find a user by UPN, update its profile, and read the result.
  name: Microsoft Entra Find And Update User
  slug: microsoft-entra-find-and-update-user-workflow
- description: Grant an app role to a service principal then list its assignments.
  name: Microsoft Entra Grant App Role Assignment
  slug: microsoft-entra-grant-app-role-assignment-workflow
- description: Find a user by UPN, remove it from a group, and verify removal.
  name: Microsoft Entra Offboard User From Group
  slug: microsoft-entra-offboard-user-from-group-workflow
- description: Create a user, add it to an existing group, and confirm membership.
  name: Microsoft Entra Onboard User To Group
  slug: microsoft-entra-onboard-user-to-group-workflow
- description: Create a new Entra ID user and read back the provisioned account.
  name: Microsoft Entra Provision User
  slug: microsoft-entra-provision-user-workflow
- description: Create an app registration then instantiate its service principal.
  name: Microsoft Entra Register Application With Service Principal
  slug: microsoft-entra-register-app-with-service-principal-workflow
- description: Add a fresh client secret to an app, then remove the old one.
  name: Microsoft Entra Rotate Application Secret
  slug: microsoft-entra-rotate-application-secret-workflow
artifact_total: 168
collections:
- collection_type: postman
  name: Microsoft Entra Microsoft Graph Identity API
  slug: postman-microsoft-entra-graph-identity
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Entra Microsoft Graph Identity Applications API
  slug: open-microsoft-entra-applications-api
- collection_type: open
  name: Microsoft Entra Microsoft Graph Identity API
  slug: open-microsoft-entra-graph-identity
- collection_type: open
  name: Microsoft Entra Microsoft Graph Identity Applications Groups API
  slug: open-microsoft-entra-groups-api
- collection_type: open
  name: Microsoft Entra Microsoft Graph Identity Applications ServicePrincipals API
  slug: open-microsoft-entra-serviceprincipals-api
- collection_type: open
  name: Microsoft Entra Microsoft Graph Identity Applications Users API
  slug: open-microsoft-entra-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-entra-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-entra-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-entra-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-entra-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-entra-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-entra-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-entra/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-entra-audit-user-memberships-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-entra-create-group-with-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-entra-create-m365-group-with-owner-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-entra-decommission-application-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-entra-deprovision-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-entra-find-and-update-application-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-entra-find-and-update-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-entra-find-and-update-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-entra-grant-app-role-assignment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-entra-offboard-user-from-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-entra-onboard-user-to-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-entra-provision-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-entra-register-app-with-service-principal-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-entra-rotate-application-secret-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://entra.microsoft.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/entra/fundamentals/
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/microsoft-entra-azure-ad-blog/bg-p/Identity
- group: operate
  title: ''
  type: Support
  url: https://learn.microsoft.com/en-us/entra/fundamentals/how-to-get-support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/licensing/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoftgraph
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/security/business/microsoft-entra-pricing
- group: design
  title: ''
  type: JSONLD
  url: json-ld/microsoft-entra-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/microsoft-entra-user-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/microsoft-entra-application-schema.json
created: '2024-01-01'
description: Microsoft Entra (formerly Azure Active Directory) provides identity and access management services including authentication, authorization, and directory services.
examples:
- key_count: 5
  name: Microsoft Entra Graph Identity Api Application Example
  slug: microsoft-entra-graph-identity-api-application-example
- key_count: 4
  name: Microsoft Entra Graph Identity App Role Assignment Collection Response Example
  slug: microsoft-entra-graph-identity-app-role-assignment-collection-response-example
- key_count: 8
  name: Microsoft Entra Graph Identity App Role Assignment Example
  slug: microsoft-entra-graph-identity-app-role-assignment-example
- key_count: 6
  name: Microsoft Entra Graph Identity App Role Example
  slug: microsoft-entra-graph-identity-app-role-example
- key_count: 4
  name: Microsoft Entra Graph Identity Application Collection Response Example
  slug: microsoft-entra-graph-identity-application-collection-response-example
- key_count: 13
  name: Microsoft Entra Graph Identity Application Example
  slug: microsoft-entra-graph-identity-application-example
- key_count: 2
  name: Microsoft Entra Graph Identity Assigned License Example
  slug: microsoft-entra-graph-identity-assigned-license-example
- key_count: 4
  name: Microsoft Entra Graph Identity Directory Object Collection Response Example
  slug: microsoft-entra-graph-identity-directory-object-collection-response-example
- key_count: 3
  name: Microsoft Entra Graph Identity Directory Object Example
  slug: microsoft-entra-graph-identity-directory-object-example
- key_count: 4
  name: Microsoft Entra Graph Identity Group Collection Response Example
  slug: microsoft-entra-graph-identity-group-collection-response-example
- key_count: 18
  name: Microsoft Entra Graph Identity Group Example
  slug: microsoft-entra-graph-identity-group-example
- key_count: 7
  name: Microsoft Entra Graph Identity Key Credential Example
  slug: microsoft-entra-graph-identity-key-credential-example
- key_count: 1
  name: Microsoft Entra Graph Identity O Data Error Example
  slug: microsoft-entra-graph-identity-o-data-error-example
- key_count: 1
  name: Microsoft Entra Graph Identity O Data Reference Example
  slug: microsoft-entra-graph-identity-o-data-reference-example
- key_count: 6
  name: Microsoft Entra Graph Identity Password Credential Example
  slug: microsoft-entra-graph-identity-password-credential-example
- key_count: 3
  name: Microsoft Entra Graph Identity Password Profile Example
  slug: microsoft-entra-graph-identity-password-profile-example
- key_count: 8
  name: Microsoft Entra Graph Identity Permission Scope Example
  slug: microsoft-entra-graph-identity-permission-scope-example
- key_count: 2
  name: Microsoft Entra Graph Identity Required Resource Access Example
  slug: microsoft-entra-graph-identity-required-resource-access-example
- key_count: 4
  name: Microsoft Entra Graph Identity Service Principal Collection Response Example
  slug: microsoft-entra-graph-identity-service-principal-collection-response-example
- key_count: 20
  name: Microsoft Entra Graph Identity Service Principal Example
  slug: microsoft-entra-graph-identity-service-principal-example
- key_count: 1
  name: Microsoft Entra Graph Identity Spa Application Example
  slug: microsoft-entra-graph-identity-spa-application-example
- key_count: 4
  name: Microsoft Entra Graph Identity User Collection Response Example
  slug: microsoft-entra-graph-identity-user-collection-response-example
- key_count: 31
  name: Microsoft Entra Graph Identity User Example
  slug: microsoft-entra-graph-identity-user-example
- key_count: 4
  name: Microsoft Entra Graph Identity Web Application Example
  slug: microsoft-entra-graph-identity-web-application-example
features:
- description: Manage user identities, authentication, and authorization across cloud and hybrid environments with single sign-on.
  name: Identity and Access Management
- description: Enforce adaptive access policies based on user, device, location, and risk signals for zero trust security.
  name: Conditional Access
- description: Automate access reviews, entitlement management, and lifecycle workflows to ensure proper access controls.
  name: Identity Governance
- description: Manage, control, and monitor privileged access with just-in-time and approval-based activation.
  name: Privileged Identity Management
- description: Issue and verify decentralized identity credentials using open standards for portable, self-sovereign identity.
  name: Verified ID
- description: Enable secure collaboration with external partners and customers through B2B and B2C identity management.
  name: External Identities
- description: Provide identity-centric secure web gateway and zero-trust network access for internet and private resources.
  name: Global Secure Access
- description: Secure and manage identities for applications, services, scripts, and containers running as software workloads.
  name: Workload Identities
finops:
- name: Microsoft Entra Finops
  service_category: Identity
  slug: microsoft-entra-finops
image: https://www.microsoft.com/en-us/security/content/dam/microsoft/final/security/includes/microsoft-entra-logo.svg
integrations:
- description: Deep integration for identity and access management across all Microsoft 365 applications and services.
  name: Microsoft 365
- description: Native identity provider for Azure resources including VMs, databases, storage, and managed identities.
  name: Azure Services
- description: Hybrid identity synchronization with on-premises Active Directory using Azure AD Connect.
  name: Active Directory
- description: SAML and SCIM integration for single sign-on and automated user provisioning with Salesforce.
  name: Salesforce
- description: SSO and automated provisioning integration with ServiceNow ITSM platform.
  name: ServiceNow
- description: Inbound provisioning from Workday HR to automate user lifecycle management.
  name: Workday
- description: SSO and provisioning integration with SAP applications and S/4HANA.
  name: SAP
- description: Cross-platform identity federation and migration support with Okta identity provider.
  name: Okta
json_schemas:
- name: ApiApplication
  property_count: 5
  slug: microsoft-entra-apiapplication
- name: Microsoft Entra Application
  property_count: 24
  slug: microsoft-entra-application
- name: ApplicationCollectionResponse
  property_count: 4
  slug: microsoft-entra-applicationcollectionresponse
- name: AppRole
  property_count: 6
  slug: microsoft-entra-approle
- name: AppRoleAssignment
  property_count: 8
  slug: microsoft-entra-approleassignment
- name: AppRoleAssignmentCollectionResponse
  property_count: 4
  slug: microsoft-entra-approleassignmentcollectionresponse
- name: AssignedLicense
  property_count: 2
  slug: microsoft-entra-assignedlicense
- name: DirectoryObject
  property_count: 3
  slug: microsoft-entra-directoryobject
- name: DirectoryObjectCollectionResponse
  property_count: 4
  slug: microsoft-entra-directoryobjectcollectionresponse
- name: ApiApplication
  property_count: 5
  slug: microsoft-entra-graph-identity-api-application
- name: AppRoleAssignmentCollectionResponse
  property_count: 4
  slug: microsoft-entra-graph-identity-app-role-assignment-collection-response
- name: AppRoleAssignment
  property_count: 8
  slug: microsoft-entra-graph-identity-app-role-assignment
- name: AppRole
  property_count: 6
  slug: microsoft-entra-graph-identity-app-role
- name: ApplicationCollectionResponse
  property_count: 4
  slug: microsoft-entra-graph-identity-application-collection-response
- name: Application
  property_count: 13
  slug: microsoft-entra-graph-identity-application
- name: AssignedLicense
  property_count: 2
  slug: microsoft-entra-graph-identity-assigned-license
- name: DirectoryObjectCollectionResponse
  property_count: 4
  slug: microsoft-entra-graph-identity-directory-object-collection-response
- name: DirectoryObject
  property_count: 3
  slug: microsoft-entra-graph-identity-directory-object
- name: GroupCollectionResponse
  property_count: 4
  slug: microsoft-entra-graph-identity-group-collection-response
- name: Group
  property_count: 18
  slug: microsoft-entra-graph-identity-group
- name: KeyCredential
  property_count: 7
  slug: microsoft-entra-graph-identity-key-credential
- name: ODataError
  property_count: 1
  slug: microsoft-entra-graph-identity-o-data-error
- name: ODataReference
  property_count: 1
  slug: microsoft-entra-graph-identity-o-data-reference
- name: PasswordCredential
  property_count: 6
  slug: microsoft-entra-graph-identity-password-credential
- name: PasswordProfile
  property_count: 3
  slug: microsoft-entra-graph-identity-password-profile
- name: PermissionScope
  property_count: 8
  slug: microsoft-entra-graph-identity-permission-scope
- name: RequiredResourceAccess
  property_count: 2
  slug: microsoft-entra-graph-identity-required-resource-access
- name: ServicePrincipalCollectionResponse
  property_count: 4
  slug: microsoft-entra-graph-identity-service-principal-collection-response
- name: ServicePrincipal
  property_count: 20
  slug: microsoft-entra-graph-identity-service-principal
- name: SpaApplication
  property_count: 1
  slug: microsoft-entra-graph-identity-spa-application
- name: UserCollectionResponse
  property_count: 4
  slug: microsoft-entra-graph-identity-user-collection-response
- name: User
  property_count: 31
  slug: microsoft-entra-graph-identity-user
- name: WebApplication
  property_count: 4
  slug: microsoft-entra-graph-identity-web-application
- name: Group
  property_count: 18
  slug: microsoft-entra-group
- name: GroupCollectionResponse
  property_count: 4
  slug: microsoft-entra-groupcollectionresponse
- name: KeyCredential
  property_count: 7
  slug: microsoft-entra-keycredential
- name: ODataError
  property_count: 1
  slug: microsoft-entra-odataerror
- name: ODataReference
  property_count: 1
  slug: microsoft-entra-odatareference
- name: PasswordCredential
  property_count: 6
  slug: microsoft-entra-passwordcredential
- name: PasswordProfile
  property_count: 3
  slug: microsoft-entra-passwordprofile
- name: PermissionScope
  property_count: 8
  slug: microsoft-entra-permissionscope
- name: RequiredResourceAccess
  property_count: 2
  slug: microsoft-entra-requiredresourceaccess
- name: ServicePrincipal
  property_count: 20
  slug: microsoft-entra-serviceprincipal
- name: ServicePrincipalCollectionResponse
  property_count: 4
  slug: microsoft-entra-serviceprincipalcollectionresponse
- name: SpaApplication
  property_count: 1
  slug: microsoft-entra-spaapplication
- name: Microsoft Entra User
  property_count: 39
  slug: microsoft-entra-user
- name: UserCollectionResponse
  property_count: 4
  slug: microsoft-entra-usercollectionresponse
- name: WebApplication
  property_count: 4
  slug: microsoft-entra-webapplication
json_structures:
- name: Microsoft Entra Graph Identity Api Application Structure
  property_count: 5
  slug: microsoft-entra-graph-identity-api-application-structure
- name: Microsoft Entra Graph Identity App Role Assignment Collection Response Structure
  property_count: 4
  slug: microsoft-entra-graph-identity-app-role-assignment-collection-response-structure
- name: Microsoft Entra Graph Identity App Role Assignment Structure
  property_count: 8
  slug: microsoft-entra-graph-identity-app-role-assignment-structure
- name: Microsoft Entra Graph Identity App Role Structure
  property_count: 6
  slug: microsoft-entra-graph-identity-app-role-structure
- name: Microsoft Entra Graph Identity Application Collection Response Structure
  property_count: 4
  slug: microsoft-entra-graph-identity-application-collection-response-structure
- name: Microsoft Entra Graph Identity Application Structure
  property_count: 13
  slug: microsoft-entra-graph-identity-application-structure
- name: Microsoft Entra Graph Identity Assigned License Structure
  property_count: 2
  slug: microsoft-entra-graph-identity-assigned-license-structure
- name: Microsoft Entra Graph Identity Directory Object Collection Response Structure
  property_count: 4
  slug: microsoft-entra-graph-identity-directory-object-collection-response-structure
- name: Microsoft Entra Graph Identity Directory Object Structure
  property_count: 3
  slug: microsoft-entra-graph-identity-directory-object-structure
- name: Microsoft Entra Graph Identity Group Collection Response Structure
  property_count: 4
  slug: microsoft-entra-graph-identity-group-collection-response-structure
- name: Microsoft Entra Graph Identity Group Structure
  property_count: 18
  slug: microsoft-entra-graph-identity-group-structure
- name: Microsoft Entra Graph Identity Key Credential Structure
  property_count: 7
  slug: microsoft-entra-graph-identity-key-credential-structure
- name: Microsoft Entra Graph Identity O Data Error Structure
  property_count: 1
  slug: microsoft-entra-graph-identity-o-data-error-structure
- name: Microsoft Entra Graph Identity O Data Reference Structure
  property_count: 1
  slug: microsoft-entra-graph-identity-o-data-reference-structure
- name: Microsoft Entra Graph Identity Password Credential Structure
  property_count: 6
  slug: microsoft-entra-graph-identity-password-credential-structure
- name: Microsoft Entra Graph Identity Password Profile Structure
  property_count: 3
  slug: microsoft-entra-graph-identity-password-profile-structure
- name: Microsoft Entra Graph Identity Permission Scope Structure
  property_count: 8
  slug: microsoft-entra-graph-identity-permission-scope-structure
- name: Microsoft Entra Graph Identity Required Resource Access Structure
  property_count: 2
  slug: microsoft-entra-graph-identity-required-resource-access-structure
- name: Microsoft Entra Graph Identity Service Principal Collection Response Structure
  property_count: 4
  slug: microsoft-entra-graph-identity-service-principal-collection-response-structure
- name: Microsoft Entra Graph Identity Service Principal Structure
  property_count: 20
  slug: microsoft-entra-graph-identity-service-principal-structure
- name: Microsoft Entra Graph Identity Spa Application Structure
  property_count: 1
  slug: microsoft-entra-graph-identity-spa-application-structure
- name: Microsoft Entra Graph Identity User Collection Response Structure
  property_count: 4
  slug: microsoft-entra-graph-identity-user-collection-response-structure
- name: Microsoft Entra Graph Identity User Structure
  property_count: 31
  slug: microsoft-entra-graph-identity-user-structure
- name: Microsoft Entra Graph Identity Web Application Structure
  property_count: 4
  slug: microsoft-entra-graph-identity-web-application-structure
- name: Microsoft Entra Structure
  property_count: 0
  slug: microsoft-entra-structure
jsonld:
- class_count: 0
  name: Microsoft Entra Context
  property_count: 5
  slug: microsoft-entra-context
- class_count: 0
  name: Microsoft Entra Graph Identity Context
  property_count: 0
  slug: microsoft-entra-graph-identity-context
layout: provider
modified: '2026-05-19'
name: Microsoft Entra
nav: Providers
network: true
overview: 'Microsoft Entra publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Groups API, ServicePrincipals API, and 1 more. Tagged areas include Access Management, Authentication, Azure AD, Entra, and Identity.


  The Microsoft Entra catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Microsoft Entra''s developer surface includes authentication, developer portal, getting-started guide, engineering blog, support, changelog, pricing, and 29 more developer resources.'
plans:
- name: Microsoft Entra Plans Pricing
  plan_count: 10
  slug: microsoft-entra-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 9
  name: Microsoft Entra Rate Limits
  slug: microsoft-entra-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Microsoft Entra API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-entra-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Microsoft Entra API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 8
  slug: microsoft-entra-spectral-rules
scopes:
- name: Microsoft Entra Scopes
  scope_count: 13
  slug: microsoft-entra-scopes
  summary_line: 13 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 52.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 50.5
    catalog_earned_first_party: 0.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 13.6
    contract_quality: 68.7
    developer_ergonomics: 65.5
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 42.1
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-entra/refs/heads/main/screenshots/microsoft-entra-2026-06-20T185457.png
security:
- kind: authentication
  name: Microsoft Entra Authentication
  slug: microsoft-entra-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Entra Domain Security
  slug: microsoft-entra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Entra Vulnerability Disclosure
  slug: microsoft-entra-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-entra
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
use_cases:
- description: Implement zero trust architecture with identity-based access controls, conditional access policies, and continuous verification.
  name: Zero Trust Implementation
- description: Synchronize and manage identities across on-premises Active Directory and cloud environments.
  name: Hybrid Identity Management
- description: Enable SSO for thousands of SaaS and on-premises applications with SAML, OIDC, and password-based authentication.
  name: Application Single Sign-On
- description: Automate user lifecycle management with SCIM-based provisioning and deprovisioning across integrated applications.
  name: Automated User Provisioning
- description: Create, secure, and monitor identities for AI agents with authentication, authorization, and lifecycle management.
  name: AI Agent Identity Management
website: https://entra.microsoft.com/
---
