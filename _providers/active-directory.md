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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Active Directory Agentic Access
  operation_count: 25
  slug: active-directory-agentic-access
  summary_line: 25 operations · 11 acting
api_count: 14
apis:
- description: Manage devices registered or joined to Microsoft Entra ID, including Entra joined, Entra registered, and hybrid Azure AD joined devices. Retrieve BitLocker recovery keys and Local Admin Password Solut
  name: Microsoft Graph Devices API
  slug: microsoft-graph-devices-api
- description: Manage Microsoft Entra built-in and custom directory roles, role assignments, and role-scoped administrative units. Assign administrator roles to users, groups, or service principals, and create scope
  name: Microsoft Graph Directory Roles and Administrative Units API
  slug: microsoft-graph-directory-roles-and-administrative-units-api
- description: Create and manage Microsoft Entra Conditional Access policies that enforce access controls based on user, location, device, and risk signals. Configure named locations, authentication context class re
  name: Microsoft Graph Conditional Access API
  slug: microsoft-graph-conditional-access-api
- description: Manage Microsoft Entra ID Governance features including access reviews, entitlement management (access packages, catalogs, and policies), Privileged Identity Management (PIM) for just-in-time role act
  name: Microsoft Graph Identity Governance API
  slug: microsoft-graph-identity-governance-api
- description: Detect, investigate, and remediate identity-based risks using Microsoft Entra ID Protection. Access risk detections, risky users, risky service principals, and risk events, and feed data into SIEM too
  name: Microsoft Graph Identity Protection API
  slug: microsoft-graph-identity-protection-api
- description: Manage authentication methods registered for users in Microsoft Entra ID, including FIDO2 security keys, Microsoft Authenticator, phone (SMS/voice call), email OTP, Windows Hello for Business, and tem
  name: Microsoft Graph Authentication Methods API
  slug: microsoft-graph-authentication-methods-api
- description: 'Access audit logs, sign-in logs, provisioning logs, and identity-related reports for monitoring, compliance, and troubleshooting. Stream logs to Azure Monitor and Log Analytics or to third-party SIEM '
  name: Microsoft Graph Identity and Access Reports API
  slug: microsoft-graph-identity-and-access-reports-api
- description: The App Role Assignments API from Microsoft Active Directory — 1 operation(s) for app role assignments.
  name: Microsoft Active Directory App Role Assignments API
  slug: active-directory-app-role-assignments-api
- description: The Applications API from Microsoft Active Directory — 2 operation(s) for applications.
  name: Microsoft Active Directory Applications API
  slug: active-directory-applications-api
- description: The Groups API from Microsoft Active Directory — 6 operation(s) for groups.
  name: Microsoft Active Directory Groups API
  slug: active-directory-groups-api
- description: The Members API from Microsoft Active Directory — 2 operation(s) for members.
  name: Microsoft Active Directory Members API
  slug: active-directory-members-api
- description: The Owners API from Microsoft Active Directory — 1 operation(s) for owners.
  name: Microsoft Active Directory Owners API
  slug: active-directory-owners-api
- description: The Service Principals API from Microsoft Active Directory — 3 operation(s) for service principals.
  name: Microsoft Active Directory Service Principals API
  slug: active-directory-service-principals-api
- description: The Users API from Microsoft Active Directory — 5 operation(s) for users.
  name: Microsoft Active Directory Users API
  slug: active-directory-users-api
arazzos:
- description: Resolve a user by UPN, read their full profile, then list their group memberships and manager.
  name: Active Directory Audit User Group Memberships
  slug: active-directory-audit-user-group-memberships-workflow
- description: Create a security group, then add two existing users to it by their object IDs.
  name: Active Directory Create Group And Add Two Members
  slug: active-directory-create-group-and-add-members-workflow
- description: Create a user, create a Microsoft 365 group owned by that user, and add the user as a member.
  name: Active Directory Create Microsoft 365 Group With Owner
  slug: active-directory-create-m365-group-with-owner-workflow
- description: Resolve an application by name, read its details, and soft-delete the registration.
  name: Active Directory Decommission Application
  slug: active-directory-decommission-application-workflow
- description: Look up a user by principal name, then patch their job title and department.
  name: Active Directory Find User And Update Profile
  slug: active-directory-find-user-and-update-profile-workflow
- description: Resolve a user by UPN, remove them from a named group, then disable the account.
  name: Active Directory Offboard User From Group
  slug: active-directory-offboard-user-from-group-workflow
- description: Find an existing group by name, create a user, and add the user to that group.
  name: Active Directory Onboard User To Existing Group
  slug: active-directory-onboard-user-to-existing-group-workflow
