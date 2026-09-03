---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 349
  human_in_the_loop: 9
  name: Inductive Automation Agentic Access
  operation_count: 673
  slug: inductive-automation-agentic-access
  summary_line: 673 operations · 349 acting · 9 human-in-the-loop
api_count: 1
apis:
- description: The Ignition Gateway REST API (available in Ignition 8.3+) provides an OpenAPI- compliant HTTP interface to Gateway configuration resources including tags, projects, modules, device connections, and h
  name: Ignition Gateway REST API
  slug: ignition-gateway-rest-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Access control configuration
  name: Inductive Automation access-control API
  slug: inductive-automation-access-control-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: EAM agent group management
  name: Inductive Automation agent-group API
  slug: inductive-automation-agent-group-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: EAM agent management
  name: Inductive Automation agent-management API
  slug: inductive-automation-agent-management-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Alarm journal resource management
  name: Inductive Automation alarm-journal-resources API
  slug: inductive-automation-alarm-journal-resources-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Alarm notification profile management
  name: Inductive Automation alarm-notification-profile API
  slug: inductive-automation-alarm-notification-profile-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: API token authentication
  name: Inductive Automation api-token API
  slug: inductive-automation-api-token-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Audit log access
  name: Inductive Automation audit API
  slug: inductive-automation-audit-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Script invocation endpoints
  name: Inductive Automation call-script API
  slug: inductive-automation-call-script-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: TLS/SSL certificate management
  name: Inductive Automation certificate-management API
  slug: inductive-automation-certificate-management-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Charts module information
  name: Inductive Automation charts-info API
  slug: inductive-automation-charts-info-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Client PKI certificate management
  name: Inductive Automation client-pki-certificate-management API
  slug: inductive-automation-client-pki-certificate-management-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Alarm configuration resources
  name: Inductive Automation config-alarm API
  slug: inductive-automation-config-alarm-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: API token configuration
  name: Inductive Automation config-api-token API
  slug: inductive-automation-config-api-token-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Audit profile configuration
  name: Inductive Automation config-audit-profiles API
  slug: inductive-automation-config-audit-profiles-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Database connection configuration
  name: Inductive Automation config-databases API
  slug: inductive-automation-config-databases-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Edge system properties
  name: Inductive Automation config-edge-system-properties API
  slug: inductive-automation-config-edge-system-properties-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Email profile configuration
  name: Inductive Automation config-email-profile API
  slug: inductive-automation-config-email-profile-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Gateway network configuration
  name: Inductive Automation config-gateway-network API
  slug: inductive-automation-config-gateway-network-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Identity provider configuration
  name: Inductive Automation config-identity-provider API
  slug: inductive-automation-config-identity-provider-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Keyboard layout configuration
  name: Inductive Automation config-keyboard-layouts API
  slug: inductive-automation-config-keyboard-layouts-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Local system properties
  name: Inductive Automation config-local-system-properties API
  slug: inductive-automation-config-local-system-properties-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: General configuration management
  name: Inductive Automation config-management API
  slug: inductive-automation-config-management-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Metrics dashboard configuration
  name: Inductive Automation config-metrics-dashboard API
  slug: inductive-automation-config-metrics-dashboard-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: OAuth2 client configuration
  name: Inductive Automation config-oauth2-client API
  slug: inductive-automation-config-oauth2-client-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Perspective module branding configuration
  name: Inductive Automation config-perspective-branding API
  slug: inductive-automation-config-perspective-branding-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Perspective font configuration
  name: Inductive Automation config-perspective-fonts API
  slug: inductive-automation-config-perspective-fonts-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Perspective icon library configuration
  name: Inductive Automation config-perspective-icons API
  slug: inductive-automation-config-perspective-icons-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Perspective theme configuration
  name: Inductive Automation config-perspective-themes API
  slug: inductive-automation-config-perspective-themes-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Secret provider configuration
  name: Inductive Automation config-secret-provider API
  slug: inductive-automation-config-secret-provider-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Security zone level configuration
  name: Inductive Automation config-security-levels API
  slug: inductive-automation-config-security-levels-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Security properties configuration
  name: Inductive Automation config-security-properties API
  slug: inductive-automation-config-security-properties-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Security zone configuration
  name: Inductive Automation config-security-zone API
  slug: inductive-automation-config-security-zone-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Store-and-forward configuration
  name: Inductive Automation config-store-forward API
  slug: inductive-automation-config-store-forward-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: System properties configuration
  name: Inductive Automation config-system-properties API
  slug: inductive-automation-config-system-properties-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Tag provider configuration
  name: Inductive Automation config-tag-provider API
  slug: inductive-automation-config-tag-provider-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Translation configuration
  name: Inductive Automation config-translations API
  slug: inductive-automation-config-translations-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: User source configuration
  name: Inductive Automation config-user-source API
  slug: inductive-automation-config-user-source-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Data synchronization
  name: Inductive Automation data-syncs API
  slug: inductive-automation-data-syncs-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Designer session management
  name: Inductive Automation designer-sessions API
  slug: inductive-automation-designer-sessions-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Device connection management
  name: Inductive Automation device API
  slug: inductive-automation-device-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Enterprise Administration Module task management
  name: Inductive Automation eam-tasks API
  slug: inductive-automation-eam-tasks-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Encryption utilities
  name: Inductive Automation encryption API
  slug: inductive-automation-encryption-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Generic entity management
  name: Inductive Automation entity API
  slug: inductive-automation-entity-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Event threshold configuration
  name: Inductive Automation event-thresholds API
  slug: inductive-automation-event-thresholds-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Thread pool executor management
  name: Inductive Automation executors API
  slug: inductive-automation-executors-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Gateway backup and restore
  name: Inductive Automation gateway-backups API
  slug: inductive-automation-gateway-backups-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Gateway information
  name: Inductive Automation gateway-info API
  slug: inductive-automation-gateway-info-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Gateway network topology
  name: Inductive Automation gateway-network API
  slug: inductive-automation-gateway-network-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Gateway script execution
  name: Inductive Automation gateway-scripts API
  slug: inductive-automation-gateway-scripts-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: General alarm settings
  name: Inductive Automation general-alarm-settings API
  slug: inductive-automation-general-alarm-settings-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: The general API from Inductive Automation — 3 operation(s) for general.
  name: Inductive Automation general API
  slug: inductive-automation-general-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: User group information
  name: Inductive Automation groups-info API
  slug: inductive-automation-groups-info-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Tag historian configuration
  name: Inductive Automation historian-config API
  slug: inductive-automation-historian-config-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Ignition Launcher operations
  name: Inductive Automation launcher API
  slug: inductive-automation-launcher-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: License activation management
  name: Inductive Automation license-activation API
  slug: inductive-automation-license-activation-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: License management operations
  name: Inductive Automation license-management API
  slug: inductive-automation-license-management-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: License status information
  name: Inductive Automation license-status API
  slug: inductive-automation-license-status-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Local device management
  name: Inductive Automation local devices API
  slug: inductive-automation-local-devices-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Logging configuration
  name: Inductive Automation logging API
  slug: inductive-automation-logging-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Managed tag provider operations
  name: Inductive Automation managed-tag-provider API
  slug: inductive-automation-managed-tag-provider-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Module certificate management
  name: Inductive Automation module-certificate API
  slug: inductive-automation-module-certificate-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Module EULA acceptance
  name: Inductive Automation module-eula API
  slug: inductive-automation-module-eula-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Module settings configuration
  name: Inductive Automation module-settings API
  slug: inductive-automation-module-settings-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Installed module management
  name: Inductive Automation modules API
  slug: inductive-automation-modules-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: OPC connection management
  name: Inductive Automation opc connection API
  slug: inductive-automation-opc-connection-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Gateway overview and status
  name: Inductive Automation overview API
  slug: inductive-automation-overview-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Perspective module session management
  name: Inductive Automation perspective-sessions API
  slug: inductive-automation-perspective-sessions-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Alarm notification pipeline status
  name: Inductive Automation pipeline-status API
  slug: inductive-automation-pipeline-status-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Ignition project management
  name: Inductive Automation projects API
  slug: inductive-automation-projects-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Quick-start setup wizard
  name: Inductive Automation quickstart API
  slug: inductive-automation-quickstart-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Gateway redundancy configuration
  name: Inductive Automation redundancy API
  slug: inductive-automation-redundancy-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Remote Gateway upgrade operations
  name: Inductive Automation remote-upgrade API
  slug: inductive-automation-remote-upgrade-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Reporting module information
  name: Inductive Automation reports-info API
  slug: inductive-automation-reports-info-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Gateway restart task management
  name: Inductive Automation restart-tasks API
  slug: inductive-automation-restart-tasks-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Alarm roster configuration
  name: Inductive Automation roster-config API
  slug: inductive-automation-roster-config-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Running script monitoring
  name: Inductive Automation running-scripts API
  slug: inductive-automation-running-scripts-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Secret provider management
  name: Inductive Automation secret-providers API
  slug: inductive-automation-secret-providers-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: OPC UA server configuration
  name: Inductive Automation server API
  slug: inductive-automation-server-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Server PKI certificate management
  name: Inductive Automation server-pki-certificate-management API
  slug: inductive-automation-server-pki-certificate-management-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Service connector configuration
  name: Inductive Automation service-connectors API
  slug: inductive-automation-service-connectors-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Sequential Function Chart configuration
  name: Inductive Automation sfc-config API
  slug: inductive-automation-sfc-config-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Storage configuration
  name: Inductive Automation storage API
  slug: inductive-automation-storage-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Data stream information
  name: Inductive Automation streams-info API
  slug: inductive-automation-streams-info-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: System performance metrics
  name: Inductive Automation system-performance API
  slug: inductive-automation-system-performance-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: JVM thread diagnostics
  name: Inductive Automation thread-diagnostics API
  slug: inductive-automation-thread-diagnostics-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: SCIM 2.0 user and group management
  name: Inductive Automation user-management-scim API
  slug: inductive-automation-user-management-scim-api
