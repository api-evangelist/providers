---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://www.openpath.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.avigilon.com/access-control — a different registrable domain (openpath.com -> avigilon.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 295
  human_in_the_loop: 4
  name: Openpath Agentic Access
  operation_count: 546
  slug: openpath-agentic-access
  summary_line: 546 operations · 295 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Authentication and Login
  name: Openpath Auth API
  slug: openpath-auth-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The billableFeatures API from Openpath — 1 operation(s) for billablefeatures.
  name: Openpath Billable Features API
  slug: openpath-billablefeatures-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Identities and MFA
  name: Openpath Identities API
  slug: openpath-identities-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: ACU Models
  name: Openpath Orgs/acu Models API
  slug: openpath-orgs-acumodels-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/acuPorts API from Openpath — 1 operation(s) for orgs/acuports.
  name: Openpath Orgs/acu Ports API
  slug: openpath-orgs-acuports-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: ACU Port Types
  name: Openpath Orgs/acu Port Types API
  slug: openpath-orgs-acuporttypes-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: ACUs
  name: Openpath Orgs/acus API
  slug: openpath-orgs-acus-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/alarmActions API from Openpath — 2 operation(s) for orgs/alarmactions.
  name: Openpath Orgs/alarm Actions API
  slug: openpath-orgs-alarmactions-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/alarmConfigurations API from Openpath — 5 operation(s) for orgs/alarmconfigurations.
  name: Openpath Orgs/alarm Configurations API
  slug: openpath-orgs-alarmconfigurations-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/alarmSeverities API from Openpath — 2 operation(s) for orgs/alarmseverities.
  name: Openpath Orgs/alarm Severities API
  slug: openpath-orgs-alarmseverities-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/alarmsExt API from Openpath — 2 operation(s) for orgs/alarmsext.
  name: Openpath Orgs/alarms Ext API
  slug: openpath-orgs-alarmsext-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/alarmStatuses API from Openpath — 2 operation(s) for orgs/alarmstatuses.
  name: Openpath Orgs/alarm Statuses API
  slug: openpath-orgs-alarmstatuses-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/authCerts API from Openpath — 2 operation(s) for orgs/authcerts.
  name: Openpath Orgs/auth Certs API
  slug: openpath-orgs-authcerts-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/badgeConfigs API from Openpath — 2 operation(s) for orgs/badgeconfigs.
  name: Openpath Orgs/badge Configs API
  slug: openpath-orgs-badgeconfigs-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/cardFormats API from Openpath — 2 operation(s) for orgs/cardformats.
  name: Openpath Orgs/card Formats API
  slug: openpath-orgs-cardformats-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/cobalt API from Openpath — 1 operation(s) for orgs/cobalt.
  name: Openpath Orgs/cobalt API
  slug: openpath-orgs-cobalt-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Contact Sensors
  name: Openpath Orgs/contact Sensors API
  slug: openpath-orgs-contactsensors-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/credentialActionTypes API from Openpath — 2 operation(s) for orgs/credentialactiontypes.
  name: Openpath Orgs/credential Action Types API
  slug: openpath-orgs-credentialactiontypes-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/credentials API from Openpath — 3 operation(s) for orgs/credentials.
  name: Openpath Orgs/credentials API
  slug: openpath-orgs-credentials-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Credential Types
  name: Openpath Orgs/credential Types API
  slug: openpath-orgs-credentialtypes-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Custom Fields
  name: Openpath Orgs/custom Fields API
  slug: openpath-orgs-customfields-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Custom Field Types
  name: Openpath Orgs/custom Field Types API
  slug: openpath-orgs-customfieldtypes-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/dashboards API from Openpath — 4 operation(s) for orgs/dashboards.
  name: Openpath Orgs/dashboards API
  slug: openpath-orgs-dashboards-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/effectiveScopes API from Openpath — 1 operation(s) for orgs/effectivescopes.
  name: Openpath Orgs/effective Scopes API
  slug: openpath-orgs-effectivescopes-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/emailAlerts API from Openpath — 1 operation(s) for orgs/emailalerts.
  name: Openpath Orgs/email Alerts API
  slug: openpath-orgs-emailalerts-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/emailAlertTypes API from Openpath — 2 operation(s) for orgs/emailalerttypes.
  name: Openpath Orgs/email Alert Types API
  slug: openpath-orgs-emailalerttypes-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Entries and Entry Hardware
  name: Openpath Orgs/entries API
  slug: openpath-orgs-entries-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Entry States
  name: Openpath Orgs/entry States API
  slug: openpath-orgs-entrystates-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/eolSupervisions API from Openpath — 2 operation(s) for orgs/eolsupervisions.
  name: Openpath Orgs/eol Supervisions API
  slug: openpath-orgs-eolsupervisions-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/features API from Openpath — 1 operation(s) for orgs/features.
  name: Openpath Orgs/features API
  slug: openpath-orgs-features-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/fobAllegions API from Openpath — 2 operation(s) for orgs/foballegions.
  name: Openpath Orgs/fob Allegions API
  slug: openpath-orgs-foballegions-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/genericInputs API from Openpath — 2 operation(s) for orgs/genericinputs.
  name: Openpath Orgs/generic Inputs API
  slug: openpath-orgs-genericinputs-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: User Groups
  name: Openpath Orgs/groups API
  slug: openpath-orgs-groups-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/hookActions API from Openpath — 2 operation(s) for orgs/hookactions.
  name: Openpath Orgs/hook Actions API
  slug: openpath-orgs-hookactions-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/hookEvents API from Openpath — 2 operation(s) for orgs/hookevents.
  name: Openpath Orgs/hook Events API
  slug: openpath-orgs-hookevents-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Identity Providers and OAuth2
  name: Openpath Orgs/identity Providers API
  slug: openpath-orgs-identityproviders-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Identity Provider Types
  name: Openpath Orgs/identity Provider Types API
  slug: openpath-orgs-identityprovidertypes-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/ios API from Openpath — 2 operation(s) for orgs/ios.
  name: Openpath Orgs/ios API
  slug: openpath-orgs-ios-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/locationMeasurementSourceTypes API from Openpath — 2 operation(s) for orgs/locationmeasurementsourcetypes.
  name: Openpath Orgs/location Measurement Source Types API
  slug: openpath-orgs-locationmeasurementsourcetypes-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/lockdownPlans API from Openpath — 4 operation(s) for orgs/lockdownplans.
  name: Openpath Orgs/lockdown Plans API
  slug: openpath-orgs-lockdownplans-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/mailrooms API from Openpath — 5 operation(s) for orgs/mailrooms.
  name: Openpath Orgs/mailrooms API
  slug: openpath-orgs-mailrooms-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/maintenanceWindow API from Openpath — 1 operation(s) for orgs/maintenancewindow.
  name: Openpath Orgs/maintenance Window API
  slug: openpath-orgs-maintenancewindow-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/maintenanceWindowAcuMap API from Openpath — 2 operation(s) for orgs/maintenancewindowacumap.
  name: Openpath Orgs/maintenance Window Acu Map API
  slug: openpath-orgs-maintenancewindowacumap-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/maintenanceWindowDefinition API from Openpath — 2 operation(s) for orgs/maintenancewindowdefinition.
  name: Openpath Orgs/maintenance Window Definition API
  slug: openpath-orgs-maintenancewindowdefinition-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/maintenanceWindowMap API from Openpath — 2 operation(s) for orgs/maintenancewindowmap.
  name: Openpath Orgs/maintenance Window Map API
  slug: openpath-orgs-maintenancewindowmap-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/mobileAppConfig API from Openpath — 1 operation(s) for orgs/mobileappconfig.
  name: Openpath Orgs/mobile App Config API
  slug: openpath-orgs-mobileappconfig-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/namespaces API from Openpath — 1 operation(s) for orgs/namespaces.
  name: Openpath Orgs/namespaces API
  slug: openpath-orgs-namespaces-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/opvideo-devices API from Openpath — 2 operation(s) for orgs/opvideo-devices.
  name: Openpath Orgs/opvideo Devices API
  slug: openpath-orgs-opvideo-devices-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/orgIdentities API from Openpath — 1 operation(s) for orgs/orgidentities.
  name: Openpath Orgs/org Identities API
  slug: openpath-orgs-orgidentities-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/orgPackagePlans API from Openpath — 2 operation(s) for orgs/orgpackageplans.
  name: Openpath Orgs/org Package Plans API
  slug: openpath-orgs-orgpackageplans-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Org Pictures
  name: Openpath Orgs/org Pictures API
  slug: openpath-orgs-orgpictures-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/packagePlans API from Openpath — 2 operation(s) for orgs/packageplans.
  name: Openpath Orgs/package Plans API
  slug: openpath-orgs-packageplans-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Entry Color Palettes
  name: Openpath Orgs/palettes API
  slug: openpath-orgs-palettes-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/parcelMessageTypes API from Openpath — 1 operation(s) for orgs/parcelmessagetypes.
  name: Openpath Orgs/parcel Message Types API
  slug: openpath-orgs-parcelmessagetypes-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/parcels API from Openpath — 12 operation(s) for orgs/parcels.
  name: Openpath Orgs/parcels API
  slug: openpath-orgs-parcels-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/parcelStatuses API from Openpath — 1 operation(s) for orgs/parcelstatuses.
  name: Openpath Orgs/parcel Statuses API
  slug: openpath-orgs-parcelstatuses-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Readers
  name: Openpath Orgs/readers API
  slug: openpath-orgs-readers-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/recentAlarms API from Openpath — 1 operation(s) for orgs/recentalarms.
  name: Openpath Orgs/recent Alarms API
  slug: openpath-orgs-recentalarms-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/recentAlarmsExt API from Openpath — 1 operation(s) for orgs/recentalarmsext.
  name: Openpath Orgs/recent Alarms Ext API
  slug: openpath-orgs-recentalarmsext-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Relay Hardware Types
  name: Openpath Orgs/relay Hardware Types API
  slug: openpath-orgs-relayhardwaretypes-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Relays
  name: Openpath Orgs/relays API
  slug: openpath-orgs-relays-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Reports and Analytics
  name: Openpath Orgs/reports API
  slug: openpath-orgs-reports-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Request-To-Exit Sensors
  name: Openpath Orgs/rexs API
  slug: openpath-orgs-rexs-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: User Roles
  name: Openpath Orgs/roles API
  slug: openpath-orgs-roles-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Schedules
  name: Openpath Orgs/schedules API
  slug: openpath-orgs-schedules-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Schedule Types
  name: Openpath Orgs/schedule Types API
  slug: openpath-orgs-scheduletypes-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Scope Resources for User Roles
  name: Openpath Orgs/scope Resources API
  slug: openpath-orgs-scoperesources-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/sharedUsers API from Openpath — 3 operation(s) for orgs/sharedusers.
  name: Openpath Orgs/shared Users API
  slug: openpath-orgs-sharedusers-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Sites
  name: Openpath Orgs/sites API
  slug: openpath-orgs-sites-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: REST Hook Subscriptions
  name: Openpath Orgs/subscriptions API
  slug: openpath-orgs-subscriptions-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/tasks API from Openpath — 5 operation(s) for orgs/tasks.
  name: Openpath Orgs/tasks API
  slug: openpath-orgs-tasks-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/termsAgreements API from Openpath — 3 operation(s) for orgs/termsagreements.
  name: Openpath Orgs/terms Agreements API
  slug: openpath-orgs-termsagreements-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/thirdPartyReaders API from Openpath — 2 operation(s) for orgs/thirdpartyreaders.
  name: Openpath Orgs/third Party Readers API
  slug: openpath-orgs-thirdpartyreaders-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/thirdPartyWiegands API from Openpath — 2 operation(s) for orgs/thirdpartywiegands.
  name: Openpath Orgs/third Party Wiegands API
  slug: openpath-orgs-thirdpartywiegands-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Entry Trigger Methods
  name: Openpath Orgs/trigger Methods API
  slug: openpath-orgs-triggermethods-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/triggerPermissionsChange API from Openpath — 1 operation(s) for orgs/triggerpermissionschange.
  name: Openpath Orgs/trigger Permissions Change API
  slug: openpath-orgs-triggerpermissionschange-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/unusedInputs API from Openpath — 2 operation(s) for orgs/unusedinputs.
  name: Openpath Orgs/unused Inputs API
  slug: openpath-orgs-unusedinputs-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Users and Credentials
  name: Openpath Orgs/users API
  slug: openpath-orgs-users-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/videoProviderTypes API from Openpath — 1 operation(s) for orgs/videoprovidertypes.
  name: Openpath Orgs/video Provider Types API
  slug: openpath-orgs-videoprovidertypes-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/widgetTypes API from Openpath — 2 operation(s) for orgs/widgettypes.
  name: Openpath Orgs/widget Types API
  slug: openpath-orgs-widgettypes-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Wiegand controls
  name: Openpath Orgs/wiegands API
  slug: openpath-orgs-wiegands-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/wirelessGateways API from Openpath — 6 operation(s) for orgs/wirelessgateways.
  name: Openpath Orgs/wireless Gateways API
  slug: openpath-orgs-wirelessgateways-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/wirelessLockGateways API from Openpath — 5 operation(s) for orgs/wirelesslockgateways.
  name: Openpath Orgs/wireless Lock Gateways API
  slug: openpath-orgs-wirelesslockgateways-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/wirelessLockProviders API from Openpath — 6 operation(s) for orgs/wirelesslockproviders.
  name: Openpath Orgs/wireless Lock Providers API
  slug: openpath-orgs-wirelesslockproviders-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/wirelessLockReaders API from Openpath — 2 operation(s) for orgs/wirelesslockreaders.
  name: Openpath Orgs/wireless Lock Readers API
  slug: openpath-orgs-wirelesslockreaders-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/wirelessLocks API from Openpath — 5 operation(s) for orgs/wirelesslocks.
  name: Openpath Orgs/wireless Locks API
  slug: openpath-orgs-wirelesslocks-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: The orgs/wirelessLockTemplates API from Openpath — 2 operation(s) for orgs/wirelesslocktemplates.
  name: Openpath Orgs/wireless Lock Templates API
  slug: openpath-orgs-wirelesslocktemplates-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Zones
  name: Openpath Orgs/zones API
  slug: openpath-orgs-zones-api