- description: Register an application, then locate and read its service principal and app role assignments.
  name: Active Directory Provision Application With Service Principal
  slug: active-directory-provision-application-with-membership-workflow
- description: Create a user, create a security group, and add the user as a member of that group.
  name: Active Directory Provision User Into New Group
  slug: active-directory-provision-user-into-new-group-workflow
- description: Resolve a group by name, update its display name and description, then list its members and owners.
  name: Active Directory Rename Group And List Members
  slug: active-directory-rename-group-and-list-members-workflow
- description: Read the signed-in user's profile, then list their group memberships and look up their manager.
  name: Active Directory Self-Service Profile Review
  slug: active-directory-self-service-profile-review-workflow
- description: Resolve a user and two groups by name, remove the user from one group and add them to another.
  name: Active Directory Transfer User Between Groups
  slug: active-directory-transfer-user-between-groups-workflow
- description: Resolve an application by name, read it, then patch its web redirect URIs and description.
  name: Active Directory Update Application Redirect URIs
  slug: active-directory-update-application-redirect-uris-workflow
artifact_total: 76
collections:
- collection_type: postman
  name: Microsoft Graph Applications and Service Principals API
  slug: postman-active-directory-applications
- collection_type: postman
  name: Microsoft Graph Groups API
  slug: postman-active-directory-groups
- collection_type: postman
  name: Microsoft Graph Users API
  slug: postman-active-directory-users
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/active-directory-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/active-directory-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/active-directory-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/active-directory-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/active-directory-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-active-directory/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/active-directory-audit-user-group-memberships-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/active-directory-create-group-and-add-members-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/active-directory-create-m365-group-with-owner-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/active-directory-decommission-application-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/active-directory-find-user-and-update-profile-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/active-directory-offboard-user-from-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/active-directory-onboard-user-to-existing-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/active-directory-provision-application-with-membership-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/active-directory-provision-user-into-new-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/active-directory-rename-group-and-list-members-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/active-directory-self-service-profile-review-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/active-directory-transfer-user-between-groups-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/active-directory-update-application-redirect-uris-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/graph
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/graph/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph/overview
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/auth-concepts
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/graph/api/overview
- group: operate
  title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/graph/throttling
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- group: build
  title: ''
  type: CLI
  url: https://learn.microsoft.com/en-us/cli/azure/ad
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/microsoft365dev/
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.microsoft.com/en-us/graph/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://learn.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/privacystatement
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/security/business/microsoft-entra-pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/graph/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoftgraph
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoftgraph/microsoft-graph-openapi
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/microsoft-graph
- group: learn
  title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/paths/m365-msgraph-associate/
- group: design
  title: ''
  type: SpectralRules
  url: rules/active-directory-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/active-directory-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/active-directory-context.jsonld
created: '2024-01-01'
description: Microsoft Active Directory and Microsoft Entra ID provide identity and access management for organizations of all sizes. Microsoft Graph API is the unified REST API gateway for accessing and managing Microsoft Entra ID (formerly Azure Active Directory), including users, groups, applications, devices, conditional access policies, identity governance, and directory administration. Legacy on-premises Active Directory is managed through LDAP, Kerberos, and PowerShell protocols; cloud identity is managed through Microsoft Graph.
examples:
- key_count: 12
  name: Applications Application Example
  slug: applications-application-example
- key_count: 17
  name: Groups Group Example
  slug: groups-group-example
- key_count: 22
  name: Users User Example
  slug: users-user-example
features:
- description: Single REST endpoint (graph.microsoft.com) for all Microsoft Entra identity and directory operations.
  name: Unified Identity API
- description: Full CRUD operations for user accounts including bulk operations, license assignment, and guest management.
  name: User Lifecycle Management
- description: Create and manage security groups, Microsoft 365 groups, and dynamic membership groups.
  name: Group Management
- description: Programmatic app registration, permission configuration, and service principal management.
  name: Application Registration
- description: Create, update, and evaluate Conditional Access policies via API for Zero Trust enforcement.
  name: Conditional Access Automation
- description: Just-in-time role activation, time-bound access, and PIM policy management via API.
  name: Privileged Identity Management
- description: Access risk signals, risky users, and risk detections for automated threat response.
  name: Identity Protection
- description: Manage MFA and passwordless authentication methods registered for users.
  name: Authentication Method Management
- description: Programmatic access to audit logs, sign-in logs, and provisioning logs for SIEM integration.
  name: Audit and Sign-in Logs