- baseURL: https://{gateway-host}:8088/api
  baseurl_source: declared
  description: Vision module client sessions
  name: Inductive Automation vision-sessions API
  slug: inductive-automation-vision-sessions-api
artifact_total: 192
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ignition Gateway REST access-control API
  slug: open-inductive-automation-access-control-api
- collection_type: open
  name: Ignition Gateway REST access-control agent-group API
  slug: open-inductive-automation-agent-group-api
- collection_type: open
  name: Ignition Gateway REST access-control agent-management API
  slug: open-inductive-automation-agent-management-api
- collection_type: open
  name: Ignition Gateway REST access-control alarm-journal-resources API
  slug: open-inductive-automation-alarm-journal-resources-api
- collection_type: open
  name: Ignition Gateway REST access-control alarm-notification-profile API
  slug: open-inductive-automation-alarm-notification-profile-api
- collection_type: open
  name: Ignition Gateway REST access-control api-token API
  slug: open-inductive-automation-api-token-api
- collection_type: open
  name: Ignition Gateway REST access-control audit API
  slug: open-inductive-automation-audit-api
- collection_type: open
  name: Ignition Gateway REST access-control call-script API
  slug: open-inductive-automation-call-script-api
- collection_type: open
  name: Ignition Gateway REST access-control certificate-management API
  slug: open-inductive-automation-certificate-management-api
