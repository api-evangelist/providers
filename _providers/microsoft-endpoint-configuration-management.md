---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 31
  human_in_the_loop: 2
  name: Microsoft Endpoint Configuration Management Agentic Access
  operation_count: 71
  slug: microsoft-endpoint-configuration-management-agentic-access
  summary_line: 71 operations · 31 acting · 2 human-in-the-loop
api_count: 25
apis:
- description: PowerShell module for Configuration Manager automation and scripting, providing over 1100 cmdlets for all major management tasks including device collections, software deployment, and compliance setti
  name: Configuration Manager PowerShell Cmdlets
  slug: configuration-manager-powershell-cmdlets
- description: Software Development Kit for extending and integrating with Configuration Manager, including WMI providers, class schemas, and programming interfaces for custom solutions.
  name: Configuration Manager SDK
  slug: configuration-manager-sdk
- description: SDKs for iOS and Android that enable mobile apps to support Intune app protection policies. Allows developers to integrate mobile application management features into line-of-business and partner apps
  name: Intune App SDK
  slug: intune-app-sdk
- description: Command-line tools for iOS and Android that enable existing line-of-business apps to be managed by Intune app protection policies without requiring source code changes.
  name: Intune App Wrapping Tool
  slug: intune-app-wrapping-tool
- description: PowerShell module providing native cmdlet support for invoking the Microsoft Intune Graph API. Enables IT administrators to automate device management, app deployment, and compliance policy operations
  name: Intune PowerShell SDK
  slug: intune-powershell-sdk
- description: Manage Configuration Manager applications.
  name: Microsoft Endpoint Configuration Management Applications API
  slug: microsoft-endpoint-configuration-management-applications-api
- description: Manage device and user collections.
  name: Microsoft Endpoint Configuration Management Collections API
  slug: microsoft-endpoint-configuration-management-collections-api
- description: Manage compliance baselines and settings.
  name: Microsoft Endpoint Configuration Management Compliance API
  slug: microsoft-endpoint-configuration-management-compliance-api
- description: Manage device compliance policies.
  name: Microsoft Endpoint Configuration Management Compliance Policies API
  slug: microsoft-endpoint-configuration-management-compliance-policies-api
- description: Manage device configuration profiles.
  name: Microsoft Endpoint Configuration Management Configuration Profiles API
  slug: microsoft-endpoint-configuration-management-configuration-profiles-api
- description: Date dimension for time-based reporting.
  name: Microsoft Endpoint Configuration Management Dates API
  slug: microsoft-endpoint-configuration-management-dates-api
- description: View and manage application deployments.
  name: Microsoft Endpoint Configuration Management Deployments API
  slug: microsoft-endpoint-configuration-management-deployments-api
- description: Remote device actions such as wipe, retire, sync, and lock.
  name: Microsoft Endpoint Configuration Management Device Actions API
  slug: microsoft-endpoint-configuration-management-device-actions-api
- description: Query and manage device resources.
  name: Microsoft Endpoint Configuration Management Devices API
  slug: microsoft-endpoint-configuration-management-devices-api
- description: Manage asynchronous report export jobs. Create export jobs, poll for completion, and download exported report files.
  name: Microsoft Endpoint Configuration Management Export Jobs API
  slug: microsoft-endpoint-configuration-management-export-jobs-api
- description: Intune management extension activities.
  name: Microsoft Endpoint Configuration Management Management Extensions API
  slug: microsoft-endpoint-configuration-management-management-extensions-api
- description: Manage legacy software packages.
  name: Microsoft Endpoint Configuration Management Packages API
  slug: microsoft-endpoint-configuration-management-packages-api
- description: Policy records and compliance activities.
  name: Microsoft Endpoint Configuration Management Policies API
  slug: microsoft-endpoint-configuration-management-policies-api
- description: Retrieve inline Intune reports for device compliance, configuration policy status, and historical data.
  name: Microsoft Endpoint Configuration Management Reports API
  slug: microsoft-endpoint-configuration-management-reports-api
