---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 2
  name: Microsoft Intune Agentic Access
  operation_count: 22
  slug: microsoft-intune-agentic-access
  summary_line: 22 operations · 16 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The Intune Data Warehouse API provides access to your Intune data in a machine-readable format for use in your favorite analytics tool. You can use the API to generate reports that provide insight int
  name: Intune Data Warehouse API
  slug: intune-data-warehouse-api
- description: The Microsoft Graph Device Management API enables programmatic management of devices enrolled in Intune, including listing managed devices, performing remote actions such as wipe and retire, and retri
  name: Intune Device Management API
  slug: intune-device-management-api
- description: The Microsoft Graph Device Configuration API allows you to define and deploy device configuration policies across enrolled devices, including operating system platform and versioning, domain membershi
  name: Intune Device Configuration API
  slug: intune-device-configuration-api
- description: The Microsoft Graph Device Compliance API enables you to define and enforce device compliance policies, such as password complexity, encryption, and threat protection levels, and retrieve compliance s
  name: Intune Device Compliance API
  slug: intune-device-compliance-api
- description: The Microsoft Graph Device Enrollment API enables you to enroll organization-owned or corporate-owned devices for management with Intune, supporting various enrollment methods depending on device type
  name: Intune Device Enrollment API
  slug: intune-device-enrollment-api
- description: The Microsoft Graph Mobile App Management (MAM) API enables you to manage app protection policies, deploy apps to devices, configure app settings, and manage app usage policies to protect organization
  name: Intune Mobile App Management API
  slug: intune-mobile-app-management-api