- collection_type: open
  name: Ignition Gateway REST access-control charts-info API
  slug: open-inductive-automation-charts-info-api
- collection_type: open
  name: Ignition Gateway REST access-control client-pki-certificate-management API
  slug: open-inductive-automation-client-pki-certificate-management-api
- collection_type: open
  name: Ignition Gateway REST access-control config-alarm API
  slug: open-inductive-automation-config-alarm-api
- collection_type: open
  name: Ignition Gateway REST access-control config-api-token API
  slug: open-inductive-automation-config-api-token-api
- collection_type: open
  name: Ignition Gateway REST access-control config-audit-profiles API
  slug: open-inductive-automation-config-audit-profiles-api
- collection_type: open
  name: Ignition Gateway REST access-control config-databases API
  slug: open-inductive-automation-config-databases-api
- collection_type: open
  name: Ignition Gateway REST access-control config-edge-system-properties API
  slug: open-inductive-automation-config-edge-system-properties-api
- collection_type: open
  name: Ignition Gateway REST access-control config-email-profile API
  slug: open-inductive-automation-config-email-profile-api
- collection_type: open
  name: Ignition Gateway REST access-control config-gateway-network API
  slug: open-inductive-automation-config-gateway-network-api
- collection_type: open
  name: Ignition Gateway REST access-control config-identity-provider API
  slug: open-inductive-automation-config-identity-provider-api