- baseURL: https://api.openpath.com
  baseurl_source: declared
  description: Token use and validation
  name: Openpath Tokens API
  slug: openpath-tokens-api
artifact_total: 183
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Openpath API Documentation auth API
  slug: open-openpath-auth-api
- collection_type: open
  name: Openpath API Documentation auth billableFeatures API
  slug: open-openpath-billablefeatures-api
- collection_type: open
  name: Openpath API Documentation auth identities API
  slug: open-openpath-identities-api
- collection_type: open
  name: Openpath API Documentation auth orgs/acuModels API
  slug: open-openpath-orgs-acumodels-api
- collection_type: open
  name: Openpath API Documentation auth orgs/acuPorts API
  slug: open-openpath-orgs-acuports-api
- collection_type: open
  name: Openpath API Documentation auth orgs/acuPortTypes API
  slug: open-openpath-orgs-acuporttypes-api
- collection_type: open
  name: Openpath API Documentation auth orgs/acus API
  slug: open-openpath-orgs-acus-api
- collection_type: open
  name: Openpath API Documentation auth orgs/alarmActions API
  slug: open-openpath-orgs-alarmactions-api
- collection_type: open
  name: Openpath API Documentation auth orgs/alarmConfigurations API
  slug: open-openpath-orgs-alarmconfigurations-api