- description: The Intune Reports Export API enables you to export Intune reporting data using Microsoft Graph API export jobs. You can create export jobs to generate reports that provide insight into device complia
  name: Intune Reports Export API
  slug: intune-reports-export-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations for managing device compliance policies. Compliance policies define rules and settings that a device must comply with to be considered compliant.
  name: Microsoft Intune Device Compliance Policies API
  slug: microsoft-intune-device-compliance-policies-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations for managing device configuration profiles. Configuration profiles define settings that are applied to enrolled devices.
  name: Microsoft Intune Device Configurations API
  slug: microsoft-intune-device-configurations-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations for managing devices enrolled in Intune. Includes listing, retrieving, creating, updating, and deleting managed device records.
  name: Microsoft Intune Managed Devices API
  slug: microsoft-intune-managed-devices-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.androidManagedAppProtection API from Microsoft Intune — 10 operation(s) for deviceappmanagement.androidmanagedappprotection.
  name: Microsoft Intune Device App Management.android Managed App Protection API
  slug: microsoft-intune-deviceappmanagement-androidmanagedappprotection-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.defaultManagedAppProtection API from Microsoft Intune — 7 operation(s) for deviceappmanagement.defaultmanagedappprotection.
  name: Microsoft Intune Device App Management.default Managed App Protection API
  slug: microsoft-intune-deviceappmanagement-defaultmanagedappprotection-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.deviceAppManagement.Actions API from Microsoft Intune — 1 operation(s) for deviceappmanagement.deviceappmanagement.actions.
  name: Microsoft Intune Device App Management.device App Management.Actions API
  slug: microsoft-intune-deviceappmanagement-deviceappmanagement-actions-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.deviceAppManagement API from Microsoft Intune — 1 operation(s) for deviceappmanagement.deviceappmanagement.
  name: Microsoft Intune Device App Management.device App Management API
  slug: microsoft-intune-deviceappmanagement-deviceappmanagement-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.iosManagedAppProtection API from Microsoft Intune — 10 operation(s) for deviceappmanagement.iosmanagedappprotection.
  name: Microsoft Intune Device App Management.ios Managed App Protection API
  slug: microsoft-intune-deviceappmanagement-iosmanagedappprotection-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.managedAppPolicy API from Microsoft Intune — 4 operation(s) for deviceappmanagement.managedapppolicy.
  name: Microsoft Intune Device App Management.managed App Policy API
  slug: microsoft-intune-deviceappmanagement-managedapppolicy-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.managedAppRegistration API from Microsoft Intune — 15 operation(s) for deviceappmanagement.managedappregistration.
  name: Microsoft Intune Device App Management.managed App Registration API
  slug: microsoft-intune-deviceappmanagement-managedappregistration-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.managedAppStatus API from Microsoft Intune — 3 operation(s) for deviceappmanagement.managedappstatus.
  name: Microsoft Intune Device App Management.managed App Status API
  slug: microsoft-intune-deviceappmanagement-managedappstatus-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.managedDeviceMobileAppConfiguration API from Microsoft Intune — 15 operation(s) for deviceappmanagement.manageddevicemobileappconfiguration.
  name: Microsoft Intune Device App Management.managed Device Mobile App Configuration API
  slug: microsoft-intune-deviceappmanagement-manageddevicemobileappconfiguration-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.managedEBook API from Microsoft Intune — 17 operation(s) for deviceappmanagement.managedebook.
  name: Microsoft Intune Device App Management.managed E Book API
  slug: microsoft-intune-deviceappmanagement-managedebook-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.mdmWindowsInformationProtectionPolicy API from Microsoft Intune — 12 operation(s) for deviceappmanagement.mdmwindowsinformationprotectionpolicy.
  name: Microsoft Intune Device App Management.mdm Windows Information Protection Policy API
  slug: microsoft-intune-deviceappmanagement-mdmwindowsinformationprotectionpolicy-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.mobileApp API from Microsoft Intune — 278 operation(s) for deviceappmanagement.mobileapp.
  name: Microsoft Intune Device App Management.mobile App API
  slug: microsoft-intune-deviceappmanagement-mobileapp-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.mobileAppCategory API from Microsoft Intune — 3 operation(s) for deviceappmanagement.mobileappcategory.
  name: Microsoft Intune Device App Management.mobile App Category API
  slug: microsoft-intune-deviceappmanagement-mobileappcategory-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.mobileAppRelationship API from Microsoft Intune — 3 operation(s) for deviceappmanagement.mobileapprelationship.
  name: Microsoft Intune Device App Management.mobile App Relationship API
  slug: microsoft-intune-deviceappmanagement-mobileapprelationship-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.targetedManagedAppConfiguration API from Microsoft Intune — 12 operation(s) for deviceappmanagement.targetedmanagedappconfiguration.
  name: Microsoft Intune Device App Management.targeted Managed App Configuration API
  slug: microsoft-intune-deviceappmanagement-targetedmanagedappconfiguration-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.vppToken API from Microsoft Intune — 4 operation(s) for deviceappmanagement.vpptoken.
  name: Microsoft Intune Device App Management.vpp Token API
  slug: microsoft-intune-deviceappmanagement-vpptoken-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceAppManagement.windowsInformationProtectionPolicy API from Microsoft Intune — 12 operation(s) for deviceappmanagement.windowsinformationprotectionpolicy.
  name: Microsoft Intune Device App Management.windows Information Protection Policy API
  slug: microsoft-intune-deviceappmanagement-windowsinformationprotectionpolicy-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.applePushNotificationCertificate API from Microsoft Intune — 2 operation(s) for devicemanagement.applepushnotificationcertificate.
  name: Microsoft Intune Device Management.apple Push Notification Certificate API
  slug: microsoft-intune-devicemanagement-applepushnotificationcertificate-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.auditEvent API from Microsoft Intune — 5 operation(s) for devicemanagement.auditevent.
  name: Microsoft Intune Device Management.audit Event API
  slug: microsoft-intune-devicemanagement-auditevent-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.complianceManagementPartner API from Microsoft Intune — 3 operation(s) for devicemanagement.compliancemanagementpartner.
  name: Microsoft Intune Device Management.compliance Management Partner API
  slug: microsoft-intune-devicemanagement-compliancemanagementpartner-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.detectedApp API from Microsoft Intune — 6 operation(s) for devicemanagement.detectedapp.
  name: Microsoft Intune Device Management.detected App API
  slug: microsoft-intune-devicemanagement-detectedapp-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.deviceAndAppManagementRoleAssignment API from Microsoft Intune — 4 operation(s) for devicemanagement.deviceandappmanagementroleassignment.
  name: Microsoft Intune Device Management.device And App Management Role Assignment API
  slug: microsoft-intune-devicemanagement-deviceandappmanagementroleassignment-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.deviceCategory API from Microsoft Intune — 3 operation(s) for devicemanagement.devicecategory.
  name: Microsoft Intune Device Management.device Category API
  slug: microsoft-intune-devicemanagement-devicecategory-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.deviceCompliancePolicy API from Microsoft Intune — 25 operation(s) for devicemanagement.devicecompliancepolicy.
  name: Microsoft Intune Device Management.device Compliance Policy API
  slug: microsoft-intune-devicemanagement-devicecompliancepolicy-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.deviceCompliancePolicyDeviceStateSummary API from Microsoft Intune — 1 operation(s) for devicemanagement.devicecompliancepolicydevicestatesummary.
  name: Microsoft Intune Device Management.device Compliance Policy Device State Summary API
  slug: microsoft-intune-devicemanagement-devicecompliancepolicydevicestatesummary-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.deviceCompliancePolicySettingStateSummary API from Microsoft Intune — 6 operation(s) for devicemanagement.devicecompliancepolicysettingstatesummary.
  name: Microsoft Intune Device Management.device Compliance Policy Setting State Summary API
  slug: microsoft-intune-devicemanagement-devicecompliancepolicysettingstatesummary-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.deviceConfiguration API from Microsoft Intune — 19 operation(s) for devicemanagement.deviceconfiguration.
  name: Microsoft Intune Device Management.device Configuration API
  slug: microsoft-intune-devicemanagement-deviceconfiguration-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.deviceConfigurationDeviceStateSummary API from Microsoft Intune — 1 operation(s) for devicemanagement.deviceconfigurationdevicestatesummary.
  name: Microsoft Intune Device Management.device Configuration Device State Summary API
  slug: microsoft-intune-devicemanagement-deviceconfigurationdevicestatesummary-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.deviceEnrollmentConfiguration API from Microsoft Intune — 8 operation(s) for devicemanagement.deviceenrollmentconfiguration.
  name: Microsoft Intune Device Management.device Enrollment Configuration API
  slug: microsoft-intune-devicemanagement-deviceenrollmentconfiguration-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.deviceManagement API from Microsoft Intune — 1 operation(s) for devicemanagement.devicemanagement.
  name: Microsoft Intune Device Management.device Management API
  slug: microsoft-intune-devicemanagement-devicemanagement-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.deviceManagement.Functions API from Microsoft Intune — 3 operation(s) for devicemanagement.devicemanagement.functions.
  name: Microsoft Intune Device Management.device Management.Functions API
  slug: microsoft-intune-devicemanagement-devicemanagement-functions-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.deviceManagementExchangeConnector API from Microsoft Intune — 4 operation(s) for devicemanagement.devicemanagementexchangeconnector.
  name: Microsoft Intune Device Management.device Management Exchange Connector API
  slug: microsoft-intune-devicemanagement-devicemanagementexchangeconnector-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.deviceManagementPartner API from Microsoft Intune — 4 operation(s) for devicemanagement.devicemanagementpartner.
  name: Microsoft Intune Device Management.device Management Partner API
  slug: microsoft-intune-devicemanagement-devicemanagementpartner-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.deviceManagementReports API from Microsoft Intune — 23 operation(s) for devicemanagement.devicemanagementreports.
  name: Microsoft Intune Device Management.device Management Reports API
  slug: microsoft-intune-devicemanagement-devicemanagementreports-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.deviceManagementTroubleshootingEvent API from Microsoft Intune — 3 operation(s) for devicemanagement.devicemanagementtroubleshootingevent.
  name: Microsoft Intune Device Management.device Management Troubleshooting Event API
  slug: microsoft-intune-devicemanagement-devicemanagementtroubleshootingevent-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.importedWindowsAutopilotDeviceIdentity API from Microsoft Intune — 4 operation(s) for devicemanagement.importedwindowsautopilotdeviceidentity.
  name: Microsoft Intune Device Management.imported Windows Autopilot Device Identity API
  slug: microsoft-intune-devicemanagement-importedwindowsautopilotdeviceidentity-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.iosUpdateDeviceStatus API from Microsoft Intune — 3 operation(s) for devicemanagement.iosupdatedevicestatus.
  name: Microsoft Intune Device Management.ios Update Device Status API
  slug: microsoft-intune-devicemanagement-iosupdatedevicestatus-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.managedDevice API from Microsoft Intune — 38 operation(s) for devicemanagement.manageddevice.
  name: Microsoft Intune Device Management.managed Device API
  slug: microsoft-intune-devicemanagement-manageddevice-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.managedDeviceOverview API from Microsoft Intune — 1 operation(s) for devicemanagement.manageddeviceoverview.
  name: Microsoft Intune Device Management.managed Device Overview API
  slug: microsoft-intune-devicemanagement-manageddeviceoverview-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.mobileAppTroubleshootingEvent API from Microsoft Intune — 7 operation(s) for devicemanagement.mobileapptroubleshootingevent.
  name: Microsoft Intune Device Management.mobile App Troubleshooting Event API
  slug: microsoft-intune-devicemanagement-mobileapptroubleshootingevent-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.mobileThreatDefenseConnector API from Microsoft Intune — 3 operation(s) for devicemanagement.mobilethreatdefenseconnector.
  name: Microsoft Intune Device Management.mobile Threat Defense Connector API
  slug: microsoft-intune-devicemanagement-mobilethreatdefenseconnector-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.notificationMessageTemplate API from Microsoft Intune — 7 operation(s) for devicemanagement.notificationmessagetemplate.
  name: Microsoft Intune Device Management.notification Message Template API
  slug: microsoft-intune-devicemanagement-notificationmessagetemplate-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.onPremisesConditionalAccessSettings API from Microsoft Intune — 1 operation(s) for devicemanagement.onpremisesconditionalaccesssettings.
  name: Microsoft Intune Device Management.on Premises Conditional Access Settings API
  slug: microsoft-intune-devicemanagement-onpremisesconditionalaccesssettings-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.remoteAssistancePartner API from Microsoft Intune — 5 operation(s) for devicemanagement.remoteassistancepartner.
  name: Microsoft Intune Device Management.remote Assistance Partner API
  slug: microsoft-intune-devicemanagement-remoteassistancepartner-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.resourceOperation API from Microsoft Intune — 3 operation(s) for devicemanagement.resourceoperation.
  name: Microsoft Intune Device Management.resource Operation API
  slug: microsoft-intune-devicemanagement-resourceoperation-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.roleDefinition API from Microsoft Intune — 7 operation(s) for devicemanagement.roledefinition.
  name: Microsoft Intune Device Management.role Definition API
  slug: microsoft-intune-devicemanagement-roledefinition-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.softwareUpdateStatusSummary API from Microsoft Intune — 1 operation(s) for devicemanagement.softwareupdatestatussummary.
  name: Microsoft Intune Device Management.software Update Status Summary API
  slug: microsoft-intune-devicemanagement-softwareupdatestatussummary-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.termsAndConditions API from Microsoft Intune — 10 operation(s) for devicemanagement.termsandconditions.
  name: Microsoft Intune Device Management.terms And Conditions API
  slug: microsoft-intune-devicemanagement-termsandconditions-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsAppHealthApplicationPerformance API from Microsoft Intune — 3 operation(s) for devicemanagement.userexperienceanalyticsapphealthapplicationperformance.
  name: Microsoft Intune Device Management.user Experience Analytics App Health Application Performance API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsapphealthapplicationperformance-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails API from Microsoft Intune — 3 operation(s) for devicemanagement.userexperienceanalyticsapphealthappperformancebya
  name: Microsoft Intune Device Management.user Experience Analytics App Health App Performance By App Version Details API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsapphealthappperformancebyappversiondetails-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId API from Microsoft Intune — 3 operation(s) for devicemanagement.userexperienceanalyticsapphealthappperformanceby
  name: Microsoft Intune Device Management.user Experience Analytics App Health App Performance By App Version Device ID API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsapphealthappperformancebyappversiondeviceid-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsAppHealthAppPerformanceByOSVersion API from Microsoft Intune — 3 operation(s) for devicemanagement.userexperienceanalyticsapphealthappperformancebyosversion
  name: Microsoft Intune Device Management.user Experience Analytics App Health App Performance By OS Version API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsapphealthappperformancebyosversion-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsAppHealthDeviceModelPerformance API from Microsoft Intune — 3 operation(s) for devicemanagement.userexperienceanalyticsapphealthdevicemodelperformance.
  name: Microsoft Intune Device Management.user Experience Analytics App Health Device Model Performance API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsapphealthdevicemodelperformance-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsAppHealthDevicePerformance API from Microsoft Intune — 3 operation(s) for devicemanagement.userexperienceanalyticsapphealthdeviceperformance.
  name: Microsoft Intune Device Management.user Experience Analytics App Health Device Performance API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsapphealthdeviceperformance-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsAppHealthDevicePerformanceDetails API from Microsoft Intune — 3 operation(s) for devicemanagement.userexperienceanalyticsapphealthdeviceperformancedetails.
  name: Microsoft Intune Device Management.user Experience Analytics App Health Device Performance Details API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsapphealthdeviceperformancedetails-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsAppHealthOSVersionPerformance API from Microsoft Intune — 3 operation(s) for devicemanagement.userexperienceanalyticsapphealthosversionperformance.
  name: Microsoft Intune Device Management.user Experience Analytics App Health OS Version Performance API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsapphealthosversionperformance-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsBaseline API from Microsoft Intune — 10 operation(s) for devicemanagement.userexperienceanalyticsbaseline.
  name: Microsoft Intune Device Management.user Experience Analytics Baseline API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsbaseline-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsCategory API from Microsoft Intune — 10 operation(s) for devicemanagement.userexperienceanalyticscategory.
  name: Microsoft Intune Device Management.user Experience Analytics Category API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticscategory-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsDevicePerformance API from Microsoft Intune — 4 operation(s) for devicemanagement.userexperienceanalyticsdeviceperformance.
  name: Microsoft Intune Device Management.user Experience Analytics Device Performance API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsdeviceperformance-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsDeviceScores API from Microsoft Intune — 3 operation(s) for devicemanagement.userexperienceanalyticsdevicescores.
  name: Microsoft Intune Device Management.user Experience Analytics Device Scores API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsdevicescores-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsDeviceStartupHistory API from Microsoft Intune — 3 operation(s) for devicemanagement.userexperienceanalyticsdevicestartuphistory.
  name: Microsoft Intune Device Management.user Experience Analytics Device Startup History API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsdevicestartuphistory-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsDeviceStartupProcess API from Microsoft Intune — 3 operation(s) for devicemanagement.userexperienceanalyticsdevicestartupprocess.
  name: Microsoft Intune Device Management.user Experience Analytics Device Startup Process API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsdevicestartupprocess-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsDeviceStartupProcessPerformance API from Microsoft Intune — 3 operation(s) for devicemanagement.userexperienceanalyticsdevicestartupprocessperformance.
  name: Microsoft Intune Device Management.user Experience Analytics Device Startup Process Performance API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsdevicestartupprocessperformance-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsMetricHistory API from Microsoft Intune — 3 operation(s) for devicemanagement.userexperienceanalyticsmetrichistory.
  name: Microsoft Intune Device Management.user Experience Analytics Metric History API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsmetrichistory-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsModelScores API from Microsoft Intune — 3 operation(s) for devicemanagement.userexperienceanalyticsmodelscores.
  name: Microsoft Intune Device Management.user Experience Analytics Model Scores API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsmodelscores-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsOverview API from Microsoft Intune — 1 operation(s) for devicemanagement.userexperienceanalyticsoverview.
  name: Microsoft Intune Device Management.user Experience Analytics Overview API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsoverview-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsScoreHistory API from Microsoft Intune — 3 operation(s) for devicemanagement.userexperienceanalyticsscorehistory.
  name: Microsoft Intune Device Management.user Experience Analytics Score History API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsscorehistory-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric API from Microsoft Intune — 1 operation(s) for devicemanagement.userexperienceanalyticsworkfromanywherehardwarereadi
  name: Microsoft Intune Device Management.user Experience Analytics Work From Anywhere Hardware Readiness Metric API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsworkfromanywherehardwarereadinessmetric-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsWorkFromAnywhereMetric API from Microsoft Intune — 6 operation(s) for devicemanagement.userexperienceanalyticsworkfromanywheremetric.
  name: Microsoft Intune Device Management.user Experience Analytics Work From Anywhere Metric API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsworkfromanywheremetric-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.userExperienceAnalyticsWorkFromAnywhereModelPerformance API from Microsoft Intune — 3 operation(s) for devicemanagement.userexperienceanalyticsworkfromanywheremodelperformance.
  name: Microsoft Intune Device Management.user Experience Analytics Work From Anywhere Model Performance API
  slug: microsoft-intune-devicemanagement-userexperienceanalyticsworkfromanywheremodelperformance-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.virtualEndpoint API from Microsoft Intune — 54 operation(s) for devicemanagement.virtualendpoint.
  name: Microsoft Intune Device Management.virtual Endpoint API
  slug: microsoft-intune-devicemanagement-virtualendpoint-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.windowsAutopilotDeviceIdentity API from Microsoft Intune — 6 operation(s) for devicemanagement.windowsautopilotdeviceidentity.
  name: Microsoft Intune Device Management.windows Autopilot Device Identity API
  slug: microsoft-intune-devicemanagement-windowsautopilotdeviceidentity-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.windowsInformationProtectionAppLearningSummary API from Microsoft Intune — 3 operation(s) for devicemanagement.windowsinformationprotectionapplearningsummary.
  name: Microsoft Intune Device Management.windows Information Protection App Learning Summary API
  slug: microsoft-intune-devicemanagement-windowsinformationprotectionapplearningsummary-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.windowsInformationProtectionNetworkLearningSummary API from Microsoft Intune — 3 operation(s) for devicemanagement.windowsinformationprotectionnetworklearningsummary.
  name: Microsoft Intune Device Management.windows Information Protection Network Learning Summary API
  slug: microsoft-intune-devicemanagement-windowsinformationprotectionnetworklearningsummary-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The deviceManagement.windowsMalwareInformation API from Microsoft Intune — 6 operation(s) for devicemanagement.windowsmalwareinformation.
  name: Microsoft Intune Device Management.windows Malware Information API
  slug: microsoft-intune-devicemanagement-windowsmalwareinformation-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Remote actions that can be performed on managed devices, including retire, wipe, sync, remote lock, reset passcode, and reboot.
  name: Microsoft Intune Remote Actions API
  slug: microsoft-intune-remote-actions-api