- description: Manage and execute PowerShell scripts.
  name: Microsoft Endpoint Configuration Management Scripts API
  slug: microsoft-endpoint-configuration-management-scripts-api
- description: Site configuration and administration.
  name: Microsoft Endpoint Configuration Management Site Administration API
  slug: microsoft-endpoint-configuration-management-site-administration-api
- description: Query software update information.
  name: Microsoft Endpoint Configuration Management Software Updates API
  slug: microsoft-endpoint-configuration-management-software-updates-api
- description: Manage OS deployment task sequences.
  name: Microsoft Endpoint Configuration Management Task Sequences API
  slug: microsoft-endpoint-configuration-management-task-sequences-api
- description: User-to-device mapping records.
  name: Microsoft Endpoint Configuration Management User Device Associations API
  slug: microsoft-endpoint-configuration-management-user-device-associations-api
- description: User dimension records.
  name: Microsoft Endpoint Configuration Management Users API
  slug: microsoft-endpoint-configuration-management-users-api
arazzos:
- description: Create a Configuration Manager application and confirm it within the application inventory.
  name: Microsoft Endpoint Configuration Management ConfigMgr Create Application
  slug: microsoft-endpoint-configuration-management-configmgr-create-application-workflow
- description: Create a Configuration Manager collection, read it back, and review application deployments targeting collections.
  name: Microsoft Endpoint Configuration Management ConfigMgr Create Collection and Review Deployments
  slug: microsoft-endpoint-configuration-management-configmgr-create-collection-review-deployments-workflow
- description: Find a Configuration Manager device by name and read its full record and discovered system.
  name: Microsoft Endpoint Configuration Management ConfigMgr Device Lookup
  slug: microsoft-endpoint-configuration-management-configmgr-device-lookup-workflow
- description: Review pending software updates, configuration baseline assignments, and target collections.
  name: Microsoft Endpoint Configuration Management ConfigMgr Update Compliance Review
  slug: microsoft-endpoint-configuration-management-configmgr-update-compliance-review-workflow
- description: Create a device compliance policy in Intune and assign it to a target group.
  name: Microsoft Endpoint Configuration Management Create and Assign Compliance Policy
  slug: microsoft-endpoint-configuration-management-create-assign-compliance-policy-workflow
- description: Create a device configuration profile in Intune and assign it to a target group.
  name: Microsoft Endpoint Configuration Management Create and Assign Device Configuration
  slug: microsoft-endpoint-configuration-management-create-assign-device-configuration-workflow
- description: Confirm a managed device, factory wipe it, and remove it from Intune.
  name: Microsoft Endpoint Configuration Management Decommission Device
  slug: microsoft-endpoint-configuration-management-decommission-device-workflow
- description: Create a mobile app in Intune, assign it to a group, and inspect its install status.
  name: Microsoft Endpoint Configuration Management Deploy Mobile App
  slug: microsoft-endpoint-configuration-management-deploy-mobile-app-workflow
- description: Inspect a managed device and branch on its compliance state to either sync or retire it.
  name: Microsoft Endpoint Configuration Management Device Compliance Triage
  slug: microsoft-endpoint-configuration-management-device-compliance-triage-workflow
- description: Locate a managed device, remotely lock it, and reset its passcode.
  name: Microsoft Endpoint Configuration Management Lost Device Lockdown
  slug: microsoft-endpoint-configuration-management-lost-device-lockdown-workflow
- description: Pull the device, policy, and setting non-compliance reports inline in one pass.
  name: Microsoft Endpoint Configuration Management Non-Compliance Report Drilldown
  slug: microsoft-endpoint-configuration-management-noncompliance-report-drilldown-workflow
- description: Create an Intune report export job, poll it, and capture the download URL when complete.
  name: Microsoft Endpoint Configuration Management Report Export Job
  slug: microsoft-endpoint-configuration-management-report-export-job-workflow
