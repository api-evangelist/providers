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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 272
  human_in_the_loop: 29
  name: Tenable Agentic Access
  operation_count: 553
  slug: tenable-agentic-access
  summary_line: 553 operations · 272 acting · 29 human-in-the-loop
api_count: 107
apis:
- description: Provide general information on Eridanis
  name: Tenable About API
  slug: tenable-about-api
- description: The Access Control (API) API from Tenable — 1 operation(s) for access control (api).
  name: Tenable Access Control (API) API
  slug: tenable-access-control-api-api
- description: The Access Control (Groups) API from Tenable — 4 operation(s) for access control (groups).
  name: Tenable Access Control (Groups) API
  slug: tenable-access-control-groups-api
- description: The Access Control (Permissions) API from Tenable — 5 operation(s) for access control (permissions).
  name: Tenable Access Control (Permissions) API
  slug: tenable-access-control-permissions-api
- description: The Access Control (Roles) API from Tenable — 3 operation(s) for access control (roles).
  name: Tenable Access Control (Roles) API
  slug: tenable-access-control-roles-api
- description: The Access Control (Users) API from Tenable — 10 operation(s) for access control (users).
  name: Tenable Access Control (Users) API
  slug: tenable-access-control-users-api
- description: The Access Groups v1 API from Tenable — 4 operation(s) for access groups v1.
  name: Tenable Access Groups v1 API
  slug: tenable-access-groups-v1-api
- description: The Access Groups v2 API from Tenable — 4 operation(s) for access groups v2.
  name: Tenable Access Groups v2 API
  slug: tenable-access-groups-v2-api
- description: The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage and maintain multiple customer instances of Tenable products. The
  name: Tenable Account Groups API
  slug: tenable-account-groups-api
- description: The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage and maintain multiple customer instances of Tenable products. Acc
  name: Tenable Accounts API
  slug: tenable-accounts-api
- description: The Activity Log API from Tenable — 1 operation(s) for activity log.
  name: Tenable Activity Log API
  slug: tenable-activity-log-api
- description: Representation of an Active Directory Object
  name: Tenable AD object API
  slug: tenable-ad-object-api
- description: The Agent Config API from Tenable — 1 operation(s) for agent config.
  name: Tenable Agent Config API
  slug: tenable-agent-config-api
- description: The Agent Exclusions API from Tenable — 2 operation(s) for agent exclusions.
  name: Tenable Agent Exclusions API
  slug: tenable-agent-exclusions-api
- description: The Agent Groups API from Tenable — 3 operation(s) for agent groups.
  name: Tenable Agent Groups API
  slug: tenable-agent-groups-api
- description: The Agent Tasks API from Tenable — 10 operation(s) for agent tasks.
  name: Tenable Agent Tasks API
  slug: tenable-agent-tasks-api
- description: The Agents API from Tenable — 4 operation(s) for agents.
  name: Tenable Agents API
  slug: tenable-agents-api
- description: New deviances alert
  name: Tenable Alert API
  slug: tenable-alert-api
- description: Token to programmatically access Eridanis
  name: Tenable API key API
  slug: tenable-api-key-api
- description: Tenable.ad global configuration
  name: Tenable Application setting API
  slug: tenable-application-setting-api