- description: Access reviews, entitlement management, and lifecycle workflows for automated IAM.
  name: Identity Governance
finops:
- name: Active Directory Finops
  service_category: Identity / Directory Services
  slug: active-directory-finops
image: https://learn.microsoft.com/en-us/entra/media/index/active-directory.svg
integrations:
- description: Microsoft Entra ID (formerly Azure AD) is the cloud identity backbone accessed via Microsoft Graph.
  name: Azure Active Directory
- description: Microsoft Graph provides unified access to Microsoft 365 user data alongside identity operations.
  name: Microsoft 365
- description: Stream Microsoft Entra sign-in and audit logs to Azure Monitor Log Analytics for analysis.
  name: Azure Monitor
- description: Feed identity risk signals and audit logs into Microsoft Sentinel SIEM for threat hunting.
  name: Microsoft Sentinel
- description: Microsoft Graph Intune APIs integrate device management with identity policies.
  name: Intune
- description: Automate user provisioning to SaaS applications using Microsoft Entra SCIM provisioning.
  name: SCIM Providers
- description: Register and manage federated applications using SAML 2.0 and OpenID Connect via Microsoft Graph.
  name: SAML and OIDC Applications
json_schemas:
- name: Application
  property_count: 12
  slug: applications-application
- name: ServicePrincipal
  property_count: 12
  slug: applications-service-principal
- name: Group
  property_count: 18
  slug: groups-group
- name: PasswordProfile
  property_count: 3
  slug: users-password-profile
- name: User
  property_count: 22
  slug: users-user
json_structures:
- name: Applications Application Structure
  property_count: 0
  slug: applications-application-structure
- name: Groups Group Structure
  property_count: 0
  slug: groups-group-structure
- name: Users User Structure
  property_count: 0
  slug: users-user-structure
jsonld:
- class_count: 1
  name: Active Directory Context
  property_count: 69
  slug: active-directory-context
layout: provider
modified: '2026-05-19'
name: Microsoft Active Directory
nav: Providers
network: true
overview: 'Microsoft Active Directory publishes 7 APIs on the [APIs.io](https://apis.io/) network, including App Role Assignments API, Applications API, Groups API, and 4 more. Tagged areas include Active Directory, Authentication, Authorization, Directory Services, and Identity Management.


  The Microsoft Active Directory catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Microsoft Active Directory''s developer surface includes authentication, developer portal, getting-started guide, documentation, API reference, CLI, engineering blog, and 34 more developer resources.'
plans:
- name: Active Directory Plans Pricing
  plan_count: 8
  slug: active-directory-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 7
  name: Active Directory Rate Limits
  slug: active-directory-rate-limits
rules:
- name: Microsoft Active Directory API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: active-directory-jsonschema-spectral-rules
- name: Microsoft Active Directory API Rules
  rule_count: 39
  severity_counts:
    error: 14
    hint: 0
    info: 5
    warn: 20
  slug: active-directory-spectral-rules
scopes:
- name: Active Directory Scopes
  scope_count: 11
  slug: active-directory-scopes
  summary_line: 11 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 71.5
  delta: -4.8
  facets:
    commercial_clarity: 71.1
    contract_quality: 75.3
    developer_ergonomics: 69.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 68.4
  previous_composite: 76.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/active-directory/refs/heads/main/screenshots/active-directory-2026-07-25T181526.png
security:
- kind: authentication
  name: Active Directory Authentication
  slug: active-directory-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Active Directory Domain Security
  slug: active-directory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Active Directory Vulnerability Disclosure
  slug: active-directory-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: active-directory
tags:
- Active Directory
- Authentication
- Authorization
- Directory Services
- Identity Management
- Microsoft Entra
- Zero Trust
use_cases:
- description: Automate user account creation, attribute updates, and deprovisioning for HR-driven identity lifecycle.
  name: User Provisioning Automation
- description: Programmatically deploy and manage Conditional Access policies across the organization.
  name: Zero Trust Policy Enforcement
- description: Stream audit logs and sign-in events to security information and event management systems.
  name: SIEM Integration
- description: Automate app registration, permission grants, and app role assignments for developer self-service.
  name: Application Access Management
- description: Detect and respond to risky sign-ins and compromised accounts via Identity Protection APIs.
  name: Identity Risk Remediation
- description: Generate access reviews, entitlement reports, and audit logs for regulatory compliance.
  name: Compliance Reporting
- description: Enforce just-in-time privileged access and audit role assignments via PIM APIs.
  name: Privileged Access Governance
website: https://developer.microsoft.com/en-us/graph
---