artifact_total: 132
collections:
- collection_type: open
  name: Microsoft Intune Graph Device Compliance Policies API
  slug: open-microsoft-intune-device-compliance-policies-api
- collection_type: open
  name: Microsoft Intune Graph Device Compliance Policies Device Configurations API
  slug: open-microsoft-intune-device-configurations-api
- collection_type: open
  name: Microsoft Intune Graph Device Compliance Policies Managed Devices API
  slug: open-microsoft-intune-managed-devices-api
- collection_type: open
  name: Microsoft Intune Graph Device Compliance Policies Remote Actions API
  slug: open-microsoft-intune-remote-actions-api
- collection_type: open
  name: Microsoft Intune Graph API
  slug: open-microsoft-intune
common:
- group: auth
  href: https://artifacts.apis.io/microsoft-intune/well-known/microsoft-intune-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-intune-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-intune/well-known/microsoft-intune-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-intune-well-known.yml
- group: design
  href: https://artifacts.apis.io/microsoft-intune/rules/microsoft-intune-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-intune-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-intune/rules/microsoft-intune-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-intune-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-intune/json-ld/microsoft-intune-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-intune-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-intune/vocabulary/microsoft-intune-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-intune-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-intune/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-intune/data-model/microsoft-intune-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-intune-data-model.yml
