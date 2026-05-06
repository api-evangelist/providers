---
name: Microsoft Active Directory
description: Microsoft Active Directory and Microsoft Entra ID provide identity and access management for organizations of all sizes. Microsoft Graph API is the unified REST API gateway for accessing and managing Microsoft Entra ID (formerly Azure Active Directory), including users, groups, applications, devices, conditional access policies, identity governance, and directory administration. Legacy on-premises Active Directory is managed through LDAP, Kerberos, and PowerShell protocols; cloud identity is managed through Microsoft Graph.
image: https://learn.microsoft.com/en-us/entra/media/index/active-directory.svg
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Active Directory
  - Authentication
  - Authorization
  - Directory Services
  - Identity Management
  - Microsoft Entra
  - Zero Trust
apis:
  - name: Microsoft Graph Users API
    description: Manage the entire lifecycle of users in Microsoft Entra ID, including creating, reading, updating, and deleting user accounts, managing licenses, group memberships, authentication methods, and profile photos. Supports both v1.0 and beta endpoints.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/users
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Directory Services
      - Identity Management
      - Users
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/users
      - type: OpenAPI
        url: openapi/active-directory-users-openapi.yaml
      - type: JSONSchema
        url: json-schema/users-user-schema.json
      - type: JSONSchema
        url: json-schema/users-password-profile-schema.json
      - type: JSONStructure
        url: json-structure/users-user-structure.json
      - type: Example
        url: examples/users-user-example.json
      - type: NaftikoCapability
        url: capabilities/shared/active-directory-users.yaml
  - name: Microsoft Graph Groups API
    description: Create and manage Microsoft Entra security groups, Microsoft 365 groups, and distribution lists. Manage group memberships, owners, and settings. Groups enable efficient entitlement management for users, licensing, and resource access.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/groups-overview
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Directory Services
      - Groups
      - Identity Management
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/groups-overview
      - type: OpenAPI
        url: openapi/active-directory-groups-openapi.yaml
      - type: JSONSchema
        url: json-schema/groups-group-schema.json
      - type: JSONStructure
        url: json-structure/groups-group-structure.json
      - type: Example
        url: examples/groups-group-example.json
      - type: NaftikoCapability
        url: capabilities/shared/active-directory-groups.yaml
  - name: Microsoft Graph Applications and Service Principals API
    description: Register and manage Microsoft Entra applications and their associated service principals programmatically. Configure app permissions, OAuth2 permission grants, app role assignments, certificates, federated identity credentials, and app consent policies.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/applications-api-overview
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Applications
      - Identity Management
      - OAuth2
      - Service Principals
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/applications-api-overview
      - type: OpenAPI
        url: openapi/active-directory-applications-openapi.yaml
      - type: JSONSchema
        url: json-schema/applications-application-schema.json
      - type: JSONSchema
        url: json-schema/applications-service-principal-schema.json
      - type: JSONStructure
        url: json-structure/applications-application-structure.json
      - type: Example
        url: examples/applications-application-example.json
      - type: NaftikoCapability
        url: capabilities/shared/active-directory-applications.yaml
  - name: Microsoft Graph Devices API
    description: Manage devices registered or joined to Microsoft Entra ID, including Entra joined, Entra registered, and hybrid Azure AD joined devices. Retrieve BitLocker recovery keys and Local Admin Password Solution (LAPS) credentials for managed devices.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/device
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Devices
      - Endpoint Management
      - Identity Management
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/device
  - name: Microsoft Graph Directory Roles and Administrative Units API
    description: Manage Microsoft Entra built-in and custom directory roles, role assignments, and role-scoped administrative units. Assign administrator roles to users, groups, or service principals, and create scoped role assignments via administrative units.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/directoryrole
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Authorization
      - Directory Services
      - Role Management
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/directoryrole
  - name: Microsoft Graph Conditional Access API
    description: Create and manage Microsoft Entra Conditional Access policies that enforce access controls based on user, location, device, and risk signals. Configure named locations, authentication context class references, and evaluate policy impact using what-if analysis.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccesspolicy
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Authorization
      - Conditional Access
      - Security
      - Zero Trust
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccesspolicy
  - name: Microsoft Graph Identity Governance API
    description: Manage Microsoft Entra ID Governance features including access reviews, entitlement management (access packages, catalogs, and policies), Privileged Identity Management (PIM) for just-in-time role activation, and lifecycle workflows for joiner/mover/leaver employee identity lifecycle automation.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-overview
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Governance
      - Identity Management
      - Lifecycle Management
      - Privileged Identity Management
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-overview
  - name: Microsoft Graph Identity Protection API
    description: Detect, investigate, and remediate identity-based risks using Microsoft Entra ID Protection. Access risk detections, risky users, risky service principals, and risk events, and feed data into SIEM tools for security correlation and incident response.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/identityprotection-overview
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Identity Protection
      - Risk Management
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/identityprotection-overview
  - name: Microsoft Graph Authentication Methods API
    description: Manage authentication methods registered for users in Microsoft Entra ID, including FIDO2 security keys, Microsoft Authenticator, phone (SMS/voice call), email OTP, Windows Hello for Business, and temporary access passes. Configure authentication method policies and authentication strength requirements.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/authenticationmethods-overview
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Authentication
      - MFA
      - Passwordless
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/authenticationmethods-overview
  - name: Microsoft Graph Identity and Access Reports API
    description: Access audit logs, sign-in logs, provisioning logs, and identity-related reports for monitoring, compliance, and troubleshooting. Stream logs to Azure Monitor and Log Analytics or to third-party SIEM tools for security operations.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/report-identity-access
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Audit Logs
      - Compliance
      - Monitoring
      - Reports
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/report-identity-access
common:
  - type: Portal
    url: https://developer.microsoft.com/en-us/graph
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/graph/get-started
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/overview
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/auth-concepts
  - type: APIReference
    url: https://learn.microsoft.com/en-us/graph/api/overview
  - type: RateLimits
    url: https://learn.microsoft.com/en-us/graph/throttling
  - type: SDK
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: CLI
    url: https://learn.microsoft.com/en-us/cli/azure/ad
  - type: Blog
    url: https://devblogs.microsoft.com/microsoft365dev/
  - type: StatusPage
    url: https://azure.status.microsoft.com/
  - type: Support
    url: https://developer.microsoft.com/en-us/graph/support
  - type: TermsOfService
    url: https://learn.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/privacystatement
  - type: Pricing
    url: https://www.microsoft.com/en-us/security/business/microsoft-entra-pricing
  - type: ChangeLog
    url: https://learn.microsoft.com/en-us/graph/changelog
  - type: GitHubOrganization
    url: https://github.com/microsoftgraph
  - type: GitHubRepository
    url: https://github.com/microsoftgraph/microsoft-graph-openapi
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/microsoft-graph
  - type: Training
    url: https://learn.microsoft.com/en-us/training/paths/m365-msgraph-associate/
  - type: SpectralRules
    url: rules/active-directory-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/identity-management-operations.yaml
  - type: Vocabulary
    url: vocabulary/active-directory-vocabulary.yaml
  - type: JSON-LD
    url: json-ld/active-directory-context.jsonld
  - type: Features
    data:
      - name: Unified Identity API
        description: Single REST endpoint (graph.microsoft.com) for all Microsoft Entra identity and directory operations.
      - name: User Lifecycle Management
        description: Full CRUD operations for user accounts including bulk operations, license assignment, and guest management.
      - name: Group Management
        description: Create and manage security groups, Microsoft 365 groups, and dynamic membership groups.
      - name: Application Registration
        description: Programmatic app registration, permission configuration, and service principal management.
      - name: Conditional Access Automation
        description: Create, update, and evaluate Conditional Access policies via API for Zero Trust enforcement.
      - name: Privileged Identity Management
        description: Just-in-time role activation, time-bound access, and PIM policy management via API.
      - name: Identity Protection
        description: Access risk signals, risky users, and risk detections for automated threat response.
      - name: Authentication Method Management
        description: Manage MFA and passwordless authentication methods registered for users.
      - name: Audit and Sign-in Logs
        description: Programmatic access to audit logs, sign-in logs, and provisioning logs for SIEM integration.
      - name: Identity Governance
        description: Access reviews, entitlement management, and lifecycle workflows for automated IAM.
  - type: UseCases
    data:
      - name: User Provisioning Automation
        description: Automate user account creation, attribute updates, and deprovisioning for HR-driven identity lifecycle.
      - name: Zero Trust Policy Enforcement
        description: Programmatically deploy and manage Conditional Access policies across the organization.
      - name: SIEM Integration
        description: Stream audit logs and sign-in events to security information and event management systems.
      - name: Application Access Management
        description: Automate app registration, permission grants, and app role assignments for developer self-service.
      - name: Identity Risk Remediation
        description: Detect and respond to risky sign-ins and compromised accounts via Identity Protection APIs.
      - name: Compliance Reporting
        description: Generate access reviews, entitlement reports, and audit logs for regulatory compliance.
      - name: Privileged Access Governance
        description: Enforce just-in-time privileged access and audit role assignments via PIM APIs.
  - type: Integrations
    data:
      - name: Azure Active Directory
        description: Microsoft Entra ID (formerly Azure AD) is the cloud identity backbone accessed via Microsoft Graph.
      - name: Microsoft 365
        description: Microsoft Graph provides unified access to Microsoft 365 user data alongside identity operations.
      - name: Azure Monitor
        description: Stream Microsoft Entra sign-in and audit logs to Azure Monitor Log Analytics for analysis.
      - name: Microsoft Sentinel
        description: Feed identity risk signals and audit logs into Microsoft Sentinel SIEM for threat hunting.
      - name: Intune
        description: Microsoft Graph Intune APIs integrate device management with identity policies.
      - name: SCIM Providers
        description: Automate user provisioning to SaaS applications using Microsoft Entra SCIM provisioning.
      - name: SAML and OIDC Applications
        description: Register and manage federated applications using SAML 2.0 and OpenID Connect via Microsoft Graph.
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
---
