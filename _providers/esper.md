---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: Unified API to query Webclips and Tenant IOS Apps
  name: Esper apps_management_App List API
  slug: esper-apps-management-app-list-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: API to search apple app store for apps
  name: Esper apps_management_Apple App Store API
  slug: esper-apps-management-apple-app-store-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: The apps_management_Esper Apps API from Esper — 1 operation(s) for apps_management_esper apps.
  name: Esper apps_management_Esper Apps API
  slug: esper-apps-management-esper-apps-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs for retrieving OEM config schemas parsed from OEM APKs
  name: Esper apps_management_OEM Config Schema API
  slug: esper-apps-management-oem-config-schema-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs for managing a tenant's preferred country/region list for App Store lookups
  name: Esper apps_management_Preferred Regions API
  slug: esper-apps-management-preferred-regions-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs for managing iOS provisioning profiles for app distribution
  name: Esper apps_management_Provisioning Profiles API
  slug: esper-apps-management-provisioning-profiles-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: API to manage Enterprise iOS apps for a tenant.
  name: Esper apps_management_Tenant Apps API
  slug: esper-apps-management-tenant-apps-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: The apps_management_Tenant Esper Apps API from Esper — 1 operation(s) for apps_management_tenant esper apps.
  name: Esper apps_management_Tenant Esper Apps API
  slug: esper-apps-management-tenant-esper-apps-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs for getting information about VPP apps. Learn more about [VPP apps](https://help.esper.io/hc/en-us/articles/20518326865681-Managing-iOS-Applications).
  name: Esper apps_management_VPP App Management API
  slug: esper-apps-management-vpp-app-management-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs for managing VPP licenses for apps. Learn more about [VPP licenses](https://help.esper.io/hc/en-us/articles/20361103311761-Setting-Up-Apple-MDM-Management).
  name: Esper apps_management_VPP License Management API
  slug: esper-apps-management-vpp-license-management-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: API to manage webclips for a tenant
  name: Esper Apps Management Webclips API
  slug: esper-apps-management-webclips-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to manage background scripts. Background scripts are scripts that can be configured to run continuously or at specified intervals on devices.
  name: Esper blueprints_Background Scripts API
  slug: esper-blueprints-background-scripts-api-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to manage blueprints. Learn more about [blueprints](https://help.esper.io/hc/en-us/articles/19118758564369-Introduction-to-Blueprints).
  name: Esper blueprints_Blueprints API
  slug: esper-blueprints-blueprints-api-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to manage custom actions. Custom actions allow you to define custom scripts and commands that can be executed on Linux devices. Currently, only Linux platform is supported for custom actions.
  name: Esper blueprints_Custom Actions API
  slug: esper-blueprints-custom-actions-api-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to view and manage command requests. Learn more about [commands](https://help.esper.io/hc/en-us/articles/16036992814609-Commonly-Used-APIs#h_01H2GZ8WM86BSQBGXE998QY8SM) or how to [schedule a comm
  name: Esper commands_Command Request API
  slug: esper-commands-command-request-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to view, filter, and manage command requests.
  name: Esper commands_Command Status API
  slug: esper-commands-command-status-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to retrieve information about the device or delete the device.
  name: Esper Device Device API
  slug: esper-device-device-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to get apps installed on iOS devices. Use [Application](https://api.esper.io/tag/Application/) to get apps for Android devices.
  name: Esper device_Device Apps API
  slug: esper-device-device-apps-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to enroll device with Google EMM
  name: Esper device_Device Enrollment in EMM API
  slug: esper-device-device-enrollment-in-emm-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to retrieve information about device's heartbeat which contains the last seen details.
  name: Esper device_Device Heartbeat API
  slug: esper-device-device-heartbeat-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to get information about device operations
  name: Esper Device Device Operations API
  slug: esper-device-deviceoperations-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: API to get Remote Viewer activity for the tenant. Currently supports only Android devices with DPC 8.4 and above along with RemoteViewer 3.x.
  name: Esper device_MultiOS Remote Viewer API
  slug: esper-device-multios-remote-viewer-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to perform ABM provisioning. Learn more about [ABM provisioning](https://help.esper.io/hc/en-us/articles/20361103311761-Setting-Up-Apple-MDM-Management)
  name: Esper device_onboarding_ABM Provisioning API
  slug: esper-device-onboarding-abm-provisioning-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to create and access DEP sync request information. Use DEP sync to sync the information from your Apple Business Manager account to the Esper console.
  name: Esper device_onboarding_DEP Sync Request API
  slug: esper-device-onboarding-dep-sync-request-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to get information about operations
  name: Esper Device Operations API
  slug: esper-device-operations-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to fetch device Blueprint Drift status
  name: Esper drift_Blueprint Drift API
  slug: esper-drift-blueprint-drift-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to list and create converge actions for devices.
  name: Esper Drift Converge API
  slug: esper-drift-converge-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: API for converge command
  name: Esper drift_Converge Command API
  slug: esper-drift-converge-command-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: The esper_cloud_api_Alarms API from Esper — 3 operation(s) for esper_cloud_api_alarms.
  name: Esper Esper Cloud API Alarms API
  slug: esper-esper-cloud-api-alarms-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: The esper_cloud_api_Alerts API from Esper — 2 operation(s) for esper_cloud_api_alerts.
  name: Esper Esper Cloud API Alerts API
  slug: esper-esper-cloud-api-alerts-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs for android device management
  name: Esper Esper Cloud API Android Device API
  slug: esper-esper-cloud-api-androiddevice-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs for application management
  name: Esper Esper Cloud API Application API
  slug: esper-esper-cloud-api-application-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs for application management
  name: Esper esper_cloud_api_Application V1 API
  slug: esper-esper-cloud-api-application-v1-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: This is the API for the former Blueprints service. ⚠️ **Deprecation Notice:** The following APIs will soon be deprecated. Use [Blueprints API](https://api.esper.io/tag/Blueprints-API) instead.
  name: Esper esper_cloud_api_Blueprint (Deprecated) API
  slug: esper-esper-cloud-api-blueprint-deprecated-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: Commands V2.0 provides advanced device commands capabilities like queuing, support for offline devices, dynamic device set for commands and command history. Commands 2.0 is in active development and w
  name: Esper esper_cloud_api_Commands V2 API
  slug: esper-esper-cloud-api-commands-v2-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: The Company Settings API manage the account information set up for your organization. Formerly known as Enterprise Information.
  name: Esper esper_cloud_api_Company Settings API
  slug: esper-esper-cloud-api-company-settings-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to manage files
  name: Esper Esper Cloud API Content API
  slug: esper-esper-cloud-api-content-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: The esper_cloud_api_Daily and Custom Reports API from Esper — 6 operation(s) for esper_cloud_api_daily and custom reports.
  name: Esper esper_cloud_api_Daily and Custom Reports API
  slug: esper-esper-cloud-api-daily-and-custom-reports-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs for device group management
  name: Esper esper_cloud_api_Device Group API
  slug: esper-esper-cloud-api-device-group-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: The esper_cloud_api_Device Telemetry API from Esper — 6 operation(s) for esper_cloud_api_device telemetry.
  name: Esper esper_cloud_api_Device Telemetry API
  slug: esper-esper-cloud-api-device-telemetry-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs for Directory Record management. These APIs are only available to the customers using the new Onboarding experience.
  name: Esper esper_cloud_api_Directory Record API
  slug: esper-esper-cloud-api-directory-record-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to Esper Compliance Policy
  name: Esper esper_cloud_api_Enterprise Policy API
  slug: esper-esper-cloud-api-enterprise-policy-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs for geofence management
  name: Esper Esper Cloud API Geofence API
  slug: esper-esper-cloud-api-geofence-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: The esper_cloud_api_Personal Access Token API from Esper — 2 operation(s) for esper_cloud_api_personal access token.
  name: Esper esper_cloud_api_Personal Access Token API
  slug: esper-esper-cloud-api-personal-access-token-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: The esper_cloud_api_Roles API from Esper — 3 operation(s) for esper_cloud_api_roles.
  name: Esper Esper Cloud API Roles API
  slug: esper-esper-cloud-api-roles-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: The esper_cloud_api_SSO Connections API from Esper — 2 operation(s) for esper_cloud_api_sso connections.
  name: Esper esper_cloud_api_SSO Connections API
  slug: esper-esper-cloud-api-sso-connections-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to manage tile icons. Tile icons allow Templates-based users to apply a icons to devices.
  name: Esper esper_cloud_api_Tile Icon API
  slug: esper-esper-cloud-api-tile-icon-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: ⚠️ **Deprecation Notice:** The following APIs will soon be deprecated. Use the console to manage API keys instead.
  name: Esper esper_cloud_api_Token (Deprecated) API
  slug: esper-esper-cloud-api-token-deprecated-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs for User Management
  name: Esper Esper Cloud API User API
  slug: esper-esper-cloud-api-user-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: ⚠️ **Deprecation Notice:** The following APIs will soon be deprecated. Please transition to the User APIs.
  name: Esper esper_cloud_api_User (Deprecated) API
  slug: esper-esper-cloud-api-user-deprecated-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: The esper_cloud_api_Wallpapers API from Esper — 2 operation(s) for esper_cloud_api_wallpapers.
  name: Esper Esper Cloud API Wallpapers API
  slug: esper-esper-cloud-api-wallpapers-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: The foundation_FoundryBuilds API from Esper — 2 operation(s) for foundation_foundrybuilds.
  name: Esper Foundation Foundry Builds API
  slug: esper-foundation-foundrybuilds-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: The foundation_FoundryDeviceModels API from Esper — 2 operation(s) for foundation_foundrydevicemodels.
  name: Esper Foundation Foundry Device Models API
  slug: esper-foundation-foundrydevicemodels-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: The foundation_FoundryEvents API from Esper — 1 operation(s) for foundation_foundryevents.
  name: Esper Foundation Foundry Events API
  slug: esper-foundation-foundryevents-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: The geofence_Device State API from Esper — 3 operation(s) for geofence_device state.
  name: Esper geofence_Device State API
  slug: esper-geofence-device-state-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: The geofence_Geofences API from Esper — 2 operation(s) for geofence_geofences.
  name: Esper Geofence Geofences API
  slug: esper-geofence-geofences-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to modify Device Groups
  name: Esper pipelines_Device Groups API
  slug: esper-pipelines-device-groups-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to modify Operation List
  name: Esper pipelines_Operation Lists API
  slug: esper-pipelines-operation-lists-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: Operations subsystem
  name: Esper Pipelines Operations API
  slug: esper-pipelines-operations-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to manage Pipeline Runs. Pipeline run status descriptions * PENDING - Pipeline run created. * QUEUED - Pipeline run queued for processing. * PROCESSING - Pipeline run received by scheduler for pr
  name: Esper pipelines_Pipeline Runs API
  slug: esper-pipelines-pipeline-runs-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: Pipelines composition APIs
  name: Esper Pipelines Pipelines API
  slug: esper-pipelines-pipelines-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to manage Stage Runs. Stage run status descriptions * PENDING - Stage run created. * QUEUED - Stage run queued for processing. * PROCESSING - Stage run received by scheduler for processing.(Proce
  name: Esper pipelines_Stage Runs API
  slug: esper-pipelines-stage-runs-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to modify Stage information
  name: Esper Pipelines Stages API
  slug: esper-pipelines-stages-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: System level APIs
  name: Esper Pipelines System API
  slug: esper-pipelines-system-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to modify Target List
  name: Esper pipelines_Target Lists API
  slug: esper-pipelines-target-lists-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to manage Target Runs. Target run status descriptions * PENDING - Target run created. * QUEUED - Target run queued for processing. * PROCESSING - Target run received by scheduler for processing (
  name: Esper pipelines_Target Runs API
  slug: esper-pipelines-target-runs-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: Targets subsystem
  name: Esper Pipelines Targets API
  slug: esper-pipelines-targets-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs for managing reports.<br /> Currently supports [App Reports](https://help.esper.io/hc/en-us/articles/27379366650257-App-Reports).
  name: Esper reports_Reports API
  slug: esper-reports-reports-api-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs for managing APNS certificates. Learn more about [APNS certificates](https://help.esper.io/hc/en-us/articles/20361103311761-Setting-Up-Apple-MDM-Management)
  name: Esper tenant_APNs certificate API
  slug: esper-tenant-apns-certificate-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to create and manage DEP profiles. Learn more about [DEP profiles](https://help.esper.io/hc/en-us/articles/20361103311761-Setting-Up-Apple-MDM-Management)
  name: Esper tenant_DEP Profile API
  slug: esper-tenant-dep-profile-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to create and access DEP tokens. Learn more about [DEP tokens](https://help.esper.io/hc/en-us/articles/20361103311761-Setting-Up-Apple-MDM-Management)
  name: Esper tenant_DEP Tokens API
  slug: esper-tenant-dep-tokens-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to enroll the enterprise in Google EMM.
  name: Esper tenant_Google Enterprise API
  slug: esper-tenant-google-enterprise-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: Unauthenticated discovery endpoint for Apple's MDMServiceConfig spec.
  name: Esper tenant_MDM Service Config API
  slug: esper-tenant-mdm-service-config-api
- baseURL: https://foo-api.esper.cloud/api
  baseurl_source: declared
  description: APIs to create, access, and delete VPP tokens. Learn more about [VPP tokens](https://help.esper.io/hc/en-us/articles/20361103311761-Setting-Up-Apple-MDM-Management).
  name: Esper tenant_VPP Token Management API
  slug: esper-tenant-vpp-token-management-api
artifact_total: 98
asyncapis:
- description: ''
  name: Esper Events Webhooks
  slug: esper-events-webhooks
collections:
- collection_type: open
  name: ESPER API REFERENCE Application API
  slug: open-esper-application-api
- collection_type: open
  name: ESPER API REFERENCE Application Application V1 API
  slug: open-esper-application-v1-api
- collection_type: open
  name: ESPER API REFERENCE Application Commands API
  slug: open-esper-commands-api
- collection_type: open
  name: ESPER API REFERENCE Application Commands V2 API
  slug: open-esper-commands-v2-api
- collection_type: open
  name: ESPER API REFERENCE Application Content API
  slug: open-esper-content-api
- collection_type: open
  name: ESPER API REFERENCE Application Device API
  slug: open-esper-device-api
- collection_type: open
  name: ESPER API REFERENCE Application Device Group API
  slug: open-esper-device-group-api
- collection_type: open
  name: ESPER API REFERENCE Application Enterprise API
  slug: open-esper-enterprise-api
- collection_type: open
  name: ESPER API REFERENCE Application Enterprise Policy API
  slug: open-esper-enterprise-policy-api
- collection_type: open
  name: ESPER API REFERENCE Application Geofence API
  slug: open-esper-geofence-api
- collection_type: open
  name: ESPER API REFERENCE Application Group Commands API
  slug: open-esper-group-commands-api
- collection_type: open
  name: ESPER API REFERENCE Application Subscription API
  slug: open-esper-subscription-api
- collection_type: open
  name: ESPER API REFERENCE Application Token API
  slug: open-esper-token-api
common:
- group: commercial
  href: https://artifacts.apis.io/esper/plans/esper-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/esper-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.esper.io/blog/rss.xml
- group: other
  href: https://artifacts.apis.io/esper/capabilities/esper-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/esper-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/esper/skills/esper-deploy-app-to-group.md
  title: ''
  type: AgentSkill
  url: skills/esper-deploy-app-to-group.md
- group: agent
  href: https://artifacts.apis.io/esper/mcp/esper-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/esper-mcp.yml
- group: other
  href: https://artifacts.apis.io/esper/overlays/esper-manage-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/esper-manage-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/esper/security/esper-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/esper-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.esper.io/
- group: auth
  href: https://artifacts.apis.io/esper/security/esper-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/esper-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://esper.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.esper.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.esper.io/hc/en-us/categories/11385054747153-Developer-Documentation
- group: docs
  title: ''
  type: APIReference
  url: https://api.esper.io/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://help.esper.io/hc/en-us/articles/14199291792145-Getting-Started-with-APIs
- group: operate
  title: ''
  type: Support
  url: https://help.esper.io/
- group: company
  title: ''
  type: Blog
  url: https://www.esper.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/esper-io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.esper.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://esper.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://esper.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.esper.io/privacy-policy
- group: build
  href: https://artifacts.apis.io/esper/packages/esper-packages.yml
  title: ''
  type: Packages
  url: packages/esper-packages.yml
- group: build
  href: https://artifacts.apis.io/esper/packages/esper-packages.yml
  title: ''
  type: SDKs
  url: packages/esper-packages.yml
- group: build
  href: https://artifacts.apis.io/esper/cli/esper-cli.yml
  title: ''
  type: CLI
  url: cli/esper-cli.yml
- group: agent
  href: https://artifacts.apis.io/esper/llms/esper-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/esper-llms.txt
created: '2026-07-17'
description: 'Esper is the DevOps platform for connected devices, providing cloud-based Android (and edge) device management, application deployment, and remote orchestration for dedicated-device fleets. The Esper Manage REST API lets developers programmatically provision, monitor, and control Android-based dedicated devices running the Esper agent: manage devices and device groups, upload and roll out applications and versions, run device and group commands, configure compliance and enterprise policies, set up geofences, manage content, and subscribe to device events via webhooks. APIs are authenticated with a Bearer API key and served per-tenant on a dedicated Esper Cloud environment, with an official Python SDK (esperclient) and CLI.'
finops:
- has_sources: true
  method: derived
  name: Esper Finops
  primary_unit: device
  service_category: ''
  slug: esper-finops
  template: false
image: https://avatars.githubusercontent.com/u/49017159?v=4
layout: provider
modified: '2026-10-06'
name: Esper
nav: Providers
network: true
overview: 'Esper publishes 74 API contracts indexed on the [APIs.io](https://apis.io/) network, including apps_management_App List API, apps_management_Apple App Store API, apps_management_Esper Apps API, and 71 more. Tagged areas include Device Management, Mobile Device Management, Android, DevOps, and IoT.


  The Esper catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Esper''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
plans:
- name: Esper Plans Pricing
  plan_count: 4
  slug: esper-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 111
  extends:
  - spectral:oas
  name: Esper API Rules
  rule_count: 70
  severity_counts:
    error: 42
    hint: 0
    info: 4
    warn: 24
  slug: esper-rules
score:
  band: strong
  composite: 62.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 66.1
    developer_ergonomics: 63.7
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 60.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 84.1
      total: 88
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/esper/esper-2026-07-25T213623.png
security:
- kind: authentication
  name: Esper Authentication
  slug: esper-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Esper Domain Security
  slug: esper-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Esper Trust Center
  slug: esper-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
skill_count: 4
skills:
- name: Upload an app and deploy it to a device group
  slug: esper-deploy-app-to-group
- name: Manage device groups
  slug: esper-manage-device-groups
- name: Find a device and run a command on it
  slug: esper-provision-and-command-device
- name: Subscribe to device events
  slug: esper-subscribe-device-events
slug: esper
tags:
- Device Management
- Mobile Device Management
- Android
- DevOps
- IoT
- Fleet Management
- Enterprise Mobility
- Edge Computing
- Kiosk
website: https://esper.io
---