- collection_type: open
  name: Openpath API Documentation auth orgs/alarmSeverities API
  slug: open-openpath-orgs-alarmseverities-api
- collection_type: open
  name: Openpath API Documentation auth orgs/alarmsExt API
  slug: open-openpath-orgs-alarmsext-api
- collection_type: open
  name: Openpath API Documentation auth orgs/alarmStatuses API
  slug: open-openpath-orgs-alarmstatuses-api
- collection_type: open
  name: Openpath API Documentation auth orgs/authCerts API
  slug: open-openpath-orgs-authcerts-api
- collection_type: open
  name: Openpath API Documentation auth orgs/badgeConfigs API
  slug: open-openpath-orgs-badgeconfigs-api
- collection_type: open
  name: Openpath API Documentation auth orgs/cardFormats API
  slug: open-openpath-orgs-cardformats-api
- collection_type: open
  name: Openpath API Documentation auth orgs/cobalt API
  slug: open-openpath-orgs-cobalt-api
- collection_type: open
  name: Openpath API Documentation auth orgs/contactSensors API
  slug: open-openpath-orgs-contactsensors-api
- collection_type: open
  name: Openpath API Documentation auth orgs/credentialActionTypes API
  slug: open-openpath-orgs-credentialactiontypes-api
- collection_type: open
  name: Openpath API Documentation auth orgs/credentials API
  slug: open-openpath-orgs-credentials-api
