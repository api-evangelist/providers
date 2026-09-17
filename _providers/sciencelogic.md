---
access_model:
  confidence: high
  label: Commercial, per managed device per month, with a 14-day trial
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://sciencelogic.com/why-sciencelogic/pricing
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.6
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: The ScienceLogic AI Platform (Skylar) — AIOps, IT infrastructure and application observability, service management, network configuration compliance, and automated remediation.
  name: ScienceLogic
  slug: sciencelogic
- description: 'The GraphQL API for Skylar One (formerly SL1). ScienceLogic''s forward-looking interface — the default AP2 user interface uses it exclusively and makes no REST calls, and performance and log data held '
  name: Skylar One GraphQL API
  slug: skylar-one-graphql-api
- description: The REST API for Skylar One (formerly SL1), giving external systems programmatic access to tickets, devices, organizations, events, monitoring policies, dynamic applications, schedules, thresholds and
  name: Skylar One REST API
  slug: skylar-one-rest-api
- description: 'A FastMCP server published by the ScienceLogic GitHub organization exposing 22 read-only tools across two sub-servers — Skylar One (backed by the SL1 GraphQL API) and Skylar Compliance (backed by the '
  name: ScienceLogic MCP Server
  slug: sciencelogic-mcp
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Agents allow a Skylar Compliance appliance to manage devices located on a remote or otherwise disjointed network, not directly routable by Skylar Compliance, without the need of complex firewall chang
  name: ScienceLogic Agent API
  slug: sciencelogic-agent-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Endpoints that can aid in debugging agent problems.
  name: ScienceLogic Agent/Debug API
  slug: sciencelogic-agent-debug-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Start and stop remote support access on agents.
  name: ScienceLogic Agent/Remote API
  slug: sciencelogic-agent-remote-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: A device backup can encapsulates one or more device configurations. Depending on the type of device, a device backup might be a simple text file or a multi-gigabyte TGZ.
  name: ScienceLogic Backup API
  slug: sciencelogic-backup-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Skylar Compliance allows you to send a CLI command to a device or group of devices and capture the output of the command. This is a very convenient tool to perform a task concurrently on a group of de
  name: ScienceLogic Command API
  slug: sciencelogic-command-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Logs from running [scheduled commands](#tag/CommandSchedule) with `StoreLog` enabled can be retrieved here.
  name: ScienceLogic Command/Output API
  slug: sciencelogic-command-output-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Commands can be scheduled to run automatically at defined intervals or once.
  name: ScienceLogic Command/Schedule API
  slug: sciencelogic-command-schedule-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Commands can have one or multiple variables. The user can upload a csv file with a list of variables and they will be parsed and used when running the command.
  name: ScienceLogic Command/Variables API
  slug: sciencelogic-command-variables-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Set of username and up to two passwords that can be used across multiple devices.
  name: ScienceLogic Credential API
  slug: sciencelogic-credential-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Allows creating or updating multiple credentials at once. It will create a scheduled task with the given credentials and create a log entry for the beginning and end of the credentials creation/modifi
  name: ScienceLogic Credential/Bulk API
  slug: sciencelogic-credential-bulk-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Allows retrieving credentials from the external vault.
  name: ScienceLogic Credential/Provider/Cyber Ark API
  slug: sciencelogic-credential-provider-cyberark-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Devices are Skylar Compliance's representation of physical or virtual network devices.
  name: ScienceLogic Device API
  slug: sciencelogic-device-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: A device backup can encapsulates one or more device configurations. Depending on the type of device, a device backup might be a simple text file or a multi-gigabyte TGZ.
  name: ScienceLogic Device/Backup API
  slug: sciencelogic-device-backup-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Allows creating multiple devices at once. It will create a scheduled task with the given devices and create a log entry for each device creation and one when all the devices are created.
  name: ScienceLogic Device/Bulk Create API
  slug: sciencelogic-device-bulkcreate-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Allows editing multiple devices at once. This losely follows the structure of the [Device](#tag/Device) model. Skylar Compliance will aggregate values for individual settings. **String** values that a
  name: ScienceLogic Device/Bulk Edit API
  slug: sciencelogic-device-bulkedit-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Dictionaries for various auto-complete and search filter settings.
  name: ScienceLogic Dictionary API
  slug: sciencelogic-dictionary-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: The Skylar Compliance device discovery engine uses a variety of methods to discover hosts on your network that can be imported into the main device list. You can also be notified by email of new devic
  name: ScienceLogic Discovery API
  slug: sciencelogic-discovery-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: New devices as discovered by a manual or scheduled device discovery run will appear here.
  name: ScienceLogic Discovery/Device API
  slug: sciencelogic-discovery-device-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Domains allow you to organise devices into separate domains, and delegate their management to Domain Administrators. A typical use is for Service Providers managing multiple customers, or large enterp
  name: ScienceLogic Domain API
  slug: sciencelogic-domain-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: An endpoint to download files from.
  name: ScienceLogic Download API
  slug: sciencelogic-download-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Allows you to export device configurations, logs and settings for multiple devices or domains.
  name: ScienceLogic Export API
  slug: sciencelogic-export-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Automatically export device configurations to a specified file server. Please do not mistake this for the [device policy export](#operation/export_device_policies) endpoint.
  name: ScienceLogic Export/Policy API
  slug: sciencelogic-export-policy-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Skylar Compliance can act as a repository for device firmware/software, allowing you to upload files like firmware images and ISO images to the appliance. Software images can also be pushed to support
  name: ScienceLogic Firmware API
  slug: sciencelogic-firmware-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: 'Jobs represent a running task in Skylar Compliance, such as a running device backup, command or creating an archive of Skylar Compliance. Normally, a job transitions from: `Pending` -> `Running` -> `D'
  name: ScienceLogic Job API
  slug: sciencelogic-job-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Labels are a way of attaching meta information to devices. They allow for arbitrary grouping and selection of devices that can go beyond the use of device specific information fields. They help you or
  name: ScienceLogic Label API
  slug: sciencelogic-label-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Almost every system activity will be logged and can be retrieved
  name: ScienceLogic Log API
  slug: sciencelogic-log-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: The login endpoint is used by the UI to authenticate a user. On successful login, it will set a session cookie that will further authenticate API requests coming from the web interface.
  name: ScienceLogic Login API
  slug: sciencelogic-login-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Network utility endpoints.
  name: ScienceLogic Network API
  slug: sciencelogic-network-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Permissions are the building blocks of what a user's role is entitled to perform. Permissions are read-only.
  name: ScienceLogic Permission API
  slug: sciencelogic-permission-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: The Permissions/ValidateRequest API from ScienceLogic — 1 operation(s) for permissions/validaterequest.
  name: ScienceLogic Permissions/Validate Request API
  slug: sciencelogic-permissions-validaterequest-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Plugins have a number of device specific settings that are required for creating a functional device configurations for backup, restore or running commands.
  name: ScienceLogic Plugin API
  slug: sciencelogic-plugin-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: The Plugin default values API from ScienceLogic — 1 operation(s) for plugin default values.
  name: ScienceLogic Plugin default values API
  slug: sciencelogic-plugin-default-values-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: The Plugin redact rule API from ScienceLogic — 2 operation(s) for plugin redact rule.
  name: ScienceLogic Plugin redact rule API
  slug: sciencelogic-plugin-redact-rule-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Skylar Compliance enables you to create policies that can be used to verify that your devices comply with corporate or regulatory guidelines. Policies are groups of one or more rules; a rule is a patt
  name: ScienceLogic Policy API
  slug: sciencelogic-policy-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: 'Rules are the individual parts of a device policy. ## Regular Expressions A regular expression specifies a set of strings as a pattern, rather than a list. For example, the pattern `C(o|as?)t` matches'
  name: ScienceLogic Policy/Rule API
  slug: sciencelogic-policy-rule-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Policy variables can be used in compliance rules as variable replacements, referenced with the `$replace$` format, where `replace` is the variable name you have defined. This enables you to use a vari
  name: ScienceLogic Policy/Variable API
  slug: sciencelogic-policy-variable-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: The Recovery API from ScienceLogic — 2 operation(s) for recovery.
  name: ScienceLogic Recovery API
  slug: sciencelogic-recovery-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: The Report API from ScienceLogic — 4 operation(s) for report.
  name: ScienceLogic Report API
  slug: sciencelogic-report-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: The Report schedule API from ScienceLogic — 2 operation(s) for report schedule.
  name: ScienceLogic Report schedule API
  slug: sciencelogic-report-schedule-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: In addition to the standard built-in roles (`Admin`, `Backup`, and `View Only`), which cannot be edited, it is possible to define granular, custom roles, which specify in detail which product elements
  name: ScienceLogic Role API
  slug: sciencelogic-role-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: The SAML API from ScienceLogic — 2 operation(s) for saml.
  name: ScienceLogic SAML API
  slug: sciencelogic-saml-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Allows a view of the next occurence of all scheduled events including device backups, Skylar Compliance archival, device discovery as well as reporting.
  name: ScienceLogic Schedule API
  slug: sciencelogic-schedule-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: The Settings/Advanced API from ScienceLogic — 1 operation(s) for settings/advanced.
  name: ScienceLogic Settings/Advanced API
  slug: sciencelogic-settings-advanced-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Configure system email alert settings.
  name: ScienceLogic Settings/Alerts API
  slug: sciencelogic-settings-alerts-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Trigger global appliance actions.
  name: ScienceLogic Settings/Appliance/Actions API
  slug: sciencelogic-settings-appliance-actions-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Allows you to set general appliance settings as well as triggering global appliance actions.
  name: ScienceLogic Settings/Appliance API
  slug: sciencelogic-settings-appliance-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Endpoints that can aid in debugging appliance problems.
  name: ScienceLogic Settings/Appliance/Debug API
  slug: sciencelogic-settings-appliance-debug-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Add, update or reset a custom logo for the appliance UI.
  name: ScienceLogic Settings/Appliance/Logo API
  slug: sciencelogic-settings-appliance-logo-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Start and stop remote support sessions.
  name: ScienceLogic Settings/Appliance/Support API
  slug: sciencelogic-settings-appliance-support-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Check, retrieve and update the appliance.
  name: ScienceLogic Settings/Appliance/Updates API
  slug: sciencelogic-settings-appliance-updates-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: You can prepare for disaster recovery scenarios by archiving the Skylar Compliance configuration. This allows you to back up the Skylar Compliance appliance automatically, to up to two remote servers,
  name: ScienceLogic Settings/Archive API
  slug: sciencelogic-settings-archive-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Configure device asset information fields including location, asset tag, and serial number.
  name: ScienceLogic Settings/Assetfield API
  slug: sciencelogic-settings-assetfield-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Configure device asset notify address.
  name: ScienceLogic Settings/Assetfield/Notifications API
  slug: sciencelogic-settings-assetfield-notifications-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: 'Allows you to configure additional authentication methods for Skylar Compliance. Supported methods are: * RADIUS * SAML * LDAP'
  name: ScienceLogic Settings/Authentication API
  slug: sciencelogic-settings-authentication-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Allows you to set default device settings that are inherited whenever a new device is added but can be overriden.
  name: ScienceLogic Settings/Device API
  slug: sciencelogic-settings-device-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Allows you to set device discovery settings for manual or scheduled device discovery runs.
  name: ScienceLogic Settings/Discovery API
  slug: sciencelogic-settings-discovery-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: 'High Availability (HA) provides a way to minimise the effects of hardware failure, by configuring two Skylar Compliance appliances in a cluster. Under normal operating conditions, the primary cluster '
  name: ScienceLogic Settings/HA API
  slug: sciencelogic-settings-ha-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Allows you to configure default log rentention and other logging related settings.
  name: ScienceLogic Settings/Logs API
  slug: sciencelogic-settings-logs-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: 'Allows you to set network settings such as the IP address and static routes. ### Network Address Translation (NAT) Skylar Compliance may use back-connections (typically TFTP or FTP) to backup certain '
  name: ScienceLogic Settings/Network API
  slug: sciencelogic-settings-network-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: 'Password policies allow you to configure various rules for enforcing password strength, for both devices and users. These settings are used in the strength meter displayed in all password fields: the '
  name: ScienceLogic Settings/Passwords API
  slug: sciencelogic-settings-passwords-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Returns the default public keys for your appliance that can be used for public key authentication with devices that support it.
  name: ScienceLogic Settings/Public Key API
  slug: sciencelogic-settings-publickey-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: 'Configure various global settings to mandate a higher level of network security for the Skylar Compliance appliance. Setting some of these options may cause compatibility problems with legacy devices '
  name: ScienceLogic Settings/Security API
  slug: sciencelogic-settings-security-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Manage TLS CSRs
  name: ScienceLogic Settings/Security/CSR API
  slug: sciencelogic-settings-security-csr-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Manage SSH settings
  name: ScienceLogic Settings/Security/SSH API
  slug: sciencelogic-settings-security-ssh-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Configure TLS certificate and key
  name: ScienceLogic Settings/Security/TLS API
  slug: sciencelogic-settings-security-tls-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: If your network has a Network Management System, you can use SNMP to perform some basic monitoring of the Skylar Compliance appliance. Skylar Compliance supports SNMP v1, v2c, and v3.
  name: ScienceLogic Settings/SNMP API
  slug: sciencelogic-settings-snmp-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Retrieve status information for the appliance.
  name: ScienceLogic Status API
  slug: sciencelogic-status-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Check if appliance is ready to accept requests
  name: ScienceLogic Status/Ping API
  slug: sciencelogic-status-ping-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: These are the messages logged to the Skylar Compliance syslog service, by both the appliance itself and any devices configured to log to it.
  name: ScienceLogic Syslog API
  slug: sciencelogic-syslog-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: The Table view API from ScienceLogic — 2 operation(s) for table view.
  name: ScienceLogic Table view API
  slug: sciencelogic-table-view-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Templates are specially marked-up configurations that can be pushed to multiple devices, for instance during a large deployment of similarly configured devices. Each template can contain parameters, w
  name: ScienceLogic Template API
  slug: sciencelogic-template-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Personal access tokens are used to authenticate requests to the API. Tokens are tied to the user that created them. All API operations undertaken via a personal access token are linked to the user acc
  name: ScienceLogic Token API
  slug: sciencelogic-token-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: Device command and backup transcripts can be retrieved here.
  name: ScienceLogic Transcript API
  slug: sciencelogic-transcript-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: 'Skylar Compliance supports three levels of user access: - **Admin:** Super User; has full control (can create/modify/delete devices and users, initiate backups/restores and change the appliance config'
  name: ScienceLogic User API
  slug: sciencelogic-user-api
- baseURL: https://{appliance}/api/v2
  baseurl_source: declared
  description: For LDAP users to be able to login to Skylar Compliance, they need to be a member of a group and the group has to be added to Skylar Compliance (with domains and roles assigned). LDAP users inherit th
  name: ScienceLogic User/LDAP API
  slug: sciencelogic-user-ldap-api
- baseURL: https://{appliance}/gql
  baseurl_source: declared
  description: A file server represents a remote storage location that can be used for archiving Skylar Compliance, exporting backups and automated exports.
  name: ScienceLogic File Server API
  slug: sciencelogic-file-server-api
artifact_total: 88
asyncapis:
- description: ''
  name: Sciencelogic Webhooks
  slug: sciencelogic-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://sciencelogic.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sciencelogic.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sciencelogic.com/dev-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sciencelogic.com/skylar_compliance/api/5-6/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sciencelogic.com/latest/Content/Web_Content_Dev_and_Integration/ScienceLogic_API/api_intro.htm
- group: company
  title: ''
  type: Blog
  url: https://sciencelogic.com/feed
- group: operate
  title: ''
  type: Support
  url: https://support.sciencelogic.com/s/
- group: operate
  title: ''
  type: Community
  url: https://community.sciencelogic.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ScienceLogic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sciencelogic
- group: commercial
  title: ''
  type: Pricing
  url: https://sciencelogic.com/why-sciencelogic/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sciencelogic.com/get-free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sciencelogic.com/company/standard-terms-and-conditions-v20260116
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sciencelogic.com/company/legal
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/authentication/sciencelogic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sciencelogic-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/conventions/sciencelogic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sciencelogic-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/errors/sciencelogic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sciencelogic-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/lifecycle/sciencelogic-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sciencelogic-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/lifecycle/sciencelogic-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/sciencelogic-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/changelog/sciencelogic-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sciencelogic-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/data-model/sciencelogic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sciencelogic-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/conformance/sciencelogic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sciencelogic-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/conformance/sciencelogic-conformance.yml
  title: ''
  type: Compliance
  url: conformance/sciencelogic-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/security/sciencelogic-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sciencelogic-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/security/sciencelogic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sciencelogic-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/well-known/sciencelogic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sciencelogic-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/packages/sciencelogic-packages.yml
  title: ''
  type: Packages
  url: packages/sciencelogic-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/mcp/sciencelogic-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sciencelogic-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/mcp/sciencelogic-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/sciencelogic-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/overlays/sciencelogic-skylar-compliance-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sciencelogic-skylar-compliance-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/asyncapi/sciencelogic-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sciencelogic-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/plans/sciencelogic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sciencelogic-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/rate-limits/sciencelogic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sciencelogic-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/finops/sciencelogic-finops.yml
  title: ''
  type: FinOps
  url: finops/sciencelogic-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/llms/sciencelogic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sciencelogic-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.sciencelogic.com/llms.txt
created: '2026-03-27'
description: ScienceLogic is an AIOps and IT operations company whose ScienceLogic AI Platform — rebranded in 2026 as the Skylar family — covers infrastructure and application observability, network configuration and compliance, and workflow automation. Skylar One (formerly SL1) is the observability platform, with a REST API and a GraphQL API served from the customer's own Administration Portal, All-In-One Appliance or Database Server; ScienceLogic states that GraphQL is the forward path and that the REST API is now limited to bug fixes. Skylar Compliance (formerly Restorepoint, acquired by ScienceLogic) publishes a 314-operation OpenAPI 3.0 contract for configuration backup, change detection, compliance policy testing and device restore. Skylar Automation (formerly PowerFlow) handles ITSM and CMDB integration, and Skylar AI adds Advisor and Analytics on top. The ScienceLogic GitHub organization also publishes an MCP server that exposes read-only Skylar One and Skylar Compliance tools to
  AI agents. Products are deployed on customer appliances, SaaS, or private/public cloud, and are licensed per managed device per month.
finops:
- name: Sciencelogic Finops
  service_category: API
  slug: sciencelogic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sciencelogic.png
layout: provider
mcp_servers:
- description: 'A FastMCP server published by the ScienceLogic GitHub organization that gives AI agents access to ScienceLogic products through their existing APIs. It mounts two sub-servers in one process: Skylar Co'
  name: ScienceLogic MCP (mcp-sl)
  slug: sciencelogic-mcp-mcp-sl
modified: '2026-08-29'
name: ScienceLogic
nav: Providers
network: true
overview: 'ScienceLogic publishes 76 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Agent/Debug API, Agent/Remote API, and 73 more. Tagged areas include AIOps, IT Operations, Observability, Monitoring, and Network Configuration Management.


  The ScienceLogic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ScienceLogic''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Sciencelogic Plans Pricing
  plan_count: 4
  slug: sciencelogic-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Sciencelogic Rate Limits
  slug: sciencelogic-rate-limits
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.8
  facets:
    access_clarity: 100.0
    contract_governance: 0.0
    contract_quality: 59.9
    developer_ergonomics: 58.9
    discoverability: 61.1
    operational_transparency: 34.2
  previous_composite: 59.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 76
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/sciencelogic/refs/heads/main/screenshots/sciencelogic-2026-06-20T193537.png
security:
- kind: authentication
  name: Sciencelogic Authentication
  slug: sciencelogic-authentication
  summary_line: apiKey/openIdConnect · 3 schemes
- kind: domain-security
  name: Sciencelogic Domain Security
  slug: sciencelogic-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Sciencelogic Trust Center
  slug: sciencelogic-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, CSA STAR
slug: sciencelogic
tags:
- AIOps
- IT Operations
- Observability
- Monitoring
- Network Configuration Management
- Compliance
- Automation
- Incident Management
website: https://sciencelogic.com
---