- collection_type: open
  name: Ignition Gateway REST access-control config-keyboard-layouts API
  slug: open-inductive-automation-config-keyboard-layouts-api
- collection_type: open
  name: Ignition Gateway REST access-control config-local-system-properties API
  slug: open-inductive-automation-config-local-system-properties-api
- collection_type: open
  name: Ignition Gateway REST access-control config-management API
  slug: open-inductive-automation-config-management-api
- collection_type: open
  name: Ignition Gateway REST access-control config-metrics-dashboard API
  slug: open-inductive-automation-config-metrics-dashboard-api
- collection_type: open
  name: Ignition Gateway REST access-control config-oauth2-client API
  slug: open-inductive-automation-config-oauth2-client-api
- collection_type: open
  name: Ignition Gateway REST access-control config-perspective-branding API
  slug: open-inductive-automation-config-perspective-branding-api
- collection_type: open
  name: Ignition Gateway REST access-control config-perspective-fonts API
  slug: open-inductive-automation-config-perspective-fonts-api
- collection_type: open
  name: Ignition Gateway REST access-control config-perspective-icons API
  slug: open-inductive-automation-config-perspective-icons-api
- collection_type: open
  name: Ignition Gateway REST access-control config-perspective-themes API
  slug: open-inductive-automation-config-perspective-themes-api
- collection_type: open
  name: Ignition Gateway REST access-control config-secret-provider API
  slug: open-inductive-automation-config-secret-provider-api
- collection_type: open
  name: Ignition Gateway REST access-control config-security-levels API
  slug: open-inductive-automation-config-security-levels-api
- collection_type: open
  name: Ignition Gateway REST access-control config-security-properties API
  slug: open-inductive-automation-config-security-properties-api
- collection_type: open
  name: Ignition Gateway REST access-control config-security-zone API
  slug: open-inductive-automation-config-security-zone-api
- collection_type: open
  name: Ignition Gateway REST access-control config-store-forward API
  slug: open-inductive-automation-config-store-forward-api
- collection_type: open
  name: Ignition Gateway REST access-control config-system-properties API
  slug: open-inductive-automation-config-system-properties-api
- collection_type: open
  name: Ignition Gateway REST access-control config-tag-provider API
  slug: open-inductive-automation-config-tag-provider-api
- collection_type: open
  name: Ignition Gateway REST access-control config-translations API
  slug: open-inductive-automation-config-translations-api
- collection_type: open
  name: Ignition Gateway REST access-control config-user-source API
  slug: open-inductive-automation-config-user-source-api
- collection_type: open
  name: Ignition Gateway REST access-control data-syncs API
  slug: open-inductive-automation-data-syncs-api
- collection_type: open
  name: Ignition Gateway REST access-control designer-sessions API
  slug: open-inductive-automation-designer-sessions-api
- collection_type: open
  name: Ignition Gateway REST access-control device API
  slug: open-inductive-automation-device-api
- collection_type: open
  name: Ignition Gateway REST access-control eam-tasks API
  slug: open-inductive-automation-eam-tasks-api
- collection_type: open
  name: Ignition Gateway REST access-control encryption API
  slug: open-inductive-automation-encryption-api
- collection_type: open
  name: Ignition Gateway REST access-control entity API
  slug: open-inductive-automation-entity-api
- collection_type: open
  name: Ignition Gateway REST access-control event-thresholds API
  slug: open-inductive-automation-event-thresholds-api
- collection_type: open
  name: Ignition Gateway REST access-control executors API
  slug: open-inductive-automation-executors-api
- collection_type: open
  name: Ignition Gateway REST access-control gateway-backups API
  slug: open-inductive-automation-gateway-backups-api
- collection_type: open
  name: Ignition Gateway REST access-control gateway-info API
  slug: open-inductive-automation-gateway-info-api
- collection_type: open
  name: Ignition Gateway REST access-control gateway-network API
  slug: open-inductive-automation-gateway-network-api
- collection_type: open
  name: Ignition Gateway REST access-control gateway-scripts API
  slug: open-inductive-automation-gateway-scripts-api
- collection_type: open
  name: Ignition Gateway REST access-control general-alarm-settings API
  slug: open-inductive-automation-general-alarm-settings-api