- collection_type: open
  name: Openpath API Documentation auth orgs/credentialTypes API
  slug: open-openpath-orgs-credentialtypes-api
- collection_type: open
  name: Openpath API Documentation auth orgs/customFields API
  slug: open-openpath-orgs-customfields-api
- collection_type: open
  name: Openpath API Documentation auth orgs/customFieldTypes API
  slug: open-openpath-orgs-customfieldtypes-api
- collection_type: open
  name: Openpath API Documentation auth orgs/dashboards API
  slug: open-openpath-orgs-dashboards-api
- collection_type: open
  name: Openpath API Documentation auth orgs/effectiveScopes API
  slug: open-openpath-orgs-effectivescopes-api
- collection_type: open
  name: Openpath API Documentation auth orgs/emailAlerts API
  slug: open-openpath-orgs-emailalerts-api
- collection_type: open
  name: Openpath API Documentation auth orgs/emailAlertTypes API
  slug: open-openpath-orgs-emailalerttypes-api
- collection_type: open
  name: Openpath API Documentation auth orgs/entries API
  slug: open-openpath-orgs-entries-api
- collection_type: open
  name: Openpath API Documentation auth orgs/entryStates API
  slug: open-openpath-orgs-entrystates-api
- collection_type: open
  name: Openpath API Documentation auth orgs/eolSupervisions API
  slug: open-openpath-orgs-eolsupervisions-api