- description: Inspect a mobile app and delete it only when it is still unpublished.
  name: Microsoft Endpoint Configuration Management Retire Unpublished App
  slug: microsoft-endpoint-configuration-management-retire-unpublished-app-workflow
- description: Read the tenant compliance summary and, when devices are non-compliant, enumerate them.
  name: Microsoft Endpoint Configuration Management Tenant Compliance Posture
  slug: microsoft-endpoint-configuration-management-tenant-compliance-posture-workflow
- description: Read an existing compliance policy, update its metadata, and reassign it to a group.
  name: Microsoft Endpoint Configuration Management Update and Reassign Compliance Policy
  slug: microsoft-endpoint-configuration-management-update-reassign-compliance-policy-workflow
- description: List a user's Azure AD owned devices and correlate them with their Intune managed devices.
  name: Microsoft Endpoint Configuration Management User Device Inventory
  slug: microsoft-endpoint-configuration-management-user-device-inventory-workflow
- description: Correlate Data Warehouse application inventory with install statuses and user-device associations.
  name: Microsoft Endpoint Configuration Management Data Warehouse App Install Analytics
  slug: microsoft-endpoint-configuration-management-warehouse-app-install-analytics-workflow
- description: Correlate Data Warehouse policies with their device activity and the device population.
  name: Microsoft Endpoint Configuration Management Data Warehouse Policy Compliance Analytics
  slug: microsoft-endpoint-configuration-management-warehouse-policy-compliance-analytics-workflow
artifact_total: 96
collections:
- collection_type: postman
  name: Microsoft Endpoint Configuration Management Configuration Manager REST API (AdminService)
  slug: postman-microsoft-endpoint-configuration-management-configmgr-rest-api
- collection_type: postman
  name: Microsoft Endpoint Configuration Management Intune Data Warehouse API
  slug: postman-microsoft-endpoint-configuration-management-intune-data-warehouse-api
- collection_type: postman
  name: Microsoft Endpoint Configuration Management Microsoft Intune Graph API
  slug: postman-microsoft-endpoint-configuration-management-intune-graph-api
- collection_type: postman
  name: Microsoft Endpoint Configuration Management Intune Reporting Export API
  slug: postman-microsoft-endpoint-configuration-management-intune-reporting-export-api
- collection_type: open
  name: Microsoft Endpoint Configuration Management Configuration Manager REST API (AdminService)
  slug: open-microsoft-endpoint-configuration-management-configmgr-rest-api
- collection_type: open
  name: Microsoft Endpoint Configuration Management Intune Data Warehouse API
  slug: open-microsoft-endpoint-configuration-management-intune-data-warehouse-api
- collection_type: open
  name: Microsoft Endpoint Configuration Management Microsoft Intune Graph API
  slug: open-microsoft-endpoint-configuration-management-intune-graph-api
- collection_type: open
  name: Microsoft Endpoint Configuration Management Intune Reporting Export API
  slug: open-microsoft-endpoint-configuration-management-intune-reporting-export-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-endpoint-configuration-management-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-endpoint-configuration-management-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-endpoint-configuration-management-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-endpoint-configuration-management-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-endpoint-configuration-management-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-endpoint-configuration-management/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-configmgr-create-application-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-configmgr-create-collection-review-deployments-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-configmgr-device-lookup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-configmgr-update-compliance-review-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-create-assign-compliance-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-create-assign-device-configuration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-decommission-device-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-deploy-mobile-app-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-device-compliance-triage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-lost-device-lockdown-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-noncompliance-report-drilldown-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-report-export-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-retire-unpublished-app-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-tenant-compliance-posture-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-update-reassign-compliance-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-user-device-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-warehouse-app-install-analytics-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-endpoint-configuration-management-warehouse-policy-compliance-analytics-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://endpoint.microsoft.com/