- description: With the WAS Applications API, you can create web application assets. For more information, see the [Targets](https://docs.tenable.com/web-app-scanning/Content/WAS/Scans/BasicSettings.htm#Targets) sec
  name: Tenable Applications API
  slug: tenable-applications-api
- description: The Asset Attributes API from Tenable — 4 operation(s) for asset attributes.
  name: Tenable Asset Attributes API
  slug: tenable-asset-attributes-api
- description: The Assets API from Tenable — 8 operation(s) for assets.
  name: Tenable Assets API
  slug: tenable-assets-api
- description: With the Attachments API, you can download auxiliary files generated by plugins during a scan. These attachments provide forensic evidence and deeper context for identified vulnerabilities. For more i
  name: Tenable Attachments API
  slug: tenable-attachments-api
- description: Attacks as detected by Tenable.ad
  name: Tenable Attack API
  slug: tenable-attack-api
- description: 'The Tenable Attack Path API enables users to retrieve details about attack path findings and attack path vectors. A Finding is an attack technique that exists in one or more attack paths that lead to '
  name: Tenable Attack Path API
  slug: tenable-attack-path-api
- description: The Tenable Attack Path Exports API enables users to export top attack paths, attack technique data, and MITRE ATT&CK heatmap data in JSON or CSV format. MITRE heatmap exports in JSON conform to the M
  name: Tenable Attack Path Exports API
  slug: tenable-attack-path-exports-api
- description: Attack types
  name: Tenable Attack type API
  slug: tenable-attack-type-api
- description: The attack type per directory configuration
  name: Tenable Attack type configuration API
  slug: tenable-attack-type-configuration-api
- description: Security profile options relative to attack types (Indicator of Attacks)
  name: Tenable Attack type option API
  slug: tenable-attack-type-option-api
- description: After you submit a scan to Tenable for ASV review, you can use the Tenable PCI ASV API to retrieve a list of your attestations and see your current attestation request status. For more information, se
  name: Tenable Attestations API
  slug: tenable-attestations-api
- description: A checker's category
  name: Tenable Category API
  slug: tenable-category-api
- description: Checkers are the implementations of the state of the art of AD security
  name: Tenable Checker API
  slug: tenable-checker-api
- description: Security profile options relative to checkers (Indicator of Exposure)
  name: Tenable Checker option API
  slug: tenable-checker-option-api
- description: The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage and maintain multiple customer instances of Tenable products. Chi
  name: Tenable Child Containers API
  slug: tenable-child-containers-api
- description: The Cloud Connectors API from Tenable — 6 operation(s) for cloud connectors.
  name: Tenable Cloud Connectors API
  slug: tenable-cloud-connectors-api
- description: Attributes sent to tenable cloud statistics
  name: Tenable Cloud statistics API
  slug: tenable-cloud-statistics-api
- description: With the Configurations API, you can create and maintain reusable scan settings. These endpoints allow you to perform standard CRUD operations on configuration objects to standardize scanning across y
  name: Tenable Configurations API
  slug: tenable-configurations-api
- description: The Credentials API from Tenable — 4 operation(s) for credentials.
  name: Tenable Credentials API
  slug: tenable-credentials-api
- description: A widget container
  name: Tenable Dashboard API
  slug: tenable-dashboard-api
- description: The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage and maintain multiple customer instances of Tenable products. Das
  name: Tenable Dashboards API
  slug: tenable-dashboards-api
- description: Security deviance items
  name: Tenable Deviance API
  slug: tenable-deviance-api
- description: Represents an Active directory
  name: Tenable Directory API
  slug: tenable-directory-api
- description: The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage and maintain multiple customer instances of Tenable products. Dom
  name: Tenable Domains API
  slug: tenable-domains-api
- description: The Downloads API enables customers to access and download installation and update files for available Tenable products. You can use the API endpoints to list product pages, list downloads available f
  name: Tenable Downloads API
  slug: tenable-downloads-api
- description: The Editor API from Tenable — 5 operation(s) for editor.
  name: Tenable Editor API
  slug: tenable-editor-api
- description: An email notification about new deviances
  name: Tenable Email notifier API
  slug: tenable-email-notifier-api
- description: A change in the Active Directory
  name: Tenable Event API
  slug: tenable-event-api
- description: The Exclusions API from Tenable — 3 operation(s) for exclusions.
  name: Tenable Exclusions API
  slug: tenable-exclusions-api
- description: With the Exports API, you can manage asynchronous finding exports. Use these endpoints to initiate export jobs, monitor status, and download results in chunks for integration with external workflow ma
  name: Tenable Exports API
  slug: tenable-exports-api
- description: The Exports (Assets) API from Tenable — 6 operation(s) for exports (assets).
  name: Tenable Exports (Assets) API
  slug: tenable-exports-assets-api
- description: The Exports (Compliance Data) API from Tenable — 5 operation(s) for exports (compliance data).
  name: Tenable Exports (Compliance Data) API
  slug: tenable-exports-compliance-data-api
- description: The Exports (Vulnerabilities) API from Tenable — 5 operation(s) for exports (vulnerabilities).
  name: Tenable Exports (Vulnerabilities) API
  slug: tenable-exports-vulnerabilities-api
- description: The Tenable Exposure View API enables users to search Tenable Exposure view for their organization's cards or retrieve the details for a specified card. For more information about Exposure View, see [
  name: Tenable Exposure View API
  slug: tenable-exposure-view-api
- description: The File API from Tenable — 1 operation(s) for file.
  name: Tenable File API
  slug: tenable-file-api
- description: The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage and maintain multiple customer instances of Tenable products. Fil
  name: Tenable Filters API
  slug: tenable-filters-api
- description: The Folders API from Tenable — 4 operation(s) for folders.
  name: Tenable Folders API
  slug: tenable-folders-api
- description: A groupment of directories
  name: Tenable Infrastructure API
  slug: tenable-infrastructure-api
- description: The Tenable Inventory API enables users to search for their organization's assets and the software installed on those assets. Additionally, API endpoints are provided to retrieve a list of asset and s
  name: Tenable Inventory API
  slug: tenable-inventory-api
- description: The Tenable Inventory Exports API enables users to export inventory assets and findings in JSON or CSV format. For more information about exporting assets and findings from Tenable Exposure Management
  name: Tenable Inventory Exports API
  slug: tenable-inventory-exports-api
- description: Configuration of LDAP for authentication purposes.
  name: Tenable LDAP configuration API
  slug: tenable-ldap-configuration-api
- description: Product license
  name: Tenable License API
  slug: tenable-license-api
- description: Configuration of the mechanism that locks out user accounts after multiple failed login attempts.
  name: Tenable Lockout policy API
  slug: tenable-lockout-policy-api
- description: 'The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage the logos of their customer''s instances. By default, the Tenable '
  name: Tenable Logos API
  slug: tenable-logos-api
- description: The Metrics API from Tenable — 1 operation(s) for metrics.
  name: Tenable Metrics API
  slug: tenable-metrics-api
- description: The Networks API from Tenable — 6 operation(s) for networks.
  name: Tenable Networks API
  slug: tenable-networks-api
- description: The OT Connectors API from Tenable — 4 operation(s) for ot connectors.
  name: Tenable OT Connectors API
  slug: tenable-ot-connectors-api
- description: 'The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage their partner information. Partner endpoints in the Tenable MSSP '
  name: Tenable Partners API
  slug: tenable-partners-api
- description: The Permissions API from Tenable — 1 operation(s) for permissions.
  name: Tenable Permissions API
  slug: tenable-permissions-api
- description: The Plugins API from Tenable — 7 operation(s) for plugins.
  name: Tenable Plugins API
  slug: tenable-plugins-api
- description: The Policies API from Tenable — 5 operation(s) for policies.
  name: Tenable Policies API
  slug: tenable-policies-api
- description: A user's preferences
  name: Tenable Preference API
  slug: tenable-preference-api
- description: A set of Checker option value
  name: Tenable Profile API
  slug: tenable-profile-api
- description: The Profiles API from Tenable — 4 operation(s) for profiles.
  name: Tenable Profiles API
  slug: tenable-profiles-api
- description: The reason why a AD object is marked as deviant
  name: Tenable Reason API
  slug: tenable-reason-api
- description: The Recast Rules API from Tenable — 4 operation(s) for recast rules.
  name: Tenable Recast Rules API
  slug: tenable-recast-rules-api
- description: Configure relays that make AD queries for Ceti
  name: Tenable Relay API
  slug: tenable-relay-api
- description: The Remediation Scans API from Tenable — 1 operation(s) for remediation scans.
  name: Tenable Remediation Scans API
  slug: tenable-remediation-scans-api
- description: Token to access the reports download
  name: Tenable Report access token API
  slug: tenable-report-access-token-api
- description: The Reports API from Tenable — 3 operation(s) for reports.
  name: Tenable Reports API
  slug: tenable-reports-api
- description: The Tenable Managed Security Service Provider (MSSP) Portal API provides a secure and accessible way for MSSP administrators to manage and maintain multiple customer instances of Tenable products. Res
  name: Tenable Resource Links API
  slug: tenable-resource-links-api
- description: Groupment of permissions that may be assigned to several users
  name: Tenable Role API
  slug: tenable-role-api
- description: Authentification configuration with SAML
  name: Tenable SAML configuration API
  slug: tenable-saml-configuration-api
- description: The Scan Control API from Tenable — 5 operation(s) for scan control.
  name: Tenable Scan Control API
  slug: tenable-scan-control-api
- description: The Scan Exports API from Tenable — 4 operation(s) for scan exports.
  name: Tenable Scan Exports API
  slug: tenable-scan-exports-api
- description: The Scan History API from Tenable — 2 operation(s) for scan history.
  name: Tenable Scan History API
  slug: tenable-scan-history-api
- description: The Scan Results API from Tenable — 3 operation(s) for scan results.
  name: Tenable Scan Results API
  slug: tenable-scan-results-api
- description: The Scan Status API from Tenable — 3 operation(s) for scan status.
  name: Tenable Scan Status API
  slug: tenable-scan-status-api
- description: The Scan Tasks API from Tenable — 7 operation(s) for scan tasks.
  name: Tenable Scan Tasks API
  slug: tenable-scan-tasks-api
- description: The Scanner Config API from Tenable — 1 operation(s) for scanner config.
  name: Tenable Scanner Config API
  slug: tenable-scanner-config-api
- description: The Scanner Groups API from Tenable — 5 operation(s) for scanner groups.
  name: Tenable Scanner Groups API
  slug: tenable-scanner-groups-api
- description: The Scanner Profiles API from Tenable — 2 operation(s) for scanner profiles.
  name: Tenable Scanner Profiles API
  slug: tenable-scanner-profiles-api
- description: The Scanner Tasks API from Tenable — 4 operation(s) for scanner tasks.
  name: Tenable Scanner Tasks API
  slug: tenable-scanner-tasks-api
- description: The Scanners API from Tenable — 5 operation(s) for scanners.
  name: Tenable Scanners API
  slug: tenable-scanners-api
- description: The Scans API from Tenable — 11 operation(s) for scans.
  name: Tenable Scans API
  slug: tenable-scans-api
- description: The directories' scores
  name: Tenable Score API
  slug: tenable-score-api
- description: The Server API from Tenable — 2 operation(s) for server.
  name: Tenable Server API
  slug: tenable-server-api
- description: The Shared Collections API from Tenable — 5 operation(s) for shared collections.
  name: Tenable Shared Collections API
  slug: tenable-shared-collections-api
- description: A syslog alert
  name: Tenable Syslog API
  slug: tenable-syslog-api
- description: The Tenable Exposure Management tags API enables users to search for their organization's tags. Additionally, API endpoints are provided to retrieve a list of asset and tag properties that can be used
  name: Tenable Tags API
  slug: tenable-tags-api
- description: The Target Groups API from Tenable — 3 operation(s) for target groups.
  name: Tenable Target Groups API
  slug: tenable-target-groups-api
- description: With the Templates API, you can manage scan and user templates. Use these endpoints to retrieve default settings or create custom templates based on organizational policies. Templates serve as the blu
  name: Tenable Templates API
  slug: tenable-templates-api
- description: A graph to represent the trust relationships between different Active Directories
  name: Tenable Topology API
  slug: tenable-topology-api
- description: A Tenable.ad user
  name: Tenable User API
  slug: tenable-user-api
- description: The Vulnerabilities API from Tenable — 4 operation(s) for vulnerabilities.
  name: Tenable Vulnerabilities API
  slug: tenable-vulnerabilities-api
- description: Contains a serie of data
  name: Tenable Widget API
  slug: tenable-widget-api
- description: The Workbenches API from Tenable — 14 operation(s) for workbenches.
  name: Tenable Workbenches API
  slug: tenable-workbenches-api
artifact_total: 221
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Downloads About API
  slug: open-tenable-about-api
- collection_type: open
  name: Downloads About Access Control (API) API
  slug: open-tenable-access-control-api-api
- collection_type: open
  name: Downloads About Access Control (Groups) API
  slug: open-tenable-access-control-groups-api
- collection_type: open
  name: Downloads About Access Control (Permissions) API
  slug: open-tenable-access-control-permissions-api
- collection_type: open
  name: Downloads About Access Control (Roles) API
  slug: open-tenable-access-control-roles-api
- collection_type: open
  name: Downloads About Access Control (Users) API
  slug: open-tenable-access-control-users-api
- collection_type: open
  name: Downloads About Access Groups v1 API
  slug: open-tenable-access-groups-v1-api
- collection_type: open
  name: Downloads About Access Groups v2 API
  slug: open-tenable-access-groups-v2-api
- collection_type: open
  name: Downloads About Account Groups API
  slug: open-tenable-account-groups-api
- collection_type: open
  name: Downloads About Accounts API
  slug: open-tenable-accounts-api
- collection_type: open
  name: Downloads About Activity Log API
  slug: open-tenable-activity-log-api
- collection_type: open
  name: Downloads About AD object API
  slug: open-tenable-ad-object-api
- collection_type: open
  name: Downloads About Agent Config API
  slug: open-tenable-agent-config-api
- collection_type: open
  name: Downloads About Agent Exclusions API
  slug: open-tenable-agent-exclusions-api
- collection_type: open
  name: Downloads About Agent Groups API
  slug: open-tenable-agent-groups-api
- collection_type: open
  name: Downloads About Agent Tasks API
  slug: open-tenable-agent-tasks-api
- collection_type: open
  name: Downloads About Agents API
  slug: open-tenable-agents-api
- collection_type: open
  name: Downloads About Alert API
  slug: open-tenable-alert-api
- collection_type: open
  name: Downloads About API key API
  slug: open-tenable-api-key-api
- collection_type: open
  name: Downloads About Application setting API
  slug: open-tenable-application-setting-api
- collection_type: open
  name: Downloads About Applications API
  slug: open-tenable-applications-api
- collection_type: open
  name: Downloads About Asset Attributes API
  slug: open-tenable-asset-attributes-api
- collection_type: open
  name: Downloads About Assets API
  slug: open-tenable-assets-api
- collection_type: open
  name: Downloads About Attachments API
  slug: open-tenable-attachments-api
- collection_type: open
  name: Downloads About Attack API
  slug: open-tenable-attack-api
- collection_type: open
  name: Downloads About Attack Path API
  slug: open-tenable-attack-path-api
- collection_type: open
  name: Downloads About Attack Path Exports API
  slug: open-tenable-attack-path-exports-api
- collection_type: open
  name: Downloads About Attack type API
  slug: open-tenable-attack-type-api
- collection_type: open
  name: Downloads About Attack type configuration API
  slug: open-tenable-attack-type-configuration-api
- collection_type: open
  name: Downloads About Attack type option API
  slug: open-tenable-attack-type-option-api
- collection_type: open
  name: Downloads About Attestations API
  slug: open-tenable-attestations-api
- collection_type: open
  name: Downloads About Category API
  slug: open-tenable-category-api
- collection_type: open
  name: Downloads About Checker API
  slug: open-tenable-checker-api
- collection_type: open
  name: Downloads About Checker option API
  slug: open-tenable-checker-option-api
- collection_type: open
  name: Downloads About Child Containers API
  slug: open-tenable-child-containers-api
- collection_type: open
  name: Downloads About Cloud Connectors API
  slug: open-tenable-cloud-connectors-api
- collection_type: open
  name: Downloads About Cloud statistics API
  slug: open-tenable-cloud-statistics-api
- collection_type: open
  name: Downloads About Configurations API
  slug: open-tenable-configurations-api
- collection_type: open
  name: Downloads About Credentials API
  slug: open-tenable-credentials-api
- collection_type: open
  name: Downloads About Dashboard API
  slug: open-tenable-dashboard-api
- collection_type: open
  name: Downloads About Dashboards API
  slug: open-tenable-dashboards-api
- collection_type: open
  name: Downloads About Deviance API
  slug: open-tenable-deviance-api
- collection_type: open
  name: Downloads About Directory API
  slug: open-tenable-directory-api
- collection_type: open
  name: Downloads About Domains API
  slug: open-tenable-domains-api
- collection_type: open
  name: About Downloads API
  slug: open-tenable-downloads-api
- collection_type: open
  name: Downloads About Editor API
  slug: open-tenable-editor-api
- collection_type: open
  name: Downloads About Email notifier API
  slug: open-tenable-email-notifier-api
- collection_type: open
  name: Downloads About Event API
  slug: open-tenable-event-api
- collection_type: open
  name: Downloads About Exclusions API
  slug: open-tenable-exclusions-api
- collection_type: open
  name: Downloads About Exports API
  slug: open-tenable-exports-api
- collection_type: open
  name: Downloads About Exports (Assets) API
  slug: open-tenable-exports-assets-api
- collection_type: open
  name: Downloads About Exports (Compliance Data) API
  slug: open-tenable-exports-compliance-data-api
- collection_type: open
  name: Downloads About Exports (Vulnerabilities) API
  slug: open-tenable-exports-vulnerabilities-api
- collection_type: open
  name: Downloads About Exposure View API
  slug: open-tenable-exposure-view-api
- collection_type: open
  name: Downloads About File API
  slug: open-tenable-file-api
- collection_type: open
  name: Downloads About Filters API
  slug: open-tenable-filters-api
- collection_type: open
  name: Downloads About Folders API
  slug: open-tenable-folders-api
- collection_type: open
  name: Downloads About Infrastructure API
  slug: open-tenable-infrastructure-api
- collection_type: open
  name: Downloads About Inventory API
  slug: open-tenable-inventory-api
- collection_type: open
  name: Downloads About Inventory Exports API
  slug: open-tenable-inventory-exports-api
- collection_type: open
  name: Downloads About LDAP configuration API
  slug: open-tenable-ldap-configuration-api
- collection_type: open
  name: Downloads About License API
  slug: open-tenable-license-api
- collection_type: open
  name: Downloads About Lockout policy API
  slug: open-tenable-lockout-policy-api
- collection_type: open
  name: Downloads About Logos API
  slug: open-tenable-logos-api
- collection_type: open
  name: Downloads About Metrics API
  slug: open-tenable-metrics-api
- collection_type: open
  name: Downloads About Networks API
  slug: open-tenable-networks-api
- collection_type: open
  name: Downloads About OT Connectors API
  slug: open-tenable-ot-connectors-api
- collection_type: open
  name: Downloads About Partners API
  slug: open-tenable-partners-api
- collection_type: open
  name: Downloads About Permissions API
  slug: open-tenable-permissions-api
- collection_type: open
  name: Downloads About Plugins API
  slug: open-tenable-plugins-api
- collection_type: open
  name: Downloads About Policies API
  slug: open-tenable-policies-api
- collection_type: open
  name: Downloads About Preference API
  slug: open-tenable-preference-api
- collection_type: open
  name: Downloads About Profile API
  slug: open-tenable-profile-api
- collection_type: open
  name: Downloads About Profiles API
  slug: open-tenable-profiles-api
- collection_type: open
  name: Downloads About Reason API
  slug: open-tenable-reason-api
- collection_type: open
  name: Downloads About Recast Rules API
  slug: open-tenable-recast-rules-api
- collection_type: open
  name: Downloads About Relay API
  slug: open-tenable-relay-api
- collection_type: open
  name: Downloads About Remediation Scans API
  slug: open-tenable-remediation-scans-api
- collection_type: open
  name: Downloads About Report access token API
  slug: open-tenable-report-access-token-api
- collection_type: open
  name: Downloads About Reports API
  slug: open-tenable-reports-api
- collection_type: open
  name: Downloads About Resource Links API
  slug: open-tenable-resource-links-api
- collection_type: open
  name: Downloads About Role API
  slug: open-tenable-role-api
- collection_type: open
  name: Downloads About SAML configuration API
  slug: open-tenable-saml-configuration-api
- collection_type: open
  name: Downloads About Scan Control API
  slug: open-tenable-scan-control-api
- collection_type: open
  name: Downloads About Scan Exports API
  slug: open-tenable-scan-exports-api
- collection_type: open
  name: Downloads About Scan History API
  slug: open-tenable-scan-history-api
- collection_type: open
  name: Downloads About Scan Results API
  slug: open-tenable-scan-results-api
- collection_type: open
  name: Downloads About Scan Status API
  slug: open-tenable-scan-status-api
- collection_type: open
  name: Downloads About Scan Tasks API
  slug: open-tenable-scan-tasks-api
- collection_type: open
  name: Downloads About Scanner Config API
  slug: open-tenable-scanner-config-api
- collection_type: open
  name: Downloads About Scanner Groups API
  slug: open-tenable-scanner-groups-api
- collection_type: open
  name: Downloads About Scanner Profiles API
  slug: open-tenable-scanner-profiles-api
- collection_type: open
  name: Downloads About Scanner Tasks API
  slug: open-tenable-scanner-tasks-api
- collection_type: open
  name: Downloads About Scanners API
  slug: open-tenable-scanners-api
- collection_type: open
  name: Downloads About Scans API
  slug: open-tenable-scans-api
- collection_type: open
  name: Downloads About Score API
  slug: open-tenable-score-api
- collection_type: open
  name: Downloads About Server API
  slug: open-tenable-server-api
- collection_type: open
  name: Downloads About Shared Collections API
  slug: open-tenable-shared-collections-api
- collection_type: open
  name: Downloads About Syslog API
  slug: open-tenable-syslog-api
- collection_type: open
  name: Downloads About Tags API
  slug: open-tenable-tags-api
- collection_type: open
  name: Downloads About Target Groups API
  slug: open-tenable-target-groups-api
- collection_type: open
  name: Downloads About Templates API
  slug: open-tenable-templates-api
- collection_type: open
  name: Downloads About Topology API
  slug: open-tenable-topology-api
- collection_type: open
  name: Downloads About User API
  slug: open-tenable-user-api
- collection_type: open
  name: Downloads About Vulnerabilities API
  slug: open-tenable-vulnerabilities-api
- collection_type: open
  name: Downloads About Widget API
  slug: open-tenable-widget-api
- collection_type: open
  name: Downloads About Workbenches API
  slug: open-tenable-workbenches-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/tenable-downloads-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.tenable.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.tenable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tenable.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.tenable.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.tenable.com/docs/welcome
- group: operate
  title: ''
  type: Support
  url: https://www.tenable.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.tenable.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tenable
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tenable.com/buy
- group: start
  title: ''
  type: SignUp
  url: https://www.tenable.com/evaluate
- group: start
  title: ''
  type: Login
  url: https://cloud.tenable.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tenable.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tenable.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tenable-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tenable.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.tenable.com/changelog
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tenable-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tenable-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tenable-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tenable-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tenable-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tenable-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.tenable.com/trust/assurance
- group: auth
  title: ''
  type: TrustCenter
  url: security/tenable-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tenable.com/security/report
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tenable-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tenable-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tenable-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/tenable-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tenable-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tenable-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tenable-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tenable-agentic-access.yml
created: '2026-07-17'
description: Tenable is a cybersecurity and exposure-management company, maker of Nessus and the Tenable One platform, providing vulnerability management, web application scanning, cloud security, identity exposure, attack surface management and OT security. Its developer platform (developer.tenable.com) exposes eight OpenAPI 3 REST APIs on cloud.tenable.com covering Vulnerability Management, Web App Scanning, Exposure Management, Platform & Settings, PCI ASV, MSSP, Identity Exposure and Downloads, all authenticated with X-ApiKeys access/secret keys, plus the official pyTenable SDK and a Tenable-hosted Hexa AI MCP server.
image: https://www.tenable.com/sites/all/themes/tenable/logo.svg
layout: provider
mcp_servers:
- description: Tenable-hosted remote MCP server exposing ~90 structured tools from Tenable's Exposure Data Fabric to any MCP-compatible client (Claude Desktop, Claude Code, Cursor). Lets an AI assistant search asset
  name: Tenable Hexa AI MCP Server
  slug: tenable-hexa-ai-mcp-server
modified: '2026-07-21'
name: Tenable
nav: Providers
network: true
overview: 'Tenable publishes 107 APIs on the [APIs.io](https://apis.io/) network, including About API, Access Control (API) API, Access Control (Groups) API, and 104 more. Tagged areas include Company, Enterprise, Cybersecurity, Vulnerability Management, and Exposure Management.


  Tenable''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
random_paper: 17
score:
  band: strong
  composite: 54.7
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 16.7
    contract_quality: 58.3
    developer_ergonomics: 61.3
    discoverability: 74.1
    governance: 16.7
    operational_transparency: 48.7
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 107
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tenable/refs/heads/main/screenshots/tenable-2026-08-17T082310.png
security:
- kind: authentication
  name: Tenable Authentication
  slug: tenable-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Tenable Domain Security
  slug: tenable-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tenable Vulnerability Disclosure
  slug: tenable-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Tenable Trust Center
  slug: tenable-trust-center
  summary_line: SOC 2, ISO/IEC 27001:2022, FedRAMP (Tenable One VM + Web App Scanning, ATO 2021), StateRAMP (Tenable One VM, Authorized), CSA STAR, NIAP (Security Center, Nessus Manager, Nessus Network Monitor, Nessus Agent), Privacy Shield Framework
slug: tenable
tags:
- Company
- Enterprise
- Cybersecurity
- Vulnerability Management
- Exposure Management
- Security
- Cloud Security
- Attack Surface Management
website: https://www.tenable.com
---