- group: design
  href: https://artifacts.apis.io/microsoft-intune/conventions/microsoft-intune-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-intune-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/graph/versioning-and-support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: design
  href: https://artifacts.apis.io/microsoft-intune/lifecycle/microsoft-intune-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-intune-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-intune/errors/microsoft-intune-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-intune-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-intune/conformance/microsoft-intune-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-intune-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-intune/llms/microsoft-intune-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-intune-llms.txt
- group: build
  href: https://artifacts.apis.io/microsoft-intune/mcp/microsoft-intune-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-intune-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-intune/mcp/microsoft-intune-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-intune-mcp.yml
- group: other
  href: https://artifacts.apis.io/microsoft-intune/hosts/microsoft-intune-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-intune-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-intune/vendors/microsoft-intune-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-intune-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-intune/packages/microsoft-intune-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-intune-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-intune/packages/microsoft-intune-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-intune-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/en-us
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: auth
  href: https://artifacts.apis.io/microsoft-intune/security/microsoft-intune-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-intune-trust-center.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-intune/plans/microsoft-intune-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-intune-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-intune/rate-limits/microsoft-intune-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-intune-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-intune/finops/microsoft-intune-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-intune-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://artifacts.apis.io/microsoft-intune/agentic-access/microsoft-intune-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-intune-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-intune/security/microsoft-intune-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-intune-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-intune/security/microsoft-intune-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-intune-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-intune/authentication/microsoft-intune-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-intune-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-intune/scopes/microsoft-intune-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-intune-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/microsoft-intune-product