- group: start
  title: ''
  type: Console
  url: https://intune.microsoft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/intune/intune-service/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/intune/configmgr/core/understand/introduction
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/intune/intune-service/developer/intune-graph-apis
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/microsoft-endpoint-manager-blog/bg-p/MicrosoftEndpointManagerBlog
- group: operate
  title: ''
  type: Support
  url: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/contact-assisted-support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/whats-new
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/security/business/microsoft-intune-pricing
- group: start
  title: ''
  type: Signup
  url: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/free-trial-sign-up
- group: start
  title: ''
  type: Login
  url: https://intune.microsoft.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/licensing/terms/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoftgraph
- group: operate
  title: ''
  type: Community
  url: https://techcommunity.microsoft.com/category/microsoftintune/blog/microsoftintuneblog
- group: company
  title: ''
  type: Website
  url: https://learn.microsoft.com/en-us/intune/configmgr/
created: '2024'
description: Microsoft Endpoint Configuration Management (formerly System Center Configuration Manager) provides comprehensive management of devices and applications across an enterprise. It enables IT administrators to manage PCs, servers, and mobile devices, deploy software, manage compliance, and protect data.
finops:
- name: Microsoft Endpoint Configuration Management Finops
  service_category: Endpoint Management
  slug: microsoft-endpoint-configuration-management-finops
image: https://docs.microsoft.com/en-us/mem/configmgr/core/media/configmgr-logo.png
json_schemas:
- name: Mobile Application
  property_count: 16
  slug: microsoft-endpoint-configuration-management-application
- name: Device Compliance Policy
  property_count: 13
  slug: microsoft-endpoint-configuration-management-compliance-policy
- name: Device Configuration Profile
  property_count: 12
  slug: microsoft-endpoint-configuration-management-configuration-profile
- name: DateEntity
  property_count: 9
  slug: microsoft-endpoint-configuration-management-dateentity
- name: Managed Device
  property_count: 51
  slug: microsoft-endpoint-configuration-management-device
- name: DeviceCompliancePolicy
  property_count: 6
  slug: microsoft-endpoint-configuration-management-devicecompliancepolicy
- name: DeviceCompliancePolicyAssignment
  property_count: 2
  slug: microsoft-endpoint-configuration-management-devicecompliancepolicyassignment
- name: DeviceConfiguration
  property_count: 6
  slug: microsoft-endpoint-configuration-management-deviceconfiguration
- name: DeviceConfigurationAssignment
  property_count: 2
  slug: microsoft-endpoint-configuration-management-deviceconfigurationassignment
- name: DeviceManagementExportJob
  property_count: 11
  slug: microsoft-endpoint-configuration-management-devicemanagementexportjob
- name: DeviceManagementExportJobCreate
  property_count: 6
  slug: microsoft-endpoint-configuration-management-devicemanagementexportjobcreate
- name: DevicePropertyHistory
  property_count: 9
  slug: microsoft-endpoint-configuration-management-devicepropertyhistory
- name: IntuneManagementExtension
  property_count: 8
  slug: microsoft-endpoint-configuration-management-intunemanagementextension
- name: ManagedDevice
  property_count: 37
  slug: microsoft-endpoint-configuration-management-manageddevice
- name: MobileApp
  property_count: 14
  slug: microsoft-endpoint-configuration-management-mobileapp
- name: MobileAppAssignment
  property_count: 4
  slug: microsoft-endpoint-configuration-management-mobileappassignment
- name: MobileAppInstallStatus
  property_count: 6
  slug: microsoft-endpoint-configuration-management-mobileappinstallstatus
- name: ODataError
  property_count: 1
  slug: microsoft-endpoint-configuration-management-odataerror
- name: Policy
  property_count: 7
  slug: microsoft-endpoint-configuration-management-policy
- name: PolicyDeviceActivity
  property_count: 6
  slug: microsoft-endpoint-configuration-management-policydeviceactivity