- collection_type: open
  name: Ignition Gateway REST access-control general API
  slug: open-inductive-automation-general-api
- collection_type: open
  name: Ignition Gateway REST access-control groups-info API
  slug: open-inductive-automation-groups-info-api
- collection_type: open
  name: Ignition Gateway REST access-control historian-config API
  slug: open-inductive-automation-historian-config-api
- collection_type: open
  name: Ignition Gateway REST access-control launcher API
  slug: open-inductive-automation-launcher-api
- collection_type: open
  name: Ignition Gateway REST access-control license-activation API
  slug: open-inductive-automation-license-activation-api
- collection_type: open
  name: Ignition Gateway REST access-control license-management API
  slug: open-inductive-automation-license-management-api
- collection_type: open
  name: Ignition Gateway REST access-control license-status API
  slug: open-inductive-automation-license-status-api
- collection_type: open
  name: Ignition Gateway REST access-control local devices API
  slug: open-inductive-automation-local-devices-api
- collection_type: open
  name: Ignition Gateway REST access-control logging API
  slug: open-inductive-automation-logging-api
- collection_type: open
  name: Ignition Gateway REST access-control managed-tag-provider API
  slug: open-inductive-automation-managed-tag-provider-api
- collection_type: open
  name: Ignition Gateway REST access-control module-certificate API
  slug: open-inductive-automation-module-certificate-api
- collection_type: open
  name: Ignition Gateway REST access-control module-eula API
  slug: open-inductive-automation-module-eula-api
- collection_type: open
  name: Ignition Gateway REST access-control module-settings API
  slug: open-inductive-automation-module-settings-api
- collection_type: open
  name: Ignition Gateway REST access-control modules API
  slug: open-inductive-automation-modules-api
- collection_type: open
  name: Ignition Gateway REST access-control opc connection API
  slug: open-inductive-automation-opc-connection-api
- collection_type: open
  name: Ignition Gateway REST access-control overview API
  slug: open-inductive-automation-overview-api
- collection_type: open
  name: Ignition Gateway REST access-control perspective-sessions API
  slug: open-inductive-automation-perspective-sessions-api
- collection_type: open
  name: Ignition Gateway REST access-control pipeline-status API
  slug: open-inductive-automation-pipeline-status-api
- collection_type: open
  name: Ignition Gateway REST access-control projects API
  slug: open-inductive-automation-projects-api
- collection_type: open
  name: Ignition Gateway REST access-control quickstart API
  slug: open-inductive-automation-quickstart-api
- collection_type: open
  name: Ignition Gateway REST access-control redundancy API
  slug: open-inductive-automation-redundancy-api
- collection_type: open
  name: Ignition Gateway REST access-control remote-upgrade API
  slug: open-inductive-automation-remote-upgrade-api
- collection_type: open
  name: Ignition Gateway REST access-control reports-info API
  slug: open-inductive-automation-reports-info-api
- collection_type: open
  name: Ignition Gateway REST access-control restart-tasks API
  slug: open-inductive-automation-restart-tasks-api
- collection_type: open
  name: Ignition Gateway REST access-control roster-config API
  slug: open-inductive-automation-roster-config-api
- collection_type: open
  name: Ignition Gateway REST access-control running-scripts API
  slug: open-inductive-automation-running-scripts-api
- collection_type: open
  name: Ignition Gateway REST access-control secret-providers API
  slug: open-inductive-automation-secret-providers-api
- collection_type: open
  name: Ignition Gateway REST access-control server API
  slug: open-inductive-automation-server-api
- collection_type: open
  name: Ignition Gateway REST access-control server-pki-certificate-management API
  slug: open-inductive-automation-server-pki-certificate-management-api
- collection_type: open
  name: Ignition Gateway REST access-control service-connectors API
  slug: open-inductive-automation-service-connectors-api
- collection_type: open
  name: Ignition Gateway REST access-control sfc-config API
  slug: open-inductive-automation-sfc-config-api
- collection_type: open
  name: Ignition Gateway REST access-control storage API
  slug: open-inductive-automation-storage-api
- collection_type: open
  name: Ignition Gateway REST access-control streams-info API
  slug: open-inductive-automation-streams-info-api
- collection_type: open
  name: Ignition Gateway REST access-control system-performance API
  slug: open-inductive-automation-system-performance-api