- group: start
  title: ''
  type: X-portal
  url: https://endpoint.microsoft.com/
- group: company
  title: ''
  type: X-blog
  url: https://techcommunity.microsoft.com/t5/microsoft-intune-blog/bg-p/MicrosoftEndpointManagerBlog
- group: learn
  title: ''
  type: X-learning
  url: https://docs.microsoft.com/en-us/learn/browse/?products=m365%2Cmem
- group: commercial
  title: ''
  type: X-privacy
  url: https://privacy.microsoft.com/
- group: commercial
  title: ''
  type: X-terms-of-service
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: operate
  title: ''
  type: X-status
  url: https://status.azure.com/
- group: build
  title: ''
  type: X-github
  url: https://github.com/microsoftgraph
- group: build
  title: ''
  type: X-github-samples
  url: https://github.com/microsoft/mggraph-intune-samples
- group: docs
  title: ''
  type: X-developer-documentation
  url: https://learn.microsoft.com/en-us/intune/intune-service/developer/intune-graph-apis
- group: build
  title: ''
  type: X-sdk
  url: https://learn.microsoft.com/en-us/intune/intune-service/developer/app-sdk
- group: start
  title: ''
  type: X-sdk-getting-started
  url: https://learn.microsoft.com/en-us/intune/intune-service/developer/app-sdk-get-started