- collection_type: open
  name: Openpath API Documentation auth orgs/features API
  slug: open-openpath-orgs-features-api
- collection_type: open
  name: Openpath API Documentation auth orgs/fobAllegions API
  slug: open-openpath-orgs-foballegions-api
- collection_type: open
  name: Openpath API Documentation auth orgs/genericInputs API
  slug: open-openpath-orgs-genericinputs-api
- collection_type: open
  name: Openpath API Documentation auth orgs/groups API
  slug: open-openpath-orgs-groups-api
- collection_type: open
  name: Openpath API Documentation auth orgs/hookActions API
  slug: open-openpath-orgs-hookactions-api
- collection_type: open
  name: Openpath API Documentation auth orgs/hookEvents API
  slug: open-openpath-orgs-hookevents-api
- collection_type: open
  name: Openpath API Documentation auth orgs/identityProviders API
  slug: open-openpath-orgs-identityproviders-api
- collection_type: open
  name: Openpath API Documentation auth orgs/identityProviderTypes API
  slug: open-openpath-orgs-identityprovidertypes-api
- collection_type: open
  name: Openpath API Documentation auth orgs/ios API
  slug: open-openpath-orgs-ios-api
- collection_type: open
  name: Openpath API Documentation auth orgs/locationMeasurementSourceTypes API
  slug: open-openpath-orgs-locationmeasurementsourcetypes-api
- collection_type: open
  name: Openpath API Documentation auth orgs/lockdownPlans API
  slug: open-openpath-orgs-lockdownplans-api
- collection_type: open
  name: Openpath API Documentation auth orgs/mailrooms API
  slug: open-openpath-orgs-mailrooms-api
- collection_type: open
  name: Openpath API Documentation auth orgs/maintenanceWindow API
  slug: open-openpath-orgs-maintenancewindow-api
- collection_type: open
  name: Openpath API Documentation auth orgs/maintenanceWindowAcuMap API
  slug: open-openpath-orgs-maintenancewindowacumap-api
- collection_type: open
  name: Openpath API Documentation auth orgs/maintenanceWindowDefinition API
  slug: open-openpath-orgs-maintenancewindowdefinition-api
- collection_type: open
  name: Openpath API Documentation auth orgs/maintenanceWindowMap API
  slug: open-openpath-orgs-maintenancewindowmap-api
- collection_type: open
  name: Openpath API Documentation auth orgs/mobileAppConfig API
  slug: open-openpath-orgs-mobileappconfig-api
- collection_type: open
  name: Openpath API Documentation auth orgs/namespaces API
  slug: open-openpath-orgs-namespaces-api
- collection_type: open
  name: Openpath API Documentation auth orgs/opvideo-devices API
  slug: open-openpath-orgs-opvideo-devices-api
- collection_type: open
  name: Openpath API Documentation auth orgs/orgIdentities API
  slug: open-openpath-orgs-orgidentities-api
- collection_type: open
  name: Openpath API Documentation auth orgs/orgPackagePlans API
  slug: open-openpath-orgs-orgpackageplans-api