- collection_type: open
  name: Ignition Gateway REST access-control thread-diagnostics API
  slug: open-inductive-automation-thread-diagnostics-api
- collection_type: open
  name: Ignition Gateway REST access-control user-management-scim API
  slug: open-inductive-automation-user-management-scim-api
- collection_type: open
  name: Ignition Gateway REST access-control vision-sessions API
  slug: open-inductive-automation-vision-sessions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/inductive-automation-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/inductive-automation-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/inductive-automation-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/inductive-automation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inductive-automation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inductive-automation-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://inductiveautomation.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.docs.inductiveautomation.com/
- group: start
  title: ''
  type: Portal
  url: https://inductiveautomation.com/moduleshowcase/api-docs
- group: company
  title: ''
  type: Blog
  url: https://inductiveautomation.com/resources/article
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inductiveautomation
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inductive-automation
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@InductiveAutomation
- group: commercial
  title: ''
  type: Pricing
  url: https://inductiveautomation.com/pricing/
- group: company
  title: ''
  type: About
  url: https://inductiveautomation.com/about-inductive-automation
- group: operate
  title: ''
  type: Support
  url: https://support.inductiveautomation.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://inductiveautomation.com/ignition/trial/
created: '2026-06-05'
description: Inductive Automation is the developer of Ignition, an industrial application platform used for SCADA, HMI, MES, and IIoT deployments across manufacturing, utilities, and infrastructure. Ignition 8.3 exposes an OpenAPI-compliant REST API through its Gateway that provides programmatic access to configuration, tags, projects, and modules, enabling containerized and cloud-native industrial automation deployments.
examples:
- key_count: 2
  name: Inductive Automation Create Database Connection Example
  slug: inductive-automation-create-database-connection-example
- key_count: 2
  name: Inductive Automation Gateway Info Example
  slug: inductive-automation-gateway-info-example
- key_count: 2
  name: Inductive Automation List Projects Example
  slug: inductive-automation-list-projects-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/inductive-automation.png
json_schemas:
- name: GatewayInfo
  property_count: 7
  slug: inductive-automation-gateway-info
- name: ResourceRecord
  property_count: 7
  slug: inductive-automation-resource-record
- name: ScimUser
  property_count: 12
  slug: inductive-automation-scim-user
json_structures:
- name: Inductive Automation Gateway Info Structure
  property_count: 0
  slug: inductive-automation-gateway-info-structure
- name: Inductive Automation Resource Record Structure
  property_count: 0
  slug: inductive-automation-resource-record-structure
jsonld:
- class_count: 34
  name: Inductive Automation Context
  property_count: 19
  slug: inductive-automation-context
layout: provider
modified: '2026-06-05'
name: Inductive Automation
nav: Providers
network: true
overview: 'Inductive Automation publishes 87 APIs on the [APIs.io](https://apis.io/) network, including access-control API, agent-group API, agent-management API, and 84 more. Tagged areas include SCADA, HMI, Manufacturing, IIoT, and Industrial Automation.


  The Inductive Automation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Inductive Automation''s developer surface includes authentication, documentation, developer portal, engineering blog, YouTube channel, pricing, support, and 10 more developer resources.'
random_paper: 5
rules:
- effective_rule_count: 5
  extends: []
  name: Inductive Automation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: inductive-automation-jsonschema-spectral-rules
- effective_rule_count: 8
  extends: []
  name: Inductive Automation API Rules
  rule_count: 8
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 5
  slug: inductive-automation-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 14
    catalog_gap: 66.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 9.8
    contract_quality: 63.4
    developer_ergonomics: 38.1
    discoverability: 63.0
    governance: 9.8
    operational_transparency: 2.6
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 87
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inductive-automation/refs/heads/main/screenshots/inductive-automation-2026-06-20T183324.png
security:
- kind: authentication
  name: Inductive Automation Authentication
  slug: inductive-automation-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Inductive Automation Domain Security
  slug: inductive-automation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Inductive Automation Vulnerability Disclosure
  slug: inductive-automation-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Inductive Automation Trust Center
  slug: inductive-automation-trust-center
  summary_line: ISO 27001
slug: inductive-automation
tags:
- SCADA
- HMI
- Manufacturing
- IIoT
- Industrial Automation
- Industrial IoT
- OPC UA
website: https://inductiveautomation.com
---