- group: build
  title: ''
  type: X-app-wrapping-tool
  url: https://learn.microsoft.com/en-us/intune/intune-service/developer/apps-prepare-mobile-application-management
- group: operate
  title: ''
  type: X-community
  url: https://techcommunity.microsoft.com/t5/microsoft-intune/ct-p/MicrosoftIntune
- group: operate
  title: ''
  type: X-support
  url: https://learn.microsoft.com/en-us/mem/get-support
- group: company
  title: ''
  type: X-twitter
  url: https://twitter.com/MSIntune
- group: other
  title: ''
  type: X-whatsnew
  url: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/in-development
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/security/blog/product/microsoft-intune/feed/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph/intune-concept-overview
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/graph/api/resources/intune-graph-overview?view=graph-rest-1.0
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/graph
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/security/microsoft-intune-pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoftgraph
- group: commercial
  title: ''
  type: TermsOfService
  url: https://learn.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/microsoftgraph/workspace/microsoft-graph/overview
created: '2024'
description: Microsoft Intune is a cloud-based service that focuses on mobile device management (MDM) and mobile application management (MAM). It helps organizations control how their devices are used, including mobile phones, tablets, and laptops, and enables management of apps on those devices.
finops:
- has_sources: true
  method: generated
  name: Microsoft Intune Finops
  primary_unit: ''
  service_category: Endpoint Management
  slug: microsoft-intune-finops
  template: false