- collection_type: open
  name: Openpath API Documentation auth orgs/orgPictures API
  slug: open-openpath-orgs-orgpictures-api
- collection_type: open
  name: Openpath API Documentation auth orgs/packagePlans API
  slug: open-openpath-orgs-packageplans-api
- collection_type: open
  name: Openpath API Documentation auth orgs/palettes API
  slug: open-openpath-orgs-palettes-api
- collection_type: open
  name: Openpath API Documentation auth orgs/parcelMessageTypes API
  slug: open-openpath-orgs-parcelmessagetypes-api
- collection_type: open
  name: Openpath API Documentation auth orgs/parcels API
  slug: open-openpath-orgs-parcels-api
- collection_type: open
  name: Openpath API Documentation auth orgs/parcelStatuses API
  slug: open-openpath-orgs-parcelstatuses-api
- collection_type: open
  name: Openpath API Documentation auth orgs/readers API
  slug: open-openpath-orgs-readers-api
- collection_type: open
  name: Openpath API Documentation auth orgs/recentAlarms API
  slug: open-openpath-orgs-recentalarms-api
- collection_type: open
  name: Openpath API Documentation auth orgs/recentAlarmsExt API
  slug: open-openpath-orgs-recentalarmsext-api
- collection_type: open
  name: Openpath API Documentation auth orgs/relayHardwareTypes API
  slug: open-openpath-orgs-relayhardwaretypes-api
- collection_type: open
  name: Openpath API Documentation auth orgs/relays API
  slug: open-openpath-orgs-relays-api
- collection_type: open
  name: Openpath API Documentation auth orgs/reports API
  slug: open-openpath-orgs-reports-api
- collection_type: open
  name: Openpath API Documentation auth orgs/rexs API
  slug: open-openpath-orgs-rexs-api
- collection_type: open
  name: Openpath API Documentation auth orgs/roles API
  slug: open-openpath-orgs-roles-api
- collection_type: open
  name: Openpath API Documentation auth orgs/schedules API
  slug: open-openpath-orgs-schedules-api
- collection_type: open
  name: Openpath API Documentation auth orgs/scheduleTypes API
  slug: open-openpath-orgs-scheduletypes-api
- collection_type: open
  name: Openpath API Documentation auth orgs/scopeResources API
  slug: open-openpath-orgs-scoperesources-api
- collection_type: open
  name: Openpath API Documentation auth orgs/sharedUsers API
  slug: open-openpath-orgs-sharedusers-api
- collection_type: open
  name: Openpath API Documentation auth orgs/sites API
  slug: open-openpath-orgs-sites-api
- collection_type: open
  name: Openpath API Documentation auth orgs/subscriptions API
  slug: open-openpath-orgs-subscriptions-api
- collection_type: open
  name: Openpath API Documentation auth orgs/tasks API
  slug: open-openpath-orgs-tasks-api
- collection_type: open
  name: Openpath API Documentation auth orgs/termsAgreements API
  slug: open-openpath-orgs-termsagreements-api
- collection_type: open
  name: Openpath API Documentation auth orgs/thirdPartyReaders API
  slug: open-openpath-orgs-thirdpartyreaders-api
- collection_type: open
  name: Openpath API Documentation auth orgs/thirdPartyWiegands API
  slug: open-openpath-orgs-thirdpartywiegands-api
- collection_type: open
  name: Openpath API Documentation auth orgs/triggerMethods API
  slug: open-openpath-orgs-triggermethods-api
- collection_type: open
  name: Openpath API Documentation auth orgs/triggerPermissionsChange API
  slug: open-openpath-orgs-triggerpermissionschange-api
- collection_type: open
  name: Openpath API Documentation auth orgs/unusedInputs API
  slug: open-openpath-orgs-unusedinputs-api
- collection_type: open
  name: Openpath API Documentation auth orgs/users API
  slug: open-openpath-orgs-users-api
- collection_type: open
  name: Openpath API Documentation auth orgs/videoProviderTypes API
  slug: open-openpath-orgs-videoprovidertypes-api
- collection_type: open
  name: Openpath API Documentation auth orgs/widgetTypes API
  slug: open-openpath-orgs-widgettypes-api
- collection_type: open
  name: Openpath API Documentation auth orgs/wiegands API
  slug: open-openpath-orgs-wiegands-api