- name: PolicyUserActivity
  property_count: 6
  slug: microsoft-endpoint-configuration-management-policyuseractivity
- name: ReportRequest
  property_count: 8
  slug: microsoft-endpoint-configuration-management-reportrequest
- name: ReportResponse
  property_count: 3
  slug: microsoft-endpoint-configuration-management-reportresponse
- name: SMS_Application
  property_count: 13
  slug: microsoft-endpoint-configuration-management-sms-application
- name: SMS_ApplicationDeployment
  property_count: 9
  slug: microsoft-endpoint-configuration-management-sms-applicationdeployment
- name: SMS_Collection
  property_count: 9
  slug: microsoft-endpoint-configuration-management-sms-collection
- name: SMS_Device
  property_count: 10
  slug: microsoft-endpoint-configuration-management-sms-device
- name: SMS_Package
  property_count: 7
  slug: microsoft-endpoint-configuration-management-sms-package
- name: SMS_R_System
  property_count: 11
  slug: microsoft-endpoint-configuration-management-sms-r-system
- name: SMS_Site
  property_count: 7
  slug: microsoft-endpoint-configuration-management-sms-site
- name: SMS_SoftwareUpdate
  property_count: 12
  slug: microsoft-endpoint-configuration-management-sms-softwareupdate
- name: SMS_TaskSequence
  property_count: 6
  slug: microsoft-endpoint-configuration-management-sms-tasksequence
- name: User
  property_count: 9
  slug: microsoft-endpoint-configuration-management-user
- name: UserDeviceAssociation
  property_count: 4
  slug: microsoft-endpoint-configuration-management-userdeviceassociation
json_structures:
- name: Microsoft Endpoint Configuration Management Structure
  property_count: 0
  slug: microsoft-endpoint-configuration-management-structure
jsonld:
- class_count: 0
  name: Microsoft Endpoint Configuration Management Context
  property_count: 7
  slug: microsoft-endpoint-configuration-management-context
layout: provider
modified: '2026-05-19'
name: Microsoft Endpoint Configuration Management
nav: Providers
network: true
overview: 'Microsoft Endpoint Configuration Management publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Collections API, Compliance API, and 17 more. Tagged areas include Compliance, Configuration Management, Device Management, Endpoint Management, and Mobile Device Management.


  The Microsoft Endpoint Configuration Management catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Endpoint Configuration Management''s developer surface includes authentication, developer portal, developer console, documentation, getting-started guide, engineering blog, support, and 34 more developer resources.'
plans:
- name: Microsoft Endpoint Configuration Management Plans Pricing
  plan_count: 3
  slug: microsoft-endpoint-configuration-management-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 3
  name: Microsoft Endpoint Configuration Management Rate Limits
  slug: microsoft-endpoint-configuration-management-rate-limits
rules:
- name: Microsoft Endpoint Configuration Management API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-endpoint-configuration-management-jsonschema-spectral-rules
scopes:
- name: Microsoft Endpoint Configuration Management Scopes
  scope_count: 7
  slug: microsoft-endpoint-configuration-management-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: exemplar
  composite: 67.5
  delta: -4.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 67.3
    developer_ergonomics: 56.5
    discoverability: 66.7
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 71.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-endpoint-configuration-management/refs/heads/main/screenshots/microsoft-endpoint-configuration-management-2026-06-20T185457.png
security:
- kind: authentication
  name: Microsoft Endpoint Configuration Management Authentication
  slug: microsoft-endpoint-configuration-management-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft Endpoint Configuration Management Domain Security
  slug: microsoft-endpoint-configuration-management-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Endpoint Configuration Management Vulnerability Disclosure
  slug: microsoft-endpoint-configuration-management-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-endpoint-configuration-management
tags:
- Compliance
- Configuration Management
- Device Management
- Endpoint Management
- Mobile Device Management
- Patch Management
- Software Deployment
website: https://learn.microsoft.com/en-us/intune/configmgr/
---