image: https://docs.microsoft.com/en-us/mem/intune/fundamentals/media/what-is-intune/intune-logo.png
json_schemas:
- name: configurationManagerClientEnabledFeatures
  property_count: 7
  slug: microsoft-intune-configurationmanagerclientenabledfeatures
- name: deviceCompliancePolicyAssignment
  property_count: 3
  slug: microsoft-intune-device-compliance-policy-assignment
- name: deviceCompliancePolicy
  property_count: 7
  slug: microsoft-intune-device-compliance-policy
- name: deviceComplianceScheduledActionForRule
  property_count: 4
  slug: microsoft-intune-device-compliance-scheduled-action-for-rule
- name: deviceConfigurationAssignment
  property_count: 3
  slug: microsoft-intune-device-configuration-assignment
- name: deviceConfiguration
  property_count: 7
  slug: microsoft-intune-device-configuration
- name: deviceActionResult
  property_count: 5
  slug: microsoft-intune-deviceactionresult
- name: deviceAndAppManagementAssignmentTarget
  property_count: 1
  slug: microsoft-intune-deviceandappmanagementassignmenttarget
- name: deviceComplianceActionItem
  property_count: 6
  slug: microsoft-intune-devicecomplianceactionitem
- name: deviceCompliancePolicy
  property_count: 7
  slug: microsoft-intune-devicecompliancepolicy
- name: deviceCompliancePolicyAssignment
  property_count: 3
  slug: microsoft-intune-devicecompliancepolicyassignment
- name: deviceComplianceScheduledActionForRule
  property_count: 4
  slug: microsoft-intune-devicecompliancescheduledactionforrule