- collection_type: open
  name: Openpath API Documentation auth orgs/wirelessGateways API
  slug: open-openpath-orgs-wirelessgateways-api
- collection_type: open
  name: Openpath API Documentation auth orgs/wirelessLockGateways API
  slug: open-openpath-orgs-wirelesslockgateways-api
- collection_type: open
  name: Openpath API Documentation auth orgs/wirelessLockProviders API
  slug: open-openpath-orgs-wirelesslockproviders-api
- collection_type: open
  name: Openpath API Documentation auth orgs/wirelessLockReaders API
  slug: open-openpath-orgs-wirelesslockreaders-api
- collection_type: open
  name: Openpath API Documentation auth orgs/wirelessLocks API
  slug: open-openpath-orgs-wirelesslocks-api
- collection_type: open
  name: Openpath API Documentation auth orgs/wirelessLockTemplates API
  slug: open-openpath-orgs-wirelesslocktemplates-api
- collection_type: open
  name: Openpath API Documentation auth orgs/zones API
  slug: open-openpath-orgs-zones-api
- collection_type: open
  name: Openpath API Documentation auth tokens API
  slug: open-openpath-tokens-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/motorola-solutions/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/openpath/refs/heads/main/capabilities/openpath-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/openpath-capability-edges.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openpath.readme.io
- group: docs
  title: ''
  type: Documentation
  url: https://openpath.readme.io
- group: docs
  title: ''
  type: APIReference
  url: https://openpath.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://openpath.readme.io/docs/basics-to-start
- group: start
  title: ''
  type: Login
  url: https://control.openpath.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openpath/refs/heads/main/authentication/openpath-authentication.yml
  title: ''
  type: Authentication
  url: authentication/openpath-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openpath/refs/heads/main/scopes/openpath-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/openpath-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openpath/refs/heads/main/well-known/openpath-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/openpath-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openpath/refs/heads/main/conventions/openpath-conventions.yml
  title: ''
  type: Conventions
  url: conventions/openpath-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openpath/refs/heads/main/errors/openpath-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/openpath-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openpath/refs/heads/main/lifecycle/openpath-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/openpath-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openpath/refs/heads/main/conformance/openpath-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openpath-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openpath/refs/heads/main/data-model/openpath-data-model.yml
  title: ''
  type: DataModel
  url: data-model/openpath-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openpath/refs/heads/main/mcp/openpath-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/openpath-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openpath/refs/heads/main/llms/openpath-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/openpath-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openpath/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openpath/refs/heads/main/agentic-access/openpath-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/openpath-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openpath/refs/heads/main/security/openpath-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openpath-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.openpath.com
created: '2026-07-17'
description: 'Openpath is a cloud-based, mobile-first access control platform for the modern workplace — touchless entry, door/reader/relay hardware (ACUs), user and credential management, roles, schedules, sites and zones, video and alarm integrations. Founded in 2016 and backed by Emergence Capital, Openpath was acquired by Motorola Solutions in 2021 and is now marketed as Avigilon Alta; openpath.com redirects to avigilon.com/access-control. Its developer surface remains live: a documented REST API at api.openpath.com (546 operations, JWT scope-based auth, OpenID Connect) with reference docs on ReadMe.'
image: https://files.readme.io/31f837c-small-Avigilon_Alta_favicon.png
layout: provider
modified: '2026-07-20'
name: Openpath
nav: Providers
network: true
overview: 'Openpath publishes 89 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Billable Features API, Identities API, and 86 more. Tagged areas include Company, Security, Access Control, Physical Security, and Identity.


  Openpath''s developer surface includes documentation, API reference, getting-started guide, authentication, and 17 more developer resources.'
random_paper: 5
scopes:
- name: Openpath Scopes
  scope_count: 3
  slug: openpath-scopes
  summary_line: 3 scopes
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.8
  facets:
    access_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 48.3
    developer_ergonomics: 32.7
    discoverability: 70.4
    operational_transparency: 0.0
  previous_composite: 29.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 89
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/openpath/refs/heads/main/screenshots/openpath-2026-08-07T190619.png
security:
- kind: authentication
  name: Openpath Authentication
  slug: openpath-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Openpath Domain Security
  slug: openpath-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openpath
tags:
- Company
- Security
- Access Control
- Physical Security
- Identity
- Credentials
- IoT
- Smart Buildings
- Avigilon Alta
- Motorola Solutions
website: https://www.openpath.com
---