- name: deviceConfiguration
  property_count: 7
  slug: microsoft-intune-deviceconfiguration
- name: deviceConfigurationAssignment
  property_count: 3
  slug: microsoft-intune-deviceconfigurationassignment
- name: deviceHealthAttestationState
  property_count: 18
  slug: microsoft-intune-devicehealthattestationstate
- name: Microsoft Intune Managed Device
  property_count: 56
  slug: microsoft-intune-managed-device
- name: managedDevice
  property_count: 55
  slug: microsoft-intune-manageddevice
- name: microsoft.graph.cloudPcOnPremisesConnection
  property_count: 21
  slug: microsoft-intune-microsoft-graph-cloud-pc-on-premises-connection
- name: microsoft.graph.deviceManagement
  property_count: 66
  slug: microsoft-intune-microsoft-graph-device-management
- name: microsoft.graph.managedDevice
  property_count: 63
  slug: microsoft-intune-microsoft-graph-managed-device
- name: microsoft.graph.userExperienceAnalyticsWorkFromAnywhereDevice
  property_count: 36
  slug: microsoft-intune-microsoft-graph-user-experience-analytics-work-from-anywhere-device
- name: microsoft.graph.user
  property_count: 139
  slug: microsoft-intune-microsoft-graph-user
- name: microsoft.graph.windowsProtectionState
  property_count: 24
  slug: microsoft-intune-microsoft-graph-windows-protection-state
- name: odataError
  property_count: 1
  slug: microsoft-intune-odataerror
json_structures:
- name: Microsoft Intune Structure
  property_count: 0
  slug: microsoft-intune-structure
jsonld:
- class_count: 0
  name: Microsoft Intune Context
  property_count: 5
  slug: microsoft-intune-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.svc.cloud.microsoft requiring OAuth; 3 tools listed.
  name: Microsoft MCP Server for Enterprise
  slug: microsoft-mcp-server-for-enterprise
modified: '2026-11-04'
name: Microsoft Intune
nav: Providers
network: true
overview: 'Microsoft Intune publishes 86 API contracts indexed on the [APIs.io](https://apis.io/) network, including Device Compliance Policies API, Device Configurations API, Managed Devices API, and 83 more. Tagged areas include App Protection, Microsoft Azure, Compliance, Device Configuration, and Endpoint Management.


  The Microsoft Intune catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Microsoft Intune''s developer surface includes support, changelog, getting-started guide, authentication, engineering blog, documentation, API reference, and 56 more developer resources.'
plans:
- name: Microsoft Intune Plans Pricing
  plan_count: 10
  slug: microsoft-intune-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Microsoft Intune Rate Limits
  slug: microsoft-intune-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Microsoft Intune — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-intune-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Microsoft Intune API Rules
  rule_count: 65
  severity_counts:
    error: 49
    hint: 0
    info: 10
    warn: 6
  slug: microsoft-intune-rules
scopes:
- name: Microsoft Intune Scopes
  scope_count: 4
  slug: microsoft-intune-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: exemplar
  composite: 69.5
  coverage:
    artifact_dirs: 34
    catalog_earned: 80.8
    catalog_earned_first_party: 24.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 36.9
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 57.9
    developer_ergonomics: 70.8
    discoverability: 73.3
    operational_transparency: 86.8
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 79
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-intune/microsoft-intune-2026-06-20T185505.png
security:
- kind: authentication
  name: Microsoft Intune Authentication
  slug: microsoft-intune-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Intune Domain Security
  slug: microsoft-intune-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Intune Vulnerability Disclosure
  slug: microsoft-intune-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Intune Trust Center
  slug: microsoft-intune-trust-center
  summary_line: GDPR
skill_count: 3
skills:
- name: microsoft-intune-app-deployment
  slug: microsoft-intune-app-deployment
- name: microsoft-intune-compliance-policy-rollout
  slug: microsoft-intune-compliance-policy-rollout
- name: microsoft-intune-device-offboarding
  slug: microsoft-intune-device-offboarding
slug: microsoft-intune
tags:
- App Protection
- Microsoft Azure
- Compliance
- Device Configuration
- Endpoint Management
- Enrollment
- MAM
- MDM
- Microsoft Graph
- Mobile Application Management
- Mobile Device Management
- Security
website: https://www.microsoft.com/
---
