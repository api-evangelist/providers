---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1883
  human_in_the_loop: 55
  name: Palo Alto Networks Agentic Access
  operation_count: 3923
  slug: palo-alto-networks-agentic-access
  summary_line: 3923 operations · 1883 acting · 55 human-in-the-loop
api_count: 468
apis:
- description: The comprehensive XML-based API for PAN-OS providing full access to all firewall configuration, operational commands, reporting, logging, and commit operations. Supports request types including keygen
  name: PAN-OS XML API
  slug: pan-os-xml-api
- description: Management interface for PAN-OS based on OpenConfig standard data models, providing gNMI and gNOI services through the OpenConfig plugin. Supports network automation for BGP, interfaces, LACP, LLDP, V
  name: PAN-OS OpenConfig API
  slug: openconfig-api
- description: The Panorama API uses the same PAN-OS XML and REST API interfaces but provides centralized management of multiple firewalls from a single management server. Supports device group and template stack op
  name: Panorama API
  slug: panorama-api
- description: 'A threat intelligence API that provided contextual information about malware, campaigns, and threat actors observed across the Palo Alto Networks global threat intelligence network. AutoFocus reached '
  name: AutoFocus API (Deprecated)
  slug: autofocus-api
- description: A public JSON API for monitoring Prisma SASE service health and status built on the Atlassian StatusPage platform. Provides endpoints for overall service status, individual component health, unresolve
  name: Prisma SASE Service Status API
  slug: prisma-sase-service-status-api
- description: A public JSON API for monitoring the status of all Palo Alto Networks cloud services and products built on the Atlassian StatusPage platform. Provides endpoints for portfolio-wide status, individual p
  name: Cross-Platform Service Status API
  slug: cross-platform-service-status-api
- description: 'The OAuth 2.0 authentication service that provides access tokens for all Prisma SASE platform APIs. Uses Client ID and Client Secret credentials to generate short-lived bearer tokens with a 15-minute '
  name: SASE Authentication Service API
  slug: sase-authentication-service-api
- description: A RESTful API for the Expedition 2.0 migration tool enabling programmatic firewall configuration migration from third-party vendors, policy optimization, and rule analysis. Supported migration from Ch
  name: Expedition API (Deprecated)
  slug: expedition-api
- description: A REST API for licensing VM-Series virtual firewalls that do not have direct internet access to the Palo Alto Networks license server. Supports automated license activation, deactivation, and manageme
  name: VM-Series Licensing API
  slug: vm-series-licensing-api
- baseURL: https://{firewall}/restapi/v10.2
  baseurl_source: declared
  description: Address group management.
  name: Palo Alto Networks AddressGroups API
  slug: palo-alto-networks-addressgroups-api
- baseURL: https://{firewall}/restapi/v10.2
  baseurl_source: declared
  description: Cloud account onboarding and management.
  name: Palo Alto Networks CloudAccounts API
  slug: palo-alto-networks-cloudaccounts-api
- baseURL: https://{firewall}/restapi/v10.2
  baseurl_source: declared
  description: Data asset discovery and inventory operations.
  name: Palo Alto Networks DataAssets API
  slug: palo-alto-networks-dataassets-api
- baseURL: https://{firewall}/restapi/v10.2
  baseurl_source: declared
  description: Data pattern configuration and lookup operations.
  name: Palo Alto Networks DataPatterns API
  slug: palo-alto-networks-datapatterns-api
- baseURL: https://{firewall}/restapi/v10.2
  baseurl_source: declared
  description: IKE gateway configuration for establishing IPSec VPN tunnels to Prisma Access.
  name: Palo Alto Networks IKEGateways API
  slug: palo-alto-networks-ikegateways-api
- baseURL: https://{firewall}/restapi/v10.2
  baseurl_source: declared
  description: Owned IP range management.
  name: Palo Alto Networks IPRanges API
  slug: palo-alto-networks-ipranges-api
- baseURL: https://{firewall}/restapi/v10.2
  baseurl_source: declared
  description: IPSec tunnel configuration for site-to-site VPN connectivity.
  name: Palo Alto Networks IPSecTunnels API
  slug: palo-alto-networks-ipsectunnels-api
- baseURL: https://{firewall}/restapi/v10.2
  baseurl_source: declared
  description: NAT policy rule management.
  name: Palo Alto Networks NATRules API
  slug: palo-alto-networks-natrules-api
- baseURL: https://{firewall}/restapi/v10.2
  baseurl_source: declared
  description: The NotificationProfiles API from Palo Alto Networks — 6 operation(s) for notificationprofiles.
  name: Palo Alto Networks NotificationProfiles API
  slug: palo-alto-networks-notificationprofiles-api
- baseURL: https://{firewall}/restapi/v10.2
  baseurl_source: declared
  description: Quality of Service rule management for traffic prioritization across WAN links.
  name: Palo Alto Networks QoSRules API
  slug: palo-alto-networks-qosrules-api
- baseURL: https://{firewall}/restapi/v10.2
  baseurl_source: declared
  description: Content release notes for PAN-OS content updates.
  name: Palo Alto Networks ReleaseNotes API
  slug: palo-alto-networks-releasenotes-api
- baseURL: https://{firewall}/restapi/v10.2
  baseurl_source: declared
  description: Remote network configuration for connecting branch offices and data centers to Prisma Access via IPSec tunnels.
  name: Palo Alto Networks RemoteNetworks API
  slug: palo-alto-networks-remotenetworks-api
- baseURL: https://{firewall}/restapi/v10.2
  baseurl_source: declared
  description: Security rules within rule stacks.
  name: Palo Alto Networks SecurityRules API
  slug: palo-alto-networks-securityrules-api
- baseURL: https://{firewall}/restapi/v10.2
  baseurl_source: declared
  description: Service connection management for providing access to internal resources through Prisma Access.
  name: Palo Alto Networks ServiceConnections API
  slug: palo-alto-networks-serviceconnections-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The 5G Deregistered Trend API from Palo Alto Networks — 1 operation(s) for 5g deregistered trend.
  name: Palo Alto Networks 5G Deregistered Trend API
  phrasing_intents:
  - id: PostMtMonitor5gUeipDeregisteredTrend
    intent: Chart deregistered UE trend
    question: How many 5G UE devices have deregistered over time?
  phrasing_ops: 1
  slug: palo-alto-networks-5g-deregistered-trend-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The 5G Network Interconnects and Bandwidth API from Palo Alto Networks — 1 operation(s) for 5g network interconnects and bandwidth.
  name: Palo Alto Networks 5G Network Interconnects and Bandwidth API
  phrasing_intents:
  - id: GetMtMonitor5gInterconnectDetails
    intent: Get 5G interconnect and bandwidth details
    question: How much total bandwidth do my 5G network interconnects have?
  phrasing_ops: 1
  slug: palo-alto-networks-5g-network-interconnects-and-bandwidth-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The 5G Registered Trend API from Palo Alto Networks — 1 operation(s) for 5g registered trend.
  name: Palo Alto Networks 5G Registered Trend API
  phrasing_intents:
  - id: PostMtMonitor5gUeipRegisteredTrend
    intent: Show the trend of registered 5G UE devices
    question: How has the number of registered 5G user equipment devices changed over time?
  phrasing_ops: 1
  slug: palo-alto-networks-5g-registered-trend-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The 5G Unknown IPs Trend API from Palo Alto Networks — 1 operation(s) for 5g unknown ips trend.
  name: Palo Alto Networks 5G Unknown IPs Trend API
  phrasing_intents:
  - id: PostMtMonitor5gUnknownipTrend
    intent: Get the trend of unknown IPs on the 5G network
    question: How has the number of unknown IP addresses on my 5G network changed over time?
  phrasing_ops: 1
  slug: palo-alto-networks-5g-unknown-ips-trend-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Active Mappings API from Palo Alto Networks — 1 operation(s) for active mappings.
  name: Palo Alto Networks Active Mappings API
  phrasing_intents:
  - id: GetMtMonitor5gMappingActiveues
    intent: Count active 5G UE mappings
    question: How many 5G user equipment mappings are active right now?
  phrasing_ops: 1
  slug: palo-alto-networks-active-mappings-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Added and Cleared Mappings API from Palo Alto Networks — 1 operation(s) for added and cleared mappings.
  name: Palo Alto Networks Added and Cleared Mappings API
  phrasing_intents:
  - id: PostMtMonitor5gUeipCount
    intent: Count added and cleared UE IP mappings
    question: How many 5G UE IP address mappings were added or cleared over a time period?
  phrasing_ops: 1
  slug: palo-alto-networks-added-and-cleared-mappings-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: The Addresses API from Palo Alto Networks — 4 operation(s) for addresses.
  name: Palo Alto Networks Addresses API
  phrasing_intents:
  - id: ListAddresses
    intent: List address objects
    question: Which address objects are configured in a given folder?
  - id: CreateAddresses
    intent: Create an address with a name and tags
    question: How do I add a new address with a description and tags?
  - id: GetAddressesByID
    intent: Get an address by ID
    question: What's stored on the address with a particular ID?
  - id: UpdateAddressesByID
    intent: Update an address's name, description or tags
    question: Can I rename an existing address or change its tags?
  - id: DeleteAddressesByID
    intent: Delete an address
    question: How do I remove an address I no longer need?
  - id: listAddresses
    intent: List firewall address objects
    question: Which IP addresses, subnets and FQDNs are defined as address objects in my SSE config?
  - id: createAddress
    intent: Create a firewall address object
    question: How do I define a new IP netmask, IP range or FQDN as a named address object?
  - id: getAddress
    intent: Get a Prisma Access address object
    question: What IP or FQDN does a particular address object resolve to?
  phrasing_ops: 10
  slug: palo-alto-networks-addresses-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: 'Prisma Cloud generates an alert when it detects a violation in a policy that is included in an active alert rule. You can use the API requests to manage alerts, including listing or viewing, snoozing '
  name: Palo Alto Networks Alerts API
  phrasing_intents:
  - id: getAlerts
    intent: Search detections across endpoint, network and cloud
    question: Can I pull endpoint, network and cloud detections filtered by severity and category in one request?
  - id: alertPolicyList
    intent: Page through policies with their alert counts
    question: Which policies have the most open alerts right now, using the newer paginated policy endpoint?
  - id: alertAggregation
    intent: Group alert counts by a policy field
    question: Can I bucket my alert counts by a policy field such as severity or policy type?
  - id: getAlertEvidenceGraph
    intent: Get an alert's evidence graph
    question: Can I get the evidence behind an alert as graph data I can draw?
  - id: create-Ondemand-Notification
    intent: Send an on-demand notification for an alert
    question: Can I push a single alert to Jira, email or Slack right now instead of waiting for a rule?
  - id: get-alert-filter-and-options
    intent: List the available alert filters
    question: What filters can I use when querying cloud alerts?
  - id: get-alert-filter-options
    intent: Autocomplete values for an alert filter
    question: What values can I pick for a specific alert filter like cloud.region?
  - id: get-alerts
    intent: List cloud alerts via query string (v1, 10k cap)
    question: Can I list Prisma Cloud alerts with query-string filters using the original v1 endpoint?
  phrasing_ops: 37
  slug: palo-alto-networks-alerts-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The API Stats API from Palo Alto Networks — 1 operation(s) for api stats.
  name: Palo Alto Networks API Stats API
  phrasing_intents:
  - id: PostMtMonitor5gApiStats
    intent: Get 5G API call statistics
    question: How many API calls succeeded or failed on the 5G interface?
  phrasing_ops: 1
  slug: palo-alto-networks-api-stats-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Applications API from Palo Alto Networks — 48 operation(s) for applications.
  name: Palo Alto Networks Applications API
  phrasing_intents:
  - id: GetSeb-apiV1Applications
    intent: List all secure browser applications
    question: Can I see every application defined in the Secure Enterprise Browser console across all types?
  - id: GetSeb-apiV1Applicationsbyid
    intent: Get a secure browser application by ID
    question: What is configured on a single secure browser application when I only know its ID?
  - id: DeleteSeb-apiV1Applicationsbyid
    intent: Delete a secure browser application by ID
    question: Can I permanently remove one secure browser application using just its ID?
  - id: GetSeb-apiV1ApplicationsTypebytype
    intent: List secure browser applications of one type
    question: Which secure browser applications exist of a particular type, like private or non-web apps?
  - id: PostSeb-apiV1ApplicationsTypebytype
    intent: Create a secure browser application
    question: How do I add a single new custom application to the Secure Enterprise Browser console?
  - id: GetSeb-apiV1ApplicationsTypeBy_typebyid
    intent: Get a secure browser application within a type
    question: Can I fetch a secure browser application by ID scoped to its type?
  - id: PatchSeb-apiV1ApplicationsTypeBy_typebyid
    intent: Partially update a secure browser application
    question: Can I change a few attributes of a secure browser application and leave the rest untouched?
  - id: DeleteSeb-apiV1ApplicationsTypeBy_typebyid
    intent: Delete a secure browser application of a type
    question: Can I remove a secure browser app when I know both its type and ID?
  phrasing_ops: 48
  slug: palo-alto-networks-applications-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Apps API from Palo Alto Networks — 4 operation(s) for apps.
  name: Palo Alto Networks Apps API
  phrasing_intents:
  - id: getRegisteredApplications
    intent: List registered SaaS apps in SSPM (sspm path)
    question: Which SaaS applications are registered in SSPM for my region?
  - id: getRegisteredApplication
    intent: Get a registered SaaS app's basic details
    question: What are the basic details of one onboarded SaaS application in SSPM?
  - id: getApplicationConfigs
    intent: Get a SaaS app's configuration details
    question: How is a particular SaaS application configured in SSPM?
  - id: getApplicationSettings
    intent: Get a SaaS app's settings
    question: What settings does SSPM report for a given SaaS application?
  - id: listOnboardedApps
    intent: List onboarded SaaS apps with posture counts
    question: Which SaaS apps are onboarded for posture assessment and how many failing checks does each have?
  - id: onboardApp
    intent: Onboard a SaaS app for posture assessment
    question: How do I connect a new SaaS application to SSPM for posture scanning?
  - id: removeApp
    intent: Remove an onboarded SaaS app from SSPM
    question: How do I stop SSPM from scanning a SaaS app and delete its results?
  phrasing_ops: 7
  slug: palo-alto-networks-apps-api
- baseURL: https://api.dig.security
  baseurl_source: declared
  description: '{''$ref'': ''desc/assets/assets.md''}'
  name: Palo Alto Networks Assets API
  phrasing_intents:
  - id: getAssetsInternetExposure
    intent: List internet-exposed assets found by Xpanse
    question: Which of our servers and cloud instances are visible from the internet according to Xpanse?
  - id: getAssetInternetExposure
    intent: Get details of one internet-exposed asset
    question: What services, certificates and observations does Xpanse show for one exposed asset?
  - id: listAssets
    intent: List assets tracked by XSIAM
    question: What devices, users and service accounts has XSIAM observed in my environment?
  - id: get-assets
    intent: List DSPM cloud data assets with filters
    question: Which data stores in my cloud are open to the world according to DSPM?
  - id: get-assets-id
    intent: Describe a DSPM data asset
    question: What does DSPM know about one specific data asset?
  - id: getApiAssets
    intent: List files and content scanned in SaaS apps
    question: Which files and folders in our connected SaaS apps are shared publicly?
  - id: getAsset
    intent: Get a scanned SaaS asset's exposure and violations
    question: Who has access to a particular file scanned by SaaS Security?
  phrasing_ops: 7
  slug: palo-alto-networks-assets-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Catalog API from Palo Alto Networks — 6 operation(s) for catalog.
  name: Palo Alto Networks Catalog API
  phrasing_intents:
  - id: catalog_get
    intent: Get identity catalog for an app type
    question: Which identity features does SSPM support for a given application type?
  - id: getCatalogApplications
    intent: List SSPM-supported SaaS applications
    question: Which SaaS applications can SaaS Security Posture Management monitor?
  - id: getCatalogApplication
    intent: Get catalog settings for an SSPM app
    question: What catalog settings does SSPM hold for one application?
  - id: getApplicationConfigurations
    intent: Get an app's catalog configuration settings
    question: Which configuration settings does SSPM check for a given SaaS app?
  - id: getApplicationScopes
    intent: Get an app's plugin scope catalog
    question: What plugin scopes does SSPM need to connect to a SaaS app?
  - id: getCommonControlComplianceProfiles
    intent: Map a common control to compliance profiles
    question: Which compliance frameworks does a given common control map to?
  phrasing_ops: 6
  slug: palo-alto-networks-catalog-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Configured UE Mappings API from Palo Alto Networks — 1 operation(s) for configured ue mappings.
  name: Palo Alto Networks Configured UE Mappings API
  phrasing_intents:
  - id: GetMtMonitor5gMappingConfiguredues
    intent: Count configured 5G UE mappings
    question: How many user equipment devices have users configured for 5G mapping?
  phrasing_ops: 1
  slug: palo-alto-networks-configured-ue-mappings-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/containers/containers.md''}'
  name: Palo Alto Networks Containers API
  phrasing_intents:
  - id: get-containers
    intent: Get container scan results (v34.03)
    question: What do container scan results look like on the older v34.03 API?
  - id: get-containers-count
    intent: Count scanned containers (v34.03)
    question: How many containers are scanned, according to the v34.03 count endpoint?
  - id: get-containers-download
    intent: Download container scan results (v34.03)
    question: Can I export container scan results as a file from the v34.03 API?
  - id: get-containers-names
    intent: List container names (v34.03)
    question: Which container names are known to the v34.03 API?
  - id: post-containers-scan
    intent: Start a container scan (v34.03)
    question: How do I trigger a container scan through the v34.03 API?
  - id: getApiV3404Containers
    intent: Get container scan results (v34.04)
    question: What vulnerabilities and compliance issues did the latest v34.04 container scan find?
  - id: getApiV3404ContainersCount
    intent: Count scanned containers (v34.04)
    question: How many containers are scanned in total on the current v34.04 API?
  - id: getApiV3404ContainersDownload
    intent: Download container scan results (v34.04)
    question: How do I download container scan results as CSV on the v34.04 API?
  phrasing_ops: 11
  slug: palo-alto-networks-containers-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/defenders/defenders.md''}'
  name: Palo Alto Networks Defenders API
  phrasing_intents:
  - id: get-defenders
    intent: List deployed Defenders (API v34.03)
    question: Which Defenders are deployed in my Compute console, per the v34.03 API?
  - id: post-defenders-aci.yaml
    intent: Add Defenders to an ACI container group YAML (v34.03)
    question: Can the v34.03 API inject a Defender into my Azure Container Instances group YAML?
  - id: post-defenders-app-embedded
    intent: Generate an App-Embedded Defender Dockerfile (v34.03)
    question: Can the v34.03 API rewrite my Dockerfile to embed a Defender in the app?
  - id: post-defenders-cloud-run.yaml
    intent: Add Defenders to a Cloud Run service YAML (v34.03)
    question: Can the v34.03 API add a Defender to my Google Cloud Run service YAML?
  - id: post-defenders-daemonset.yaml
    intent: Generate a Defender DaemonSet YAML (v34.03)
    question: How do I get a Kubernetes DaemonSet YAML to roll out Defenders using API v34.03?
  - id: get-defenders-download
    intent: Download the deployed Defenders list as CSV (v34.03)
    question: Can I export my deployed Defenders to a file with the v34.03 API?
  - id: post-defenders-eks-fargate.yaml
    intent: Add Defenders to an EKS Fargate manifest (v34.03)
    question: Can the v34.03 API inject Defenders into a Kubernetes controller manifest for EKS on Fargate?
  - id: post-defenders-fargate.json
    intent: Protect an ECS Fargate task definition in JSON (v34.03)
    question: Can the v34.03 API return a protected Fargate task definition in JSON?
  phrasing_ops: 44
  slug: palo-alto-networks-defenders-api
- baseURL: https://api.stratacloud.paloaltonetworks.com/aiops/bpa/v1
  baseurl_source: declared
  description: The Devices API from Palo Alto Networks — 10 operation(s) for devices.
  name: Palo Alto Networks Devices API
  phrasing_intents:
  - id: GetSeb-apiV1Devices
    intent: List browser-protected endpoint devices
    question: Which devices running the secure enterprise browser have disk encryption turned off?
  - id: GetSeb-apiV1Devicesbyid
    intent: Get one secure browser device
    question: How do I pull the full record for one secure browser device?
  - id: PostSeb-apiV1DevicesArchive
    intent: Archive browser devices
    question: How do I archive devices that are no longer in use?
  - id: PostSeb-apiV1DevicesRestore
    intent: Restore archived browser devices
    question: How do I bring an archived device back to active?
  - id: PostSeb-apiV1DevicesSuspend
    intent: Suspend browser devices
    question: How do I temporarily block a lost laptop from the enterprise browser?
  - id: PostSeb-apiV1DevicesResume
    intent: Resume suspended browser devices
    question: How do I lift a suspension on a device?
  - id: PostSeb-apiV1DevicesDelete
    intent: Permanently delete browser devices
    question: How do I permanently remove devices from the enterprise browser inventory?
  - id: PostSeb-apiV1DevicesForce-reauth
    intent: Force users to re-authenticate on devices
    question: How do I make a user sign in again to the browser on a specific device?
  phrasing_ops: 14
  slug: palo-alto-networks-devices-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Directory Sync Service API from Palo Alto Networks — 4 operation(s) for directory sync service.
  name: Palo Alto Networks Directory Sync Service API
  phrasing_intents:
  - id: getHttps:ApiSasePaloaltonetworksComCieDirectorySyncV1Domains
    intent: Check sync status of directory domains
    question: When did each of my directory domains last sync successfully?
  - id: postHttps:ApiSasePaloaltonetworksComCieDirectorySyncV1CacheUsers
    intent: Check a user's group membership
    question: Is a particular user a member of a given directory group?
  - id: postHttps:ApiSasePaloaltonetworksComCieDirectorySyncV1CacheGroups
    intent: Check whether a group contains a user
    question: Does a particular directory group contain a given user?
  - id: getCieDirectorySyncV1Domains
    intent: List directory sync domains
    question: Which domains are configured in the Cloud Identity Engine Directory Sync Service?
  - id: postCieDirectorySyncV1CacheUsers
    intent: Query synced directory users
    question: How do I list every user synced from a directory domain?
  - id: postCieDirectorySyncV1CacheGroups
    intent: Query synced directory groups
    question: How do I list every group synced from a directory domain?
  - id: postCieDirectorySyncV1ConnectionUpdateSecret
    intent: Rotate a directory connection's client secret
    question: How do I rotate the client secret on an existing directory connection?
  phrasing_ops: 7
  slug: palo-alto-networks-directory-sync-service-api
- baseURL: https://api.prismacloud.io/code/api/v1
  baseurl_source: declared
  description: The Errors API from Palo Alto Networks — 10 operation(s) for errors.
  name: Palo Alto Networks Errors API
  phrasing_intents:
  - id: getErrorsInFile
    intent: List code security errors in one file
    question: What misconfigurations were found in a specific file of my repository?
  - id: getErrorsFiles
    intent: List files that have code errors
    question: Which files in my repository have security findings?
  - id: getErrorsInFiles
    intent: Get file metadata by UUID
    question: How do I get metadata for a scanned file when I only have its UUID?
  - id: getFixedCode
    intent: Get remediated code for a finding
    question: Can I preview the fixed resource code for a misconfiguration before applying it?
  - id: getGitBlameAuthors
    intent: List git blame authors of a repository
    question: Who are the git authors that committed to a given repository?
  - id: submitActions
    intent: Fix or suppress code security violations
    question: How do I open a pull request that fixes several violations at once?
  - id: supply-chain-fix
    intent: Remediate packages and IaC from supply chain view
    question: How do I fix vulnerable packages found on the supply chain screen?
  - id: getPeriodicFindings
    intent: Get code issues from periodic branch scans
    question: What code issues did the scheduled branch scans find?
  phrasing_ops: 11
  slug: palo-alto-networks-errors-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/hosts/hosts.md''}'
  name: Palo Alto Networks Hosts API
  phrasing_intents:
  - id: get-hosts
    intent: Get host scan results (v34.03)
    question: On the v34.03 API, which hosts have critical vulnerabilities in their scan results?
  - id: get-hosts-download
    intent: Download host scan results (v34.03)
    question: Can I download host scan results as a file through the v34.03 API?
  - id: post-hosts-evaluate
    intent: Resolve hosts (v34.03)
    question: What does resolving hosts do in the v34.03 Hosts API?
  - id: get-hosts-info
    intent: Get host information (v34.03)
    question: Can I get host information rather than full scan results on the v34.03 API?
  - id: post-hosts-scan
    intent: Start a host scan (v34.03)
    question: How do I trigger a host scan using the v34.03 API?
  - id: getApiV3404Hosts
    intent: Get host scan results (v34.04)
    question: Which hosts have high severity findings in the v34.04 host scan results?
  - id: getApiV3404HostsDownload
    intent: Download host scan results (v34.04)
    question: Can I download the current v34.04 host scan results as a report?
  - id: postApiV3404HostsEvaluate
    intent: Resolve hosts (v34.04)
    question: Can I resolve a list of images to hosts with the v34.04 API?
  phrasing_ops: 11
  slug: palo-alto-networks-hosts-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The IDP API from Palo Alto Networks — 9 operation(s) for idp.
  name: Palo Alto Networks IDP API
  phrasing_intents:
  - id: idps_get
    intent: List the tenant's identity providers
    question: Which identity providers are connected to my SaaS security posture tenant?
  - id: idps_post
    intent: Register a new identity provider
    question: How do I add an identity provider to my SSPM tenant?
  - id: idps_accounts_logout_get
    intent: Check the status of a forced account logout
    question: Did the forced logout of accounts on my identity provider finish?
  - id: idps_accounts_logout_post
    intent: Force-log out users from an identity provider
    question: How can I terminate sessions for compromised users in my identity provider?
  - id: idps_feature_state_get
    intent: Check an identity provider feature's scan state
    question: When was a feature on my identity provider last scanned, and is it healthy?
  - id: idps_idp_accounts_count_get
    intent: Count accounts on an identity provider
    question: How many user accounts are linked to my identity provider?
  - id: idps_idp_accounts_csv_report_get
    intent: Generate a CSV report of identity provider accounts
    question: Can I export the user accounts in my identity provider to CSV for an access review?
  - id: idps_mfa_activity_get
    intent: View MFA activity logs for an identity provider
    question: What multi-factor authentication events has my identity provider recorded, with user and IP?
  phrasing_ops: 11
  slug: palo-alto-networks-idp-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/images/images.md''}'
  name: Palo Alto Networks Images API
  phrasing_intents:
  - id: get-images
    intent: Get image scan results (v34.03)
    question: Where do I see container image scan results with the v34.03 API?
  - id: get-images-download
    intent: Download image scan results (v34.03)
    question: Can I export deployed image scan results with the older v34.03 endpoint?
  - id: post-images-evaluate
    intent: Resolve images (v34.03)
    question: Can I resolve a batch of images to their scan data using v34.03?
  - id: get-images-names
    intent: List image names (v34.03)
    question: What container image names has Defender seen, according to v34.03?
  - id: post-images-scan
    intent: Start an image scan (v34.03)
    question: Can I rescan deployed images on a host with the v34.03 API?
  - id: get-images-twistlock_defender_app_embedded.tar.gz
    intent: Download App-Embedded Defender (v34.03)
    question: Where can I get the App-Embedded Defender archive from the v34.03 API?
  - id: post-images-twistlock_defender_layer.zip
    intent: Download serverless Defender layer (v34.03)
    question: Can I download the serverless Defender layer bundle for a runtime on v34.03?
  - id: getApiV3404Images
    intent: Get image scan results
    question: What vulnerabilities and compliance issues are in my deployed container images?
  phrasing_ops: 16
  slug: palo-alto-networks-images-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Incidents by Severity API from Palo Alto Networks — 1 operation(s) for incidents by severity.
  name: Palo Alto Networks Incidents by Severity API
  phrasing_intents:
  - id: PostMtMonitor5gIncidentsCount
    intent: Count 5G incidents by severity
    question: How many 5G incidents do I have at each severity level?
  phrasing_ops: 1
  slug: palo-alto-networks-incidents-by-severity-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: 'With multiple out-of-the-box integration options, you can integrate Prisma Cloud into security workflows and technologies that already exist in your organization. **Note**: For Prisma Cloud integratio'
  name: Palo Alto Networks Integrations API
  phrasing_intents:
  - id: searchIntegrations
    intent: Search available integration packs
    question: Which integration packs are installed in my Cortex XSOAR instance?
  - id: searchIntegrationInstances
    intent: Search configured integration instances
    question: What configured integration instances are connected in XSOAR?
  - id: get-supported-integration-channels-v1
    intent: List supported integration types
    question: What kinds of external integrations does Prisma Cloud support for my tenant?
  - id: get-all-integrations-v1
    intent: List a tenant's integrations
    question: Which integrations are configured on my Prisma Cloud tenant?
  - id: create-integration-v1
    intent: Add an integration
    question: How do I connect Prisma Cloud to an external system like a ticketing or messaging tool?
  - id: get-integration-v1
    intent: Get an integration by ID
    question: What is the configuration of a specific integration on my tenant?
  - id: update-integration-state-v1
    intent: Enable or disable an integration
    question: Can I temporarily turn off an integration without deleting it?
  - id: update-integration-v1
    intent: Update an integration's configuration
    question: Can I change the name or configuration of an existing integration?
  phrasing_ops: 14
  slug: palo-alto-networks-integrations-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Interconnect API from Palo Alto Networks — 6 operation(s) for interconnect.
  name: Palo Alto Networks Interconnect API
  phrasing_intents:
  - id: GetMtSp-interconnectInterconnects
    intent: List all Service Provider Interconnects
    question: Which SP Interconnects are configured across my AWS and GCP regions?
  - id: PostMtSp-interconnectInterconnects
    intent: Provision a new Service Provider Interconnect
    question: How do I set up a private interconnect between my service provider network and Prisma Access?
  - id: GetMtSp-interconnectInterconnectsSummary
    intent: Summarize interconnect health and capacity
    question: How many of my interconnects are active versus inactive?
  - id: GetMtSp-interconnectInterconnectsBy_interconnectid
    intent: Get one interconnect's configuration and status
    question: What VLAN attachments and status does a specific interconnect have?
  - id: DeleteMtSp-interconnectInterconnectsBy_interconnectid
    intent: Permanently remove an interconnect
    question: How do I retire an interconnect we no longer need for egress?
  - id: GetMtSp-interconnectRegions
    intent: List supported interconnect regions and edges
    question: Which regions and edge locations support SP Interconnect?
  - id: GetMtSp-interconnectRegionsPhysical-connections
    intent: List GCP colocation sites for physical links
    question: Where can I provision a physical interconnect link on the GCP network?
  - id: PostMtSp-interconnectSettings
    intent: Configure a tenant's egress routing
    question: How do I switch a tenant's egress traffic to the private service provider path?
  phrasing_ops: 9
  slug: palo-alto-networks-interconnect-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The IP Pool API from Palo Alto Networks — 1 operation(s) for ip pool.
  name: Palo Alto Networks IP Pool API
  phrasing_intents:
  - id: PutMtSp-interconnectInterconnectsBy_interconnectidIp-pool
    intent: Update an interconnect's IP address pool
    question: Can I change the IP blocks on an interconnect pool that already exists?
  - id: GetMtSp-interconnectInterconnectsBy_interconnectidIp-pool
    intent: View an interconnect's IP address pool
    question: Which CIDR ranges are assigned to my service provider interconnect?
  - id: DeleteMtSp-interconnectInterconnectsBy_interconnectidIp-pool
    intent: Remove an interconnect's IP address pool
    question: What happens to routing when I delete an interconnect's IP pool?
  - id: PostMtSp-interconnectInterconnectsBy_interconnectidIp-pool
    intent: Attach a new IP address pool to an interconnect
    question: How do I provision the first IP address pool on a new interconnect?
  phrasing_ops: 4
  slug: palo-alto-networks-ip-pool-api
- baseURL: https://api.strata.paloaltonetworks.com/config/operations/v1
  baseurl_source: declared
  description: Jobs
  name: Palo Alto Networks Jobs API
  phrasing_intents:
  - id: ListJobs
    intent: List configuration jobs
    question: What configuration jobs have run recently?
  - id: GetJobsByID
    intent: Get a configuration job
    question: What happened with a specific configuration job?
  - id: getJobStatus
    intent: Get the status and results of a device job
    question: Has the asynchronous job running on my device finished yet?
  - id: getJob
    intent: Get the status of an SSE config push or commit job
    question: Did my Prisma Access configuration push or commit succeed?
  phrasing_ops: 4
  slug: palo-alto-networks-jobs-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Licenses API from Palo Alto Networks — 1 operation(s) for licenses.
  name: Palo Alto Networks Licenses API
  phrasing_intents:
  - id: get-subscription-v1-licenses
    intent: List SASE license details
    question: Which licenses are allocated to my tenant service group?
  - id: getZTNALicenses
    intent: Get ZTNA license entitlements
    question: How many ZTNA users am I licensed for and how many are active?
  phrasing_ops: 2
  slug: palo-alto-networks-licenses-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Locations API from Palo Alto Networks — 1 operation(s) for locations.
  name: Palo Alto Networks Locations API
  phrasing_intents:
  - id: get-sse-config-v1-locations
    intent: List Prisma Access locations from SSE config
    question: Which Prisma Access locations can I use in my SSE configuration?
  - id: listPrismaAccessLocations
    intent: List Prisma Access gateway locations with services
    question: Which Prisma Access gateway locations are available, by region, country and city?
  phrasing_ops: 2
  slug: palo-alto-networks-locations-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: Log Forwarding Profiles
  name: Palo Alto Networks Log Forwarding Profiles API
  phrasing_intents:
  - id: ListLogForwardingProfiles
    intent: List log forwarding profiles
    question: Which log forwarding profiles are defined in a given configuration folder?
  - id: CreateLogForwardingProfiles
    intent: Create a log forwarding profile with match list
    question: How do I create a log forwarding profile with a match list of log types and filters?
  - id: GetLogForwardingProfilesByID
    intent: Get a log forwarding profile's match list config
    question: What match list is configured on an existing log forwarding profile configuration object?
  - id: UpdateLogForwardingProfilesByID
    intent: Update a log forwarding profile's match list
    question: Can I replace the match list on an existing log forwarding configuration object?
  - id: DeleteLogForwardingProfilesByID
    intent: Delete a log forwarding configuration object
    question: Can I delete a log forwarding profile configuration resource by its UUID?
  - id: getLogForwardingProfile
    intent: Get a log forwarding profile's log types
    question: Which log types does a particular log forwarding profile send?
  - id: updateLogForwardingProfile
    intent: Change a log forwarding profile's log types
    question: Can I change which log types a forwarding profile includes?
  - id: deleteLogForwardingProfile
    intent: Delete a log forwarding profile and its destinations
    question: Does deleting a log forwarding profile also remove all its destinations?
  phrasing_ops: 9
  slug: palo-alto-networks-log-forwarding-profiles-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Mappings Region API from Palo Alto Networks — 1 operation(s) for mappings region.
  name: Palo Alto Networks Mappings Region API
  phrasing_intents:
  - id: GetMtMonitor5gMappingRegion
    intent: List regions with 5G mappings
    question: Which regions have 5G mappings?
  phrasing_ops: 1
  slug: palo-alto-networks-mappings-region-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The MobileAgent API from Palo Alto Networks — 9 operation(s) for mobileagent.
  name: Palo Alto Networks Mobile Agent API
  phrasing_intents:
  - id: delete-sse-config-v1-mobile-agent-agent-profiles
    intent: Delete a GlobalProtect agent profile
    question: Can I remove a GlobalProtect agent profile my mobile users no longer need?
  - id: get-sse-config-v1-mobile-agent-agent-profiles
    intent: List GlobalProtect agent profiles
    question: Which GlobalProtect agent profiles are configured for my mobile users?
  - id: post-sse-config-v1-mobile-agent-agent-profiles
    intent: Create a GlobalProtect agent profile
    question: How do I create a new GlobalProtect agent profile for a group of mobile users?
  - id: put-sse-config-v1-mobile-agent-agent-profiles
    intent: Change a GlobalProtect agent profile
    question: Can I change the gateways an existing GlobalProtect agent profile connects to?
  - id: get-sse-config-v1-mobile-agent-agent-versions
    intent: List available GlobalProtect agent versions
    question: Which GlobalProtect app versions can I deploy to my mobile users?
  - id: delete-sse-config-v1-mobile-agent-authentication-settings
    intent: Delete a GlobalProtect authentication setting
    question: Can I remove a GlobalProtect authentication setting I no longer use?
  - id: get-sse-config-v1-mobile-agent-authentication-settings
    intent: List GlobalProtect authentication settings
    question: What authentication settings are configured for GlobalProtect users?
  - id: post-sse-config-v1-mobile-agent-authentication-settings
    intent: Create a GlobalProtect authentication setting
    question: How do I add a new authentication setting for GlobalProtect users on a specific OS?
  phrasing_ops: 26
  slug: palo-alto-networks-mobileagent-api
- baseURL: https://mssp-api.prismacloud.io
  baseurl_source: declared
  description: The MSSP Account Management API from Palo Alto Networks — 4 operation(s) for mssp account management.
  name: Palo Alto Networks MSSP Account Management API
  phrasing_intents:
  - id: tosAcceptance
    intent: Accept terms of service for an MSSP
    question: How does an MSSP accept the terms of service through the API?
  - id: getMssp
    intent: Get an MSSP account's details
    question: What are the details of our managed security service provider account?
  - id: getMsspOperations
    intent: List an MSSP's operations
    question: Which operations have run on an MSSP account and did any fail?
  - id: getMsspLicensePools
    intent: Get an MSSP's license pool
    question: How many licenses are left in our MSSP license pool?
  phrasing_ops: 4
  slug: palo-alto-networks-mssp-account-management-api
- baseURL: https://mssp-api.prismacloud.io
  baseurl_source: declared
  description: The Mssp License Endpoints API from Palo Alto Networks — 2 operation(s) for mssp license endpoints.
  name: Palo Alto Networks Mssp License Endpoints API
  phrasing_intents:
  - id: getMsspLicenseUsageV1
    intent: Get MSSP license usage for a pool
    question: How much of a license pool have my managed tenants consumed?
  - id: getMsspLicenseInfoV1
    intent: Get MSSP license info
    question: What licenses does my MSSP account hold?
  phrasing_ops: 2
  slug: palo-alto-networks-mssp-license-endpoints-api
- baseURL: https://mssp-api.prismacloud.io
  baseurl_source: declared
  description: The MSSP Managed Tenant Lifecycle Endpoints API from Palo Alto Networks — 3 operation(s) for mssp managed tenant lifecycle endpoints.
  name: Palo Alto Networks MSSP Managed Tenant Lifecycle Endpoints API
  phrasing_intents:
  - id: getManagedTenants
    intent: List an MSSP's managed tenants
    question: Which tenants does my MSSP manage?
  - id: createManagedTenant
    intent: Create a managed tenant for an MSSP
    question: How do I onboard a new customer tenant under my MSSP?
  - id: getManagedTenantById
    intent: Get a managed tenant's details
    question: What details are stored for one of my managed tenants?
  - id: softDeleteManagedTenant
    intent: Mark a managed tenant as deleted
    question: Can I offboard a customer tenant from my MSSP?
  - id: updateManagedTenant
    intent: Modify a managed tenant
    question: Can I move a managed tenant into a different tenant group?
  - id: seamlessLogin
    intent: Log in to a managed tenant seamlessly
    question: Can I jump straight into a customer's tenant without separate credentials?
  phrasing_ops: 6
  slug: palo-alto-networks-mssp-managed-tenant-lifecycle-endpoints-api
- baseURL: https://mssp-api.prismacloud.io
  baseurl_source: declared
  description: The MSSP Operations Retry API from Palo Alto Networks — 1 operation(s) for mssp operations retry.
  name: Palo Alto Networks MSSP Operations Retry API
  phrasing_intents:
  - id: retryOperation
    intent: Retry a failed MSSP operation
    question: Is there a way to retry a tenant operation that failed for my MSSP?
  phrasing_ops: 1
  slug: palo-alto-networks-mssp-operations-retry-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The Notifications API from Palo Alto Networks — 4 operation(s) for notifications.
  name: Palo Alto Networks Notifications API
  phrasing_intents:
  - id: postApiCloud20AggNotificationsList
    intent: List notifications across child tenants
    question: Which upgrade and announcement notifications have my child tenants received?
  - id: postApiCloud20AggNotificationsListCount
    intent: Count notifications
    question: How many unread notifications do I have?
  - id: postApiCloud20AggNotificationsListState
    intent: Mark notifications read or unread
    question: How do I mark a batch of notifications as read?
  - id: getApiCloud20AggNotificationsListStateByNotificationId
    intent: Check whether a notification is read
    question: Have I already read a particular notification?
  phrasing_ops: 4
  slug: palo-alto-networks-notifications-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Physical Connection API from Palo Alto Networks — 2 operation(s) for physical connection.
  name: Palo Alto Networks Physical Connection API
  phrasing_intents:
  - id: GetMtSp-interconnectInterconnectsPhysical-connections
    intent: List interconnect physical connections
    question: What physical links back my service provider interconnects, and what speeds do they run at?
  - id: PostMtSp-interconnectInterconnectsPhysical-connections
    intent: Provision an interconnect physical connection
    question: How do I request a new physical link at a colocation facility before setting up virtual circuits?
  - id: DeleteMtSp-interconnectInterconnectsPhysical-connectionsBy_physicalconnectionid
    intent: Decommission an interconnect physical connection
    question: How do I decommission a physical interconnect link we no longer use?
  - id: GetMtSp-interconnectInterconnectsPhysical-connectionsBy_physicalconnectionid
    intent: Get one interconnect physical connection
    question: What colocation address and HA status does a specific physical link have?
  phrasing_ops: 4
  slug: palo-alto-networks-physical-connection-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Policies API from Palo Alto Networks — 82 operation(s) for policies.
  name: Palo Alto Networks Policies API
  phrasing_intents:
  - id: validateCustomPolicy
    intent: Validate a YAML code policy definition
    question: Can I check that my YAML build policy definition is valid before saving it?
  - id: savePolicy
    intent: Save a new custom code policy
    question: How do I save a new YAML-based build policy in Prisma Cloud Application Security?
  - id: getCustomPoliciesTable
    intent: List custom code policies as a table
    question: Where can I see all the custom build policies I've written?
  - id: updatePolicy
    intent: Update a custom YAML code policy
    question: Can I edit the YAML of a custom build policy I already saved?
  - id: removePolicy
    intent: Delete a custom code policy
    question: How do I remove a custom build policy I no longer need?
  - id: policyPreview
    intent: Preview results of a code policy
    question: Can I see which resources a YAML build policy would flag before I save it?
  - id: clonePolicy
    intent: Clone an existing code policy
    question: Can I copy an existing build policy and tweak it as my own?
  - id: get-policies-compliance-ci-images
    intent: Get the CI image compliance policy (v34.03)
    question: What compliance rules apply to images scanned in CI under API v34.03?
  phrasing_ops: 166
  slug: palo-alto-networks-policies-api
- baseURL: https://mssp-api.prismacloud.io
  baseurl_source: declared
  description: 'APIs to interact with the MSSP Backend Service # Authentication'
  name: Palo Alto Networks Policy Group Lifecycle Endpoints API
  phrasing_intents:
  - id: get-policy-group-by-id
    intent: Get an MSSP policy group
    question: What policies are in a specific policy group for my MSSP tenant?
  - id: update-policy-group
    intent: Update an MSSP policy group
    question: How do I change the policies assigned to an existing policy group?
  - id: delete-policy-group
    intent: Delete an empty MSSP policy group
    question: How do I delete a policy group from my MSSP account?
  - id: get-all-policy-groups
    intent: List all MSSP policy groups
    question: Which policy groups exist across my MSSP tenant groups?
  - id: create-policy-group
    intent: Create an MSSP policy group
    question: How do I create a new policy group for my managed tenants?
  phrasing_ops: 5
  slug: palo-alto-networks-policy-group-lifecycle-endpoints-api
- baseURL: https://mssp-api.prismacloud.io
  baseurl_source: declared
  description: 'APIs to interact with the MSSP Backend Service # Authentication'
  name: Palo Alto Networks Policy Group to Tenant Group Management API
  phrasing_intents:
  - id: add-tenant-group-policy-group-mapping
    intent: Assign policy groups to a tenant group
    question: How do I apply a set of policy groups to one of my MSSP tenant groups?
  - id: delete-tenant-group-policy-group-mapping
    intent: Remove a policy group from a tenant group
    question: How do I detach a policy group from a tenant group?
  phrasing_ops: 2
  slug: palo-alto-networks-policy-group-to-tenant-group-management-api
- baseURL: https://security.api.aisecurity.paloaltonetworks.com
  baseurl_source: declared
  description: '{''$ref'': ''desc/profiles/profiles.md''}'
  name: Palo Alto Networks Profiles API
  phrasing_intents:
  - id: get-profiles-app-embedded
    intent: List app-embedded runtime profiles (v34.03)
    question: Which app-embedded Defender runtime profiles exist on the older v34.03 Compute API?
  - id: get-profiles-app-embedded-download
    intent: Export app-embedded profiles as CSV (v34.03)
    question: Can I export app-embedded runtime profiles to a file with the v34.03 API?
  - id: get-profiles-container
    intent: List runtime container profiles (v34.03)
    question: What runtime models has Defender learned for my containers, per the v34.03 API?
  - id: get-profiles-container-download
    intent: Export runtime container profiles (v34.03)
    question: Can I get container runtime profiles as a downloadable file from API v34.03?
  - id: post-profiles-container-learn
    intent: Relearn container runtime profiles (v34.03)
    question: How do I make Defender relearn container runtime models on the v34.03 API?
  - id: get-profiles-host
    intent: List runtime host profiles (v34.03)
    question: What runtime host profiles are recorded for my hosts in the v34.03 API?
  - id: get-profiles-host-download
    intent: Export runtime host profiles (v34.03)
    question: Is there a v34.03 way to download host runtime profiles as a file?
  - id: getApiV3404ProfilesAppEmbedded
    intent: List app-embedded runtime profiles
    question: What app-embedded Defender profiles are protecting my serverless and Fargate apps?
  phrasing_ops: 22
  slug: palo-alto-networks-profiles-api
- baseURL: https://mssp-api.prismacloud.io
  baseurl_source: declared
  description: The Proxy Endpoint Provider API from Palo Alto Networks — 1 operation(s) for proxy endpoint provider.
  name: Palo Alto Networks Proxy Endpoint Provider API
  phrasing_intents:
  - id: proxyRequest
    intent: Proxy a GET request through the tenant proxy
    question: Can I read data through the tenant proxy endpoint with a GET request?
  - id: proxyRequest_3
    intent: Proxy a PUT request through the tenant proxy
    question: Can I replace a resource by sending a PUT through the tenant proxy?
  - id: proxyRequest_2
    intent: Proxy a POST request through the tenant proxy
    question: Can I create something by POSTing through the tenant proxy endpoint?
  - id: proxyRequest_5
    intent: Proxy a DELETE request through the tenant proxy
    question: Can I delete a resource by sending DELETE through the tenant proxy?
  - id: proxyRequest_6
    intent: Proxy an OPTIONS request through the tenant proxy
    question: Which methods does the tenant proxy allow, via an OPTIONS preflight?
  - id: proxyRequest_1
    intent: Proxy a HEAD request through the tenant proxy
    question: Can I check headers only with a HEAD call through the tenant proxy?
  - id: proxyRequest_4
    intent: Proxy a PATCH request through the tenant proxy
    question: Can I partially update something by sending PATCH through the tenant proxy?
  phrasing_ops: 7
  slug: palo-alto-networks-proxy-endpoint-provider-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Registered UE Mappings API from Palo Alto Networks — 1 operation(s) for registered ue mappings.
  name: Palo Alto Networks Registered UE Mappings API
  phrasing_intents:
  - id: GetMtMonitor5gUeipRegistered
    intent: Count registered 5G UE mappings
    question: How many devices have registered UE-to-IP mappings on my 5G network?
  phrasing_ops: 1
  slug: palo-alto-networks-registered-ue-mappings-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/registry/registry.md''}'
  name: Palo Alto Networks Registry API
  phrasing_intents:
  - id: delete-registry-webhook-webhook
    intent: Remove the registry webhook
    question: How can I turn off the registry webhook so registries stop pushing events?
  - id: post-registry-webhook-webhook
    intent: Send a registry webhook event
    question: Can a container registry push an event to Prisma Cloud Compute through a webhook?
  - id: get-registry
    intent: Get registry scan results (v34.03)
    question: Where can I see registry image scan results using the v34.03 API version?
  - id: get-registry-download
    intent: Download registry scan results (v34.03)
    question: Can I export registry scan findings to a file with the older v34.03 endpoint?
  - id: get-registry-names
    intent: List registry image names (v34.03)
    question: What image names has the registry scanner found, per the v34.03 API?
  - id: get-registry-progress
    intent: Check registry scan progress (v34.03)
    question: Is my registry scan still running, according to the v34.03 progress endpoint?
  - id: post-registry-scan
    intent: Start a registry scan (v34.03)
    question: Can I kick off a registry scan on demand through the v34.03 API?
  - id: post-registry-scan-select
    intent: Scan selected registries (v34.03)
    question: Can I scan only a chosen set of registries rather than all of them on v34.03?
  phrasing_ops: 20
  slug: palo-alto-networks-registry-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Remote Networks API from Palo Alto Networks — 4 operation(s) for remote networks.
  name: Palo Alto Networks Remote Networks API
  phrasing_intents:
  - id: delete-v1-remote-networks
    intent: Bulk delete remote network IPSec tunnels
    question: Can I remove a whole set of IPSec tunnels sharing a prefix?
  - id: get-v1-remote-networks
    intent: Check a remote network tunnel job's status
    question: How do I check whether my bulk IPSec tunnel create, modify or delete finished?
  - id: post-v1-remote-networks
    intent: Bulk create remote network IPSec tunnels
    question: How do I create a batch of new IPSec tunnels for my branch sites?
  - id: put-v1-remote-networks
    intent: Bulk modify remote network IPSec tunnels
    question: Can I modify many remote network IPSec tunnels in one request?
  - id: get-v1-remote-networks-read
    intent: Read IPSec tunnel status results
    question: Where do I pick up the tunnel status results from a read request I queued?
  - id: post-v1-remote-networks-read
    intent: Request a read of IPSec tunnels
    question: Can I ask for the status of specific remote network tunnels?
  - id: listRemoteNetworks
    intent: List Prisma Access remote networks
    question: Which branch and data center sites are connected to Prisma Access as remote networks?
  - id: createRemoteNetwork
    intent: Create a Prisma Access remote network
    question: How do I connect a new branch office to Prisma Access as a remote network?
  phrasing_ops: 17
  slug: palo-alto-networks-remote-networks-api
- baseURL: https://api.sase.paloaltonetworks.com/ai-red-teaming/data-plane
  baseurl_source: declared
  description: Operations for generating and retrieving scan job reports for static and dynamic.
  name: Palo Alto Networks Report API
  phrasing_intents:
  - id: list_attacks_v1_report_static__job_id__list_attacks_get
    intent: List attacks run in an attack library scan
    question: Which attacks succeeded against my AI model in an attack library scan?
  - id: get_attack_detail_v1_report_static__job_id__attack__attack_id__get
    intent: Get one single-turn attack's details
    question: What did the model output for a specific attack in my scan?
  - id: get_attack_report_v1_report_static__job_id__report_get
    intent: Get the attack library scan report
    question: Where do I read the summary report for an attack library red teaming scan?
  - id: get_static_runtime_security_policy_config_v1_report_static__job_id__runtime_policy_config_get
    intent: Get runtime profile suggested by a library scan
    question: What runtime security profile is recommended from my attack library scan?
  - id: get_static_remediations_v1_report_static__job_id__remediation_get
    intent: Get remediation steps from a library scan
    question: Beyond runtime protection, what other fixes does an attack library scan suggest?
  - id: get_dynamic_job_report_v1_report_dynamic__job_id__report_get
    intent: Get the agent scan report
    question: Where do I see the results of a dynamic agent red teaming scan?
  - id: get_dynamic_runtime_security_policy_config_v1_report_dynamic__job_id__runtime_policy_config_get
    intent: Get runtime profile suggested by an agent scan
    question: Which runtime security profile should protect my agent based on its dynamic scan?
  - id: get_dynamic_remediations_v1_report_dynamic__job_id__remediation_get
    intent: Get remediation steps from an agent scan
    question: What should I fix in my AI agent after a dynamic scan?
  phrasing_ops: 17
  slug: palo-alto-networks-report-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: 'Creating compliance reports is the best way to monitor your cloud accounts across all cloud types and ensure that you are adhering to all compliance standards. You can create compliance reports based '
  name: Palo Alto Networks Reports API
  phrasing_intents:
  - id: list-reports
    intent: List compliance report configurations
    question: Which compliance reports are configured for my cloud accounts?
  - id: save-report
    intent: Create a compliance report configuration
    question: How do I set up a recurring compliance report for my AWS accounts?
  - id: get-report-types
    intent: List compliance report types by cloud
    question: What compliance report types are available for each cloud type?
  - id: get-specified-report
    intent: Get a compliance report configuration
    question: How do I see the settings and pass/fail counts of one report config?
  - id: update-report
    intent: Update a compliance report configuration
    question: Can I change the schedule of an existing recurring compliance report?
  - id: delete-report
    intent: Delete a compliance report configuration
    question: How do I remove a compliance report configuration I no longer need?
  - id: download-report
    intent: Download the latest compliance report
    question: How do I download the most recent run of a scheduled compliance report?
  - id: get-historical-report-by-id
    intent: List past runs of a scheduled report
    question: What past runs exist for a scheduled compliance report?
  phrasing_ops: 16
  slug: palo-alto-networks-reports-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Repositories API from Palo Alto Networks — 6 operation(s) for repositories.
  name: Palo Alto Networks Repositories API
  phrasing_intents:
  - id: getRepositories
    intent: List integrated code repositories
    question: Which repositories are integrated with Application Security, and who owns them?
  - id: updateRepositories
    intent: Onboard multiple repositories for an integration
    question: How do I onboard a batch of repositories from one VCS integration at once?
  - id: getBranches
    intent: List a repository's branches with CI/CD runs
    question: Which branches of a repository have had CI/CD runs, and what was their status?
  - id: getQueryRepositories
    intent: Map repository UUIDs to repository names
    question: How do I turn a list of repository UUIDs into readable repository names?
  - id: searchRepositories
    intent: Search repositories by owner, name or source
    question: How can I find a repository by owner and name among everything I have connected?
  - id: getVCSRepositoryPage
    intent: Page through VCS repositories (code API path)
    question: Is there a filtered, paged repositories view under the /code API path?
  - id: getVCSRepository
    intent: List repositories with technologies and pipelines
    question: What technologies, pipelines and contributors does each of my repositories have?
  - id: postApiV1VcsRepositoryRepositories
    intent: Page through VCS repositories with filters
    question: How do I get a filtered page of VCS repositories through the /api/v1 repositories POST?
  phrasing_ops: 11
  slug: palo-alto-networks-repositories-api
- baseURL: https://api.sase.paloaltonetworks.com/iam/v1
  baseurl_source: declared
  description: The Roles API from Palo Alto Networks — 2 operation(s) for roles.
  name: Palo Alto Networks Roles API
  phrasing_intents:
  - id: listRoles
    intent: List assignable IAM roles
    question: Which roles can I assign in SASE access policies?
  - id: get-iam-v1-roles
    intent: List all IAM roles
    question: What roles exist in the IAM v1 service?
  - id: get-iam-v1-roles-name
    intent: Get an IAM role
    question: What does a specific IAM role allow?
  phrasing_ops: 3
  slug: palo-alto-networks-roles-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The SaaS Instance API from Palo Alto Networks — 7 operation(s) for saas instance.
  name: Palo Alto Networks SaaS Instance API
  phrasing_intents:
  - id: saas_instances_get
    intent: List connected SaaS instances
    question: Which SaaS applications are connected to my SSPM tenant?
  - id: saas_instances_saas_accounts_get
    intent: List user accounts in a SaaS instance
    question: Who has an account in one of my connected SaaS apps, and what roles do they hold?
  - id: saas_instances_saas_accounts_count_get
    intent: Count user accounts in a SaaS instance
    question: How many user accounts exist in a given SaaS app?
  - id: saas_instances_saas_accounts_count_csv_report_post
    intent: Generate a CSV report of SaaS accounts
    question: Can I get a CSV export of everyone who has access to a SaaS app for an audit?
  - id: saas_instances_saas_activity_get
    intent: Get activity logs for a SaaS instance
    question: What have users been doing inside a connected SaaS app, and from where?
  - id: saas_instances_tickets_get
    intent: List remediation tickets for a SaaS instance
    question: Which remediation tickets are open for misconfigurations in a SaaS app?
  - id: saas_instances_tickets_post
    intent: Open a remediation ticket for a SaaS instance
    question: How do I open a ticket to track fixing a flagged SaaS misconfiguration?
  - id: saas_instances_tickets_delete
    intent: Delete or unlink SaaS instance tickets
    question: How do I unlink a resolved ticket from a SaaS instance?
  phrasing_ops: 9
  slug: palo-alto-networks-saas-instance-api
- baseURL: https://security.api.aisecurity.paloaltonetworks.com
  baseurl_source: declared
  description: Operations for creating and managing scan jobs.
  name: Palo Alto Networks Scan API
  phrasing_intents:
  - id: submitScanSync
    intent: Scan an AI prompt or response synchronously
    question: How do I check a user prompt or model response for threats and get the verdict right away?
  - id: submitScanAsync
    intent: Submit an asynchronous AI security scan
    question: Can I queue AI prompt scans in the background and get a scan ID and report ID back?
  - id: getAsyncScanResults
    intent: Get results of an asynchronous scan
    question: Has my asynchronous prompt scan finished, and what did it detect?
  - id: create_job_v1_scan_post
    intent: Create a scan job against a target
    question: How do I start a new red-team style scan against one of my AI targets?
  - id: list_jobs_v1_scan_get
    intent: List scan jobs
    question: Which scan jobs are running or finished for my AI targets?
  - id: get_job_v1_scan__job_id__get
    intent: Get details of a scan job
    question: What's the current status and configuration of a specific scan job?
  - id: abort_job_v1_scan__job_id__abort_post
    intent: Abort a running scan job
    question: How do I stop a scan job that's still running?
  phrasing_ops: 7
  slug: palo-alto-networks-scan-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Scans API from Palo Alto Networks — 14 operation(s) for scans.
  name: Palo Alto Networks Scans API
  phrasing_intents:
  - id: scanIntegrations
    intent: Refresh all resources with a full integration scan
    question: How do I force Application Security to rescan every cloud and IaC resource across my integrations?
  - id: get-scans
    intent: List CI image scan results (v34.03)
    question: Where can I list all CI image scan results on the older v34.03 Compute API?
  - id: post-scans
    intent: Add a CLI scan result (v34.03)
    question: How do I push a twistcli scan result into Console through the v34.03 API?
  - id: get-scans-download
    intent: Download CI image scan results (v34.03)
    question: How can I export CI image scan results as a file from the v34.03 API?
  - id: get-scans-id
    intent: Get one CI image scan result (v34.03)
    question: How do I fetch a single CI image scan result by ID on the v34.03 API?
  - id: getApiV3404Scans
    intent: List CI image scan results (v34.04)
    question: Which CI image scans failed in the latest v34.04 Compute API results?
  - id: postApiV3404Scans
    intent: Add a CLI scan result (v34.04)
    question: How do I submit a CLI scan result to the current v34.04 scans endpoint?
  - id: getApiV3404ScansDownload
    intent: Download CI image scan results (v34.04)
    question: Can I download CI image scan results as a report file from the v34.04 API?
  phrasing_ops: 18
  slug: palo-alto-networks-scans-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: You can use the Resource Query Language (RQL) to perform configuration checks across cloud services as well as gain real-time insights into user and network events to gain security visibility and crea
  name: Palo Alto Networks Search API
  phrasing_intents:
  - id: search-config
    intent: Run an RQL config search
    question: How do I run an RQL config query to find misconfigured cloud resources in Prisma Cloud?
  - id: search-network
    intent: Search network flow logs with RQL
    question: How can I query cloud flow logs to see which network traffic reached a resource?
  - id: search-events
    intent: Search audit events with RQL
    question: How do I find console and API access events in the audit log using RQL?
  - id: search-events-aggregated
    intent: Run an aggregated audit event search
    question: Can I get audit event results broken down by location and service?
  - id: search-events-filtered
    intent: Filter audit event search results
    question: How do I narrow down the results of an aggregated audit event search with extra filters?
  - id: search-events-page
    intent: Get the next page of audit event results
    question: My audit event search returned over 100 results — how do I fetch the next page?
  - id: search-events-raw
    intent: Get raw metadata for an audit event
    question: How do I see the raw metadata behind a single audit event?
  - id: search-suggest
    intent: Autocomplete a partial RQL query
    question: What can I type next to finish a partial RQL query?
  phrasing_ops: 20
  slug: palo-alto-networks-search-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: The Services API from Palo Alto Networks — 12 operation(s) for services.
  name: Palo Alto Networks Services API
  phrasing_intents:
  - id: getServices
    intent: Find internet-exposed services
    question: Which open ports and protocols are exposed to the internet on my assets?
  - id: ListServices
    intent: List service objects
    question: Which service objects are defined in my security configuration folder?
  - id: CreateServices
    intent: Create a service object
    question: How do I define a new service object with a protocol and port?
  - id: GetServicesByID
    intent: Get a service object
    question: What protocol and ports does a specific service object define?
  - id: UpdateServicesByID
    intent: Update a service object
    question: Can I change the port on an existing service object?
  - id: DeleteServicesByID
    intent: Delete a service object
    question: Can I remove a service object that no rule uses anymore?
  phrasing_ops: 6
  slug: palo-alto-networks-services-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: '{''$ref'': ''desc/settings/settings.md''}'
  name: Palo Alto Networks Settings API
  phrasing_intents:
  - id: post-settings-certificates
    intent: Set custom CA client cert settings (v34.03)
    question: Can I upload a custom CA certificate through the v34.03 settings API?
  - id: get-settings-certs
    intent: Get Compute certificate settings (v34.03)
    question: What does the v34.03 API report for Compute certificate settings?
  - id: post-settings-certs
    intent: Set Compute certificate settings (v34.03)
    question: Can I change the console SAN list via the v34.03 API?
  - id: post-settings-console-certificate
    intent: Set console access cert settings (v34.03)
    question: Can I set a custom console certificate through the v34.03 API?
  - id: get-settings-custom-labels
    intent: Get custom alert labels (v34.03)
    question: Which alert labels does the v34.03 API return?
  - id: post-settings-custom-labels
    intent: Set custom alert labels (v34.03)
    question: Can I add alert labels through the v34.03 settings API?
  - id: get-settings-defender
    intent: Get advanced Defender settings (v34.03)
    question: What does the v34.03 API return for advanced Defender settings?
  - id: get-settings-intelligence
    intent: Get Intelligence Stream settings (v34.03)
    question: What Intelligence Stream settings does the v34.03 API report?
  phrasing_ops: 84
  slug: palo-alto-networks-settings-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Onboarding Sites information
  name: Palo Alto Networks Sites API
  phrasing_intents:
  - id: listSites
    intent: List SD-WAN sites
    question: Which SD-WAN branch and data center sites are configured in my tenant?
  - id: createSite
    intent: Create an SD-WAN site
    question: How do I add a new branch office as an SD-WAN site?
  - id: getSite
    intent: Get an SD-WAN site's configuration
    question: What is the configuration of a specific SD-WAN site?
  - id: updateSite
    intent: Update an SD-WAN site
    question: How do I change the address or tags of an SD-WAN site?
  - id: deleteSite
    intent: Delete an SD-WAN site
    question: What happens to associated configuration when I delete an SD-WAN site?
  - id: createSites
    intent: Bulk-create sites all-or-nothing
    question: Can I create several sites at once and have none created if one fails validation?
  - id: getSites
    intent: List sites with claims and resolution history
    question: Which sites are still unclaimed, and what is their resolution history?
  - id: getSiteByID
    intent: Get a site with its claims
    question: Who has claimed a particular site and how was it resolved?
  phrasing_ops: 10
  slug: palo-alto-networks-sites-api
- baseURL: https://mssp-api.prismacloud.io
  baseurl_source: declared
  description: The Stack Details Endpoint API from Palo Alto Networks — 1 operation(s) for stack details endpoint.
  name: Palo Alto Networks Stack Details Endpoint API
  phrasing_intents:
  - id: requestStackMapping
    intent: List stacks and their API hosts
    question: Which API host should I call for my stack?
  phrasing_ops: 1
  slug: palo-alto-networks-stack-details-endpoint-api
- baseURL: https://api.threatvault.paloaltonetworks.com/service/v1
  baseurl_source: declared
  description: '{''$ref'': ''desc/stats/stats.md''}'
  name: Palo Alto Networks Stats API
  phrasing_intents:
  - id: get-stats-app-firewall-count
    intent: Count app firewalls (v34.03)
    question: How many application firewalls are deployed according to the v34.03 stats endpoint?
  - id: get-stats-compliance
    intent: Get compliance stats (v34.03)
    question: What do my compliance statistics look like on the v34.03 API?
  - id: get-stats-compliance-download
    intent: Download compliance stats as a file (v34.03)
    question: Can I export compliance statistics to a file with the v34.03 API?
  - id: post-stats-compliance-refresh
    intent: Recalculate compliance stats (v34.03)
    question: How do I force the v34.03 compliance statistics to recalculate?
  - id: get-stats-daily
    intent: Get daily compliance trend (v34.03)
    question: Where can I see day-by-day compliance numbers on the v34.03 API?
  - id: get-stats-dashboard
    intent: Get dashboard summary stats (v34.03)
    question: What numbers feed the Compute dashboard on the v34.03 API?
  - id: get-stats-events
    intent: Get runtime event stats (v34.03)
    question: How many security events were recorded in a time window on the v34.03 API?
  - id: get-stats-license
    intent: Get license usage stats (v34.03)
    question: How much of my license am I consuming according to the v34.03 stats API?
  phrasing_ops: 27
  slug: palo-alto-networks-stats-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Suppressions API from Palo Alto Networks — 4 operation(s) for suppressions.
  name: Palo Alto Networks Suppressions API
  phrasing_intents:
  - id: getSuppressions
    intent: List Code Security suppression rules
    question: Which suppression rules are turned on in Prisma Cloud Application Security?
  - id: createSuppression
    intent: Suppress a policy by policy ID
    question: How do I snooze or dismiss a Code Security policy by its policy ID?
  - id: updateSuppression
    intent: Update a suppression under a policy
    question: How do I edit an existing suppression rule attached to a policy?
  - id: deleteSuppression
    intent: Delete a suppression under a policy
    question: How do I remove a suppression tied to a specific policy and suppression ID?
  - id: getSuppressionsJustifications
    intent: Get a policy's suppression justifications
    question: Why was a policy suppressed for certain accounts or repositories?
  - id: listSuppressions
    intent: List suppressions by policy or scope
    question: Which suppressions exist for a particular Checkov policy ID?
  - id: postSuppressions
    intent: Create a scoped suppression with expiry
    question: How do I suppress a Checkov policy for specific resources as an accepted risk?
  - id: deleteSuppressionsBySuppressionId
    intent: Delete a suppression by its ID
    question: How do I delete a suppression rule using only its suppression ID?
  phrasing_ops: 8
  slug: palo-alto-networks-suppressions-api
- baseURL: https://mssp-api.prismacloud.io
  baseurl_source: declared
  description: The Tenant Group Lifecycle Endpoints API from Palo Alto Networks — 2 operation(s) for tenant group lifecycle endpoints.
  name: Palo Alto Networks Tenant Group Lifecycle Endpoints API
  phrasing_intents:
  - id: getTenantGroupsByMsspId
    intent: List an MSSP's tenant groups
    question: Which tenant groups has my MSSP created for its managed tenants?
  - id: createTenantGroup
    intent: Create an MSSP tenant group
    question: How do I group several managed tenants together as an MSSP?
  - id: getTenantGroupById
    intent: Get an MSSP tenant group
    question: Which managed tenants belong to a specific tenant group?
  - id: deleteTenantGroupById
    intent: Delete an empty MSSP tenant group
    question: Can I delete a tenant group that still contains tenants?
  - id: patchTenantGroupById
    intent: Modify an MSSP tenant group
    question: Can I rename a tenant group or change which tenants it holds?
  phrasing_ops: 5
  slug: palo-alto-networks-tenant-group-lifecycle-endpoints-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Throughput Trend API from Palo Alto Networks — 1 operation(s) for throughput trend.
  name: Palo Alto Networks Throughput Trend API
  phrasing_intents:
  - id: PostMtMonitor5gInterconnectThroughput
    intent: Get 5G interconnect throughput trend
    question: How has ingress and egress throughput on my 5G interconnect changed over time?
  phrasing_ops: 1
  slug: palo-alto-networks-throughput-trend-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Total Number of Configured Users API from Palo Alto Networks — 1 operation(s) for total number of configured users.
  name: Palo Alto Networks Total Number of Configured Users API
  phrasing_intents:
  - id: GetMtMonitor5gUsers
    intent: Count configured 5G users
    question: How many users are configured on the 5G service?
  phrasing_ops: 1
  slug: palo-alto-networks-total-number-of-configured-users-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Total Proxies API from Palo Alto Networks — 1 operation(s) for total proxies.
  name: Palo Alto Networks Total Proxies API
  phrasing_intents:
  - id: GetMtMonitor5gProxy
    intent: Count configured 5G proxy servers
    question: How many proxy servers are configured in my 5G setup?
  phrasing_ops: 1
  slug: palo-alto-networks-total-proxies-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Total Tenants API from Palo Alto Networks — 1 operation(s) for total tenants.
  name: Palo Alto Networks Total Tenants API
  phrasing_intents:
  - id: GetMtMonitor5gTenants
    intent: Count 5G monitoring tenants
    question: How many tenants are in my 5G security monitoring?
  phrasing_ops: 1
  slug: palo-alto-networks-total-tenants-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The UE IP Region API from Palo Alto Networks — 1 operation(s) for ue ip region.
  name: Palo Alto Networks UE IP Region API
  phrasing_intents:
  - id: GetMtMonitor5gUeipRegion
    intent: List regions with registered UEs
    question: In which regions are 5G UEs registered?
  phrasing_ops: 1
  slug: palo-alto-networks-ue-ip-region-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The UE Mappings API from Palo Alto Networks — 1 operation(s) for ue mappings.
  name: Palo Alto Networks UE Mappings API
  phrasing_intents:
  - id: PostMtMonitor5gMapping
    intent: List or search 5G UE mappings
    question: How do I find a 5G device's mapping by IMSI, IMEI or IP address?
  phrasing_ops: 1
  slug: palo-alto-networks-ue-mappings-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Unknown IP Regions API from Palo Alto Networks — 1 operation(s) for unknown ip regions.
  name: Palo Alto Networks Unknown IP  Regions API
  phrasing_intents:
  - id: GetMtMonitor5gUnknownipRegion
    intent: Show regions where unknown 5G IPs are seen
    question: In which regions are unknown IP addresses showing up on my 5G network?
  phrasing_ops: 1
  slug: palo-alto-networks-unknown-ip-regions-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Unknown UE Mappings API from Palo Alto Networks — 1 operation(s) for unknown ue mappings.
  name: Palo Alto Networks Unknown UE Mappings API
  phrasing_intents:
  - id: GetMtMonitor5gMappingUnknownues
    intent: Count unknown 5G UE mappings
    question: How many UE mappings registered through RADIUS or the API were never configured by me?
  phrasing_ops: 1
  slug: palo-alto-networks-unknown-ue-mappings-api
- baseURL: https://mssp-api.prismacloud.io
  baseurl_source: declared
  description: The User Authentication API from Palo Alto Networks — 2 operation(s) for user authentication.
  name: Palo Alto Networks User Authentication API
  phrasing_intents:
  - id: processLogin
    intent: Log in with username and password
    question: What's the way to sign in with a username and password to get a token?
  - id: refreshToken
    intent: Refresh a user JWT for an MSSP
    question: Can I refresh my JWT before it expires?
  phrasing_ops: 2
  slug: palo-alto-networks-user-authentication-api
- baseURL: https://mssp-api.prismacloud.io
  baseurl_source: declared
  description: The User Management API from Palo Alto Networks — 5 operation(s) for user management.
  name: Palo Alto Networks User Management API
  phrasing_intents:
  - id: resetPassword
    intent: Change a user's password
    question: How do I set a new password for a user account?
  - id: getUser
    intent: Look up an MSSP console user
    question: What are the first and last names on a user in my MSSP console?
  - id: updateUser
    intent: Update an MSSP console user
    question: Can I correct a user's first or last name in the MSSP console?
  - id: deleteUser
    intent: Delete an MSSP console user
    question: How do I remove a user from an MSSP account?
  - id: validateToken
    intent: Validate a forgot-password reset token
    question: What happens after a user submits the password reset token from their email?
  - id: listUsers
    intent: List users of an MSSP console
    question: Who has user access to my managed security service provider console?
  - id: createUser
    intent: Add a user to an MSSP account
    question: How do I give a new person access to an MSSP account?
  - id: resetToken
    intent: Email a user a password reset token
    question: How does a user who forgot their password get a reset email?
  phrasing_ops: 8
  slug: palo-alto-networks-user-management-api
- baseURL: https://api.stratacloud.paloaltonetworks.com/aiops/bpa/v1
  baseurl_source: declared
  description: The Users API from Palo Alto Networks — 11 operation(s) for users.
  name: Palo Alto Networks Users API
  phrasing_intents:
  - id: GetSeb-apiV1Users
    intent: List Prisma Browser users with filters
    question: Which Prisma Browser users are currently suspended?
  - id: GetSeb-apiV1Usersbyid
    intent: Get one Prisma Browser user by ID
    question: How do I look up the details of a single Prisma Browser user by their ID?
  - id: PostSeb-apiV1UsersSuspend
    intent: Suspend Prisma Browser users
    question: How do I cut off a user's access to Prisma Browser on all their devices?
  - id: PostSeb-apiV1UsersResume
    intent: Reactivate suspended Prisma Browser users
    question: How can I give a suspended user their Prisma Browser access back?
  - id: PostSeb-apiV1UsersForce-reauth
    intent: Force users to re-authenticate in the browser
    question: Can I make a user sign in to Prisma Browser again on all of their devices?
  - id: get-users
    intent: List Compute console users (v34.03 API)
    question: Which console users exist in Prisma Cloud Compute on the v34.03 API?
  - id: post-users
    intent: Add a Compute console user (v34.03 API)
    question: How do I create a new Compute console user with the v34.03 API?
  - id: put-users
    intent: Update a Compute console user (v34.03 API)
    question: Can I change a Compute user's role through the v34.03 API?
  phrasing_ops: 19
  slug: palo-alto-networks-users-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Vlan Attachment API from Palo Alto Networks — 4 operation(s) for vlan attachment.
  name: Palo Alto Networks Vlan Attachment API
  phrasing_intents:
  - id: GetMtSp-interconnectInterconnectsBy_interconnectidVlan-attachments
    intent: List VLAN attachments on an interconnect
    question: Which virtual circuits are configured on my service provider interconnect?
  - id: PostMtSp-interconnectInterconnectsBy_interconnectidVlan-attachments
    intent: Provision a VLAN attachment
    question: How do I create a new virtual circuit for Prisma Access traffic on an interconnect?
  - id: GetMtSp-interconnectInterconnectsBy_interconnectidVlan-attachmentsBy_vlanattachmentid
    intent: Get a VLAN attachment
    question: What BGP timers and MD5 settings does one virtual circuit use?
  - id: DeleteMtSp-interconnectInterconnectsBy_interconnectidVlan-attachmentsBy_vlanattachmentid
    intent: Delete a VLAN attachment
    question: How do I retire a virtual circuit on an interconnect?
  - id: PostMtSp-interconnectInterconnectsBy_interconnectidVlan-attachmentsBy_vlanattachmentidAccept
    intent: Accept a pending AWS attachment
    question: My AWS Direct Connect attachment is pending acceptance; how do I confirm it?
  - id: GetMtSp-interconnectInterconnectsBy_interconnectidVlan-attachmentsBy_vlanattachmentidLogs
    intent: Get Cloud Router logs for an attachment
    question: Can I pull GCP Cloud Router logs for a VLAN attachment?
  phrasing_ops: 6
  slug: palo-alto-networks-vlan-attachment-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Access Keys are a secure way to enable programmatic access to the Prisma Cloud API. By default, only the System Admin has API access and can enable API access for other administrators. If you have API
  name: Palo Alto Networks Access Keys API
  phrasing_intents:
  - id: get-my-access-keys
    intent: List access keys
    question: Which Prisma Cloud access keys exist for me or my tenant?
  - id: add-access-keys
    intent: Create an access key
    question: How do I generate a new API access key for myself?
  - id: get-access-key-by-id
    intent: Get an access key's metadata
    question: When does a specific access key expire and who owns it?
  - id: delete-access-keys
    intent: Delete an access key
    question: How do I permanently delete an access key that leaked?
  - id: update-access-key-status
    intent: Activate or deactivate an access key
    question: Can I temporarily deactivate an access key instead of deleting it?
  phrasing_ops: 5
  slug: palo-alto-networks-access-keys-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: You can use Account Groups to combine access to multiple cloud accounts with similar or different applications that span multiple divisions or business units, so that you can manage administrative acc
  name: Palo Alto Networks Account Groups API
  phrasing_intents:
  - id: get-account-groups
    intent: List account groups with details
    question: Which account groups can I access in Prisma Cloud?
  - id: add-account-group
    intent: Create an account group
    question: How do I group several cloud accounts together in Prisma Cloud?
  - id: get-account-group-name
    intent: List account group IDs and names
    question: What are the names and IDs of all my account groups?
  - id: get-account-group-name-by-cloudType
    intent: List account group names for a cloud type
    question: Which account groups contain AWS accounts versus Azure or GCP?
  - id: get-account-group
    intent: Get an account group's details
    question: What cloud accounts belong to a specific account group?
  - id: update-account-group
    intent: Update an account group
    question: How do I add or remove cloud accounts from an existing account group?
  - id: delete-account-group
    intent: Delete an account group
    question: How do I remove an account group I no longer need?
  phrasing_ops: 7
  slug: palo-alto-networks-account-groups-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Action Plan Management APIs
  name: Palo Alto Networks Action Plan Management APIs API
  phrasing_intents:
  - id: list-action-plans
    intent: List action plans by criticality
    question: What action plans does my tenant have, most critical first?
  - id: update-an-action-plan
    intent: Change an action plan's status or assignee
    question: How do I reassign an action plan to someone else?
  - id: update-an-action-plan-feedback
    intent: Give thumbs up or down feedback on an action plan
    question: Can I tell Prisma Cloud an action plan wasn't useful?
  - id: recommendation-summary-action-plan
    intent: Summarize remediation recommendations for a plan
    question: What do the policy recommendations behind an action plan add up to?
  - id: action-plan-related-alerts
    intent: List alerts related to an action plan
    question: Which alerts are tied to a given action plan?
  - id: action-plan-impacted-assets
    intent: List assets impacted by an action plan
    question: Which cloud assets are affected by an action plan?
  - id: action-plan-notification-service
    intent: Send a Jira or Slack notification for a plan
    question: How do I push an action plan to Jira or Slack on demand?
  - id: get-action-plan-names
    intent: List action plan names
    question: What are the names of all my action plans?
  phrasing_ops: 12
  slug: palo-alto-networks-action-plan-management-apis-api
- baseURL: https://api.sase.paloaltonetworks.com/ai-red-teaming/mgmt-plane
  baseurl_source: declared
  description: Operations for managing custom target adapters.
  name: Palo Alto Networks Adapters API
  phrasing_intents:
  - id: create_adapter_v1_adapters_post
    intent: Create a red teaming adapter
    question: How do I create an adapter script that connects red teaming to my AI endpoint?
  - id: list_adapters_v1_adapters_get
    intent: List red teaming target adapters
    question: Which red teaming adapters are set up for my AI targets?
  - id: get_adapter_config_v1_adapters_config_get
    intent: Get adapter configuration defaults
    question: What default settings apply to new red teaming adapters?
  - id: get_adapter_v1_adapters__adapter_uuid__get
    intent: Get a red teaming adapter
    question: How do I view the details of one adapter by its UUID?
  - id: update_adapter_v1_adapters__adapter_uuid__put
    intent: Update a red teaming adapter
    question: How do I change the script of an existing adapter?
  - id: delete_adapter_v1_adapters__adapter_uuid__delete
    intent: Delete a red teaming adapter
    question: How do I remove an adapter I no longer need?
  - id: validate_adapter_v1_adapters_validate_post
    intent: Validate an adapter script end to end
    question: Can I test an adapter script against my target before saving it?
  phrasing_ops: 7
  slug: palo-alto-networks-adapters-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: Address Groups
  name: Palo Alto Networks Address Groups API
  phrasing_intents:
  - id: ListAddressGroups
    intent: List address groups
    question: Which address groups exist in a given folder?
  - id: CreateAddressGroups
    intent: Create an address group
    question: How do I create a new address group with a description and tags?
  - id: GetAddressGroupsByID
    intent: Get an address group
    question: What's configured on a specific address group?
  - id: UpdateAddressGroupsByID
    intent: Update an address group
    question: Can I rename an existing address group or change its tags?
  - id: DeleteAddressGroupsByID
    intent: Delete an address group
    question: How do I remove an address group I no longer use?
  - id: listAddressGroups
    intent: List firewall address groups
    question: Which address groups are configured on my firewall, static and dynamic?
  - id: createAddressGroup
    intent: Create a static or dynamic address group
    question: Can I build an address group that picks up addresses automatically by tag?
  - id: getAddressGroup
    intent: Get an address group
    question: What members or filter does a specific address group have?
  phrasing_ops: 10
  slug: palo-alto-networks-address-groups-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Adoption Advisor API provides visibility into which Prisma Cloud capabilities you have adopted and helps you uncover security capabilities that you not have yet explored.
  name: Palo Alto Networks Adoption Advisor API
  phrasing_intents:
  - id: get-adoption-check-score
    intent: Get the adoption check score
    question: Which Prisma Cloud capabilities have we adopted and which are still unused?
  - id: adoption-advisor-get-all-report-configs
    intent: List Adoption Advisor report configs
    question: What scheduled Adoption Advisor reports are configured?
  - id: create-adoption-advisor-config
    intent: Schedule an Adoption Advisor report
    question: How do I schedule a recurring Adoption Advisor report by email?
  - id: adoption-advisor-create-report
    intent: Generate an Adoption Advisor report now
    question: Can I generate an Adoption Advisor report immediately instead of waiting for the schedule?
  - id: adoption-advisor-update-report
    intent: Update an Adoption Advisor report
    question: Can I change the recipients or schedule of an existing Adoption Advisor report?
  - id: adoption-advisor-delete-report
    intent: Delete an Adoption Advisor report
    question: How do I stop and remove an Adoption Advisor report configuration?
  - id: adoption-advisor-download-latest-report
    intent: Download the latest Adoption Advisor report
    question: Where can I download the most recent run of an Adoption Advisor report?
  - id: adoption-advisor-download-report-by-id-and-creation-time
    intent: Download a past Adoption Advisor report run
    question: Can I download an older Adoption Advisor report from a specific date?
  phrasing_ops: 8
  slug: palo-alto-networks-adoption-advisor-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: Advanced Device Objects
  name: Palo Alto Networks Advanced Device Objects API
  phrasing_intents:
  - id: ListAdvancedDeviceObjects
    intent: List advanced device objects
    question: What advanced device objects exist in a folder or snippet?
  - id: CreateAdvancedDeviceObjects
    intent: Create an advanced device object
    question: How do I create a new advanced device object?
  - id: UpdateAdvancedDeviceObjectsByPath
    intent: Update an advanced device object by name
    question: Can I update an advanced device object by name and folder instead of by ID?
  - id: DeleteAdvancedDeviceObjectsByNames
    intent: Delete advanced device objects by name
    question: Can I delete several advanced device objects by their names at once?
  - id: GetAdvancedDeviceObjectsByID
    intent: Get an advanced device object
    question: How can I look up one advanced device object by its ID?
  - id: UpdateAdvancedDeviceObjectsByID
    intent: Update an advanced device object by ID
    question: Can I rename an advanced device object when I have its ID?
  - id: DeleteAdvancedDeviceObjectsByID
    intent: Delete an advanced device object by ID
    question: How do I delete one advanced device object using its ID?
  phrasing_ops: 7
  slug: palo-alto-networks-advanced-device-objects-api
- baseURL: https://api.threatvault.paloaltonetworks.com/service/v1
  baseurl_source: declared
  description: The Advanced Threat Prevention API from Palo Alto Networks — 2 operation(s) for advanced threat prevention.
  name: Palo Alto Networks Advanced Threat Prevention API
  phrasing_intents:
  - id: postatpreportsbatchmode
    intent: Get Advanced Threat Prevention reports in batch
    question: Can I pull several Advanced Threat Prevention reports at once by report ID?
  - id: getatppcaps
    intent: Download packet captures for an ATP report
    question: How do I download the PCAP recorded during a threat's analysis?
  phrasing_ops: 2
  slug: palo-alto-networks-advanced-threat-prevention-api
- baseURL: https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
  baseurl_source: declared
  description: Agent Authentication Settings
  name: Palo Alto Networks Agent Authentication Settings API
  phrasing_intents:
  - id: GetGlobalProtectAuthenticationSettings
    intent: List GlobalProtect authentication settings
    question: Which GlobalProtect agent authentication settings are configured?
  - id: CreateGlobalProtectAuthenticationSettings
    intent: Create a GlobalProtect authentication setting
    question: How do I add a new GlobalProtect authentication setting for a specific operating system?
  - id: UpdateGlobalProtectAuthenticationSettings
    intent: Update a GlobalProtect authentication setting
    question: How do I change which authentication profile an existing GlobalProtect setting uses?
  - id: DeleteGlobalProtectAuthenticationSettings
    intent: Delete a GlobalProtect authentication setting
    question: How do I remove a GlobalProtect authentication setting by name?
  - id: MoveGlobalProtectAuthenticationSettings
    intent: Reorder a GlobalProtect authentication setting
    question: How do I change the evaluation order of GlobalProtect authentication settings?
  phrasing_ops: 5
  slug: palo-alto-networks-agent-authentication-settings-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Retrieve the agent client version distribution, providing agent details.
  name: Palo Alto Networks Agent Users API
  phrasing_intents:
  - id: post-insights-v3.0-resource-export-query-users-agent-user_list
    intent: Export the list of agent users
    question: Can I export the full list of GlobalProtect agent users to a file?
  - id: post-insights-v3.0-resource-query-users-agent-client_version_distribution
    intent: Show agent client version distribution
    question: Which agent client versions are my users running, and how many of each?
  - id: post-insights-v3.0-resource-query-users-agent-connected_entity_count
    intent: Count connected entities
    question: How many entities are connected through the agent right now under a given filter?
  - id: post-insights-v3.0-resource-query-users-agent-connected_user_count_histogram
    intent: Chart connected users over time
    question: What does the number of connected agent users look like over time?
  - id: post-insights-v3.0-resource-query-users-agent-connected_user_device_count_histogram
    intent: Chart connected user devices over time
    question: How has the number of connected user devices changed over time?
  - id: post-insights-v3.0-resource-query-users-agent-current_connected_device_count
    intent: Count devices connected right now
    question: How many devices are connected through the agent at this moment?
  - id: post-insights-v3.0-resource-query-users-agent-current_connected_user_count
    intent: Count users connected right now
    question: How many agent users are connected at this moment?
  - id: post-insights-v3.0-resource-query-users-agent-device_list
    intent: List agent devices
    question: Which devices have the agent installed and connected?
  phrasing_ops: 12
  slug: palo-alto-networks-agent-users-api-api
- baseURL: https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
  baseurl_source: declared
  description: Agent Versions
  name: Palo Alto Networks Agent Versions API
  phrasing_intents:
  - id: ListGlobalProtectVersions
    intent: List GlobalProtect agent versions
    question: Which GlobalProtect agent versions are available?
  phrasing_ops: 1
  slug: palo-alto-networks-agent-versions-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/agentless/agentless.md''}'
  name: Palo Alto Networks Agentless API
  phrasing_intents:
  - id: post-agentless-max-scanners
    intent: Set max agentless scanners for an account (v34.03)
    question: How do I cap the number of agentless scanners for a cloud account on the v34.03 API?
  - id: get-agentless-progress
    intent: View agentless scan progress (v34.03)
    question: How far along is the current agentless scan according to the v34.03 API?
  - id: post-agentless-scan
    intent: Start an agentless scan (v34.03)
    question: How do I kick off an agentless scan with the v34.03 API?
  - id: get-agentless-scan-statistics
    intent: Get agentless scan statistics (v34.03)
    question: What statistics does the v34.03 API report for agentless scans?
  - id: post-agentless-stop
    intent: Stop an ongoing agentless scan (v34.03)
    question: How do I halt a running agentless scan through the v34.03 API?
  - id: post-agentless-templates
    intent: Download agentless permission templates (v34.03)
    question: Where do I get the cloud permission templates agentless scanning needs, on v34.03?
  - id: postApiV3404AgentlessMaxScanners
    intent: Set max agentless scanners for an account (v34.04)
    question: How do I limit how many agentless scanners run for an account on the current v34.04 API?
  - id: getApiV3404AgentlessProgress
    intent: View agentless scan progress (v34.04)
    question: Is my agentless scan still running according to the v34.04 API?
  phrasing_ops: 12
  slug: palo-alto-networks-agentless-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Endpoint to retrieve the count of active users without requiring an agent.
  name: Palo Alto Networks Agentless Users API
  phrasing_intents:
  - id: post-insights-v3.0-resource-query-agentless-risky_user_count
    intent: Count risky users
    question: How many risky users do we have right now?
  - id: post-insights-v3.0-resource-query-users-agentless-active_user_count
    intent: Count active agentless users
    question: How many users are active without an agent installed?
  - id: post-insights-v3.0-resource-query-users-agentless-active_user_list
    intent: List active internal users (agentless)
    question: Who are the internal users active on the network without an agent?
  - id: post-insights-v3.0-resource-query-users-agentless-session_list
    intent: List agentless user sessions
    question: What sessions have internal users had without the agent running?
  - id: post-insights-v3.0-resource-query-users-agentless-user_count_histogram
    intent: Chart agentless users over time
    question: How has the number of agentless internal users changed over time?
  - id: post-insights-v3.0-resource-query-users-agentless-users
    intent: Get agentless user data
    question: Where can I pull general agentless user data from Prisma Access Insights?
  phrasing_ops: 6
  slug: palo-alto-networks-agentless-users-api-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Aggregate Interfaces
  name: Palo Alto Networks Aggregate Interfaces API
  phrasing_intents:
  - id: ListAggregateInterfaces
    intent: List aggregate interfaces
    question: Which aggregate Ethernet interfaces are configured in Strata Cloud Manager?
  - id: CreateAggregateInterfaces
    intent: Create an aggregate interface
    question: How do I create a new aggregate interface group?
  - id: GetAggregateInterfacesByID
    intent: Get an aggregate interface
    question: What are the settings of a specific aggregate interface?
  - id: UpdateAggregateInterfacesByID
    intent: Update an aggregate interface
    question: How do I edit an existing aggregate interface?
  - id: DeleteAggregateInterfacesByID
    intent: Delete an aggregate interface
    question: How do I delete an aggregate interface?
  phrasing_ops: 5
  slug: palo-alto-networks-aggregate-interfaces-api
- baseURL: https://api.sase.paloaltonetworks.com/aisec
  baseurl_source: declared
  description: Operations related to AI security profile management
  name: Palo Alto Networks AI Sec Profile API
  phrasing_intents:
  - id: CreateNewAIProfile
    intent: Create an AI security profile
    question: How do I create a new AI security profile with its own policy?
  - id: DeleteAIProfile
    intent: Delete an AI security profile
    question: How do I delete an AI security profile normally, with safety checks?
  - id: UpdateProfileByProfileId
    intent: Update an AI security profile
    question: How do I change the policy or name of an existing AI security profile?
  - id: GetAllAIProfilesForTsgId
    intent: List AI security profiles
    question: Which AI security profiles exist for my tenant service group?
  - id: ForceDeleteAIProfile
    intent: Force delete an AI security profile
    question: How do I force-delete an AI profile that won't delete normally?
  phrasing_ops: 5
  slug: palo-alto-networks-ai-sec-profile-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Alert rules define what policy violations trigger alerts for cloud accounts within the selected account group and where to send the alert notifications. Alert rules give you a lot of flexibility in ho
  name: Palo Alto Networks Alert Rules API
  phrasing_intents:
  - id: get-alert-rules-v2
    intent: List alert rules
    question: Which Prisma Cloud alert rules can my role see?
  - id: add-alert-rule
    intent: Create an alert rule
    question: How do I create an alert rule that scans all policies for a set of accounts?
  - id: get-alert-rule
    intent: Get an alert rule
    question: Where do I see the notification configuration of one alert rule?
  - id: update-alert-rule
    intent: Update an alert rule
    question: How do I add policies to an existing alert rule?
  - id: delete-alert-rule
    intent: Delete an alert rule
    question: Can I remove an alert rule I no longer use?
  phrasing_ops: 5
  slug: palo-alto-networks-alert-rules-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Set the enterprise level settings to build standard training models for anomaly detection, alert disposition, and some other global settings such as the timeout before the user is locked out for inact
  name: Palo Alto Networks Anomalies API
  phrasing_intents:
  - id: getAllWhitelistEntries
    intent: List anomaly trusted list entries
    question: Which IPs or resources are on my anomaly trusted list?
  - id: addToTrustedList
    intent: Add entries to the anomaly trusted list
    question: How do I stop anomaly policies alerting on a known IP?
  - id: getWhitelistEntryById
    intent: Get an anomaly trusted list entry
    question: What does a particular anomaly trusted list entry contain?
  - id: updateWhitelist
    intent: Update an anomaly trusted list entry
    question: How do I change the entries in an existing anomaly trusted list?
  - id: deleteFromTrustedList
    intent: Delete an anomaly trusted list entry
    question: How do I remove something from the anomaly trusted list?
  - id: getAnomaliesSettings
    intent: Get anomaly settings for a policy
    question: What alert disposition and training threshold does one anomaly policy use?
  - id: updateSettings
    intent: Update anomaly settings for a policy
    question: How do I make an anomaly policy less noisy?
  - id: getAllowedTrustedListTypes
    intent: List trusted list types
    question: What kinds of anomaly trusted lists can I create?
  phrasing_ops: 10
  slug: palo-alto-networks-anomalies-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: Anti-Spyware Profiles
  name: Palo Alto Networks Anti-Spyware Profiles API
  phrasing_intents:
  - id: ListAntiSpywareProfiles
    intent: List anti-spyware profiles
    question: Which anti-spyware profiles are configured in my Strata Cloud Manager tenant?
  - id: CreateAntiSpywareProfiles
    intent: Create a anti-spyware profile
    question: How do I create a new anti-spyware profile?
  - id: GetAntiSpywareProfilesByID
    intent: Get a anti-spyware profile
    question: What settings does a specific anti-spyware profile contain?
  - id: UpdateAntiSpywareProfilesByID
    intent: Update a anti-spyware profile
    question: How do I change the rules or threat exceptions in an existing anti-spyware profile?
  - id: DeleteAntiSpywareProfilesByID
    intent: Delete a anti-spyware profile
    question: Which call removes a anti-spyware profile I no longer use?
  - id: get-sse-config-v1-anti-spyware-profiles
    intent: List anti-spyware profiles in a folder
    question: Which anti-spyware profiles are configured in my Prisma Access folder?
  - id: post-sse-config-v1-anti-spyware-profiles
    intent: Create an anti-spyware profile
    question: How do I add an anti-spyware profile to a folder through the SSE config v1 API?
  - id: delete-sse-config-v1-anti-spyware-profiles-id
    intent: Delete an anti-spyware profile
    question: How do I remove an anti-spyware profile?
  phrasing_ops: 10
  slug: palo-alto-networks-anti-spyware-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: Anti-Spyware Signatures
  name: Palo Alto Networks Anti-Spyware Signatures API
  phrasing_intents:
  - id: ListAntiSpywareSignatures
    intent: List custom anti-spyware signatures
    question: Which custom anti-spyware signatures are defined in a folder?
  - id: CreateAntiSpywareSignatures
    intent: Create a custom anti-spyware signature
    question: How do I add my own spyware threat signature with a threat ID?
  - id: GetAntiSpywareSignaturesByID
    intent: Get an anti-spyware signature
    question: What severity and default action does one anti-spyware signature have?
  - id: UpdateAntiSpywareSignaturesByID
    intent: Update an anti-spyware signature
    question: Can I change the default action on an existing spyware signature?
  - id: DeleteAntiSpywareSignaturesByID
    intent: Delete an anti-spyware signature
    question: How do I remove a custom anti-spyware signature?
  - id: get-sse-config-v1-anti-spyware-signatures
    intent: List custom anti-spyware signatures
    question: Which custom anti-spyware signatures are in a Prisma Access folder?
  - id: post-sse-config-v1-anti-spyware-signatures
    intent: Create a custom anti-spyware signature
    question: How do I add my own anti-spyware signature for a new threat?
  - id: delete-sse-config-v1-anti-spyware-signatures-id
    intent: Delete a custom anti-spyware signature
    question: How do I delete a spyware signature through the SSE config v1 API?
  phrasing_ops: 9
  slug: palo-alto-networks-anti-spyware-signatures-api
- baseURL: https://api.sase.paloaltonetworks.com/aisec
  baseurl_source: declared
  description: Operations related to API key management
  name: Palo Alto Networks API key API
  phrasing_intents:
  - id: CreateNewAPIKey
    intent: Create an API key for an AI app
    question: How do I issue a new API key tied to a deployment profile's auth code?
  - id: GetAllAPIKeysForTsgId
    intent: List API keys for my tenant
    question: Which API keys exist for my tenant service group and when do they rotate?
  - id: DeleteAPIKey
    intent: Delete an API key and its app
    question: Can I permanently delete an API key along with the customer app attached to it?
  - id: RegenerateAPIKeyById
    intent: Regenerate an API key
    question: How do I rotate an API key and get a fresh secret?
  phrasing_ops: 4
  slug: palo-alto-networks-api-key-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Application API
  name: Palo Alto Networks Application API
  phrasing_intents:
  - id: post-insights-v3.0-resource-query-accelerated_applications-accelerated_application_list
    intent: List accelerated applications
    question: Which of my Prisma Access applications are being accelerated right now?
  - id: post-insights-v3.0-resource-query-accelerated_applications-accelerated_applications-throughput_before_after_boost_histogram
    intent: Chart throughput before and after acceleration boost
    question: How much did acceleration boost throughput compared to before it was applied?
  - id: post-insights-v3.0-resource-query-accelerated_applications-applications_count
    intent: Count accelerated applications
    question: What's the total number of apps that have acceleration turned on?
  - id: post-insights-v3.0-resource-query-accelerated_applications-better_response_time
    intent: Get response time data for accelerated apps
    question: Are accelerated applications actually responding faster?
  - id: post-insights-v3.0-resource-query-accelerated_applications-data_transfer_throughput_per_app
    intent: Get transfer and throughput per accelerated app
    question: Which accelerated application moves the most data and at what throughput?
  - id: post-insights-v3.0-resource-query-accelerated_applications-packet_loss_per_app_histogram
    intent: Chart packet loss per accelerated application
    question: Which accelerated apps are dropping packets, and when?
  - id: post-insights-v3.0-resource-query-accelerated_applications-performance_boost
    intent: Get acceleration performance boost metrics
    question: What performance boost is acceleration delivering for my applications?
  - id: post-insights-v3.0-resource-query-accelerated_applications-rtt_variance_histogram
    intent: Chart RTT variance for accelerated apps
    question: How much does round-trip time vary for accelerated applications?
  phrasing_ops: 36
  slug: palo-alto-networks-application-api-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/application-control/application-control.md''}'
  name: Palo Alto Networks Application Control API
  phrasing_intents:
  - id: get-application-control-host
    intent: List host app control rules (v34.03)
    question: What host application control rules exist in the v34.03 API?
  - id: put-application-control-host
    intent: Update host app control rules (v34.03)
    question: How do I update host application control rules on a 34.03 console?
  - id: delete-application-control-host-id
    intent: Delete a host app control rule (v34.03)
    question: How do I delete a host application control rule using API v34.03?
  - id: getApiV3404ApplicationControlHost
    intent: List host app control rules (v34.04)
    question: Which host application control rules are defined in the v34.04 API?
  - id: putApiV3404ApplicationControlHost
    intent: Update host app control rules (v34.04)
    question: Can I disable a host app control rule through the newer v34.04 endpoint?
  - id: deleteApiV3404ApplicationControlHostById
    intent: Delete a host app control rule (v34.04)
    question: Which endpoint deletes a host app control rule on the newer 34.04 release?
  phrasing_ops: 6
  slug: palo-alto-networks-application-control-api
- baseURL: https://api.strata.paloaltonetworks.com/config/deployment/v1
  baseurl_source: declared
  description: Prisma Access tenant initialization
  name: Palo Alto Networks Application Defaults API
  phrasing_intents:
  - id: CreateApplicationDefaults
    intent: Create Prisma Access application defaults
    question: I don't use the UI; how do I create the Prisma Access application defaults like certificates?
  phrasing_ops: 1
  slug: palo-alto-networks-application-defaults-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: Application Filters
  name: Palo Alto Networks Application Filters API
  phrasing_intents:
  - id: ListApplicationFilters
    intent: List application filters
    question: What application filters are defined in Strata Cloud Manager?
  - id: CreateApplicationFilters
    intent: Create an application filter
    question: How do I build a filter that matches all apps known to be used by malware?
  - id: GetApplicationFiltersByID
    intent: Get an application filter
    question: Where can I see the criteria of one application filter?
  - id: UpdateApplicationFiltersByID
    intent: Update an application filter
    question: How do I add a subcategory to an existing application filter?
  - id: DeleteApplicationFiltersByID
    intent: Delete an application filter
    question: Can I remove an application filter from Strata Cloud Manager?
  - id: get-sse-config-v1-application-filters
    intent: List application filters in a folder
    question: What application filters are configured in my Prisma Access folder?
  - id: post-sse-config-v1-application-filters
    intent: Create an application filter
    question: How do I create a filter that matches risky or evasive applications?
  - id: delete-sse-config-v1-application-filters-id
    intent: Delete an application filter
    question: How do I remove an application filter?
  phrasing_ops: 10
  slug: palo-alto-networks-application-filters-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: The Application Groups API from Palo Alto Networks — 4 operation(s) for application groups.
  name: Palo Alto Networks Application Groups API
  phrasing_intents:
  - id: GetSeb-apiV1Application-groups
    intent: List Enterprise Browser application groups
    question: Which application groups are defined for the Enterprise Browser?
  - id: PostSeb-apiV1Application-groups
    intent: Create an Enterprise Browser application group
    question: How do I group several browser applications under one name?
  - id: GetSeb-apiV1Application-groupsbyid
    intent: Get an Enterprise Browser application group
    question: Which apps are members of a specific browser application group?
  - id: PatchSeb-apiV1Application-groupsbyid
    intent: Partially update a browser application group
    question: Can I change just the description of a browser application group and leave the rest?
  - id: DeleteSeb-apiV1Application-groupsbyid
    intent: Delete an Enterprise Browser application group
    question: How do I permanently remove a browser application group?
  - id: ListApplicationGroups
    intent: List firewall application groups
    question: What application groups are defined in a folder, snippet or device configuration?
  - id: CreateApplicationGroups
    intent: Create a firewall application group
    question: How do I bundle App-IDs into an application group for security rules?
  - id: GetApplicationGroupsByID
    intent: Get a firewall application group
    question: Which applications are in a given policy application group?
  phrasing_ops: 15
  slug: palo-alto-networks-application-groups-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Application Monitor
  name: Palo Alto Networks Application Monitor Resource API
  phrasing_intents:
  - id: get-mt-monitor-v1-agg-custom-appmonitor-applications
    intent: Get monitored applications with experience trend
    question: How has the user experience for each monitored application trended over time?
  - id: get-mt-monitor-v1-agg-custom-appmonitor-nodetrend
    intent: Get one application's experience score trend
    question: What does the historical experience score look like for one specific app?
  - id: get-mt-monitor-v1-agg-custom-appmonitor-tenants
    intent: Get child tenant experience and usage scores
    question: Which child tenants have the worst Remote Network or Mobile User experience scores?
  phrasing_ops: 3
  slug: palo-alto-networks-application-monitor-resource-api-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: Application Override Rules
  name: Palo Alto Networks Application Override Rules API
  phrasing_intents:
  - id: ListApplicationOverrideRules
    intent: List application override rules
    question: Which application override rules exist in a given folder?
  - id: CreateApplicationOverrideRules
    intent: Create an application override rule
    question: How do I force traffic on a certain port to be identified as a specific application?
  - id: GetApplicationOverrideRulesByID
    intent: Get an application override rule
    question: What ports and application does a specific override rule use?
  - id: UpdateApplicationOverrideRulesByID
    intent: Update an application override rule
    question: Can I change the port on an existing application override rule?
  - id: DeleteApplicationOverrideRulesByID
    intent: Delete an application override rule
    question: How do I remove an application override rule?
  - id: MoveApplicationOverrideRulesByID
    intent: Reorder an application override rule
    question: Can I move an app override rule above or below another rule?
  - id: get-sse-config-v1-app-override-rules
    intent: List application override rules
    question: Which application override rules are in a folder's pre or post rulebase?
  - id: post-sse-config-v1-app-override-rules
    intent: Create an application override rule
    question: How do I force traffic on a specific port and protocol to be identified as a custom application?
  phrasing_ops: 12
  slug: palo-alto-networks-application-override-rules-api
- baseURL: https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
  baseurl_source: declared
  description: Application Settings
  name: Palo Alto Networks Application Settings API
  phrasing_intents:
  - id: ListGlobalProtectAgentProfiles
    intent: List GlobalProtect agent profiles
    question: Which GlobalProtect agent profiles are set up for Prisma Access?
  - id: CreateGlobalProtectAgentProfiles
    intent: Create a GlobalProtect agent profile
    question: How do I create a new GlobalProtect app configuration for a group of users?
  - id: UpdateGlobalProtectAgentProfiles
    intent: Update a GlobalProtect agent profile
    question: How do I change the gateways an existing GlobalProtect agent profile connects to?
  - id: DeleteGlobalProtectAgentProfiles
    intent: Delete a GlobalProtect agent profile
    question: How do I remove a GlobalProtect agent profile by name?
  phrasing_ops: 4
  slug: palo-alto-networks-application-settings-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: 'When you delete an asset in a cloud account that is onboarded on Prisma Cloud, the asset is marked as deleted. After 90 days, the configuration details of the deleted assets are archived. You can use '
  name: Palo Alto Networks Archived Assets API
  phrasing_intents:
  - id: bulkExportResourceArchives
    intent: Export archives of deleted asset configurations
    question: How do I get the configuration of cloud assets that were deleted in a date range?
  phrasing_ops: 1
  slug: palo-alto-networks-archived-assets-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Asset Explorer APIs enable you to list resource information filters, autocomplete suggestions for resource information filter, and list resource scan information.
  name: Palo Alto Networks Asset Explorer API
  phrasing_intents:
  - id: get-resource-info-filters-and-options
    intent: List resource scan info filters
    question: What filters can I use when exploring resource scan results in the asset explorer?
  - id: get-resource-info-filter-options
    intent: Autocomplete values for a resource info filter
    question: What values are available for one resource info filter in the asset explorer?
  - id: get-resource-scan-info
    intent: Get v1 resource scan pass/fail results
    question: Which of my cloud resources failed policy scans in a given time window, using the original scan info endpoint?
  - id: post-resource-scan-info
    intent: Query v1 resource scan info by POST
    question: Is there a POST version of the older resource scan info call that takes filters and a time range in the body?
  - id: get-resource-scan-info-v2
    intent: Get V2 resource scan pass/fail results
    question: Which resources are currently failing policy checks according to the V2 scan info endpoint?
  - id: post-resource-scan-info-v2
    intent: Query V2 resource scan info by POST
    question: Can I send body filters and choose fields for the V2 resource scan info query?
  - id: asset_2
    intent: Get details for one unified asset
    question: How do I see the raw cloud provider JSON for a single asset by its RRN?
  phrasing_ops: 7
  slug: palo-alto-networks-asset-explorer-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Asset Inventory APIs provide up-to-date information of all cloud assets that you are monitoring through Prisma Cloud. You can request inventory data, list available filters to narrow inventory req
  name: Palo Alto Networks Asset Inventory API
  phrasing_intents:
  - id: get-asset-inventory-v2-filters-and-options
    intent: List asset inventory filters
    question: Which filters can I apply to the Prisma Cloud asset inventory?
  - id: get-asset-inventory-v2-dashboard-filter-options
    intent: Suggest values for an inventory filter
    question: Can I get autocomplete suggestions for an asset inventory filter?
  - id: get-all-saved-asset-inventory-filters
    intent: List saved asset inventory filters
    question: What asset inventory filters have we saved?
  - id: save-asset-inventory-filter
    intent: Save an asset inventory filter
    question: How do I save an asset inventory filter so I can reuse it later?
  - id: get-saved-asset-inventory-filter
    intent: Get a saved asset inventory filter
    question: What criteria does one of my saved inventory filters contain?
  - id: update-saved-asset-inventory-filter
    intent: Update a saved asset inventory filter
    question: How do I change the criteria of an inventory filter I already saved?
  - id: delete-saved-asset-inventory-filter
    intent: Delete a saved asset inventory filter
    question: How do I delete a saved asset inventory filter?
  - id: asset-inventory-v2
    intent: Get asset pass/fail inventory for a period (v2)
    question: How many assets passed or failed scans over the last 30 days, using the legacy v2 view?
  phrasing_ops: 15
  slug: palo-alto-networks-asset-inventory-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Asset Relationship Type Management APIs enable you to list information about Prisma cloud asset relationship type definitions and asset relationship definitions
  name: Palo Alto Networks Asset Relationship Definitions API
  phrasing_intents:
  - id: get-asset-relationship-type-definitions
    intent: List asset relationship types
    question: What kinds of relationship types between assets does Prisma Cloud support?
  - id: get-asset-relationship-definitions
    intent: List supported asset relationships
    question: Which assets can be related to which, across cloud types?
  phrasing_ops: 2
  slug: palo-alto-networks-asset-relationship-definitions-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The AssociateRulestacks API from Palo Alto Networks — 2 operation(s) for associaterulestacks.
  name: Palo Alto Networks Associate Rulestacks API
  phrasing_intents:
  - id: put-v1-config-ngfirewalls-ngfirewallname-globalrulestack
    intent: Attach a global rulestack to a Cloud NGFW
    question: How do I apply a global (Firewall Manager) rulestack to my Cloud NGFW?
  - id: put-v1-config-ngfirewalls-ngfirewallname-rulestack
    intent: Attach a local rulestack to a Cloud NGFW
    question: How do I apply a local rulestack to one of my Cloud NGFW firewalls?
  phrasing_ops: 2
  slug: palo-alto-networks-associaterulestacks-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: As part of compliance requirement for organizations, companies need to demonstrate they are pro-actively tracking security issues and taking steps to remediate issues as they occur. Prisma Cloud Audit
  name: Palo Alto Networks Audit Logs API
  phrasing_intents:
  - id: getAuditLogs
    intent: Search audit logs by time range and filters
    question: How do I pull audit logs for a specific time window with filters?
  - id: getResourceTypes
    intent: Suggest audit log filter values
    question: What resource types or users can I filter audit logs by?
  - id: rl-audit-logs
    intent: Get Prisma Cloud platform audit logs
    question: Who did what on the Prisma Cloud platform in the last few hours?
  phrasing_ops: 3
  slug: palo-alto-networks-audit-logs-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/audits/audits.md''}'
  name: Palo Alto Networks Audits API
  phrasing_intents:
  - id: get-audits-access
    intent: List Docker access audit events (v34.03)
    question: Which Docker commands were allowed or blocked on my hosts, according to the v34.03 audits API?
  - id: get-audits-access-download
    intent: Download Docker access audit events (v34.03)
    question: Can I export Docker access audit events to a file using the v34.03 API?
  - id: get-audits-admission
    intent: List Kubernetes admission audit events (v34.03)
    question: Which admission control decisions were audited in a namespace under v34.03?
  - id: get-audits-admission-download
    intent: Download admission audit events (v34.03)
    question: Can I download admission controller audits as a file from the v34.03 API?
  - id: get-audits-firewall-app-agentless
    intent: List WAAS agentless audit events (v34.03)
    question: What web attacks did WAAS agentless protection record under the v34.03 API?
  - id: get-audits-firewall-app-agentless-download
    intent: Download WAAS agentless audit events (v34.03)
    question: Can I export WAAS agentless firewall audits to a file in v34.03?
  - id: get-audits-firewall-app-agentless-timeslice
    intent: Chart WAAS agentless audits over time (v34.03)
    question: How are WAAS agentless audit events spread across a timeframe in v34.03?
  - id: get-audits-firewall-app-app-embedded
    intent: List WAAS app-embedded audit events (v34.03)
    question: What attacks did app-embedded WAAS defenders block, per the v34.03 audits API?
  phrasing_ops: 96
  slug: palo-alto-networks-audits-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/authenticate/authenticate.md''}'
  name: Palo Alto Networks Authenticate API
  phrasing_intents:
  - id: post-authenticate
    intent: Get an access token (v34.03)
    question: How do I get an access token for the Compute API using the v34.03 authenticate path?
  - id: postApiV3404Authenticate
    intent: Get an access token (v34.04)
    question: Which call issues a user access token on the current v34.04 API?
  phrasing_ops: 2
  slug: palo-alto-networks-authenticate-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/authenticate-client/authenticate-client.md''}'
  name: Palo Alto Networks Authenticate Client API
  phrasing_intents:
  - id: post-authenticate-client
    intent: Get a client access token (v34.03)
    question: How do I get a client authentication token from the older v34.03 API?
  - id: postApiV3404AuthenticateClient
    intent: Get a client access token (v34.04)
    question: How do I get a client authentication access token on the current v34.04 API?
  phrasing_ops: 2
  slug: palo-alto-networks-authenticate-client-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: Authentication Portals
  name: Palo Alto Networks Authentication Portals API
  phrasing_intents:
  - id: ListAuthenticationPortals
    intent: List authentication portals
    question: Which authentication portals are configured in my Strata Cloud Manager folders?
  - id: CreateAuthenticationPortals
    intent: Create an authentication portal
    question: How do I set up a new authentication portal with a redirect host and TLS profile?
  - id: GetAuthenticationPortalsByID
    intent: Get an authentication portal
    question: What settings does a particular authentication portal have?
  - id: UpdateAuthenticationPortalsByID
    intent: Update an authentication portal
    question: How do I change the certificate profile on an existing authentication portal?
  - id: DeleteAuthenticationPortalsByID
    intent: Delete an authentication portal
    question: How do I remove an authentication portal?
  - id: get-sse-config-v1-authentication-portals
    intent: List authentication portals
    question: Which authentication portals are configured in a folder?
  - id: post-sse-config-v1-authentication-portals
    intent: Create an authentication portal
    question: How do I set up a new authentication portal for users?
  - id: delete-sse-config-v1-authentication-portals-id
    intent: Delete an authentication portal
    question: How do I remove an authentication portal through the SSE config v1 API?
  phrasing_ops: 9
  slug: palo-alto-networks-authentication-portals-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: Authentication Profiles
  name: Palo Alto Networks Authentication Profiles API
  phrasing_intents:
  - id: ListAuthenticationProfiles
    intent: List authentication profiles
    question: Which authentication profiles are configured in a folder?
  - id: CreateAuthenticationProfiles
    intent: Create an authentication profile
    question: How do I create an authentication profile with multi-factor authentication?
  - id: GetAuthenticationProfilesByID
    intent: Get an authentication profile
    question: What method and lockout settings does one authentication profile use?
  - id: UpdateAuthenticationProfilesByID
    intent: Update an authentication profile
    question: How do I change the allow list on an existing authentication profile?
  - id: DeleteAuthenticationProfilesByID
    intent: Delete an authentication profile
    question: How do I remove an authentication profile?
  - id: get-sse-config-v1-authentication-profiles
    intent: List authentication profiles
    question: Which authentication profiles exist in a Prisma Access folder?
  - id: post-sse-config-v1-authentication-profiles
    intent: Create an authentication profile
    question: How do I create an authentication profile with MFA and lockout settings?
  - id: delete-sse-config-v1-authentication-profiles-id
    intent: Delete an authentication profile
    question: How do I delete an authentication profile I no longer use?
  phrasing_ops: 10
  slug: palo-alto-networks-authentication-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: Authentication Rules
  name: Palo Alto Networks Authentication Rules API
  phrasing_intents:
  - id: ListAuthenticationRules
    intent: List authentication rules
    question: Which authentication rules are in my pre or post rulebase?
  - id: CreateAuthenticationRules
    intent: Create an authentication rule
    question: How do I require users to authenticate before reaching a service?
  - id: GetAuthenticationRulesByID
    intent: Get an authentication rule
    question: What sources, destinations and enforcement does a specific authentication rule use?
  - id: UpdateAuthenticationRulesByID
    intent: Update an authentication rule
    question: How do I change the destinations covered by an existing authentication rule?
  - id: DeleteAuthenticationRulesByID
    intent: Delete an authentication rule
    question: How do I remove an authentication rule I no longer need?
  - id: MoveAuthenticationRulesByID
    intent: Reorder an authentication rule
    question: How do I move an authentication rule to the top of the rulebase?
  - id: get-sse-config-v1-authentication-rules
    intent: List authentication rules
    question: Which authentication policy rules are set in a folder?
  - id: post-sse-config-v1-authentication-rules
    intent: Create an authentication rule
    question: Can I require users to authenticate before reaching certain destinations?
  phrasing_ops: 11
  slug: palo-alto-networks-authentication-rules-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: Authentication Sequences
  name: Palo Alto Networks Authentication Sequences API
  phrasing_intents:
  - id: ListAuthenticationSequences
    intent: List authentication sequences
    question: Which authentication sequences are configured in my Strata Cloud Manager folders?
  - id: CreateAuthenticationSequences
    intent: Create an authentication sequence
    question: How do I chain several authentication profiles into one sequence?
  - id: GetAuthenticationSequencesByID
    intent: Get an authentication sequence
    question: What profiles are in a specific authentication sequence, and in what order?
  - id: UpdateAuthenticationSequencesByID
    intent: Update an authentication sequence
    question: Can I change the profile order in an existing authentication sequence?
  - id: DeleteAuthenticationSequencesByID
    intent: Delete an authentication sequence
    question: Can I remove an authentication sequence that's no longer referenced?
  - id: get-sse-config-v1-authentication-sequences
    intent: List authentication sequences in a folder
    question: Which authentication sequences are defined in my Prisma Access folder?
  - id: post-sse-config-v1-authentication-sequences
    intent: Create an authentication sequence
    question: How do I set up a new authentication sequence that tries several authentication profiles in order?
  - id: delete-sse-config-v1-authentication-sequences-id
    intent: Delete an authentication sequence
    question: How do I remove an authentication sequence I no longer need?
  phrasing_ops: 10
  slug: palo-alto-networks-authentication-sequences-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: Authentication Settings
  name: Palo Alto Networks Authentication Settings API
  phrasing_intents:
  - id: ListAuthenticationSettings
    intent: List GlobalProtect authentication settings
    question: Which GlobalProtect agent authentication settings are configured?
  - id: CreateAuthenticationSettings
    intent: Create a GlobalProtect authentication setting
    question: How do I add a new GlobalProtect authentication setting with its own ID?
  - id: GetAuthenticationSettingsByID
    intent: Get device authentication settings
    question: What authentication is configured in a specific device authentication settings object?
  - id: UpdateAuthenticationSettingsByID
    intent: Update device authentication settings
    question: Can I change the authentication used by an existing device settings object?
  - id: DeleteAuthenticationSettingsByID
    intent: Delete device authentication settings
    question: Can I delete a device authentication settings object?
  phrasing_ops: 5
  slug: palo-alto-networks-authentication-settings-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Authorization API from Palo Alto Networks — 1 operation(s) for authorization.
  name: Palo Alto Networks Authorization API
  phrasing_intents:
  - id: getAuthInfo
    intent: Get SaaS app authorization information
    question: What authorization does a SaaS application type require in the SSPM catalog?
  phrasing_ops: 1
  slug: palo-alto-networks-authorization-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: Auto-Tag Actions
  name: Palo Alto Networks Auto-Tag Actions API
  phrasing_intents:
  - id: ListAuto-TagActions
    intent: List auto-tag actions
    question: Which auto-tag actions are configured to tag hosts based on log events?
  - id: CreateAuto-TagActions
    intent: Create an auto-tag action
    question: How do I automatically tag an IP when a matching log entry appears?
  - id: UpdateAuto-TagActions
    intent: Update an auto-tag action
    question: Can I change the log filter on an existing auto-tag action?
  - id: DeleteAuto-TagActions
    intent: Delete an auto-tag action
    question: How do I stop an auto-tag action from tagging anything by removing it?
  - id: delete-sse-config-v1-auto-tag-actions
    intent: Delete an auto tag action
    question: How do I stop an auto tag action from tagging anything?
  - id: get-sse-config-v1-auto-tag-actions
    intent: List auto tag actions
    question: Which auto tag actions are configured to tag sources from log matches?
  - id: post-sse-config-v1-auto-tag-actions
    intent: Create an auto tag action
    question: How do I automatically tag an IP when a log entry matches a filter?
  - id: put-sse-config-v1-auto-tag-actions
    intent: Edit an auto tag action
    question: Via the SSE config v1 path, can I change the log filter of an auto tag action?
  phrasing_ops: 8
  slug: palo-alto-networks-auto-tag-actions-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Auto VPN Clusters
  name: Palo Alto Networks Auto VPN Clusters API
  phrasing_intents:
  - id: ListAutoVPNClusters
    intent: List Auto VPN clusters
    question: Which Auto VPN clusters are configured?
  - id: CreateAutoVPNClusters
    intent: Create an Auto VPN cluster
    question: How do I set up a new Auto VPN cluster linking branches to hubs?
  - id: GetAutoVPNClustersByID
    intent: Get an Auto VPN cluster
    question: What branches and hubs belong to a specific Auto VPN cluster?
  - id: UpdateAutoVPNClustersByID
    intent: Update an Auto VPN cluster
    question: How do I add branches to an existing Auto VPN cluster?
  - id: DeleteAutoVPNClustersByID
    intent: Delete an Auto VPN cluster
    question: How do I tear down an Auto VPN cluster?
  phrasing_ops: 5
  slug: palo-alto-networks-auto-vpn-clusters-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Auto VPN Config Push
  name: Palo Alto Networks Auto VPN Config Push API
  phrasing_intents:
  - id: CreateAutoVPNPushConfigs
    intent: Push Auto VPN configuration to devices
    question: How do I push Auto VPN configuration out to my firewalls?
  phrasing_ops: 1
  slug: palo-alto-networks-auto-vpn-config-push-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Auto VPN Monitor
  name: Palo Alto Networks Auto VPN Monitor API
  phrasing_intents:
  - id: GetAutoVPNMonitor
    intent: Check Auto VPN cluster status
    question: Are my Auto VPN clusters up?
  phrasing_ops: 1
  slug: palo-alto-networks-auto-vpn-monitor-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Auto VPN Settings
  name: Palo Alto Networks Auto VPN Settings API
  phrasing_intents:
  - id: GetAutoVPNSettings
    intent: Get Auto VPN settings
    question: What VPN address pool and AS range does Auto VPN use?
  - id: UpdateAutoVPNSettings
    intent: Update Auto VPN settings
    question: Can I change the VPN address pool used by Auto VPN?
  phrasing_ops: 2
  slug: palo-alto-networks-auto-vpn-settings-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: Autoscale Settings
  name: Palo Alto Networks Autoscale Settings API
  phrasing_intents:
  - id: GetAutoscaleSettings
    intent: Get device autoscale settings
    question: What virtualization autoscale settings are configured for a folder or device?
  - id: CreateAutoscaleSettings
    intent: Create device autoscale settings
    question: How do I set up autoscale settings for the first time?
  - id: UpdateAutoscaleSettings
    intent: Update device autoscale settings
    question: How do I change the existing autoscale metrics settings for AWS CloudWatch?
  - id: DeleteAutoscaleSettings
    intent: Delete device autoscale settings
    question: Can I remove the autoscale settings from a folder?
  phrasing_ops: 4
  slug: palo-alto-networks-autoscale-settings-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: To ingest the VPC flow logs from Amazon S3 buckets to Prisma Cloud, you need an AWS logging account. If you need flow logs ingestion, after onboarding your AWS account, you must onboard the logging ac
  name: Palo Alto Networks AWS Logging Accounts API
  phrasing_intents:
  - id: getLoggingArchiveAccounts
    intent: List all AWS logging accounts
    question: Which AWS logging accounts are onboarded to Prisma Cloud?
  - id: saveLoggingAccount
    intent: Add a new AWS logging account
    question: How do I onboard a new AWS logging account with its role and S3 buckets?
  - id: generate-log-account-cft
    intent: Generate a CloudFormation template for a new logging account
    question: Can Prisma Cloud generate the CloudFormation template I need before onboarding a logging account?
  - id: checkLoggingAccountStatus
    intent: Check permissions status for logging account details
    question: Before saving, can I check whether a logging account's role and buckets have the right permissions?
  - id: getLoggingArchiveAccount
    intent: Get one AWS logging account
    question: How do I see the details of a single AWS logging account?
  - id: deleteBucket
    intent: Remove an S3 bucket from a logging account
    question: Can I detach one S3 bucket from a logging account without deleting the account?
  - id: generate-log-account-cft-existing
    intent: Regenerate the CFT for an existing logging account
    question: Can I download a fresh CloudFormation template for a logging account that's already onboarded?
  - id: generate-log-account-cft-role
    intent: Regenerate a logging account CFT after a role name change
    question: I renamed the IAM role on my logging account; how do I get an updated CFT?
  phrasing_ops: 17
  slug: palo-alto-networks-aws-logging-accounts-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Background jobs is an asynchronous way of managing the report. When you want to download the results up to 100k records, you can create a background job and use the available apis to check the job sta
  name: Palo Alto Networks Background Jobs API
  phrasing_intents:
  - id: list-reports
    intent: List background report jobs
    question: Which background report jobs have I created in the last 30 days?
  - id: get-report-metadata-by-id
    intent: Get a background report's metadata
    question: What are the details of a particular background report job?
  - id: get-report-status-by-id
    intent: Check a background report's status
    question: Is my background report finished yet?
  - id: download-report-by-id
    intent: Download a finished report
    question: How do I download the results of a finished background report?
  phrasing_ops: 4
  slug: palo-alto-networks-background-jobs-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Bandwidth Allocations API from Palo Alto Networks — 4 operation(s) for bandwidth allocations.
  name: Palo Alto Networks Bandwidth Allocations API
  phrasing_intents:
  - id: delete-v1-bandwidth-allocations
    intent: Delete an aggregated bandwidth region (v1)
    question: Can I remove a bandwidth region through the v1 endpoint?
  - id: get-v1-bandwidth-allocations
    intent: Check status of a v1 bandwidth allocation request
    question: How do I check whether my v1 aggregated bandwidth allocation request finished?
  - id: post-v1-bandwidth-allocations
    intent: Allocate aggregated bandwidth to regions (v1)
    question: How do I allocate aggregated bandwidth across Prisma Access regions with the v1 API?
  - id: put-v1-bandwidth-allocations
    intent: Edit aggregated bandwidth regions (v1)
    question: Can I change existing aggregated bandwidth allocations with the v1 endpoint?
  - id: get-v1-bandwidth-allocations-read
    intent: Get bandwidth allocation configurations for a read request
    question: Where do I fetch the results of a bandwidth allocation read request?
  - id: post-v1-bandwidth-allocations-read
    intent: Request bandwidth allocation config for regions
    question: How do I ask for the bandwidth allocation configuration of specific regions?
  - id: delete-v2-bandwidth-allocations
    intent: Delete an aggregated bandwidth region (v2)
    question: How do I delete an aggregated bandwidth region with the v2 API?
  - id: get-v2-bandwidth-allocations
    intent: Get aggregated bandwidth regions (v2)
    question: Which aggregated bandwidth regions does the v2 API return for my request?
  phrasing_ops: 18
  slug: palo-alto-networks-bandwidth-allocations-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Bandwidth Consumption API from Palo Alto Networks — 1 operation(s) for bandwidth consumption.
  name: Palo Alto Networks Bandwidth Consumption API
  phrasing_intents:
  - id: PostMtMonitor5gUeipBandwidth
    intent: Get 5G user bandwidth consumption
    question: How much ingress and egress bandwidth are my 5G users consuming?
  phrasing_ops: 1
  slug: palo-alto-networks-bandwidth-consumption-api
- baseURL: https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1
  baseurl_source: declared
  description: Monitoring and reporting for benchmarked compliance frameworks with BPC verdict tracking.
  name: Palo Alto Networks Benchmark Monitoring API
  phrasing_intents:
  - id: getBenchmarkMonitoring
    intent: Query benchmark monitoring data
    question: Which best-practice checks are failing on my firewalls via the unversioned benchmark endpoint?
  - id: getBenchmarkMonitoringDownload
    intent: Download benchmark monitoring data
    question: How do I export benchmark monitoring data from the unversioned endpoint as CSV?
  - id: GetBenchmarkMonitoring
    intent: Query compliance framework benchmark data
    question: How do I pull benchmark compliance data from the compliance-frameworks v1 API?
  - id: DownloadBenchmarkMonitoring
    intent: Download compliance framework benchmark data
    question: Can I download compliance-frameworks v1 benchmark data as JSON instead of CSV?
  phrasing_ops: 4
  slug: palo-alto-networks-benchmark-monitoring-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: BGP Address Family Profiles
  name: Palo Alto Networks BGP Address Family Profiles API
  phrasing_intents:
  - id: ListBGPAddressFamilyProfiles
    intent: List BGP address family profiles
    question: Which BGP address family profiles are defined in a folder?
  - id: CreateBGPAddressFamilyProfiles
    intent: Create a BGP address family profile
    question: How do I set up a new BGP address family profile with IPv4 settings?
  - id: GetBGPAddressFamilyProfilesByID
    intent: Get a BGP address family profile
    question: What IPv4 settings does a particular BGP address family profile have?
  - id: UpdateBGPAddressFamilyProfilesByID
    intent: Update a BGP address family profile
    question: Can I change the IPv4 settings on an existing BGP address family profile?
  - id: DeleteBGPAddressFamilyProfilesByID
    intent: Delete a BGP address family profile
    question: How do I remove a BGP address family profile I no longer use?
  phrasing_ops: 5
  slug: palo-alto-networks-bgp-address-family-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: BGP Authentication Profiles
  name: Palo Alto Networks BGP Authentication Profiles API
  phrasing_intents:
  - id: ListBGPAuthenticationProfiles
    intent: List BGP authentication profiles
    question: Which BGP authentication profiles are configured in a folder or on a device?
  - id: CreateBGPAuthenticationProfiles
    intent: Create a BGP authentication profile
    question: How do I set up a shared secret for BGP peer authentication?
  - id: GetBGPAuthenticationProfilesByID
    intent: Get a BGP authentication profile
    question: Where can I view one BGP authentication profile by ID?
  - id: UpdateBGPAuthenticationProfilesByID
    intent: Update a BGP authentication profile
    question: How do I rotate the secret on an existing BGP authentication profile?
  - id: DeleteBGPAuthenticationProfilesByID
    intent: Delete a BGP authentication profile
    question: Can I delete a BGP authentication profile I no longer use?
  phrasing_ops: 5
  slug: palo-alto-networks-bgp-authentication-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: BGP Filtering Profiles
  name: Palo Alto Networks BGP Filtering Profiles API
  phrasing_intents:
  - id: ListBGPFilteringProfiles
    intent: List BGP filtering profiles
    question: Which BGP filtering profiles are configured in a folder?
  - id: CreateBGPFilteringProfiles
    intent: Create a BGP filtering profile
    question: How do I create a BGP filtering profile for IPv4 routes?
  - id: GetBGPFilteringProfilesByID
    intent: Get a BGP filtering profile
    question: What IPv4 filters are in a specific BGP filtering profile?
  - id: UpdateBGPFilteringProfilesByID
    intent: Update a BGP filtering profile
    question: Can I change the IPv4 filters on an existing BGP filtering profile?
  - id: DeleteBGPFilteringProfilesByID
    intent: Delete a BGP filtering profile
    question: How do I delete a BGP filtering profile I don't need?
  phrasing_ops: 5
  slug: palo-alto-networks-bgp-filtering-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: BGP Redistribution Profiles
  name: Palo Alto Networks BGP Redistribution Profiles API
  phrasing_intents:
  - id: ListBGPRedistributionProfiles
    intent: List BGP redistribution profiles
    question: Which BGP redistribution profiles are defined?
  - id: CreateBGPRedistributionProfiles
    intent: Create a BGP redistribution profile
    question: How do I redistribute static or connected routes into BGP?
  - id: GetBGPRedistributionProfilesByID
    intent: Get a BGP redistribution profile
    question: What routes does a particular BGP redistribution profile redistribute?
  - id: UpdateBGPRedistributionProfilesByID
    intent: Update a BGP redistribution profile
    question: How do I change which routes an existing BGP redistribution profile covers?
  - id: DeleteBGPRedistributionProfilesByID
    intent: Delete a BGP redistribution profile
    question: How do I remove a BGP redistribution profile?
  phrasing_ops: 5
  slug: palo-alto-networks-bgp-redistribution-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: BGP Route Map Redistributions
  name: Palo Alto Networks BGP Route Map Redistributions API
  phrasing_intents:
  - id: ListBGPRouteMapRedistributions
    intent: List BGP route map redistributions
    question: Which BGP route map redistributions are defined in a folder?
  - id: CreateBGPRouteMapRedistributions
    intent: Create a BGP route map redistribution
    question: How do I add a BGP route map redistribution?
  - id: GetBGPRouteMapRedistributionsByID
    intent: Get a BGP route map redistribution
    question: What's in a specific BGP route map redistribution?
  - id: UpdateBGPRouteMapRedistributionsByID
    intent: Update a BGP route map redistribution
    question: Can I rename a BGP route map redistribution?
  - id: DeleteBGPRouteMapRedistributionsByID
    intent: Delete a BGP route map redistribution
    question: How do I remove a BGP route map redistribution?
  phrasing_ops: 5
  slug: palo-alto-networks-bgp-route-map-redistributions-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: BGP Route Maps
  name: Palo Alto Networks BGP Route Maps API
  phrasing_intents:
  - id: ListBGPRouteMaps
    intent: List BGP route maps
    question: Which BGP route maps are configured on my firewalls?
  - id: CreateBGPRouteMaps
    intent: Create a BGP route map
    question: How do I create a BGP route map to control route redistribution?
  - id: GetBGPRouteMapsByID
    intent: Get a BGP route map
    question: What match and set rules are in a specific BGP route map?
  - id: UpdateBGPRouteMapsByID
    intent: Update a BGP route map
    question: How do I change the entries of an existing BGP route map?
  - id: DeleteBGPRouteMapsByID
    intent: Delete a BGP route map
    question: How do I delete a BGP route map?
  phrasing_ops: 5
  slug: palo-alto-networks-bgp-route-maps-api
- baseURL: https://api.strata.paloaltonetworks.com/config/deployment/v1
  baseurl_source: declared
  description: BGP routing for Service Connections
  name: Palo Alto Networks BGP Routing API
  phrasing_intents:
  - id: GetBGPRouting
    intent: Get service connection BGP routing settings
    question: What BGP routing preference are my Prisma Access service connections using?
  - id: UpdateBGPRouting
    intent: Update service connection BGP routing settings
    question: How do I change the BGP routing preference for service connections?
  phrasing_ops: 2
  slug: palo-alto-networks-bgp-routing-api
- baseURL: https://bpa.paloaltonetworks.com
  baseurl_source: declared
  description: The BPA Report API API from Palo Alto Networks — 3 operation(s) for bpa report api.
  name: Palo Alto Networks BPA Report API
  phrasing_intents:
  - id: get-bpa-v1-jobs-id
    intent: Check a BPA report job status
    question: Has my Best Practice Assessment job finished processing?
  - id: get-bpa-v1-reports-id
    intent: Get the download URL for a BPA report
    question: Where can I download a completed BPA report?
  - id: post-bpa-v1-requests
    intent: Request a Best Practice Assessment report
    question: How do I generate a Best Practice Assessment report for a firewall?
  phrasing_ops: 3
  slug: palo-alto-networks-bpa-report-api-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Branch User API API from Palo Alto Networks — 8 operation(s) for branch user api.
  name: Palo Alto Networks Branch User API
  phrasing_intents:
  - id: post-insights-v3.0-resource-export-query-users-branch-user_list
    intent: Export the branch user list
    question: Can I export all branch users with their devices and applications?
  - id: post-insights-v3.0-resource-query-branch-risky_user_count
    intent: Count risky branch users
    question: How many risky users are there at our branches?
  - id: post-insights-v3.0-resource-query-users-branch-active_user_count
    intent: Count active branch users
    question: How many users are active at branch sites right now?
  - id: post-insights-v3.0-resource-query-users-branch-active_user_list
    intent: List active branch users
    question: Who are the active users at our branch offices?
  - id: post-insights-v3.0-resource-query-users-branch-connected_entity_count
    intent: Count connected entities for branch users
    question: How many entities are connected for branch users?
  - id: post-insights-v3.0-resource-query-users-branch-session_list
    intent: List branch user sessions
    question: What sessions have branch users had recently?
  - id: post-insights-v3.0-resource-query-users-branch-user_count_histogram
    intent: Chart branch user counts over time
    question: How has the number of branch users trended over time?
  - id: post-insights-v3.0-resource-query-users-branch-user_list
    intent: List branch users with device and app details
    question: Which branch users are there, and what devices and apps do they use?
  phrasing_ops: 8
  slug: palo-alto-networks-branch-user-api-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Built-In Accounts.
  name: Palo Alto Networks Built-In Accounts API
  phrasing_intents:
  - id: get-v1-serviceaccounts
    intent: List service accounts
    question: Which service accounts do I have access to?
  - id: create-v1-serviceaccounts
    intent: Create a service account
    question: How do I create a service account for machine-to-machine authentication?
  - id: get-v1-serviceaccounts-byId
    intent: Get a service account
    question: What are the settings on one particular service account?
  - id: patch-v1-serviceaccounts-byId
    intent: Enable or disable a service account
    question: Can I disable a service account without deleting it?
  - id: delete-v1-serviceaccounts-byId
    intent: Delete a service account
    question: Does deleting a service account also invalidate its credentials?
  - id: get-v1-serviceaccountscopes
    intent: List available service account scopes
    question: What scopes can I grant to a service account?
  - id: put-v1-serviceaccounts-byId-ocitoken
    intent: Regenerate a service account's OCI registry token
    question: Can I rotate the OCI registry token for a service account?
  - id: put-v1-serviceaccounts-byId-credentials
    intent: Extend a service account's credential lifetime
    question: Can I extend how long a service account's credentials stay valid?
  phrasing_ops: 8
  slug: palo-alto-networks-built-in-accounts-api
- baseURL: https://api.sase.paloaltonetworks.com/ai-red-teaming/data-plane
  baseurl_source: declared
  description: Operations for managing scan categories.
  name: Palo Alto Networks Categories API
  phrasing_intents:
  - id: get_all_categories_v1_categories_get
    intent: List categories and subcategories
    question: What categories and subcategories are available?
  phrasing_ops: 1
  slug: palo-alto-networks-categories-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Certificate Approvals.
  name: Palo Alto Networks Certificate Approvals API
  phrasing_intents:
  - id: certificaterequests_approve
    intent: Approve or reject a certificate request
    question: How do I approve a certificate request waiting on me?
  - id: certificaterequests_bulk_approve
    intent: Approve or reject many certificate requests
    question: Can I approve a batch of pending certificate requests at once?
  - id: certificaterequests_approval_rule_create
    intent: Create a certificate approval rule
    question: How do I require approval before certain certificates are issued?
  - id: certificaterequests_approval_rules_getAll
    intent: List certificate approval rules
    question: What approval rules govern certificate requests in our company?
  - id: certificaterequests_approval_rule_getById
    intent: Get a certificate approval rule
    question: Who are the approvers on one specific certificate approval rule?
  - id: certificaterequests_approval_rule_update
    intent: Update a certificate approval rule
    question: How do I change the approvers on an existing certificate rule?
  - id: certificaterequests_approval_rule_delete
    intent: Delete a certificate approval rule
    question: How do I remove a certificate approval rule we no longer need?
  - id: certificaterequests_approvalrequest
    intent: Get the approval request for a certificate
    question: Where is a certificate request in its approval workflow?
  phrasing_ops: 8
  slug: palo-alto-networks-certificate-approvals-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Certificate Auto-renewal Monitoring.
  name: Palo Alto Networks Certificate Auto-renewal Monitoring API
  phrasing_intents:
  - id: get-v1-tenant-renewal-configuration
    intent: Get certificate auto-renewal settings
    question: What renewal window is set for certificate expiration monitoring?
  - id: put-v1-tenant-renewal-configuration
    intent: Update certificate auto-renewal settings
    question: How do I change when certificates are renewed before they expire?
  - id: post-v1-run-autorenewal
    intent: Run the certificate renewal check now
    question: Can I trigger the daily certificate renewal check immediately?
  - id: get-v1-status
    intent: Get certificate auto-renewal status
    question: Is the certificate auto-renewal monitoring process running?
  phrasing_ops: 4
  slug: palo-alto-networks-certificate-auto-renewal-monitoring-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Certificate Discovery.
  name: Palo Alto Networks Certificate Discovery API
  phrasing_intents:
  - id: integrationsservices_getAll
    intent: List certificate discovery services
    question: Which discovery and key pair services are set up for certificate management?
  - id: integrationsservices_create
    intent: Add a certificate discovery service
    question: How do I set up a new certificate discovery service?
  - id: integrationsservices_getById
    intent: Get a certificate discovery service
    question: What targets and schedule does one discovery service have?
  - id: integrationsservices_delete
    intent: Remove a certificate discovery service
    question: How do I delete a discovery service?
  - id: integrationsservices_update
    intent: Update a certificate discovery service
    question: How do I change the schedule of an existing discovery service?
  phrasing_ops: 5
  slug: palo-alto-networks-certificate-discovery-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Certificate Import.
  name: Palo Alto Networks Certificate Import API
  phrasing_intents:
  - id: certificateimports_create
    intent: Import certificates into the inventory
    question: Can I add raw base64 certificates to my certificate inventory?
  phrasing_ops: 1
  slug: palo-alto-networks-certificate-import-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Certificate Inventory Monitoring.
  name: Palo Alto Networks Certificate Inventory Monitoring API
  phrasing_intents:
  - id: inventorymonitoringconfiguration_getByType
    intent: Get a certificate inventory monitoring config
    question: How is certificate inventory monitoring currently configured for a given type?
  - id: inventorymonitoringconfiguration_update
    intent: Update a certificate inventory monitoring config
    question: How do I change the certificate inventory monitoring configuration for a type?
  - id: inventorymonitoringconfigurationscheduler_update
    intent: Update or trigger the inventory monitoring scheduler
    question: Can I kick off a certificate inventory monitoring run right now?
  - id: get-v1-tenant-expiration-notification-configuration
    intent: Get certificate expiration notification settings
    question: Who gets notified when our certificates are about to expire?
  - id: put-v1-tenant-expiration-notification-configuration
    intent: Update certificate expiration notification settings
    question: How do I add extra recipients to certificate expiration notifications?
  phrasing_ops: 5
  slug: palo-alto-networks-certificate-inventory-monitoring-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Certificate Policy.
  name: Palo Alto Networks Certificate Policy API
  phrasing_intents:
  - id: certificateissuingtemplate_getAll
    intent: List certificate issuing templates
    question: Which issuing templates control how certificates get requested?
  - id: certificateissuingtemplate_create
    intent: Create a certificate issuing template
    question: How do I set up an issuing template with allowed key types and a CA product?
  - id: certificateissuingtemplate_getById
    intent: Get an issuing template
    question: What settings does one issuing template enforce?
  - id: certificateissuingtemplate_update
    intent: Overwrite an issuing template
    question: Does updating an issuing template replace all of its settings?
  - id: certificateissuingtemplate_delete
    intent: Delete an issuing template
    question: How do I remove an issuing template nobody uses?
  - id: domainssynchronization
    intent: Sync issuing template domains from a CA
    question: Can I pull the domain list from my CA into my issuing templates?
  phrasing_ops: 6
  slug: palo-alto-networks-certificate-policy-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: Certificate Profiles
  name: Palo Alto Networks Certificate Profiles API
  phrasing_intents:
  - id: ListCertificateProfiles
    intent: List certificate profiles
    question: Which certificate profiles are configured in a given folder?
  - id: CreateCertificateProfiles
    intent: Create a certificate profile
    question: How do I create a certificate profile with trusted CA certificates?
  - id: GetCertificateProfilesByID
    intent: Get a certificate profile
    question: How do I view one certificate profile's settings by ID?
  - id: UpdateCertificateProfilesByID
    intent: Update a certificate profile
    question: How do I change the CA list or CRL settings on an existing certificate profile?
  - id: DeleteCertificateProfilesByID
    intent: Delete a certificate profile
    question: How do I delete a certificate profile?
  - id: get-sse-config-v1-certificate-profiles
    intent: List certificate profiles
    question: Which certificate profiles exist in a Prisma Access folder?
  - id: post-sse-config-v1-certificate-profiles
    intent: Create a certificate profile
    question: How do I create a certificate profile with my CA certificates?
  - id: delete-sse-config-v1-certificate-profiles-id
    intent: Delete a certificate profile
    question: Can I delete a certificate profile I no longer use?
  phrasing_ops: 10
  slug: palo-alto-networks-certificate-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Certificate Request.
  name: Palo Alto Networks Certificate Request API
  phrasing_intents:
  - id: certificaterequests_getAll
    intent: List all certificate requests
    question: What certificate requests have been made so far?
  - id: certificaterequests_create
    intent: Request a new or renewed certificate
    question: How do I request a certificate for an application using an issuing template?
  - id: certificaterequests_getById
    intent: Get a certificate request's details
    question: What's the status of a certificate request I submitted?
  - id: certificaterequests_resubmitById
    intent: Resubmit a certificate request
    question: Can I retry a certificate request that failed?
  - id: certificaterequests_validation
    intent: Check a certificate request before submitting
    question: Can I test whether a certificate request complies with the issuing template without submitting it?
  - id: getCertificateRequestsByExpression
    intent: Search certificate requests
    question: Can I search certificate requests with a filter expression and sort order?
  phrasing_ops: 6
  slug: palo-alto-networks-certificate-request-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Certificate Revocation Approvals.
  name: Palo Alto Networks Certificate Revocation Approvals API
  phrasing_intents:
  - id: certificaterevocations_approval_rule_create
    intent: Create a certificate revocation approval rule
    question: How do I require approval before a certificate can be revoked?
  - id: certificaterevocations_approval_rules_getAll
    intent: List certificate revocation approval rules
    question: Which approval rules govern certificate revocation requests in my company?
  - id: certificaterevocations_approval_rule_getById
    intent: Get a certificate revocation approval rule
    question: Who approves revocations under a particular approval rule?
  - id: certificaterevocations_approval_rule_update
    intent: Update a certificate revocation approval rule
    question: How do I change the approvers on an existing revocation approval rule?
  - id: certificaterevocations_approval_rule_delete
    intent: Delete a certificate revocation approval rule
    question: Can I remove an approval rule from the revocation workflow?
  phrasing_ops: 5
  slug: palo-alto-networks-certificate-revocation-approvals-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Certificate Tags.
  name: Palo Alto Networks Certificate Tags API
  phrasing_intents:
  - id: tags_getAll
    intent: List all tags
    question: What tags have been defined for my certificates so far?
  - id: tags_create
    intent: Create a tag
    question: How do I create a new tag, optionally with some starting values?
  - id: tags_getByName
    intent: Get a tag by name
    question: What does the tag called owner look like, looked up by its name?
  - id: tags_deleteByName
    intent: Delete a tag by name
    question: How do I remove a tag I no longer use?
  - id: tags_get_values
    intent: List the values of one tag
    question: Which values are allowed for a particular tag?
  - id: tag_values_create
    intent: Add values to an existing tag
    question: Can I add new values to a tag that already exists?
  - id: tags_deleteValueByName
    intent: Delete one value from a tag
    question: How do I remove a single value from a tag without deleting the tag?
  - id: tags_getAllValues
    intent: List values across all tags
    question: What values exist across every tag at once?
  phrasing_ops: 12
  slug: palo-alto-networks-certificate-tags-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The CertificateObjects API from Palo Alto Networks — 2 operation(s) for certificateobjects.
  name: Palo Alto Networks Certificate Objects API
  phrasing_intents:
  - id: get-v1-config-rulestacks-rulestackname-certificates
    intent: List certificate objects in a rulestack
    question: Which certificate objects are attached to a Cloud NGFW rulestack?
  - id: post-v1-config-rulestacks-rulestackname-certificates
    intent: Create a certificate object in a rulestack
    question: How do I add a server certificate object to a rulestack?
  - id: delete-v1-config-rulestacks-rulestackname-certificates-name
    intent: Delete a rulestack certificate object
    question: Which call removes a certificate object from a rulestack?
  - id: get-v1-config-rulestacks-rulestackname-certificates-name
    intent: Get certificate object metadata
    question: What metadata does a specific certificate object in my rulestack have?
  - id: put-v1-config-rulestacks-rulestackname-certificates-name
    intent: Update a rulestack certificate object
    question: How do I change the signer ARN of an existing rulestack certificate?
  phrasing_ops: 5
  slug: palo-alto-networks-certificateobjects-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Certificates API from Palo Alto Networks — 15 operation(s) for certificates.
  name: Palo Alto Networks Certificates API
  phrasing_intents:
  - id: get-sse-config-v1-certificates
    intent: List certificates in a Prisma Access SSE folder
    question: Which certificates are configured in a given Prisma Access folder on the SSE config API?
  - id: post-sse-config-v1-certificates
    intent: Generate a certificate in a Prisma Access SSE folder
    question: How do I generate a new certificate inside a Prisma Access folder with the SSE config API?
  - id: delete-sse-config-v1-certificates-id
    intent: Delete a certificate from Prisma Access SSE config
    question: How do I remove a certificate from the Prisma Access SSE configuration?
  - id: post-sse-config-v1-certificates:import
    intent: Import a certificate into a Prisma Access SSE folder
    question: Can I upload an existing certificate file into a Prisma Access SSE folder?
  - id: ListCertificates
    intent: List Strata Cloud Manager certificates
    question: Which certificates are attached to a particular snippet or device in Strata Cloud Manager?
  - id: CreateCertificates
    intent: Generate a signed certificate in Strata Cloud Manager
    question: How do I generate a certificate signed by an existing CA in Strata Cloud Manager configuration?
  - id: ImportCertificates
    intent: Import a certificate into Strata Cloud Manager
    question: How do I bring my own certificate file into Strata Cloud Manager configuration without choosing a folder?
  - id: GetCertificatesByID
    intent: Get a Strata Cloud Manager certificate
    question: How can I view the settings of one managed certificate by its ID?
  phrasing_ops: 18
  slug: palo-alto-networks-certificates-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/certs/certs.md''}'
  name: Palo Alto Networks Certs API
  phrasing_intents:
  - id: get-certs-ca.pem
    intent: Download the CA certificate
    question: Where do I get the CA certificate PEM file for Defender trust?
  - id: get-certs-server-certs.sh
    intent: Get a server certificate script for a Defender
    question: How do I generate server certificates for a Defender host?
  phrasing_ops: 2
  slug: palo-alto-networks-certs-api
- baseURL: https://api.sase.paloaltonetworks.com/ai-red-teaming/data-plane/network-broker
  baseurl_source: declared
  description: The Channels API from Palo Alto Networks — 3 operation(s) for channels.
  name: Palo Alto Networks Channels API
  phrasing_intents:
  - id: listChannels
    intent: List red teaming network channels
    question: Which network channels are set up for AI red teaming?
  - id: createChannel
    intent: Create a network channel
    question: How do I add a new network channel for red teaming scans?
  - id: getChannelStats
    intent: Get network channel statistics
    question: How many network channels do I have and in what states?
  - id: getChannel
    intent: Get a network channel
    question: How do I look up one network channel's details?
  - id: updateChannel
    intent: Rename or redescribe a network channel
    question: Can I rename an existing network channel?
  phrasing_ops: 5
  slug: palo-alto-networks-channels-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The CheckovVersion API from Palo Alto Networks — 1 operation(s) for checkovversion.
  name: Palo Alto Networks Checkov Version API
  phrasing_intents:
  - id: getCheckovVersion
    intent: Get the Checkov version in use
    question: Which Checkov version is Prisma Cloud Application Security currently running?
  phrasing_ops: 1
  slug: palo-alto-networks-checkovversion-api
- baseURL: https://api.strata.paloaltonetworks.com/posture
  baseurl_source: declared
  description: Operations for managing custom posture checks including CRUD and batch operations.
  name: Palo Alto Networks Checks API
  phrasing_intents:
  - id: ListPostureChecks
    intent: List posture checks
    question: Which posture checks, custom and predefined, are available to me?
  - id: CreatePostureCheck
    intent: Create a custom posture check
    question: How do I write my own posture check against security rules?
  - id: GetPostureCheckByID
    intent: Get a posture check
    question: What rule expression and rationale does a specific posture check use?
  - id: UpdatePostureCheckByID
    intent: Update a custom posture check
    question: Can I change the severity of one of my custom posture checks?
  - id: DeletePostureCheckByID
    intent: Delete a custom posture check
    question: How do I delete a single custom posture check?
  - id: ClonePostureCheckByID
    intent: Clone a posture check
    question: Can I copy a predefined posture check and customize the copy?
  - id: BatchUpsertPostureChecks
    intent: Create or update many posture checks at once
    question: Is there a way to create and update many posture checks in a single request?
  - id: BatchDeletePostureChecks
    intent: Delete many posture checks at once
    question: Can I delete several custom posture checks in one request?
  phrasing_ops: 8
  slug: palo-alto-networks-checks-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The CI-CD Risks API from Palo Alto Networks — 5 operation(s) for ci-cd risks.
  name: Palo Alto Networks CI-CD Risks API
  phrasing_intents:
  - id: pipelineRisksGetAll
    intent: Summarize CI/CD pipeline risks
    question: What CI/CD risks exist across my repositories and pipeline systems?
  - id: pipelineRisksGetAlertsByPolicy
    intent: List events for a CI/CD risk policy
    question: Which open events are raised under a specific CI/CD risk policy?
  - id: pipelineRisksGetDetailsByPolicyGet
    intent: Get details of a CI/CD risk policy
    question: What does a given CI/CD risk policy check for?
  - id: pipelineRisksSuppressEvents
    intent: Suppress CI/CD risk events
    question: How do I silence CI/CD risk events I've accepted?
  - id: pipelineRisksUnsuppressEvents
    intent: Unsuppress CI/CD risk events
    question: Can I bring back CI/CD risk events I suppressed earlier?
  phrasing_ops: 5
  slug: palo-alto-networks-ci-cd-risks-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The ciderRepository API from Palo Alto Networks — 3 operation(s) for ciderrepository.
  name: Palo Alto Networks Cider Repository API
  phrasing_intents:
  - id: getVCSRepositoryCount
    intent: Count VCS repositories
    question: How many code repositories are connected for CI/CD security?
  - id: inCiderFilterData
    intent: Get repository filter options
    question: What fields can I filter code repositories by?
  - id: reposFilter
    intent: Search VCS repositories
    question: Can I search my VCS repositories by name?
  phrasing_ops: 3
  slug: palo-alto-networks-ciderrepository-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Cie Token Resource API API from Palo Alto Networks — 2 operation(s) for cie token resource api.
  name: Palo Alto Networks Cie Token Resource API
  phrasing_intents:
  - id: PostMtManage5gCieToken
    intent: Store a tenant's Cloud Identity Engine token
    question: How do I authorize identity sync for a leaf tenant by saving its Cloud Identity Engine token?
  - id: PostMtManage5gCieTokenDetails
    intent: Check a tenant's CIE token status
    question: Is my leaf tenant's Cloud Identity Engine token still valid?
  phrasing_ops: 2
  slug: palo-alto-networks-cie-token-resource-api-api
- baseURL: https://api.dig.security
  baseurl_source: declared
  description: '{''$ref'': ''desc/classification/classification.md''}'
  name: Palo Alto Networks Classification API
  phrasing_intents:
  - id: post-classification-asset-files-id
    intent: List classified files in a data asset
    question: Which files in a data asset contain sensitive data types?
  - id: post-classification-asset-fields-id
    intent: List classified fields in a data asset
    question: Which database fields in an asset hold sensitive data?
  - id: get-classification-data-types
    intent: List data types found by classification
    question: What sensitive data types has classification found across my data?
  phrasing_ops: 3
  slug: palo-alto-networks-classification-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: You can use the APIs in this category to perform operations that are nonspecific to cloud account types, such as listing all the cloud accounts, listing supported features, and deleting an account. Fo
  name: Palo Alto Networks Cloud Accounts (All) API
  phrasing_intents:
  - id: list-cloud-account-status-details
    intent: See which security capabilities are failing for an account
    question: Why is my cloud account showing warnings or errors in Prisma Cloud?
  - id: get-cloud-accounts
    intent: List all onboarded cloud accounts
    question: What cloud accounts have been onboarded so far?
  - id: get-cloud-account-names
    intent: List cloud account names and IDs
    question: How do I get just the names and IDs of my active cloud accounts?
  - id: get-cloud-account-names-by-post
    intent: Filter cloud account names with custom criteria
    question: Can I filter cloud account names by an arbitrary filter key and value over a time range?
  - id: get-cloud-types
    intent: List supported cloud types
    question: Which cloud providers can be onboarded as accounts?
  - id: get-cloud-account
    intent: Get details of one cloud account
    question: How can I see the full details and features of a single cloud account?
  - id: delete-cloud-account
    intent: Remove an onboarded cloud account
    question: How do I offboard a cloud account from Prisma Cloud?
  - id: patch-cloud-account
    intent: Update a cloud account’s settings
    question: Can I change the account groups or auto consent setting on an onboarded account?
  phrasing_ops: 14
  slug: palo-alto-networks-cloud-accounts-all-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: To begin monitoring the resources on your cloud infrastructure, you must first connect your public cloud accounts to Prisma™ Cloud. When you add your cloud account to Prisma Cloud, the API integration
  name: Palo Alto Networks Cloud Accounts API
  phrasing_intents:
  - id: get-cloud-accounts
    intent: List all onboarded cloud accounts
    question: Which cloud accounts are onboarded to Prisma Cloud right now?
  - id: get-cloud-account-names
    intent: Get cloud account IDs and names
    question: What are the IDs and names of my active cloud accounts?
  - id: get-cloud-account-names-by-post
    intent: Look up cloud account names with a filter body
    question: Can I filter cloud account names by a time range and a filter key in a POST body?
  - id: get-cloud-org-accounts
    intent: List member accounts under a cloud organization
    question: Which child accounts or projects sit under my onboarded cloud organization?
  - id: get-cloud-types
    intent: List supported cloud types
    question: What cloud types does Prisma Cloud support?
  - id: get-cloud-account-owners
    intent: List owner emails for a cloud account
    question: Who owns this cloud account?
  - id: add-cloud-account
    intent: Onboard a cloud account by cloud type
    question: How do I onboard a new Azure, GCP or Alibaba account into Prisma Cloud?
  - id: generateterraformscript
    intent: Generate an OCI onboarding Terraform script
    question: How do I get a Terraform template to onboard my Oracle Cloud tenancy?
  phrasing_ops: 35
  slug: palo-alto-networks-cloud-accounts-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: To monitor the resources on your AWS cloud infrastructure, you must first add your AWS accounts to Prisma Cloud. When you add your cloud account to Prisma Cloud, the API integration between AWS and Pr
  name: Palo Alto Networks Cloud Accounts (AWS) API
  phrasing_intents:
  - id: add-aws-cloud-account
    intent: Onboard an AWS cloud account
    question: How do I onboard an AWS account into Prisma Cloud using an IAM role ARN?
  - id: get-ancestors-for-given-members-ous
    intent: List ancestors of AWS member accounts and OUs
    question: Which parent OUs sit above certain member accounts in my onboarded AWS organization?
  - id: update-aws-cloud-account
    intent: Update an onboarded AWS cloud account
    question: How do I change the role ARN or features on an AWS account already in Prisma Cloud?
  - id: get-list-of-children-under-parent-aws
    intent: List child OUs and accounts under an AWS parent
    question: What accounts and OUs live directly under a given organizational unit in my AWS organization?
  - id: get-aws-cloud-account-status
    intent: Check the status of an AWS cloud account
    question: Why is my AWS account showing errors in Prisma Cloud — what do its status messages say?
  - id: get-ancestors-for-given-members-ous-legacy
    intent: List AWS ancestors via the legacy endpoint
    question: Is there an older cloud-accounts-manager endpoint for finding the ancestors of AWS member accounts?
  - id: get-list-of-children-under-parent-aws-legacy
    intent: List AWS OU children via the legacy endpoint
    question: Is there a legacy call to list child accounts and OUs under an AWS parent without sending credentials in the body?
  - id: generate-cft-template-link-aws
    intent: Generate an AWS CloudFormation quick-create link
    question: How do I get a CloudFormation quick-create link with a presigned template URL for onboarding AWS?
  phrasing_ops: 11
  slug: palo-alto-networks-cloud-accounts-aws-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: 'To monitor the resources on your Azure cloud infrastructure, you must first add your Azure accounts to Prisma Cloud. When you add your cloud account to Prisma Cloud, the API integration between Azure '
  name: Palo Alto Networks Cloud Accounts (Azure) API
  phrasing_intents:
  - id: add-azure-cloud-account
    intent: Onboard an Azure account to Prisma Cloud
    question: How do I connect an Azure subscription or tenant to Prisma Cloud?
  - id: update-azure-cloud-account
    intent: Update an onboarded Azure account
    question: How do I rotate the client secret on an Azure account already in Prisma Cloud?
  - id: get-azure-cloud-account-status
    intent: Check an Azure account's onboarding status
    question: Will my Azure credentials work before I actually onboard the account?
  - id: get-ancestors-for-given-subscriptions-and-management-groups
    intent: List ancestors of Azure subscriptions
    question: Which management groups does an Azure subscription sit under?
  - id: list-children-under-parent
    intent: List management groups and subscriptions under a parent
    question: What management groups and subscriptions are under my Azure tenant?
  - id: generate-template-link
    intent: Generate the Azure onboarding Terraform template
    question: How do I get the Terraform template to grant Prisma Cloud access to Azure?
  phrasing_ops: 6
  slug: palo-alto-networks-cloud-accounts-azure-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: To monitor the resources on your GCP cloud infrastructure, you must first add your GCP accounts to Prisma Cloud. When you add your cloud account to Prisma Cloud, the API integration between GCP and Pr
  name: Palo Alto Networks Cloud Accounts (GCP) API
  phrasing_intents:
  - id: get-gcp-cloud-account-status
    intent: Check a GCP account's onboarding status
    question: Will my GCP project onboard cleanly into Prisma Cloud with the security features I picked?
  - id: add-gcp-cloud-account
    intent: Onboard a GCP account to Prisma Cloud
    question: How do I connect a new GCP project or organization to Prisma Cloud?
  - id: update-gcp-cloud-account
    intent: Update an onboarded GCP account
    question: How do I change the settings of a GCP account that's already onboarded?
  - id: get-list-of-children-under-parent
    intent: List GCP folders and projects under a parent
    question: What folders and projects sit directly under my GCP organization or folder?
  - id: get-ancestors-for-given-projects-folders
    intent: List ancestors of GCP projects and folders
    question: Which folders and organization does a given GCP project roll up to?
  - id: get-previously-saved-resource-hierarchy
    intent: Get a cloud account's saved resource hierarchy
    question: What resource hierarchy selection did I save for a cloud account?
  - id: get-list-of-folders-under-parent
    intent: List only the child folders of a parent
    question: What folders exist under my GCP organization, without the projects?
  - id: get-list-of-projects-under-parent
    intent: List only the child projects of a parent
    question: Which GCP projects live under a specific folder, excluding subfolders?
  phrasing_ops: 9
  slug: palo-alto-networks-cloud-accounts-gcp-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: To monitor the resources on your OCI or Alibaba cloud infrastructure, you must first add your OCI or Alibaba accounts to Prisma Cloud. When you add your cloud account to Prisma Cloud, the API integrat
  name: Palo Alto Networks Cloud Accounts (OCI and Alibaba) API
  phrasing_intents:
  - id: generateterraformscript
    intent: Generate the OCI onboarding Terraform script
    question: How do I get a Terraform script to onboard my Oracle Cloud tenancy to Prisma Cloud?
  - id: get-cloud-account-status
    intent: Trial-run OCI or Alibaba account onboarding
    question: Can I validate my Oracle Cloud or Alibaba Cloud parameters before adding the account?
  - id: add-cloud-account
    intent: Onboard an OCI or Alibaba cloud account
    question: How do I add an Oracle Cloud or Alibaba Cloud account to Prisma Cloud?
  - id: update-cloud-account
    intent: Update an OCI or Alibaba cloud account
    question: How do I change the settings of an Oracle Cloud account already onboarded?
  - id: getCloudDeploymentTypes
    intent: List Alibaba cloud deployment types
    question: Which deployment types can I choose when onboarding an Alibaba Cloud account?
  phrasing_ops: 5
  slug: palo-alto-networks-cloud-accounts-oci-and-alibaba-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/cloud/cloud.md''}'
  name: Palo Alto Networks Cloud API
  phrasing_intents:
  - id: get-cloud-discovery
    intent: Get cloud discovery scan results (v34.03)
    question: What did the last cloud discovery scan find, according to the v34.03 API?
  - id: get-cloud-discovery-download
    intent: Export cloud discovery results (v34.03)
    question: Can I download cloud discovery scan results as a file with version v34.03?
  - id: get-cloud-discovery-entities
    intent: List discovered cloud entities (v34.03)
    question: Which discovered cloud entities are undefended, per the v34.03 API?
  - id: post-cloud-discovery-scan
    intent: Start a cloud discovery scan (v34.03)
    question: How do I kick off a cloud discovery scan through the v34.03 API?
  - id: post-cloud-discovery-stop
    intent: Stop a running cloud discovery scan (v34.03)
    question: How do I cancel a cloud discovery scan that is running, on v34.03?
  - id: get-cloud-discovery-vms
    intent: List discovered VMs (v34.03)
    question: Which discovered virtual machines lack a Defender, per the v34.03 API?
  - id: getApiV3404CloudDiscovery
    intent: Get cloud discovery scan results
    question: Which cloud services and registries did discovery find in my accounts?
  - id: getApiV3404CloudDiscoveryDownload
    intent: Download cloud discovery scan results
    question: How do I download a CSV of cloud discovery results in Prisma Cloud Compute?
  phrasing_ops: 12
  slug: palo-alto-networks-cloud-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The Cloud Dynamic User Groups API from Palo Alto Networks — 4 operation(s) for cloud dynamic user groups.
  name: Palo Alto Networks Cloud Dynamic User Groups API
  phrasing_intents:
  - id: GetDirectory-syncV1Cloud-dug-definitionCategory
    intent: List dynamic group categories for a directory
    question: Which categories and context attributes can I use to build cloud dynamic user groups?
  - id: GetDirectory-syncV1User-attr-values
    intent: List the values of a user attribute
    question: What distinct values does a user attribute like department have in my directory?
  - id: PostDirectory-syncV1Cloud-dug-definition
    intent: Create cloud dynamic user groups
    question: How do I create a user group that updates automatically from directory attributes?
  - id: GetDirectory-syncV1Cloud-dug-definitionGroup
    intent: List or look up cloud dynamic user groups
    question: Which cloud dynamic user groups exist in my directory?
  - id: PutDirectory-syncV1Cloud-dug-definitionGroup
    intent: Update a cloud dynamic user group
    question: How do I change the attribute constraints of an existing cloud dynamic user group?
  - id: DeleteDirectory-syncV1Cloud-dug-definitionGroup
    intent: Delete cloud dynamic user groups
    question: How do I delete one cloud dynamic user group by its object GUID?
  phrasing_ops: 6
  slug: palo-alto-networks-cloud-dynamic-user-groups-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Cloud Ingested Logs API from Palo Alto Networks — 5 operation(s) for cloud ingested logs.
  name: Palo Alto Networks Cloud Ingested Logs API
  phrasing_intents:
  - id: get-eventbridge-configuration-details
    intent: Get an AWS account's EventBridge log config
    question: How is EventBridge audit log ingestion set up for one of my AWS accounts?
  - id: save-or-update-eventbridge-config
    intent: Save or update an account's EventBridge config
    question: How do I save EventBridge log ingestion settings for an AWS account?
  - id: get-eventbridge-configuration-status
    intent: Check an account's EventBridge config status
    question: Is EventBridge log ingestion working for my AWS account yet?
  - id: generate-eventbridge-cft
    intent: Download the EventBridge CloudFormation template
    question: Where do I get the CloudFormation template to set up EventBridge in my AWS account?
  phrasing_ops: 4
  slug: palo-alto-networks-cloud-ingested-logs-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Use code to cloud dashboard to get a continuously updated snapshot view into the security posture of your cloud environment, streamline tracking and reporting. You can use the following APIs to get th
  name: Palo Alto Networks Code to Cloud API
  phrasing_intents:
  - id: code-to-cloud-list-deploy-trend
    intent: Get the 30-day deploy-time vulnerability trend
    question: How have critical and high image vulnerabilities trended over the last 30 days?
  - id: code-to-cloud-list-runtime-trend
    intent: Get the 30-day runtime alert trend
    question: How have open critical and high runtime alerts trended this month?
  phrasing_ops: 2
  slug: palo-alto-networks-code-to-cloud-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The CodeFixes API from Palo Alto Networks — 1 operation(s) for codefixes.
  name: Palo Alto Networks Code Fixes API
  phrasing_intents:
  - id: fixCheckovErrors
    intent: Suggest fixes for IaC misconfigurations
    question: Can I get suggested fixes for misconfigurations in my Terraform or other IaC files?
  phrasing_ops: 1
  slug: palo-alto-networks-codefixes-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The Coderepos-Ci API from Palo Alto Networks — 2 operation(s) for coderepos-ci.
  name: Palo Alto Networks Coderepos Ci API
  phrasing_intents:
  - id: post-coderepos-ci-evaluate
    intent: Evaluate a code repo CI scan (v34.03)
    question: Can I evaluate a code repository scan result against policy on the v34.03 API?
  - id: postApiV3404CodereposCiEvaluate
    intent: Evaluate a code repo CI scan (v34.04)
    question: How do I resolve code repos from a CI scan on the v34.04 API?
  phrasing_ops: 2
  slug: palo-alto-networks-coderepos-ci-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: '{''$ref'': ''desc/collections/collections.md''}'
  name: Palo Alto Networks Collections API
  phrasing_intents:
  - id: get-collections
    intent: List Compute collections (v34.03)
    question: Which Compute collections exist when I call the v34.03 API?
  - id: post-collections
    intent: Add a Compute collection (v34.03)
    question: How do I group images and hosts into a new collection on v34.03?
  - id: delete-collections-id
    intent: Delete a Compute collection (v34.03)
    question: How do I delete a Compute collection with the v34.03 API?
  - id: put-collections-id
    intent: Update a Compute collection (v34.03)
    question: Can I change which hosts belong to an existing collection on v34.03?
  - id: get-collections-id-usages
    intent: See which policies use a collection (v34.03)
    question: Which policies reference a given collection, using v34.03?
  - id: getApiV3404Collections
    intent: List Compute collections (v34.04)
    question: What collections are configured in Compute on the v34.04 API?
  - id: postApiV3404Collections
    intent: Add a Compute collection (v34.04)
    question: How do I create a collection of containers and functions on v34.04?
  - id: deleteApiV3404CollectionsById
    intent: Delete a Compute collection (v34.04)
    question: Is there a v34.04 call to permanently delete a collection?
  phrasing_ops: 15
  slug: palo-alto-networks-collections-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Command Center API from Palo Alto Networks — 5 operation(s) for command center.
  name: Palo Alto Networks Command Center API
  phrasing_intents:
  - id: command-center-list-total-alerts-by-severity
    intent: Count alerts by severity for a swimlane
    question: How many critical, high and medium alerts do I have in the command center?
  - id: command-center-list-top-assets
    intent: List assets with the most alerts
    question: Which cloud assets have the highest number of alerts?
  - id: command-center-list-top-policies
    intent: List policies generating the most alerts
    question: Which policies are triggering the most alerts?
  - id: command-center-list-top-vulnerabilities
    intent: List hosts and images with most vulnerabilities
    question: Which hosts and container images have the most vulnerabilities?
  - id: command-center-list-total-vulnerable-images-hosts
    intent: Summarize vulnerable images and hosts
    question: How many of my images and hosts are vulnerable in total?
  phrasing_ops: 5
  slug: palo-alto-networks-command-center-api
- baseURL: https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1
  baseurl_source: declared
  description: Analytics and reporting for compliance frameworks including summaries, scores, and timelines.
  name: Palo Alto Networks Compliance Analytics API
  phrasing_intents:
  - id: getCFSummary
    intent: List compliance framework summaries (legacy path)
    question: How do I get a summary of compliance frameworks from the older unversioned summaries endpoint?
  - id: getOverallCompliance
    intent: Get a framework's compliance scores (legacy path)
    question: What are the overall compliance scores for a framework via the older unversioned call?
  - id: getConfigurationsAssessedTimeline
    intent: Get a 30-day compliance timeline (legacy path)
    question: How has a framework's compliance score trended over the last 30 days on the legacy API?
  - id: getConfigurationsAssessed
    intent: Get assessed configurations (legacy path)
    question: Which configurations were assessed for a framework using the unversioned endpoint?
  - id: getComplianceControls
    intent: Get a framework's controls (legacy path)
    question: What controls make up a compliance framework, using the older unversioned call?
  - id: ListComplianceFrameworkSummaries
    intent: List compliance framework summaries (v1)
    question: Which compliance frameworks are available, summarized per current revision in v1?
  - id: GetOverallCompliance
    intent: Get a framework's compliance scores (v1)
    question: How compliant am I with a given framework overall, per the v1 API?
  - id: GetComplianceTimeline
    intent: Get a compliance score timeline up to a year (v1)
    question: Can I see a framework's compliance trend over a full year, not just 30 days?
  phrasing_ops: 10
  slug: palo-alto-networks-compliance-analytics-api
- baseURL: https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1
  baseurl_source: declared
  description: Operations for managing compliance framework definitions including CRUD, clone, benchmark, and release operations.
  name: Palo Alto Networks Compliance Frameworks API
  phrasing_intents:
  - id: getAllFrameworks
    intent: List compliance frameworks (unversioned path)
    question: Which compliance frameworks exist in my tenant service group, via the unversioned definitions endpoint?
  - id: createFramework
    intent: Create a compliance framework (unversioned path)
    question: How do I define a new compliance framework through the unversioned definitions endpoint?
  - id: getLatestRevision
    intent: Get a framework revision (unversioned path)
    question: Can I fetch the in-progress draft of a framework from the unversioned definitions endpoint?
  - id: updateFramework
    intent: Update a compliance framework (unversioned path)
    question: How does editing a framework on the unversioned endpoint decide between the in-progress draft and a new revision?
  - id: deleteFramework
    intent: Delete a compliance framework (unversioned path)
    question: Does deleting a framework on the unversioned definitions endpoint remove every revision too?
  - id: cloneFramework
    intent: Clone a compliance framework (unversioned path)
    question: Can I copy an existing framework into my TSG using the unversioned clone action?
  - id: benchmarkFramework
    intent: Mark framework as benchmark (unversioned path)
    question: How do I flag a framework as a benchmark on the unversioned definitions endpoint?
  - id: unBenchmarkFramework
    intent: Remove benchmark flag (unversioned path)
    question: Can I clear the benchmark designation from a framework via the unversioned definitions endpoint?
  phrasing_ops: 16
  slug: palo-alto-networks-compliance-frameworks-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Compliance Posture API methods provide information related to your compliance posture across various compliance standards. The filters available through the API enable you to view your status acro
  name: Palo Alto Networks Compliance Posture API
  phrasing_intents:
  - id: get-compliance-posture
    intent: Get the v1 compliance pass/fail breakdown
    question: How do I get passed and failed counts across all my compliance standards for the last few days using the original v1 posture endpoint?
  - id: post-compliance-posture
    intent: Query the v1 compliance breakdown with body filters
    question: Is there a POST version of the old compliance statistics breakdown that takes filters and a time range in the request body?
  - id: get-compliance-posture-for-standard
    intent: Get v1 compliance stats for one standard
    question: What are the passed and failed results for a single compliance standard over a set time window in the v1 API?
  - id: post-compliance-posture-for-standard
    intent: Query v1 compliance stats for a standard by POST
    question: Can I send body filters and a time range when fetching one standard's compliance statistics in the legacy API?
  - id: get-compliance-posture-for-requirement
    intent: Get v1 compliance stats for one requirement
    question: How can I see section-level pass/fail results for one requirement inside a compliance standard with the v1 API?
  - id: post-compliance-posture-for-requirement
    intent: Query v1 requirement compliance stats by POST
    question: Is there a POST endpoint for the old per-requirement compliance breakdown that accepts body filters?
  - id: get-compliance-posture-trend
    intent: Get the v1 compliance trend over time
    question: How has my overall pass/fail compliance trended over the past month in the v1 API?
  - id: post-compliance-posture-trend
    intent: Query the v1 compliance trend by POST
    question: Can I request the old overall compliance trend with filters and a time range in a POST body?
  phrasing_ops: 26
  slug: palo-alto-networks-compliance-posture-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: You can create your own custom compliance standards that are tailored to your own business needs, standards, and organizational policies. When defining a custom compliance standard, you can add requir
  name: Palo Alto Networks Compliance Standards API
  phrasing_intents:
  - id: get-all-standards
    intent: List compliance standards
    question: Which compliance standards, built-in and custom, are available in my Prisma Cloud tenant?
  - id: add-standard
    intent: Create a custom compliance standard
    question: How do I create my own compliance standard for internal controls?
  - id: get-standards-by-id
    intent: Get a compliance standard
    question: What are the details of a specific compliance standard, like how many policies are assigned?
  - id: update-standard
    intent: Update a compliance standard
    question: Can I rename an existing custom compliance standard?
  - id: delete-standard
    intent: Delete a compliance standard
    question: How do I remove a custom compliance standard we no longer use?
  - id: clone-standard
    intent: Clone a compliance standard
    question: Can I copy an existing compliance standard to start a customized version of it?
  - id: get-requirements
    intent: List requirements in a compliance standard
    question: What requirements make up a particular compliance standard?
  - id: add-requirement
    intent: Add a requirement to a compliance standard
    question: How do I add a new requirement to my custom compliance standard?
  phrasing_ops: 15
  slug: palo-alto-networks-compliance-standards-api
- baseURL: https://api.strata.paloaltonetworks.com/posture
  baseurl_source: declared
  description: Operations for identifying unused or redundant configuration objects.
  name: Palo Alto Networks Config Cleanup API
  phrasing_intents:
  - id: GetZeroHitRules
    intent: Find security rules that never matched traffic
    question: Which of my security rules have never been hit and could be cleaned up?
  phrasing_ops: 1
  slug: palo-alto-networks-config-cleanup-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Config Match List
  name: Palo Alto Networks Config Match List API
  phrasing_intents:
  - id: ListConfigMatchList
    intent: List config match list entries
    question: What config log match list entries are defined in a folder?
  - id: CreateConfigMatchList
    intent: Create a config match list entry
    question: How do I forward config logs that match a filter to syslog or email?
  - id: GetConfigMatchListByID
    intent: Get a config match list entry
    question: How can I view one config match list entry's filter and destinations?
  - id: UpdateConfigMatchListByID
    intent: Update a config match list entry
    question: Can I change the filter on an existing config match list?
  - id: DeleteConfigMatchListByID
    intent: Delete a config match list entry
    question: How do I delete a config match list entry?
  phrasing_ops: 5
  slug: palo-alto-networks-config-match-list-api
- baseURL: https://api.strata.paloaltonetworks.com/posture
  baseurl_source: declared
  description: Config file upload for BPA result.
  name: Palo Alto Networks Config Upload API
  phrasing_intents:
  - id: InitiateConfigUpload
    intent: Start a config file upload for best practice assessment
    question: How do I upload a firewall config to run a Best Practice Assessment?
  - id: GetBpaResultByID
    intent: Check a Best Practice Assessment result
    question: Has my Best Practice Assessment finished processing?
  phrasing_ops: 2
  slug: palo-alto-networks-config-upload-api
- baseURL: https://api.strata.paloaltonetworks.com/config/operations/v1
  baseurl_source: declared
  description: Config Versions
  name: Palo Alto Networks Config Versions API
  phrasing_intents:
  - id: LoadConfigVersions
    intent: Load a config version into the candidate
    question: Can I load an older configuration version into my candidate config?
  - id: PushCandidateConfigVersions
    intent: Push the candidate configuration
    question: How do I push my candidate configuration out to devices?
  - id: ListConfigVersions
    intent: List configuration versions
    question: What configuration versions have been saved so far?
  - id: DeleteCandidateConfigVersions
    intent: Discard the candidate config
    question: Can I throw away my candidate changes and roll back to the running config?
  - id: GetConfigVersionsByID
    intent: Get a specific configuration version
    question: How can I view the contents of one saved configuration version?
  - id: GetRunningConfigVersions
    intent: Get the running config version per folder
    question: Which configuration version is currently running in each folder?
  phrasing_ops: 6
  slug: palo-alto-networks-config-versions-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The Configuration Management API from Palo Alto Networks — 1 operation(s) for configuration management.
  name: Palo Alto Networks Configuration Management API
  phrasing_intents:
  - id: PostSeb-apiV1Configuration-managementDraftPublish
    intent: Publish the configuration draft
    question: How do I publish my pending configuration draft so it takes effect?
  - id: get-sse-config-v1-config-versions
    intent: List candidate configuration versions
    question: What candidate configuration versions exist in Prisma Access?
  - id: delete-sse-config-v1-config-versions-candidate
    intent: Discard candidate changes and revert to running
    question: How do I throw away uncommitted changes and go back to the running configuration?
  - id: post-sse-config-v1-config-versions-candidate:push
    intent: Push the candidate configuration to folders
    question: How do I push my pending Prisma Access candidate changes out to a folder?
  - id: get-sse-config-v1-config-versions-running
    intent: Show the running configuration
    question: What configuration is currently running in each Prisma Access folder?
  - id: get-sse-config-v1-config-versions-version
    intent: Get a configuration by version number
    question: How do I view a specific past configuration version?
  - id: post-sse-config-v1-config-versions:load
    intent: Load a configuration from a snapshot version
    question: How do I load an older snapshot as my candidate configuration?
  - id: get-sse-config-v1-jobs
    intent: List configuration job history
    question: What configuration push and commit jobs have run recently?
  phrasing_ops: 10
  slug: palo-alto-networks-configuration-management-api
- baseURL: https://api.strata.paloaltonetworks.com
  baseurl_source: declared
  description: The Connection Source API from Palo Alto Networks — 7 operation(s) for connection source.
  name: Palo Alto Networks Connection Source API
  phrasing_intents:
  - id: ListConnectionSources
    intent: List DNS resolver connection sources
    question: Which connection sources are set up for my DNS resolver?
  - id: CreateConnectionSource
    intent: Create a connection source
    question: How do I add a new connection source tied to a resolver profile?
  - id: ListSubnets
    intent: List all tenant subnets
    question: What subnets are registered across my whole tenant, regardless of connection source?
  - id: GetSubnetByID
    intent: Get a tenant subnet
    question: How do I look up one tenant subnet by its ID without knowing its connection source?
  - id: DeleteConnectionSourceByID
    intent: Delete a connection source
    question: How do I remove a connection source I no longer need?
  - id: GetConnectionSourceByID
    intent: Get a connection source
    question: Which profile is a specific connection source associated with?
  - id: UpdateConnectionSourceByID
    intent: Update a connection source
    question: How do I point an existing connection source at a different profile?
  - id: ListConnectionSourceSubnets
    intent: List a connection source's subnets
    question: Which subnets belong to one particular connection source?
  phrasing_ops: 12
  slug: palo-alto-networks-connection-source-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Connector API from Palo Alto Networks — 13 operation(s) for connector.
  name: Palo Alto Networks Connector API
  phrasing_intents:
  - id: list.connectors.v2
    intent: List ZTNA connectors
    question: Which ZTNA connectors are deployed in my Prisma Access tenant?
  - id: create.connector.v2
    intent: Create a ZTNA connector
    question: How do I register a new ZTNA connector and put it in a connector group?
  - id: get.connector.v2
    intent: Get a ZTNA connector's details
    question: What is the current configuration of one specific ZTNA connector?
  - id: update.connector.v2
    intent: Update a ZTNA connector
    question: How do I rename a ZTNA connector or move it to a different connector group?
  - id: delete.connector.v2
    intent: Delete a ZTNA connector
    question: How do I remove a ZTNA connector I no longer use?
  - id: list.connector.filters.v2
    intent: Get filter values for connector fields
    question: What values can I filter ZTNA connectors by for a given field?
  - id: get.connector.quiesce.v2
    intent: Check a connector's quiesce state
    question: Is a particular ZTNA connector currently quiesced?
  - id: update.connector.quiesce.v2
    intent: Quiesce or resume a ZTNA connector
    question: How do I put a ZTNA connector into quiesce mode before taking it down?
  phrasing_ops: 22
  slug: palo-alto-networks-connector-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Connector-Group API from Palo Alto Networks — 9 operation(s) for connector-group.
  name: Palo Alto Networks Connector Group API
  phrasing_intents:
  - id: list.connector_groups.v2
    intent: List connector groups
    question: What connector groups do I have set up for private app access?
  - id: create.connector_group.v2
    intent: Create a connector group
    question: How do I create a new connector group in Palo Alto Networks ZTNA Connector?
  - id: get.connector_group.v2
    intent: Get a connector group
    question: What are the settings of a single connector group?
  - id: update.connector_group.v2
    intent: Update a connector group
    question: How do I rename an existing connector group?
  - id: delete.connector-group.v2
    intent: Delete a connector group
    question: How do I remove a connector group I no longer need?
  - id: list.connector_group.filters.v2
    intent: List filter values for connector group fields
    question: What values can I filter connector groups on for a given field?
  - id: list.connector_group.connectors.v2
    intent: List connectors in a connector group
    question: Which connectors belong to a particular connector group?
  - id: list.connector_group.fqdn_rules.v2
    intent: List FQDN applications served by a connector group
    question: Which FQDN applications are routed through a connector group?
  phrasing_ops: 15
  slug: palo-alto-networks-connector-group-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: Content Cloud Settings
  name: Palo Alto Networks Content Cloud Settings API
  phrasing_intents:
  - id: ListContentCloudSettings
    intent: List Content Cloud settings
    question: What Content Cloud settings are defined across my folders?
  - id: CreateContentCloudSettings
    intent: Create Content Cloud settings
    question: How do I create a new Content Cloud settings object?
  - id: GetContentCloudSettingsByID
    intent: Get Content Cloud settings
    question: What is in a specific Content Cloud settings object?
  - id: UpdateContentCloudSettingsByID
    intent: Update Content Cloud settings
    question: How do I change existing Content Cloud settings?
  - id: DeleteContentCloudSettingsByID
    intent: Delete Content Cloud settings
    question: How do I delete a Content Cloud settings object?
  phrasing_ops: 5
  slug: palo-alto-networks-content-cloud-settings-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: Content-ID Settings
  name: Palo Alto Networks Content-ID Settings API
  phrasing_intents:
  - id: ListContentIDSettings
    intent: List Content-ID settings
    question: What Content-ID settings apply to a folder or device?
  - id: CreateContentIDSettings
    intent: Create Content-ID settings
    question: How do I define new Content-ID settings?
  - id: GetContentIDSettingsByID
    intent: Get Content-ID settings by id
    question: What values are in one specific Content-ID settings object?
  - id: UpdateContentIDSettingsByID
    intent: Update Content-ID settings
    question: How do I change existing Content-ID settings?
  - id: DeleteContentIDSettingsByID
    intent: Delete Content-ID settings
    question: How do I delete a Content-ID settings object?
  phrasing_ops: 5
  slug: palo-alto-networks-content-id-settings-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Control Plane Resource API API from Palo Alto Networks — 9 operation(s) for control plane resource api.
  name: Palo Alto Networks Control Plane Resource API
  phrasing_intents:
  - id: GetMtManage5gControlCertDownload
    intent: Download the 5G security certificate
    question: How do I download the certificate needed to activate 5G connectivity for a region?
  - id: GetMtManage5gControlProxycert
    intent: Check whether a 5G proxy certificate exists
    question: Is a proxy certificate already present in my root TSG before 5G activation?
  - id: PostMtManage5gControlProxycertUpload
    intent: Upload a 5G proxy certificate
    question: How do I upload a proxy certificate to secure 5G control plane signaling?
  - id: GetMtManage5gControlRadiusproxy
    intent: Get the RADIUS proxy shared secret
    question: Where can I audit the RADIUS proxy shared secret configured on the root TSG?
  - id: PostMtManage5gControlRadiusproxy
    intent: Configure the RADIUS proxy server
    question: How do I point the 5G control plane at a RADIUS proxy by name and IP address?
  - id: GetMtManage5gControlRadiussecret
    intent: View the RADIUS shared secret
    question: How can I see the active RADIUS shared secret to troubleshoot 5G auth failures?
  - id: PostMtManage5gControlRadiussecret
    intent: Set or rotate the RADIUS shared secret
    question: How do I rotate the RADIUS shared secret for the root TSG?
  - id: GetMtManage5gControlRadiusservers
    intent: List RADIUS servers for 5G
    question: Which RADIUS servers are configured for 5G connectivity in my region?
  phrasing_ops: 12
  slug: palo-alto-networks-control-plane-resource-api-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Credential Management.
  name: Palo Alto Networks Credential Management API
  phrasing_intents:
  - id: get-public-cms-conf
    intent: List Credential Manager Service configurations
    question: Which Credential Manager Service configurations are set up for my company?
  - id: post-public-cms-conf
    intent: Add Credential Manager Service configurations
    question: How do I connect a privileged access management vault as a new Credential Manager Service?
  - id: put-public-cms-conf
    intent: Update a Credential Manager Service configuration
    question: How do I change the settings of an existing credential manager configuration?
  - id: get-public-cms-conf-id
    intent: Get one Credential Manager Service configuration
    question: What are the details of a single credential manager configuration by its ID?
  - id: delete-public-cms-conf-id
    intent: Delete a Credential Manager Service configuration
    question: How do I remove a credential manager configuration we no longer use?
  - id: post-public-cms-conf-test
    intent: Test a credential manager connection before saving
    question: Can I test connectivity to a privileged access vault with unsaved configuration details?
  - id: post-public-cms-conf-test-id
    intent: Test a saved credential manager configuration
    question: Is my saved credential manager configuration still able to reach the vault?
  - id: get-public-cms-credential
    intent: List shared credentials
    question: What shared credentials does my company have stored?
  phrasing_ops: 14
  slug: palo-alto-networks-credential-management-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/credentials/credentials.md''}'
  name: Palo Alto Networks Credentials API
  phrasing_intents:
  - id: get-credentials
    intent: List stored credentials (v34.03)
    question: How do I list all cloud credentials stored in the credentials store with v34.03?
  - id: post-credentials
    intent: Add a credential (v34.03)
    question: How do I add a new cloud account credential through the v34.03 API?
  - id: delete-credentials-id
    intent: Delete a credential (v34.03)
    question: How do I remove a credential from the store with the v34.03 API?
  - id: get-credentials-id-usages
    intent: See where a credential is used (v34.03)
    question: Which scans and integrations use a given credential, per the v34.03 API?
  - id: getApiV3404Credentials
    intent: List stored credentials (v34.04)
    question: Which credentials are in my credentials store on the current v34.04 API?
  - id: postApiV3404Credentials
    intent: Add a credential (v34.04)
    question: Where do I register a new cloud or registry credential on v34.04?
  - id: deleteApiV3404CredentialsById
    intent: Delete a credential (v34.04)
    question: What's the v34.04 call to delete a credential I no longer need?
  - id: getApiV3404CredentialsByIdUsages
    intent: See where a credential is used (v34.04)
    question: Where is a particular credential referenced, according to the v34.04 API?
  phrasing_ops: 8
  slug: palo-alto-networks-credentials-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The Current API from Palo Alto Networks — 4 operation(s) for current.
  name: Palo Alto Networks Current API
  phrasing_intents:
  - id: get-current-collections
    intent: List my collections (v34.03)
    question: Which collections can my current user see, using the v34.03 API?
  - id: get-current-projects
    intent: List my projects (v34.03)
    question: Which projects does my current user belong to, per the v34.03 API?
  - id: getApiV3404CurrentCollections
    intent: List my collections (v34.04)
    question: What collections am I scoped to on the current v34.04 API?
  - id: getApiV3404CurrentProjects
    intent: List my projects (v34.04)
    question: What projects is the logged-in user assigned to on v34.04?
  phrasing_ops: 4
  slug: palo-alto-networks-current-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/custom-compliance/custom-compliance.md''}'
  name: Palo Alto Networks Custom Compliance API
  phrasing_intents:
  - id: get-custom-compliance
    intent: List custom compliance checks (v34.03)
    question: What custom compliance checks are defined when I call the v34.03 API version?
  - id: put-custom-compliance
    intent: Update a custom compliance check (v34.03)
    question: How do I update a custom compliance check's script through the v34.03 API?
  - id: delete-custom-compliance-id
    intent: Delete a custom compliance check (v34.03)
    question: Which v34.03 call permanently removes a custom compliance check?
  - id: getApiV3404CustomCompliance
    intent: List custom compliance checks (v34.04)
    question: Which custom compliance checks exist in the current v34.04 API?
  - id: putApiV3404CustomCompliance
    intent: Update a custom compliance check (v34.04)
    question: How do I rename a custom compliance check using the v34.04 API?
  - id: deleteApiV3404CustomComplianceById
    intent: Delete a custom compliance check (v34.04)
    question: Is it possible to permanently remove one of my custom checks through the newer v34.04 path?
  phrasing_ops: 6
  slug: palo-alto-networks-custom-compliance-api
- baseURL: https://api.strata.paloaltonetworks.com
  baseurl_source: declared
  description: The Custom FQDN API from Palo Alto Networks — 2 operation(s) for custom fqdn.
  name: Palo Alto Networks Custom FQDN API
  phrasing_intents:
  - id: ListCustomFqdns
    intent: List custom FQDN groups
    question: Which custom FQDN groups are defined for the DNS resolver?
  - id: CreateCustomFqdn
    intent: Create a custom FQDN group
    question: How do I create a custom FQDN group of internal domains for the resolver?
  - id: DeleteCustomFqdnByID
    intent: Delete a custom FQDN group
    question: Can I remove a custom FQDN group from the resolver?
  - id: GetCustomFqdnByID
    intent: Get a custom FQDN group
    question: Which domains are in a specific custom FQDN group?
  - id: UpdateCustomFqdnByID
    intent: Update a custom FQDN group
    question: How do I change the domain list of an existing custom FQDN group?
  phrasing_ops: 5
  slug: palo-alto-networks-custom-fqdn-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/custom-rules/custom-rules.md''}'
  name: Palo Alto Networks Custom Rules API
  phrasing_intents:
  - id: get-custom-rules
    intent: List custom runtime rules (v34.03)
    question: Which custom rules are defined, according to the older v34.03 API?
  - id: delete-custom-rules-id
    intent: Delete a custom rule (v34.03)
    question: How do I delete a custom rule through the v34.03 API?
  - id: put-custom-rules-id
    intent: Update a custom rule (v34.03)
    question: How do I change a custom rule's script with the v34.03 API?
  - id: getApiV3404CustomRules
    intent: List custom runtime rules (v34.04)
    question: What custom rules exist in Prisma Cloud Compute on the current v34.04 API?
  - id: deleteApiV3404CustomRulesById
    intent: Delete a custom rule (v34.04)
    question: How do I delete a custom rule using the v34.04 API?
  - id: putApiV3404CustomRulesById
    intent: Update a custom rule (v34.04)
    question: How do I edit a custom rule on the v34.04 API?
  phrasing_ops: 6
  slug: palo-alto-networks-custom-rules-api
- baseURL: https://api.sase.paloaltonetworks.com/aisec
  baseurl_source: declared
  description: Operations related to custom topic management
  name: Palo Alto Networks Custom Topic API
  phrasing_intents:
  - id: CreateNewCustomTopic
    intent: Create a custom topic
    question: How do I define a custom topic with example usages for AI security detection?
  - id: DeleteCustomTopic
    intent: Delete a custom topic
    question: Can I delete a custom topic through the normal safety-checked path?
  - id: ForceDeleteCustomTopic
    intent: Force delete a custom topic
    question: Is there a way to force delete a custom topic that fails the normal safety checks?
  - id: UpdateTopicByTopicId
    intent: Modify a custom topic
    question: Can I change the description and examples of an existing custom topic?
  - id: GetAllCustomTopicsForTsgId
    intent: List all custom topics
    question: Which custom topics exist for my tenant service group?
  phrasing_ops: 5
  slug: palo-alto-networks-custom-topic-api
- baseURL: https://api.sase.paloaltonetworks.com/ai-red-teaming/data-plane
  baseurl_source: declared
  description: Operations for custom attack configurations and prompts.
  name: Palo Alto Networks Custom Attack API
  phrasing_intents:
  - id: get_custom_attack_report_v1_custom_attacks_report__job_id__get
    intent: Get the full custom attack report for a job
    question: Where can I see the complete report for an AI red-teaming custom attack job?
  - id: get_prompt_sets_v1_custom_attacks_report__job_id__prompt_sets_get
    intent: List prompt sets in a custom attack report
    question: Which prompt sets were run as part of a custom attack job report?
  - id: get_prompts_by_set_v1_custom_attacks_report__job_id__prompt_set__prompt_set_id__prompts_get
    intent: List report prompts for one prompt set
    question: What prompts from a single prompt set were used in a custom attack report?
  - id: get_prompt_detail_v1_custom_attacks_report__job_id__prompt__prompt_id__get
    intent: Get details of one prompt in an attack report
    question: How do I see the full detail for one prompt in a custom attack report?
  - id: list_custom_attacks_v1_custom_attacks_job__job_id__list_custom_attacks_get
    intent: List the custom attacks run in a job
    question: Which individual custom attacks were executed in a red-teaming job?
  - id: get_attack_outputs_v1_custom_attacks_job__job_id__attack__attack_id__list_outputs_get
    intent: Get the outputs produced by one custom attack
    question: How do I see what the target model responded with for a specific custom attack?
  - id: get_property_stats_v1_custom_attacks_job__job_id__property_stats_get
    intent: Get property-based stats for a custom attack job
    question: Can I break down a custom attack job's results by prompt property?
  - id: create_prompt_set_v1_custom_attack_custom_prompt_set_post
    intent: Create a custom prompt set
    question: How do I create my own custom prompt set for AI red teaming?
  phrasing_ops: 27
  slug: palo-alto-networks-customattack-api
- baseURL: https://api.sase.paloaltonetworks.com/aisec
  baseurl_source: declared
  description: Operations related to customer application management
  name: Palo Alto Networks Customer App API
  phrasing_intents:
  - id: GetCustomerApp
    intent: Get an AI Runtime Security customer app
    question: Can I look up a registered customer app by its name?
  - id: DeleteCustomerApp
    intent: Delete a customer app
    question: What's needed to remove a customer app from my tenant service group?
  - id: updateCustomerAppById
    intent: Update a customer app
    question: How do I change the AI model recorded for a customer app?
  - id: GetAllCustomerAppsForTsgID
    intent: List all customer apps in my tenant
    question: Which customer apps are registered for my TSG?
  phrasing_ops: 4
  slug: palo-alto-networks-customer-app-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Dashboard API from Palo Alto Networks — 11 operation(s) for dashboard.
  name: Palo Alto Networks Dashboard API
  phrasing_intents:
  - id: getDashboardCommonErrorsByPolicyData
    intent: List policies with the most open code issues
    question: Which code security policies are failing most often in my repositories?
  - id: getDashboardErrorsBySeverityData
    intent: Count code issues by severity
    question: How many code issues do I have at each severity level?
  - id: getDashboardIacErrorsByCategoryData
    intent: Count IaC misconfigurations by category
    question: What types of infrastructure-as-code misconfigurations are most common, like IAM or networking?
  - id: getDashboardData
    intent: List the most frequent non-compliant package licenses
    question: Which non-compliant open source licenses show up most in my scanned repos?
  - id: getPrIssuesOverTimeData
    intent: Chart pull request scan results per day
    question: How many pull requests failed, passed or got resolved each day?
  - id: getDashboardTopCvssVulnerabilitiesData
    intent: List vulnerabilities with the highest CVSS scores
    question: Which vulnerabilities in my code have the highest CVSS scores?
  - id: getDashboardTopVulnerableRepositoriesData
    intent: Rank repositories by critical and high issues
    question: Which repositories have the most high and critical severity errors?
  - id: getVcsScanIssuesOverTimeData
    intent: Chart code issue statuses over 30 days
    question: How have my open, fix-pending, fixed and suppressed code issues changed day by day?
  phrasing_ops: 11
  slug: palo-alto-networks-dashboard-api
- baseURL: https://api.dlp.paloaltonetworks.com
  baseurl_source: declared
  description: The Data Patterns API from Palo Alto Networks — 2 operation(s) for data patterns.
  name: Palo Alto Networks Data Patterns API
  phrasing_intents:
  - id: get-v2-api-data-patterns
    intent: List data patterns
    question: Which DLP data patterns exist in my tenant?
  - id: post-v2-api-data-patterns
    intent: Create a custom data pattern
    question: How do I define a custom data pattern to detect our internal ID numbers?
  - id: delete-v2-api-data-patterns-resourceid
    intent: Archive a data pattern
    question: Is deleting a data pattern permanent or does it archive it?
  - id: get-v2-api-data-patterns-resourceid
    intent: Get a data pattern
    question: What matching rules does a specific data pattern use?
  - id: patch-v2-api-data-patterns-resourceid
    intent: Partially update a data pattern
    question: Can I change just the description or tags of a data pattern without resending it all?
  - id: put-v2-api-data-patterns-resourceid
    intent: Replace a data pattern
    question: How do I fully overwrite an existing data pattern's definition?
  - id: listDataPatterns
    intent: List DLP data patterns
    question: Which DLP data patterns are available, like credit card or social security number detectors?
  - id: getDataPattern
    intent: Get a DLP data pattern's detection rules
    question: What regular expressions and confidence settings does a specific data pattern use?
  phrasing_ops: 8
  slug: palo-alto-networks-data-patterns-api
- baseURL: https://api.dlp.paloaltonetworks.com
  baseurl_source: declared
  description: The Data Profiles API from Palo Alto Networks — 2 operation(s) for data profiles.
  name: Palo Alto Networks Data Profiles API
  phrasing_intents:
  - id: get-v2-api-data-profiles
    intent: List data profiles
    question: Which DLP data profiles exist for my tenant?
  - id: post-v2-api-data-profiles
    intent: Create a data profile
    question: How do I create a data profile with my own detection rules?
  - id: get-v2-api-data-profiles-resourceid
    intent: Get a data profile
    question: What detection rules does a particular data profile use?
  - id: patch-v2-api-data-profiles-resourceid
    intent: Partially update a data profile
    question: Can I change just the description of a data profile without resending everything?
  - id: put-v2-api-data-profiles-resourceid
    intent: Replace a data profile
    question: How do I fully overwrite a data profile's detection rules?
  phrasing_ops: 5
  slug: palo-alto-networks-data-profiles-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Data Resource
  name: Palo Alto Networks Data Resource API
  phrasing_intents:
  - id: post-mt-monitor-v1-agg-alerts
    intent: Count alerts across tenants
    question: How many alerts are open across all my Prisma Access tenants right now?
  - id: post-mt-monitor-v1-agg-alerts-list
    intent: List alert counts by source across tenants
    question: Which sources are generating the most alerts across my tenants?
  - id: post-mt-monitor-v1-agg-applicationusage
    intent: List application usage by application type
    question: What kinds of applications are my users consuming the most, grouped by application type?
  - id: post-mt-monitor-v1-agg-applications
    intent: Count applications across tenants
    question: How many distinct applications are seen across all my tenants?
  - id: post-mt-monitor-v1-agg-applications-list
    intent: List applications seen across tenants
    question: Which applications are actually in use across my tenants, listed out?
  - id: post-mt-monitor-v1-agg-applications-source
    intent: Count applications by source
    question: How many applications come from remote networks versus mobile users versus proxy nodes?
  - id: post-mt-monitor-v1-agg-applications-summary
    intent: Summarize risky applications across tenants
    question: How many risky applications are showing up across my tenants?
  - id: post-mt-monitor-v1-agg-incidents-count
    intent: Count incidents by severity
    question: How many critical versus warning incidents do my tenants have?
  phrasing_ops: 28
  slug: palo-alto-networks-data-resource-api-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Data Security capabilities on Prisma Cloud enable you to discover and classify data stored in AWS S3 buckets and protect accidental exposure, misuse, or sharing of sensitive data. The data dashboa
  name: Palo Alto Networks Data Security Dashboard API
  phrasing_intents:
  - id: get-dashboard-alerts
    intent: Summarize total, public, sensitive and malware objects
    question: How many of my cloud storage objects are public, sensitive, or malware?
  - id: get-dashboard-object-by-classification
    intent: Top public object counts by classification
    question: Which data classifications have the most publicly exposed objects?
  - id: get-dashboard-object-by-owner
    intent: Object exposure counts per owner
    question: Which owners have the most exposed objects in my cloud storage?
  - id: get-dashboard-object-by-region
    intent: Object counts by region and classification
    question: Which cloud regions hold the most classified objects?
  - id: get-dashboard-object-sensitive
    intent: Count sensitive objects by exposure
    question: How many sensitive objects are exposed publicly versus kept private?
  - id: get-dashboard-resource-by-exposure
    intent: Count resources and objects by exposure
    question: How many storage resources do I have, and how exposed are their objects?
  - id: get-dashboard-violations
    intent: List data security dashboard violations
    question: What data security policy violations show on my dashboard?
  phrasing_ops: 7
  slug: palo-alto-networks-data-security-dashboard-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Data Security capabilities on Prisma Cloud enable you to discover and classify data stored in AWS S3 buckets and protect accidental exposure, misuse, or sharing of sensitive data. The data invento
  name: Palo Alto Networks Data Security Inventory API
  phrasing_intents:
  - id: get-data-usage
    intent: Get data scanning usage for the tenant
    question: How much data has been scanned for my tenant so far?
  - id: get-classification-report-v2
    intent: Get a data classification report with snippet masking
    question: Can I see the classification report for a file along with whether its snippets are masked?
  - id: get-classification-report
    intent: Get the original data classification report
    question: What sensitive data classifications were detected in a specific stored object?
  - id: get-inventory-objects
    intent: List data inventory objects by table level
    question: How many public, sensitive or malware-infected objects do I have per cloud service?
  - id: get-inventory-objects-l4
    intent: Page through bucket objects at level 4
    question: How can I quickly page through the individual objects inside a bucket?
  - id: get-inventory-object-details
    intent: Get details of one inventory object
    question: What do we know about a single file in my data inventory?
  - id: get-inventory-objects-by-classification
    intent: Count objects by classification, malware and exposure
    question: How many of my objects are classified sensitive, contain malware, or are publicly exposed?
  - id: get-inventory-aggregate-alerts-by-classification
    intent: Count object alerts by exposure, classification and severity
    question: How many data alerts do I have grouped by exposure and severity?
  phrasing_ops: 14
  slug: palo-alto-networks-data-security-inventory-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Data Security Onboarding API from Palo Alto Networks — 5 operation(s) for data security onboarding.
  name: Palo Alto Networks Data Security Onboarding API
  phrasing_intents:
  - id: get-account-config-by-storage-uuid
    intent: Get data security account config by storage UUID
    question: Which data security account config belongs to a given storage UUID?
  - id: get-account-config-by-pcds-account-id
    intent: Get data security account config by account ID
    question: What is the onboarding config for a specific PCDS account?
  - id: update-pcds-account-config
    intent: Update a data security account config
    question: Can I change the scan option for a data security onboarded account?
  - id: get-status-pcds-account
    intent: Check a data security account's permissions
    question: Is my data security account missing any cloud permissions?
  - id: generate-network-acl-script-by-account-id
    intent: Generate an Azure network ACL script
    question: How can I fix network connectivity issues for data security scanning in Azure?
  - id: get-azure-terraform-script
    intent: Generate an Azure onboarding Terraform script
    question: Where do I get a Terraform script with all permissions needed to onboard Azure for data security?
  phrasing_ops: 6
  slug: palo-alto-networks-data-security-onboarding-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Prisma Cloud Data Security enables you to discover and classify data stored in AWS S3 buckets and protect accidental exposure, misuse, or sharing of sensitive data. You can use the data security setti
  name: Palo Alto Networks Data Security Settings API
  phrasing_intents:
  - id: get-resource-inventory
    intent: List S3 buckets in the data resource inventory
    question: Which of my onboarded AWS S3 buckets are in the Prisma Cloud data resource inventory?
  - id: update-resource-config
    intent: Turn data scanning on or off for resources
    question: Can I enable sensitive data scanning for a specific set of S3 resources through the v2 resource config?
  - id: get-all-data-patterns
    intent: Filter my data patterns by mode and editor
    question: Can I list only the custom data patterns someone updated in a given time range?
  - id: add-data-pattern
    intent: Create a data pattern in my tenant
    question: How do I define a new regex-based data pattern for sensitive data detection?
  - id: clone-data-pattern
    intent: Clone a data pattern in my tenant
    question: Can I copy an existing predefined data pattern so I can tweak its confidence levels?
  - id: get-data-pattern-details
    intent: Get one data pattern's details
    question: What regexes and detection technique does a particular data pattern use?
  - id: get-data-pattern-name
    intent: List data pattern names and confidence levels
    question: Which data pattern names exist in my tenant and what confidence levels does each support?
  - id: update-data-pattern
    intent: Update a data pattern in my tenant
    question: Can I change the regexes on a custom data pattern I already created?
  phrasing_ops: 39
  slug: palo-alto-networks-data-security-settings-api
- baseURL: https://api.dig.security
  baseurl_source: declared
  description: The Data Type Findings API from Palo Alto Networks — 1 operation(s) for data type findings.
  name: Palo Alto Networks Data Type Findings API
  phrasing_intents:
  - id: get-data-type-findings
    intent: List sensitive data type findings
    question: Which sensitive data types have been found in my cloud data stores?
  phrasing_ops: 1
  slug: palo-alto-networks-data-type-findings-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: DataFiltering
  name: Palo Alto Networks Data Filtering API
  phrasing_intents:
  - id: ListDataFilteringProfiles
    intent: List data filtering profiles
    question: What data filtering profiles do I have configured for data loss prevention?
  - id: CreateDataFilteringProfiles
    intent: Create a data filtering profile
    question: How do I create a new data filtering profile with its own rules?
  - id: GetDataFilteringProfilesByID
    intent: Get a data filtering profile by ID
    question: What rules are inside a specific data filtering profile?
  - id: UpdateDataFilteringProfilesByID
    intent: Update a data filtering profile
    question: How do I change the rules on a data filtering profile that already exists?
  - id: DeleteDataFilteringProfilesByID
    intent: Delete a data filtering profile
    question: How do I get rid of a data filtering profile I no longer use?
  phrasing_ops: 5
  slug: palo-alto-networks-datafiltering-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: DataObjects
  name: Palo Alto Networks Data Objects API
  phrasing_intents:
  - id: ListDataObjects
    intent: List data objects
    question: Which data loss prevention data objects are defined?
  - id: CreateDataObjects
    intent: Create a data object
    question: How do I define a new data object for data pattern matching?
  - id: GetDataObjectsByID
    intent: Get a data object
    question: What patterns does a specific data object contain?
  - id: UpdateDataObjectsByID
    intent: Update a data object
    question: How do I change the pattern type of an existing data object?
  - id: DeleteDataObjectsByID
    intent: Delete a data object
    question: How do I remove a data object I no longer need?
  phrasing_ops: 5
  slug: palo-alto-networks-dataobjects-api
- baseURL: https://pa-us.api.prismaaccess.com
  baseurl_source: declared
  description: The DataResource API from Palo Alto Networks — 2 operation(s) for dataresource.
  name: Palo Alto Networks Data Resource API
  phrasing_intents:
  - id: post-api-sase-v2.0-resource-query-resource_name
    intent: Query a SASE data resource
    question: How do I query monitoring data from my Prisma SASE tenant?
  - id: get-api-sase-v2.0-resource-resource_name
    intent: Describe a SASE data resource's properties
    question: Which properties can I query on a SASE data resource?
  phrasing_ops: 2
  slug: palo-alto-networks-dataresource-api
- baseURL: https://pa-us.api.prismaaccess.com
  baseurl_source: declared
  description: The DataResourceCustom API from Palo Alto Networks — 2 operation(s) for dataresourcecustom.
  name: Palo Alto Networks Data Resource Custom API
  phrasing_intents:
  - id: post-api-sase-v2.0-resource-custom-query-feature_name-request_name
    intent: Query custom mobile user resource data
    question: How many mobile users are concurrently connected right now?
  - id: get-api-sase-v2.0-resource-custom-feature_name-request_name
    intent: Describe a custom resource's properties
    question: What properties can I query on the connected mobile users resource?
  phrasing_ops: 2
  slug: palo-alto-networks-dataresourcecustom-api
- baseURL: https://pa-us.api.prismaaccess.com
  baseurl_source: declared
  description: The DataResourceExport API from Palo Alto Networks — 4 operation(s) for dataresourceexport.
  name: Palo Alto Networks Data Resource Export API
  phrasing_intents:
  - id: post-api-sase-v2.0-resource-download
    intent: Download a custom resource export CSV
    question: How do I download the CSV produced by a custom resource export job?
  - id: post-api-sase-v2.0-resource-download-status
    intent: Check a resource export job status
    question: Is my custom resource export job finished yet?
  - id: post-api-sase-v2.0-resource-export-schedule-query-resource_name
    intent: Export a general resource to CSV
    question: Can I export every property of a resource to a CSV file?
  - id: post-api-sase-v2.0-resourceexport-schedule-custom-query-feature_name-resource_name
    intent: Create a custom resource export job
    question: Can I export custom data for a specific feature and resource combination?
  phrasing_ops: 4
  slug: palo-alto-networks-dataresourceexport-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: Decryption Exclusions
  name: Palo Alto Networks Decryption Exclusions API
  phrasing_intents:
  - id: ListDecryptionExclusions
    intent: List decryption exclusions
    question: Which sites are excluded from SSL decryption in a folder?
  - id: CreateDecryptionExclusions
    intent: Create a decryption exclusion
    question: How do I exclude a site from SSL decryption?
  - id: GetDecryptionExclusionsByID
    intent: Get a decryption exclusion
    question: What does a particular decryption exclusion cover?
  - id: UpdateDecryptionExclusionsByID
    intent: Update a decryption exclusion
    question: Can I change the name or description of an existing decryption exclusion?
  - id: DeleteDecryptionExclusionsByID
    intent: Delete a decryption exclusion
    question: How do I start decrypting a site again by removing its exclusion?
  - id: get-sse-config-v1-decryption-exclusions
    intent: List decryption exclusions
    question: Which sites are excluded from SSL decryption in my folder?
  - id: post-sse-config-v1-decryption-exclusions
    intent: Create a decryption exclusion
    question: How do I add a decryption exclusion to a specific Prisma Access folder through the SSE config API?
  - id: delete-sse-config-v1-decryption-exclusions-id
    intent: Delete a decryption exclusion
    question: How do I delete a decryption exclusion through the SSE config v1 endpoint?
  phrasing_ops: 10
  slug: palo-alto-networks-decryption-exclusions-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: Decryption Profiles
  name: Palo Alto Networks Decryption Profiles API
  phrasing_intents:
  - id: ListDecryptionProfiles
    intent: List decryption profiles
    question: Which SSL decryption profiles are defined in a folder, snippet or device?
  - id: CreateDecryptionProfiles
    intent: Create a decryption profile
    question: How do I create a decryption profile with SSL forward proxy settings?
  - id: GetDecryptionProfilesByID
    intent: Get a decryption profile
    question: What SSL settings does one decryption profile have?
  - id: UpdateDecryptionProfilesByID
    intent: Update a decryption profile
    question: How do I change the inbound inspection settings on an existing decryption profile?
  - id: DeleteDecryptionProfilesByID
    intent: Delete a decryption profile
    question: Can I delete a decryption profile that is no longer used?
  - id: get-sse-config-v1-decryption-profiles
    intent: List decryption profiles
    question: Which decryption profiles are configured in a folder?
  - id: post-sse-config-v1-decryption-profiles
    intent: Create a decryption profile
    question: How do I set up a decryption profile for SSL forward proxy?
  - id: delete-sse-config-v1-decryption-profiles-id
    intent: Delete a decryption profile
    question: How do I remove a decryption profile?
  phrasing_ops: 10
  slug: palo-alto-networks-decryption-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: Decryption Rules
  name: Palo Alto Networks Decryption Rules API
  phrasing_intents:
  - id: ListDecryptionRules
    intent: List decryption rules
    question: Which SSL decryption rules are in my pre or post rulebase?
  - id: CreateDecryptionRules
    intent: Create a decryption rule
    question: How do I add a rule to decrypt traffic between two zones?
  - id: GetDecryptionRulesByID
    intent: Get a decryption rule
    question: What does a specific decryption rule match and do?
  - id: UpdateDecryptionRulesByID
    intent: Update a decryption rule
    question: Can I change the action or zones on an existing decryption rule?
  - id: DeleteDecryptionRulesByID
    intent: Delete a decryption rule
    question: How do I remove a decryption rule?
  - id: MoveDecryptionRulesByID
    intent: Reorder a decryption rule
    question: Can I move a decryption rule above or below another rule?
  - id: get-sse-config-v1-decryption-rules
    intent: List decryption rules
    question: Which SSL decryption rules are configured in a Prisma Access folder?
  - id: post-sse-config-v1-decryption-rules
    intent: Create a decryption rule
    question: How do I add a rule that decrypts traffic for certain URL categories?
  phrasing_ops: 12
  slug: palo-alto-networks-decryption-rules-api
- baseURL: https://api.sase.paloaltonetworks.com/aisec
  baseurl_source: declared
  description: Operations related to deployment profile management
  name: Palo Alto Networks Deployment Profiles API
  phrasing_intents:
  - id: GetDeploymentProfilesByTsgId
    intent: List deployment profiles
    question: Which deployment profiles belong to my tenant service group?
  phrasing_ops: 1
  slug: palo-alto-networks-deployment-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
  baseurl_source: declared
  description: Destinations
  name: Palo Alto Networks Destinations API
  phrasing_intents:
  - id: ListGlobalProtectDestinations
    intent: List GlobalProtect forwarding destinations
    question: Which GlobalProtect forwarding profile destinations are defined?
  - id: CreateGlobalProtectDestination
    intent: Create a GlobalProtect forwarding destination
    question: How do I add a destination to a GlobalProtect forwarding profile by FQDN?
  - id: GetGlobalProtectDestinationByID
    intent: Get a GlobalProtect forwarding destination
    question: Which FQDNs and IPs does a given GlobalProtect destination cover?
  - id: UpdateGlobalProtectDestinationByID
    intent: Update a GlobalProtect forwarding destination
    question: How do I change the FQDN or IP addresses on an existing GlobalProtect destination?
  - id: DeleteGlobalProtectDestination
    intent: Delete a GlobalProtect forwarding destination
    question: How do I remove a GlobalProtect forwarding destination?
  phrasing_ops: 5
  slug: palo-alto-networks-destinations-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Development Pipeline API from Palo Alto Networks — 2 operation(s) for development pipeline.
  name: Palo Alto Networks Development Pipeline API
  phrasing_intents:
  - id: getCodeReviewData
    intent: Get code review run data
    question: How many issues did recent code reviews find in my repositories, by severity?
  - id: getProjectsData
    intent: Get integrated VCS repository metadata
    question: Which of my integrated repositories have the most weekly commits or failed PRs?
  phrasing_ops: 2
  slug: palo-alto-networks-development-pipeline-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: Device Context Segment Association
  name: Palo Alto Networks Device Context Segment Association API
  phrasing_intents:
  - id: ListDeviceContextSegmentAssociation
    intent: List device context segment associations
    question: Which device context segment associations are configured?
  - id: CreateDeviceContextSegmentAssociation
    intent: Create a device context segment association
    question: How do I add a new device context segment association?
  - id: DeleteDeviceContextSegmentAssociationByName
    intent: Delete segment associations by name
    question: Can I delete device context segment associations using their name instead of an ID?
  - id: GetDeviceContextSegmentAssociationByID
    intent: Get a device context segment association
    question: What does a specific device context segment association look like?
  - id: UpdateDeviceContextSegmentAssociationByID
    intent: Update a device context segment association
    question: How do I rename an existing device context segment association?
  - id: DeleteDeviceContextSegmentAssociationByID
    intent: Delete a segment association by ID
    question: How do I delete one specific segment association by its UUID?
  phrasing_ops: 6
  slug: palo-alto-networks-device-context-segment-association-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: Device Context Segments
  name: Palo Alto Networks Device Context Segments API
  phrasing_intents:
  - id: ListDeviceContextSegments
    intent: List device context segments
    question: Which device context segments are configured?
  - id: CreateDeviceContextSegment
    intent: Create a device context segment
    question: How do I add a new device context segment?
  - id: DeleteDeviceContextSegmentsByName
    intent: Delete device context segments by name
    question: Can I delete several device context segments by name at once?
  - id: GetDeviceContextSegmentByID
    intent: Get a device context segment
    question: What's configured in one device context segment?
  - id: UpdateDeviceContextSegmentByID
    intent: Update a device context segment
    question: Can I rename an existing device context segment?
  - id: DeleteDeviceContextSegmentByID
    intent: Delete a device context segment by ID
    question: How do I remove a single device context segment by its UUID?
  phrasing_ops: 6
  slug: palo-alto-networks-device-context-segments-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The Device Groups API from Palo Alto Networks — 2 operation(s) for device groups.
  name: Palo Alto Networks Device Groups API
  phrasing_intents:
  - id: GetSeb-apiV1Device-groups
    intent: List device groups
    question: Which device groups exist for my enterprise browser?
  - id: PostSeb-apiV1Device-groups
    intent: Create a device group
    question: How do I create a new device group for a platform?
  - id: GetSeb-apiV1Device-groupsbydevice-group-id
    intent: Get a device group
    question: What settings does a specific device group have?
  - id: PutSeb-apiV1Device-groupsbydevice-group-id
    intent: Replace a device group
    question: If I replace a device group, what happens to attributes I leave out?
  - id: PatchSeb-apiV1Device-groupsbydevice-group-id
    intent: Partially update a device group
    question: Can I add or remove device serial numbers from a group without replacing it?
  - id: DeleteSeb-apiV1Device-groupsbydevice-group-id
    intent: Delete a device group
    question: Can I delete a device group I no longer use?
  phrasing_ops: 6
  slug: palo-alto-networks-device-groups-api
- baseURL: https://api.strata.paloaltonetworks.com/operations/v1
  baseurl_source: declared
  description: Operations for device management and troubleshooting
  name: Palo Alto Networks Device Operations API
  phrasing_intents:
  - id: getLocalConfigVersions
    intent: List local config versions for a device
    question: How can I see the history of local configurations pushed to a firewall?
  - id: downloadLocalConfig
    intent: Download a device’s local config file
    question: Can I download the actual XML config file that was pushed to a device?
  - id: requestRouteTable
    intent: Start a job to fetch device route tables
    question: Can I pull the route table from several firewalls at once?
  - id: requestDnsProxy
    intent: Start a job to fetch the DNS proxy table
    question: How do I see the DNS proxy table on my firewalls?
  - id: requestFIBTable
    intent: Start a job to fetch the FIB table
    question: Can I retrieve the forwarding information base from a firewall?
  - id: requestLoggingServiceForwardingStatus
    intent: Check log forwarding status on devices
    question: Are my firewalls successfully forwarding logs to the logging service?
  - id: requestDeviceInterfaces
    intent: Start a job to fetch device interfaces
    question: How can I list the network interfaces on a firewall remotely?
  - id: requestDeviceRules
    intent: Start a job to fetch rules from devices
    question: Can I retrieve the rules actually running on a device?
  phrasing_ops: 9
  slug: palo-alto-networks-device-operations-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: Device Redistribution Collector Settings
  name: Palo Alto Networks Device Redistribution Collector Settings API
  phrasing_intents:
  - id: ListDeviceRedistributionCollectorSettings
    intent: List redistribution collector settings
    question: Which devices have User-ID redistribution collector settings configured?
  - id: CreateDeviceRedistributionCollectorSettings
    intent: Create redistribution collector settings
    question: How do I configure a device as a redistribution collector?
  - id: GetDeviceRedistributionCollectorSettingsByID
    intent: Get redistribution collector settings
    question: What are the current settings for one redistribution collector?
  - id: UpdateDeviceRedistributionCollectorSettingsByID
    intent: Update redistribution collector settings
    question: How do I change an existing redistribution collector's settings?
  - id: DeleteDeviceRedistributionCollectorSettingsByID
    intent: Delete redistribution collector settings
    question: How do I delete a redistribution collector configuration?
  phrasing_ops: 5
  slug: palo-alto-networks-device-redistribution-collector-settings-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: DHCP Interfaces
  name: Palo Alto Networks DHCP Interfaces API
  phrasing_intents:
  - id: ListDHCPInterfaces
    intent: List DHCP interfaces
    question: Which DHCP interfaces are configured on a device or in a folder?
  - id: CreateDHCPInterfaces
    intent: Create a DHCP interface
    question: How do I enable DHCP on a new interface?
  - id: GetDHCPInterfacesByID
    intent: Get a DHCP interface
    question: Can I fetch one DHCP interface by its UUID?
  - id: UpdateDHCPInterfacesByID
    intent: Update a DHCP interface
    question: Can I change which interface an existing DHCP interface entry points to?
  - id: DeleteDHCPInterfacesByID
    intent: Delete a DHCP interface
    question: How do I stop an interface from serving DHCP by removing its entry?
  phrasing_ops: 5
  slug: palo-alto-networks-dhcp-interfaces-api
- baseURL: https://api.dlp.paloaltonetworks.com
  baseurl_source: declared
  description: The Dictionaries API from Palo Alto Networks — 2 operation(s) for dictionaries.
  name: Palo Alto Networks Dictionaries API
  phrasing_intents:
  - id: get-v2-api-dictionaries
    intent: List data dictionaries
    question: What dictionaries have been uploaded for my tenant?
  - id: post-v2-api-dictionaries
    intent: Upload a new dictionary file
    question: How do I create a dictionary by uploading a word list file?
  - id: delete-v2-api-dictionaries-resourceid
    intent: Delete a dictionary
    question: How do I delete a dictionary I no longer use?
  - id: get-v2-api-dictionaries-resourceid
    intent: Get a dictionary
    question: How do I look up a single dictionary by its ID?
  - id: patch-v2-api-dictionaries-resourceid
    intent: Edit a dictionary's metadata
    question: Can I make a dictionary case sensitive without re-uploading the file?
  - id: put-v2-api-dictionaries-resourceid
    intent: Replace a dictionary with a new file
    question: Can I replace a dictionary's contents by uploading a fresh file?
  phrasing_ops: 6
  slug: palo-alto-networks-dictionaries-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Discovered-Application API from Palo Alto Networks — 2 operation(s) for discovered-application.
  name: Palo Alto Networks Discovered Application API
  phrasing_intents:
  - id: list.discovered_application.v2
    intent: List discovered SaaS applications
    question: Which applications have been discovered in use across my tenant?
  - id: list.discovered_application.filters.v2
    intent: Get filter values for discovered applications
    question: What values can I filter discovered applications by for a given field?
  phrasing_ops: 2
  slug: palo-alto-networks-discovered-application-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Discovery and Exposure Management(CDEM) APIs help you in identifying unmanaged or exposed assets that must be secured. You can use the APIs in this section to fetch the details that are displayed in t
  name: Palo Alto Networks Discovery and Exposure Management API
  phrasing_intents:
  - id: onboard-Cloud-Accounts
    intent: Onboard unmanaged cloud accounts to CSPM
    question: How do I bring cloud accounts found by exposure discovery under CSPM protection?
  - id: asset-inventory-for-l3
    intent: List discovered assets with filters
    question: Which internet-exposed assets were discovered in my AWS and Azure clouds?
  - id: get-asset-findings
    intent: Get security findings for an asset
    question: What security findings and vulnerabilities were discovered on a specific asset?
  - id: get-finding-filters
    intent: Get the filter values for an asset's findings
    question: Which finding types and severities can I filter on for a particular asset?
  - id: asset-snooze
    intent: Snooze notifications for unmanaged assets
    question: How do I silence alerts from unmanaged internet-exposed assets for a while?
  - id: asset-unsnooze
    intent: Unsnooze snoozed unmanaged assets
    question: How do I turn notifications back on for assets I previously snoozed?
  - id: send-asset-detail-email-from-sidecar
    intent: Email asset details to colleagues
    question: Can I email the details of an exposed asset to my team?
  - id: asset-download
    intent: Download a filtered list of unmanaged assets
    question: Can I export the list of unmanaged assets to a file?
  phrasing_ops: 26
  slug: palo-alto-networks-discovery-and-exposure-management-api
- baseURL: https://api.dlp.paloaltonetworks.com
  baseurl_source: declared
  description: DLP API
  name: Palo Alto Networks DLP API
  phrasing_intents:
  - id: getReport
    intent: Get a DLP scan report
    question: Can I retrieve an Enterprise DLP report by its ID?
  - id: updateIncidentAssignee
    intent: Assign an Enterprise DLP incident
    question: How do I assign a DLP incident to an analyst?
  - id: updateIncidentNotes
    intent: Update notes on a DLP incident
    question: Can I write investigation notes on an Enterprise DLP incident?
  - id: deleteIncidentNotes
    intent: Remove notes from a DLP incident
    question: Is there a way to clear the notes on a DLP incident?
  - id: updateIncidentResolutionStatus
    intent: Set a DLP incident's resolution
    question: How do I mark an Enterprise DLP incident as resolved?
  - id: getIncidentAssignees
    intent: List DLP incident assignees
    question: Who can DLP incidents be assigned to?
  - id: createOrUpdateIncidentAssignees
    intent: Add or update a DLP incident assignee
    question: How do I add a new person who can be assigned DLP incidents?
  - id: getIncidentAssigneesById
    intent: Get a DLP incident assignee
    question: Where can I look up one DLP assignee's details?
  phrasing_ops: 10
  slug: palo-alto-networks-dlp-api-api
- baseURL: https://api.dlp.paloaltonetworks.com
  baseurl_source: declared
  description: Beta DLP APIs
  name: Palo Alto Networks DLP API (Beta) API
  phrasing_intents:
  - id: getIncidentInventory
    intent: Query DLP incidents for a time range
    question: How do I start retrieving DLP incidents for a particular time range?
  - id: getIncidentInventoryTableResults
    intent: Page through DLP incidents with a token
    question: How do I fetch the next page of DLP incidents after my initial query?
  - id: exportIncidentsAndGetUrl
    intent: Export DLP incidents to a CSV download link
    question: Can I download DLP incidents as a CSV file?
  - id: updateIncidents
    intent: Update assignee, status or priority of DLP incidents
    question: How do I assign or resolve several DLP incidents at once?
  - id: getIncidentDetails
    intent: Get details of a DLP incident
    question: How do I see the full details of one DLP incident?
  phrasing_ops: 5
  slug: palo-alto-networks-dlp-api-beta-api
- baseURL: https://api.sase.paloaltonetworks.com/aisec
  baseurl_source: declared
  description: Operations related to DLP profile management
  name: Palo Alto Networks DLP Profiles API
  phrasing_intents:
  - id: GetAllDlpProfilesByTsgId
    intent: List all DLP profiles
    question: Which data loss prevention profiles exist for my tenant service group?
  phrasing_ops: 1
  slug: palo-alto-networks-dlp-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: DNS Proxies
  name: Palo Alto Networks DNS Proxies API
  phrasing_intents:
  - id: ListDNSProxies
    intent: List DNS proxies
    question: Which DNS proxies are configured in a given folder?
  - id: CreateDNSProxies
    intent: Create a DNS proxy
    question: How do I set up a DNS proxy on my firewall interfaces?
  - id: GetDNSProxiesByID
    intent: Get a DNS proxy
    question: What domain server rules does one DNS proxy use?
  - id: UpdateDNSProxiesByID
    intent: Update a DNS proxy
    question: How do I change the domain server rules on an existing DNS proxy?
  - id: DeleteDNSProxiesByID
    intent: Delete a DNS proxy
    question: Can I remove a DNS proxy I no longer use?
  phrasing_ops: 5
  slug: palo-alto-networks-dns-proxies-api
- baseURL: https://api.dns.service.paloaltonetworks.com
  baseurl_source: declared
  description: DNS Security API
  name: Palo Alto Networks DNS Security API
  phrasing_intents:
  - id: PublicApi_V1DomainChangeRequest
    intent: Request a domain category change
    question: How do I ask for a domain to be recategorized in DNS Security?
  - id: PublicApi_V1DomainInfo
    intent: Look up WHOIS, passive DNS and category for domains
    question: What's the WHOIS, passive DNS and DGA score for a suspicious domain?
  phrasing_ops: 2
  slug: palo-alto-networks-dns-security-api-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: DNS Security Profiles
  name: Palo Alto Networks DNS Security Profiles API
  phrasing_intents:
  - id: ListDNSSecurityProfiles
    intent: List DNS security profiles
    question: Which DNS security profiles are configured in my Strata Cloud Manager tenant?
  - id: CreateDNSSecurityProfiles
    intent: Create a DNS security profile
    question: How do I create a new DNS security profile?
  - id: GetDNSSecurityProfilesByID
    intent: Get a DNS security profile
    question: What settings does a specific DNS security profile contain?
  - id: UpdateDNSSecurityProfilesByID
    intent: Update a DNS security profile
    question: How do I change botnet domain handling in an existing DNS security profile?
  - id: DeleteDNSSecurityProfilesByID
    intent: Delete a DNS security profile
    question: Which call removes a DNS security profile I no longer use?
  - id: get-sse-config-v1-dns-security-profiles
    intent: List DNS security profiles
    question: What DNS security profiles are configured in a folder?
  - id: post-sse-config-v1-dns-security-profiles
    intent: Create a DNS security profile
    question: How do I create a DNS security profile that handles botnet domains?
  - id: delete-sse-config-v1-dns-security-profiles-id
    intent: Delete a DNS security profile
    question: Can I delete a DNS security profile?
  phrasing_ops: 10
  slug: palo-alto-networks-dns-security-profiles-api
- baseURL: https://api.dlp.paloaltonetworks.com
  baseurl_source: declared
  description: The Document Types API from Palo Alto Networks — 2 operation(s) for document types.
  name: Palo Alto Networks Document Types API
  phrasing_intents:
  - id: get-v2-api-document-types
    intent: List DLP document types
    question: Which custom document types has my tenant trained for data loss prevention?
  - id: post-v2-api-document-types
    intent: Create a document type from training files
    question: How do I teach DLP a new document type by uploading example files?
  - id: delete-v2-api-document-types-resourceid
    intent: Delete a document type
    question: How do I remove a document type I no longer need?
  - id: get-v2-api-document-types-resourceid
    intent: Get a document type
    question: What category and detection technique does a particular document type use?
  - id: patch-v2-api-document-types-resourceid
    intent: Partially update a document type
    question: Can I change just the description of a document type without replacing it?
  - id: put-v2-api-document-types-resourceid
    intent: Replace a document type entirely
    question: Can I fully overwrite a document type's definition in one call?
  phrasing_ops: 6
  slug: palo-alto-networks-document-types-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: DoS Protection Profiles
  name: Palo Alto Networks DoS Protection Profiles API
  phrasing_intents:
  - id: ListDoSProtectionProfiles
    intent: List DoS protection profiles
    question: Which DoS protection profiles are configured in a folder?
  - id: CreateDoSProtectionProfiles
    intent: Create a DoS protection profile
    question: How do I create a DoS protection profile with flood thresholds?
  - id: GetDoSProtectionProfilesByID
    intent: Get a DoS protection profile
    question: How do I view one DoS protection profile's flood and resource settings?
  - id: UpdateDoSProtectionProfilesByID
    intent: Update a DoS protection profile
    question: Can I change the flood protection thresholds on an existing DoS profile?
  - id: DeleteDoSProtectionProfilesByID
    intent: Delete a DoS protection profile
    question: How do I delete a DoS protection profile?
  phrasing_ops: 5
  slug: palo-alto-networks-dos-protection-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: DoS Protection Rules
  name: Palo Alto Networks DoS Protection Rules API
  phrasing_intents:
  - id: ListDoSProtectionRules
    intent: List DoS protection rules
    question: Which DoS protection rules are in a folder?
  - id: CreateDoSProtectionRules
    intent: Create a DoS protection rule
    question: How do I protect a service from floods with a new DoS protection rule?
  - id: GetDoSProtectionRulesByID
    intent: Get a DoS protection rule
    question: What zones and protection profile does a given DoS rule use?
  - id: UpdateDoSProtectionRulesByID
    intent: Update a DoS protection rule
    question: Can I disable an existing DoS protection rule without deleting it?
  - id: DeleteDoSProtectionRulesByID
    intent: Delete a DoS protection rule
    question: How do I remove a DoS protection rule?
  phrasing_ops: 5
  slug: palo-alto-networks-dos-protection-rules-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: Dynamic User Groups
  name: Palo Alto Networks Dynamic User Groups API
  phrasing_intents:
  - id: ListDynamicUserGroups
    intent: List dynamic user groups
    question: Which dynamic user groups are defined in my configuration?
  - id: CreateDynamicUserGroups
    intent: Create a dynamic user group
    question: How do I create a user group whose membership is driven by tags?
  - id: GetDynamicUserGroupsByID
    intent: Get a dynamic user group
    question: What filter does a particular dynamic user group use?
  - id: UpdateDynamicUserGroupsByID
    intent: Update a dynamic user group
    question: How do I change the filter on an existing dynamic user group?
  - id: DeleteDynamicUserGroupsByID
    intent: Delete a dynamic user group
    question: How do I remove a dynamic user group?
  - id: get-sse-config-v1-dynamic-user-groups
    intent: List dynamic user groups in a folder
    question: What dynamic user groups are defined in a Prisma Access folder?
  - id: post-sse-config-v1-dynamic-user-groups
    intent: Create a tag-based dynamic user group
    question: How do I create a user group whose membership follows user tags?
  - id: delete-sse-config-v1-dynamic-user-groups-id
    intent: Delete a dynamic user group
    question: Can I remove a dynamic user group from Prisma Access?
  phrasing_ops: 10
  slug: palo-alto-networks-dynamic-user-groups-api
- baseURL: https://api.strata.paloaltonetworks.com
  baseurl_source: declared
  description: The EDL CA Certificates API from Palo Alto Networks — 4 operation(s) for edl ca certificates.
  name: Palo Alto Networks EDL CA Certificates API
  phrasing_intents:
  - id: ListCACerts
    intent: List EDL CA certificates
    question: Which CA certificates are uploaded for external dynamic lists?
  - id: DeleteCACertByID
    intent: Delete an EDL CA certificate
    question: How do I remove an EDL CA certificate I no longer trust?
  - id: GetCACertByID
    intent: Get EDL CA certificate metadata
    question: How can I see the metadata of one EDL CA certificate?
  - id: DownloadCACertAsFile
    intent: Download an EDL CA certificate as PEM
    question: Can I download an EDL CA certificate as a PEM file?
  - id: UploadCACertFromFile
    intent: Upload an EDL CA certificate
    question: How do I upload a CA certificate for my external dynamic lists?
  phrasing_ops: 5
  slug: palo-alto-networks-edl-ca-certificates-api
- baseURL: https://api.strata.paloaltonetworks.com
  baseurl_source: declared
  description: The EDL Definitions API from Palo Alto Networks — 2 operation(s) for edl definitions.
  name: Palo Alto Networks EDL Definitions API
  phrasing_intents:
  - id: ListEDLDefinitions
    intent: List external dynamic list definitions
    question: Which external dynamic lists is the DNS resolver pulling from?
  - id: CreateEDLDefinition
    intent: Create an external dynamic list definition
    question: How do I add an external dynamic list URL for the DNS resolver to poll?
  - id: DeleteEDLDefinitionByID
    intent: Delete an external dynamic list definition
    question: How do I stop the resolver using an external dynamic list?
  - id: GetEDLDefinitionByID
    intent: Get an external dynamic list definition
    question: What URL and polling interval does a specific EDL use?
  - id: UpdateEDLDefinitionByID
    intent: Update an external dynamic list definition
    question: How do I change the polling frequency of an existing EDL?
  phrasing_ops: 5
  slug: palo-alto-networks-edl-definitions-api
- baseURL: https://api.dlp.paloaltonetworks.com
  baseurl_source: declared
  description: The EDM Datasets API from Palo Alto Networks — 2 operation(s) for edm datasets.
  name: Palo Alto Networks EDM Datasets API
  phrasing_intents:
  - id: get-v2-api-edm-datasets
    intent: List EDM datasets
    question: Which exact data matching datasets are uploaded for my tenant?
  - id: delete-v2-api-edm-datasets-resourceid
    intent: Delete an EDM dataset
    question: How do I remove an EDM dataset I no longer need?
  - id: get-v2-api-edm-datasets-resourceid
    intent: Get an EDM dataset
    question: What are the details of one exact data matching dataset?
  phrasing_ops: 3
  slug: palo-alto-networks-edm-datasets-api
- baseURL: https://api.us-west1.email.dlp.paloaltonetworks.com
  baseurl_source: declared
  description: The Email DLP API API from Palo Alto Networks — 3 operation(s) for email dlp api.
  name: Palo Alto Networks Email DLP API
  phrasing_intents:
  - id: get-incident-api-v1-incidents
    intent: List Email DLP incidents
    question: Which emails triggered data loss prevention incidents this week?
  - id: patch-incident-api-v1-incidents-incidentid-status
    intent: Update an Email DLP incident's status
    question: How do I mark an Email DLP incident as resolved?
  - id: get-report-api-v1-reports-reportid
    intent: Get a DLP report
    question: What sensitive data did a DLP report detect?
  phrasing_ops: 3
  slug: palo-alto-networks-email-dlp-api-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The EmailProfiles API from Palo Alto Networks — 2 operation(s) for emailprofiles.
  name: Palo Alto Networks Email Profiles API
  phrasing_intents:
  - id: get-logging-service-logforwarding-v1-email-profiles
    intent: List log forwarding email profiles
    question: Which email profiles are set up to forward logs, and what are their profile IDs?
  - id: post-logging-service-logforwarding-v1-email-profiles
    intent: Create a log forwarding email profile
    question: How do I have certain logs emailed to an address automatically?
  - id: delete-logging-service-logforwarding-v1-email-profiles-profileid
    intent: Delete an email profile
    question: How do I stop logs being emailed by deleting an email profile?
  - id: get-logging-service-logforwarding-v1-email-profiles-profileid
    intent: Get an email profile and its etag
    question: How do I get the etag I need before editing an email profile?
  - id: put-logging-service-logforwarding-v1-email-profiles-profileid
    intent: Update an email profile
    question: How do I change the recipient on an existing log email profile?
  phrasing_ops: 5
  slug: palo-alto-networks-emailprofiles-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Enable 5 GAPI API from Palo Alto Networks — 2 operation(s) for enable 5 gapi.
  name: Palo Alto Networks Enable 5 GAPI API
  phrasing_intents:
  - id: GetMtManage5gIpcidrBy_compute_region
    intent: Show a region's 5G CIDR blocks
    question: Which IPv4 and IPv6 ranges are assigned to a compute region?
  - id: PostMtManage5gSetup
    intent: Activate 5G connectivity in a region
    question: How do I turn on 5G connectivity for a compute region?
  phrasing_ops: 2
  slug: palo-alto-networks-enable-5-gapi-api
- baseURL: https://api.dlp.paloaltonetworks.com
  baseurl_source: declared
  description: The Endpoint Policies API from Palo Alto Networks — 2 operation(s) for endpoint policies.
  name: Palo Alto Networks Endpoint Policies API
  phrasing_intents:
  - id: get-v2-api-endpoint-policies
    intent: List endpoint policies
    question: What endpoint policies does my tenant have?
  - id: post-v2-api-endpoint-policies
    intent: Create an endpoint policy
    question: How do I create a new endpoint policy with a severity and a response action?
  - id: delete-v2-api-endpoint-policies-resourceid
    intent: Delete an endpoint policy
    question: Can I delete an endpoint policy I no longer need?
  - id: get-v2-api-endpoint-policies-resourceid
    intent: Get an endpoint policy
    question: Where can I see a single endpoint policy's configuration?
  - id: patch-v2-api-endpoint-policies-resourceid
    intent: Partially update an endpoint policy
    question: Can I change just one field of an endpoint policy with a merge patch?
  - id: put-v2-api-endpoint-policies-resourceid
    intent: Replace an endpoint policy in full
    question: How do I overwrite an entire endpoint policy with a new definition?
  phrasing_ops: 6
  slug: palo-alto-networks-endpoint-policies-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Retrieve the count of active users, providing insights into user activity.
  name: Palo Alto Networks Enterprise Browser Users API
  phrasing_intents:
  - id: post-insights-v3.0-resource-query-users-eb-active_user_count
    intent: Count active Enterprise Browser users
    question: How many people are actively using Prisma Access Browser?
  - id: post-insights-v3.0-resource-query-users-eb-user_count_histogram
    intent: Get an Enterprise Browser user histogram
    question: Can I see how Enterprise Browser usage is distributed over time?
  - id: post-insights-v3.0-resource-query-users-eb-user_list
    intent: List Enterprise Browser users
    question: Which users are on the Enterprise Browser?
  phrasing_ops: 3
  slug: palo-alto-networks-enterprise-browser-users-api-api
- baseURL: https://api.sase.paloaltonetworks.com/ai-red-teaming/data-plane
  baseurl_source: declared
  description: Operations for retrieving and managing error logs.
  name: Palo Alto Networks Error Logs API
  phrasing_intents:
  - id: list_error_logs_for_job_v1_error_log_job__job_id__get
    intent: List error logs for a scan job
    question: Why did my red teaming scan job fail?
  - id: list_error_logs_for_target_profile_v1_error_log_target_profile__target_id__get
    intent: List profiling errors for a target
    question: What went wrong in the latest profiling run for a target?
  phrasing_ops: 2
  slug: palo-alto-networks-errorlogs-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Ethernet Interfaces
  name: Palo Alto Networks Ethernet Interfaces API
  phrasing_intents:
  - id: ListEthernetInterfaces
    intent: List ethernet interfaces
    question: Which ethernet interfaces are configured on a firewall device?
  - id: CreateEthernetInterfaces
    intent: Create an ethernet interface
    question: How do I configure a new ethernet interface?
  - id: GetEthernetInterfacesByID
    intent: Get an ethernet interface
    question: What is the link state and PoE setting of one ethernet interface?
  - id: UpdateEthernetInterfacesByID
    intent: Update an ethernet interface
    question: How do I bring an existing ethernet interface link down administratively?
  - id: DeleteEthernetInterfacesByID
    intent: Delete an ethernet interface
    question: How do I remove an ethernet interface configuration?
  phrasing_ops: 5
  slug: palo-alto-networks-ethernet-interfaces-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Event Logs.
  name: Palo Alto Networks Event Logs API
  phrasing_intents:
  - id: activitylogs_getByExpression
    intent: Search activity logs with a total count
    question: How many activity log entries match my filter, and what are they?
  - id: activitylogs_getAllByExpression
    intent: Export filtered activity logs to JSON or CSV
    question: Can I export filtered event logs as a CSV file?
  - id: activitylogtypes_get
    intent: List activity types used in event logging
    question: What kinds of activities are recorded in event logs, like failed logins?
  phrasing_ops: 3
  slug: palo-alto-networks-event-logs-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: External Dynamic Lists
  name: Palo Alto Networks External Dynamic Lists API
  phrasing_intents:
  - id: ListExternalDynamicLists
    intent: List external dynamic lists
    question: Which external dynamic lists feed my firewall policies?
  - id: CreateExternalDynamicLists
    intent: Create an external dynamic list
    question: How do I add a new external dynamic list of IPs or URLs?
  - id: GetExternalDynamicListsByID
    intent: Get an external dynamic list
    question: What source and type does a specific external dynamic list use?
  - id: UpdateExternalDynamicListsByID
    intent: Update an external dynamic list
    question: Can I change the type or source of an existing external dynamic list?
  - id: DeleteExternalDynamicListsByID
    intent: Delete an external dynamic list
    question: Can I remove an external dynamic list that no rule uses?
  - id: get-sse-config-v1-external-dynamic-lists
    intent: List external dynamic lists
    question: Which external dynamic lists are configured in a Prisma Access folder?
  - id: post-sse-config-v1-external-dynamic-lists
    intent: Create an external dynamic list
    question: How do I add an external dynamic list of IPs or domains for use in security policy?
  - id: delete-sse-config-v1-external-dynamic-lists-id
    intent: Delete an external dynamic list
    question: Can I delete an external dynamic list that policy no longer references?
  phrasing_ops: 10
  slug: palo-alto-networks-external-dynamic-lists-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/feeds/feeds.md''}'
  name: Palo Alto Networks Feeds API
  phrasing_intents:
  - id: get-feeds-custom-custom-vulnerabilities
    intent: Get custom vulnerability feed (v34.03)
    question: Which custom vulnerability rules are defined in the older v34.03 Prisma Cloud Compute feed endpoint?
  - id: put-feeds-custom-custom-vulnerabilities
    intent: Replace custom vulnerability rules (v34.03)
    question: How do I push custom vulnerability rules through the v34.03 feeds API?
  - id: get-feeds-custom-malware
    intent: Get custom malware feed (v34.03)
    question: Which custom malware signatures are in my feed via the older v34.03 API?
  - id: put-feeds-custom-malware
    intent: Replace custom malware signatures (v34.03)
    question: Can I upload custom malware signatures through the v34.03 feeds API?
  - id: getApiV3404FeedsCustomCustomVulnerabilities
    intent: Get custom vulnerability feed (v34.04)
    question: What custom vulnerability rules does my Prisma Cloud Compute console hold on the current v34.04 API?
  - id: putApiV3404FeedsCustomCustomVulnerabilities
    intent: Replace custom vulnerability rules (v34.04)
    question: What's the way to update my custom vulnerability rules on the v34.04 API?
  - id: getApiV3404FeedsCustomMalware
    intent: Get custom malware feed (v34.04)
    question: What custom malware signatures are loaded on the current v34.04 API?
  - id: putApiV3404FeedsCustomMalware
    intent: Replace custom malware signatures (v34.04)
    question: How do I add my own malware signatures with the v34.04 feeds API?
  phrasing_ops: 8
  slug: palo-alto-networks-feeds-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: File Blocking Profiles
  name: Palo Alto Networks File Blocking Profiles API
  phrasing_intents:
  - id: ListFileBlockingProfiles
    intent: List file blocking profiles
    question: Which file blocking profiles are configured in my folders?
  - id: CreateFileBlockingProfiles
    intent: Create a file blocking profile
    question: How do I create a profile that blocks certain file types from being uploaded or downloaded?
  - id: GetFileBlockingProfilesByID
    intent: Get a file blocking profile
    question: What file types does a specific file blocking profile block?
  - id: UpdateFileBlockingProfilesByID
    intent: Update a file blocking profile
    question: Can I change the rules on a file blocking profile I already have?
  - id: DeleteFileBlockingProfilesByID
    intent: Delete a file blocking profile
    question: How do I delete a file blocking profile?
  - id: get-sse-config-v1-file-blocking-profiles
    intent: List file blocking profiles
    question: What file blocking profiles are set up in a folder?
  - id: post-sse-config-v1-file-blocking-profiles
    intent: Create a file blocking profile
    question: How do I block users from uploading or downloading certain file types?
  - id: delete-sse-config-v1-file-blocking-profiles-id
    intent: Delete a file blocking profile
    question: How do I remove a file blocking profile I no longer need?
  phrasing_ops: 10
  slug: palo-alto-networks-file-blocking-profiles-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The FileBlockingAction API from Palo Alto Networks — 2 operation(s) for fileblockingaction.
  name: Palo Alto Networks File Blocking Action API
  phrasing_intents:
  - id: get-v1-config-rulestacks-rulestackname-fileblockingprofiles-custom-filetypes
    intent: List file blocking file types on a rulestack
    question: Which file types does the custom file blocking profile on a rulestack cover?
  - id: get-v1-config-rulestacks-rulestackname-fileblockingprofiles-custom-filetypes-type
    intent: Get file blocking settings for one file type
    question: What action and direction are set for a single file type in a rulestack's file blocking profile?
  - id: put-v1-config-rulestacks-rulestackname-fileblockingprofiles-custom-filetypes-type
    intent: Set the file blocking action for a file type
    question: How do I block a specific file type from being uploaded or downloaded through a rulestack?
  phrasing_ops: 3
  slug: palo-alto-networks-fileblockingaction-api
- baseURL: https://api.strata.paloaltonetworks.com/config/setup/v1
  baseurl_source: declared
  description: Configuration folders
  name: Palo Alto Networks Folders API
  phrasing_intents:
  - id: ListFolders
    intent: List configuration folders
    question: Which configuration folders exist in Strata Cloud Manager?
  - id: CreateFolder
    intent: Create a configuration folder
    question: How do I create a new folder under an existing parent folder?
  - id: GetFolderByID
    intent: Get a configuration folder
    question: What's the parent and snippet list of a specific folder?
  - id: UpdateFolderByID
    intent: Update a configuration folder
    question: How do I move an existing folder to a different parent?
  - id: DeleteFolderByID
    intent: Delete a configuration folder
    question: How do I remove a folder I no longer use?
  phrasing_ops: 5
  slug: palo-alto-networks-folders-api
- baseURL: https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
  baseurl_source: declared
  description: Forwarding Profiles
  name: Palo Alto Networks Forwarding Profiles API
  phrasing_intents:
  - id: ListGlobalProtectForwardingProfiles
    intent: List GlobalProtect forwarding profiles
    question: Which GlobalProtect forwarding profiles are configured in a folder?
  - id: CreateGlobalProtectForwardingProfile
    intent: Create a GlobalProtect forwarding profile
    question: How do I set up a new GlobalProtect forwarding profile?
  - id: GetGlobalProtectForwardingProfileByID
    intent: Get a GlobalProtect forwarding profile
    question: What type and definition method does a given forwarding profile use?
  - id: UpdateGlobalProtectForwardingProfileByID
    intent: Update a GlobalProtect forwarding profile
    question: Can I change the type of an existing GlobalProtect forwarding profile?
  - id: DeleteGlobalProtectForwardingProfile
    intent: Delete a GlobalProtect forwarding profile
    question: How do I remove a GlobalProtect forwarding profile?
  phrasing_ops: 5
  slug: palo-alto-networks-forwarding-profiles-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The FQDN API from Palo Alto Networks — 3 operation(s) for fqdn.
  name: Palo Alto Networks FQDN API
  phrasing_intents:
  - id: list.fqdn_rules.v2
    intent: List FQDN-based applications
    question: Which FQDN applications are published through my ZTNA connectors?
  - id: create.fqdn_rule.v2
    intent: Create an FQDN-based application
    question: How do I publish a new application by FQDN through a connector group?
  - id: get.fqdn_rule.v2
    intent: Get an FQDN-based application
    question: What's configured on one FQDN application?
  - id: update.fqdn_rule.v2
    intent: Update an FQDN-based application
    question: Can I turn off an FQDN application without deleting it?
  - id: delete.fqdn_rule.v2
    intent: Delete an FQDN-based application
    question: How do I remove an FQDN application from my connectors?
  - id: get.fqdn_rule.filters.v2
    intent: Get filter values for FQDN rule fields
    question: What values can I filter FQDN applications by for a given field?
  phrasing_ops: 6
  slug: palo-alto-networks-fqdn-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The FQDNList API from Palo Alto Networks — 2 operation(s) for fqdnlist.
  name: Palo Alto Networks FQDN List API
  phrasing_intents:
  - id: get-v1-config-rulestacks-rulestackname-fqdnlists
    intent: List FQDN lists in a rulestack
    question: Which FQDN lists does a Cloud NGFW rulestack contain?
  - id: post-v1-config-rulestacks-rulestackname-fqdnlists
    intent: Create an FQDN list in a rulestack
    question: How do I add a list of domain names to a Cloud NGFW rulestack?
  - id: delete-v1-config-rulestacks-rulestackname-fqdnlists-name
    intent: Delete an FQDN list from a rulestack
    question: How do I delete an FQDN list from a rulestack?
  - id: get-v1-config-rulestacks-rulestackname-fqdnlists-name
    intent: Get an FQDN list from a rulestack
    question: What domains are in a specific FQDN list on my rulestack?
  - id: put-v1-config-rulestacks-rulestackname-fqdnlists-name
    intent: Update an FQDN list in a rulestack
    question: How do I change the domains in an existing FQDN list?
  phrasing_ops: 5
  slug: palo-alto-networks-fqdnlist-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: General Settings
  name: Palo Alto Networks General Settings API
  phrasing_intents:
  - id: ListGeneralSettings
    intent: List general settings
    question: What general settings are configured for a folder or device?
  - id: CreateGeneralSettings
    intent: Create general settings
    question: How do I create a general settings object?
  - id: GetGeneralSettingsByID
    intent: Get general settings by ID
    question: What's in one specific general settings object?
  - id: UpdateGeneralSettingsByID
    intent: Update general settings
    question: Can I change existing general settings?
  - id: DeleteGeneralSettingsByID
    intent: Delete general settings
    question: How do I remove a general settings object?
  phrasing_ops: 5
  slug: palo-alto-networks-general-settings-api
- baseURL: https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
  baseurl_source: declared
  description: Global Settings
  name: Palo Alto Networks Global Settings API
  phrasing_intents:
  - id: GetGlobalProtectSettings
    intent: Get GlobalProtect global settings
    question: What GlobalProtect agent version and global settings are configured in Prisma Access?
  - id: UpdateMobileAgentSettings
    intent: Update GlobalProtect global settings
    question: How do I change the GlobalProtect agent version for my users?
  phrasing_ops: 2
  slug: palo-alto-networks-global-settings-api
- baseURL: https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
  baseurl_source: declared
  description: GlobalProtect Enablement
  name: Palo Alto Networks GlobalProtect Enablement API
  phrasing_intents:
  - id: GetGlobalProtectEnablement
    intent: Check if GlobalProtect is enabled
    question: Is GlobalProtect enabled in my Prisma Access tenant?
  - id: CreateGlobalProtectEnablement
    intent: Enable GlobalProtect in Prisma Access
    question: How do I enable GlobalProtect in Prisma Access if I don't use the UI?
  phrasing_ops: 2
  slug: palo-alto-networks-globalprotect-enablement-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Globalprotect Match List
  name: Palo Alto Networks Globalprotect Match List API
  phrasing_intents:
  - id: ListGlobalprotectMatchList
    intent: List GlobalProtect match list entries
    question: Which GlobalProtect log match list entries are configured?
  - id: CreateGlobalprotectMatchList
    intent: Create a GlobalProtect match list entry
    question: How do I forward matching GlobalProtect logs to syslog?
  - id: GetGlobalprotectMatchListByID
    intent: Get a GlobalProtect match list entry
    question: What filter and forwarding does one GlobalProtect match list entry use?
  - id: UpdateGlobalprotectMatchListByID
    intent: Update a GlobalProtect match list entry
    question: How do I change the filter on an existing GlobalProtect match list entry?
  - id: DeleteGlobalprotectMatchListByID
    intent: Delete a GlobalProtect match list entry
    question: How do I remove a GlobalProtect match list entry?
  phrasing_ops: 5
  slug: palo-alto-networks-globalprotect-match-list-api
- baseURL: https://api.sase.paloaltonetworks.com/ai-red-teaming/data-plane
  baseurl_source: declared
  description: Operations related to GoalCategories.
  name: Palo Alto Networks Goal Categories API
  phrasing_intents:
  - id: get_goal_categories_v1_goal_categories__target_type__get
    intent: Get goal categories for a target type
    question: Which goal categories are available for a given target type?
  phrasing_ops: 1
  slug: palo-alto-networks-goalcategories-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Group Resource API API from Palo Alto Networks — 5 operation(s) for group resource api.
  name: Palo Alto Networks Group Resource API
  phrasing_intents:
  - id: PostMtManage5gUsergroup
    intent: Create a 5G subscriber group
    question: How do I group 5G subscriber identities to apply one security policy?
  - id: PostMtManage5gUsergroupList
    intent: List a tenant's 5G user groups
    question: Which 5G user groups exist for a tenant?
  - id: GetMtManage5gUsergroupBy_groupid
    intent: List members of a 5G subscriber group
    question: Which subscriber identities belong to a given 5G group?
  - id: PutMtManage5gUsergroupBy_group_id
    intent: Update a 5G subscriber group
    question: How do I add or remove subscribers from an existing 5G group?
  - id: DeleteMtManage5gUsergroupBy_identity_id
    intent: Delete a 5G user group
    question: Is deleting a 5G user group permanent?
  phrasing_ops: 5
  slug: palo-alto-networks-group-resource-api-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/groups/groups.md''}'
  name: Palo Alto Networks Groups API
  phrasing_intents:
  - id: get-groups
    intent: List user groups (v34.03)
    question: Which user groups are defined in Compute, per the v34.03 API?
  - id: post-groups
    intent: Add a user group (v34.03)
    question: Can I create a group mapped to an LDAP or SAML group on v34.03?
  - id: get-groups-names
    intent: List group names (v34.03)
    question: Can I get just group names with the older v34.03 endpoint?
  - id: delete-groups-id
    intent: Delete a user group (v34.03)
    question: Can I remove a group with the v34.03 API?
  - id: put-groups-id
    intent: Update a user group (v34.03)
    question: Can I change a group's role through the v34.03 API?
  - id: getApiV3404Groups
    intent: List user groups
    question: Which user groups have access to Prisma Cloud Compute?
  - id: postApiV3404Groups
    intent: Add a user group
    question: How do I create a group that maps to an OIDC or LDAP group?
  - id: getApiV3404GroupsNames
    intent: List group names
    question: Can I get a quick list of group names only?
  phrasing_ops: 10
  slug: palo-alto-networks-groups-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: High Availability Configurations
  name: Palo Alto Networks High Availability Configurations API
  phrasing_intents:
  - id: GetHAConfiguration
    intent: Get a device's HA configuration
    question: Is high availability turned on for my firewall?
  - id: CreateHAConfiguration
    intent: Create an HA configuration
    question: How do I set up high availability on a firewall for the first time?
  - id: UpdateHAConfiguration
    intent: Update a device's HA configuration
    question: Can I change the HA group or interface on a device that already has HA?
  - id: DeleteHAConfiguration
    intent: Delete a device's HA configuration
    question: Can I remove high availability from a device entirely?
  - id: AutocompleteHAPorts
    intent: Suggest ports for HA setup
    question: Which ports can I pick for an HA link on this device?
  - id: AutocompleteHAIPAddresses
    intent: Suggest IP addresses for HA setup
    question: What IP addresses are available to assign to an HA interface?
  - id: AutocompleteHANetmasks
    intent: Suggest netmasks for HA setup
    question: Which netmasks can I use on an HA interface?
  - id: AutocompleteHAGateways
    intent: Suggest gateways for HA setup
    question: What gateway addresses are available for an HA interface?
  phrasing_ops: 8
  slug: palo-alto-networks-high-availability-configurations-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: High Availability Devices
  name: Palo Alto Networks High Availability Devices API
  phrasing_intents:
  - id: ListHADevices
    intent: List high availability devices
    question: Which firewalls are configured as high availability devices?
  phrasing_ops: 1
  slug: palo-alto-networks-high-availability-devices-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: HIP Objects
  name: Palo Alto Networks HIP Objects API
  phrasing_intents:
  - id: ListHIPObjects
    intent: List HIP objects
    question: Which host information profile (HIP) objects are defined?
  - id: CreateHIPObjects
    intent: Create a HIP object
    question: How do I create a HIP object that checks disk encryption on endpoints?
  - id: GetHIPObjectsByID
    intent: Get a HIP object
    question: What endpoint checks does a particular HIP object define?
  - id: UpdateHIPObjectsByID
    intent: Update a HIP object
    question: How do I change the checks in an existing HIP object?
  - id: DeleteHIPObjectsByID
    intent: Delete a HIP object
    question: How do I delete a HIP object?
  - id: get-sse-config-v1-hip-objects
    intent: List HIP objects
    question: Which host information profile objects are defined in a folder?
  - id: post-sse-config-v1-hip-objects
    intent: Create a HIP object
    question: How do I create a HIP object that checks for disk encryption or anti-malware?
  - id: delete-sse-config-v1-hip-objects-id
    intent: Delete a HIP object
    question: How do I delete a HIP object using the SSE config v1 path?
  phrasing_ops: 10
  slug: palo-alto-networks-hip-objects-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: HIP Profiles
  name: Palo Alto Networks HIP Profiles API
  phrasing_intents:
  - id: ListHIPProfiles
    intent: List HIP profiles
    question: Which host information profiles are defined for GlobalProtect posture checks?
  - id: CreateHIPProfiles
    intent: Create a HIP profile
    question: How do I create a HIP profile that matches compliant endpoints?
  - id: GetHIPProfilesByID
    intent: Get a HIP profile
    question: What match criteria does a particular HIP profile use?
  - id: UpdateHIPProfilesByID
    intent: Update a HIP profile
    question: How do I change the match condition on an existing HIP profile?
  - id: DeleteHIPProfilesByID
    intent: Delete a HIP profile
    question: How do I delete a HIP profile?
  - id: get-sse-config-v1-hip-profiles
    intent: List HIP profiles
    question: Which host information profiles are defined in a folder?
  - id: post-sse-config-v1-hip-profiles
    intent: Create a HIP profile
    question: How do I create a host information profile to check endpoint posture?
  - id: delete-sse-config-v1-hip-profiles-id
    intent: Delete a HIP profile
    question: What's the way to remove a HIP profile?
  phrasing_ops: 10
  slug: palo-alto-networks-hip-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Hipmatch Match List
  name: Palo Alto Networks Hipmatch Match List API
  phrasing_intents:
  - id: ListHipmatchMatchList
    intent: List HIP match log forwarding entries
    question: Which HIP match list entries are configured in a folder or snippet?
  - id: CreateHipmatchMatchList
    intent: Create a HIP match list entry
    question: How do I forward HIP match logs to syslog or email?
  - id: GetHipmatchMatchListByID
    intent: Get a HIP match list entry
    question: What filter and forwarding targets does a specific hipmatch entry use?
  - id: UpdateHipmatchMatchListByID
    intent: Update a HIP match list entry
    question: Can I change the filter on an existing hipmatch match list entry?
  - id: DeleteHipmatchMatchListByID
    intent: Delete a HIP match list entry
    question: What's the way to remove a hipmatch match list entry?
  phrasing_ops: 5
  slug: palo-alto-networks-hipmatch-match-list-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: HTTP Header Profiles
  name: Palo Alto Networks HTTP Header Profiles API
  phrasing_intents:
  - id: ListHTTPHeaderProfiles
    intent: List HTTP header profiles
    question: Which HTTP header profiles are configured in my Strata Cloud Manager tenant?
  - id: CreateHTTPHeaderProfiles
    intent: Create a HTTP header profile
    question: How do I create a new HTTP header profile?
  - id: GetHTTPHeaderProfilesByID
    intent: Get a HTTP header profile
    question: What settings does a specific HTTP header profile contain?
  - id: UpdateHTTPHeaderProfilesByID
    intent: Update a HTTP header profile
    question: How do I change the headers an existing HTTP header profile inserts?
  - id: DeleteHTTPHeaderProfilesByID
    intent: Delete a HTTP header profile
    question: Which call removes a HTTP header profile I no longer use?
  - id: get-sse-config-v1-http-header-profiles
    intent: List HTTP header profiles
    question: Which HTTP header insertion profiles exist in a folder?
  - id: post-sse-config-v1-http-header-profiles
    intent: Create an HTTP header profile
    question: How do I create a profile that inserts custom HTTP headers?
  - id: delete-sse-config-v1-http-header-profiles-id
    intent: Delete an HTTP header profile
    question: How do I delete an HTTP header profile?
  phrasing_ops: 10
  slug: palo-alto-networks-http-header-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: HTTP Server Profiles
  name: Palo Alto Networks HTTP Server Profiles API
  phrasing_intents:
  - id: ListHTTPServerProfiles
    intent: List HTTP server profiles
    question: Which HTTP server profiles are set up for log forwarding?
  - id: CreateHTTPServerProfiles
    intent: Create an HTTP server profile
    question: How do I add an HTTP server profile to send logs to a web endpoint?
  - id: GetHTTPServerProfilesByID
    intent: Get an HTTP server profile
    question: What servers and format does a given HTTP server profile use?
  - id: UpdateHTTPServerProfilesByID
    intent: Update an HTTP server profile
    question: Can I change the destination servers on an existing HTTP server profile?
  - id: DeleteHTTPServerProfilesByID
    intent: Delete an HTTP server profile
    question: Can I delete an HTTP server profile that's no longer used?
  phrasing_ops: 5
  slug: palo-alto-networks-http-server-profiles-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The HTTPSProfiles API from Palo Alto Networks — 2 operation(s) for httpsprofiles.
  name: Palo Alto Networks HTTPS Profiles API
  phrasing_intents:
  - id: get-logging-service-logforwarding-v1-https-profiles
    intent: List log forwarding HTTPS profiles
    question: Which HTTPS profiles are set up to forward Cortex Data Lake logs to my SIEM?
  - id: post-logging-service-logforwarding-v1-https-profiles
    intent: Create an HTTPS log forwarding profile
    question: How do I start forwarding Cortex Data Lake logs to an HTTPS receiver or SIEM?
  - id: delete-logging-service-logforwarding-v1-https-profiles-profileid
    intent: Delete an HTTPS log forwarding profile
    question: How do I stop forwarding logs to an HTTPS receiver I no longer use?
  - id: get-logging-service-logforwarding-v1-https-profiles-profileid
    intent: Get one HTTPS log forwarding profile
    question: What destination and log types is a specific HTTPS forwarding profile configured with?
  - id: put-logging-service-logforwarding-v1-https-profiles-profileid
    intent: Update an HTTPS log forwarding profile
    question: Can I change the receiver or log types on an HTTPS forwarding profile I already created?
  phrasing_ops: 5
  slug: palo-alto-networks-httpsprofiles-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: 'Prisma Cloud identity and access management (IAM) security provides: * Visiblity—Query all relevant IAM entities * Gonvernance—Monitor your cloud environment for overly-used permissions * Response—Aut'
  name: Palo Alto Networks IAM API
  phrasing_intents:
  - id: get-permissions-with-post
    intent: Run an IAM query to list permissions
    question: How do I run an IAM query in Prisma Cloud to see who can access what?
  - id: get-next-permissions-page-with-post
    intent: Get the next page of IAM permission results
    question: What do I pass to fetch the next page after a v1 IAM permissions query?
  - id: get-permissions-access-with-post
    intent: See when a permission was last used
    question: How can I tell when a specific IAM permission was actually last used?
  - id: get-next-permissions-access-with-post
    intent: Get the next page of permission last-access data
    question: How do I keep paging through permission last-access results in v1?
  - id: get-remediation-with-post
    intent: Get remediations for IAM alerts
    question: How do I get suggested remediations for a batch of IAM alerts?
  - id: get-rql-with-get
    intent: Get the IAM query behind an alert
    question: Which IAM query triggered a given alert, using the original v1 lookup?
  - id: get-suggestions-with-post
    intent: Get autocomplete suggestions for an IAM query
    question: How can I tell whether my partial IAM query is valid yet?
  - id: search-permissions-v3
    intent: Search IAM permissions with the v3 API
    question: How do I search permissions with the v3 IAM search and get a next page token?
  phrasing_ops: 21
  slug: palo-alto-networks-iam-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Prisma Cloud identity and access management (IAM) security integrates with the identity provider (IdP) service Okta to ingest single sign-on (SSO) data for the effective permissions calculation in the
  name: Palo Alto Networks IAM IDP API
  phrasing_intents:
  - id: test-integration-with-post
    intent: Test an Okta identity provider integration
    question: How do I check whether my Okta integration with Prisma Cloud is valid before saving it?
  phrasing_ops: 1
  slug: palo-alto-networks-iam-idp-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The IKE Crypto Profiles API from Palo Alto Networks — 4 operation(s) for ike crypto profiles.
  name: Palo Alto Networks IKE Crypto Profiles API
  phrasing_intents:
  - id: delete-v1-ike-crypto-profiles
    intent: Delete an IKE crypto profile by name (v1)
    question: How do I remove an IKE crypto profile by its name for a sub-tenant?
  - id: get-v1-ike-crypto-profiles
    intent: Check status of IKE crypto profile creation
    question: Did my IKE crypto profile request finish, and what UUID was assigned?
  - id: post-v1-ike-crypto-profiles
    intent: Create an IKE crypto profile (v1)
    question: How do I add a new IKE crypto profile for a sub-tenant?
  - id: put-v1-ike-crypto-profiles
    intent: Edit an IKE crypto profile (v1)
    question: Can I change the encryption or DH group of an IKE crypto profile for a sub-tenant?
  - id: get-v1-ike-crypto-profiles-read
    intent: Fetch results of an IKE profile read request
    question: Where do I collect the IKE crypto profile list after submitting a read request?
  - id: post-v1-ike-crypto-profiles-read
    intent: Submit a request to read IKE crypto profiles
    question: How do I start a read of specific IKE crypto profiles by name?
  - id: ListIKECryptoProfiles
    intent: List IKE crypto profiles in a folder
    question: What IKE crypto profiles are defined in a configuration folder or snippet?
  - id: CreateIKECryptoProfiles
    intent: Create an IKE crypto profile
    question: How do I define a new IKE crypto profile for my VPN tunnels?
  phrasing_ops: 16
  slug: palo-alto-networks-ike-crypto-profiles-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The IKE Gateway API from Palo Alto Networks — 1 operation(s) for ike gateway.
  name: Palo Alto Networks IKE Gateway API
  phrasing_intents:
  - id: get-v1-ike-gateways-read
    intent: Get IKE gateway configs by UUID
    question: What IKE gateway configuration is tied to a given UUID?
  - id: post-v1-ike-gateways-read
    intent: Read IKE gateways by name
    question: Can I look up several remote network IKE gateways by their names at once?
  phrasing_ops: 2
  slug: palo-alto-networks-ike-gateway-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: IKE Gateways
  name: Palo Alto Networks IKE Gateways API
  phrasing_intents:
  - id: ListIKEGateways
    intent: List IKE gateways
    question: Which IKE gateways are configured in Strata Cloud Manager?
  - id: CreateIKEGateways
    intent: Create an IKE gateway in the candidate config
    question: How do I stage a new IKE gateway in the candidate configuration?
  - id: GetIKEGatewaysByID
    intent: Get an IKE gateway
    question: What peer and authentication settings does one IKE gateway have?
  - id: UpdateIKEGatewaysByID
    intent: Update an IKE gateway
    question: How do I change the peer address on an existing IKE gateway?
  - id: DeleteIKEGatewaysByID
    intent: Delete an IKE gateway
    question: How do I remove an IKE gateway I no longer use?
  - id: GenerateIKEGatewayPPKKey
    intent: Generate a post-quantum PPK key
    question: How do I get a post-quantum pre-shared key for an IKE gateway?
  - id: get-sse-config-v1-ike-gateways
    intent: List IKE gateways in an SSE config folder
    question: Which IKE gateways are configured in a given Prisma Access folder?
  - id: post-sse-config-v1-ike-gateways
    intent: Create an IKE gateway via SSE config
    question: What do I need to create an IKE gateway through the SSE config v1 API?
  phrasing_ops: 11
  slug: palo-alto-networks-ike-gateways-api
- baseURL: https://api.strata.paloaltonetworks.com
  baseurl_source: declared
  description: The Incidents APIs API from Palo Alto Networks — 2 operation(s) for incidents apis.
  name: Palo Alto Networks Incidents APIs API
  phrasing_intents:
  - id: searchIncidents
    intent: Search network security incidents
    question: Which network security incidents occurred in my tenant recently?
  - id: getIncidentDetails
    intent: Get details of a security incident
    question: What happened in a specific network security incident?
  phrasing_ops: 2
  slug: palo-alto-networks-incidents-apis-api
- baseURL: https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
  baseurl_source: declared
  description: Infrastructure Settings
  name: Palo Alto Networks Infrastructure Settings API
  phrasing_intents:
  - id: GetGlobalProtectInfrastructureSettings
    intent: Get GlobalProtect infrastructure settings
    question: What DNS servers and IP pools are set in my GlobalProtect infrastructure settings?
  - id: CreateGlobalProtectInfrastructureSettings
    intent: Create GlobalProtect infrastructure settings
    question: How do I set up GlobalProtect infrastructure settings for the first time?
  - id: UpdateGlobalProtectInfrastructureSettings
    intent: Update GlobalProtect infrastructure settings
    question: Can I change the portal hostname in GlobalProtect infrastructure settings?
  - id: DeleteGlobalProtectInfrastructureSettings
    intent: Delete GlobalProtect infrastructure settings
    question: How do I delete a GlobalProtect infrastructure setting?
  - id: post-sse-config-v1-enable
    intent: Initialize defaults for a new Prisma Access tenant
    question: How do I set up application defaults for a newly onboarded Prisma Access tenant?
  - id: get-sse-config-v1-shared-infrastructure-settings
    intent: List shared infrastructure settings
    question: What infrastructure subnet and BGP AS are configured for Prisma Access?
  - id: put-sse-config-v1-shared-infrastructure-settings
    intent: Edit shared infrastructure settings
    question: How do I change the Prisma Access infrastructure subnet?
  phrasing_ops: 7
  slug: palo-alto-networks-infrastructure-settings-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Insights Resources API API from Palo Alto Networks — 1 operation(s) for insights resources api.
  name: Palo Alto Networks Insights Resources API
  phrasing_intents:
  - id: post-mt-monitor-v1-agg-upgrades-list
    intent: List upgrades across tenants
    question: Which upgrades are scheduled or completed across my tenants?
  phrasing_ops: 1
  slug: palo-alto-networks-insights-resources-api-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Instance API from Palo Alto Networks — 1 operation(s) for instance.
  name: Palo Alto Networks Instance API
  phrasing_intents:
  - id: get-subscription-v1-instances
    intent: List licensed tenant instances
    question: Which instances have licenses allocated in my tenant service group?
  - id: post-subscription-v1-instances
    intent: Allocate a license to a child tenant
    question: How do I allocate a license to a child tenant as a new instance?
  phrasing_ops: 2
  slug: palo-alto-networks-instance-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: With Prisma Cloud service’s multiple out-of-the-box integration options, you can integrate Prisma Cloud into existing security workflows and technologies of your organization. You can use [Integration
  name: Palo Alto Networks Integrations Pull API
  phrasing_intents:
  - id: get-all-integrations-metadata
    intent: List integration metadata by type
    question: Where can I find the IDs of my Okta, Qualys or Tenable integrations?
  - id: get-all-integrations
    intent: List all integrations
    question: Which Okta, Qualys and Tenable integrations are configured in Prisma Cloud?
  - id: save-integration
    intent: Add an Okta, Qualys or Tenable integration
    question: How do I connect Tenable to Prisma Cloud as a new integration?
  - id: test-integration
    intent: Test an integration's configuration
    question: Can I verify that my Qualys credentials work before saving the integration?
  - id: get-integration-by-id
    intent: Get an integration by ID
    question: What is configured on one specific integration?
  - id: update-integration
    intent: Update an integration
    question: Can I rotate the credentials on an existing Tenable integration?
  - id: delete-integration
    intent: Delete an integration
    question: Can I remove an Okta integration I no longer use?
  phrasing_ops: 7
  slug: palo-alto-networks-integrations-pull-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The IntelligentFeed API from Palo Alto Networks — 2 operation(s) for intelligentfeed.
  name: Palo Alto Networks Intelligent Feed API
  phrasing_intents:
  - id: post-v1-config-rulestacks-rulestackname-feeds
    intent: Create an intelligence feed on a rulestack
    question: How do I add an external dynamic list as an intelligence feed on my Cloud NGFW rulestack?
  - id: delete-v1-config-rulestacks-rulestackname-feeds-name
    intent: Delete an intelligence feed
    question: How do I remove a threat intelligence feed from a rulestack?
  - id: get-v1-config-rulestacks-rulestackname-feeds-name
    intent: Get an intelligence feed's data
    question: What threat data has an intelligence feed collected for my rulestack?
  - id: put-v1-config-rulestacks-rulestackname-feeds-name
    intent: Update an intelligence feed
    question: Can I change the URL or refresh frequency of an existing intelligence feed?
  phrasing_ops: 4
  slug: palo-alto-networks-intelligentfeed-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The Interconnect API API from Palo Alto Networks — 1 operation(s) for interconnect api.
  name: Palo Alto Networks Interconnect API
  phrasing_intents:
  - id: GetMtManage5gInterconnect
    intent: List regional 5G interconnects
    question: Which regions have 5G interconnects, and how much bandwidth capacity do they have?
  phrasing_ops: 1
  slug: palo-alto-networks-interconnect-api-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Interconnect Throughput API from Palo Alto Networks — 1 operation(s) for interconnect throughput.
  name: Palo Alto Networks Interconnect Throughput API
  phrasing_intents:
  - id: PostMtSp-interconnectMonitorInterconnectsThroughput
    intent: Monitor interconnect throughput
    question: Is any service provider interconnect hitting a throughput bottleneck?
  phrasing_ops: 1
  slug: palo-alto-networks-interconnect-throughput-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Interconnect Traffic API from Palo Alto Networks — 1 operation(s) for interconnect traffic.
  name: Palo Alto Networks Interconnect Traffic API
  phrasing_intents:
  - id: PostMtSp-interconnectMonitorInterconnectsTraffic
    intent: Get data transfer totals for interconnects
    question: How much data has moved in and out through my interconnects for billing?
  phrasing_ops: 1
  slug: palo-alto-networks-interconnect-traffic-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Interface Management Profiles
  name: Palo Alto Networks Interface Management Profiles API
  phrasing_intents:
  - id: ListInterfaceManagementProfiles
    intent: List interface management profiles
    question: Which interface management profiles exist in my firewall configuration?
  - id: CreateInterfaceManagementProfiles
    intent: Create an interface management profile
    question: How do I allow HTTPS, SSH or ping on a firewall interface?
  - id: GetInterfaceManagementProfilesByID
    intent: Get an interface management profile
    question: Which management services does a particular interface profile allow?
  - id: UpdateInterfaceManagementProfilesByID
    intent: Update an interface management profile
    question: How do I turn off telnet on an existing interface management profile?
  - id: DeleteInterfaceManagementProfilesByID
    intent: Delete an interface management profile
    question: How do I remove an interface management profile?
  phrasing_ops: 5
  slug: palo-alto-networks-interface-management-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/deployment/v1
  baseurl_source: declared
  description: Internal DNS servers
  name: Palo Alto Networks Internal DNS Servers API
  phrasing_intents:
  - id: ListInternalDNSServers
    intent: List internal DNS servers
    question: Which internal DNS servers are configured for Prisma Access?
  - id: CreateInternalDNSServers
    intent: Add an internal DNS server
    question: How do I resolve internal domains through my own DNS servers in Prisma Access?
  - id: GetInternalDNSServersByID
    intent: Get an internal DNS server
    question: Where can I see one internal DNS server's settings?
  - id: UpdateInternalDNSServersByID
    intent: Update an internal DNS server
    question: How do I change the primary IP of an existing internal DNS server?
  - id: DeleteInternalDNSServersByID
    intent: Delete an internal DNS server
    question: Can I remove an internal DNS server entry?
  - id: get-sse-config-v1-internal-dns-servers
    intent: List internal DNS servers in a folder
    question: Which internal DNS servers resolve my private domains in Prisma Access?
  - id: post-sse-config-v1-internal-dns-servers
    intent: Add an internal DNS server
    question: How do I send lookups for my internal domains to our own DNS server?
  - id: delete-sse-config-v1-internal-dns-servers-id
    intent: Delete an internal DNS server
    question: How do I remove an internal DNS server entry?
  phrasing_ops: 10
  slug: palo-alto-networks-internal-dns-servers-api
- baseURL: https://api.strata.paloaltonetworks.com
  baseurl_source: declared
  description: The Internal Domains API from Palo Alto Networks — 2 operation(s) for internal domains.
  name: Palo Alto Networks Internal Domains API
  phrasing_intents:
  - id: ListInternalDomains
    intent: List internal domains
    question: Which internal domains are configured for the DNS resolver?
  - id: CreateInternalDomain
    intent: Add a custom internal domain
    question: How do I add a custom internal domain?
  - id: DeleteInternalDomainByID
    intent: Delete a custom internal domain
    question: How do I remove a custom internal domain?
  - id: GetInternalDomainByID
    intent: Get an internal domain
    question: Can I look up one internal domain by ID?
  - id: UpdateInternalDomainByID
    intent: Update a custom internal domain
    question: Can I change the domain name on a custom internal domain entry?
  phrasing_ops: 5
  slug: palo-alto-networks-internal-domains-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The InternetController API from Palo Alto Networks — 1 operation(s) for internetcontroller.
  name: Palo Alto Networks Internet Controller API
  phrasing_intents:
  - id: InternetController.getInternetMetric
    intent: Get internet experience metrics
    question: How is internet performance looking for my users over a time range?
  phrasing_ops: 1
  slug: palo-alto-networks-internetcontroller-api
- baseURL: https://api.strata.paloaltonetworks.com
  baseurl_source: declared
  description: The IoT Public APIs are listed below.
  name: Palo Alto Networks IoT Public API
  phrasing_intents:
  - id: device-detail
    intent: Look up an IoT device by MAC address
    question: What does IoT Security know about the device with a given MAC address?
  - id: device-detail-ip
    intent: Look up an IoT device by IP address
    question: Which device is sitting at a particular IP address in my IoT inventory?
  - id: device-inventory
    intent: List the full IoT device inventory
    question: How do I export every device in my IoT Security inventory?
  - id: device-inventory-V2
    intent: List the device inventory with chosen attributes
    question: Can I choose which device attributes come back when I pull the IoT inventory?
  - id: device-search
    intent: Search for a device or multi-interface device
    question: How can I find a multi-interface device by one of its IP or MAC addresses?
  - id: profile-mapping
    intent: Map device profiles to categories and verticals
    question: Which category and industry vertical does each IoT device profile belong to?
  - id: tags-list
    intent: List user-defined device tags
    question: What user-defined tags have been assigned to my IoT devices?
  - id: tag
    intent: Add a manual tag to devices
    question: How do I tag a group of IoT devices manually?
  phrasing_ops: 56
  slug: palo-alto-networks-iot-public-api-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The IP Pool Usage API from Palo Alto Networks — 1 operation(s) for ip pool usage.
  name: Palo Alto Networks IP Pool Usage API
  phrasing_intents:
  - id: GetMtSp-interconnectMonitorIp-pool-usage
    intent: Check IP pool usage for an interconnect
    question: Am I about to run out of IP addresses on an interconnect?
  phrasing_ops: 1
  slug: palo-alto-networks-ip-pool-usage-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The IPSec Crypto Profiles API from Palo Alto Networks — 4 operation(s) for ipsec crypto profiles.
  name: Palo Alto Networks IPSec Crypto Profiles API
  phrasing_intents:
  - id: delete-v1-ipsec-crypto-profiles
    intent: Delete an IPSec crypto profile by name (v1)
    question: Can I delete a v1 IPSec crypto profile just by name?
  - id: get-v1-ipsec-crypto-profiles
    intent: Check status of an IPSec crypto profile job
    question: Did my IPSec crypto profile create or delete request succeed?
  - id: post-v1-ipsec-crypto-profiles
    intent: Create an IPSec crypto profile (v1 async)
    question: Can I create an IPSec crypto profile for a Panorama sub-tenant?
  - id: put-v1-ipsec-crypto-profiles
    intent: Modify an IPSec crypto profile (v1 async)
    question: How do I change the lifetime on an IPSec crypto profile in a multi-tenant Panorama setup?
  - id: get-v1-ipsec-crypto-profiles-read
    intent: Fetch results of an IPSec profile read job
    question: Where do I pick up the IPSec profile configurations after submitting a read request?
  - id: post-v1-ipsec-crypto-profiles-read
    intent: Request a read of IPSec crypto profiles
    question: How do I start an async read of specific IPSec crypto profiles?
  - id: ListIPsecCryptoProfiles
    intent: List IPsec crypto profiles in a folder
    question: Which IPsec crypto profiles are defined in a given folder or snippet?
  - id: CreateIPsecCryptoProfiles
    intent: Create an IPsec crypto profile
    question: How do I add an IPsec crypto profile with additional key exchange for post-quantum tunnels?
  phrasing_ops: 16
  slug: palo-alto-networks-ipsec-crypto-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Iptag Match List
  name: Palo Alto Networks Iptag Match List API
  phrasing_intents:
  - id: ListIptagMatchList
    intent: List IP-tag match list entries
    question: Which IP-tag log forwarding match list entries are configured?
  - id: CreateIptagMatchList
    intent: Create an IP-tag match list entry
    question: How do I forward IP-tag logs matching a filter to syslog?
  - id: GetIptagMatchListByID
    intent: Get an IP-tag match list entry
    question: Where does a specific IP-tag match entry forward its logs?
  - id: UpdateIptagMatchListByID
    intent: Update an IP-tag match list entry
    question: Can I change the filter on an existing IP-tag match entry?
  - id: DeleteIptagMatchListByID
    intent: Delete an IP-tag match list entry
    question: Can I remove an IP-tag match list entry?
  phrasing_ops: 5
  slug: palo-alto-networks-iptag-match-list-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Issuer Certificates.
  name: Palo Alto Networks Issuer Certificates API
  phrasing_intents:
  - id: intermediatecertificates_getAll
    intent: List issuer intermediate certificates
    question: Which intermediate CA certificates have been issued to my distributed issuer instances?
  phrasing_ops: 1
  slug: palo-alto-networks-issuer-certificates-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Issuer Configurations.
  name: Palo Alto Networks Issuer Configurations API
  phrasing_intents:
  - id: configurations_create
    intent: Create an Issuer configuration
    question: How do I link a Sub CA provider, issuance policies and an identity provider into a new Issuer configuration?
  - id: configurations_getAll
    intent: List Issuer configurations
    question: Which distributed Issuer configurations have been set up?
  - id: configurations_getById
    intent: Get an Issuer configuration
    question: Which policies and Sub CA provider does a specific Issuer configuration use?
  - id: configurations_update
    intent: Update an Issuer configuration
    question: Can I swap the policies on an Issuer configuration without touching other fields?
  - id: configurations_delete
    intent: Remove an Issuer configuration
    question: Will Issuer instances stop working if I delete the configuration they use?
  phrasing_ops: 5
  slug: palo-alto-networks-issuer-configurations-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Issuer Sub CA Providers.
  name: Palo Alto Networks Issuer Sub CA Providers API
  phrasing_intents:
  - id: subcaproviders_create
    intent: Create a subordinate CA provider
    question: How do I set up a new subordinate CA provider for distributed issuers?
  - id: subcaprovider_getAll
    intent: List subordinate CA providers
    question: Which subordinate CA providers are set up for distributed issuance?
  - id: subcaproviders_getById
    intent: Get a subordinate CA provider
    question: What are the settings of one specific sub CA provider?
  - id: subcaproviders_update
    intent: Update a subordinate CA provider
    question: Can I change just the validity period on an existing sub CA provider?
  - id: subcaproviders_delete
    intent: Delete a subordinate CA provider
    question: How do I remove a subordinate CA provider?
  phrasing_ops: 5
  slug: palo-alto-networks-issuer-sub-ca-providers-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The JIRA API from Palo Alto Networks — 3 operation(s) for jira.
  name: Palo Alto Networks JIRA API
  phrasing_intents:
  - id: getJiraIssue
    intent: Get a Jira issue from an SSPM integration
    question: Can I look up the details of a Jira ticket created from SSPM?
  - id: getJiraProjectDetail
    intent: Get a Jira project from an SSPM integration
    question: What are the details of a Jira project connected to SSPM?
  - id: getJiraProjects
    intent: List Jira projects in an SSPM integration
    question: Which Jira projects are onboarded to my SSPM ticketing integration?
  phrasing_ops: 3
  slug: palo-alto-networks-jira-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: Kerberos Server Profiles
  name: Palo Alto Networks Kerberos Server Profiles API
  phrasing_intents:
  - id: ListKerberosServerProfiles
    intent: List Kerberos server profiles
    question: Which Kerberos server profiles are configured in a folder or snippet?
  - id: CreateKerberosServerProfiles
    intent: Create a Kerberos server profile
    question: How do I add Kerberos servers for authentication?
  - id: GetKerberosServerProfilesByID
    intent: Get a Kerberos server profile
    question: Which servers does a specific Kerberos server profile use?
  - id: UpdateKerberosServerProfilesByID
    intent: Update a Kerberos server profile
    question: Can I change the servers listed in an existing Kerberos server profile?
  - id: DeleteKerberosServerProfilesByID
    intent: Delete a Kerberos server profile
    question: How do I remove a Kerberos server profile?
  - id: get-sse-config-v1-kerberos-server-profiles
    intent: List Kerberos server profiles
    question: Which Kerberos server profiles are configured for authentication?
  - id: post-sse-config-v1-kerberos-server-profiles
    intent: Create a Kerberos server profile
    question: How do I add a new Kerberos server profile pointing at my KDC servers?
  - id: delete-sse-config-v1-kerberos-server-profiles-id
    intent: Delete a Kerberos server profile
    question: How do I remove a Kerberos server profile I no longer use?
  phrasing_ops: 10
  slug: palo-alto-networks-kerberos-server-profiles-api
- baseURL: https://api.dig.security
  baseurl_source: declared
  description: '{''$ref'': ''desc/labels/labels.md''}'
  name: Palo Alto Networks Labels API
  phrasing_intents:
  - id: get-labels
    intent: List labels with a DIG API key
    question: How do I list labels using the DIG API key header on the v1 endpoint?
  - id: ListLabels
    intent: List labels
    question: What labels are defined in my configuration?
  - id: CreateLabel
    intent: Create a label
    question: How do I create a new label with a description?
  - id: GetLabelByID
    intent: Get a label
    question: What are the details of a specific label?
  - id: UpdateLabelByID
    intent: Update a label
    question: How do I rename an existing label?
  - id: DeleteLabelByID
    intent: Delete a label
    question: How do I delete a label I no longer need?
  phrasing_ops: 6
  slug: palo-alto-networks-labels-api
- baseURL: https://api.sase.paloaltonetworks.com/ai-red-teaming/data-plane
  baseurl_source: declared
  description: Operations for language configuration and multilingual support.
  name: Palo Alto Networks Languages API
  phrasing_intents:
  - id: get_languages_v1_languages_get
    intent: List languages available for red teaming scans
    question: Which languages can I run an AI red teaming scan in?
  phrasing_ops: 1
  slug: palo-alto-networks-languages-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Layer 3 Subinterfaces
  name: Palo Alto Networks Layer 2 Subinterfaces API
  phrasing_intents:
  - id: ListLayer2Subinterfaces
    intent: List layer 2 subinterfaces
    question: Which layer 2 subinterfaces are configured on my firewalls?
  - id: CreateLayer2Subinterfaces
    intent: Create a layer 2 subinterface
    question: How do I add a VLAN-tagged layer 2 subinterface?
  - id: GetLayer2SubinterfacesByID
    intent: Get a layer 2 subinterface
    question: What VLAN tag and parent does a specific L2 subinterface use?
  - id: UpdateLayer2SubinterfacesByID
    intent: Update a layer 2 subinterface
    question: How do I change the VLAN tag on an existing layer 2 subinterface?
  - id: DeleteLayer2SubinterfacesByID
    intent: Delete a layer 2 subinterface
    question: How do I remove a layer 2 subinterface?
  phrasing_ops: 5
  slug: palo-alto-networks-layer-2-subinterfaces-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Layer 3 Subinterfaces
  name: Palo Alto Networks Layer 3 Subinterfaces API
  phrasing_intents:
  - id: ListLayer3Subinterfaces
    intent: List layer 3 subinterfaces
    question: Which layer 3 subinterfaces are configured on a device?
  - id: CreateLayer3Subinterfaces
    intent: Create a layer 3 subinterface
    question: How do I add a VLAN-tagged layer 3 subinterface to a parent interface?
  - id: GetLayer3SubinterfacesByID
    intent: Get a layer 3 subinterface
    question: What tag, MTU and parent interface does a particular subinterface have?
  - id: UpdateLayer3SubinterfacesByID
    intent: Update a layer 3 subinterface
    question: Can I change the MTU on an existing layer 3 subinterface?
  - id: DeleteLayer3SubinterfacesByID
    intent: Delete a layer 3 subinterface
    question: How do I remove a layer 3 subinterface?
  phrasing_ops: 5
  slug: palo-alto-networks-layer-3-subinterfaces-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: LDAP Server Profiles
  name: Palo Alto Networks LDAP Server Profiles API
  phrasing_intents:
  - id: ListLDAPServerProfiles
    intent: List LDAP server profiles
    question: Which LDAP server profiles are configured for directory lookups?
  - id: CreateLDAPServerProfiles
    intent: Create an LDAP server profile
    question: How do I connect the firewall to my directory by adding an LDAP server profile?
  - id: GetLDAPServerProfilesByID
    intent: Get an LDAP server profile
    question: What servers and base DN does a given LDAP server profile use?
  - id: UpdateLDAPServerProfiles
    intent: Update an LDAP server profile
    question: How do I change the bind password on an existing LDAP server profile?
  - id: DeleteLDAPServerProfilesByID
    intent: Delete an LDAP server profile
    question: How do I delete an LDAP server profile?
  - id: get-sse-config-v1-ldap-server-profiles
    intent: List LDAP server profiles
    question: Which LDAP server profiles are set up in my folder?
  - id: post-sse-config-v1-ldap-server-profiles
    intent: Create an LDAP server profile
    question: How do I connect my LDAP directory by creating a server profile?
  - id: delete-sse-config-v1-ldap-server-profiles-id
    intent: Delete an LDAP server profile
    question: How do I remove an LDAP server profile?
  phrasing_ops: 10
  slug: palo-alto-networks-ldap-server-profiles-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The License Resources API API from Palo Alto Networks — 3 operation(s) for license resources api.
  name: Palo Alto Networks License Resources API
  phrasing_intents:
  - id: get-mt-monitor-v1-agg-custom-license-quota
    intent: List license quotas across tenants
    question: What license quota does each of my tenants have?
  - id: get-mt-monitor-v1-agg-custom-license-setup-status
    intent: List license setup status across tenants
    question: Has the license service been set up for all my tenants?
  - id: get-mt-monitor-v1-agg-custom-license-utilization
    intent: List license utilization across tenants
    question: How much of their Mobile Users license are my tenants consuming?
  phrasing_ops: 3
  slug: palo-alto-networks-license-resources-api-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Prisma Cloud License endpoints enable you to query your Prisma Cloud usage.
  name: Palo Alto Networks Licensing API
  phrasing_intents:
  - id: license-usage-count-by-cloud-paginated_1_1
    intent: Count resource usage for one cloud (v1, deprecated)
    question: How do I get per-account resource usage for a single cloud with the older v1 licensing API?
  - id: license-usage-graph_1
    intent: Chart resource usage over time (v1, deprecated)
    question: Can the deprecated v1 licensing API show resource usage trends over time?
  - id: license-usage-count-by-cloud-paginated
    intent: Count resource usage per account by cloud (v2)
    question: How many licensed resources is each account using across several cloud types?
  - id: license-usage-graph
    intent: Chart resource usage over time (v2)
    question: How has our licensed resource usage trended over the past quarter?
  - id: getCreditAllocationRules
    intent: List credit allocation rules with usage
    question: How many credits has each allocation rule used so far?
  - id: createCreditAllocationRule
    intent: Create a credit allocation rule
    question: How do I allocate a budget of credits to specific account groups?
  - id: getCreditAllocationRuleSummary
    intent: Summarize credit allocation rules
    question: What's the overall summary of credit allocation across all rules?
  - id: getCreditAllocationRule
    intent: Get a credit allocation rule
    question: How is a single credit allocation rule configured?
  phrasing_ops: 11
  slug: palo-alto-networks-licensing-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Link Tags
  name: Palo Alto Networks Link Tags API
  phrasing_intents:
  - id: ListLinkTags
    intent: List link tags
    question: Which link tags are defined for my SD-WAN links?
  - id: CreateLinkTags
    intent: Create a link tag
    question: How do I create a new link tag with a color?
  - id: GetLinkTagsByID
    intent: Get a link tag
    question: What color and comments does one link tag have?
  - id: UpdateLinkTagsByID
    intent: Update a link tag
    question: How do I change an existing link tag's color?
  - id: DeleteLinkTagsByID
    intent: Delete a link tag
    question: How do I remove a link tag?
  phrasing_ops: 5
  slug: palo-alto-networks-link-tags-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: LLDP Profiles
  name: Palo Alto Networks LLDP Profiles API
  phrasing_intents:
  - id: ListLLDPProfiles
    intent: List LLDP profiles
    question: Which LLDP profiles are defined in a folder?
  - id: CreateLLDPProfiles
    intent: Create an LLDP profile
    question: How do I create an LLDP profile for firewall interfaces?
  - id: GetLLDPProfilesByID
    intent: Get an LLDP profile
    question: What mode and TLVs does a specific LLDP profile use?
  - id: UpdateLLDPProfilesByID
    intent: Update an LLDP profile
    question: Can I switch an existing LLDP profile to transmit-only mode?
  - id: DeleteLLDPProfilesByID
    intent: Delete an LLDP profile
    question: How do I remove an LLDP profile?
  phrasing_ops: 5
  slug: palo-alto-networks-lldp-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: Local User Groups
  name: Palo Alto Networks Local User Groups API
  phrasing_intents:
  - id: ListLocalUserGroups
    intent: List local user groups
    question: Which local user groups are configured?
  - id: CreateLocalUserGroups
    intent: Create a local user group
    question: How do I create a local user group and add users to it?
  - id: GetLocalUserGroupsByID
    intent: Get a local user group
    question: Who is in a specific local user group?
  - id: UpdateLocalUserGroupsByID
    intent: Update a local user group
    question: How do I change the members of an existing local user group?
  - id: DeleteLocalUserGroupsByID
    intent: Delete a local user group
    question: How do I delete a local user group?
  - id: get-sse-config-v1-local-user-groups
    intent: List local user groups in a folder
    question: Which local user groups exist in a given configuration folder?
  - id: post-sse-config-v1-local-user-groups
    intent: Create a local user group
    question: How do I create a local user group inside a specific folder?
  - id: delete-sse-config-v1-local-user-groups-id
    intent: Delete a local user group
    question: How do I delete a local user group through the SSE config v1 path?
  phrasing_ops: 10
  slug: palo-alto-networks-local-user-groups-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: Local Users
  name: Palo Alto Networks Local Users API
  phrasing_intents:
  - id: ListLocalUsers
    intent: List local users
    question: Which local user accounts are configured on my firewalls?
  - id: CreateLocalUsers
    intent: Create a local user
    question: How do I add a local user account in Strata Cloud Manager?
  - id: GetLocalUsersByID
    intent: Get a local user
    question: Is a specific local user account disabled?
  - id: UpdateLocalUsersByID
    intent: Update a local user
    question: How do I reset a local user's password?
  - id: DeleteLocalUsersByID
    intent: Delete a local user
    question: How do I delete a local user account?
  - id: get-sse-config-v1-local-users
    intent: List local users
    question: Which local users are defined in a configuration folder?
  - id: post-sse-config-v1-local-users
    intent: Create a local user
    question: How do I add a local user account with a password?
  - id: delete-sse-config-v1-local-users-id
    intent: Delete a local user
    question: How do I delete a local user through the SSE config v1 API?
  phrasing_ops: 10
  slug: palo-alto-networks-local-users-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Information on the location.
  name: Palo Alto Networks Location Information API
  phrasing_intents:
  - id: get-v1-location-informations
    intent: Check a location information request
    question: Is my location information request finished yet?
  - id: post-v1-location-informations
    intent: Request location-mapped information
    question: How do I request region information mapped to locations?
  phrasing_ops: 2
  slug: palo-alto-networks-location-information-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Logical Routers
  name: Palo Alto Networks Logical Routers API
  phrasing_intents:
  - id: ListLogicalRouters
    intent: List logical routers
    question: Which logical routers are defined in a folder?
  - id: CreateLogicalRouters
    intent: Create a logical router
    question: How do I add a new logical router with its own VRFs?
  - id: GetLogicalRoutersByID
    intent: Get a logical router
    question: What VRFs does a particular logical router have?
  - id: UpdateLogicalRoutersByID
    intent: Update a logical router
    question: How do I change the VRFs on an existing logical router?
  - id: DeleteLogicalRoutersByID
    intent: Delete a logical router
    question: Is there a way to remove a logical router?
  phrasing_ops: 5
  slug: palo-alto-networks-logical-routers-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: 'For secure access to the Prisma Cloud REST API, you need a Prisma Cloud API access key. An access key includes an Access Key ID and a Secret Key. After you use Prisma Cloud to generate an access key, '
  name: Palo Alto Networks Login API
  phrasing_intents:
  - id: app-login
    intent: Log in to Prisma Cloud with an access key
    question: How do I get a JWT token for the Prisma Cloud API using an access key?
  - id: extend-session
    intent: Extend a Prisma Cloud session token
    question: Can I keep my Prisma Cloud API session alive without logging in again?
  phrasing_ops: 2
  slug: palo-alto-networks-login-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: Login Banner Settings
  name: Palo Alto Networks Login Banner Settings API
  phrasing_intents:
  - id: ListLoginBannerSettings
    intent: List login banner settings
    question: Which login banner and message-of-the-day settings are configured?
  - id: CreateLoginBannerSettings
    intent: Create login banner settings
    question: How do I set a message of the day shown when admins log in?
  - id: GetLoginBannerSettingsByID
    intent: Get login banner settings
    question: What does a particular login banner configuration say?
  - id: UpdateLoginBannerSettingsByID
    intent: Update login banner settings
    question: How do I change the text of an existing login banner?
  - id: DeleteLoginBannerSettingsByID
    intent: Delete login banner settings
    question: Which call removes a login banner configuration?
  phrasing_ops: 5
  slug: palo-alto-networks-login-banner-settings-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The LogProfile API from Palo Alto Networks — 1 operation(s) for logprofile.
  name: Palo Alto Networks Log Profile API
  phrasing_intents:
  - id: get-v1-config-ngfirewalls-ngfirewallname-logprofile
    intent: Get a cloud NGFW’s log destination
    question: Where is my cloud NGFW sending its logs?
  - id: put-v1-config-ngfirewalls-ngfirewallname-logprofile
    intent: Change a cloud NGFW’s log destination
    question: Can I change the log destination on a cloud NGFW without a commit?
  phrasing_ops: 2
  slug: palo-alto-networks-logprofile-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Loopback Interfaces
  name: Palo Alto Networks Loopback Interfaces API
  phrasing_intents:
  - id: ListLoopbackInterfaces
    intent: List loopback interfaces
    question: What loopback interfaces are configured on my firewalls?
  - id: CreateLoopbackInterfaces
    intent: Create a loopback interface
    question: How do I add a loopback interface with an IP address?
  - id: GetLoopbackInterfacesByID
    intent: Get a loopback interface
    question: What IP addresses are assigned to a particular loopback interface?
  - id: UpdateLoopbackInterfacesByID
    intent: Update a loopback interface
    question: Can I change the IP on an existing loopback interface?
  - id: DeleteLoopbackInterfacesByID
    intent: Delete a loopback interface
    question: Can I delete a loopback interface?
  phrasing_ops: 5
  slug: palo-alto-networks-loopback-interfaces-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Machine Installations.
  name: Palo Alto Networks Machine Installations API
  phrasing_intents:
  - id: machineidentities_getAll
    intent: List all machine identities
    question: Which machine identities are installed across my machines?
  - id: machineidentities_create
    intent: Install a certificate on a machine
    question: How do I add a machine identity that binds a certificate to a machine?
  - id: machineidentities_getById
    intent: Get a machine identity
    question: What certificate and binding does a particular machine identity have?
  - id: machineidentities_delete
    intent: Remove a machine identity
    question: How do I remove a machine identity I no longer need?
  - id: machineidentities_update
    intent: Update a machine identity
    question: Can I swap the certificate on an existing machine identity?
  - id: machineidentities_initiateWorkflow
    intent: Run a workflow on a machine identity
    question: Can I test the connection for a machine identity?
  - id: getMachineIdentitiesByExpression
    intent: Search machine identities by expression
    question: How do I search machine identities with a filter expression?
  phrasing_ops: 7
  slug: palo-alto-networks-machine-installations-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Machine Types.
  name: Palo Alto Networks Machine Types API
  phrasing_intents:
  - id: machineTypes_getAll
    intent: List machine types (deprecated)
    question: What machine types were available in the deprecated machine types endpoint?
  phrasing_ops: 1
  slug: palo-alto-networks-machine-types-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Machines.
  name: Palo Alto Networks Machines API
  phrasing_intents:
  - id: machines_getAll
    intent: List all machines
    question: Which machines are registered for certificate provisioning?
  - id: machines_create
    intent: Add a machine
    question: How do I register a new machine with a plugin and connection details?
  - id: machines_getById
    intent: Get a machine's details
    question: What are the connection details and status of one machine?
  - id: machines_delete
    intent: Delete a machine
    question: How do I remove a machine from the inventory?
  - id: machines_update
    intent: Update a machine's settings
    question: Can I turn on scheduled discovery for an existing machine?
  - id: machines_initiateWorkflow
    intent: Start a workflow on a machine
    question: How do I kick off a named workflow on a machine?
  - id: getMachinesByExpression
    intent: Search machines by expression
    question: Can I find machines that match a search expression, with paging and ordering?
  - id: abort-v1-batchprovisionings-forMachineId
    intent: Abort a machine's batch provisioning
    question: How do I stop a batch provisioning run that is in progress on a machine?
  phrasing_ops: 10
  slug: palo-alto-networks-machines-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The ManageCustomURLCategories API from Palo Alto Networks — 2 operation(s) for managecustomurlcategories.
  name: Palo Alto Networks Manage Custom URL Categories API
  phrasing_intents:
  - id: get-v1-config-rulestacks-rulestackname-urlcustomcategories
    intent: List custom URL categories in a rulestack
    question: Which custom URL categories are defined in a cloud NGFW rulestack?
  - id: post-v1-config-rulestacks-rulestackname-urlcustomcategories
    intent: Create a custom URL category
    question: How do I create a custom URL category to allow exceptions to URL filtering?
  - id: delete-v1-config-rulestacks-rulestackname-urlcustomcategories-name
    intent: Delete a custom URL category
    question: How do I delete a custom URL category from a rulestack?
  - id: get-v1-config-rulestacks-rulestackname-urlcustomcategories-name
    intent: Get a custom URL category
    question: What URLs and action are set on a specific custom URL category?
  - id: put-v1-config-rulestacks-rulestackname-urlcustomcategories-name
    intent: Update a custom URL category
    question: How do I change the URLs in an existing custom URL category?
  phrasing_ops: 5
  slug: palo-alto-networks-managecustomurlcategories-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: Management Interface Settings
  name: Palo Alto Networks Management Interface Settings API
  phrasing_intents:
  - id: ListManagementInterfaceSettings
    intent: List management interface settings
    question: What management interface settings are defined in Strata Cloud Manager?
  - id: CreateManagementInterfaceSettings
    intent: Create management interface settings
    question: How do I define new management interface settings for my firewalls in Strata Cloud Manager?
  - id: GetManagementInterfaceSettingsByID
    intent: Get management interface settings by ID
    question: How do I look up one management interface settings resource by its UUID?
  - id: UpdateManagementInterfaceSettingsByID
    intent: Update management interface settings
    question: Can I change an existing management interface settings resource in place?
  - id: DeleteManagementInterfaceSettingsByID
    intent: Delete management interface settings
    question: How do I remove a management interface settings resource I no longer need?
  phrasing_ops: 5
  slug: palo-alto-networks-management-interface-settings-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The ManageNGFW API from Palo Alto Networks — 4 operation(s) for managengfw.
  name: Palo Alto Networks Manage NGFW API
  phrasing_intents:
  - id: get-v1-config-ngfirewalls
    intent: List cloud NGFW firewalls
    question: Which Cloud NGFW firewalls are deployed in my account?
  - id: post-v1-config-ngfirewalls
    intent: Create a cloud NGFW firewall
    question: How do I deploy a new Cloud NGFW firewall into my VPC?
  - id: delete-v1-config-ngfirewalls-ngfirewallname
    intent: Delete a cloud NGFW firewall
    question: How do I tear down an NGFW firewall safely?
  - id: get-v1-config-ngfirewalls-ngfirewallname
    intent: Get a cloud NGFW firewall
    question: What is the configuration of one of my NGFW firewalls?
  - id: put-v1-config-ngfirewalls-ngfirewallname-description
    intent: Update a firewall's description
    question: How do I change the description on an NGFW firewall?
  - id: put-v1-config-ngfirewalls-ngfirewallname-subnets
    intent: Change a firewall's subnet mappings
    question: How do I add a subnet to an existing NGFW firewall?
  phrasing_ops: 6
  slug: palo-alto-networks-managengfw-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The ManageNGFW-V2 API from Palo Alto Networks — 15 operation(s) for managengfw-v2.
  name: Palo Alto Networks Manage NGFW V2 API
  phrasing_intents:
  - id: delete-v2-linkaccounts
    intent: Unlink an AWS account from Cloud NGFW
    question: Can I remove a linked AWS account from Cloud NGFW?
  - id: get-v2-linkaccounts
    intent: List linked AWS accounts for Cloud NGFW
    question: Which AWS accounts are linked to my Cloud NGFW tenant?
  - id: post-v2-linkaccounts
    intent: Link an AWS account to Cloud NGFW
    question: How do I onboard a new AWS account into Cloud NGFW?
  - id: get-v2-ngfirewalls-v2
    intent: List Cloud NGFW firewalls in a region
    question: Which Cloud NGFW firewalls do I have running in a given AWS region?
  - id: post-v2-ngfirewalls-v2
    intent: Create a Cloud NGFW firewall
    question: How do I deploy a new Cloud NGFW firewall across availability zones?
  - id: get-v2-ngfirewalls-v1
    intent: List legacy V1 firewalls via the V2 endpoint
    question: Can I still list my older V1-style firewalls through the V2 API?
  - id: post-v2-ngfirewalls-v1
    intent: Create a legacy V1 firewall in a VPC
    question: What does it take to create a V1-style firewall tied to a VPC and subnet mappings?
  - id: delete-v2-ngfirewalls-firewall_id
    intent: Delete a firewall by its ID
    question: What is the call to tear down a Cloud NGFW firewall using its firewall ID?
  phrasing_ops: 28
  slug: palo-alto-networks-managengfw-v2-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The ManageNGFWTags API from Palo Alto Networks — 1 operation(s) for managengfwtags.
  name: Palo Alto Networks Manage NGFW Tags API
  phrasing_intents:
  - id: delete-v1-config-ngfirewalls-ngfirewallname-tags
    intent: Remove tags from a Cloud NGFW firewall
    question: How do I remove specific tags from a Cloud NGFW firewall?
  - id: get-v1-config-ngfirewalls-ngfirewallname-tags
    intent: List tags on a Cloud NGFW firewall
    question: Which tags are attached to my Cloud NGFW firewall?
  - id: post-v1-config-ngfirewalls-ngfirewallname-tags
    intent: Add tags to a Cloud NGFW firewall
    question: How do I tag a Cloud NGFW firewall for cost tracking or ownership?
  phrasing_ops: 3
  slug: palo-alto-networks-managengfwtags-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The ManagePredefinedURLCategories API from Palo Alto Networks — 1 operation(s) for managepredefinedurlcategories.
  name: Palo Alto Networks Manage Predefined URL Categories API
  phrasing_intents:
  - id: get-v1-config-urlcategories
    intent: List predefined URL categories
    question: What predefined URL categories can I use in Cloud NGFW rules?
  phrasing_ops: 1
  slug: palo-alto-networks-managepredefinedurlcategories-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The ManagePrefixLists API from Palo Alto Networks — 2 operation(s) for manageprefixlists.
  name: Palo Alto Networks Manage Prefix Lists API
  phrasing_intents:
  - id: get-v1-config-rulestacks-rulestackname-prefixlists
    intent: List prefix lists in a rulestack
    question: Which prefix lists are defined on a Cloud NGFW rulestack?
  - id: post-v1-config-rulestacks-rulestackname-prefixlists
    intent: Create a prefix list in a rulestack
    question: How do I add a set of CIDR prefixes to a rulestack for rules to reference?
  - id: delete-v1-config-rulestacks-rulestackname-prefixlists-name
    intent: Delete a prefix list from a rulestack
    question: How do I remove a prefix list from a rulestack?
  - id: get-v1-config-rulestacks-rulestackname-prefixlists-name
    intent: Describe one prefix list
    question: What CIDRs are in a specific prefix list on my rulestack?
  - id: put-v1-config-rulestacks-rulestackname-prefixlists-name
    intent: Update a prefix list's prefixes
    question: Can I replace the CIDRs in an existing prefix list?
  phrasing_ops: 5
  slug: palo-alto-networks-manageprefixlists-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The ManageRulestacks API from Palo Alto Networks — 5 operation(s) for managerulestacks.
  name: Palo Alto Networks Manage Rulestacks API
  phrasing_intents:
  - id: get-v1-config-rulestacks
    intent: List rulestacks
    question: Which rulestacks exist for my Cloud NGFW, global and local?
  - id: post-v1-config-rulestacks
    intent: Create a rulestack
    question: How do I create a new global or local rulestack for Cloud NGFW?
  - id: delete-v1-config-rulestacks-rulestackname
    intent: Delete a rulestack
    question: How do I remove a rulestack I no longer use?
  - id: get-v1-config-rulestacks-rulestackname
    intent: Get a rulestack's configuration
    question: What is configured in a particular rulestack?
  - id: put-v1-config-rulestacks-rulestackname
    intent: Update a rulestack's configuration
    question: Can I change a rulestack's settings after it is created?
  - id: get-v1-config-rulestacks-rulestackname-commit
    intent: Check a rulestack's commit status
    question: Has my last rulestack commit succeeded?
  - id: post-v1-config-rulestacks-rulestackname-commit
    intent: Commit rulestack changes
    question: How do I push my pending rulestack edits live?
  - id: post-v1-config-rulestacks-rulestackname-revert
    intent: Discard uncommitted rulestack changes
    question: Can I throw away the edits I haven't committed on a rulestack?
  phrasing_ops: 9
  slug: palo-alto-networks-managerulestacks-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The ManageRulestackTags API from Palo Alto Networks — 1 operation(s) for managerulestacktags.
  name: Palo Alto Networks Manage Rulestack Tags API
  phrasing_intents:
  - id: delete-v1-config-rulestacks-rulestackname-tags
    intent: Remove tags from a rulestack
    question: How do I remove specific tag keys from a rulestack?
  - id: get-v1-config-rulestacks-rulestackname-tags
    intent: List tags on a rulestack
    question: What tags are applied to a Cloud NGFW rulestack?
  - id: post-v1-config-rulestacks-rulestackname-tags
    intent: Add tags to a rulestack
    question: How do I tag a rulestack for cost tracking or ownership?
  phrasing_ops: 3
  slug: palo-alto-networks-managerulestacktags-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The ManageSecurityRules API from Palo Alto Networks — 2 operation(s) for managesecurityrules.
  name: Palo Alto Networks Manage Security Rules API
  phrasing_intents:
  - id: get-v1-config-rulestacks-rulestackname-rulelists-rulelistname
    intent: List security rules in a rulestack
    question: What security rules are in my Cloud NGFW rulestack, in priority order?
  - id: post-v1-config-rulestacks-rulestackname-rulelists-rulelistname
    intent: Create a security rule in a rulestack
    question: How do I add a new security rule to a Cloud NGFW rulestack?
  - id: delete-v1-config-rulestacks-rulestackname-rulelists-rulelistname-priorities-priority
    intent: Delete a security rule at a priority
    question: How do I remove a security rule from a Cloud NGFW rulestack?
  - id: get-v1-config-rulestacks-rulestackname-rulelists-rulelistname-priorities-priority
    intent: Describe a security rule at a priority
    question: What does the rule at a specific priority in my rulestack do?
  - id: put-v1-config-rulestacks-rulestackname-rulelists-rulelistname-priorities-priority
    intent: Update a security rule at a priority
    question: How do I change an existing security rule in a Cloud NGFW rulestack?
  phrasing_ops: 5
  slug: palo-alto-networks-managesecurityrules-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The ManageSubscription API from Palo Alto Networks — 1 operation(s) for managesubscription.
  name: Palo Alto Networks Manage Subscription API
  phrasing_intents:
  - id: get-v1-mgmt-subscribe
    intent: List Cloud NGFW subscriptions
    question: Which Cloud NGFW subscriptions does my account have?
  phrasing_ops: 1
  slug: palo-alto-networks-managesubscription-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: MFA Servers
  name: Palo Alto Networks MFA Servers API
  phrasing_intents:
  - id: ListMFAServers
    intent: List MFA server profiles
    question: Which MFA server profiles are configured in Strata Cloud Manager?
  - id: CreateMFAServers
    intent: Create an MFA server profile
    question: How do I connect an MFA vendor to Strata Cloud Manager?
  - id: GetMFAServersByID
    intent: Get an MFA server profile
    question: Where can I see one MFA server profile?
  - id: UpdateMFAServersByID
    intent: Update an MFA server profile
    question: How do I switch an MFA server to a different certificate profile?
  - id: DeleteMFAServersByID
    intent: Delete an MFA server profile
    question: Can I remove an MFA server profile?
  - id: get-sse-config-v1-mfa-servers
    intent: List MFA servers in a folder
    question: Which multi-factor authentication servers are configured in a folder?
  - id: post-sse-config-v1-mfa-servers
    intent: Create an MFA server
    question: How do I add a multi-factor authentication server?
  - id: delete-sse-config-v1-mfa-servers-id
    intent: Delete an MFA server
    question: How do I remove an MFA server?
  phrasing_ops: 10
  slug: palo-alto-networks-mfa-servers-api
- baseURL: https://api.strata.paloaltonetworks.com
  baseurl_source: declared
  description: The Misconfigured Domains API from Palo Alto Networks — 2 operation(s) for misconfigured domains.
  name: Palo Alto Networks Misconfigured Domains API
  phrasing_intents:
  - id: ListMisconfiguredDomains
    intent: List misconfigured domains
    question: Which domains are flagged as misconfigured in the DNS resolver?
  - id: CreateMisconfiguredDomain
    intent: Add a misconfigured domain
    question: How do I flag a domain as misconfigured?
  - id: DeleteMisconfiguredDomainByID
    intent: Delete a misconfigured domain entry
    question: How do I unflag a domain that's no longer misconfigured?
  - id: GetMisconfiguredDomainByID
    intent: Get a misconfigured domain entry
    question: What are the details of one misconfigured domain entry?
  - id: UpdateMisconfiguredDomainByID
    intent: Update a misconfigured domain entry
    question: How do I correct the domain name on an existing misconfigured entry?
  phrasing_ops: 5
  slug: palo-alto-networks-misconfigured-domains-api
- baseURL: https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
  baseurl_source: declared
  description: Mobile User Locations
  name: Palo Alto Networks Mobile User Locations API
  phrasing_intents:
  - id: ListGlobalProtectLocations
    intent: List GlobalProtect mobile user locations
    question: Which GlobalProtect locations are available for mobile users?
  - id: UpdateGlobalProtectLocations
    intent: Select a GlobalProtect location
    question: How do I enable a new GlobalProtect location for remote users?
  phrasing_ops: 2
  slug: palo-alto-networks-mobile-user-locations-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Endpoint to retrieve the device count histogram with possible filters.
  name: Palo Alto Networks Monitored Users API
  phrasing_intents:
  - id: post-insights-v3.0-resource-query-user-monitored-user_count
    intent: Count monitored users
    question: How many users are currently being monitored in my Prisma Access tenant?
  - id: post-insights-v3.0-resource-query-user-monitored-user_count_histogram
    intent: Get a histogram of monitored users
    question: How has the number of monitored users changed over time?
  - id: post-insights-v3.0-resource-query-users-monitored-device_count
    intent: Count monitored devices
    question: How many devices belonging to monitored users are being tracked?
  - id: post-insights-v3.0-resource-query-users-monitored-device_count_histogram
    intent: Get a histogram of monitored devices
    question: What does the trend of monitored device counts look like over time?
  - id: post-insights-v3.0-resource-query-users-monitored-user_experience_score
    intent: Get user experience scores
    question: What experience scores are my monitored users getting?
  phrasing_ops: 5
  slug: palo-alto-networks-monitored-users-api-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: NAT Rules
  name: Palo Alto Networks NAT Rules API
  phrasing_intents:
  - id: ListNatRules
    intent: List NAT rules
    question: Which NAT rules are in the pre-rulebase of a folder?
  - id: CreateNatRules
    intent: Create a NAT rule
    question: How do I create a NAT rule that translates source addresses?
  - id: GetNatRulesByID
    intent: Get a NAT rule
    question: What translation does one NAT rule perform?
  - id: UpdateNatRulesByID
    intent: Update a NAT rule
    question: How do I disable an existing NAT rule without deleting it?
  - id: DeleteNatRulesByID
    intent: Delete a NAT rule
    question: How do I delete a NAT rule?
  - id: listNatRules
    intent: List Prisma Access NAT rules
    question: Which NAT rules are configured in a Prisma Access folder or snippet?
  - id: createNatRule
    intent: Create a Prisma Access NAT rule
    question: How do I add a NAT rule to a Prisma Access folder?
  phrasing_ops: 7
  slug: palo-alto-networks-nat-rules-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The NavController API from Palo Alto Networks — 1 operation(s) for navcontroller.
  name: Palo Alto Networks Nav Controller API
  phrasing_intents:
  - id: NavController.getNavTraffic
    intent: Get ADEM traffic telemetry
    question: What does traffic look like for my tenant in ADEM telemetry?
  phrasing_ops: 1
  slug: palo-alto-networks-navcontroller-api
- baseURL: https://api.strata.paloaltonetworks.com/config/deployment/v1
  baseurl_source: declared
  description: Prisma Access locations
  name: Palo Alto Networks Network Locations API
  phrasing_intents:
  - id: ListLocations
    intent: List Prisma Access locations
    question: Which Prisma Access locations are available?
  phrasing_ops: 1
  slug: palo-alto-networks-network-locations-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Network Packet Broker Profile management
  name: Palo Alto Networks Network Packet Broker Profiles API
  phrasing_intents:
  - id: ListNetworkPacketBrokerProfiles
    intent: List network packet broker profiles
    question: Which network packet broker profiles are defined in my configuration?
  - id: CreateNetworkPacketBrokerProfiles
    intent: Create a network packet broker profile
    question: How do I set up a packet broker profile to forward traffic to a security chain?
  - id: GetNetworkPacketBrokerProfilesByID
    intent: Get a network packet broker profile
    question: Which interfaces does a specific packet broker profile use?
  - id: UpdateNetworkPacketBrokerProfilesByID
    intent: Update a network packet broker profile
    question: Can I change the secondary interface on an existing packet broker profile?
  - id: DeleteNetworkPacketBrokerProfilesByID
    intent: Delete a network packet broker profile
    question: Can I remove a packet broker profile we stopped using?
  phrasing_ops: 5
  slug: palo-alto-networks-network-packet-broker-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Network Packet Broker Rule management
  name: Palo Alto Networks Network Packet Broker Rules API
  phrasing_intents:
  - id: ListNetworkPacketBrokerRules
    intent: List Network Packet Broker rules
    question: Which Network Packet Broker rules are configured in a folder?
  - id: CreateNetworkPacketBrokerRules
    intent: Create a Network Packet Broker rule
    question: How do I create a packet broker rule that forwards traffic between specific zones?
  - id: GetNetworkPacketBrokerRulesByID
    intent: Get a Network Packet Broker rule
    question: What zones and action does a specific packet broker rule use?
  - id: UpdateNetworkPacketBrokerRulesByID
    intent: Update a Network Packet Broker rule
    question: Can I disable an existing packet broker rule without deleting it?
  - id: DeleteNetworkPacketBrokerRulesByID
    intent: Delete a Network Packet Broker rule
    question: Can I permanently remove a Network Packet Broker rule?
  phrasing_ops: 5
  slug: palo-alto-networks-network-packet-broker-rules-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: 'Notification templates allow you to configure notifications about the Prisma Cloud alerts to: * Email * ServiceNow * Jira'
  name: Palo Alto Networks Notification Templates API
  phrasing_intents:
  - id: get-all-templates-v1
    intent: List notification templates
    question: Which notification templates exist in my Prisma Cloud tenant?
  - id: create-template-v1
    intent: Create a notification template
    question: How do I create a notification template for one of my alert integrations?
  - id: get-template-v1
    intent: Get a notification template
    question: How do I view the configuration of one notification template?
  - id: update-template-v1
    intent: Update a notification template
    question: How do I rename or disable an existing notification template?
  - id: delete-template-v1
    intent: Delete a notification template
    question: How do I delete a notification template I no longer use?
  - id: test-template-v1
    intent: Test a notification template
    question: Can I send a test notification to check a template before saving it?
  phrasing_ops: 6
  slug: palo-alto-networks-notification-templates-api
- baseURL: https://api.sase.paloaltonetworks.com/aisec
  baseurl_source: declared
  description: Operations related to OAuth tokens
  name: Palo Alto Networks OAUTH API
  phrasing_intents:
  - id: GetApigeeOauthToken
    intent: Get an OAuth token for a customer app
    question: What do I send to get an OAuth token for my customer app's client credentials?
  phrasing_ops: 1
  slug: palo-alto-networks-oauth-api
- baseURL: https://api.dlp.paloaltonetworks.com
  baseurl_source: declared
  description: The OCR Enablement API from Palo Alto Networks — 1 operation(s) for ocr enablement.
  name: Palo Alto Networks OCR Enablement API
  phrasing_intents:
  - id: get-v2-api-ocr
    intent: Get OCR enablement settings
    question: Is OCR turned on for DLP scanning of images?
  - id: put-v2-api-ocr
    intent: Turn OCR on or off for a service
    question: How do I enable OCR for a specific service?
  phrasing_ops: 2
  slug: palo-alto-networks-ocr-enablement-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: OCSP Responders
  name: Palo Alto Networks OCSP Responders API
  phrasing_intents:
  - id: ListOCSPResponders
    intent: List OCSP responders
    question: Which OCSP responders are configured for certificate revocation checks?
  - id: CreateOCSPResponders
    intent: Create an OCSP responder
    question: How do I add an OCSP responder host for checking certificate status?
  - id: GetOCSPRespondersByID
    intent: Get an OCSP responder
    question: What host name does a given OCSP responder use?
  - id: UpdateOCSPRespondersByID
    intent: Update an OCSP responder
    question: Can I point an existing OCSP responder at a new host?
  - id: DeleteOCSPRespondersByID
    intent: Delete an OCSP responder
    question: How do I remove an OCSP responder I no longer use?
  phrasing_ops: 5
  slug: palo-alto-networks-ocsp-responders-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The OCSPResponder API from Palo Alto Networks — 2 operation(s) for ocspresponder.
  name: Palo Alto Networks OCSP Responder API
  phrasing_intents:
  - id: get-sse-config-v1-ocsp-responder
    intent: List OCSP responders
    question: Which OCSP responders are configured for certificate revocation checks?
  - id: post-sse-config-v1-ocsp-responder
    intent: Create an OCSP responder
    question: How do I add a new OCSP responder hostname for checking certificate status?
  - id: delete-sse-config-v1-ocsp-responder-id
    intent: Delete an OCSP responder
    question: How do I remove an OCSP responder that's no longer in service?
  - id: get-sse-config-v1-ocsp-responder-id
    intent: Get an OCSP responder by ID
    question: What hostname is a specific OCSP responder using?
  - id: put-sse-config-v1-ocsp-responder-id
    intent: Edit an OCSP responder
    question: How do I change the hostname of an OCSP responder I already set up?
  phrasing_ops: 5
  slug: palo-alto-networks-ocspresponder-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: You can use the AWS S3 Flow Logs API for AWS S3 onboarding for organization and standalone accounts on all supported stacks.
  name: Palo Alto Networks Onboarding AWS S3 Flow Logs API
  phrasing_intents:
  - id: get-aws-s3-flowlog
    intent: Get AWS S3 flow log settings for an account
    question: Which S3 buckets is a monitored AWS account using for VPC flow logs?
  - id: save-aws-s3-flowlog
    intent: Save AWS S3 flow log settings
    question: How do I tell Prisma Cloud which S3 buckets hold my AWS flow logs?
  - id: check-aws-s3-flowlog
    intent: Check AWS S3 flow log ingestion status
    question: Are my S3 flow log buckets set up correctly for a monitored AWS account?
  phrasing_ops: 3
  slug: palo-alto-networks-onboarding-aws-s3-flow-logs-api
- baseURL: https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1
  baseurl_source: declared
  description: Onboarding rules information
  name: Palo Alto Networks Onboarding Rules API
  phrasing_intents:
  - id: createOnboardingRule
    intent: Create an onboarding rule
    question: How do I automatically onboard devices that match certain criteria?
  - id: listOnboardingRules
    intent: List onboarding rules by priority
    question: Which onboarding rules are configured and in what order are they evaluated?
  - id: moveOnboardingRuleByID
    intent: Reorder an onboarding rule
    question: Can I move an onboarding rule to the top of the list?
  - id: getOnboardingRuleByID
    intent: Get an onboarding rule
    question: What match criteria and actions does one onboarding rule use?
  - id: updateOnboardingRuleByID
    intent: Update an onboarding rule
    question: How do I change the actions an existing onboarding rule performs?
  - id: deleteOnboardingRuleByID
    intent: Delete an onboarding rule
    question: Can I get rid of an onboarding rule?
  phrasing_ops: 6
  slug: palo-alto-networks-onboarding-rules-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: OSPF Authentication Profiles
  name: Palo Alto Networks OSPF Authentication Profiles API
  phrasing_intents:
  - id: ListOSPFAuthenticationProfiles
    intent: List OSPF authentication profiles
    question: Which OSPF authentication profiles are defined?
  - id: CreateOSPFAuthenticationProfiles
    intent: Create an OSPF authentication profile
    question: How do I add a new OSPF authentication profile?
  - id: GetOSPFAuthenticationProfilesByID
    intent: Get an OSPF authentication profile
    question: What does a specific OSPF authentication profile contain?
  - id: UpdateOSPFAuthenticationProfilesByID
    intent: Update an OSPF authentication profile
    question: How do I rename an existing OSPF authentication profile?
  - id: DeleteOSPFAuthenticationProfilesByID
    intent: Delete an OSPF authentication profile
    question: How do I remove an OSPF authentication profile?
  phrasing_ops: 5
  slug: palo-alto-networks-ospf-authentication-profiles-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Endpoint to retrieve the count of active users based on specified filters.
  name: Palo Alto Networks Other Users API
  phrasing_intents:
  - id: post-insights-v3.0-resource-query-other-risky_user_count
    intent: Count risky users
    question: How many risky users does Prisma Access see right now?
  - id: post-insights-v3.0-resource-query-users-other-active_user_count
    intent: Count active users
    question: What is the total number of active users connected at the moment?
  - id: post-insights-v3.0-resource-query-users-other-active_user_list
    intent: List active users with connection details
    question: Which users are active and how are they connected?
  - id: post-insights-v3.0-resource-query-users-other-session_list
    intent: List user sessions
    question: What sessions have users opened through Prisma Access?
  - id: post-insights-v3.0-resource-query-users-other-user_count_histogram
    intent: Get user count over time
    question: How has the number of users changed over time as a histogram?
  - id: post-insights-v3.0-resource-query-users-other-user_list
    intent: List internal users
    question: Who are the internal users seen by Prisma Access Insights?
  phrasing_ops: 6
  slug: palo-alto-networks-other-users-api-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Packages API from Palo Alto Networks — 5 operation(s) for packages.
  name: Palo Alto Networks Packages API
  phrasing_intents:
  - id: getPackagesByFile
    intent: List packages declared in a file
    question: Which open source packages come from a specific manifest file in my repo?
  - id: getDirectSubDependenciesByUuid
    intent: List a package's direct sub-dependencies
    question: What packages does a given dependency pull in directly?
  - id: getPackageByUuid
    intent: Get a package
    question: What do we know about one specific package in our code scans?
  - id: searchPackages
    intent: Search packages across repositories
    question: Which repositories use a package whose name matches a search term?
  - id: getCvesByPackageUuid
    intent: List CVEs affecting a package
    question: Which CVEs affect a specific package in my codebase?
  phrasing_ops: 5
  slug: palo-alto-networks-packages-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The PackagesAlerts API from Palo Alto Networks — 3 operation(s) for packagesalerts.
  name: Palo Alto Networks Packages Alerts API
  phrasing_intents:
  - id: getAffectedResourcesByLicenses
    intent: Find resources affected by license alerts
    question: Which resources would be affected if I suppress alerts for certain license types?
  - id: getAffectedResourcesByPackages
    intent: Find resources affected by package alerts
    question: Which resources use a package whose alerts I want to suppress?
  - id: getAffectedResourcesByPolicy
    intent: Find resources affected by a policy's alerts
    question: Which resources are flagged by a given policy before I suppress it?
  phrasing_ops: 3
  slug: palo-alto-networks-packagesalerts-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: PBF Rules
  name: Palo Alto Networks PBF Rules API
  phrasing_intents:
  - id: ListPBFRules
    intent: List policy-based forwarding rules
    question: Which policy-based forwarding rules are set up in a folder?
  - id: CreatePBFRules
    intent: Create a policy-based forwarding rule
    question: How do I route traffic for a specific application out a different path with a PBF rule?
  - id: GetPBFRulesByID
    intent: Get a policy-based forwarding rule
    question: What source, destination and forwarding action does one PBF rule use?
  - id: UpdatePBFRulesByID
    intent: Update a policy-based forwarding rule
    question: How do I change the forwarding action of an existing PBF rule?
  - id: DeletePBFRulesByID
    intent: Delete a policy-based forwarding rule
    question: How do I delete a PBF rule?
  phrasing_ops: 5
  slug: palo-alto-networks-pbf-rules-api
- baseURL: https://api.dlp.paloaltonetworks.com
  baseurl_source: declared
  description: The Peripherals API from Palo Alto Networks — 2 operation(s) for peripherals.
  name: Palo Alto Networks Peripherals API
  phrasing_intents:
  - id: get-v2-api-peripherals
    intent: List peripheral devices
    question: Which peripheral devices are registered for my tenant?
  - id: post-v2-api-peripherals
    intent: Create a peripheral device
    question: How do I register a new peripheral device?
  - id: delete-v2-api-peripherals-resourceid
    intent: Delete a peripheral device
    question: How do I remove a peripheral device?
  - id: get-v2-api-peripherals-resourceid
    intent: Get a peripheral device
    question: What are the details of one peripheral device?
  - id: put-v2-api-peripherals-resourceid
    intent: Replace a peripheral device
    question: Can I change an existing peripheral's type?
  phrasing_ops: 5
  slug: palo-alto-networks-peripherals-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: 'Permission groups enable you to restrict access to one or more features available on the Prisma Cloud administrative console. Permission group APIs allow you to retrieve, update or delete one or more '
  name: Palo Alto Networks Permission Groups API
  phrasing_intents:
  - id: getFeatures
    intent: List features for custom permission groups
    question: Which Prisma Cloud features can I grant in a custom permission group?
  - id: get_1
    intent: Get a permission group by ID
    question: What features and permissions does a specific permission group grant?
  - id: update_1
    intent: Update a permission group
    question: Can I add another feature to an existing permission group?
  - id: delete
    intent: Delete a permission group
    question: How do I delete a custom permission group?
  - id: getAll
    intent: List all permission groups
    question: What permission groups exist in my Prisma Cloud tenant?
  - id: save
    intent: Create a custom permission group
    question: How do I create a custom permission group that limits console access?
  phrasing_ops: 6
  slug: palo-alto-networks-permission-groups-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Permissions API from Palo Alto Networks — 2 operation(s) for permissions.
  name: Palo Alto Networks Permissions API
  phrasing_intents:
  - id: get-iam-v1-permissions
    intent: List access permissions
    question: What IAM permissions exist in the Palo Alto Networks platform?
  - id: get-iam-v1-permissions-name
    intent: Get a permission
    question: What does a specific service.resource.action permission grant?
  phrasing_ops: 2
  slug: palo-alto-networks-permissions-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/_ping/_ping.md''}'
  name: Palo Alto Networks Ping API
  phrasing_intents:
  - id: get-_ping
    intent: Check the Console is reachable (v34.03)
    question: How do I check the Console is up using the v34.03 ping?
  - id: getApiV3404Ping
    intent: Check the Console is reachable (v34.04)
    question: Is the Console responding on the current v34.04 API?
  phrasing_ops: 2
  slug: palo-alto-networks-ping-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The plugin API from Palo Alto Networks — 5 operation(s) for plugin.
  name: Palo Alto Networks Plugin API
  phrasing_intents:
  - id: getPluginUsersByFilter
    intent: List third-party plugin users
    question: Which users in my SaaS apps have installed third-party plugins?
  - id: getPluginsForUser
    intent: List plugins a user has installed
    question: What third-party plugins has a specific user installed?
  - id: getPluginsByFilter
    intent: List third-party plugins
    question: Which third-party plugins are present across my SaaS apps?
  - id: getPlugin
    intent: Get details on a plugin
    question: What do we know about a specific third-party plugin?
  - id: getClassificationStatusAggregates
    intent: Summarize plugins by classification status
    question: How many plugins fall into each classification status?
  phrasing_ops: 5
  slug: palo-alto-networks-plugin-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The Plugins API from Palo Alto Networks — 2 operation(s) for plugins.
  name: Palo Alto Networks Plugins API
  phrasing_intents:
  - id: GetSeb-apiV1ApplicationsPlugins
    intent: List all application plugins
    question: Which plugins are configured across all browser applications?
  - id: GetSeb-apiV1ApplicationsBy_idPlugins
    intent: Get an application's plugin
    question: What plugin is configured for a specific application?
  - id: PostSeb-apiV1ApplicationsBy_idPlugins
    intent: Add a plugin to an application
    question: How do I attach a new plugin to an application?
  - id: PutSeb-apiV1ApplicationsBy_idPlugins
    intent: Update an application's plugin
    question: Can I change the plugin settings on an application that already has one?
  - id: DeleteSeb-apiV1ApplicationsBy_idPlugins
    intent: Remove an application's plugin
    question: How do I remove the plugin from an application?
  phrasing_ops: 5
  slug: palo-alto-networks-plugins-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Plugins (Connectors).
  name: Palo Alto Networks Plugins (Connectors) API
  phrasing_intents:
  - id: get-v1-plugins
    intent: List plugins for the tenant
    question: Which plugins and connectors are available in my tenant?
  - id: post-v1-plugins
    intent: Create a custom tenant plugin
    question: How do I add my own custom plugin for exclusive use in my tenant?
  - id: get-v1-plugins-id
    intent: Get a plugin
    question: How do I look up the details of one plugin?
  - id: patch-v1-plugins-id
    intent: Update a custom tenant plugin
    question: How do I change the manifest or image of a local plugin?
  - id: delete-v1-plugins-id
    intent: Delete a custom tenant plugin
    question: Can I permanently delete a local plugin my tenant owns?
  - id: post-v1-plugins-id-exclusions
    intent: Disable a plugin for the tenant
    question: How do I turn off a plugin without deleting it?
  - id: delete-v1-plugins-id-exclusions
    intent: Re-enable a disabled plugin
    question: How do I turn a disabled plugin back on?
  - id: get-v1-plugins-exclusions
    intent: List disabled plugins
    question: Which plugins are currently disabled in my tenant?
  phrasing_ops: 8
  slug: palo-alto-networks-plugins-connectors-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: A policy is a set of one or more constraints or conditions that must be adhered to. Prisma Cloud provides predefined policies for configurations and access controls that adhere to established security
  name: Palo Alto Networks Policy API
  phrasing_intents:
  - id: get-policy-filters-and-options
    intent: List supported policy filters and default options
    question: Which filters can I use when listing Prisma Cloud policies?
  - id: get-policy-filter-options
    intent: Autocomplete values for a policy filter
    question: What values are available for a specific policy filter like compliance standard?
  - id: get-policies
    intent: List policies (v1)
    question: Which high-severity policies are enabled in Prisma Cloud?
  - id: add-policy
    intent: Create a custom policy
    question: How do I create my own custom policy with a rule and severity?
  - id: get-policies-v2
    intent: List policies (v2, faster)
    question: Is there a faster way to list policies that also lets me filter by rule type and subtype?
  - id: get-policy
    intent: Get a policy by ID
    question: What rule, severity and remediation does a specific policy have?
  - id: update-policy
    intent: Update an existing policy
    question: Can I change the severity or rule of an existing policy?
  - id: delete-policy
    intent: Delete a policy
    question: How do I permanently remove a custom policy?
  phrasing_ops: 11
  slug: palo-alto-networks-policy-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Private Key Import.
  name: Palo Alto Networks Private Key Import API
  phrasing_intents:
  - id: certificates_import
    intent: Import certificates with private keys
    question: How do I import certificates and their private keys onto an edge instance?
  - id: certificatesImport_getByImportId
    intent: Get certificate import details
    question: Did my certificate import succeed?
  phrasing_ops: 2
  slug: palo-alto-networks-private-key-import-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: Profile Groups
  name: Palo Alto Networks Profile Groups API
  phrasing_intents:
  - id: ListProfileGroups
    intent: List security profile groups
    question: Which security profile groups are available for my rules?
  - id: CreateProfileGroups
    intent: Create a security profile group
    question: How do I bundle antivirus, spyware and URL filtering profiles into one group?
  - id: GetProfileGroupsByID
    intent: Get a security profile group
    question: Which profiles are inside a particular profile group?
  - id: UpdateProfileGroupsByID
    intent: Update a security profile group
    question: How do I swap the vulnerability profile in an existing group?
  - id: DeleteProfileGroupsByID
    intent: Delete a security profile group
    question: How do I delete a profile group?
  - id: get-sse-config-v1-profile-groups
    intent: List security profile groups
    question: Which security profile groups are defined in a folder?
  - id: post-sse-config-v1-profile-groups
    intent: Create a security profile group
    question: Can I create a profile group in a folder that bundles vulnerability and spyware profiles?
  - id: delete-sse-config-v1-profile-groups-id
    intent: Delete a security profile group
    question: How do I delete a security profile group via the SSE config v1 path?
  phrasing_ops: 10
  slug: palo-alto-networks-profile-groups-api
- baseURL: https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1
  baseurl_source: declared
  description: Onboarding Properties information
  name: Palo Alto Networks Properties API
  phrasing_intents:
  - id: createProperty
    intent: Create a site property definition
    question: How do I define a new custom property with min and max constraints?
  - id: listProperties
    intent: List site property definitions
    question: Which custom properties are defined for my sites?
  - id: getPropertyByID
    intent: Get a property definition
    question: How do I look up one property definition by its UUID?
  - id: updatePropertyByID
    intent: Update a property definition
    question: Can I change a property's constraints without breaking sites that use it?
  - id: deletePropertyByID
    intent: Delete a property definition
    question: How do I delete a property that no sites use anymore?
  phrasing_ops: 5
  slug: palo-alto-networks-properties-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: QoS Profiles
  name: Palo Alto Networks QoS Profiles API
  phrasing_intents:
  - id: ListQoSProfiles
    intent: List QoS profiles
    question: Which QoS profiles are configured in a folder?
  - id: CreateQoSProfiles
    intent: Create a QoS profile
    question: How do I create a QoS profile that caps aggregate bandwidth?
  - id: GetQoSProfilesByID
    intent: Get a QoS profile
    question: What bandwidth limits are in a particular QoS profile?
  - id: UpdateQoSProfilesByID
    intent: Update a QoS profile
    question: How do I change the class bandwidth on an existing QoS profile?
  - id: DeleteQoSProfilesByID
    intent: Delete a QoS profile
    question: Is there a way to remove a QoS profile?
  - id: get-sse-config-v1-qos-profiles
    intent: List QoS profiles
    question: Which quality of service profiles exist in a Prisma Access folder?
  - id: post-sse-config-v1-qos-profiles
    intent: Create a QoS profile
    question: How do I create a QoS profile with an aggregate bandwidth limit?
  - id: delete-sse-config-v1-qos-profiles-id
    intent: Delete a QoS profile
    question: Which call removes a QoS profile?
  phrasing_ops: 10
  slug: palo-alto-networks-qos-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: QoS Rules
  name: Palo Alto Networks QoS Rules API
  phrasing_intents:
  - id: ListQoSPolicyRules
    intent: List QoS policy rules
    question: What QoS policy rules are configured in a folder?
  - id: CreateQoSPolicyRules
    intent: Create a QoS policy rule
    question: How do I add a rule that prioritizes traffic by QoS class?
  - id: GetQoSPolicyRulesByID
    intent: Get a QoS policy rule
    question: What does a particular QoS rule do?
  - id: UpdateQoSPolicyRulesByID
    intent: Update a QoS policy rule
    question: How do I change the action on an existing QoS rule?
  - id: DeleteQoSPolicyRulesByID
    intent: Delete a QoS policy rule
    question: How do I remove a QoS rule?
  - id: MoveQoSPolicyRulesByID
    intent: Reorder a QoS policy rule
    question: How do I move a QoS rule to the top or bottom of the rulebase?
  - id: listQoSRules
    intent: List SD-WAN QoS rules
    question: Which QoS rules prioritize traffic on my SD-WAN links?
  - id: createQoSRule
    intent: Create an SD-WAN QoS rule
    question: How do I prioritize an application's traffic over my WAN links?
  phrasing_ops: 8
  slug: palo-alto-networks-qos-rules-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The QoSPolicyRules API from Palo Alto Networks — 3 operation(s) for qospolicyrules.
  name: Palo Alto Networks Qo S Policy Rules API
  phrasing_intents:
  - id: get-sse-config-v1-qos-policy-rules
    intent: List QoS policy rules in a folder
    question: What quality of service rules are configured in a Prisma Access folder?
  - id: post-sse-config-v1-qos-policy-rules
    intent: Create a QoS policy rule
    question: How do I prioritize traffic with a new QoS rule?
  - id: delete-sse-config-v1-qos-policy-rules-id
    intent: Delete a QoS policy rule
    question: Can I remove a QoS rule I no longer need?
  - id: get-sse-config-v1-qos-policy-rules-id
    intent: Get a QoS policy rule
    question: Where can I see a single QoS rule's settings?
  - id: put-sse-config-v1-qos-policy-rules-id
    intent: Edit a QoS policy rule
    question: How do I change the action of an existing QoS rule?
  - id: post-sse-config-v1-qos-policy-rules-id:move
    intent: Reorder a QoS policy rule
    question: How do I move a QoS rule to the top of the rulebase?
  phrasing_ops: 6
  slug: palo-alto-networks-qospolicyrules-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: Quarantined Devices
  name: Palo Alto Networks Quarantined Devices API
  phrasing_intents:
  - id: ListQuarantinedDevices
    intent: List quarantined devices
    question: Which devices are currently quarantined from GlobalProtect?
  - id: CreateQuarantinedDevices
    intent: Quarantine a device
    question: How do I quarantine a compromised device?
  - id: DeleteQuarantinedDevices
    intent: Release a device from quarantine
    question: How do I take a device out of quarantine?
  - id: delete-sse-config-v1-quarantined-devices
    intent: Release a device from quarantine
    question: How do I take a device off the quarantine list?
  - id: get-sse-config-v1-quarantined-devices
    intent: List quarantined devices
    question: Which devices are currently on the quarantine list?
  - id: post-sse-config-v1-quarantined-devices
    intent: Quarantine a device
    question: How do I quarantine a compromised endpoint?
  phrasing_ops: 6
  slug: palo-alto-networks-quarantined-devices-api
- baseURL: https://api.sase.paloaltonetworks.com/ai-red-teaming/data-plane
  baseurl_source: declared
  description: Operations for quota management and limits.
  name: Palo Alto Networks Quota API
  phrasing_intents:
  - id: post_quota_summary_v1_metering_quota_post
    intent: Get the quota summary for the tenant
    question: How much of my quota has the current tenant service group used?
  phrasing_ops: 1
  slug: palo-alto-networks-quota-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: RADIUS Server Profiles
  name: Palo Alto Networks RADIUS Server Profiles API
  phrasing_intents:
  - id: ListRADIUSServerProfiles
    intent: List RADIUS server profiles
    question: Which RADIUS server profiles are configured for authentication?
  - id: CreateRADIUSServerProfiles
    intent: Create a RADIUS server profile
    question: How do I add a RADIUS server for user authentication?
  - id: GetRADIUSServerProfilesByID
    intent: Get a RADIUS server profile
    question: What servers and protocol does a RADIUS profile use?
  - id: UpdateRADIUSServerProfilesByID
    intent: Update a RADIUS server profile
    question: Can I change the authentication protocol on an existing RADIUS profile?
  - id: DeleteRADIUSServerProfilesByID
    intent: Delete a RADIUS server profile
    question: Can I delete a RADIUS server profile?
  - id: get-sse-config-v1-radius-server-profiles
    intent: List RADIUS server profiles
    question: Which RADIUS server profiles are configured?
  - id: post-sse-config-v1-radius-server-profiles
    intent: Create a RADIUS server profile
    question: How do I add RADIUS servers to a folder, snippet or device?
  - id: delete-sse-config-v1-radius-server-profiles-id
    intent: Delete a RADIUS server profile
    question: How do I delete a RADIUS server profile?
  phrasing_ops: 10
  slug: palo-alto-networks-radius-server-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
  baseurl_source: declared
  description: Regional and Custom Proxies
  name: Palo Alto Networks Regional and Custom Proxies API
  phrasing_intents:
  - id: ListGlobalProtectRegionalAndCustomProxies
    intent: List GlobalProtect regional and custom proxies
    question: Which regional and custom proxies are configured for GlobalProtect forwarding profiles?
  - id: CreateGlobalProtectRegionalAndCustomProxies
    intent: Create a GlobalProtect regional or custom proxy
    question: How do I add a custom proxy for GlobalProtect users in Prisma Access?
  - id: GetGlobalProtectRegionalAndCustomProxyByID
    intent: Get a GlobalProtect regional or custom proxy
    question: How do I see the full configuration of one GlobalProtect regional proxy?
  - id: UpdateGlobalProtectRegionalAndCustomProxyByID
    intent: Update a GlobalProtect regional or custom proxy
    question: Can I change the proxy servers on an existing GlobalProtect regional proxy?
  - id: DeleteGlobalProtectRegionalAndCustomProxies
    intent: Delete a GlobalProtect regional or custom proxy
    question: How do I remove a GlobalProtect custom proxy I no longer route through?
  phrasing_ops: 5
  slug: palo-alto-networks-regional-and-custom-proxies-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Regions API from Palo Alto Networks — 4 operation(s) for regions.
  name: Palo Alto Networks Regions API
  phrasing_intents:
  - id: get-sse-config-v1-regions
    intent: List region objects in an SSE folder
    question: Which region objects are defined in a given SSE config folder?
  - id: post-sse-config-v1-regions
    intent: Create a region object (SSE config v1)
    question: How do I define a custom region with a geo location on the SSE v1 API?
  - id: delete-sse-config-v1-regions-id
    intent: Delete a region object (SSE config v1)
    question: How do I remove a custom region using the SSE config v1 path?
  - id: get-sse-config-v1-regions-id
    intent: Get a region object by ID (SSE config v1)
    question: What addresses and coordinates does one SSE region object contain?
  - id: put-sse-config-v1-regions-id
    intent: Edit a region object (SSE config v1)
    question: Can I change the IP addresses on an SSE region object?
  - id: ListRegions
    intent: List region objects by folder, snippet or device
    question: What region objects exist on a particular device or snippet?
  - id: CreateRegions
    intent: Create a region object
    question: What's required to create a region object outside the SSE config path?
  - id: GetRegionsByID
    intent: Get a region object
    question: How can I read an existing region object's addresses?
  phrasing_ops: 10
  slug: palo-alto-networks-regions-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Remediations API from Palo Alto Networks — 3 operation(s) for remediations.
  name: Palo Alto Networks Remediations API
  phrasing_intents:
  - id: postRemediationsBuildTime
    intent: Open or update a PR with build-time fixes
    question: How do I have code security open a pull request that fixes misconfigured resources?
  - id: getRemediationFixCode
    intent: Get the fix code for a remediation
    question: How do I see the suggested code change for a specific fix?
  - id: getRemediationBaseFile
    intent: Get the original file for a remediation
    question: Can I view the original file a remediation will modify?
  phrasing_ops: 3
  slug: palo-alto-networks-remediations-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Remote Networks License Info
  name: Palo Alto Networks Remote Networks License API
  phrasing_intents:
  - id: getRemoteNetworksLicenseInfo
    intent: Get remote networks license information
    question: What license model are my Prisma Access remote networks using?
  phrasing_ops: 1
  slug: palo-alto-networks-remote-networks-license-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The Report API API from Palo Alto Networks — 8 operation(s) for report api.
  name: Palo Alto Networks Report API
  phrasing_intents:
  - id: PostMtPabReportCount
    intent: Count security events for a tenant
    question: How many browser security events has my tenant recorded in total?
  - id: PostMtPabReportExtension_blocked
    intent: Report blocked browser extensions
    question: Which browser extensions were blocked for my users?
  - id: PostMtPabReportExtension_category
    intent: Report browser extensions by category
    question: What kinds of browser extensions are my users running, grouped by category?
  - id: PostMtPabReportMalicious_website
    intent: Report malicious websites detected
    question: Which malicious websites did the browser detect for my tenant?
  - id: PostMtPabReportMalware_blocked
    intent: Report blocked malware
    question: How much malware did the browser block for my users?
  - id: PostMtPabReportMalware_website
    intent: Report websites identified as malware sources
    question: Which websites were flagged as sources of malware?
  - id: PostMtPabReportWebsite_blocked
    intent: Report blocked websites
    question: Which websites did the browser block for my users?
  - id: PostMtPabReportWebsite_category
    intent: Report website access by category
    question: What categories of websites are my users visiting most?
  phrasing_ops: 8
  slug: palo-alto-networks-report-api-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The Repository API from Palo Alto Networks — 1 operation(s) for repository.
  name: Palo Alto Networks Repository API
  phrasing_intents:
  - id: getRepository
    intent: Get a single code repository
    question: Who owns a given repository and is it public?
  phrasing_ops: 1
  slug: palo-alto-networks-repository-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Repository Importance Score indicates the relative criticality of a repository, allowing you to focus on the most critical repositories, thereby enabling you to make informed decisions about secur
  name: Palo Alto Networks Repository Importance Score API
  phrasing_intents:
  - id: getRepositoriesImportanceScore
    intent: Get repository importance scores
    question: How security-critical is each of my repositories according to its importance score?
  - id: setRepositoryImportanceScore
    intent: Set a custom repository importance score
    question: How do I override the calculated importance score for a repository?
  phrasing_ops: 2
  slug: palo-alto-networks-repository-importance-score-api
- baseURL: https://api.strata.paloaltonetworks.com
  baseurl_source: declared
  description: The Resolver Info API from Palo Alto Networks — 1 operation(s) for resolver info.
  name: Palo Alto Networks Resolver Info API
  phrasing_intents:
  - id: GetResolverInfo
    intent: Get ADNS resolver IP information
    question: What are the IP addresses of my ADNS resolvers?
  phrasing_ops: 1
  slug: palo-alto-networks-resolver-info-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: '### Where Do I Find the RRN For My Resource? You can find the RRN for a resource in the URL when you view that resource in the Prisma Cloud Resource explorer. The following is an example of such a URL'
  name: Palo Alto Networks Resource Explorer API
  phrasing_intents:
  - id: get-resource
    intent: Get a cloud resource's details
    question: How do I look up the full details of a cloud resource by its RRN?
  - id: get-alerts-for-resource
    intent: List alerts on a cloud resource
    question: Which alerts are open against a specific cloud resource?
  - id: get-network-for-resource
    intent: Get a resource's network port settings
    question: Which network ports are open on a given cloud resource?
  - id: get-host-findings-for-alert
    intent: List host findings for an alert
    question: What host findings are attached to a specific alert?
  - id: get-host-findings
    intent: List host findings for a resource
    question: Which host findings, like GuardDuty or vulnerability results, exist for a resource?
  - id: get-timeline-for-resource
    intent: Get a resource's event and alert timeline
    question: What has happened to a cloud resource over time, event by event?
  - id: get-resource-raw
    intent: Get a resource's raw config at a point in time
    question: How do I see the raw cloud provider JSON for a resource as it was at a past point in time?
  - id: get-external-integrations-for-resource
    intent: List external ingest integrations for a resource
    question: Which external ingestion integrations are feeding data about this resource?
  phrasing_ops: 8
  slug: palo-alto-networks-resource-explorer-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: A Resource List is a way to identify resources that are assigned with a specific tag or label.
  name: Palo Alto Networks Resource Lists API
  phrasing_intents:
  - id: get-all-resource-list-for-customer
    intent: List resource lists of a type
    question: What resource lists do I have of a given type?
  - id: add-resource-list
    intent: Create a resource list
    question: How do I create a new resource list with members?
  - id: get-resource-list-types
    intent: List resource list types
    question: Which kinds of resource lists are supported?
  - id: get-resource-list-by-id
    intent: Get a resource list
    question: How can I see the members of one resource list?
  - id: update-resource-list
    intent: Update a resource list
    question: Can I change the members of an existing resource list?
  - id: delete-resource-list-by-id
    intent: Delete a resource list
    question: How do I remove a resource list I no longer need?
  phrasing_ops: 6
  slug: palo-alto-networks-resource-lists-api
- baseURL: https://api.dig.security
  baseurl_source: declared
  description: The Risk Findings API from Palo Alto Networks — 3 operation(s) for risk findings.
  name: Palo Alto Networks Risk Findings API
  phrasing_intents:
  - id: patch-risk-findings-id-id-status-status
    intent: Change a DSPM risk finding's status
    question: How do I mark a data security risk finding as resolved?
  - id: get-risk-findings
    intent: List DSPM risk findings
    question: Which data security risk findings are high severity right now?
  - id: get-risk-findings-id-id
    intent: Describe a DSPM risk finding
    question: What are the full details of one risk finding?
  phrasing_ops: 3
  slug: palo-alto-networks-risk-findings-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Route Access Lists
  name: Palo Alto Networks Route Access Lists API
  phrasing_intents:
  - id: ListRouteAccessLists
    intent: List route access lists
    question: Which route access lists are configured in a folder?
  - id: CreateRouteAccessLists
    intent: Create a route access list
    question: How do I create a route access list to filter routes?
  - id: GetRouteAccessListsByID
    intent: Get a route access list
    question: What entries does a specific route access list contain?
  - id: UpdateRouteAccessListsByID
    intent: Update a route access list
    question: Can I change the type of an existing route access list?
  - id: DeleteRouteAccessListsByID
    intent: Delete a route access list
    question: How do I delete a route access list?
  phrasing_ops: 5
  slug: palo-alto-networks-route-access-lists-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Route Community Lists
  name: Palo Alto Networks Route Community Lists API
  phrasing_intents:
  - id: ListRouteCommunityLists
    intent: List BGP route community lists
    question: Which route community lists are defined for my BGP routing?
  - id: CreateRouteCommunityLists
    intent: Create a route community list
    question: How do I create a new community list for route filtering?
  - id: GetRouteCommunityListsByID
    intent: Get a route community list
    question: What communities are in a particular route community list?
  - id: UpdateRouteCommunityListsByID
    intent: Update a route community list
    question: How do I change the entries in an existing route community list?
  - id: DeleteRouteCommunityListsByID
    intent: Delete a route community list
    question: How do I remove a route community list?
  phrasing_ops: 5
  slug: palo-alto-networks-route-community-lists-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Route Path Access Lists
  name: Palo Alto Networks Route Path Access Lists API
  phrasing_intents:
  - id: ListRoutePathAccessLists
    intent: List AS path access lists
    question: Which BGP AS path access lists are defined in Strata Cloud Manager?
  - id: CreateRoutePathAccessLists
    intent: Create an AS path access list
    question: How do I filter BGP routes by AS path?
  - id: GetRoutePathAccessListsByID
    intent: Get an AS path access list
    question: Where can I see the AS path entries in one access list?
  - id: UpdateRoutePathAccessListsByID
    intent: Update an AS path access list
    question: How do I add AS path entries to an existing access list?
  - id: DeleteRoutePathAccessListsByID
    intent: Delete an AS path access list
    question: Can I remove a route path access list?
  phrasing_ops: 5
  slug: palo-alto-networks-route-path-access-lists-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Route Prefix Lists
  name: Palo Alto Networks Route Prefix Lists API
  phrasing_intents:
  - id: ListRoutePrefixLists
    intent: List route prefix lists
    question: What route prefix lists are defined for my devices?
  - id: CreateRoutePrefixLists
    intent: Create a route prefix list
    question: How do I create a route prefix list for routing policy?
  - id: GetRoutePrefixListsByID
    intent: Get a route prefix list
    question: How can I see the entries in one route prefix list?
  - id: UpdateRoutePrefixListsByID
    intent: Update a route prefix list
    question: Can I change the type or description of a route prefix list I already made?
  - id: DeleteRoutePrefixListsByID
    intent: Delete a route prefix list
    question: How do I delete a route prefix list?
  phrasing_ops: 5
  slug: palo-alto-networks-route-prefix-lists-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The RouteController API from Palo Alto Networks — 1 operation(s) for routecontroller.
  name: Palo Alto Networks Route Controller API
  phrasing_intents:
  - id: RouteController.getRouteHops
    intent: Get a traceroute summary for overlay and underlay paths
    question: What hops does traffic take across overlay and underlay paths for my users?
  phrasing_ops: 1
  slug: palo-alto-networks-routecontroller-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Rules API from Palo Alto Networks — 4 operation(s) for rules.
  name: Palo Alto Networks Rules API
  phrasing_intents:
  - id: getSchemeForAccount
    intent: Get enforcement rules for one code account
    question: Which enforcement thresholds apply to a specific repository account?
  - id: getSchemeForCustomer
    intent: List all code enforcement rules
    question: What enforcement rules do we have across IaC, secrets, images and open source?
  - id: addRule
    intent: Create an enforcement exception for repositories
    question: How do I relax enforcement thresholds for a specific set of repositories?
  - id: editRule
    intent: Update a code enforcement rule or exception
    question: How do I change the thresholds on an existing enforcement rule?
  - id: deleteRule
    intent: Delete an enforcement exception rule
    question: How do I remove an enforcement exception we no longer need?
  - id: getAccounts
    intent: List build-time repository accounts
    question: Which repositories are connected for build-time code scanning?
  phrasing_ops: 6
  slug: palo-alto-networks-rules-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The RumController API from Palo Alto Networks — 2 operation(s) for rumcontroller.
  name: Palo Alto Networks Rum Controller API
  phrasing_intents:
  - id: RumController.getRumMetric
    intent: Get real user monitoring metrics
    question: How do I pull real user monitoring metrics from ADEM for my tenant?
  - id: RumController.getRumScore
    intent: Get real user experience scores
    question: What is the real user experience score for my users in ADEM?
  phrasing_ops: 2
  slug: palo-alto-networks-rumcontroller-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: Saas Tenant Restrictions
  name: Palo Alto Networks Saas Tenant Restrictions API
  phrasing_intents:
  - id: GetSaasTenantRestrictions
    intent: Get SaaS tenant restrictions
    question: Which SaaS tenant restrictions are configured, such as for Microsoft 365 or Dropbox?
  - id: UpdateSaasTenantRestrictions
    intent: Update SaaS tenant restrictions
    question: How do I restrict access to only my organization's SaaS tenants using domains and headers?
  phrasing_ops: 2
  slug: palo-alto-networks-saas-tenant-restrictions-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: SAML Server Profiles
  name: Palo Alto Networks SAML Server Profiles API
  phrasing_intents:
  - id: ListSAMLServerProfiles
    intent: List SAML server profiles
    question: Which SAML identity provider profiles are configured for authentication?
  - id: CreateSAMLServerProfiles
    intent: Create a SAML server profile
    question: How do I register a SAML identity provider for single sign-on?
  - id: GetSAMLServerProfilesByID
    intent: Get a SAML server profile
    question: What SSO URL and certificate does a given SAML server profile use?
  - id: UpdateSAMLServerProfilesByID
    intent: Update a SAML server profile
    question: How do I rotate the IdP certificate on an existing SAML server profile?
  - id: DeleteSAMLServerProfilesByID
    intent: Delete a SAML server profile
    question: How do I remove a SAML identity provider profile we stopped using?
  - id: get-sse-config-v1-saml-server-profiles
    intent: List SAML server profiles
    question: Which SAML identity provider profiles are configured in a folder?
  - id: post-sse-config-v1-saml-server-profiles
    intent: Create a SAML server profile
    question: How do I add a SAML identity provider profile with its signing certificate?
  - id: delete-sse-config-v1-saml-server-profiles-id
    intent: Delete a SAML server profile
    question: How do I remove a SAML identity provider profile?
  phrasing_ops: 10
  slug: palo-alto-networks-saml-server-profiles-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/sandbox/sandbox.md''}'
  name: Palo Alto Networks Sandbox API
  slug: palo-alto-networks-sandbox-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The SBOM API from Palo Alto Networks — 16 operation(s) for sbom.
  name: Palo Alto Networks SBOM API
  phrasing_intents:
  - id: getBOMReport
    intent: Download a repository's BOM report
    question: How do I get a bill of materials report for one of my code repositories?
  - id: sbomDependencies
    intent: List open-source packages found across VCS
    question: Which open-source packages are used across my organization's connected repositories?
  - id: get-sbom-download-cli-images
    intent: Download SBOMs for CLI-scanned CI images (v34.03)
    question: How do I pull SBOMs for container images my CI pipeline scanned with twistcli, on v34.03?
  - id: get-sbom-download-cli-serverless
    intent: Download SBOMs for CI-scanned functions (v34.03)
    question: How do I get SBOMs for functions I scanned from the command line in CI, using v34.03?
  - id: get-sbom-download-hosts
    intent: Download host SBOMs (v34.03)
    question: How do I export a software bill of materials for my protected hosts on v34.03?
  - id: get-sbom-download-images
    intent: Download deployed image SBOMs (v34.03)
    question: How do I download SBOMs for container images running in my environment, on v34.03?
  - id: get-sbom-download-registry
    intent: Download registry image SBOMs (v34.03)
    question: How do I export SBOMs for images stored in my container registries, via v34.03?
  - id: get-sbom-download-serverless
    intent: Download deployed function SBOMs (v34.03)
    question: How do I export SBOMs for cloud functions discovered in my accounts, on v34.03?
  phrasing_ops: 16
  slug: palo-alto-networks-sbom-api
- baseURL: https://service.api.aisecurity.paloaltonetworks.com
  baseurl_source: declared
  description: Operations for retrieving detailed scan reports
  name: Palo Alto Networks Scan Reports API
  phrasing_intents:
  - id: GetThreatScanReports
    intent: Get threat scan reports by ID
    question: What did the threat scans find for a set of report IDs?
  phrasing_ops: 1
  slug: palo-alto-networks-scan-reports-api
- baseURL: https://service.api.aisecurity.paloaltonetworks.com
  baseurl_source: declared
  description: Operations for retrieving scan results
  name: Palo Alto Networks Scan Results API
  phrasing_intents:
  - id: GetScanResultsByScanIDs
    intent: Get results for up to five scans
    question: What did my scans find, if I have their scan IDs?
  phrasing_ops: 1
  slug: palo-alto-networks-scan-results-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: SCEP Profiles
  name: Palo Alto Networks SCEP Profiles API
  phrasing_intents:
  - id: ListSCEPProfiles
    intent: List SCEP profiles
    question: Which SCEP certificate enrollment profiles are configured?
  - id: CreateSCEPProfiles
    intent: Create a SCEP profile
    question: How do I set up SCEP so the firewall can enroll certificates from my CA?
  - id: GetSCEPProfilesByID
    intent: Get a SCEP profile
    question: What SCEP server URL and CA identity does one profile use?
  - id: UpdateSCEPProfilesByID
    intent: Update a SCEP profile
    question: How do I change the SCEP server URL on an existing profile?
  - id: DeleteSCEPProfilesByID
    intent: Delete a SCEP profile
    question: How do I remove a SCEP profile?
  - id: get-sse-config-v1-scep-profiles
    intent: List SCEP profiles
    question: Which SCEP profiles are set up for certificate enrollment?
  - id: post-sse-config-v1-scep-profiles
    intent: Create a SCEP profile
    question: How do I create a SCEP profile to enroll certificates from our CA?
  - id: delete-sse-config-v1-scep-profiles-id
    intent: Delete a SCEP profile
    question: Can I remove a SCEP profile that's no longer used?
  phrasing_ops: 10
  slug: palo-alto-networks-scep-profiles-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Schedules API from Palo Alto Networks — 4 operation(s) for schedules.
  name: Palo Alto Networks Schedules API
  phrasing_intents:
  - id: get-sse-config-v1-schedules
    intent: List Prisma Access schedules in a folder
    question: Which schedule objects exist in a Prisma Access folder?
  - id: post-sse-config-v1-schedules
    intent: Create a Prisma Access schedule
    question: How do I create a time-based schedule object in a Prisma Access folder?
  - id: delete-sse-config-v1-schedules-id
    intent: Delete a Prisma Access schedule
    question: How do I remove a schedule object from Prisma Access?
  - id: get-sse-config-v1-schedules-id
    intent: Get a Prisma Access schedule
    question: What time ranges are defined in a particular Prisma Access schedule?
  - id: put-sse-config-v1-schedules-id
    intent: Edit a Prisma Access schedule
    question: How do I change the time window of an existing Prisma Access schedule?
  - id: ListSchedules
    intent: List Strata Cloud Manager schedules
    question: What schedules are configured in a Strata Cloud Manager folder, snippet or device?
  - id: CreateSchedules
    intent: Create a Strata Cloud Manager schedule
    question: How do I create a schedule object in Strata Cloud Manager?
  - id: GetSchedulesByID
    intent: Get a Strata Cloud Manager schedule
    question: What does one Strata Cloud Manager schedule object contain?
  phrasing_ops: 10
  slug: palo-alto-networks-schedules-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: SD-WAN Error Correction Profiles
  name: Palo Alto Networks SD-WAN Error Correction Profiles API
  phrasing_intents:
  - id: ListSDWANErrorCorrectionProfiles
    intent: List SD-WAN error correction profiles
    question: Which SD-WAN error correction profiles are defined in my configuration?
  - id: CreateSDWANErrorCorrectionProfiles
    intent: Create an SD-WAN error correction profile
    question: How do I set up forward error correction for SD-WAN with an activation threshold?
  - id: GetSDWANErrorCorrectionProfilesByID
    intent: Get an SD-WAN error correction profile
    question: What activation threshold and mode does a specific SD-WAN error correction profile use?
  - id: UpdateSDWANErrorCorrectionProfilesByID
    intent: Update an SD-WAN error correction profile
    question: Can I lower the activation threshold on an existing SD-WAN error correction profile?
  - id: DeleteSDWANErrorCorrectionProfilesByID
    intent: Delete an SD-WAN error correction profile
    question: Can I delete an SD-WAN error correction profile I no longer need?
  phrasing_ops: 5
  slug: palo-alto-networks-sd-wan-error-correction-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: SD-WAN Path Quality Profiles
  name: Palo Alto Networks SD-WAN Path Quality Profiles API
  phrasing_intents:
  - id: ListSDWANPathQualityProfiles
    intent: List SD-WAN path quality profiles
    question: Which SD-WAN path quality profiles are defined in my folders?
  - id: CreateSDWANPathQualityProfiles
    intent: Create an SD-WAN path quality profile
    question: How do I set latency, jitter and packet loss thresholds for SD-WAN path selection?
  - id: GetSDWANPathQualityProfilesByID
    intent: Get an SD-WAN path quality profile
    question: What thresholds does a specific SD-WAN path quality profile use?
  - id: UpdateSDWANPathQualityProfilesByID
    intent: Update an SD-WAN path quality profile
    question: Can I tighten the thresholds on an existing path quality profile?
  - id: DeleteSDWANPathQualityProfilesByID
    intent: Delete an SD-WAN path quality profile
    question: How do I delete an SD-WAN path quality profile?
  phrasing_ops: 5
  slug: palo-alto-networks-sd-wan-path-quality-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: SD-WAN Rules
  name: Palo Alto Networks SD-WAN Rules API
  phrasing_intents:
  - id: ListSDWANRules
    intent: List SD-WAN rules
    question: Which SD-WAN traffic steering rules are defined in a folder?
  - id: CreateSDWANRules
    intent: Create an SD-WAN rule
    question: How do I steer an application's traffic using a path quality profile?
  - id: GetSDWANRulesByID
    intent: Get an SD-WAN rule
    question: What applications and path quality profile does a particular SD-WAN rule use?
  - id: UpdateSDWANRulesByID
    intent: Update an SD-WAN rule
    question: Can I switch the path quality profile on an existing SD-WAN rule?
  - id: DeleteSDWANRulesByID
    intent: Delete an SD-WAN rule
    question: How do I remove an SD-WAN rule?
  phrasing_ops: 5
  slug: palo-alto-networks-sd-wan-rules-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: SD-WAN SaaS Quality Profiles
  name: Palo Alto Networks SD-WAN SaaS Quality Profiles API
  phrasing_intents:
  - id: ListSDWANSaaSQualityProfiles
    intent: List SD-WAN SaaS quality profiles
    question: What SD-WAN SaaS quality profiles have I defined?
  - id: CreateSDWANSaaSQualityProfiles
    intent: Create an SD-WAN SaaS quality profile
    question: How do I create a SaaS quality profile to monitor SaaS app performance over SD-WAN?
  - id: GetSDWANSaaSQualityProfilesByID
    intent: Get an SD-WAN SaaS quality profile by ID
    question: What monitor mode is a specific SaaS quality profile using?
  - id: UpdateSDWANSaaSQualityProfilesByID
    intent: Update an SD-WAN SaaS quality profile
    question: How do I change the monitor mode on an existing SaaS quality profile?
  - id: DeleteSDWANSaaSQualityProfilesByID
    intent: Delete an SD-WAN SaaS quality profile
    question: How do I remove a SaaS quality profile from SD-WAN configuration?
  phrasing_ops: 5
  slug: palo-alto-networks-sd-wan-saas-quality-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: SD-WAN Traffic Distribution Profiles
  name: Palo Alto Networks SD-WAN Traffic Distribution Profiles API
  phrasing_intents:
  - id: ListSDWANTrafficDistributionProfiles
    intent: List SD-WAN traffic distribution profiles
    question: Which SD-WAN traffic distribution profiles are configured?
  - id: CreateSDWANTrafficDistributionProfiles
    intent: Create an SD-WAN traffic distribution profile
    question: How do I define how SD-WAN traffic is spread across links?
  - id: GetSDWANTrafficDistributionProfilesByID
    intent: Get an SD-WAN traffic distribution profile
    question: What distribution method and link tags does a specific profile use?
  - id: UpdateSDWANTrafficDistributionProfilesByID
    intent: Update an SD-WAN traffic distribution profile
    question: How do I switch an existing profile to a different distribution method?
  - id: DeleteSDWANTrafficDistributionProfilesByID
    intent: Delete an SD-WAN traffic distribution profile
    question: How do I remove an SD-WAN traffic distribution profile?
  phrasing_ops: 5
  slug: palo-alto-networks-sd-wan-traffic-distribution-profiles-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Search Manager APIs enable you to manage your recent and saved Resource Query Language (RQL) queries.
  name: Palo Alto Networks Search Manager API
  phrasing_intents:
  - id: search-history
    intent: List recent or saved searches
    question: What searches have I run recently in Prisma Cloud?
  - id: search-history-by-id
    intent: Get a saved or recent search query
    question: What RQL query is behind a saved search?
  - id: search-history-save
    intent: Save a search query to Saved Searches
    question: How do I save an RQL search so I can reuse it later?
  - id: search-history-delete
    intent: Delete a saved search
    question: How do I delete a saved search query?
  phrasing_ops: 4
  slug: palo-alto-networks-search-manager-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: Security Rules
  name: Palo Alto Networks Security Rules API
  phrasing_intents:
  - id: ListRules
    intent: List security rules
    question: Which security rules are in my pre-rulebase for a folder?
  - id: CreateSecurityRules
    intent: Create a Prisma Access security rule
    question: How do I add a security rule to the Prisma Access candidate configuration?
  - id: GetSecurityRulesByID
    intent: Get a security rule
    question: What sources, destinations and actions does one security rule have?
  - id: UpdateSecurityRulesByID
    intent: Update a Prisma Access security rule
    question: How do I edit a Prisma Access security rule in the candidate configuration?
  - id: DeleteSecurityRulesByID
    intent: Delete a security rule
    question: How do I delete a security rule from the policy?
  - id: MoveSecurityRulesByID
    intent: Reorder a security rule in the rulebase
    question: How do I move a security rule to the top of the rulebase?
  - id: get-sse-config-v1-security-rules
    intent: List security rules via the SSE config API
    question: Which security rules are in the pre or post rulebase of a folder through the SSE config v1 endpoint?
  - id: post-sse-config-v1-security-rules
    intent: Create a security rule via the SSE config API
    question: How do I add a security rule to a folder through the SSE config v1 API?
  phrasing_ops: 17
  slug: palo-alto-networks-security-rules-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Security Zones
  name: Palo Alto Networks Security Zones API
  phrasing_intents:
  - id: ListZones
    intent: List security zones
    question: Which security zones are defined in a folder or snippet?
  - id: CreateZones
    intent: Create a security zone
    question: How do I create a new security zone and assign network interfaces to it?
  - id: GetZonesByID
    intent: Get a security zone
    question: What interfaces and ACLs belong to a specific security zone?
  - id: UpdateZonesByID
    intent: Update a security zone
    question: How do I enable device identification on an existing security zone?
  - id: DeleteZonesByID
    intent: Delete a security zone
    question: How do I delete a security zone?
  phrasing_ops: 5
  slug: palo-alto-networks-security-zones-api
- baseURL: https://api.sase.paloaltonetworks.com/ai-red-teaming/data-plane
  baseurl_source: declared
  description: Operations for managing sentiment and scan report summaries.
  name: Palo Alto Networks Sentiment API
  phrasing_intents:
  - id: create_or_update_sentiment_v1_sentiment_post
    intent: Rate a scan report
    question: Can I upvote or downvote the report from a scan job?
  - id: get_job_sentiment_v1_sentiment__job_id__get
    intent: Get feedback on a scan
    question: What sentiment was recorded for a scan job's report?
  phrasing_ops: 2
  slug: palo-alto-networks-sentiment-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/serverless/serverless.md''}'
  name: Palo Alto Networks Serverless API
  phrasing_intents:
  - id: get-serverless
    intent: Get serverless function scan results (v34.03)
    question: What did the v34.03 serverless scan find across my functions?
  - id: get-serverless-download
    intent: Download serverless scan results (v34.03)
    question: How do I export the v34.03 serverless scan results as a file?
  - id: post-serverless-evaluate
    intent: Resolve serverless functions (v34.03)
    question: How do I resolve a set of serverless functions against v34.03 scan data?
  - id: get-serverless-names
    intent: List scanned serverless function names (v34.03)
    question: Which serverless function names has the v34.03 scanner seen?
  - id: post-serverless-scan
    intent: Start a serverless function scan (v34.03)
    question: How do I kick off a new serverless function scan with v34.03?
  - id: post-serverless-stop
    intent: Stop a serverless function scan (v34.03)
    question: How do I stop a running v34.03 serverless scan?
  - id: getApiV3404Serverless
    intent: Get serverless function scan results (v34.04)
    question: What did the v34.04 serverless scan find in my cloud functions?
  - id: getApiV3404ServerlessDownload
    intent: Download serverless scan results (v34.04)
    question: Can I export v34.04 serverless function scan results to a file?
  phrasing_ops: 12
  slug: palo-alto-networks-serverless-api
- baseURL: https://api.strata.paloaltonetworks.com/config/deployment/v1
  baseurl_source: declared
  description: Service Connection groups
  name: Palo Alto Networks Service Connection Groups API
  phrasing_intents:
  - id: ListServiceConnectionGroups
    intent: List service connection groups
    question: Which service connection groups are configured in my folder?
  - id: CreateServiceConnectionGroups
    intent: Create a service connection group
    question: How do I group service connections together under one target?
  - id: GetServiceConnectionGroupsByID
    intent: Get a service connection group
    question: What targets belong to a specific service connection group?
  - id: UpdateServiceConnectionGroupsByID
    intent: Update a service connection group
    question: Can I change which service connections an existing group targets?
  - id: DeleteServiceConnectionGroupsByID
    intent: Delete a service connection group
    question: How do I remove a service connection group?
  - id: get-sse-config-v1-service-connection-groups
    intent: List service connection groups
    question: Which service connection groups are configured in a folder?
  - id: post-sse-config-v1-service-connection-groups
    intent: Create a service connection group
    question: How do I group several service connections together?
  - id: delete-sse-config-v1-service-connection-groups-id
    intent: Delete a service connection group
    question: How do I delete a service connection group?
  phrasing_ops: 10
  slug: palo-alto-networks-service-connection-groups-api
- baseURL: https://api.strata.paloaltonetworks.com/config/deployment/v1
  baseurl_source: declared
  description: Service Connections
  name: Palo Alto Networks Service Connections API
  phrasing_intents:
  - id: ListServiceConnections
    intent: List service connections
    question: Which Prisma Access service connections are set up?
  - id: CreateServiceConnections
    intent: Stage a new service connection
    question: Is a new service connection live right away, or does it need a push?
  - id: GetServiceConnectionsByID
    intent: Get a service connection
    question: What tunnel and region does a given service connection use?
  - id: UpdateServiceConnectionsByID
    intent: Update a service connection in the candidate config
    question: Can I enable QoS on a service connection that already exists?
  - id: DeleteServiceConnectionsByID
    intent: Delete a service connection
    question: How do I remove a service connection?
  - id: get-sse-config-v1-bgp-routing
    intent: View Prisma Access BGP routing settings
    question: What BGP routing preference is set for my Prisma Access service connections?
  - id: put-sse-config-v1-bgp-routing
    intent: Change Prisma Access BGP routing settings
    question: How do I switch the routing preference between default and hot-potato?
  - id: get-sse-config-v1-service-connections
    intent: List service connections in an SSE folder
    question: Which service connections are configured in a given SSE config folder?
  phrasing_ops: 12
  slug: palo-alto-networks-service-connections-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: Service Groups
  name: Palo Alto Networks Service Groups API
  phrasing_intents:
  - id: ListServiceGroups
    intent: List service groups
    question: Which service groups are defined in a given folder?
  - id: CreateServiceGroups
    intent: Create a service group
    question: How do I bundle several services into one group for security rules?
  - id: GetServiceGroupsByID
    intent: Get a service group
    question: Which services belong to a specific service group?
  - id: UpdateServiceGroupsByID
    intent: Update a service group
    question: Can I add a service to an existing service group?
  - id: DeleteServiceGroupsByID
    intent: Delete a service group
    question: How do I remove a service group?
  - id: get-sse-config-v1-service-groups
    intent: List service groups
    question: Which service groups exist in a configuration folder?
  - id: post-sse-config-v1-service-groups
    intent: Create a service group
    question: How do I bundle several services into one service group?
  - id: delete-sse-config-v1-service-groups-id
    intent: Delete a service group
    question: How do I delete a service group?
  phrasing_ops: 10
  slug: palo-alto-networks-service-groups-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: Service Route Settings
  name: Palo Alto Networks Service Route Settings API
  phrasing_intents:
  - id: ListServiceRouteSettings
    intent: List service route settings
    question: Which service routes are configured on my firewalls?
  - id: CreateServiceRouteSettings
    intent: Create service route settings
    question: How do I define which interface a firewall uses to reach services like DNS or syslog?
  - id: GetServiceRouteSettingsByID
    intent: Get service route settings
    question: What routes are in a particular service route settings entry?
  - id: UpdateServiceRouteSettingsByID
    intent: Update service route settings
    question: How do I change the routes in existing service route settings?
  - id: DeleteServiceRouteSettingsByID
    intent: Delete service route settings
    question: How do I delete a service route settings entry?
  phrasing_ops: 5
  slug: palo-alto-networks-service-route-settings-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: Services Settings
  name: Palo Alto Networks Service Settings API
  phrasing_intents:
  - id: ListServiceSettings
    intent: List service settings
    question: What device service settings are configured, like DNS and NTP servers?
  - id: CreateServiceSettings
    intent: Create service settings
    question: How do I define new device service settings?
  - id: GetServiceSettingsByID
    intent: Get service settings
    question: What does one service settings object contain?
  - id: UpdateServiceSettingsByID
    intent: Update service settings
    question: How do I change existing device service settings?
  - id: DeleteServiceSettingsByID
    intent: Delete service settings
    question: How do I delete a service settings object?
  phrasing_ops: 5
  slug: palo-alto-networks-service-settings-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: Session Settings
  name: Palo Alto Networks Session Settings API
  phrasing_intents:
  - id: ListSessionSettings
    intent: List session settings
    question: What session settings are configured in a folder?
  - id: CreateSessionSettings
    intent: Create session settings
    question: How do I define new firewall session settings?
  - id: GetSessionSettingsByID
    intent: Get session settings
    question: Can I view one session settings object by UUID?
  - id: UpdateSessionSettingsByID
    intent: Update session settings
    question: How do I change existing session settings?
  - id: DeleteSessionSettingsByID
    intent: Delete session settings
    question: Is there a way to remove a session settings object?
  phrasing_ops: 5
  slug: palo-alto-networks-session-settings-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: Session Timeouts Settings
  name: Palo Alto Networks Session Timeouts Settings API
  phrasing_intents:
  - id: ListSessionTimeoutsSettings
    intent: List session timeout settings
    question: Which session timeout settings are configured across my firewalls?
  - id: CreateSessionTimeoutsSettings
    intent: Create session timeout settings
    question: How do I set custom TCP and UDP session timeouts?
  - id: GetSessionTimeoutsSettingsByID
    intent: Get session timeout settings
    question: What timeout values does one session settings entry use?
  - id: UpdateSessionTimeoutsSettingsByID
    intent: Update session timeout settings
    question: How do I change an existing session timeout value?
  - id: DeleteSessionTimeoutsSettingsByID
    intent: Delete session timeout settings
    question: Which call removes a session timeout settings entry?
  phrasing_ops: 5
  slug: palo-alto-networks-session-timeouts-settings-api
- baseURL: https://api.strata.paloaltonetworks.com/config/deployment/v1
  baseurl_source: declared
  description: Shared infrastructure settings
  name: Palo Alto Networks Shared Infrastructure Settings API
  phrasing_intents:
  - id: GetSharedInfrastructureSettings
    intent: Get Prisma Access shared infrastructure settings
    question: What infrastructure subnet and BGP AS is Prisma Access using?
  - id: UpdateSharedInfrastructureSettings
    intent: Update Prisma Access infrastructure settings
    question: How do I change the infrastructure subnet Prisma Access uses?
  phrasing_ops: 2
  slug: palo-alto-networks-shared-infrastructure-settings-api
- baseURL: https://api.strata.paloaltonetworks.com/config/setup/v1
  baseurl_source: declared
  description: Shared Snippets
  name: Palo Alto Networks Shared Snippets API
  phrasing_intents:
  - id: ListSharedSnippets
    intent: List shared snippets
    question: Which shared configuration snippets are available to me?
  - id: ConvertSharedSnippets
    intent: Update a shared snippet
    question: How do I pull the latest version of a shared snippet?
  - id: LoadSharedSnippets
    intent: Load a shared snippet into configuration
    question: How do I load a shared snippet so it can be used in my config?
  phrasing_ops: 3
  slug: palo-alto-networks-shared-snippets-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/signup/signup.md''}'
  name: Palo Alto Networks Signup API
  phrasing_intents:
  - id: post-signup
    intent: Create the initial admin account
    question: How do I create the first admin account on a new Compute console?
  phrasing_ops: 1
  slug: palo-alto-networks-signup-api
- baseURL: https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1
  baseurl_source: declared
  description: Onboarding Site Groups Information
  name: Palo Alto Networks Site Groups API
  phrasing_intents:
  - id: createSiteGroup
    intent: Create a site group
    question: How do I create a site group with its own list of properties?
  - id: listSiteGroups
    intent: List site groups
    question: What site groups exist in my tenant?
  - id: getSiteGroupByID
    intent: Get a site group
    question: What properties does a particular site group define?
  - id: updateSiteGroupByID
    intent: Update a site group
    question: Why would renaming a site group be blocked?
  - id: deleteSiteGroupByID
    intent: Delete a site group
    question: Can I delete a site group that sites or onboarding rules still use?
  phrasing_ops: 5
  slug: palo-alto-networks-site-groups-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Sites API
  name: Palo Alto Networks Sites API
  phrasing_intents:
  - id: post-insights-v3.0-resource-query-sites-bandwidth_consumption_histogram
    intent: Get a site bandwidth consumption histogram
    question: How is bandwidth consumption distributed across my Prisma Access sites?
  - id: post-insights-v3.0-resource-query-sites-session_count
    intent: Count sessions across sites
    question: How many sessions are my sites handling?
  - id: post-insights-v3.0-resource-query-sites-site_count
    intent: Count sites
    question: How many sites do I have in Prisma Access Insights?
  - id: post-insights-v3.0-resource-query-sites-site_location_search_contains
    intent: Search sites by location
    question: Which sites are in a particular city or location?
  - id: post-insights-v3.0-resource-query-sites-site_traffic
    intent: Get detailed site traffic
    question: What does traffic look like at each of my sites?
  phrasing_ops: 5
  slug: palo-alto-networks-sites-api-api
- baseURL: https://api.strata.paloaltonetworks.com/config/setup/v1
  baseurl_source: declared
  description: Snippet Audit Logs
  name: Palo Alto Networks Snippet Audit Logs API
  phrasing_intents:
  - id: GetSnippetAuditLogsByID
    intent: Get snippet audit logs
    question: What's the audit trail for a snippet shared between tenants?
  - id: CreateSnippetAuditLogs
    intent: Record a snippet audit log entry
    question: How do I record that a snippet was shared from one tenant to another?
  phrasing_ops: 2
  slug: palo-alto-networks-snippet-audit-logs-api
- baseURL: https://api.strata.paloaltonetworks.com/config/setup/v1
  baseurl_source: declared
  description: Configuration snippets and category information
  name: Palo Alto Networks Snippet Categories API
  phrasing_intents:
  - id: ListSnippetCategories
    intent: List snippet categories
    question: What categories are available for organizing configuration snippets?
  - id: GetSnippetCategoryByID
    intent: Get a snippet category
    question: How do I look up a single snippet category by its ID?
  - id: DeleteSnippetCategoryByID
    intent: Delete a snippet category
    question: Can I remove a snippet category I no longer use?
  phrasing_ops: 3
  slug: palo-alto-networks-snippet-categories-api
- baseURL: https://api.strata.paloaltonetworks.com/config/setup/v1
  baseurl_source: declared
  description: Snippet Snapshots
  name: Palo Alto Networks Snippet Snapshots API
  phrasing_intents:
  - id: SaveSnippetSnapshot
    intent: Save a snapshot of a snippet
    question: Can I save the current state of a configuration snippet as a snapshot?
  - id: PublishSnippetSnapshot
    intent: Publish a snippet snapshot to tenants
    question: How do I push a snippet snapshot out to other tenant service groups?
  - id: CompareSnippetSnapshot
    intent: Compare two versions of a snippet
    question: What changed in a snippet between two snapshot versions?
  - id: DiffSnippetSnapshot
    intent: Diff one object inside a snippet across versions
    question: How did a single object inside a snippet change between snapshot versions?
  - id: LoadSnippetSnapshot
    intent: Load (roll back to) a snippet snapshot
    question: Can I roll a snippet back to an earlier saved snapshot?
  - id: UpdateSnippetSnapshot
    intent: Pull snippet snapshot updates for a tenant
    question: Can I apply the latest snapshot updates of a snippet to a particular tenant?
  - id: ConvertSnippetSnapshot
    intent: Convert a snippet snapshot
    question: Can I convert a snippet snapshot and keep a local copy?
  phrasing_ops: 7
  slug: palo-alto-networks-snippet-snapshots-api
- baseURL: https://api.strata.paloaltonetworks.com/config/setup/v1
  baseurl_source: declared
  description: Configuration snippets
  name: Palo Alto Networks Snippets API
  phrasing_intents:
  - id: ListSnippets
    intent: List configuration snippets
    question: What configuration snippets exist in my Strata Cloud Manager tenant?
  - id: CreateSnippet
    intent: Create a configuration snippet
    question: How do I create a reusable configuration snippet in Strata Cloud Manager?
  - id: GetSnippetByID
    intent: Get a configuration snippet
    question: How do I look up a single snippet by its UUID?
  - id: UpdateSnippetByID
    intent: Update a configuration snippet
    question: Can I rename an existing snippet or change its labels?
  - id: DeleteSnippetByID
    intent: Delete a configuration snippet
    question: How do I remove a snippet I no longer use?
  phrasing_ops: 5
  slug: palo-alto-networks-snippets-api
- baseURL: https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
  baseurl_source: declared
  description: Source Applications
  name: Palo Alto Networks Source Applications API
  phrasing_intents:
  - id: ListGlobalProtectSourceApplications
    intent: List GlobalProtect source applications
    question: Which GlobalProtect source applications are defined for forwarding profiles?
  - id: CreateGlobalProtectSourceApplication
    intent: Create a GlobalProtect source application
    question: How do I group applications into a source application for a forwarding profile?
  - id: GetGlobalProtectSourceApplicationByID
    intent: Get a GlobalProtect source application
    question: Which applications are in one GlobalProtect source application?
  - id: UpdateGlobalProtectSourceApplicationByID
    intent: Update a GlobalProtect source application
    question: Can I add more apps to an existing GlobalProtect source application?
  - id: DeleteGlobalProtectSourceApplication
    intent: Delete a GlobalProtect source application
    question: How do I delete a GlobalProtect source application?
  phrasing_ops: 5
  slug: palo-alto-networks-source-applications-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: Ssl Decrypt
  name: Palo Alto Networks Ssl Decryption Settings API
  phrasing_intents:
  - id: getSslDecryptionSettings
    intent: Get SSL decryption settings
    question: Which forward trust and untrust certificates are used for SSL decryption?
  - id: postSslDecryptionSettings
    intent: Create SSL decryption settings
    question: How do I set the forward trust certificate for SSL decryption the first time?
  - id: putSslDecryptionSettings
    intent: Replace SSL decryption settings
    question: How do I overwrite the existing SSL decryption settings?
  - id: deleteSslDecryptionSettings
    intent: Delete SSL decryption settings
    question: Can I clear out the SSL decryption settings entirely?
  phrasing_ops: 4
  slug: palo-alto-networks-ssl-decryption-settings-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: On Prisma Cloud, you can enable single sign-on (SSO) using an Identity Provider (IdP) that supports Security Assertion Markup Language (SAML) or OpenID Connect (OIDC), such as Okta, Microsoft Active D
  name: Palo Alto Networks SSO API
  phrasing_intents:
  - id: get-saml-config
    intent: Get the tenant SAML configuration
    question: How is SAML single sign-on currently set up for my Prisma Cloud tenant?
  - id: update-saml-config
    intent: Update the tenant SAML configuration
    question: Can I rotate the IdP certificate on an existing SAML setup?
  - id: create-saml-config
    intent: Create the tenant SAML configuration
    question: How do I set up SAML SSO for the first time on my tenant?
  - id: get-oauth2-config
    intent: Get the tenant OIDC configuration
    question: What OpenID Connect settings does my tenant use for sign-in?
  - id: update-oauth2-config
    intent: Replace the tenant OIDC configuration
    question: How do I overwrite every setting of our OIDC configuration at once?
  - id: create-oauth2-config
    intent: Create the tenant OIDC configuration
    question: How do I set up OpenID Connect sign-in for my tenant for the first time?
  - id: patch-oauth2-config
    intent: Partially update the tenant OIDC configuration
    question: Can I change just one OIDC setting without resending the whole configuration?
  - id: get-oidc-login-url
    intent: Get the OIDC login URL
    question: Where do users go to sign in to my tenant with OpenID Connect?
  phrasing_ops: 8
  slug: palo-alto-networks-sso-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/statuses/statuses.md''}'
  name: Palo Alto Networks Statuses API
  phrasing_intents:
  - id: get-statuses-buildah
    intent: Get buildah feature status (v34.03)
    question: Is the buildah feature enabled according to the v34.03 API?
  - id: get-statuses-registry
    intent: Get registry scan status (v34.03)
    question: Is a registry scan currently running, per the v34.03 API?
  - id: getApiV3404StatusesBuildah
    intent: Get buildah feature status (v34.04)
    question: Is buildah enabled in the current v34.04 API?
  - id: getApiV3404StatusesRegistry
    intent: Get registry scan status (v34.04)
    question: What is the status of the latest registry scan on v34.04?
  phrasing_ops: 4
  slug: palo-alto-networks-statuses-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Subnet API from Palo Alto Networks — 3 operation(s) for subnet.
  name: Palo Alto Networks Subnet API
  phrasing_intents:
  - id: list.subnet_rules.v2
    intent: List connector subnets
    question: Which subnets are defined in my ZTNA connector setup?
  - id: create.subnet_rule.v2
    intent: Create a connector subnet
    question: How do I add a subnet to a connector group?
  - id: get.subnet_rule.v2
    intent: Get a connector subnet
    question: What IP ranges and group does a specific connector subnet have?
  - id: update.subnet_rule.v2
    intent: Update a connector subnet
    question: Can I change the IP ranges on an existing connector subnet?
  - id: delete.subnet_rule.v2
    intent: Delete a connector subnet
    question: How do I remove a subnet from my connector configuration?
  - id: list.subnet_rules.filters.v2
    intent: Get filter values for subnet fields
    question: What values can I filter connector subnets on for a given field?
  phrasing_ops: 6
  slug: palo-alto-networks-subnet-api
- baseURL: https://api.strata.paloaltonetworks.com/config/setup/v1
  baseurl_source: declared
  description: Subscribed Tenants information
  name: Palo Alto Networks Subscribed Tenants API
  phrasing_intents:
  - id: ListSubscribedTenantsByID
    intent: List tenants subscribed to a snippet
    question: Which tenants are subscribed to a shared configuration snippet?
  - id: CreateSubscribedTenant
    intent: Subscribe a tenant to a snippet
    question: How do I subscribe a tenant to a shared snippet?
  - id: UpdateSubscribedTenantBySnippetID
    intent: Update a snippet's subscribed tenant
    question: Can I change the properties of a tenant's subscription to a snippet?
  - id: DeleteSubscribedTenantBySnippedID
    intent: Unsubscribe tenants from a snippet
    question: How do I remove tenants from a snippet subscription?
  phrasing_ops: 4
  slug: palo-alto-networks-subscribed-tenants-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The Summary API API from Palo Alto Networks — 3 operation(s) for summary api.
  name: Palo Alto Networks Summary API
  phrasing_intents:
  - id: PostMtPabSummary
    intent: Count configured Prisma Browser users
    question: How many users are configured for Prisma Browser in a given region?
  - id: PostMtPabSummaryCie
    intent: Get Cloud Identity Engine summary
    question: What does the Cloud Identity Engine summary show for a region?
  - id: PostMtPabSummaryTenants
    intent: Summarize tenants in a region
    question: What summary information is available for all my tenants in one region?
  phrasing_ops: 3
  slug: palo-alto-networks-summary-api-api
- baseURL: https://api.strata.paloaltonetworks.com/config/objects/v1
  baseurl_source: declared
  description: Syslog Server Profiles
  name: Palo Alto Networks Syslog Server Profiles API
  phrasing_intents:
  - id: ListSyslogServerProfiles
    intent: List syslog server profiles
    question: Which syslog server profiles are set up for log forwarding?
  - id: CreateSyslogServerProfiles
    intent: Create a syslog server profile
    question: How do I forward firewall logs to my own syslog server?
  - id: GetSyslogServerProfilesByID
    intent: Get a syslog server profile
    question: Where can I see the servers in one syslog profile?
  - id: UpdateSyslogServerProfilesByID
    intent: Update a syslog server profile
    question: How do I change the destination servers of a syslog profile?
  - id: DeleteSyslogServerProfilesByID
    intent: Delete a syslog server profile
    question: Can I stop forwarding logs by removing a syslog profile?
  phrasing_ops: 5
  slug: palo-alto-networks-syslog-server-profiles-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The SyslogProfiles API from Palo Alto Networks — 2 operation(s) for syslogprofiles.
  name: Palo Alto Networks Syslog Profiles API
  phrasing_intents:
  - id: get-logging-service-logforwarding-v1-syslog-profiles
    intent: List syslog forwarding profiles
    question: What syslog profiles do I have for log forwarding?
  - id: post-logging-service-logforwarding-v1-syslog-profiles
    intent: Create a syslog forwarding profile
    question: How do I start sending logs to my syslog server?
  - id: delete-logging-service-logforwarding-v1-syslog-profiles-profileid
    intent: Delete a syslog profile
    question: How do I stop forwarding logs by deleting a syslog profile?
  - id: get-logging-service-logforwarding-v1-syslog-profiles-profileid
    intent: Get a syslog profile
    question: How can I see one syslog profile and its etag?
  - id: put-logging-service-logforwarding-v1-syslog-profiles-profileid
    intent: Update a syslog profile
    question: Can I change where an existing syslog profile sends logs?
  phrasing_ops: 5
  slug: palo-alto-networks-syslogprofiles-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Quickly check if Prisma Cloud is available.
  name: Palo Alto Networks System API
  phrasing_intents:
  - id: health-check
    intent: Check that the Prisma Cloud API is up
    question: Is the Prisma Cloud API up and running right now?
  phrasing_ops: 1
  slug: palo-alto-networks-system-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: System Match List
  name: Palo Alto Networks System Match List API
  phrasing_intents:
  - id: ListSystemMatchList
    intent: List system log match list entries
    question: Which system log match lists are forwarding logs to syslog or email?
  - id: CreateSystemMatchList
    intent: Create a system log match list entry
    question: How do I forward system logs matching a filter to a syslog server?
  - id: GetSystemMatchListByID
    intent: Get a system match list entry
    question: What filter and destinations does a specific system match list use?
  - id: UpdateSystemMatchListByID
    intent: Update a system match list entry
    question: How do I change the log filter on an existing system match list?
  - id: DeleteSystemMatchListByID
    intent: Delete a system match list entry
    question: How do I remove a system log match list entry?
  phrasing_ops: 5
  slug: palo-alto-networks-system-match-list-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: TACACS Server Profiles
  name: Palo Alto Networks TACACS Server Profiles API
  phrasing_intents:
  - id: ListTACACSServerProfiles
    intent: List TACACS+ server profiles
    question: Which TACACS+ server profiles are configured for admin authentication?
  - id: CreateTACACSServerProfiles
    intent: Create a TACACS+ server profile
    question: How do I add a TACACS+ server profile with a chosen authentication protocol?
  - id: GetTACACSServerProfilesByID
    intent: Get a TACACS+ server profile
    question: What servers and protocol does a particular TACACS+ profile use?
  - id: UpdateTACACSServerProfilesByID
    intent: Update a TACACS+ server profile
    question: How do I change the servers listed in an existing TACACS+ profile?
  - id: DeleteTACACSServerProfilesByID
    intent: Delete a TACACS+ server profile
    question: How do I remove a TACACS+ server profile?
  - id: get-sse-config-v1-tacacs-server-profiles
    intent: List TACACS+ server profiles
    question: Which TACACS+ server profiles does the SSE config v1 endpoint list for a folder, snippet or device?
  - id: post-sse-config-v1-tacacs-server-profiles
    intent: Create a TACACS+ server profile
    question: How do I add a TACACS+ server for administrator authentication?
  - id: delete-sse-config-v1-tacacs-server-profiles-id
    intent: Delete a TACACS+ server profile
    question: How do I delete a TACACS server profile?
  phrasing_ops: 10
  slug: palo-alto-networks-tacacs-server-profiles-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Tag Rules API from Palo Alto Networks — 4 operation(s) for tag rules.
  name: Palo Alto Networks Tag Rules API
  phrasing_intents:
  - id: getTags
    intent: List IaC tag rules
    question: Which tag rules are applied to our IaC templates?
  - id: saveTag
    intent: Create a custom IaC tag rule
    question: How do I create a rule that automatically tags resources in my IaC?
  - id: getTag
    intent: Get a tag rule
    question: What does one specific tag rule define?
  - id: updateTag
    intent: Update an IaC tag rule
    question: How do I change the definition of a tag rule I already created for my IaC templates?
  - id: deleteTag
    intent: Delete an IaC tag rule
    question: How do I permanently remove a tag rule from Application Security?
  - id: getAffectedResources
    intent: Preview resources a tag rule would affect
    question: Which resources would a tag rule change before I save it?
  - id: getTagOOTBRules
    intent: Get an out-of-the-box tag rule
    question: What does a built-in (out-of-the-box) tag rule do?
  phrasing_ops: 7
  slug: palo-alto-networks-tag-rules-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Tags API from Palo Alto Networks — 10 operation(s) for tags.
  name: Palo Alto Networks Tags API
  phrasing_intents:
  - id: get-sse-config-v1-tags
    intent: List SSE config tags in a folder
    question: Which tags are defined in my Shared SSE configuration folder?
  - id: post-sse-config-v1-tags
    intent: Create an SSE config tag in a folder
    question: How do I add a new tag to an SSE configuration folder?
  - id: delete-sse-config-v1-tags-id
    intent: Delete an SSE config tag
    question: How do I remove a tag from my SSE configuration?
  - id: get-sse-config-v1-tags-id
    intent: Get an SSE config tag by ID
    question: How can I see the color and comments of one SSE configuration tag by its UUID?
  - id: put-sse-config-v1-tags-id
    intent: Edit an SSE config tag
    question: Can I rename or recolor an existing SSE configuration tag?
  - id: get-tags
    intent: List vulnerability tags (Compute v34.03)
    question: Which vulnerability tags exist in Compute on the v34.03 API?
  - id: post-tags
    intent: Add a vulnerability tag (Compute v34.03)
    question: How do I create a vulnerability tag via the v34.03 Compute API?
  - id: delete-tags-id
    intent: Delete a vulnerability tag (Compute v34.03)
    question: How do I delete a whole Compute tag through the v34.03 API?
  phrasing_ops: 22
  slug: palo-alto-networks-tags-api
- baseURL: https://api.sase.paloaltonetworks.com/ai-red-teaming/mgmt-plane
  baseurl_source: declared
  description: Operations for managing scan targets (create, update, delete, list).
  name: Palo Alto Networks Target API
  phrasing_intents:
  - id: create_target_v1_target_post
    intent: Create a scan target
    question: How do I register a new target to scan?
  - id: list_targets_v1_target_get
    intent: List scan targets
    question: Which AI red-teaming scan targets have I configured?
  - id: get_target_v1_target__target_uuid__get
    intent: Get a scan target's details
    question: What configuration is stored for a particular scan target?
  - id: update_target_v1_target__target_uuid__put
    intent: Update a scan target
    question: Can I change a target's connection settings after creating it?
  - id: delete_target_v1_target__target_uuid__delete
    intent: Delete a scan target
    question: Can I permanently remove a scan target I no longer need?
  - id: start_profiling_v1_target__target_uuid__profile_post
    intent: Start profiling a target
    question: Can I manually kick off profiling for a target?
  - id: update_target_profile_v1_target__target_uuid__profile_put
    intent: Edit a target's background context
    question: Can I edit a target's background and extra context without revalidating the connection?
  - id: get_profiling_results_v1_target__target_uuid__profile_get
    intent: Get a target's profiling results
    question: What did profiling learn about my target?
  phrasing_ops: 13
  slug: palo-alto-networks-target-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The Tas-Droplets API from Palo Alto Networks — 12 operation(s) for tas-droplets.
  name: Palo Alto Networks Tas Droplets API
  phrasing_intents:
  - id: get-tas-droplets
    intent: List scanned TAS droplets (v34.03)
    question: Using the v34.03 API, which Tanzu Application Service droplets have been scanned?
  - id: get-tas-droplets-addresses
    intent: List TAS cloud controller addresses (v34.03)
    question: What TAS cloud controller addresses does the v34.03 API know about?
  - id: get-tas-droplets-download
    intent: Download TAS droplet scan results (v34.03)
    question: How do I export TAS droplet scan results with the v34.03 API?
  - id: get-tas-droplets-progress
    intent: View TAS droplet scan progress (v34.03)
    question: How far along is the TAS droplet scan according to the v34.03 API?
  - id: post-tas-droplets-scan
    intent: Start a TAS droplet scan (v34.03)
    question: How do I kick off a TAS droplet scan with the v34.03 API?
  - id: post-tas-droplets-stop
    intent: Stop an ongoing TAS droplet scan (v34.03)
    question: Can I cancel a TAS droplet scan in progress with the v34.03 API?
  - id: getApiV3404TasDroplets
    intent: List scanned TAS droplets (v34.04)
    question: Which Tanzu droplets have vulnerabilities in the current v34.04 API?
  - id: getApiV3404TasDropletsAddresses
    intent: List TAS cloud controller addresses (v34.04)
    question: Which cloud controller addresses does the v34.04 TAS droplet API return?
  phrasing_ops: 12
  slug: palo-alto-networks-tas-droplets-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: TCP Settings
  name: Palo Alto Networks TCP Settings API
  phrasing_intents:
  - id: ListTCPSettings
    intent: List TCP settings
    question: What TCP settings are configured for my firewalls?
  - id: CreateTCPSettings
    intent: Create TCP settings
    question: How do I define new TCP session settings?
  - id: GetTCPSettingsByID
    intent: Get TCP settings by ID
    question: What values does a specific TCP settings object hold?
  - id: UpdateTCPSettingsByID
    intent: Update TCP settings
    question: Can I change an existing TCP settings object?
  - id: DeleteTCPSettingsByID
    intent: Delete TCP settings
    question: Can I remove a TCP settings object?
  phrasing_ops: 5
  slug: palo-alto-networks-tcp-settings-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The Technologies API from Palo Alto Networks — 4 operation(s) for technologies.
  name: Palo Alto Networks Technologies API
  phrasing_intents:
  - id: getApps
    intent: List third-party apps in version control
    question: Which third-party apps are installed in our version control system?
  - id: getWebhooks
    intent: List third-party webhooks in version control
    question: What third-party webhooks are configured across our repositories?
  - id: assetsInventoryGetAll
    intent: List technologies and their sources
    question: What technologies are used across our code, and where does each come from?
  - id: getCiInventory
    intent: List CI/CD pipeline tools
    question: Which third-party services and tools do our CI/CD pipelines use?
  phrasing_ops: 4
  slug: palo-alto-networks-technologies-api
- baseURL: https://api.sase.paloaltonetworks.com/ai-red-teaming/data-plane
  baseurl_source: declared
  description: Operations for managing scan templates and configurations.
  name: Palo Alto Networks Templates API
  phrasing_intents:
  - id: get_scan_metadata_v1_scan_scan_metadata_get
    intent: Get metadata for red teaming scan targets
    question: What metadata is available about my AI red teaming scan targets?
  phrasing_ops: 1
  slug: palo-alto-networks-templates-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The Tenant API API from Palo Alto Networks — 6 operation(s) for tenant api.
  name: Palo Alto Networks Tenant API
  phrasing_intents:
  - id: PostMtPabTenant
    intent: Create a managed tenant
    question: How do I provision a new managed tenant in a specific region?
  - id: GetMtPabTenantAuth_profile
    intent: List tenant authentication profiles
    question: Which authentication profiles can I assign to a new tenant?
  - id: GetMtPabTenantDirectories
    intent: List available directories
    question: Which user directories are available for tenant onboarding?
  - id: GetMtPabTenantLicenses
    intent: Get tenant license utilization
    question: How many licenses have we used and how many remain?
  - id: GetMtPabTenantRegion
    intent: List tenant deployment regions
    question: In which regions can I deploy a new tenant?
  - id: PostMtPabTenantUser_group
    intent: List user groups in a directory
    question: Which user groups exist in a particular directory?
  phrasing_ops: 6
  slug: palo-alto-networks-tenant-api-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Tenant API from Palo Alto Networks — 4 operation(s) for tenant.
  name: Palo Alto Networks Tenant API
  phrasing_intents:
  - id: get.license.v2
    intent: Get the tenant's license details
    question: What license does my SSE connector tenant currently have?
  - id: start_onboarding.v2
    intent: Start onboarding a tenant
    question: How do I kick off onboarding for a new SSE connector tenant?
  - id: start_offboarding.v2
    intent: Offboard and delete a tenant
    question: How do I mark my tenant for deletion and trigger cleanup?
  - id: get.tenant.status.v2
    intent: Check the tenant's current status
    question: Is my tenant still onboarding, active, or being deleted?
  phrasing_ops: 4
  slug: palo-alto-networks-tenant-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Use the Tenant Resource API to list all tenants in the hierarchy.
  name: Palo Alto Networks Tenant Resources API
  phrasing_intents:
  - id: get-mt-monitor-v1-agg-custom-tenant-hierarchy
    intent: List the tenant hierarchy
    question: Which tenants sit under my multitenant hierarchy?
  phrasing_ops: 1
  slug: palo-alto-networks-tenant-resources-api-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The TenantServiceGroup API from Palo Alto Networks — 4 operation(s) for tenantservicegroup.
  name: Palo Alto Networks Tenant Service Group API
  phrasing_intents:
  - id: get-tenancy-v1-tenant_service_groups
    intent: List tenant service groups
    question: Which tenant service groups can my service account see?
  - id: post-tenancy-v1-tenant_service_groups
    intent: Create a tenant service group
    question: How do I create a new tenant under a parent TSG?
  - id: delete-tenancy-v1-tenant_service_groups-tsg_id
    intent: Delete a tenant service group
    question: How do I delete a tenant service group?
  - id: get-tenancy-v1-tenant_service_groups-tsg_id
    intent: Get a tenant service group
    question: How do I look up a tenant service group by TSG ID?
  - id: put-tenancy-v1-tenant_service_groups-tsg_id
    intent: Update a tenant service group
    question: Can I change the display name or support contact of a tenant service group?
  - id: post-tenancy-v1-tenant_service_groups-tsg_id-operations-list_ancestors
    intent: List a tenant's ancestor TSGs
    question: What are the parent tenants above a given TSG, up to the root?
  - id: post-tenancy-v1-tenant_service_groups-tsg_id-operations-list_children
    intent: List a tenant's child TSGs
    question: Which child tenants sit directly under a tenant service group?
  phrasing_ops: 7
  slug: palo-alto-networks-tenantservicegroup-api
- baseURL: https://api.threatvault.paloaltonetworks.com/service/v1
  baseurl_source: declared
  description: The Threat Prevention API from Palo Alto Networks — 6 operation(s) for threat prevention.
  name: Palo Alto Networks Threat Prevention API
  phrasing_intents:
  - id: getCVECoverage
    intent: Check threat coverage for a CVE
    question: Does Palo Alto Networks threat prevention cover a specific CVE?
  - id: releasenotes
    intent: Get content release notes
    question: What changed in a particular content release version?
  - id: threats
    intent: Look up threat signatures
    question: Which Threat Vault signatures cover a given CVE?
  - id: threatsbatch
    intent: Batch look up threat signatures
    question: Can I look up up to 100 threat signatures at once by id or hash?
  - id: threatshistory
    intent: Get a signature's release history
    question: When was a threat signature first released and modified?
  - id: edl
    intent: Get predefined external dynamic list content
    question: What IPs are in a predefined external dynamic list?
  - id: ip_feed
    intent: Look up IP feed information
    question: Which IP feed is an address listed in?
  - id: ip_feed_batch
    intent: Batch look up IP feed entries
    question: Can I check up to 100 IP addresses against the IP feed in one request?
  phrasing_ops: 8
  slug: palo-alto-networks-threat-prevention-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for TLS Server Endpoints.
  name: Palo Alto Networks TLS Server Endpoints API
  phrasing_intents:
  - id: certificateinstances_getAll
    intent: List certificate installations on TLS endpoints
    question: Where is each certificate installed across my TLS server endpoints?
  - id: certificateinstances_getById
    intent: Get a certificate installation's details
    question: How do I see the details of one certificate installation on a TLS endpoint?
  - id: certificateinstances_validation
    intent: Request TLS validation of certificate installations
    question: How do I recheck that certificates are correctly installed on specific TLS endpoints?
  - id: certificateinstances_search_getByExpression
    intent: Search certificate installations by criteria
    question: Which TLS endpoints are serving certificates that expire soon?
  phrasing_ops: 4
  slug: palo-alto-networks-tls-server-endpoints-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: TLS Service Profiles
  name: Palo Alto Networks TLS Service Profiles API
  phrasing_intents:
  - id: ListTLSServiceProfiles
    intent: List TLS service profiles
    question: Which TLS service profiles are configured in a folder?
  - id: CreateTLSServiceProfiles
    intent: Create a TLS service profile
    question: How do I create a TLS service profile with a certificate and protocol versions?
  - id: GetTLSServiceProfilesByID
    intent: Get a TLS service profile
    question: Which certificate and protocol versions does a TLS service profile use?
  - id: UpdateTLSServiceProfilesByID
    intent: Update a TLS service profile
    question: Can I swap the certificate on an existing TLS service profile?
  - id: DeleteTLSServiceProfilesByID
    intent: Delete a TLS service profile
    question: How do I remove a TLS service profile?
  - id: get-sse-config-v1-tls-service-profiles
    intent: List TLS service profiles
    question: Which TLS service profiles are configured in my folder?
  - id: post-sse-config-v1-tls-service-profiles
    intent: Create a TLS service profile
    question: How do I create a TLS service profile that uses a specific SSL certificate?
  - id: delete-sse-config-v1-tls-service-profiles-id
    intent: Delete a TLS service profile
    question: How do I remove a TLS service profile I'm no longer using?
  phrasing_ops: 10
  slug: palo-alto-networks-tls-service-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/deployment/v1
  baseurl_source: declared
  description: Traffic steering rules for Service Connections
  name: Palo Alto Networks Traffic Steering Rules API
  phrasing_intents:
  - id: ListTrafficSteeringRules
    intent: List Service Connection traffic steering rules
    question: Which traffic steering rules route traffic to Service Connections?
  - id: CreateTrafficSteeringRules
    intent: Create a traffic steering rule
    question: How do I steer certain traffic through a Service Connection?
  - id: GetTrafficSteeringRulesByID
    intent: Get a traffic steering rule
    question: What source, destination and action does a specific steering rule use?
  - id: UpdateTrafficSteeringRulesByID
    intent: Update a traffic steering rule
    question: How do I change the action on an existing steering rule?
  - id: DeleteTrafficSteeringRulesByID
    intent: Delete a traffic steering rule
    question: How do I remove a traffic steering rule?
  - id: get-sse-config-v1-traffic-steering-rules
    intent: List traffic steering rules
    question: Which traffic steering rules send traffic to my service connections?
  - id: post-sse-config-v1-traffic-steering-rules
    intent: Create a traffic steering rule
    question: How do I steer traffic from certain sources to a service connection?
  - id: delete-sse-config-v1-traffic-steering-rules-id
    intent: Delete a traffic steering rule
    question: How do I remove a traffic steering rule using the SSE config v1 path?
  phrasing_ops: 10
  slug: palo-alto-networks-traffic-steering-rules-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/trust/trust.md''}'
  name: Palo Alto Networks Trust API
  phrasing_intents:
  - id: get-trust-data
    intent: Get trusted images and registries (v34.03)
    question: Which repositories, images and registries are trusted, per the v34.03 API?
  - id: put-trust-data
    intent: Update trusted images and registries (v34.03)
    question: Can I change which images are trusted through the v34.03 endpoint?
  - id: getApiV3404TrustData
    intent: Get trusted images and registries (v34.04)
    question: Which repositories, images and registries are trusted, per the current v34.04 API?
  - id: putApiV3404TrustData
    intent: Update trusted images and registries (v34.04)
    question: Can I change which registries are trusted through the v34.04 endpoint?
  phrasing_ops: 4
  slug: palo-alto-networks-trust-api
- baseURL: https://api.strata.paloaltonetworks.com/config/setup/v1
  baseurl_source: declared
  description: Trust Information with shared snippets
  name: Palo Alto Networks Trust Information API
  phrasing_intents:
  - id: ListTrustedTenantsWithSnippets
    intent: List trusted tenants with snippets
    question: Which tenants do I trust to share configuration snippets with?
  phrasing_ops: 1
  slug: palo-alto-networks-trust-information-api
- baseURL: https://api.strata.paloaltonetworks.com/config/setup/v1
  baseurl_source: declared
  description: Validates trust information
  name: Palo Alto Networks Trust Validations API
  phrasing_intents:
  - id: ValidateTrust
    intent: Validate a trust between tenants
    question: Can I confirm a trust between a donor tenant and a recipient tenant is valid?
  phrasing_ops: 1
  slug: palo-alto-networks-trust-validations-api
- baseURL: https://api.strata.paloaltonetworks.com/config/identity/v1
  baseurl_source: declared
  description: Trusted Certificate Authorities
  name: Palo Alto Networks Trusted Certificate Authorities API
  phrasing_intents:
  - id: ListTrustedCertificateAuthorities
    intent: List trusted certificate authorities
    question: Which certificate authorities are on my trusted list?
  - id: get-sse-config-v1-trusted-certificate-authorities
    intent: List trusted certificate authorities
    question: Which certificate authorities are trusted in a Prisma Access folder?
  phrasing_ops: 2
  slug: palo-alto-networks-trusted-certificate-authorities-api
- baseURL: https://api.strata.paloaltonetworks.com/config/setup/v1
  baseurl_source: declared
  description: Overview of published and subscribed tenants
  name: Palo Alto Networks Trusted Tenants Overview API
  phrasing_intents:
  - id: GetTrustedTenantsOverview
    intent: Get trusted tenants overview
    question: Which tenants publish to or subscribe from mine?
  phrasing_ops: 1
  slug: palo-alto-networks-trusted-tenants-overview-api
- baseURL: https://api.strata.paloaltonetworks.com/config/setup/v1
  baseurl_source: declared
  description: Trusts between tenants
  name: Palo Alto Networks Trusts API
  phrasing_intents:
  - id: CreateTrust
    intent: Create a trust between tenants
    question: How do I set up a trust between a donor tenant and a recipient tenant?
  - id: DeleteTrust
    intent: Delete tenant trusts
    question: How do I remove a trust between tenants?
  phrasing_ops: 2
  slug: palo-alto-networks-trusts-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Tunnel Interfaces
  name: Palo Alto Networks Tunnel Interfaces API
  phrasing_intents:
  - id: ListTunnelInterfaces
    intent: List tunnel interfaces
    question: Which tunnel interfaces are configured on a device?
  - id: CreateTunnelInterfaces
    intent: Create a tunnel interface
    question: How do I add a tunnel interface for a VPN with an IP address?
  - id: GetTunnelInterfacesByID
    intent: Get a tunnel interface
    question: What IP addresses and MTU does a specific tunnel interface have?
  - id: UpdateTunnelInterfacesByID
    intent: Update a tunnel interface
    question: How do I change the MTU on an existing tunnel interface?
  - id: DeleteTunnelInterfacesByID
    intent: Delete a tunnel interface
    question: How do I delete a tunnel interface?
  phrasing_ops: 5
  slug: palo-alto-networks-tunnel-interfaces-api
- baseURL: https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
  baseurl_source: declared
  description: Tunnel Settings
  name: Palo Alto Networks Tunnel Settings API
  phrasing_intents:
  - id: ListGlobalProtectTunnelSettings
    intent: List GlobalProtect tunnel settings
    question: Which GlobalProtect tunnel settings are configured?
  - id: CreateGlobalProtectTunnelSettings
    intent: Create a GlobalProtect tunnel setting
    question: How do I create a new GlobalProtect tunnel setting for certain operating systems?
  - id: UpdateGlobalProtectTunnelSettings
    intent: Update a GlobalProtect tunnel setting
    question: How do I change split tunneling on an existing GlobalProtect tunnel setting?
  - id: DeleteGlobalProtectTunnelSettings
    intent: Delete a GlobalProtect tunnel setting
    question: How do I remove a GlobalProtect tunnel setting?
  phrasing_ops: 4
  slug: palo-alto-networks-tunnel-settings-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The UE Enrichment API from Palo Alto Networks — 2 operation(s) for ue enrichment.
  name: Palo Alto Networks UE Enrichment API
  phrasing_intents:
  - id: PostMtManage5gRegisterUe
    intent: Register a 5G subscriber session
    question: How does the 5G core tell Strata Cloud Manager that a device has attached?
  - id: PostMtManage5gDeregisterUe
    intent: End a 5G subscriber session
    question: How do I signal that a 5G device has disconnected?
  phrasing_ops: 2
  slug: palo-alto-networks-ue-enrichment-api
- baseURL: https://stratacloudmanager.paloaltonetworks.com
  baseurl_source: declared
  description: The UE Info Resource API API from Palo Alto Networks — 6 operation(s) for ue info resource api.
  name: Palo Alto Networks UE Info Resource API
  phrasing_intents:
  - id: PostMtManage5gTenantueinfo
    intent: Map a device's IMSI and IMEI to a tenant
    question: How do I onboard a 5G device by tying its IMSI and IMEI to a tenant?
  - id: PostMtManage5gTenantueinfoDelete
    intent: Bulk delete tenant device mappings
    question: How do I remove many tenant-to-device mappings at once when offboarding a tenant?
  - id: PostMtManage5gTenantueinfoList
    intent: List a tenant's device identity mappings
    question: Which IMSI and IMEI mappings belong to a given tenant service group?
  - id: PostMtManage5gTenantueinfoUpload
    intent: Bulk upload device identity mappings
    question: How do I onboard thousands of 5G devices at once from a file?
  - id: PutMtManage5gTenantueinfoBy_identity_id
    intent: Update a device identity mapping
    question: How do I fix a typo in a device's IMSI or IMEI mapping?
  - id: DeleteMtManage5gTenantueinfoBy_identity_id
    intent: Remove a single device identity mapping
    question: How do I delete the mapping for just one decommissioned device?
  - id: GetMtManage5gTenantueinfoBy_ueinfoid
    intent: Get one device identity record
    question: How do I look up the full identity record for one subscriber device?
  phrasing_ops: 7
  slug: palo-alto-networks-ue-info-resource-api-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: Update Schedule Settings
  name: Palo Alto Networks Update Schedule Settings API
  phrasing_intents:
  - id: ListUpdateScheduleSettings
    intent: List update schedule settings
    question: When are content and threat updates scheduled for a folder?
  - id: CreateUpdateScheduleSettings
    intent: Create update schedule settings
    question: How do I set up a schedule for dynamic updates?
  - id: GetUpdateScheduleSettingsByID
    intent: Get update schedule settings by ID
    question: What does a specific update schedule contain?
  - id: UpdateUpdateScheduleSettingsByID
    intent: Change update schedule settings
    question: Can I change when an existing update schedule runs?
  - id: DeleteUpdateScheduleSettingsByID
    intent: Delete update schedule settings
    question: How do I remove an update schedule?
  phrasing_ops: 5
  slug: palo-alto-networks-update-schedule-settings-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: URL Access Profiles
  name: Palo Alto Networks URL Access Profiles API
  phrasing_intents:
  - id: ListURLAccessProfiles
    intent: List URL access profiles
    question: Which URL filtering profiles are configured?
  - id: CreateURLAccessProfiles
    intent: Create a URL access profile
    question: How do I create a URL filtering profile that blocks certain categories?
  - id: GetURLAccessProfilesByID
    intent: Get a URL access profile
    question: Which categories does a particular URL access profile allow or block?
  - id: UpdateURLAccessProfilesByID
    intent: Update a URL access profile
    question: How do I add categories to the block list of an existing URL access profile?
  - id: DeleteURLAccessProfilesByID
    intent: Delete a URL access profile
    question: How do I remove a URL access profile?
  - id: get-sse-config-v1-url-access-profiles
    intent: List URL access profiles
    question: Which URL filtering access profiles exist in a folder?
  - id: post-sse-config-v1-url-access-profiles
    intent: Create a URL access profile
    question: Within a specific folder, how do I set up a URL filtering profile blocking chosen categories?
  - id: delete-sse-config-v1-url-access-profiles-id
    intent: Delete a URL access profile
    question: How do I delete a URL access profile?
  phrasing_ops: 10
  slug: palo-alto-networks-url-access-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: URL Admin Override
  name: Palo Alto Networks URL Admin Override API
  phrasing_intents:
  - id: URLAdminOverride
    intent: Get URL admin override settings
    question: What URL admin override settings are configured in a folder?
  - id: AddURLAdminOverride
    intent: Add a URL admin override
    question: How do I let admins override URL blocks with a password?
  - id: DeleteURLAdminOverrideByUUID
    intent: Delete a URL admin override
    question: How do I remove a URL admin override?
  phrasing_ops: 3
  slug: palo-alto-networks-url-admin-override-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: URL Categories
  name: Palo Alto Networks URL Categories API
  phrasing_intents:
  - id: ListURLCategories
    intent: List custom URL categories
    question: Which custom URL categories have we defined?
  - id: CreateURLCategories
    intent: Create a custom URL category
    question: How do I create a custom URL category for a list of sites?
  - id: GetURLCategoriesByID
    intent: Get a custom URL category
    question: What sites are in a particular custom URL category?
  - id: UpdateURLCategoriesByID
    intent: Update a custom URL category
    question: Can I add more sites to an existing custom URL category?
  - id: DeleteURLCategoriesByID
    intent: Delete a custom URL category
    question: How do I remove a custom URL category?
  - id: get-sse-config-v1-url-categories
    intent: List custom URL categories
    question: Which custom URL categories exist in a Prisma Access folder?
  - id: post-sse-config-v1-url-categories
    intent: Create a custom URL category
    question: How do I create a custom URL category with my own list of sites?
  - id: delete-sse-config-v1-url-categories-id
    intent: Delete a custom URL category
    question: How do I delete a custom URL category?
  phrasing_ops: 10
  slug: palo-alto-networks-url-categories-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: Predefined URL categories
  name: Palo Alto Networks URL Filtering Categories API
  phrasing_intents:
  - id: ListURLFilteringCategories
    intent: List custom URL categories
    question: What custom URL categories have I defined for URL filtering?
  - id: get-sse-config-v1-url-filtering-categories
    intent: List URL filtering categories
    question: What URL filtering categories are available for my security profiles?
  phrasing_ops: 2
  slug: palo-alto-networks-url-filtering-categories-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The User Groups API from Palo Alto Networks — 2 operation(s) for user groups.
  name: Palo Alto Networks User Groups API
  phrasing_intents:
  - id: GetSeb-apiV1User-groups
    intent: List Enterprise Browser user groups
    question: Which user groups are defined for the Enterprise Browser?
  - id: PostSeb-apiV1User-groups
    intent: Create an Enterprise Browser user group
    question: How do I create a browser user group from a list of user IDs?
  - id: GetSeb-apiV1User-groupsbyid
    intent: Get an Enterprise Browser user group
    question: Who is in a specific browser user group?
  - id: PutSeb-apiV1User-groupsbyid
    intent: Update an Enterprise Browser user group
    question: What's the way to change the users in an existing browser user group?
  - id: DeleteSeb-apiV1User-groupsbyid
    intent: Delete an Enterprise Browser user group
    question: How do I delete a browser user group?
  phrasing_ops: 5
  slug: palo-alto-networks-user-groups-api
- baseURL: https://api.strata.paloaltonetworks.com/config/mobile-agent/v1
  baseurl_source: declared
  description: User Locations
  name: Palo Alto Networks User Locations API
  phrasing_intents:
  - id: ListGlobalProtectUserLocations
    intent: List GlobalProtect user locations
    question: Which GlobalProtect user locations are set up for forwarding profiles?
  - id: CreateGlobalProtectUserLocation
    intent: Create a GlobalProtect user location
    question: How do I add a new GlobalProtect user location for a forwarding profile?
  - id: GetGlobalProtectUserLocationByID
    intent: Get a GlobalProtect user location
    question: How do I view the details of one GlobalProtect user location?
  - id: UpdateGlobalProtectUserLocationByID
    intent: Update a GlobalProtect user location
    question: How do I change the location choice on an existing GlobalProtect user location?
  - id: DeleteGlobalProtectUserLocation
    intent: Delete a GlobalProtect user location
    question: How do I delete a GlobalProtect user location?
  phrasing_ops: 5
  slug: palo-alto-networks-user-locations-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Manage your Prisma Cloud user profiles.
  name: Palo Alto Networks User Profile API
  phrasing_intents:
  - id: get-my-profile
    intent: View my own user profile
    question: What does my own Prisma Cloud profile say about me, like my roles and time zone?
  - id: update-my-profile
    intent: Update my own user profile
    question: Can I change my own name or time zone without an admin?
  - id: get-user-profiles-v3
    intent: List users and service accounts
    question: Which users and service accounts exist in my tenant?
  - id: add-user-v3
    intent: Add a user or service account
    question: How do I create a service account for automation instead of a person?
  - id: get-user-profiles-v2
    intent: List users with their roles (v2)
    question: Which users belong to my tenant and what roles does each hold?
  - id: add-user-v2
    intent: Add an administrative user (v2)
    question: How do I add a new admin who needs more than one role?
  - id: get-user-profile-v2
    intent: Get a user's profile by email
    question: What roles and settings does a specific user have?
  - id: update-profile-v2
    intent: Update another user's profile (v2)
    question: Can I change another admin's roles or time zone?
  phrasing_ops: 14
  slug: palo-alto-networks-user-profile-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The User Requests API from Palo Alto Networks — 4 operation(s) for user requests.
  name: Palo Alto Networks User Requests API
  phrasing_intents:
  - id: GetSeb-apiV1User-requests
    intent: List user access requests
    question: Which user requests are still pending approval?
  - id: GetSeb-apiV1User-requestsbyid
    intent: Get a user request
    question: What did the user ask for in a specific request?
  - id: PostSeb-apiV1User-requestsBy_idAction
    intent: Approve or deny a user request
    question: How do I approve a user's access request?
  - id: PostSeb-apiV1User-requestsBy_idRevoke
    intent: Revoke an approved user request
    question: Can I take back an approval I already granted?
  phrasing_ops: 4
  slug: palo-alto-networks-user-requests-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Manage your Prisma Cloud user roles.
  name: Palo Alto Networks User Roles API
  phrasing_intents:
  - id: get-user-roles
    intent: List Prisma Cloud user roles
    question: Which user roles exist in my Prisma Cloud tenant with their full settings?
  - id: add-user-role
    intent: Create a user role
    question: How do I create a custom role that only sees certain account groups?
  - id: get-user-role-name
    intent: List user role IDs and names
    question: What are just the names and IDs of my user roles?
  - id: get-user-role-types
    intent: List permission groups for user roles
    question: Which permission groups can a user role be based on?
  - id: get-user-role
    intent: Get a user role
    question: Where do I see the settings of one specific user role?
  - id: update-user-role
    intent: Update a user role
    question: How do I change which account groups an existing role can access?
  - id: delete-user-role
    intent: Delete a user role
    question: Can I remove a role I no longer need?
  phrasing_ops: 7
  slug: palo-alto-networks-user-roles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Userid Match List
  name: Palo Alto Networks Userid Match List API
  phrasing_intents:
  - id: ListUseridMatchList
    intent: List User-ID match list entries
    question: Which User-ID match list entries exist in a folder?
  - id: CreateUseridMatchList
    intent: Create a User-ID match list entry
    question: How do I forward User-ID log matches to syslog or email?
  - id: GetUseridMatchListByID
    intent: Get a User-ID match list entry
    question: What filter and forwarding targets does one User-ID match list entry use?
  - id: UpdateUseridMatchListByID
    intent: Update a User-ID match list entry
    question: How do I change the filter on an existing User-ID match list entry?
  - id: DeleteUseridMatchListByID
    intent: Delete a User-ID match list entry
    question: Is there a way to remove a User-ID match list entry?
  phrasing_ops: 5
  slug: palo-alto-networks-userid-match-list-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The UserOnboarding-LinkAccount API from Palo Alto Networks — 2 operation(s) for useronboarding-linkaccount.
  name: Palo Alto Networks User Onboarding Link Account API
  phrasing_intents:
  - id: get-v1-mgmt-linkaccounts
    intent: List accounts linked to the admin account
    question: Which accounts are linked to my Cloud NGFW admin account?
  - id: get-v1-mgmt-linkaccounts-accountid
    intent: Get a linked account
    question: What are the details of one account linked to my admin account?
  phrasing_ops: 2
  slug: palo-alto-networks-useronboarding-linkaccount-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The UserOnboarding-MemberAccounts API from Palo Alto Networks — 2 operation(s) for useronboarding-memberaccounts.
  name: Palo Alto Networks User Onboarding Member Accounts API
  phrasing_intents:
  - id: get-v1-mgmt-xaccountroles
    intent: List onboarded member accounts and cross-account roles
    question: Which member accounts are onboarded to Cloud NGFW with cross-account roles?
  - id: get-v1-mgmt-xaccountroles-accountid
    intent: Describe a member account and its cross-account role
    question: What cross-account role and status does one member account have?
  phrasing_ops: 2
  slug: palo-alto-networks-useronboarding-memberaccounts-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Users API
  name: Palo Alto Networks Users API
  phrasing_intents:
  - id: post-insights-v3.0-resource-query-users-agent-connected_user_count
    intent: Count users connected via agent
    question: How many users are connected through the endpoint agent?
  - id: post-insights-v3.0-resource-query-users-agentless-connected_user_count
    intent: Count agentless proxy users
    question: How many users are connected via the agentless proxy?
  - id: post-insights-v3.0-resource-query-users-all-user_list_all
    intent: List all users with details
    question: Can I get a detailed list of every user across all connection types?
  - id: post-insights-v3.0-resource-query-users-branch-connected_user_count
    intent: Count branch-connected users
    question: How many users are connected from branch sites?
  - id: post-insights-v3.0-resource-query-users-eb-connected_user_count
    intent: Count Enterprise Browser users
    question: How many users are connected through Enterprise Browser?
  - id: post-insights-v3.0-resource-query-users-other-connected_entity_count
    intent: Count connected users on other hosts
    question: How many users are connected from other hosts?
  phrasing_ops: 6
  slug: palo-alto-networks-users-api-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/util/util.md''}'
  name: Palo Alto Networks Util API
  phrasing_intents:
  - id: get-util-prisma-cloud-jenkins-plugin.hpi
    intent: Download the Jenkins plugin for Compute
    question: Where can I download the Jenkins plugin for Prisma Cloud Compute?
  - id: get-util-tas-tile
    intent: Download the VMware TAS tile for Compute
    question: Where do I get the VMware Tanzu Application Service tile for Compute?
  - id: get-util-arm64-twistcli
    intent: Download ARM64 Linux twistcli (v34.03)
    question: 'I''m pinned to the older v34.03 console: where''s the twistcli build for ARM64 Linux servers?'
  - id: get-util-osx-arm64-twistcli
    intent: Download Apple Silicon macOS twistcli (v34.03)
    question: On the older 34.03 release, is there a twistcli that runs natively on M1 or M2 Macs?
  - id: get-util-osx-twistcli
    intent: Download Intel macOS twistcli (v34.03)
    question: For an Intel Mac on the older 34.03 console, which twistcli do I need?
  - id: get-util-twistcli
    intent: Download Linux twistcli (v34.03)
    question: 'My CI runs on x86_64 Linux with the older 34.03 console: where is its twistcli?'
  - id: get-util-windows-twistcli.exe
    intent: Download Windows twistcli (v34.03)
    question: 'Our Windows build agents use the older 34.03 console: which scanner exe do they need?'
  - id: getApiV3404UtilArm64Twistcli
    intent: Download ARM64 Linux twistcli (v34.04)
    question: Where's the newest v34.04 twistcli for ARM64 Linux cloud instances?
  phrasing_ops: 12
  slug: palo-alto-networks-util-api
- baseURL: https://api.strata.paloaltonetworks.com/config/setup/v1
  baseurl_source: declared
  description: Configuration variables
  name: Palo Alto Networks Variables API
  phrasing_intents:
  - id: ListVariables
    intent: List configuration variables
    question: Which configuration variables are defined in my tenant?
  - id: CreateVariable
    intent: Create a configuration variable
    question: How do I define a variable that devices can reuse in their configuration?
  - id: GetVariableByID
    intent: Get a configuration variable
    question: What value and type does a specific variable hold?
  - id: UpdateVariableByID
    intent: Update a configuration variable
    question: How do I change the value of an existing variable?
  - id: DeleteVariableByID
    intent: Delete a configuration variable
    question: Which call removes a variable I no longer use?
  phrasing_ops: 5
  slug: palo-alto-networks-variables-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/version/version.md''}'
  name: Palo Alto Networks Version API
  phrasing_intents:
  - id: get-version
    intent: Get Compute version (v34.03 API)
    question: What Prisma Cloud Compute version does the v34.03 API report?
  - id: getApiV3404Version
    intent: Get Compute version (v34.04 API)
    question: What Prisma Cloud Compute version does the v34.04 API report?
  phrasing_ops: 2
  slug: palo-alto-networks-version-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The VLAN Attachment Latency API from Palo Alto Networks — 1 operation(s) for vlan attachment latency.
  name: Palo Alto Networks VLAN Attachment Latency API
  phrasing_intents:
  - id: PostMtSp-interconnectMonitorVlanattachmentsLatency
    intent: Get VLAN attachment latency trends
    question: What's the latency between Prisma Access and my service provider edge over time?
  phrasing_ops: 1
  slug: palo-alto-networks-vlan-attachment-latency-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The VLAN Attachment Statistics API from Palo Alto Networks — 1 operation(s) for vlan attachment statistics.
  name: Palo Alto Networks VLAN Attachment Statistics API
  phrasing_intents:
  - id: PostMtSp-interconnectMonitorVlanattachmentsStats
    intent: Get VLAN attachment statistics
    question: What throughput and BGP state are my interconnect VLAN attachments showing?
  phrasing_ops: 1
  slug: palo-alto-networks-vlan-attachment-statistics-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The VLAN Attachment Throughput API from Palo Alto Networks — 1 operation(s) for vlan attachment throughput.
  name: Palo Alto Networks VLAN Attachment Throughput API
  phrasing_intents:
  - id: PostMtSp-interconnectMonitorVlanattachmentsThroughput
    intent: Track VLAN attachment throughput trends
    question: How is load spread across the VLAN attachments in my interconnect?
  phrasing_ops: 1
  slug: palo-alto-networks-vlan-attachment-throughput-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The VLAN Attachment Traffic API from Palo Alto Networks — 1 operation(s) for vlan attachment traffic.
  name: Palo Alto Networks VLAN Attachment Traffic API
  phrasing_intents:
  - id: PostMtSp-interconnectMonitorVlanattachmentsTraffic
    intent: Analyze VLAN attachment traffic trends
    question: How much data has a VLAN attachment carried over time?
  phrasing_ops: 1
  slug: palo-alto-networks-vlan-attachment-traffic-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: VLAN Interfaces
  name: Palo Alto Networks VLAN Interfaces API
  phrasing_intents:
  - id: ListVLANInterfaces
    intent: List VLAN interfaces
    question: What VLAN interfaces are configured on my firewalls?
  - id: CreateVLANInterfaces
    intent: Create a VLAN interface
    question: How do I create a VLAN interface with a VLAN tag?
  - id: GetVLANInterfacesByID
    intent: Get a VLAN interface
    question: What VLAN tag and settings does a given VLAN interface have?
  - id: UpdateVLANlInterfacesByID
    intent: Update a VLAN interface
    question: Can I change the VLAN tag on an existing VLAN interface?
  - id: DeleteVLANInterfacesByID
    intent: Delete a VLAN interface
    question: Can I delete a VLAN interface?
  phrasing_ops: 5
  slug: palo-alto-networks-vlan-interfaces-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: '{''$ref'': ''desc/vms/vms.md''}'
  name: Palo Alto Networks Vms API
  phrasing_intents:
  - id: get-vms
    intent: Get VM image scan results (v34.03)
    question: What vulnerabilities and compliance issues were found in my VM images on the v34.03 API?
  - id: get-vms-download
    intent: Download VM image scan results (v34.03)
    question: Can I export VM image scan results to a file on the v34.03 API?
  - id: get-vms-labels
    intent: List VM image tags (v34.03)
    question: What tags are applied to my scanned VM images on the v34.03 API?
  - id: get-vms-names
    intent: List scanned VM image names (v34.03)
    question: Which VM image names have been scanned according to the v34.03 API?
  - id: post-vms-scan
    intent: Start a VM image scan (v34.03)
    question: How do I kick off a VM image scan with the v34.03 API?
  - id: post-vms-stop
    intent: Stop a running VM image scan (v34.03)
    question: How do I halt an in-progress VM image scan on the v34.03 API?
  - id: getApiV3404Vms
    intent: Get VM image scan results (v34.04)
    question: What vulnerabilities were found in my VM images on the current v34.04 API?
  - id: getApiV3404VmsDownload
    intent: Download VM image scan results (v34.04)
    question: Can I export VM image scan results to a file on the current v34.04 API?
  phrasing_ops: 12
  slug: palo-alto-networks-vms-api
- baseURL: https://api.strata.paloaltonetworks.com/config/device/v1
  baseurl_source: declared
  description: VPN Settings
  name: Palo Alto Networks VPN Settings API
  phrasing_intents:
  - id: ListVPNSettings
    intent: List VPN settings
    question: What VPN settings are configured for a folder?
  - id: CreateVPNSettings
    intent: Create VPN settings
    question: How do I create new VPN settings?
  - id: GetVPNSettingsByID
    intent: Get VPN settings
    question: How do I view one set of VPN settings by ID?
  - id: UpdateVPNSettingsByID
    intent: Update VPN settings
    question: Can I change existing VPN settings?
  - id: DeleteVPNSettingsByID
    intent: Delete VPN settings
    question: How do I delete a VPN settings object?
  phrasing_ops: 5
  slug: palo-alto-networks-vpn-settings-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for VSatellite.
  name: Palo Alto Networks V Satellite API
  phrasing_intents:
  - id: create-edgeinstances-update
    intent: Trigger a manual Satellite instance update
    question: Can I force a VSatellite instance to update now instead of waiting for the update window?
  - id: edgeencryptionkeys_getAll
    intent: List Satellite encryption keys
    question: Which encryption keys are registered for my VSatellite deployments?
  - id: edgeencryptionkeys_getById
    intent: Get a Satellite encryption key
    question: How do I look up a single satellite encryption key by its id?
  - id: edgeinstances_getAll
    intent: List Satellite instances
    question: Which VSatellite instances does my company have deployed?
  - id: edgeinstances_getById
    intent: Get a Satellite instance
    question: What is the current state of one of my VSatellite instances?
  - id: edgeinstances_update
    intent: Rename or reprioritize a Satellite instance
    question: How do I rename a VSatellite instance?
  - id: pairingcodes_create
    intent: Generate a Satellite pairing code
    question: How do I get a pairing code to register a new VSatellite instance?
  - id: recoverycodes_create
    intent: Generate a Satellite recovery code
    question: How do I restore a VSatellite instance that I need to rebuild?
  phrasing_ops: 14
  slug: palo-alto-networks-vsatellite-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Vulnerabilities Dashboard API from Palo Alto Networks — 31 operation(s) for vulnerabilities dashboard.
  name: Palo Alto Networks Vulnerabilities Dashboard API
  phrasing_intents:
  - id: c2c-trace-api
    intent: Trace an asset from code to cloud
    question: Can I see how a vulnerable asset connects across code, build, deploy and run stages?
  - id: cve-overview
    intent: Get a basic CVE overview (legacy v1)
    question: What CVSS score, severity and affected packages does a CVE have in my environment, using the original overview endpoint?
  - id: cve-overview-v-2
    intent: Get a CVE overview with EPSS and exploit details
    question: Does a CVE have a known exploit and what is its EPSS score in my environment?
  - id: cve-overview-v-3
    intent: Get a CVE overview filtered by cloud account
    question: Can I scope a CVE's EPSS and CVSS details to specific account groups or cloud accounts?
  - id: get-burndown
    intent: Get the 30-day vulnerability burndown
    question: How many vulnerabilities have we remediated over the past 30 days compared to the total?
  - id: list-vulnerable-assets-cve
    intent: List assets affected by a CVE (legacy)
    question: Which assets are affected by a particular CVE, using the original assets-by-CVE endpoint?
  - id: list-vulnerable-assets-cve-v-2
    intent: List assets affected by a CVE per account
    question: Which of my cloud accounts have assets exposed to a specific CVE?
  - id: prioritised-vulnerability
    intent: Count top-priority vulnerabilities (v1)
    question: How many urgent, exploitable and patchable vulnerabilities do we have in total?
  phrasing_ops: 31
  slug: palo-alto-networks-vulnerabilities-dashboard-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: Vulnerability Protection Profiles
  name: Palo Alto Networks Vulnerability Protection Profiles API
  phrasing_intents:
  - id: ListVulnerabilityProtectionProfiles
    intent: List vulnerability protection profiles
    question: Which vulnerability protection profiles are defined in Strata Cloud Manager?
  - id: CreateVulnerabilityProtectionProfiles
    intent: Create a vulnerability protection profile
    question: How do I create a new vulnerability protection profile for my security policy?
  - id: GetVulnerabilityProtectionProfilesByID
    intent: Get a vulnerability protection profile
    question: What rules and threat exceptions does a particular vulnerability protection profile contain?
  - id: UpdateVulnerabilityProtectionProfilesByID
    intent: Update a vulnerability protection profile
    question: Can I change the rules on a vulnerability protection profile that already exists?
  - id: DeleteVulnerabilityProtectionProfilesByID
    intent: Delete a vulnerability protection profile
    question: How do I remove a vulnerability protection profile I no longer use?
  - id: get-sse-config-v1-vulnerability-protection-profiles
    intent: List vulnerability protection profiles
    question: Which vulnerability protection profiles are configured in my folder?
  - id: post-sse-config-v1-vulnerability-protection-profiles
    intent: Create a vulnerability protection profile
    question: How do I create a profile that blocks exploit attempts against known vulnerabilities?
  - id: delete-sse-config-v1-vulnerability-protection-profiles-id
    intent: Delete a vulnerability protection profile
    question: How do I remove a vulnerability protection profile?
  phrasing_ops: 10
  slug: palo-alto-networks-vulnerability-protection-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: Vulnerability Protection Signatures
  name: Palo Alto Networks Vulnerability Protection Signatures API
  phrasing_intents:
  - id: ListVulnerabilityProtectionSignatures
    intent: List custom vulnerability signatures
    question: Which custom vulnerability protection signatures exist in a folder?
  - id: CreateVulnerabilityProtectionSignatures
    intent: Create a custom vulnerability signature
    question: How do I write a custom vulnerability protection signature for an exploit?
  - id: GetVulnerabilityProtectionSignaturesByID
    intent: Get a vulnerability protection signature
    question: What CVE and affected host does a given vulnerability signature cover?
  - id: UpdateVulnerabilityProtectionSignaturesByID
    intent: Update a vulnerability protection signature
    question: Can I change the default action on a custom vulnerability signature?
  - id: DeleteVulnerabilityProtectionSignaturesByID
    intent: Delete a vulnerability protection signature
    question: How do I remove a custom vulnerability protection signature?
  - id: get-sse-config-v1-vulnerability-protection-signatures
    intent: List custom vulnerability signatures
    question: Which custom vulnerability protection signatures exist through the SSE config v1 API?
  - id: post-sse-config-v1-vulnerability-protection-signatures
    intent: Create a custom vulnerability signature
    question: How do I write a custom signature to block an exploit for a specific CVE?
  - id: delete-sse-config-v1-vulnerability-protection-signatures-id
    intent: Delete a custom vulnerability signature
    question: Can I remove a custom vulnerability signature?
  phrasing_ops: 10
  slug: palo-alto-networks-vulnerability-protection-signatures-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The Waas API from Palo Alto Networks — 2 operation(s) for waas.
  name: Palo Alto Networks Waas API
  phrasing_intents:
  - id: post-waas-openapi-scans
    intent: Scan an OpenAPI file for WAAS findings (v34.03)
    question: Can the v34.03 API check my OpenAPI spec for WAAS observations?
  - id: postApiV3404WaasOpenapiScans
    intent: Scan an OpenAPI file for WAAS findings (v34.04)
    question: How do I find WAAS issues in an OpenAPI definition with the current v34.04 API?
  phrasing_ops: 2
  slug: palo-alto-networks-waas-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: The Widgets API from Palo Alto Networks — 5 operation(s) for widgets.
  name: Palo Alto Networks Widgets API
  phrasing_intents:
  - id: value-widgets-alert-metrics-resolution-reason
    intent: Count resolved alerts by resolution reason
    question: Why are my alerts being resolved, broken down by reason?
  - id: value-widgets-alert-metrics
    intent: Get mean alert resolution time by severity
    question: How long does it take on average to resolve alerts of each severity?
  - id: value-widgets-get-vulnerabilities-trend
    intent: Get the vulnerabilities trend over time
    question: Are we discovering more vulnerabilities than we resolve over time?
  - id: value-widgets-get-assets-with-alerts
    intent: Get the trend of assets generating alerts
    question: Which cloud assets are generating alerts?
  - id: value-widgets-get-discovered-vs-secured
    intent: Compare discovered versus secured resources
    question: How many discovered resources are actually protected by defenders?
  phrasing_ops: 5
  slug: palo-alto-networks-widgets-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Wildcard API from Palo Alto Networks — 3 operation(s) for wildcard.
  name: Palo Alto Networks Wildcard API
  phrasing_intents:
  - id: list.wildcards.v2
    intent: List ZTNA connector wildcards
    question: Which wildcard FQDN apps are configured on my connectors?
  - id: create.wildcard.v2
    intent: Create a connector wildcard
    question: How do I publish a wildcard domain like *.example.com through a connector group?
  - id: get.wildcard.v2
    intent: Get a connector wildcard
    question: How do I see the configuration of one wildcard?
  - id: update.wildcard.v2
    intent: Update a connector wildcard
    question: Can I change the FQDN or ports on an existing wildcard?
  - id: delete.wildcard.v2
    intent: Delete a connector wildcard
    question: How do I delete a wildcard from my connectors?
  - id: list.wildcard.filters.v2
    intent: List filter values for wildcard fields
    question: What filter values can I use for a wildcard field?
  phrasing_ops: 6
  slug: palo-alto-networks-wildcard-api
- baseURL: https://api.strata.paloaltonetworks.com/config/security/v1
  baseurl_source: declared
  description: WildFire Anti-Virus Profiles
  name: Palo Alto Networks WildFire Anti-Virus Profiles API
  phrasing_intents:
  - id: ListWildFireAntiVirusProfiles
    intent: List WildFire and antivirus profiles
    question: Which WildFire and antivirus security profiles are configured?
  - id: CreateWildFireAntiVirusProfiles
    intent: Create a WildFire and antivirus profile
    question: How do I create a new malware scanning profile with WildFire analysis?
  - id: GetWildFireAntiVirusProfilesByID
    intent: Get a WildFire and antivirus profile
    question: What rules and exceptions does a specific WildFire antivirus profile contain?
  - id: UpdateWildFireAntiVirusProfilesByID
    intent: Update a WildFire and antivirus profile
    question: How do I add a threat exception to an existing WildFire profile?
  - id: DeleteWildFireAntiVirusProfilesByID
    intent: Delete a WildFire and antivirus profile
    question: How do I remove a WildFire antivirus profile?
  - id: get-sse-config-v1-wildfire-anti-virus-profiles
    intent: List WildFire antivirus profiles
    question: Which WildFire antivirus profiles are configured in a folder?
  - id: post-sse-config-v1-wildfire-anti-virus-profiles
    intent: Create a WildFire antivirus profile
    question: How do I create a WildFire antivirus profile with my own rules?
  - id: delete-sse-config-v1-wildfire-anti-virus-profiles-id
    intent: Delete a WildFire antivirus profile
    question: How do I remove a WildFire antivirus profile using the SSE config v1 path?
  phrasing_ops: 10
  slug: palo-alto-networks-wildfire-anti-virus-profiles-api
- baseURL: https://api.strata.paloaltonetworks.com/ngts
  baseurl_source: declared
  description: APIs for Workload Issuance Policies.
  name: Palo Alto Networks Workload Issuance Policies API
  phrasing_intents:
  - id: policies_create
    intent: Create a Workload Issuance policy
    question: How do I create a policy that restricts which certificates an issuer can create?
  - id: policies_getAll
    intent: List Workload Issuance policies
    question: Which Workload Issuance policies constrain how certificates are issued?
  - id: policies_getById
    intent: Get a Workload Issuance policy
    question: What key algorithm and validity period does one issuance policy enforce?
  - id: policies_update
    intent: Update a Workload Issuance policy
    question: How do I change the validity period on an existing issuance policy?
  - id: policies_delete
    intent: Delete a Workload Issuance policy
    question: How do I remove a Workload Issuance policy?
  phrasing_ops: 5
  slug: palo-alto-networks-workload-issuance-policies-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: Zone Protection Profiles
  name: Palo Alto Networks Zone Protection Profiles API
  phrasing_intents:
  - id: ListZoneProtectionProfiles
    intent: List zone protection profiles
    question: Which zone protection profiles guard my security zones?
  - id: CreateZoneProtectionProfiles
    intent: Create a zone protection profile
    question: How do I create a zone protection profile with flood and scan protection?
  - id: GetZoneProtectionProfilesByID
    intent: Get a zone protection profile
    question: What flood thresholds does a specific zone protection profile set?
  - id: UpdateZoneProtectionProfilesByID
    intent: Update a zone protection profile
    question: Can I tighten scan protection on an existing zone protection profile?
  - id: DeleteZoneProtectionProfilesByID
    intent: Delete a zone protection profile
    question: Can I remove a zone protection profile no zone uses?
  phrasing_ops: 5
  slug: palo-alto-networks-zone-protection-profiles-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The ZoomParticipantController API from Palo Alto Networks — 2 operation(s) for zoomparticipantcontroller.
  name: Palo Alto Networks Zoom Participant Controller API
  phrasing_intents:
  - id: ZoomParticipantController.getZoomParticipant
    intent: Get Zoom meeting participant details
    question: Which users joined Zoom meetings and what did their experience look like?
  - id: ZoomParticipantController.getZoomParticipantScore
    intent: Get Zoom participant experience scores
    question: What experience scores did Zoom participants get?
  phrasing_ops: 2
  slug: palo-alto-networks-zoomparticipantcontroller-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The ZoomQosController API from Palo Alto Networks — 1 operation(s) for zoomqoscontroller.
  name: Palo Alto Networks Zoom Qos Controller API
  phrasing_intents:
  - id: ZoomQosController.getZoomQosMetric
    intent: Get Zoom call quality metrics
    question: How has Zoom call quality looked for my users over the past day?
  phrasing_ops: 1
  slug: palo-alto-networks-zoomqoscontroller-api
- baseURL: https://api.sase.paloaltonetworks.com/iam/v1
  baseurl_source: declared
  description: Access policy management for role-based access control.
  name: Palo Alto Networks Access Policies API
  phrasing_intents:
  - id: listAccessPolicies
    intent: List access policies for a tenant
    question: Which roles has each service account or user been granted across my tenant service groups?
  - id: createAccessPolicy
    intent: Grant a role to a principal in a TSG
    question: How do I give a service account a role within a tenant service group?
  - id: getAccessPolicy
    intent: Get an access policy
    question: Which principal, role and TSG does one access policy bind?
  - id: updateAccessPolicy
    intent: Change the role on an access policy
    question: Can I switch a principal to a different role without recreating the access policy?
  - id: deleteAccessPolicy
    intent: Revoke an access policy
    question: Can I revoke a role binding from a service account?
  - id: get-iam-v1-access_policies
    intent: List IAM access policies
    question: Which access policies grant a particular role in my tenant?
  - id: post-iam-v1-access_policies
    intent: Assign an access policy to a user
    question: How do I give a user or service account a role on a tenant service group?
  - id: delete-iam-v1-access_policies-id
    intent: Revoke an access policy
    question: Can I remove a user's role by deleting their access policy?
  phrasing_ops: 9
  slug: palo-alto-networks-access-policies-api
- baseURL: https://security.paloaltonetworks.com/api
  baseurl_source: declared
  description: Query and retrieve PSIRT security advisories.
  name: Palo Alto Networks Advisories API
  phrasing_intents:
  - id: listAdvisories
    intent: List security advisories
    question: What are the latest Palo Alto Networks PSIRT security advisories?
  - id: getAdvisory
    intent: Get a security advisory
    question: Which versions are affected and fixed for a specific advisory?
  - id: getAdvisoryByCVE
    intent: Find advisories for a CVE
    question: Which advisories reference a particular CVE?
  phrasing_ops: 3
  slug: palo-alto-networks-advisories-api
- baseURL: https://api.sase.paloaltonetworks.com/adem/telemetry/v2
  baseurl_source: declared
  description: Monitored agent and endpoint inventory management.
  name: Palo Alto Networks Agents API
  phrasing_intents:
  - id: listMonitoredAgents
    intent: List monitored ADEM agents
    question: Which endpoints have ADEM agents registered for monitoring?
  phrasing_ops: 1
  slug: palo-alto-networks-agents-api
- baseURL: https://api.sase.paloaltonetworks.com/adem/telemetry/v2
  baseurl_source: declared
  description: Agent and endpoint experience score monitoring for tracking the health and experience of monitored user devices.
  name: Palo Alto Networks Agent Scores API
  phrasing_intents:
  - id: getAgentScores
    intent: Get digital experience scores for agents
    question: Which users have the poorest digital experience scores from their devices?
  phrasing_ops: 1
  slug: palo-alto-networks-agentscores-api
- baseURL: https://api.sase.paloaltonetworks.com/mt/monitor/v1
  baseurl_source: declared
  description: Multi-tenant aggregated data queries.
  name: Palo Alto Networks Aggregation Queries API
  phrasing_intents:
  - id: queryThreatData
    intent: Aggregate threat events across tenants
    question: How many threat events did my managed tenants see, broken down by severity?
  - id: queryURLData
    intent: Aggregate URL categorization and web activity
    question: Which URL categories are my tenants' users visiting most?
  - id: queryApplicationData
    intent: Aggregate application usage across tenants
    question: Which applications use the most sessions and bytes across my tenants?
  - id: queryBandwidthData
    intent: Aggregate bandwidth utilization by location
    question: How much bandwidth are my SASE locations using for capacity planning?
  - id: queryLicenseData
    intent: Aggregate license utilization across tenants
    question: How much of our SASE license capacity is each tenant consuming?
  phrasing_ops: 5
  slug: palo-alto-networks-aggregation-queries-api
- baseURL: https://api.sase.paloaltonetworks.com/sspm
  baseurl_source: declared
  description: SaaS application catalog and metadata.
  name: Palo Alto Networks App Catalog API
  phrasing_intents:
  - id: listAppCatalog
    intent: Browse the SaaS app catalog for SSPM
    question: Which SaaS applications does SSPM support for posture checks?
  phrasing_ops: 1
  slug: palo-alto-networks-app-catalog-api
- baseURL: https://api.sase.paloaltonetworks.com/adem/telemetry/v2
  baseurl_source: declared
  description: Application experience score monitoring providing aggregated performance ratings for SaaS and internal applications.
  name: Palo Alto Networks Application Scores API
  phrasing_intents:
  - id: getApplicationScores
    intent: Get application experience scores
    question: How good is the user experience of a monitored app, on a 0 to 100 score?
  phrasing_ops: 1
  slug: palo-alto-networks-applicationscores-api
- baseURL: https://api.threatvault.paloaltonetworks.com/service/v1
  baseurl_source: declared
  description: Advanced Threat Prevention detailed analysis reports and PCAP files.
  name: Palo Alto Networks ATP API
  phrasing_intents:
  - id: getAtpReports
    intent: Get Advanced Threat Prevention analysis reports
    question: What did inline cloud analysis find about a threat with a given SHA-256 hash?
  - id: getAtpReportPcaps
    intent: Download packet captures for an ATP report
    question: How do I download the PCAP recorded during a threat's analysis?
  phrasing_ops: 2
  slug: palo-alto-networks-atp-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: Email attachment retrieval operations.
  name: Palo Alto Networks Attachments API
  phrasing_intents:
  - id: getEmailIncidentAttachments
    intent: Get attachments of an email DLP incident
    question: Which attachments triggered a specific email DLP incident?
  phrasing_ops: 1
  slug: palo-alto-networks-attachments-api
- baseURL: https://api.sase.paloaltonetworks.com/ai-red-teaming
  baseurl_source: declared
  description: Available attack category reference data.
  name: Palo Alto Networks Attack Categories API
  phrasing_intents:
  - id: listAttackCategories
    intent: List AI attack categories for scans
    question: Which AI attack categories can I pick when starting a vulnerability scan?
  phrasing_ops: 1
  slug: palo-alto-networks-attack-categories-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: Attack surface rule configuration and management.
  name: Palo Alto Networks Attack Surface Rules API
  phrasing_intents:
  - id: getAttackSurfaceRules
    intent: List attack surface rules
    question: What attack surface rules does Xpanse use to classify exposures?
  - id: updateAttackSurfaceRule
    intent: Update an attack surface rule
    question: Can I disable an attack surface rule or change its severity?
  phrasing_ops: 2
  slug: palo-alto-networks-attacksurfacerules-api
- baseURL: https://api.stratacloud.paloaltonetworks.com/aiops/bpa/v1
  baseurl_source: declared
  description: Audit and management log retrieval.
  name: Palo Alto Networks Audit API
  phrasing_intents:
  - id: getAuditManagementLogs
    intent: Get Cortex XDR audit management logs
    question: Who changed policies or logged in to the Cortex XDR console?
  - id: getManagementLogs
    intent: Get XSIAM audit management logs
    question: Who created or changed API keys in the XSIAM console?
  phrasing_ops: 2
  slug: palo-alto-networks-audit-api
- baseURL: https://api.stratacloud.paloaltonetworks.com/aiops/bpa/v1
  baseurl_source: declared
  description: Token-based authentication for API access.
  name: Palo Alto Networks Authentication API
  phrasing_intents:
  - id: authenticate
    intent: Get a Prisma Cloud Compute bearer token
    question: How do I get a bearer token for the Prisma Cloud Compute API?
  - id: login
    intent: Log in with a Prisma Cloud access key
    question: How do I exchange a Prisma Cloud access key for a JWT?
  phrasing_ops: 2
  slug: palo-alto-networks-authentication-api
- baseURL: https://api.sase.paloaltonetworks.com/config-orchestration/v1
  baseurl_source: declared
  description: Bandwidth allocation visibility.
  name: Palo Alto Networks Bandwidth API
  phrasing_intents:
  - id: getBandwidthAllocations
    intent: Check available bandwidth per Prisma Access location
    question: How much licensed bandwidth is still available in each Prisma Access location?
  phrasing_ops: 1
  slug: palo-alto-networks-bandwidth-api
- baseURL: https://api.stratacloud.paloaltonetworks.com/aiops/bpa/v1
  baseurl_source: declared
  description: Completed assessment report retrieval.
  name: Palo Alto Networks BPA Reports API
  phrasing_intents:
  - id: getBPAReport
    intent: Get a Best Practice Assessment report
    question: What overall and category scores did my firewall get in its Best Practice Assessment?
  - id: getBPAReportChecks
    intent: List check results in a BPA report
    question: Which individual best practice checks failed in a BPA report?
  phrasing_ops: 2
  slug: palo-alto-networks-bpa-reports-api
- baseURL: https://api.stratacloud.paloaltonetworks.com/aiops/bpa/v1
  baseurl_source: declared
  description: Best Practice Assessment request submission and status tracking.
  name: Palo Alto Networks BPA Requests API
  phrasing_intents:
  - id: submitBPARequest
    intent: Request a Best Practice Assessment for a firewall
    question: How do I run a Best Practice Assessment against one of my NGFW devices?
  - id: getBPARequestStatus
    intent: Check the status of a BPA request
    question: Has my Best Practice Assessment finished processing yet?
  phrasing_ops: 2
  slug: palo-alto-networks-bpa-requests-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Data classification results and taxonomy operations.
  name: Palo Alto Networks Classifications API
  phrasing_intents:
  - id: listClassifications
    intent: List DSPM data classification labels
    question: What data classifications does DSPM use to detect sensitive data?
  phrasing_ops: 1
  slug: palo-alto-networks-classifications-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: Configuration commit operations.
  name: Palo Alto Networks Commit API
  phrasing_intents:
  - id: getCommitStatus
    intent: Check the status of a firewall commit
    question: Has my firewall commit finished, and did it succeed?
  - id: commitConfiguration
    intent: Commit candidate configuration to the firewall
    question: How do I apply my staged configuration changes to the running firewall config?
  phrasing_ops: 2
  slug: palo-alto-networks-commit-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Compliance posture and reporting.
  name: Palo Alto Networks Compliance API
  phrasing_intents:
  - id: listComplianceStandards
    intent: List available compliance standards
    question: Which compliance standards like CIS, NIST, PCI-DSS or HIPAA are available in Prisma Cloud?
  phrasing_ops: 1
  slug: palo-alto-networks-compliance-api
- baseURL: https://api.stratacloud.paloaltonetworks.com/aiops/bpa/v1
  baseurl_source: declared
  description: Candidate configuration management and job tracking.
  name: Palo Alto Networks Configuration API
  phrasing_intents:
  - id: pushCandidateConfig
    intent: Push the candidate configuration
    question: How do I push my candidate configuration out to devices?
  - id: getJobStatus
    intent: Check an asynchronous job's status
    question: Has my configuration push finished yet?
  - id: postSseConfigV1ConfigVersionsCandidate:push
    intent: Push candidate config to folders (SSE v1)
    question: Can I deploy staged changes to firewalls in specific folders through the SSE config v1 API?
  phrasing_ops: 3
  slug: palo-alto-networks-configuration-api
- baseURL: https://api.sase.paloaltonetworks.com/ztna
  baseurl_source: declared
  description: Logical grouping of ZTNA connectors for high availability.
  name: Palo Alto Networks Connector Groups API
  phrasing_intents:
  - id: listConnectorGroups
    intent: List ZTNA connector groups
    question: What connector groups do I have for load balancing ZTNA connectors?
  - id: createConnectorGroup
    intent: Create a ZTNA connector group
    question: How do I create a new group to organize ZTNA connectors?
  - id: getConnectorGroup
    intent: Get a connector group's details
    question: What are the full details of a specific connector group?
  - id: updateConnectorGroup
    intent: Update a connector group
    question: How do I rename an existing connector group?
  - id: deleteConnectorGroup
    intent: Delete an empty connector group
    question: How do I delete a connector group?
  phrasing_ops: 5
  slug: palo-alto-networks-connector-groups-api
- baseURL: https://api.sase.paloaltonetworks.com/ztna
  baseurl_source: declared
  description: ZTNA connector lifecycle management.
  name: Palo Alto Networks Connectors API
  phrasing_intents:
  - id: listConnectors
    intent: List ZTNA connectors
    question: Which ZTNA connectors are deployed and are they healthy?
  - id: createConnector
    intent: Create a ZTNA connector and install token
    question: How do I get an installation token to deploy a new ZTNA connector?
  - id: getConnector
    intent: Get a ZTNA connector's details
    question: What version and health status is a specific ZTNA connector running?
  - id: updateConnector
    intent: Update a ZTNA connector
    question: How do I rename an existing ZTNA connector?
  - id: deleteConnector
    intent: Delete a ZTNA connector
    question: How do I decommission a ZTNA connector?
  - id: scheduleConnectorUpgrade
    intent: Schedule a ZTNA connector software upgrade
    question: How do I upgrade a ZTNA connector's software during a maintenance window?
  phrasing_ops: 6
  slug: palo-alto-networks-connectors-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Execute custom data resource queries with filters and aggregations
  name: Palo Alto Networks Custom Queries API
  phrasing_intents:
  - id: executeCustomQuery
    intent: Run a custom Prisma Access monitoring query
    question: Can I query Prisma Access monitoring data with my own filters, groupings and time range?
  phrasing_ops: 1
  slug: palo-alto-networks-custom-queries-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Export data resource results for external processing
  name: Palo Alto Networks Data Exports API
  phrasing_intents:
  - id: exportDataResource
    intent: Export a data resource query for bulk download
    question: Can I export insights query results in bulk for external processing?
  - id: getExportJobStatus
    intent: Check the status of a data export job
    question: Is my data export finished yet?
  phrasing_ops: 2
  slug: palo-alto-networks-data-exports-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Query Prisma Access deployment health and performance data resources
  name: Palo Alto Networks Data Resources API
  phrasing_intents:
  - id: queryDataResource
    intent: Query a Prisma Access data resource
    question: How healthy are my Prisma Access tunnels over the last day?
  phrasing_ops: 1
  slug: palo-alto-networks-data-resources-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Data store inventory and discovery operations.
  name: Palo Alto Networks Data Stores API
  phrasing_intents:
  - id: listDataStores
    intent: List discovered cloud data stores
    question: Which cloud databases and buckets hold sensitive data?
  phrasing_ops: 1
  slug: palo-alto-networks-datastores-api
- baseURL: https://api.sase.paloaltonetworks.com/browser-mgmt
  baseurl_source: declared
  description: Browser deployment configuration management.
  name: Palo Alto Networks Deployments API
  phrasing_intents:
  - id: listDeployments
    intent: List browser deployments
    question: Which Prisma Access Browser deployments are configured?
  - id: createDeployment
    intent: Create a browser deployment
    question: How do I roll out the secure browser to a new platform like macOS?
  - id: getDeployment
    intent: Get a browser deployment
    question: What settings does one browser deployment have?
  - id: updateDeployment
    intent: Update a browser deployment
    question: Can I switch the update channel of an existing browser deployment?
  - id: deleteDeployment
    intent: Delete a browser deployment
    question: How do I remove a browser deployment configuration?
  phrasing_ops: 5
  slug: palo-alto-networks-deployments-api
- baseURL: https://api.stratacloud.paloaltonetworks.com/aiops/bpa/v1
  baseurl_source: declared
  description: The Device API from Palo Alto Networks — 2 operation(s) for device.
  name: Palo Alto Networks Device API
  phrasing_intents:
  - id: listDeviceTags
    intent: List IoT Security device tags
    question: What tags are defined for labelling devices in IoT Security?
  - id: listVirtualSystems
    intent: List firewall virtual systems
    question: Which virtual systems (vsys) are configured on my firewall?
  phrasing_ops: 2
  slug: palo-alto-networks-device-api
- baseURL: https://api.dns.service.paloaltonetworks.com/v1
  baseurl_source: declared
  description: Domain categorization and threat intelligence lookups.
  name: Palo Alto Networks Domains API
  phrasing_intents:
  - id: getDomain
    intent: Check one domain's DNS Security verdict
    question: Is a particular domain considered malicious by DNS Security?
  - id: getDomainBulk
    intent: Check verdicts for many domains at once
    question: Can I look up categories for a batch of domains in one call?
  phrasing_ops: 2
  slug: palo-alto-networks-domains-api
- baseURL: https://api.sase.paloaltonetworks.com/logging-service/v1
  baseurl_source: declared
  description: Email forwarding destination management.
  name: Palo Alto Networks Email Destinations API
  phrasing_intents:
  - id: listEmailDestinations
    intent: List a log forwarding profile's email destinations
    question: Which email addresses receive logs from a log forwarding profile?
  - id: createEmailDestination
    intent: Add an email destination to log forwarding
    question: How do I send log alerts by email from a log forwarding profile?
  phrasing_ops: 2
  slug: palo-alto-networks-email-destinations-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: Endpoint management, isolation, and scanning.
  name: Palo Alto Networks Endpoints API
  phrasing_intents:
  - id: getEndpoints
    intent: List enrolled endpoints
    question: Which endpoints are enrolled in Cortex XDR?
  - id: isolateEndpoints
    intent: Isolate endpoints from the network
    question: How do I cut a compromised laptop off from the network?
  - id: unisolateEndpoints
    intent: Release endpoints from isolation
    question: How do I restore network access to an endpoint after an investigation?
  - id: scanEndpoints
    intent: Run a malware scan on endpoints
    question: Can I trigger a malware scan on specific endpoints?
  phrasing_ops: 4
  slug: palo-alto-networks-endpoints-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: Investigation entry (work note) management.
  name: Palo Alto Networks Entries API
  phrasing_intents:
  - id: addEntry
    intent: Add an entry to an investigation
    question: How do I add a note to an incident's war room?
  phrasing_ops: 1
  slug: palo-alto-networks-entries-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: Cloud NGFW firewall instance management.
  name: Palo Alto Networks Firewalls API
  phrasing_intents:
  - id: listFirewalls
    intent: List Cloud NGFW firewalls in an AWS account
    question: Which Cloud NGFW firewalls are running in my AWS account?
  - id: createFirewall
    intent: Create a Cloud NGFW firewall in a VPC
    question: How do I deploy a new Cloud NGFW firewall into one of my AWS VPCs?
  - id: getFirewall
    intent: Get a Cloud NGFW firewall's configuration
    question: What is the current status of a specific Cloud NGFW firewall?
  - id: updateFirewall
    intent: Update an existing Cloud NGFW firewall
    question: How do I switch an existing cloud firewall to a different rule stack?
  - id: deleteFirewall
    intent: Delete a Cloud NGFW firewall
    question: How do I tear down a Cloud NGFW firewall and remove its VPC endpoints?
  phrasing_ops: 5
  slug: palo-alto-networks-firewalls-api
- baseURL: https://api.prismacloud.io/code/api/v1
  baseurl_source: declared
  description: Automated fix suggestions for pull requests.
  name: Palo Alto Networks Fixes API
  phrasing_intents:
  - id: getFixSuggestionsForPR
    intent: Get fix suggestions for a pull request
    question: What code fixes are suggested for misconfigurations found in my pull request?
  phrasing_ops: 1
  slug: palo-alto-networks-fixes-api
- baseURL: https://api.sase.paloaltonetworks.com/ztna
  baseurl_source: declared
  description: FQDN-based access rules for ZTNA applications.
  name: Palo Alto Networks FQDN Rules API
  phrasing_intents:
  - id: listFQDNRules
    intent: List FQDN-based ZTNA access rules
    question: Which hostnames can users reach through ZTNA today?
  - id: createFQDNRule
    intent: Create an FQDN-based ZTNA access rule
    question: How do I give users access to an internal hostname through a connector group?
  phrasing_ops: 2
  slug: palo-alto-networks-fqdn-rules-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: FQDN list management for use in security rule destination criteria.
  name: Palo Alto Networks FQDN Lists API
  phrasing_intents:
  - id: listFqdnLists
    intent: List FQDN lists in a rule stack
    question: Which FQDN lists of domain names exist in my rule stack?
  - id: createFqdnList
    intent: Create an FQDN list in a rule stack
    question: How do I create a list of domains to use as a security rule destination?
  phrasing_ops: 2
  slug: palo-alto-networks-fqdnlists-api
- baseURL: https://api.sase.paloaltonetworks.com/logging-service/v1
  baseurl_source: declared
  description: HTTPS forwarding destination management.
  name: Palo Alto Networks HTTPS Destinations API
  phrasing_intents:
  - id: listHTTPSDestinations
    intent: List HTTPS destinations on a log forwarding profile
    question: Where is a log forwarding profile sending logs over HTTPS?
  - id: createHTTPSDestination
    intent: Add an HTTPS webhook destination for logs
    question: How do I forward logs to my own webhook over HTTPS?
  phrasing_ops: 2
  slug: palo-alto-networks-https-destinations-api
- baseURL: https://api.dlp.paloaltonetworks.com/v4
  baseurl_source: declared
  description: Incident management and investigation.
  name: Palo Alto Networks Incidents API
  phrasing_intents:
  - id: getIncidents
    intent: List Cortex XDR incidents
    question: Which Cortex XDR incidents are open right now at high severity?
  - id: getIncidentExtraData
    intent: Get a Cortex XDR incident with its alerts
    question: How do I see every alert and artifact attached to one Cortex XDR incident?
  - id: updateIncident
    intent: Update a Cortex XDR incident
    question: How do I reassign a Cortex XDR incident to another analyst?
  - id: postIncidentManagementGetIncidents
    intent: List Xpanse attack surface incidents
    question: Which attack surface exposures has Xpanse flagged that still need remediation?
  - id: postIncidentManagementUpdateIncident
    intent: Update an Xpanse attack surface incident
    question: How do I close an attack surface incident once the exposure is fixed?
  - id: createIncident
    intent: Create a Cortex XSOAR incident
    question: How do I open a new incident in Cortex XSOAR from an external alert?
  - id: searchIncidentsGet
    intent: Search XSOAR incidents with a query string
    question: Can I search XSOAR incidents with a Lucene query like status:Active AND severity:High?
  - id: searchIncidentsPost
    intent: Search XSOAR incidents with a structured filter
    question: How do I run a complex XSOAR incident search with field selection and sorting?
  phrasing_ops: 20
  slug: palo-alto-networks-incidents-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: Data source configuration for log ingestion.
  name: Palo Alto Networks Ingestion API
  phrasing_intents:
  - id: configureDatasource
    intent: Configure a log ingestion data source
    question: How do I get third-party logs ingested into XSIAM?
  phrasing_ops: 1
  slug: palo-alto-networks-ingestion-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: Investigation management.
  name: Palo Alto Networks Investigations API
  phrasing_intents:
  - id: getInvestigation
    intent: Get an investigation's details
    question: What's in the war room and playbook status of a specific investigation?
  - id: createInvestigation
    intent: Start an investigation on an incident
    question: How do I open a new investigation on an existing incident?
  phrasing_ops: 2
  slug: palo-alto-networks-investigations-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: LAN network configuration for defining local networks at SD-WAN sites.
  name: Palo Alto Networks LAN Networks API
  phrasing_intents:
  - id: listSiteLANNetworks
    intent: List LAN networks at an SD-WAN site
    question: Which local subnets and VLANs are served at an SD-WAN site?
  - id: createSiteLANNetwork
    intent: Add a LAN network to an SD-WAN site
    question: How do I add a new subnet to an SD-WAN branch site?
  phrasing_ops: 2
  slug: palo-alto-networks-lannetworks-api
- baseURL: https://api.sase.paloaltonetworks.com/adem/telemetry/v2
  baseurl_source: declared
  description: Detailed network performance metrics providing granular visibility into each segment of the user-to-application connection.
  name: Palo Alto Networks Metrics API
  phrasing_intents:
  - id: getPerformanceMetrics
    intent: Get ADEM performance metrics
    question: What latency, jitter and packet loss are users seeing to an application?
  phrasing_ops: 1
  slug: palo-alto-networks-metrics-api
- baseURL: https://api.stratacloud.paloaltonetworks.com/aiops/bpa/v1
  baseurl_source: declared
  description: Site performance metrics, application usage data, and alarm monitoring.
  name: Palo Alto Networks Monitoring API
  phrasing_intents:
  - id: getSiteMetrics
    intent: Get performance metrics for an SD-WAN site
    question: What latency, jitter and packet loss is my SD-WAN site seeing?
  - id: getApplicationUsage
    intent: Get application usage across SD-WAN sites
    question: Which applications use the most bandwidth across my SD-WAN?
  - id: listAlarms
    intent: List active SD-WAN alarms
    question: Are there any active alarms on my SD-WAN right now?
  - id: get5GSecurityMetrics
    intent: Get 5G security metrics per network slice
    question: How many threats were detected in 5G traffic per network slice?
  phrasing_ops: 4
  slug: palo-alto-networks-monitoring-api
- baseURL: https://api.sase.paloaltonetworks.com/5g/v1
  baseurl_source: declared
  description: 5G network slice configuration and management.
  name: Palo Alto Networks Network Slices API
  phrasing_intents:
  - id: listNetworkSlices
    intent: List 5G network slices
    question: Which 5G network slices are configured for my tenant?
  - id: createNetworkSlice
    intent: Create a 5G network slice
    question: How do I define a new 5G network slice with its own security policy?
  - id: getNetworkSlice
    intent: Get a 5G network slice
    question: What are the full details of a specific 5G network slice?
  - id: updateNetworkSlice
    intent: Update a 5G network slice
    question: Can I change the security policy on an existing 5G slice?
  - id: deleteNetworkSlice
    intent: Delete a 5G network slice
    question: How do I remove a 5G network slice configuration?
  phrasing_ops: 5
  slug: palo-alto-networks-network-slices-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: Address objects, address groups, service objects, service groups, and tag management.
  name: Palo Alto Networks Objects API
  phrasing_intents:
  - id: listAddresses
    intent: List firewall address objects
    question: Which IP addresses, subnets and FQDNs are defined as address objects on my firewall?
  - id: createAddress
    intent: Create a firewall address object
    question: How do I define a new IP netmask, IP range or FQDN as a named address object?
  - id: updateAddress
    intent: Replace an address object's definition
    question: How do I change the IP subnet an existing address object points to?
  - id: deleteAddress
    intent: Delete a firewall address object
    question: Why can't I remove an address object that a security rule still references?
  - id: listAddressGroups
    intent: List firewall address groups
    question: Which address groups are configured on my firewall, static and dynamic?
  - id: createAddressGroup
    intent: Create a static or dynamic address group
    question: Can I build an address group that picks up addresses automatically by tag?
  - id: updateAddressGroup
    intent: Replace an address group definition
    question: How do I change the members of an existing static address group?
  - id: deleteAddressGroup
    intent: Delete a firewall address group
    question: Is it possible to remove an address group without deleting the address objects inside it?
  phrasing_ops: 20
  slug: palo-alto-networks-objects-api
- baseURL: https://api.sase.paloaltonetworks.com/config-orchestration/v1
  baseurl_source: declared
  description: Remote network onboarding status.
  name: Palo Alto Networks Onboarding API
  phrasing_intents:
  - id: getOnboardingStatus
    intent: Check remote network onboarding status
    question: Has my new remote network finished provisioning and brought its tunnel up?
  phrasing_ops: 1
  slug: palo-alto-networks-onboarding-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: Path policy rule management for controlling traffic steering decisions across available WAN links.
  name: Palo Alto Networks Path Rules API
  phrasing_intents:
  - id: listPathRules
    intent: List SD-WAN path policy rules
    question: Which SD-WAN path rules steer traffic across my WAN links?
  - id: createPathRule
    intent: Create an SD-WAN path policy rule
    question: How do I steer an application over a preferred WAN link?
  phrasing_ops: 2
  slug: palo-alto-networks-pathrules-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: Playbook listing and execution.
  name: Palo Alto Networks Playbooks API
  phrasing_intents:
  - id: listPlaybooks
    intent: List XSOAR playbooks
    question: Which automated response playbooks are available in my XSOAR instance?
  - id: runPlaybook
    intent: Run a playbook on an incident
    question: How do I kick off a response playbook against an incident?
  phrasing_ops: 2
  slug: palo-alto-networks-playbooks-api
- baseURL: https://api.sase.paloaltonetworks.com/sspm
  baseurl_source: declared
  description: Security posture check results and remediation status.
  name: Palo Alto Networks Posture Checks API
  phrasing_intents:
  - id: listPostureChecks
    intent: List SaaS posture check results
    question: Which SaaS security posture checks are failing across my onboarded apps?
  - id: getPostureCheck
    intent: Get a posture check's details
    question: How do I fix a specific failing SaaS posture check?
  - id: updatePostureCheckStatus
    intent: Update a posture check's status
    question: How do I suppress a SaaS posture check with a justification?
  phrasing_ops: 3
  slug: palo-alto-networks-posture-checks-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: IP prefix list management for use in security rule source and destination criteria.
  name: Palo Alto Networks Prefix Lists API
  phrasing_intents:
  - id: listPrefixLists
    intent: List prefix lists in a rulestack
    question: What IP prefix lists are defined in my rulestack?
  - id: createPrefixList
    intent: Create a prefix list
    question: How do I create a list of CIDR blocks to use in security rules?
  phrasing_ops: 2
  slug: palo-alto-networks-prefixlists-api
- baseURL: https://security.paloaltonetworks.com/api
  baseurl_source: declared
  description: Query affected products referenced in security advisories.
  name: Palo Alto Networks Products API
  phrasing_intents:
  - id: listAffectedProducts
    intent: List products with security advisories
    question: Which products have at least one published security advisory?
  phrasing_ops: 1
  slug: palo-alto-networks-products-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: Email recipient retrieval operations.
  name: Palo Alto Networks Recipients API
  phrasing_intents:
  - id: getEmailIncidentRecipients
    intent: List recipients of an email DLP incident
    question: Who received the email that triggered a DLP incident, including CC and BCC?
  phrasing_ops: 1
  slug: palo-alto-networks-recipients-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Data security risk identification and management.
  name: Palo Alto Networks Risks API
  phrasing_intents:
  - id: listRisks
    intent: List data security risks
    question: Which data stores have sensitive data exposed by insecure configurations?
  - id: getRisk
    intent: Get details and remediation for a data risk
    question: What remediation steps are recommended for a specific data risk?
  - id: updateRiskStatus
    intent: Change a data risk's status
    question: How do I mark a data risk as remediated after fixing the data store?
  phrasing_ops: 3
  slug: palo-alto-networks-risks-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: Rule stack management. Rule stacks contain the security policy applied to Cloud NGFW instances.
  name: Palo Alto Networks Rule Stacks API
  phrasing_intents:
  - id: listRuleStacks
    intent: List Cloud NGFW rule stacks
    question: Which rule stacks exist in my Cloud NGFW account?
  - id: createRuleStack
    intent: Create a firewall rule stack
    question: How do I create a new rule stack to hold security rules and FQDN lists for Cloud NGFW?
  - id: getRuleStack
    intent: Get a rule stack's configuration
    question: What is configured in a specific rule stack right now?
  - id: updateRuleStack
    intent: Update a rule stack's configuration
    question: How do I stage changes to an existing rule stack before committing them?
  - id: deleteRuleStack
    intent: Delete a rule stack
    question: How do I delete a rule stack I no longer need?
  - id: commitRuleStack
    intent: Commit a rule stack to running config
    question: How do I push my staged rule stack changes out to the active firewalls?
  phrasing_ops: 6
  slug: palo-alto-networks-rulestacks-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: Script execution and results retrieval.
  name: Palo Alto Networks Scripts API
  phrasing_intents:
  - id: runScript
    intent: Run a library script on endpoints
    question: Can I run a remediation script on several endpoints at once?
  - id: getScriptExecutionResults
    intent: Get results of a script run
    question: What output did my script produce on each endpoint?
  phrasing_ops: 2
  slug: palo-alto-networks-scripts-api
- baseURL: https://api.sase.paloaltonetworks.com/5g/v1
  baseurl_source: declared
  description: 5G security policy management.
  name: Palo Alto Networks Security Policies API
  phrasing_intents:
  - id: list5GSecurityPolicies
    intent: List 5G security policies
    question: Which 5G security policies are applied to my network slices?
  - id: create5GSecurityPolicy
    intent: Create a 5G security policy
    question: How do I create a 5G security policy with threat prevention and URL filtering?
  - id: get5GSecurityPolicy
    intent: Get a 5G security policy
    question: What inspection settings does a particular 5G security policy enforce?
  - id: update5GSecurityPolicy
    intent: Update a 5G security policy
    question: Can I disable an existing 5G security policy without deleting it?
  - id: delete5GSecurityPolicy
    intent: Delete a 5G security policy
    question: How do I remove a 5G security policy?
  phrasing_ops: 5
  slug: palo-alto-networks-security-policies-api
- baseURL: https://api.sase.paloaltonetworks.com/iam/v1
  baseurl_source: declared
  description: Service account management and credential generation.
  name: Palo Alto Networks Service Accounts API
  phrasing_intents:
  - id: listServiceAccounts
    intent: List service accounts
    question: Which service accounts exist for API automation in my tenant?
  - id: createServiceAccount
    intent: Create a service account
    question: How do I create a machine identity for API automation?
  - id: getServiceAccount
    intent: Get a service account
    question: What are the full details of one service account?
  - id: updateServiceAccount
    intent: Rename or re-describe a service account
    question: Can I change a service account's display name?
  - id: deleteServiceAccount
    intent: Delete a service account
    question: What happens to active API sessions when I delete a service account?
  - id: generateServiceAccountCredentials
    intent: Generate client credentials for a service account
    question: How do I get a client ID and secret for a service account?
  - id: revokeServiceAccountKey
    intent: Revoke a service account key
    question: Can I revoke one leaked key without deleting the whole service account?
  - id: get-iam-v1-service_accounts
    intent: List service accounts
    question: Which service accounts exist in my Prisma SASE tenant?
  phrasing_ops: 13
  slug: palo-alto-networks-service-accounts-api
- baseURL: https://api.strata.paloaltonetworks.com
  baseurl_source: declared
  description: The Sse API from Palo Alto Networks — 2 operation(s) for sse.
  name: Palo Alto Networks Sse API
  phrasing_intents:
  - id: listServices
    intent: List service objects
    question: Which TCP and UDP service objects are defined for my security policies?
  - id: createService
    intent: Create a service object
    question: How do I define a custom port or port range as a service object?
  - id: getService
    intent: Get a service object
    question: What protocol and ports does a particular service object cover?
  - id: updateService
    intent: Update a service object
    question: How do I change the port on an existing service object?
  - id: deleteService
    intent: Delete a service object
    question: How do I remove a service object?
  phrasing_ops: 5
  slug: palo-alto-networks-sse-api
- baseURL: https://api.dns.service.paloaltonetworks.com/v1
  baseurl_source: declared
  description: Network access and DNS query statistics.
  name: Palo Alto Networks Statistics API
  phrasing_intents:
  - id: getNetworkStats
    intent: Get DNS and network access statistics
    question: How many DNS queries did a customer environment make over a time window?
  phrasing_ops: 1
  slug: palo-alto-networks-statistics-api
- baseURL: https://wildfire.paloaltonetworks.com/publicapi
  baseurl_source: declared
  description: File, URL, and link submission for malware analysis.
  name: Palo Alto Networks Submit API
  phrasing_intents:
  - id: submitFile
    intent: Submit a file to WildFire for malware analysis
    question: How do I check whether a suspicious executable or Office document is malware?
  - id: submitUrl
    intent: Submit a URL to WildFire for phishing analysis
    question: Can WildFire tell me if a website is phishing or serving malware?
  - id: submitLink
    intent: Submit an email or document link to WildFire
    question: How do I analyze a hyperlink I pulled out of an email body?
  phrasing_ops: 3
  slug: palo-alto-networks-submit-api
- baseURL: https://api.sase.paloaltonetworks.com/ztna
  baseurl_source: declared
  description: Subnet-based access rules for ZTNA network segments.
  name: Palo Alto Networks Subnet Rules API
  phrasing_intents:
  - id: listSubnetRules
    intent: List subnet-based ZTNA access rules
    question: Which IP ranges are reachable through my ZTNA connectors?
  - id: createSubnetRule
    intent: Create a subnet-based ZTNA access rule
    question: How do I make a subnet reachable through a ZTNA connector group?
  phrasing_ops: 2
  slug: palo-alto-networks-subnet-rules-api
- baseURL: https://api.stratacloud.paloaltonetworks.com/aiops/bpa/v1
  baseurl_source: declared
  description: Subscription and license management.
  name: Palo Alto Networks Subscriptions API
  phrasing_intents:
  - id: listSubscriptions
    intent: List subscriptions for a tenant service group
    question: What active subscriptions and SKUs does my tenant service group have?
  - id: getSubscription
    intent: Get subscription details
    question: When does a particular subscription term end and how much of it is used?
  - id: getSubscriptionEntitlements
    intent: Get a subscription's entitlements
    question: Which individual features are entitled under a subscription and how many remain available?
  - id: allocateLicenses
    intent: Allocate subscription licenses to child TSGs
    question: How do I split license capacity from one subscription across child tenants?
  phrasing_ops: 4
  slug: palo-alto-networks-subscriptions-api
- baseURL: https://api.sase.paloaltonetworks.com/logging-service/v1
  baseurl_source: declared
  description: Syslog forwarding destination management.
  name: Palo Alto Networks Syslog Destinations API
  phrasing_intents:
  - id: listSyslogDestinations
    intent: List syslog destinations for a profile
    question: Which syslog servers is a log forwarding profile sending to?
  - id: createSyslogDestination
    intent: Add a syslog destination to a profile
    question: How do I forward logs to my SIEM over syslog?
  phrasing_ops: 2
  slug: palo-alto-networks-syslog-destinations-api
- baseURL: https://api.sase.paloaltonetworks.com/ai-red-teaming
  baseurl_source: declared
  description: AI scan target definition and management.
  name: Palo Alto Networks Targets API
  phrasing_intents:
  - id: createScanTarget
    intent: Register an AI application as a scan target
    question: How do I add an LLM endpoint so it can be vulnerability scanned?
  - id: listScanTargets
    intent: List AI red teaming scan targets
    question: Which AI application endpoints have I registered as scan targets?
  - id: getScanTarget
    intent: Get details of a scan target
    question: What endpoint URL and auth configuration does a specific scan target have?
  - id: deleteScanTarget
    intent: Delete a scan target
    question: How do I remove an AI application I no longer want to scan?
  phrasing_ops: 4
  slug: palo-alto-networks-targets-api
- baseURL: https://api.stratacloud.paloaltonetworks.com/aiops/bpa/v1
  baseurl_source: declared
  description: Tenant Service Group lifecycle management and hierarchy queries.
  name: Palo Alto Networks Tenant Service Groups API
  phrasing_intents:
  - id: listTenantServiceGroups
    intent: List Tenant Service Groups
    question: Which Tenant Service Groups can my service account see?
  - id: createTenantServiceGroup
    intent: Create a Tenant Service Group
    question: How do I create a new tenant under an existing TSG?
  - id: getTenantServiceGroup
    intent: Get Tenant Service Group details
    question: What licenses and status does a specific Tenant Service Group have?
  - id: updateTenantServiceGroup
    intent: Update a Tenant Service Group
    question: How do I rename a Tenant Service Group?
  - id: deleteTenantServiceGroup
    intent: Delete a Tenant Service Group
    question: How do I permanently remove a Tenant Service Group?
  - id: listChildTenantServiceGroups
    intent: List child TSGs of a Tenant Service Group
    question: Which tenants sit directly under a given TSG?
  phrasing_ops: 6
  slug: palo-alto-networks-tenant-service-groups-api
- baseURL: https://api.sase.paloaltonetworks.com/5g/v1
  baseurl_source: declared
  description: Multi-tenant 5G configuration management.
  name: Palo Alto Networks Tenants API
  phrasing_intents:
  - id: list5GTenants
    intent: List 5G tenant configurations
    question: Which customers or business units have tenant configurations in my 5G security deployment?
  - id: create5GTenant
    intent: Create a 5G tenant configuration
    question: How do I onboard a new business unit as a 5G security tenant?
  - id: get5GTenant
    intent: Get a 5G tenant configuration
    question: What slices and default policy does one 5G tenant use?
  - id: update5GTenant
    intent: Update a 5G tenant configuration
    question: Can I reassign slices for an existing 5G tenant?
  - id: delete5GTenant
    intent: Delete a 5G tenant configuration
    question: How do I offboard a tenant from my 5G security deployment?
  phrasing_ops: 5
  slug: palo-alto-networks-tenants-api
- baseURL: https://api.sase.paloaltonetworks.com/adem/telemetry/v2
  baseurl_source: declared
  description: Synthetic test results for proactive monitoring of application reachability and performance from user endpoints.
  name: Palo Alto Networks Tests API
  phrasing_intents:
  - id: getTestResults
    intent: Get synthetic test results
    question: What latency and availability did a synthetic test measure?
  phrasing_ops: 1
  slug: palo-alto-networks-tests-api
- baseURL: https://api.threatvault.paloaltonetworks.com/service/v1
  baseurl_source: declared
  description: Threat signature lookup and metadata retrieval.
  name: Palo Alto Networks Threats API
  phrasing_intents:
  - id: getThreats
    intent: Look up threat signatures
    question: Which Threat Vault signatures cover a given CVE?
  - id: getThreatHistory
    intent: Get the version history of a signature
    question: How has a specific threat signature changed over time?
  phrasing_ops: 2
  slug: palo-alto-networks-threats-api
- baseURL: https://wildfire.paloaltonetworks.com/publicapi
  baseurl_source: declared
  description: Retrieve analysis verdicts by file hash.
  name: Palo Alto Networks Verdict API
  phrasing_intents:
  - id: getVerdict
    intent: Get the WildFire verdict for a file hash
    question: Is this file hash malware, grayware, phishing, or benign according to WildFire?
  - id: getBulkVerdicts
    intent: Get WildFire verdicts for many hashes
    question: Can I check up to 500 file hashes against WildFire in one request?
  phrasing_ops: 2
  slug: palo-alto-networks-verdict-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: Device vulnerability tracking operations.
  name: Palo Alto Networks Vulnerabilities API
  phrasing_intents:
  - id: listVulnerabilities
    intent: List vulnerabilities on IoT devices
    question: Which known vulnerabilities affect my discovered IoT devices?
  - id: getVulnerabilityDetail
    intent: Get vulnerability details for a device
    question: What is the CVE detail and remediation for a vulnerability on one device?
  phrasing_ops: 2
  slug: palo-alto-networks-vulnerabilities-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: WAN interface configuration for defining upstream connectivity including ISP links, MPLS circuits, and LTE connections.
  name: Palo Alto Networks WAN Interfaces API
  phrasing_intents:
  - id: listSiteWANInterfaces
    intent: List WAN interfaces at a site
    question: Which WAN links, like broadband, MPLS or LTE, are configured at a site?
  - id: createSiteWANInterface
    intent: Create a WAN interface at a site
    question: How do I add a new WAN circuit to a branch site?
  phrasing_ops: 2
  slug: palo-alto-networks-waninterfaces-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: XQL (Extended Query Language) query execution.
  name: Palo Alto Networks XQL API
  phrasing_intents:
  - id: startXqlQuery
    intent: Start an XQL query
    question: How do I query endpoint and network telemetry in the Cortex XDR data lake?
  - id: getXqlQueryResults
    intent: Get results of an XQL query
    question: When is my XQL query finished and ready to read?
  phrasing_ops: 2
  slug: palo-alto-networks-xql-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Agent Controller API from Palo Alto Networks — 3 operation(s) for agent controller.
  name: Palo Alto Networks Agent Controller API
  phrasing_intents:
  - id: AgentController.getAgentProperties
    intent: Get ADEM agent properties
    question: What properties are reported by Autonomous DEM agents on user endpoints?
  - id: AgentController.getAgentMetric
    intent: Get ADEM agent metrics
    question: What performance metrics are my ADEM agents reporting?
  - id: AgentController.getAgentScore
    intent: Get ADEM agent experience scores
    question: Which users have the worst digital experience scores?
  phrasing_ops: 3
  slug: palo-alto-networks-agent-controller-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The application controller API from Palo Alto Networks — 2 operation(s) for application controller.
  name: Palo Alto Networks application controller API
  phrasing_intents:
  - id: ApplicationController.getApplicationMetric
    intent: Get application experience metrics
    question: What are the raw application performance metrics for my users over a time range?
  - id: ApplicationController.getApplicationScore
    intent: Get application experience scores
    question: How are my applications scoring on digital experience?
  phrasing_ops: 2
  slug: palo-alto-networks-application-controller-api
- baseURL: https://auth.apps.paloaltonetworks.com
  baseurl_source: declared
  description: The Auth Service API from Palo Alto Networks — 2 operation(s) for auth service.
  name: Palo Alto Networks Auth Service API
  phrasing_intents:
  - id: post-auth-v1-oauth2-access_token
    intent: Get a SASE access token
    question: How do I get an access token for the SASE APIs with my client ID and secret?
  - id: post-auth-v1-oauth2-userinfo
    intent: Get claims for a supplied access token
    question: Can I inspect the claims of a token other than the one I'm calling with?
  - id: get-auth-v1-oauth2-userinfo
    intent: Get claims for my current token
    question: Who does the token I'm calling with belong to?
  phrasing_ops: 3
  slug: palo-alto-networks-auth-service-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Custom Roles API from Palo Alto Networks — 2 operation(s) for custom roles.
  name: Palo Alto Networks Custom Roles API
  phrasing_intents:
  - id: get-iam-v1-custom_roles
    intent: List custom roles
    question: Which custom IAM roles are available to my tenant service group?
  - id: post-iam-v1-custom_roles
    intent: Create a custom role
    question: How do I create a custom role with only specific permissions?
  - id: delete-iam-v1-custom_roles-name
    intent: Delete a custom role
    question: How do I delete a custom role?
  - id: get-iam-v1-custom_roles-name
    intent: Get a custom role
    question: What permissions does a particular custom role grant?
  - id: put-iam-v1-custom_roles-name
    intent: Update a custom role
    question: Can I change the permissions on an existing custom role?
  phrasing_ops: 5
  slug: palo-alto-networks-custom-roles-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Data asset discovery and inventory operations.
  name: Palo Alto Networks Data Assets API
  phrasing_intents:
  - id: listDataAssets
    intent: List discovered cloud data assets
    question: Which tables, columns or buckets contain sensitive data in my cloud?
  - id: getDataAsset
    intent: Get a data asset's classification and risk
    question: What sensitive data findings and risk posture does one data asset have?
  phrasing_ops: 2
  slug: palo-alto-networks-data-assets-api
- baseURL: https://api.prismacloud.io
  baseurl_source: declared
  description: Manage a list of trusted IP addresses with respect to alerts and a list of trusted login IP addresses.
  name: Palo Alto Networks IP Allowlist API
  phrasing_intents:
  - id: get-networks-list
    intent: List trusted public networks
    question: Which public networks are on my trusted IP allow list?
  - id: add-a-network
    intent: Add a trusted public network
    question: How do I add a new trusted network to the IP allow list?
  - id: get-network-info
    intent: Get a trusted network
    question: What CIDRs are in a specific trusted network?
  - id: rename-a-network
    intent: Rename a trusted network
    question: Can I rename a trusted network without recreating it?
  - id: add-cidr-block
    intent: Add a CIDR block to a trusted network
    question: How do I add an IP range to one of my trusted networks?
  - id: update-cidr-block
    intent: Update a CIDR block in a trusted network
    question: Can I change an existing CIDR range in a trusted network?
  - id: delete-cidr-block
    intent: Remove a CIDR block from a trusted network
    question: How do I drop an IP range from a trusted network?
  - id: list-login-ip-allow-lists
    intent: List login IP allow lists
    question: Which IP ranges are allowed to log in to my Prisma Cloud tenant?
  phrasing_ops: 14
  slug: palo-alto-networks-ip-allowlist-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: Owned IP range management.
  name: Palo Alto Networks IP Ranges API
  phrasing_intents:
  - id: getOwnedIpRanges
    intent: List IP ranges owned by the organization
    question: Which IP ranges does Xpanse treat as owned by my organization?
  phrasing_ops: 1
  slug: palo-alto-networks-ip-ranges-api
- baseURL: https://api.strata.paloaltonetworks.com/config/network/v1
  baseurl_source: declared
  description: IPsec Tunnels
  name: Palo Alto Networks IP Sec Tunnels API
  phrasing_intents:
  - id: ListIPsecTunnels
    intent: List Prisma Access IPSec tunnels
    question: Which IPSec VPN tunnels connect my branches to Prisma Access?
  - id: CreateIPsecTunnels
    intent: Create a Prisma Access IPSec tunnel
    question: How do I add an IPSec tunnel to the Prisma Access candidate configuration?
  - id: GetIPsecTunnelsByID
    intent: Get a Prisma Access IPSec tunnel
    question: What is the configuration of one Prisma Access IPSec tunnel in the candidate config?
  - id: UpdateIPsecTunnelsByID
    intent: Update a Prisma Access IPSec tunnel
    question: How do I change a Prisma Access IPSec tunnel in the candidate configuration?
  - id: DeleteIPsecTunnelsByID
    intent: Delete a Prisma Access IPSec tunnel
    question: How do I remove an IPSec tunnel from the Prisma Access candidate configuration?
  - id: get-sse-config-v1-ipsec-tunnels
    intent: List IPSec tunnels via the SSE config API
    question: Which IPSec tunnels exist in a folder through the SSE config v1 endpoint?
  - id: post-sse-config-v1-ipsec-tunnels
    intent: Create an IPSec tunnel via the SSE config API
    question: How do I create an IPSec tunnel through the SSE config v1 API?
  - id: delete-sse-config-v1-ipsec-tunnels-id
    intent: Delete an IPSec tunnel via the SSE config API
    question: How do I delete an IPSec tunnel with the SSE config v1 endpoint?
  phrasing_ops: 10
  slug: palo-alto-networks-ip-sec-tunnels-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The License Types API from Palo Alto Networks — 1 operation(s) for license types.
  name: Palo Alto Networks License Types API
  phrasing_intents:
  - id: get-sse-config-v1-license-types
    intent: List Prisma Access licenses
    question: What Prisma Access licenses do I have?
  phrasing_ops: 1
  slug: palo-alto-networks-license-types-api
- baseURL: https://api.us-east-1.aws.cloudngfw.paloaltonetworks.com
  baseurl_source: declared
  description: The Manage API tokens API from Palo Alto Networks — 4 operation(s) for manage api tokens.
  name: Palo Alto Networks Manage API tokens API
  phrasing_intents:
  - id: get-v1-mgmt-tokens
    intent: Describe programmatic access settings
    question: Is programmatic API access enabled for my Cloud NGFW tenant?
  - id: get-v1-mgmt-tokens-cloudfirewalladmin
    intent: Get a token for the firewall admin role
    question: How do I get a JWT to call firewall management APIs as a CloudFirewallAdmin?
  - id: get-v1-mgmt-tokens-cloudglobalrulestackadmin
    intent: Get a token for the global rulestack admin role
    question: Which token do I need to manage global rulestacks programmatically?
  - id: get-v1-mgmt-tokens-cloudrulestackadmin
    intent: Get a token for the local rulestack admin role
    question: What token lets me manage local rulestacks through the API?
  phrasing_ops: 4
  slug: palo-alto-networks-manage-api-tokens-api
- baseURL: https://{firewall}/api/
  baseurl_source: declared
  description: The Notification Profiles API from Palo Alto Networks — 6 operation(s) for notification profiles.
  name: Palo Alto Networks Notification Profiles API
  phrasing_intents:
  - id: getApiCloud20AggNotificationsProfiles
    intent: List multi-tenant notification profiles
    question: Which notification profiles are set up for my tenant?
  - id: postApiCloud20AggNotificationsProfiles
    intent: Create a notification profile
    question: How do I set up a notification profile that alerts on child tenant upgrades?
  - id: getApiCloud20AggNotificationsProfilesByNotificationProfileId
    intent: Get a notification profile
    question: What tenants and channels does one notification profile cover?
  - id: deleteApiCloud20AggNotificationsProfilesByNotificationProfileId
    intent: Delete a notification profile
    question: How do I permanently remove a notification profile?
  - id: putApiCloud20AggNotificationsProfilesOpstate
    intent: Enable or disable a notification profile
    question: How do I turn on a notification profile so it starts sending alerts?
  - id: getApiCloud20AggNotificationsProfilesTypes
    intent: List notification types and categories
    question: What notification types and categories can a profile subscribe to?
  - id: postApiCloud20AggNotificationsProfilesWebhookTest
    intent: Test a notification webhook
    question: Can the notification service reach my webhook URL before I use it in a profile?
  - id: postApiCloud20AggNotificationsProfilesRetryOp
    intent: Retry pushing an incident profile to tenants
    question: What can I do when an incident profile failed to push to some child tenants?
  phrasing_ops: 8
  slug: palo-alto-networks-notification-profiles-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The Permission Sets API from Palo Alto Networks — 2 operation(s) for permission sets.
  name: Palo Alto Networks Permission Sets API
  phrasing_intents:
  - id: get-iam-v1-permission_sets
    intent: List permission sets
    question: Which permission sets can I use when building a custom role?
  - id: get-iam-v1-permission_sets-name
    intent: Get a permission set
    question: What exactly does a specific permission set grant?
  phrasing_ops: 2
  slug: palo-alto-networks-permission-sets-api
- baseURL: https://api.threatvault.paloaltonetworks.com/service/v1
  baseurl_source: declared
  description: Content release notes for PAN-OS content updates.
  name: Palo Alto Networks Release Notes API
  phrasing_intents:
  - id: getReleaseNotes
    intent: Get content release notes
    question: What changed in a particular content release version?
  phrasing_ops: 1
  slug: palo-alto-networks-release-notes-api
- baseURL: https://api.sase.paloaltonetworks.com
  baseurl_source: declared
  description: The User Accounts API from Palo Alto Networks — 1 operation(s) for user accounts.
  name: Palo Alto Networks User Accounts API
  phrasing_intents:
  - id: get-iam-v1-sso_users
    intent: Check whether an email has a login account
    question: Does this email address already have a Palo Alto Networks login account?
  - id: post-iam-v1-sso_users
    intent: Create an SSO login account
    question: How do I create an SSO account for a new user?
  phrasing_ops: 2
  slug: palo-alto-networks-user-accounts-api
arazzos:
- description: Find an endpoint by filter, isolate it from the network, then poll until isolation is confirmed.
  name: Cortex XDR Endpoint Isolation and Verification
  slug: palo-alto-networks-cortex-xdr-endpoint-isolation-workflow
- description: List XDR incidents, pull full detail for one, then update its status and assignee.
  name: Cortex XDR Incident Triage and Resolution
  slug: palo-alto-networks-cortex-xdr-incident-triage-workflow
- description: Run a remediation script on endpoints, then poll the action until execution results are ready.
  name: Cortex XDR Script Remediation with Result Polling
  slug: palo-alto-networks-cortex-xdr-script-remediation-workflow
- description: Launch an XQL query against the XDR data lake and poll until results are ready.
  name: Cortex XDR XQL Threat Hunt
  slug: palo-alto-networks-cortex-xdr-xql-hunt-workflow
- description: List XSIAM incidents, enumerate assets, then run an XQL hunt and poll for results.
  name: Cortex XSIAM Incident-Driven Asset and XQL Hunt
  slug: palo-alto-networks-cortex-xsiam-incident-hunt-workflow
- description: Create an XSOAR incident, run a response playbook against it, then log a war room entry.
  name: Cortex XSOAR Incident Response Orchestration
  slug: palo-alto-networks-cortex-xsoar-incident-response-workflow
- description: List unresolved IoT Security alerts, inspect one, then mark it resolved with a reason.
  name: IoT Security Alert Investigation and Resolution
  slug: palo-alto-networks-iot-security-alert-remediation-workflow
- description: List IoT devices, inspect one device, then pull its policy recommendations.
  name: IoT Security Device Risk and Policy Recommendation
  slug: palo-alto-networks-iot-security-device-risk-workflow
- description: Authenticate to Prisma Cloud, list open alerts, inspect one, then dismiss it with a note.
  name: Prisma Cloud Alert Triage and Dismissal
  slug: palo-alto-networks-prisma-cloud-alert-triage-workflow
- description: Authenticate to Prisma Cloud, list policies, inspect one, then update it.
  name: Prisma Cloud Policy Review and Update
  slug: palo-alto-networks-prisma-cloud-policy-lifecycle-workflow
- description: Authenticate to Prisma Cloud, run an RQL config query, then run a matching RQL asset query.
  name: Prisma Cloud RQL Configuration and Asset Search
  slug: palo-alto-networks-prisma-cloud-rql-config-search-workflow
artifact_total: 2251
asyncapis:
- description: ''
  name: Palo Alto Cortex XDR Webhooks
  slug: palo-alto-cortex-xdr-webhooks-asyncapi-original
- description: Cortex XSIAM Data Ingestion provides streaming log and event ingestion endpoints for collecting security telemetry from external data sources into the XSIAM data lake. The ingestion service accepts da
  name: Cortex XSIAM Data Ingestion
  slug: palo-alto-cortex-xsiam-data-ingestion-asyncapi-original
- description: Prisma Cloud Cloud Security Posture Management (CSPM) Webhooks deliver real-time event notifications for policy violations and security alerts across multi-cloud environments including AWS, Azure, GCP
  name: Prisma Cloud CSPM Webhooks
  slug: palo-alto-prisma-cloud-webhooks-asyncapi-original
- description: Palo Alto Networks SASE (Secure Access Service Edge) delivers real-time notifications for security incidents, platform announcements, dataplane upgrades, and certificate expiration warnings across mul
  name: SASE Multitenant Notifications
  slug: palo-alto-sase-notifications-asyncapi-original
- description: Strata Logging Service Log Forwarding enables security operations teams to forward security logs from Palo Alto Networks next-generation firewalls, Prisma Access, and other Strata products to external
  name: Strata Logging Service Log Forwarding
  slug: palo-alto-strata-logging-forwarding-asyncapi-original
collections:
- collection_type: postman
  name: Palo Alto Networks AIOps for NGFW BPA API
  slug: postman-palo-alto-aiops-ngfw-bpa-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Autonomous DEM API
  slug: postman-palo-alto-autonomous-dem-api-openapi-original
- collection_type: postman
  name: CIE Directory Sync Service APIs Mounted on Strata Cloud Manger
  slug: postman-palo-alto-cloud-identity-engine-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Cloud NGFW for AWS REST API
  slug: postman-palo-alto-cloud-ngfw-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Cortex XDR REST API
  slug: postman-palo-alto-cortex-xdr-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Cortex Xpanse REST API
  slug: postman-palo-alto-cortex-xpanse-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Cortex XSIAM REST API
  slug: postman-palo-alto-cortex-xsiam-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Cortex XSOAR REST API
  slug: postman-palo-alto-cortex-xsoar-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Enterprise DLP API
  slug: postman-palo-alto-dlp-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks DNS Security API
  slug: postman-palo-alto-dns-security-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Email DLP API
  slug: postman-palo-alto-email-dlp-api-openapi-original
- collection_type: postman
  name: Incident Security Service Posture Management API
  slug: postman-palo-alto-identity-security-posture-management-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks IoT Security API
  slug: postman-palo-alto-iot-security-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks PAN-OS REST API
  slug: postman-palo-alto-pan-os-rest-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Prisma Access Configuration API
  slug: postman-palo-alto-prisma-access-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Prisma Access Browser Management API
  slug: postman-palo-alto-prisma-access-browser-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Prisma Access Insights API
  slug: postman-palo-alto-prisma-access-insights-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Prisma AIRS AI Red Teaming API
  slug: postman-palo-alto-prisma-airs-ai-red-teaming-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Prisma AIRS API
  slug: postman-palo-alto-prisma-airs-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Prisma Cloud Code Security API
  slug: postman-palo-alto-prisma-cloud-code-security-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Prisma Cloud Compute API
  slug: postman-palo-alto-prisma-cloud-compute-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Prisma Cloud CSPM API
  slug: postman-palo-alto-prisma-cloud-cspm-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Prisma Cloud DSPM API
  slug: postman-palo-alto-prisma-cloud-dspm-api-openapi-original
- collection_type: postman
  name: 'Prisma Cloud: Managed Security Service Provider (MSSP)'
  slug: postman-palo-alto-prisma-cloud-mssp-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Prisma SD-WAN API
  slug: postman-palo-alto-prisma-sd-wan-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks SaaS Security API
  slug: postman-palo-alto-saas-security-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks SASE 5G Managed Services API
  slug: postman-palo-alto-sase-5g-api-openapi-original
- collection_type: postman
  name: SASE 5G Monitor Service API
  slug: postman-palo-alto-sase-5g-monitor-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks SASE Aggregate Monitoring API
  slug: postman-palo-alto-sase-aggregate-monitoring-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks SASE Configuration Orchestration API
  slug: postman-palo-alto-sase-config-orchestration-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks SASE IAM Service API
  slug: postman-palo-alto-sase-iam-api-openapi-original
- collection_type: postman
  name: SP Interconnect Manage APIs
  slug: postman-palo-alto-sase-multitenant-interconnect-api-openapi-original
- collection_type: postman
  name: Multi-Tenant Notifications API
  slug: postman-palo-alto-sase-multitenant-notifications-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks SASE Subscription Service API
  slug: postman-palo-alto-sase-subscription-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks SASE Tenancy Service API
  slug: postman-palo-alto-sase-tenancy-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Security Advisory API
  slug: postman-palo-alto-security-advisory-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks SaaS Security Posture Management API
  slug: postman-palo-alto-sspm-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Strata Cloud Manager API
  slug: postman-palo-alto-strata-cloud-manager-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Strata Logging Service API
  slug: postman-palo-alto-strata-logging-service-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks Threat Vault API
  slug: postman-palo-alto-threat-vault-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks WildFire API
  slug: postman-palo-alto-wildfire-api-openapi-original
- collection_type: postman
  name: Palo Alto Networks ZTNA Connector API
  slug: postman-palo-alto-ztna-connector-api-openapi-original
- collection_type: open
  name: 'Prisma Cloud: Managed Security Service Provider (MSSP)'
  slug: open-palo-alto-prisma-cloud-mssp-api-openapi-original
common:
- group: commercial
  href: https://artifacts.apis.io/palo-alto-networks/plans/palo-alto-networks-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/palo-alto-networks-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/palo-alto-networks/rate-limits/palo-alto-networks-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/palo-alto-networks-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/palo-alto-networks/finops/palo-alto-networks-finops.yml
  title: ''
  type: FinOps
  url: finops/palo-alto-networks-finops.yml
- group: other
  href: https://artifacts.apis.io/palo-alto-networks/capabilities/palo-alto-networks-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/palo-alto-networks-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/demisto/content/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/demisto/content/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/demisto/content/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/demisto/content/blob/master/LICENSE
- group: agent
  href: https://artifacts.apis.io/palo-alto-networks/agentic-access/palo-alto-networks-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/palo-alto-networks-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/palo-alto-networks/security/palo-alto-networks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/palo-alto-networks-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/palo-alto-networks/authentication/palo-alto-networks-authentication.yml
  title: ''
  type: Authentication
  url: authentication/palo-alto-networks-authentication.yml
- group: auth
  href: https://artifacts.apis.io/palo-alto-networks/scopes/palo-alto-networks-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/palo-alto-networks-scopes.yml
- group: design
  href: https://artifacts.apis.io/palo-alto-networks/arazzo/palo-alto-networks-cortex-xdr-endpoint-isolation-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-cortex-xdr-endpoint-isolation-workflow.yml
- group: design
  href: https://artifacts.apis.io/palo-alto-networks/arazzo/palo-alto-networks-cortex-xdr-incident-triage-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-cortex-xdr-incident-triage-workflow.yml
- group: design
  href: https://artifacts.apis.io/palo-alto-networks/arazzo/palo-alto-networks-cortex-xdr-script-remediation-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-cortex-xdr-script-remediation-workflow.yml
- group: design
  href: https://artifacts.apis.io/palo-alto-networks/arazzo/palo-alto-networks-cortex-xdr-xql-hunt-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-cortex-xdr-xql-hunt-workflow.yml
- group: design
  href: https://artifacts.apis.io/palo-alto-networks/arazzo/palo-alto-networks-cortex-xsiam-incident-hunt-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-cortex-xsiam-incident-hunt-workflow.yml
- group: design
  href: https://artifacts.apis.io/palo-alto-networks/arazzo/palo-alto-networks-cortex-xsoar-incident-response-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-cortex-xsoar-incident-response-workflow.yml
- group: design
  href: https://artifacts.apis.io/palo-alto-networks/arazzo/palo-alto-networks-iot-security-alert-remediation-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-iot-security-alert-remediation-workflow.yml
- group: design
  href: https://artifacts.apis.io/palo-alto-networks/arazzo/palo-alto-networks-iot-security-device-risk-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-iot-security-device-risk-workflow.yml
- group: design
  href: https://artifacts.apis.io/palo-alto-networks/arazzo/palo-alto-networks-prisma-cloud-alert-triage-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-prisma-cloud-alert-triage-workflow.yml
- group: design
  href: https://artifacts.apis.io/palo-alto-networks/arazzo/palo-alto-networks-prisma-cloud-policy-lifecycle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-prisma-cloud-policy-lifecycle-workflow.yml
- group: design
  href: https://artifacts.apis.io/palo-alto-networks/arazzo/palo-alto-networks-prisma-cloud-rql-config-search-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-prisma-cloud-rql-config-search-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://pan.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paloaltonetworks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paloaltonetworks.com/develop/api
- group: company
  title: ''
  type: Website
  url: https://www.paloaltonetworks.com
- group: operate
  title: ''
  type: Support
  url: https://www.paloaltonetworks.com/services/support
- group: company
  title: ''
  type: Blog
  url: https://www.paloaltonetworks.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.paloaltonetworks.com/blog/feed/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paloaltonetworks.com/
- group: operate
  title: ''
  type: Forums
  url: https://live.paloaltonetworks.com/
- group: auth
  title: ''
  type: Security
  url: https://security.paloaltonetworks.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PaloAltoNetworks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/demisto
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pan-unit42
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/PaloAltoNetworks/pan-os-python
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/PaloAltoNetworks/pango
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/PaloAltoNetworks/pan-python
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/PaloAltoNetworks/pan-os-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaloAltoNetworks/prisma-sase-sdk-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaloAltoNetworks/cortex-cloud-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaloAltoNetworks/cloud-ngfw-aws-go
- group: build
  title: ''
  type: CLI
  url: https://github.com/PaloAltoNetworks/homebrew-cortexcli
- group: build
  title: ''
  type: CLI
  url: https://github.com/PaloAltoNetworks/upgrade-assurance-cli
- group: other
  title: ''
  type: TerraformProvider
  url: https://registry.terraform.io/providers/PaloAltoNetworks/panos/latest
- group: other
  title: ''
  type: TerraformProvider
  url: https://registry.terraform.io/providers/PaloAltoNetworks/scm/latest
- group: other
  title: ''
  type: TerraformProvider
  url: https://registry.terraform.io/providers/PaloAltoNetworks/cortexcloud/latest
- group: other
  title: ''
  type: TerraformProvider
  url: https://registry.terraform.io/providers/PaloAltoNetworks/prismasdwan/latest
- group: build
  title: ''
  type: Tools
  url: https://github.com/PaloAltoNetworks/pan-os-upgrade-assurance
- group: build
  title: ''
  type: Tools
  url: https://github.com/PaloAltoNetworks/prisma-cloud-scan
- group: build
  title: ''
  type: Tools
  url: https://github.com/PaloAltoNetworks/cobra-tool
- group: start
  title: ''
  type: Portal
  url: https://gallery.pan.dev/
- group: other
  title: ''
  type: TerraformProvider
  url: https://registry.terraform.io/namespaces/PaloAltoNetworks
- group: other
  title: ''
  type: TerraformProvider
  url: https://registry.terraform.io/providers/PaloAltoNetworks/cloudngfwaws/latest
- group: other
  title: ''
  type: TerraformProvider
  url: https://registry.terraform.io/providers/PaloAltoNetworks/prismacloud/latest
- group: other
  title: ''
  type: TerraformProvider
  url: https://registry.terraform.io/providers/PaloAltoNetworks/prismacloudcompute/latest
- group: build
  title: ''
  type: AnsibleCollection
  url: https://galaxy.ansible.com/paloaltonetworks/panos
- group: learn
  title: ''
  type: Training
  url: https://www.paloaltonetworks.com/services/education
- group: learn
  title: ''
  type: Training
  url: https://learn.paloaltonetworks.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paloaltonetworks.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paloaltonetworks.com/legal
- group: design
  href: https://artifacts.apis.io/palo-alto-networks/json-ld/palo-alto-networks-security-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/palo-alto-networks-security-context.jsonld
- group: docs
  href: https://artifacts.apis.io/palo-alto-networks/asyncapi/palo-alto-sase-notifications-asyncapi-original.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/palo-alto-sase-notifications-asyncapi-original.yml
- group: other
  title: ''
  type: X
  url: https://x.com/PaloAltoNtwks
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@pabornetworks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/palo-alto-networks
- group: company
  title: ''
  type: Blog
  url: https://medium.com/palo-alto-networks-developer-blog
- group: company
  title: ''
  type: BlogRSS
  url: https://medium.com/feed/palo-alto-networks-developer-blog
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.paloaltonetworks.com/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: https://pan.dev/sase/docs/release-notes/changelog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://pan.dev/scm/docs/release-notes/changelog/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/paloaltonetworks
- group: operate
  title: ''
  type: Slack
  url: https://start.paloaltonetworks.com/join-our-slack-community
- group: company
  title: ''
  type: Blog
  url: https://unit42.paloaltonetworks.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://unit42.paloaltonetworks.com/feed/
- group: start
  title: ''
  type: Portal
  url: https://cortex.pan.dev/
- group: start
  title: ''
  type: Portal
  url: https://xsoar.pan.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://pan.dev/swfw/
- group: build
  title: ''
  type: IntegrationsApplication
  url: https://splunkbase.splunk.com/app/2757
- group: company
  title: ''
  type: Partner
  url: https://www.paloaltonetworks.com/partners
- group: design
  href: https://artifacts.apis.io/palo-alto-networks/rules/palo-alto-networks-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/palo-alto-networks-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/palo-alto-networks/vocabulary/palo-alto-networks-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/palo-alto-networks-vocabulary.yaml
- group: design
  href: https://artifacts.apis.io/palo-alto-networks/json-ld/palo-alto-networks-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/palo-alto-networks-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/PaloAltoNetworks/pan-mcp-relay
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/PaloAltoNetworks/openapi/blob/659339799ae30a06c3bf1859507a4a6c131814fc/.spectral.yaml
created: '2024-01-01'
description: Palo Alto Networks is a global cybersecurity leader providing advanced security platforms and services across network security, cloud security, and security operations. Its developer platform at pan.dev offers REST and XML APIs for PAN-OS firewalls, Strata Cloud Manager, Prisma Cloud (CSPM, CWPP, code security), Prisma Access and SD-WAN for SASE, Cortex XDR/XSOAR/XSIAM for security operations, and cloud-delivered security services including WildFire, Threat Vault, IoT Security, and DLP.
examples:
- key_count: 10
  name: Aiops Ngfw Bpa Api Bpa Check Example
  slug: aiops-ngfw-bpa-api-bpa-check-example
- key_count: 10
  name: Aiops Ngfw Bpa Api Bpa Report Example
  slug: aiops-ngfw-bpa-api-bpa-report-example
- key_count: 3
  name: Aiops Ngfw Bpa Api Bpa Request Example
  slug: aiops-ngfw-bpa-api-bpa-request-example
- key_count: 7
  name: Aiops Ngfw Bpa Api Bpa Request Status Example
  slug: aiops-ngfw-bpa-api-bpa-request-status-example
- key_count: 11
  name: Autonomous Dem Api Agent Score Example
  slug: autonomous-dem-api-agent-score-example
- key_count: 13
  name: Autonomous Dem Api Application Score Example
  slug: autonomous-dem-api-application-score-example
- key_count: 9
  name: Autonomous Dem Api Monitored Agent Example
  slug: autonomous-dem-api-monitored-agent-example
- key_count: 8
  name: Autonomous Dem Api Monitored Application Example
  slug: autonomous-dem-api-monitored-application-example
- key_count: 9
  name: Autonomous Dem Api Performance Metric Example
  slug: autonomous-dem-api-performance-metric-example
- key_count: 11
  name: Autonomous Dem Api Test Result Example
  slug: autonomous-dem-api-test-result-example
- key_count: 3
  name: Cloud Identity Engine Api Attr_Based_Filter Example
  slug: cloud-identity-engine-api-attr_based_filter-example
- key_count: 1
  name: Cloud Identity Engine Api Check_Group_Membership Example
  slug: cloud-identity-engine-api-check_group_membership-example
- key_count: 2
  name: Cloud Identity Engine Api Check_User_In_Particular_Group Example
  slug: cloud-identity-engine-api-check_user_in_particular_group-example
- key_count: 1
  name: Cloud Identity Engine Api Domain_Param Example
  slug: cloud-identity-engine-api-domain_param-example
- key_count: 2
  name: Cloud Identity Engine Api Fetch_All_Users_Attrs Example
  slug: cloud-identity-engine-api-fetch_all_users_attrs-example
- key_count: 3
  name: Cloud Identity Engine Api Group_Filter Example
  slug: cloud-identity-engine-api-group_filter-example
- key_count: 2
  name: Cloud Identity Engine Api List_All_Groups_In_Domain Example
  slug: cloud-identity-engine-api-list_all_groups_in_domain-example
- key_count: 2
  name: Cloud Identity Engine Api List_All_Users_In_Domain Example
  slug: cloud-identity-engine-api-list_all_users_in_domain-example
- key_count: 1
  name: Cloud Identity Engine Api List_Groups_User_Belongs_To Example
  slug: cloud-identity-engine-api-list_groups_user_belongs_to-example
- key_count: 2
  name: Cloud Identity Engine Api List_Specific_Groups Example
  slug: cloud-identity-engine-api-list_specific_groups-example
- key_count: 1
  name: Cloud Identity Engine Api List_Specific_Users Example
  slug: cloud-identity-engine-api-list_specific_users-example
- key_count: 2
  name: Cloud Identity Engine Api List_Users_In_Particular_Group Example
  slug: cloud-identity-engine-api-list_users_in_particular_group-example
- key_count: 2
  name: Cloud Identity Engine Api Pagination_Params Example
  slug: cloud-identity-engine-api-pagination_params-example
- key_count: 3
  name: Cloud Ngfw Api Firewall Example
  slug: cloud-ngfw-api-firewall-example
- key_count: 2
  name: Cloud Ngfw Api Firewall Request Example
  slug: cloud-ngfw-api-firewall-request-example
- key_count: 4
  name: Cloud Ngfw Api Firewall Summary Example
  slug: cloud-ngfw-api-firewall-summary-example
- key_count: 3
  name: Cloud Ngfw Api Fqdn List Example
  slug: cloud-ngfw-api-fqdn-list-example
- key_count: 2
  name: Cloud Ngfw Api Fqdn List Request Example
  slug: cloud-ngfw-api-fqdn-list-request-example
- key_count: 1
  name: Cloud Ngfw Api Fqdn List Summary Example
  slug: cloud-ngfw-api-fqdn-list-summary-example
- key_count: 3
  name: Cloud Ngfw Api Prefix List Example
  slug: cloud-ngfw-api-prefix-list-example
- key_count: 2
  name: Cloud Ngfw Api Prefix List Request Example
  slug: cloud-ngfw-api-prefix-list-request-example
- key_count: 1
  name: Cloud Ngfw Api Prefix List Summary Example
  slug: cloud-ngfw-api-prefix-list-summary-example
- key_count: 2
  name: Cloud Ngfw Api Response Status Example
  slug: cloud-ngfw-api-response-status-example
- key_count: 5
  name: Cloud Ngfw Api Rule Destination Example
  slug: cloud-ngfw-api-rule-destination-example
- key_count: 4
  name: Cloud Ngfw Api Rule Source Example
  slug: cloud-ngfw-api-rule-source-example
- key_count: 3
  name: Cloud Ngfw Api Rule Stack Example
  slug: cloud-ngfw-api-rule-stack-example
- key_count: 2
  name: Cloud Ngfw Api Rule Stack Request Example
  slug: cloud-ngfw-api-rule-stack-request-example
- key_count: 3
  name: Cloud Ngfw Api Rule Stack Summary Example
  slug: cloud-ngfw-api-rule-stack-summary-example
- key_count: 2
  name: Cloud Ngfw Api Security Rule Example
  slug: cloud-ngfw-api-security-rule-example
- key_count: 2
  name: Cloud Ngfw Api Security Rule Request Example
  slug: cloud-ngfw-api-security-rule-request-example
- key_count: 3
  name: Cloud Ngfw Api Security Rule Summary Example
  slug: cloud-ngfw-api-security-rule-summary-example
- key_count: 17
  name: Cortex Xdr Api Alert Example
  slug: cortex-xdr-api-alert-example
- key_count: 9
  name: Cortex Xdr Api Audit Log Example
  slug: cortex-xdr-api-audit-log-example
- key_count: 20
  name: Cortex Xdr Api Endpoint Example
  slug: cortex-xdr-api-endpoint-example
- key_count: 3
  name: Cortex Xdr Api Filter Example
  slug: cortex-xdr-api-filter-example
- key_count: 0
  name: Cortex Xdr Api Incident Detail Example
  slug: cortex-xdr-api-incident-detail-example
- key_count: 21
  name: Cortex Xdr Api Incident Example
  slug: cortex-xdr-api-incident-example
- key_count: 2
  name: Cortex Xdr Api Sort Order Example
  slug: cortex-xdr-api-sort-order-example
- key_count: 21
  name: Cortex Xdr Incident Example
  slug: cortex-xdr-incident-example
- key_count: 10
  name: Cortex Xdr Webhooks Alert Payload Example
  slug: cortex-xdr-webhooks-alert-payload-example
- key_count: 10
  name: Cortex Xdr Webhooks Incident Payload Example
  slug: cortex-xdr-webhooks-incident-payload-example
- key_count: 14
  name: Cortex Xpanse Api Asm Incident Example
  slug: cortex-xpanse-api-asm-incident-example
- key_count: 0
  name: Cortex Xpanse Api Asset Internet Exposure Detail Example
  slug: cortex-xpanse-api-asset-internet-exposure-detail-example
- key_count: 13
  name: Cortex Xpanse Api Asset Internet Exposure Example
  slug: cortex-xpanse-api-asset-internet-exposure-example
- key_count: 10
  name: Cortex Xpanse Api Attack Surface Rule Example
  slug: cortex-xpanse-api-attack-surface-rule-example
- key_count: 9
  name: Cortex Xpanse Api Audit Log Example
  slug: cortex-xpanse-api-audit-log-example
- key_count: 13
  name: Cortex Xpanse Api Exposed Service Example
  slug: cortex-xpanse-api-exposed-service-example
- key_count: 3
  name: Cortex Xpanse Api Filter Example
  slug: cortex-xpanse-api-filter-example
- key_count: 10
  name: Cortex Xpanse Api Owned Ip Range Example
  slug: cortex-xpanse-api-owned-ip-range-example
- key_count: 2
  name: Cortex Xpanse Api Sort Order Example
  slug: cortex-xpanse-api-sort-order-example
- key_count: 12
  name: Cortex Xsiam Api Alert Example
  slug: cortex-xsiam-api-alert-example
- key_count: 10
  name: Cortex Xsiam Api Asset Example
  slug: cortex-xsiam-api-asset-example
- key_count: 9
  name: Cortex Xsiam Api Audit Log Example
  slug: cortex-xsiam-api-audit-log-example
- key_count: 14
  name: Cortex Xsiam Api Endpoint Example
  slug: cortex-xsiam-api-endpoint-example
- key_count: 3
  name: Cortex Xsiam Api Filter Example
  slug: cortex-xsiam-api-filter-example
- key_count: 15
  name: Cortex Xsiam Api Incident Example
  slug: cortex-xsiam-api-incident-example
- key_count: 2
  name: Cortex Xsiam Api Sort Order Example
  slug: cortex-xsiam-api-sort-order-example
- key_count: 8
  name: Cortex Xsiam Data Ingestion Event Data Payload Example
  slug: cortex-xsiam-data-ingestion-event-data-payload-example
- key_count: 8
  name: Cortex Xsiam Data Ingestion Log Data Payload Example
  slug: cortex-xsiam-data-ingestion-log-data-payload-example
- key_count: 8
  name: Cortex Xsiam Data Ingestion Xdr Data Payload Example
  slug: cortex-xsiam-data-ingestion-xdr-data-payload-example
- key_count: 4
  name: Cortex Xsoar Api Create Entry Request Example
  slug: cortex-xsoar-api-create-entry-request-example
- key_count: 10
  name: Cortex Xsoar Api Create Incident Request Example
  slug: cortex-xsoar-api-create-incident-request-example
- key_count: 9
  name: Cortex Xsoar Api Entry Example
  slug: cortex-xsoar-api-entry-example
- key_count: 20
  name: Cortex Xsoar Api Incident Example
  slug: cortex-xsoar-api-incident-example
- key_count: 5
  name: Cortex Xsoar Api Incident Search Request Example
  slug: cortex-xsoar-api-incident-search-request-example
- key_count: 3
  name: Cortex Xsoar Api Incident Search Response Example
  slug: cortex-xsoar-api-incident-search-response-example
- key_count: 9
  name: Cortex Xsoar Api Integration Example
  slug: cortex-xsoar-api-integration-example
- key_count: 8
  name: Cortex Xsoar Api Integration Instance Example
  slug: cortex-xsoar-api-integration-instance-example
- key_count: 9
  name: Cortex Xsoar Api Investigation Example
  slug: cortex-xsoar-api-investigation-example
- key_count: 8
  name: Cortex Xsoar Api Playbook Example
  slug: cortex-xsoar-api-playbook-example
- key_count: 9
  name: Cortex Xsoar Api Update Incident Request Example
  slug: cortex-xsoar-api-update-incident-request-example
- key_count: 11
  name: Cortex Xsoar Integration Manifest Example
  slug: cortex-xsoar-integration-manifest-example
- key_count: 5
  name: Dlp Api Content Snippet Example
  slug: dlp-api-content-snippet-example
- key_count: 9
  name: Dlp Api Data Pattern Example
  slug: dlp-api-data-pattern-example
- key_count: 18
  name: Dlp Api Dlp Incident Example
  slug: dlp-api-dlp-incident-example
- key_count: 8
  name: Dlp Api Incident Summary Example
  slug: dlp-api-incident-summary-example
- key_count: 10
  name: Dns Security Api Domain Detail Example
  slug: dns-security-api-domain-detail-example
- key_count: 8
  name: Dns Security Api Network Stats Example
  slug: dns-security-api-network-stats-example
- key_count: 6
  name: Email Dlp Api Email Attachment Example
  slug: email-dlp-api-email-attachment-example
- key_count: 15
  name: Email Dlp Api Email Dlp Incident Example
  slug: email-dlp-api-email-dlp-incident-example
- key_count: 3
  name: Email Dlp Api Email Recipient Example
  slug: email-dlp-api-email-recipient-example
- key_count: 8
  name: Identity Security Posture Management Api Create Ticket Request Example
  slug: identity-security-posture-management-api-create-ticket-request-example
- key_count: 3
  name: Identity Security Posture Management Api Download Csv Request Example
  slug: identity-security-posture-management-api-download-csv-request-example
- key_count: 2
  name: Identity Security Posture Management Api Feature State Example
  slug: identity-security-posture-management-api-feature-state-example
- key_count: 3
  name: Identity Security Posture Management Api Idp Info Example
  slug: identity-security-posture-management-api-idp-info-example
- key_count: 2
  name: Identity Security Posture Management Api List Response Idp Info Example
  slug: identity-security-posture-management-api-list-response-idp-info-example
- key_count: 2
  name: Identity Security Posture Management Api List Response Map String Object Example
  slug: identity-security-posture-management-api-list-response-map-string-object-example
- key_count: 2
  name: Identity Security Posture Management Api List Response Mfa Activity Example
  slug: identity-security-posture-management-api-list-response-mfa-activity-example
- key_count: 2
  name: Identity Security Posture Management Api List Response Saa S Account Example
  slug: identity-security-posture-management-api-list-response-saa-s-account-example
- key_count: 2
  name: Identity Security Posture Management Api List Response Saa S Activity Example
  slug: identity-security-posture-management-api-list-response-saa-s-activity-example
- key_count: 2
  name: Identity Security Posture Management Api List Response Saa S Instance Info Example
  slug: identity-security-posture-management-api-list-response-saa-s-instance-info-example
- key_count: 2
  name: Identity Security Posture Management Api List Response Ticket Example
  slug: identity-security-posture-management-api-list-response-ticket-example
- key_count: 3
  name: Identity Security Posture Management Api Mfa Activity Count By App Type Example
  slug: identity-security-posture-management-api-mfa-activity-count-by-app-type-example
- key_count: 18
  name: Identity Security Posture Management Api Mfa Activity Example
  slug: identity-security-posture-management-api-mfa-activity-example
- key_count: 1
  name: Identity Security Posture Management Api Remediation Request Example
  slug: identity-security-posture-management-api-remediation-request-example
- key_count: 28
  name: Identity Security Posture Management Api Saa S Account Example
  slug: identity-security-posture-management-api-saa-s-account-example
- key_count: 15
  name: Identity Security Posture Management Api Saa S Activity Example
  slug: identity-security-posture-management-api-saa-s-activity-example
- key_count: 3
  name: Identity Security Posture Management Api Saa S Instance Info Example
  slug: identity-security-posture-management-api-saa-s-instance-info-example
- key_count: 12
  name: Identity Security Posture Management Api Ticket Example
  slug: identity-security-posture-management-api-ticket-example
- key_count: 3
  name: Identity Security Posture Management Api Unlink Ticket Request Example
  slug: identity-security-posture-management-api-unlink-ticket-request-example
- key_count: 11
  name: Iot Security Api Alert Example
  slug: iot-security-api-alert-example
- key_count: 7
  name: Iot Security Api Asset Report Example
  slug: iot-security-api-asset-report-example
- key_count: 18
  name: Iot Security Api Device Example
  slug: iot-security-api-device-example
- key_count: 5
  name: Iot Security Api Device Tag Example
  slug: iot-security-api-device-tag-example
- key_count: 10
  name: Iot Security Api Policy Recommendation Example
  slug: iot-security-api-policy-recommendation-example
- key_count: 10
  name: Iot Security Api Vulnerability Example
  slug: iot-security-api-vulnerability-example
- key_count: 3
  name: Palo Alto Security Advisory Example
  slug: palo-alto-security-advisory-example
- key_count: 7
  name: Pan Os Rest Api Address Example
  slug: pan-os-rest-api-address-example
- key_count: 5
  name: Pan Os Rest Api Address Group Example
  slug: pan-os-rest-api-address-group-example
- key_count: 3
  name: Pan Os Rest Api Commit Status Example
  slug: pan-os-rest-api-commit-status-example
- key_count: 12
  name: Pan Os Rest Api Nat Rule Example
  slug: pan-os-rest-api-nat-rule-example
- key_count: 3
  name: Pan Os Rest Api Pan Os Response Example
  slug: pan-os-rest-api-pan-os-response-example
- key_count: 11
  name: Pan Os Rest Api Qos Rule Example
  slug: pan-os-rest-api-qos-rule-example
- key_count: 17
  name: Pan Os Rest Api Security Rule Example
  slug: pan-os-rest-api-security-rule-example
- key_count: 4
  name: Pan Os Rest Api Service Example
  slug: pan-os-rest-api-service-example
- key_count: 3
  name: Pan Os Rest Api Service Group Example
  slug: pan-os-rest-api-service-group-example
- key_count: 3
  name: Pan Os Rest Api Tag Example
  slug: pan-os-rest-api-tag-example
- key_count: 3
  name: Pan Os Rest Api Virtual System Example
  slug: pan-os-rest-api-virtual-system-example
- key_count: 20
  name: Pan Os Security Rule Example
  slug: pan-os-security-rule-example
- key_count: 8
  name: Prisma Access Api Ike Gateway Example
  slug: prisma-access-api-ike-gateway-example
- key_count: 6
  name: Prisma Access Api Ip Sec Tunnel Example
  slug: prisma-access-api-ip-sec-tunnel-example
- key_count: 8
  name: Prisma Access Api Job Status Example
  slug: prisma-access-api-job-status-example
- key_count: 6
  name: Prisma Access Api Mobile Agent Infrastructure Settings Example
  slug: prisma-access-api-mobile-agent-infrastructure-settings-example
- key_count: 8
  name: Prisma Access Api Remote Network Example
  slug: prisma-access-api-remote-network-example
- key_count: 18
  name: Prisma Access Api Security Rule Example
  slug: prisma-access-api-security-rule-example
- key_count: 8
  name: Prisma Access Api Service Connection Example
  slug: prisma-access-api-service-connection-example
- key_count: 8
  name: Prisma Access Browser Api Browser Deployment Example
  slug: prisma-access-browser-api-browser-deployment-example
- key_count: 5
  name: Prisma Access Browser Api Browser Deployment Request Example
  slug: prisma-access-browser-api-browser-deployment-request-example
- key_count: 10
  name: Prisma Access Browser Api Browser Policy Example
  slug: prisma-access-browser-api-browser-policy-example
- key_count: 7
  name: Prisma Access Browser Api Browser Policy Request Example
  slug: prisma-access-browser-api-browser-policy-request-example
- key_count: 9
  name: Prisma Access Browser Api Browser Session Example
  slug: prisma-access-browser-api-browser-session-example
- key_count: 6
  name: Prisma Access Browser Api Browser User Example
  slug: prisma-access-browser-api-browser-user-example
- key_count: 7
  name: Prisma Access Browser Api Managed Device Example
  slug: prisma-access-browser-api-managed-device-example
- key_count: 7
  name: Prisma Access Browser Api Usage Report Example
  slug: prisma-access-browser-api-usage-report-example
- key_count: 2
  name: Prisma Access Insights Api Custom Query Example
  slug: prisma-access-insights-api-custom-query-example
- key_count: 5
  name: Prisma Access Insights Api Data Resource Query Example
  slug: prisma-access-insights-api-data-resource-query-example
- key_count: 4
  name: Prisma Access Insights Api Data Resource Response Example
  slug: prisma-access-insights-api-data-resource-response-example
- key_count: 3
  name: Prisma Access Insights Api Export Job Response Example
  slug: prisma-access-insights-api-export-job-response-example
- key_count: 5
  name: Prisma Access Insights Api Export Job Status Example
  slug: prisma-access-insights-api-export-job-status-example
- key_count: 2
  name: Prisma Access Insights Api Query Filter Example
  slug: prisma-access-insights-api-query-filter-example
- key_count: 3
  name: Prisma Access Insights Api Time Range Example
  slug: prisma-access-insights-api-time-range-example
- key_count: 6
  name: Prisma Airs Ai Red Teaming Api Attack Category Example
  slug: prisma-airs-ai-red-teaming-api-attack-category-example
- key_count: 12
  name: Prisma Airs Ai Red Teaming Api Scan Example
  slug: prisma-airs-ai-red-teaming-api-scan-example
- key_count: 9
  name: Prisma Airs Ai Red Teaming Api Scan Report Example
  slug: prisma-airs-ai-red-teaming-api-scan-report-example
- key_count: 4
  name: Prisma Airs Ai Red Teaming Api Scan Request Example
  slug: prisma-airs-ai-red-teaming-api-scan-request-example
- key_count: 8
  name: Prisma Airs Ai Red Teaming Api Scan Target Example
  slug: prisma-airs-ai-red-teaming-api-scan-target-example
- key_count: 7
  name: Prisma Airs Ai Red Teaming Api Scan Target Request Example
  slug: prisma-airs-ai-red-teaming-api-scan-target-request-example
- key_count: 9
  name: Prisma Airs Ai Red Teaming Api Vulnerability Finding Example
  slug: prisma-airs-ai-red-teaming-api-vulnerability-finding-example
- key_count: 6
  name: Prisma Airs Api Ai Profile Example
  slug: prisma-airs-api-ai-profile-example
- key_count: 4
  name: Prisma Airs Api Content Scan Result Example
  slug: prisma-airs-api-content-scan-result-example
- key_count: 2
  name: Prisma Airs Api Scan Content Example
  slug: prisma-airs-api-scan-content-example
- key_count: 3
  name: Prisma Airs Api Scan Request Example
  slug: prisma-airs-api-scan-request-example
- key_count: 8
  name: Prisma Airs Api Scan Response Example
  slug: prisma-airs-api-scan-response-example
- key_count: 15
  name: Prisma Cloud Code Security Api Code Error Example
  slug: prisma-cloud-code-security-api-code-error-example
- key_count: 12
  name: Prisma Cloud Code Security Api Fix Example
  slug: prisma-cloud-code-security-api-fix-example
- key_count: 12
  name: Prisma Cloud Code Security Api Repository Example
  slug: prisma-cloud-code-security-api-repository-example
- key_count: 6
  name: Prisma Cloud Code Security Api Scan Integration Example
  slug: prisma-cloud-code-security-api-scan-integration-example
- key_count: 8
  name: Prisma Cloud Code Security Api Scan Status Example
  slug: prisma-cloud-code-security-api-scan-status-example
- key_count: 9
  name: Prisma Cloud Code Security Api Suppression Example
  slug: prisma-cloud-code-security-api-suppression-example
- key_count: 5
  name: Prisma Cloud Compute Api Ci Scan Example
  slug: prisma-cloud-compute-api-ci-scan-example
- key_count: 5
  name: Prisma Cloud Compute Api Compliance Issue Example
  slug: prisma-cloud-compute-api-compliance-issue-example
- key_count: 1
  name: Prisma Cloud Compute Api Compliance Policy Example
  slug: prisma-cloud-compute-api-compliance-policy-example
- key_count: 11
  name: Prisma Cloud Compute Api Container Example
  slug: prisma-cloud-compute-api-container-example
- key_count: 8
  name: Prisma Cloud Compute Api Defender Example
  slug: prisma-cloud-compute-api-defender-example
- key_count: 5
  name: Prisma Cloud Compute Api Defender Summary Example
  slug: prisma-cloud-compute-api-defender-summary-example
- key_count: 12
  name: Prisma Cloud Compute Api Host Example
  slug: prisma-cloud-compute-api-host-example
- key_count: 13
  name: Prisma Cloud Compute Api Image Example
  slug: prisma-cloud-compute-api-image-example
- key_count: 8
  name: Prisma Cloud Compute Api Registry Config Example
  slug: prisma-cloud-compute-api-registry-config-example
- key_count: 1
  name: Prisma Cloud Compute Api Runtime Policy Example
  slug: prisma-cloud-compute-api-runtime-policy-example
- key_count: 10
  name: Prisma Cloud Compute Api Vulnerability Example
  slug: prisma-cloud-compute-api-vulnerability-example
- key_count: 1
  name: Prisma Cloud Compute Api Vulnerability Policy Example
  slug: prisma-cloud-compute-api-vulnerability-policy-example
- key_count: 9
  name: Prisma Cloud Cspm Api Alert Example
  slug: prisma-cloud-cspm-api-alert-example
- key_count: 3
  name: Prisma Cloud Cspm Api Alert Filter Example
  slug: prisma-cloud-cspm-api-alert-filter-example
- key_count: 6
  name: Prisma Cloud Cspm Api Cloud Account Example
  slug: prisma-cloud-cspm-api-cloud-account-example
- key_count: 8
  name: Prisma Cloud Cspm Api Compliance Standard Example
  slug: prisma-cloud-cspm-api-compliance-standard-example
- key_count: 11
  name: Prisma Cloud Cspm Api Policy Example
  slug: prisma-cloud-cspm-api-policy-example
- key_count: 8
  name: Prisma Cloud Cspm Api Policy Input Example
  slug: prisma-cloud-cspm-api-policy-input-example
- key_count: 7
  name: Prisma Cloud Cspm Api Report Example
  slug: prisma-cloud-cspm-api-report-example
- key_count: 3
  name: Prisma Cloud Cspm Api Search Result Example
  slug: prisma-cloud-cspm-api-search-result-example
- key_count: 2
  name: Prisma Cloud Cspm Api Time Range Example
  slug: prisma-cloud-cspm-api-time-range-example
- key_count: 9
  name: Prisma Cloud Dspm Api Classification Example
  slug: prisma-cloud-dspm-api-classification-example
- key_count: 12
  name: Prisma Cloud Dspm Api Data Asset Example
  slug: prisma-cloud-dspm-api-data-asset-example
- key_count: 16
  name: Prisma Cloud Dspm Api Data Risk Example
  slug: prisma-cloud-dspm-api-data-risk-example
- key_count: 14
  name: Prisma Cloud Dspm Api Data Security Alert Example
  slug: prisma-cloud-dspm-api-data-security-alert-example
- key_count: 15
  name: Prisma Cloud Dspm Api Data Store Example
  slug: prisma-cloud-dspm-api-data-store-example
- key_count: 10
  name: Prisma Cloud Dspm Api Dspm Policy Example
  slug: prisma-cloud-dspm-api-dspm-policy-example
- key_count: 1
  name: Prisma Cloud Mssp Api Change Password Request Example
  slug: prisma-cloud-mssp-api-change-password-request-example
- key_count: 3
  name: Prisma Cloud Mssp Api Contact Info Example
  slug: prisma-cloud-mssp-api-contact-info-example
- key_count: 8
  name: Prisma Cloud Mssp Api Create Managed Tenant Request Example
  slug: prisma-cloud-mssp-api-create-managed-tenant-request-example
- key_count: 4
  name: Prisma Cloud Mssp Api Create Mssp Request Example
  slug: prisma-cloud-mssp-api-create-mssp-request-example
- key_count: 3
  name: Prisma Cloud Mssp Api Create Policy Group Response Example
  slug: prisma-cloud-mssp-api-create-policy-group-response-example
- key_count: 2
  name: Prisma Cloud Mssp Api Create Tenant Group Request Example
  slug: prisma-cloud-mssp-api-create-tenant-group-request-example
- key_count: 2
  name: Prisma Cloud Mssp Api Form Login Request Example
  slug: prisma-cloud-mssp-api-form-login-request-example
- key_count: 3
  name: Prisma Cloud Mssp Api Form Login Response Example
  slug: prisma-cloud-mssp-api-form-login-response-example
- key_count: 6
  name: Prisma Cloud Mssp Api Jwk Response Example
  slug: prisma-cloud-mssp-api-jwk-response-example
- key_count: 1
  name: Prisma Cloud Mssp Api Jwks Response Example
  slug: prisma-cloud-mssp-api-jwks-response-example
- key_count: 2
  name: Prisma Cloud Mssp Api License Info Example
  slug: prisma-cloud-mssp-api-license-info-example
- key_count: 9
  name: Prisma Cloud Mssp Api License Pool Info Example
  slug: prisma-cloud-mssp-api-license-pool-info-example
- key_count: 20
  name: Prisma Cloud Mssp Api Managed Tenant Detailed Response Example
  slug: prisma-cloud-mssp-api-managed-tenant-detailed-response-example
- key_count: 6
  name: Prisma Cloud Mssp Api Managed Tenant License Response Example
  slug: prisma-cloud-mssp-api-managed-tenant-license-response-example
- key_count: 19
  name: Prisma Cloud Mssp Api Managed Tenant Response Example
  slug: prisma-cloud-mssp-api-managed-tenant-response-example
- key_count: 2
  name: Prisma Cloud Mssp Api Managed Tenants Response Example
  slug: prisma-cloud-mssp-api-managed-tenants-response-example
- key_count: 5
  name: Prisma Cloud Mssp Api Module Info Example
  slug: prisma-cloud-mssp-api-module-info-example
- key_count: 3
  name: Prisma Cloud Mssp Api Module Info Request Example
  slug: prisma-cloud-mssp-api-module-info-request-example
- key_count: 7
  name: Prisma Cloud Mssp Api Mssp License Info Response Example
  slug: prisma-cloud-mssp-api-mssp-license-info-response-example
- key_count: 5
  name: Prisma Cloud Mssp Api Mssp License Pool Request Example
  slug: prisma-cloud-mssp-api-mssp-license-pool-request-example
- key_count: 9
  name: Prisma Cloud Mssp Api Mssp License Pool Response Example
  slug: prisma-cloud-mssp-api-mssp-license-pool-response-example
- key_count: 2
  name: Prisma Cloud Mssp Api Mssp License Pools Response Example
  slug: prisma-cloud-mssp-api-mssp-license-pools-response-example
- key_count: 4
  name: Prisma Cloud Mssp Api Mssp License Usage Request Object Example
  slug: prisma-cloud-mssp-api-mssp-license-usage-request-object-example
- key_count: 2
  name: Prisma Cloud Mssp Api Mssp License Usage Response Example
  slug: prisma-cloud-mssp-api-mssp-license-usage-response-example
- key_count: 2
  name: Prisma Cloud Mssp Api Mssp List User Response Example
  slug: prisma-cloud-mssp-api-mssp-list-user-response-example
- key_count: 6
  name: Prisma Cloud Mssp Api Mssp Response Example
  slug: prisma-cloud-mssp-api-mssp-response-example
- key_count: 3
  name: Prisma Cloud Mssp Api Mssp User Request Example
  slug: prisma-cloud-mssp-api-mssp-user-request-example
- key_count: 5
  name: Prisma Cloud Mssp Api Mssp User Response Example
  slug: prisma-cloud-mssp-api-mssp-user-response-example
- key_count: 3
  name: Prisma Cloud Mssp Api Operation Ack Request Example
  slug: prisma-cloud-mssp-api-operation-ack-request-example
- key_count: 13
  name: Prisma Cloud Mssp Api Operation Response Example
  slug: prisma-cloud-mssp-api-operation-response-example
- key_count: 2
  name: Prisma Cloud Mssp Api Operations Response Example
  slug: prisma-cloud-mssp-api-operations-response-example
- key_count: 3
  name: Prisma Cloud Mssp Api Policy Group Info Example
  slug: prisma-cloud-mssp-api-policy-group-info-example
- key_count: 4
  name: Prisma Cloud Mssp Api Policy Group List Response Example
  slug: prisma-cloud-mssp-api-policy-group-list-response-example
- key_count: 2
  name: Prisma Cloud Mssp Api Policy Group Request Example
  slug: prisma-cloud-mssp-api-policy-group-request-example
- key_count: 4
  name: Prisma Cloud Mssp Api Policy Group Response Example
  slug: prisma-cloud-mssp-api-policy-group-response-example
- key_count: 2
  name: Prisma Cloud Mssp Api Policy Groups List Response Example
  slug: prisma-cloud-mssp-api-policy-groups-list-response-example
- key_count: 2
  name: Prisma Cloud Mssp Api Recur String Example
  slug: prisma-cloud-mssp-api-recur-string-example
- key_count: 2
  name: Prisma Cloud Mssp Api Relative Time Duration Example
  slug: prisma-cloud-mssp-api-relative-time-duration-example
- key_count: 0
  name: Prisma Cloud Mssp Api Relative Time Range Config Example
  slug: prisma-cloud-mssp-api-relative-time-range-config-example
- key_count: 2
  name: Prisma Cloud Mssp Api Schedule Task Request Example
  slug: prisma-cloud-mssp-api-schedule-task-request-example
- key_count: 2
  name: Prisma Cloud Mssp Api Seamless Login Response Example
  slug: prisma-cloud-mssp-api-seamless-login-response-example
- key_count: 2
  name: Prisma Cloud Mssp Api Stack Mapping Plan Types List Response Example
  slug: prisma-cloud-mssp-api-stack-mapping-plan-types-list-response-example
- key_count: 3
  name: Prisma Cloud Mssp Api Stack Mapping Response Example
  slug: prisma-cloud-mssp-api-stack-mapping-response-example
- key_count: 9
  name: Prisma Cloud Mssp Api Task Example
  slug: prisma-cloud-mssp-api-task-example
- key_count: 5
  name: Prisma Cloud Mssp Api Tenant Change Response Example
  slug: prisma-cloud-mssp-api-tenant-change-response-example
- key_count: 4
  name: Prisma Cloud Mssp Api Tenant Group License Info Example
  slug: prisma-cloud-mssp-api-tenant-group-license-info-example
- key_count: 4
  name: Prisma Cloud Mssp Api Tenant Group Mapping Details Example
  slug: prisma-cloud-mssp-api-tenant-group-mapping-details-example
- key_count: 1
  name: Prisma Cloud Mssp Api Tenant Group Policy Group Map Request Example
  slug: prisma-cloud-mssp-api-tenant-group-policy-group-map-request-example
- key_count: 2
  name: Prisma Cloud Mssp Api Tenant Group Policy Group Mapping Example
  slug: prisma-cloud-mssp-api-tenant-group-policy-group-mapping-example
- key_count: 3
  name: Prisma Cloud Mssp Api Tenant Group Policy Group Mapping Response Example
  slug: prisma-cloud-mssp-api-tenant-group-policy-group-mapping-response-example
- key_count: 1
  name: Prisma Cloud Mssp Api Tenant Group Policy Group Mappings Response Example
  slug: prisma-cloud-mssp-api-tenant-group-policy-group-mappings-response-example
- key_count: 5
  name: Prisma Cloud Mssp Api Tenant Group Response Example
  slug: prisma-cloud-mssp-api-tenant-group-response-example
- key_count: 2
  name: Prisma Cloud Mssp Api Tenant Groups Response Example
  slug: prisma-cloud-mssp-api-tenant-groups-response-example
- key_count: 2
  name: Prisma Cloud Mssp Api Tenant Ids Example
  slug: prisma-cloud-mssp-api-tenant-ids-example
- key_count: 9
  name: Prisma Cloud Mssp Api Tenant License Usage Example
  slug: prisma-cloud-mssp-api-tenant-license-usage-example
- key_count: 4
  name: Prisma Cloud Mssp Api Tenant Update Example
  slug: prisma-cloud-mssp-api-tenant-update-example
- key_count: 3
  name: Prisma Cloud Mssp Api Time Range Config Object Example
  slug: prisma-cloud-mssp-api-time-range-config-object-example
- key_count: 0
  name: Prisma Cloud Mssp Api To Now Time Range Config Example
  slug: prisma-cloud-mssp-api-to-now-time-range-config-example
- key_count: 1
  name: Prisma Cloud Mssp Api Token Refresh Response Example
  slug: prisma-cloud-mssp-api-token-refresh-response-example
- key_count: 4
  name: Prisma Cloud Mssp Api Update Managed Tenant Request Example
  slug: prisma-cloud-mssp-api-update-managed-tenant-request-example
- key_count: 2
  name: Prisma Cloud Mssp Api Update Mssp Request Example
  slug: prisma-cloud-mssp-api-update-mssp-request-example
- key_count: 2
  name: Prisma Cloud Mssp Api Update Tenant Group Request Example
  slug: prisma-cloud-mssp-api-update-tenant-group-request-example
- key_count: 0
  name: Prisma Cloud Mssp Api V1 Response Example
  slug: prisma-cloud-mssp-api-v1-response-example
- key_count: 1
  name: Prisma Cloud Mssp Api Validate Token Request Example
  slug: prisma-cloud-mssp-api-validate-token-request-example
- key_count: 1
  name: Prisma Cloud Mssp Api Validate Token Response Example
  slug: prisma-cloud-mssp-api-validate-token-response-example
- key_count: 18
  name: Prisma Cloud Policy Example
  slug: prisma-cloud-policy-example
- key_count: 11
  name: Prisma Cloud Webhooks Alert Payload Example
  slug: prisma-cloud-webhooks-alert-payload-example
- key_count: 12
  name: Prisma Sd Wan Api Alarm Example
  slug: prisma-sd-wan-api-alarm-example
- key_count: 7
  name: Prisma Sd Wan Api Application Usage Example
  slug: prisma-sd-wan-api-application-usage-example
- key_count: 9
  name: Prisma Sd Wan Api Lan Network Example
  slug: prisma-sd-wan-api-lan-network-example
- key_count: 10
  name: Prisma Sd Wan Api Path Rule Example
  slug: prisma-sd-wan-api-path-rule-example
- key_count: 11
  name: Prisma Sd Wan Api Qo S Rule Example
  slug: prisma-sd-wan-api-qo-s-rule-example
- key_count: 10
  name: Prisma Sd Wan Api Site Example
  slug: prisma-sd-wan-api-site-example
- key_count: 7
  name: Prisma Sd Wan Api Site Metric Example
  slug: prisma-sd-wan-api-site-metric-example
- key_count: 12
  name: Prisma Sd Wan Api Wan Interface Example
  slug: prisma-sd-wan-api-wan-interface-example
- key_count: 7
  name: Saas Security Api Application Example
  slug: saas-security-api-application-example
- key_count: 12
  name: Saas Security Api Asset Example
  slug: saas-security-api-asset-example
- key_count: 13
  name: Saas Security Api Incident Example
  slug: saas-security-api-incident-example
- key_count: 2
  name: Saas Security Api Log Forwarding Settings Example
  slug: saas-security-api-log-forwarding-settings-example
- key_count: 8
  name: Saas Security Api User Activity Example
  slug: saas-security-api-user-activity-example
- key_count: 6
  name: Saas Security Api User Example
  slug: saas-security-api-user-example
- key_count: 10
  name: Sase 5G Api Network Slice Example
  slug: sase-5g-api-network-slice-example
- key_count: 5
  name: Sase 5G Api Network Slice Request Example
  slug: sase-5g-api-network-slice-request-example
- key_count: 8
  name: Sase 5G Api Security Metrics5 G Example
  slug: sase-5g-api-security-metrics5-g-example
- key_count: 11
  name: Sase 5G Api Security Policy5 G Example
  slug: sase-5g-api-security-policy5-g-example
- key_count: 8
  name: Sase 5G Api Security Policy5 G Request Example
  slug: sase-5g-api-security-policy5-g-request-example
- key_count: 7
  name: Sase 5G Api Tenant5 G Example
  slug: sase-5g-api-tenant5-g-example
- key_count: 4
  name: Sase 5G Api Tenant5 G Request Example
  slug: sase-5g-api-tenant5-g-request-example
- key_count: 1
  name: Sase 5G Monitor Api Count Filter Request Example
  slug: sase-5g-monitor-api-count-filter-request-example
- key_count: 2
  name: Sase 5G Monitor Api Incidents Count Request Example
  slug: sase-5g-monitor-api-incidents-count-request-example
- key_count: 5
  name: Sase 5G Monitor Api Mapping Request Example
  slug: sase-5g-monitor-api-mapping-request-example
- key_count: 3
  name: Sase 5G Monitor Api Throughput Request Example
  slug: sase-5g-monitor-api-throughput-request-example
- key_count: 3
  name: Sase 5G Monitor Api Trend Request Example
  slug: sase-5g-monitor-api-trend-request-example
- key_count: 7
  name: Sase Aggregate Monitoring Api Aggregation Query Example
  slug: sase-aggregate-monitoring-api-aggregation-query-example
- key_count: 5
  name: Sase Aggregate Monitoring Api Aggregation Response Example
  slug: sase-aggregate-monitoring-api-aggregation-response-example
- key_count: 5
  name: Sase Aggregate Monitoring Api Tenant Summary Example
  slug: sase-aggregate-monitoring-api-tenant-summary-example
- key_count: 5
  name: Sase Config Orchestration Api Bandwidth Allocation Example
  slug: sase-config-orchestration-api-bandwidth-allocation-example
- key_count: 3
  name: Sase Config Orchestration Api I Psec Tunnel Example
  slug: sase-config-orchestration-api-i-psec-tunnel-example
- key_count: 5
  name: Sase Config Orchestration Api Ike Gateway Config Example
  slug: sase-config-orchestration-api-ike-gateway-config-example
- key_count: 5
  name: Sase Config Orchestration Api Ike Gateway Example
  slug: sase-config-orchestration-api-ike-gateway-example
- key_count: 6
  name: Sase Config Orchestration Api Onboarding Status Example
  slug: sase-config-orchestration-api-onboarding-status-example
- key_count: 6
  name: Sase Config Orchestration Api Prisma Access Location Example
  slug: sase-config-orchestration-api-prisma-access-location-example
- key_count: 11
  name: Sase Config Orchestration Api Remote Network Example
  slug: sase-config-orchestration-api-remote-network-example
- key_count: 6
  name: Sase Config Orchestration Api Remote Network Request Example
  slug: sase-config-orchestration-api-remote-network-request-example
- key_count: 7
  name: Sase Iam Api Access Policy Example
  slug: sase-iam-api-access-policy-example
- key_count: 4
  name: Sase Iam Api Access Policy Request Example
  slug: sase-iam-api-access-policy-request-example
- key_count: 5
  name: Sase Iam Api Role Example
  slug: sase-iam-api-role-example
- key_count: 6
  name: Sase Iam Api Service Account Credentials Example
  slug: sase-iam-api-service-account-credentials-example
- key_count: 8
  name: Sase Iam Api Service Account Example
  slug: sase-iam-api-service-account-example
- key_count: 4
  name: Sase Iam Api Service Account Request Example
  slug: sase-iam-api-service-account-request-example
- key_count: 2
  name: Sase Iam Api Service Account Update Example
  slug: sase-iam-api-service-account-update-example
- key_count: 2
  name: Sase Multitenant Interconnect Api Dedicated Vlan Attachment Details Entry Example
  slug: sase-multitenant-interconnect-api-dedicated-vlan-attachment-details-entry-example
- key_count: 11
  name: Sase Multitenant Interconnect Api Interconnect Request Example
  slug: sase-multitenant-interconnect-api-interconnect-request-example
- key_count: 3
  name: Sase Multitenant Interconnect Api Ip Block Entry Example
  slug: sase-multitenant-interconnect-api-ip-block-entry-example
- key_count: 2
  name: Sase Multitenant Interconnect Api Ip Pool Request Example
  slug: sase-multitenant-interconnect-api-ip-pool-request-example
- key_count: 7
  name: Sase Multitenant Interconnect Api Physical Connection Entry Example
  slug: sase-multitenant-interconnect-api-physical-connection-entry-example
- key_count: 2
  name: Sase Multitenant Interconnect Api Settings Entry Example
  slug: sase-multitenant-interconnect-api-settings-entry-example
- key_count: 2
  name: Sase Multitenant Interconnect Api Vlan Attachment Custom Ip Address Example
  slug: sase-multitenant-interconnect-api-vlan-attachment-custom-ip-address-example
- key_count: 12
  name: Sase Multitenant Interconnect Api Vlan Attachment Request Example
  slug: sase-multitenant-interconnect-api-vlan-attachment-request-example
- key_count: 1
  name: Sase Multitenant Notifications Api Email Channel Details Example
  slug: sase-multitenant-notifications-api-email-channel-details-example
- key_count: 2
  name: Sase Multitenant Notifications Api Email Details Example
  slug: sase-multitenant-notifications-api-email-details-example
- key_count: 5
  name: Sase Multitenant Notifications Api Mt Notif Agg Key Example
  slug: sase-multitenant-notifications-api-mt-notif-agg-key-example
- key_count: 11
  name: Sase Multitenant Notifications Api Mt Notification Example
  slug: sase-multitenant-notifications-api-mt-notification-example
- key_count: 3
  name: Sase Multitenant Notifications Api Notif Category Detail Example
  slug: sase-multitenant-notifications-api-notif-category-detail-example
- key_count: 5
  name: Sase Multitenant Notifications Api Notif Channel Example
  slug: sase-multitenant-notifications-api-notif-channel-example
- key_count: 2
  name: Sase Multitenant Notifications Api Notif Filter Example
  slug: sase-multitenant-notifications-api-notif-filter-example
- key_count: 3
  name: Sase Multitenant Notifications Api Notif List Api Req Body Example
  slug: sase-multitenant-notifications-api-notif-list-api-req-body-example
- key_count: 11
  name: Sase Multitenant Notifications Api Notif Profile Example
  slug: sase-multitenant-notifications-api-notif-profile-example
- key_count: 2
  name: Sase Multitenant Notifications Api Notif State Change Api Body Example
  slug: sase-multitenant-notifications-api-notif-state-change-api-body-example
- key_count: 3
  name: Sase Multitenant Notifications Api Notif Sub Category Detail Example
  slug: sase-multitenant-notifications-api-notif-sub-category-detail-example
- key_count: 2
  name: Sase Multitenant Notifications Api Notif Type Detail Example
  slug: sase-multitenant-notifications-api-notif-type-detail-example
- key_count: 2
  name: Sase Multitenant Notifications Api Sort By Example
  slug: sase-multitenant-notifications-api-sort-by-example
- key_count: 3
  name: Sase Multitenant Notifications Api Webhook Channel Details Example
  slug: sase-multitenant-notifications-api-webhook-channel-details-example
- key_count: 9
  name: Sase Notifications Announcement Notification Example
  slug: sase-notifications-announcement-notification-example
- key_count: 11
  name: Sase Notifications Certificate Expiry Notification Example
  slug: sase-notifications-certificate-expiry-notification-example
- key_count: 10
  name: Sase Notifications Dataplane Upgrade Notification Example
  slug: sase-notifications-dataplane-upgrade-notification-example
- key_count: 9
  name: Sase Notifications Incident Detail Example
  slug: sase-notifications-incident-detail-example
- key_count: 10
  name: Sase Notifications Incident Notification Example
  slug: sase-notifications-incident-notification-example
- key_count: 3
  name: Sase Notifications Service Info Example
  slug: sase-notifications-service-info-example
- key_count: 3
  name: Sase Notifications Tenant Context Example
  slug: sase-notifications-tenant-context-example
- key_count: 4
  name: Sase Subscription Api Allocation Entry Example
  slug: sase-subscription-api-allocation-entry-example
- key_count: 1
  name: Sase Subscription Api Allocation Request Example
  slug: sase-subscription-api-allocation-request-example
- key_count: 5
  name: Sase Subscription Api Entitlement Example
  slug: sase-subscription-api-entitlement-example
- key_count: 4
  name: Sase Subscription Api Subscription Entitlements Example
  slug: sase-subscription-api-subscription-entitlements-example
- key_count: 11
  name: Sase Subscription Api Subscription Example
  slug: sase-subscription-api-subscription-example
- key_count: 11
  name: Sase Tenancy Api Tenant Service Group Example
  slug: sase-tenancy-api-tenant-service-group-example
- key_count: 6
  name: Sase Tenancy Api Tenant Service Group Request Example
  slug: sase-tenancy-api-tenant-service-group-request-example
- key_count: 3
  name: Sase Tenancy Api Tenant Service Group Update Example
  slug: sase-tenancy-api-tenant-service-group-update-example
- key_count: 15
  name: Security Advisory Api Advisory Example
  slug: security-advisory-api-advisory-example
- key_count: 2
  name: Security Advisory Api Affected Product Example
  slug: security-advisory-api-affected-product-example
- key_count: 2
  name: Security Advisory Api Product Example
  slug: security-advisory-api-product-example
- key_count: 6
  name: Sspm Api Catalog App Example
  slug: sspm-api-catalog-app-example
- key_count: 7
  name: Sspm Api Jira Integration Example
  slug: sspm-api-jira-integration-example
- key_count: 7
  name: Sspm Api Jira Integration Request Example
  slug: sspm-api-jira-integration-request-example
- key_count: 3
  name: Sspm Api Onboard App Request Example
  slug: sspm-api-onboard-app-request-example
- key_count: 8
  name: Sspm Api Onboarded App Example
  slug: sspm-api-onboarded-app-example
- key_count: 11
  name: Sspm Api Posture Check Example
  slug: sspm-api-posture-check-example
- key_count: 10
  name: Strata Cloud Manager Api Address Example
  slug: strata-cloud-manager-api-address-example
- key_count: 7
  name: Strata Cloud Manager Api Address Group Example
  slug: strata-cloud-manager-api-address-group-example
- key_count: 4
  name: Strata Cloud Manager Api Address Group List Example
  slug: strata-cloud-manager-api-address-group-list-example
- key_count: 5
  name: Strata Cloud Manager Api Address Group Request Example
  slug: strata-cloud-manager-api-address-group-request-example
- key_count: 4
  name: Strata Cloud Manager Api Address List Example
  slug: strata-cloud-manager-api-address-list-example
- key_count: 7
  name: Strata Cloud Manager Api Address Request Example
  slug: strata-cloud-manager-api-address-request-example
- key_count: 1
  name: Strata Cloud Manager Api Delete Response Example
  slug: strata-cloud-manager-api-delete-response-example
- key_count: 8
  name: Strata Cloud Manager Api Job Example
  slug: strata-cloud-manager-api-job-example
- key_count: 15
  name: Strata Cloud Manager Api Nat Rule Example
  slug: strata-cloud-manager-api-nat-rule-example
- key_count: 4
  name: Strata Cloud Manager Api Nat Rule List Example
  slug: strata-cloud-manager-api-nat-rule-list-example
- key_count: 11
  name: Strata Cloud Manager Api Nat Rule Request Example
  slug: strata-cloud-manager-api-nat-rule-request-example
- key_count: 18
  name: Strata Cloud Manager Api Security Rule Example
  slug: strata-cloud-manager-api-security-rule-example
- key_count: 4
  name: Strata Cloud Manager Api Security Rule List Example
  slug: strata-cloud-manager-api-security-rule-list-example
- key_count: 15
  name: Strata Cloud Manager Api Security Rule Request Example
  slug: strata-cloud-manager-api-security-rule-request-example
- key_count: 6
  name: Strata Cloud Manager Api Service Example
  slug: strata-cloud-manager-api-service-example
- key_count: 4
  name: Strata Cloud Manager Api Service List Example
  slug: strata-cloud-manager-api-service-list-example
- key_count: 4
  name: Strata Cloud Manager Api Service Request Example
  slug: strata-cloud-manager-api-service-request-example
- key_count: 17
  name: Strata Logging Forwarding Auth Log Payload Example
  slug: strata-logging-forwarding-auth-log-payload-example
- key_count: 24
  name: Strata Logging Forwarding Threat Log Payload Example
  slug: strata-logging-forwarding-threat-log-payload-example
- key_count: 30
  name: Strata Logging Forwarding Traffic Log Payload Example
  slug: strata-logging-forwarding-traffic-log-payload-example
- key_count: 19
  name: Strata Logging Forwarding Url Log Payload Example
  slug: strata-logging-forwarding-url-log-payload-example
- key_count: 19
  name: Strata Logging Forwarding Wildfire Log Payload Example
  slug: strata-logging-forwarding-wildfire-log-payload-example
- key_count: 8
  name: Strata Logging Service Api Email Destination Example
  slug: strata-logging-service-api-email-destination-example
- key_count: 6
  name: Strata Logging Service Api Email Destination Request Example
  slug: strata-logging-service-api-email-destination-request-example
- key_count: 3
  name: Strata Logging Service Api Forwarding Status Example
  slug: strata-logging-service-api-forwarding-status-example
- key_count: 7
  name: Strata Logging Service Api Https Destination Example
  slug: strata-logging-service-api-https-destination-example
- key_count: 6
  name: Strata Logging Service Api Https Destination Request Example
  slug: strata-logging-service-api-https-destination-request-example
- key_count: 8
  name: Strata Logging Service Api Log Forwarding Profile Example
  slug: strata-logging-service-api-log-forwarding-profile-example
- key_count: 4
  name: Strata Logging Service Api Log Forwarding Profile Request Example
  slug: strata-logging-service-api-log-forwarding-profile-request-example
- key_count: 9
  name: Strata Logging Service Api Syslog Destination Example
  slug: strata-logging-service-api-syslog-destination-example
- key_count: 7
  name: Strata Logging Service Api Syslog Destination Request Example
  slug: strata-logging-service-api-syslog-destination-request-example
- key_count: 2
  name: Threat Vault Api Api Stats Example
  slug: threat-vault-api-api-stats-example
- key_count: 6
  name: Threat Vault Api Atp Report Example
  slug: threat-vault-api-atp-report-example
- key_count: 5
  name: Threat Vault Api Atp Report List Example
  slug: threat-vault-api-atp-report-list-example
- key_count: 7
  name: Threat Vault Api Release Note Example
  slug: threat-vault-api-release-note-example
- key_count: 5
  name: Threat Vault Api Release Notes List Example
  slug: threat-vault-api-release-notes-list-example
- key_count: 5
  name: Threat Vault Api Threat History Entry Example
  slug: threat-vault-api-threat-history-entry-example
- key_count: 5
  name: Threat Vault Api Threat History List Example
  slug: threat-vault-api-threat-history-list-example
- key_count: 6
  name: Threat Vault Api Threat List Example
  slug: threat-vault-api-threat-list-example
- key_count: 16
  name: Threat Vault Api Threat Signature Example
  slug: threat-vault-api-threat-signature-example
- key_count: 1
  name: Wildfire Api Analysis Report Example
  slug: wildfire-api-analysis-report-example
- key_count: 1
  name: Wildfire Api Bulk Verdict Response Example
  slug: wildfire-api-bulk-verdict-response-example
- key_count: 6
  name: Wildfire Api Sandbox Report Example
  slug: wildfire-api-sandbox-report-example
- key_count: 1
  name: Wildfire Api Submit Response Example
  slug: wildfire-api-submit-response-example
- key_count: 1
  name: Wildfire Api Verdict Response Example
  slug: wildfire-api-verdict-response-example
- key_count: 10
  name: Ztna Connector Api Connector Example
  slug: ztna-connector-api-connector-example
- key_count: 6
  name: Ztna Connector Api Connector Group Example
  slug: ztna-connector-api-connector-group-example
- key_count: 3
  name: Ztna Connector Api Connector Group Request Example
  slug: ztna-connector-api-connector-group-request-example
- key_count: 3
  name: Ztna Connector Api Connector Request Example
  slug: ztna-connector-api-connector-request-example
- key_count: 7
  name: Ztna Connector Api Fqdn Rule Example
  slug: ztna-connector-api-fqdn-rule-example
- key_count: 5
  name: Ztna Connector Api Fqdn Rule Request Example
  slug: ztna-connector-api-fqdn-rule-request-example
- key_count: 5
  name: Ztna Connector Api License Info Example
  slug: ztna-connector-api-license-info-example
- key_count: 6
  name: Ztna Connector Api Subnet Rule Example
  slug: ztna-connector-api-subnet-rule-example
- key_count: 4
  name: Ztna Connector Api Subnet Rule Request Example
  slug: ztna-connector-api-subnet-rule-request-example
- key_count: 9
  name: Ztna Connector Api Ztna Application Example
  slug: ztna-connector-api-ztna-application-example
- key_count: 7
  name: Ztna Connector Api Ztna Application Request Example
  slug: ztna-connector-api-ztna-application-request-example
features:
- description: Next-generation firewall policies with application, user, and content awareness for enforcing zero trust across on-premises and cloud environments.
  name: Zero Trust Network Security
- description: Machine learning and deep learning models that detect and prevent known and unknown threats in real time across network traffic, files, and URLs.
  name: AI-Powered Threat Prevention
- description: Full lifecycle cloud security spanning code, build, deploy, and runtime with CSPM, CWPP, code security, and data security posture management.
  name: Cloud-Native Application Protection
- description: Automated incident response with playbooks, integrations, and case management through Cortex XSOAR and XSIAM platforms.
  name: Security Orchestration and Automation
- description: Cross-data-source threat detection correlating endpoint, network, cloud, and identity data through Cortex XDR for unified security operations.
  name: Extended Detection and Response
- description: Real-time scanning of AI application prompts and responses for prompt injection, data leakage, toxic content, and other AI-specific threats.
  name: AI Runtime Security
- description: Cloud-delivered security and networking combining Prisma Access, SD-WAN, ZTNA, and cloud SWG for secure access from any location.
  name: Secure Access Service Edge
- description: Continuous discovery and monitoring of internet-facing assets and exposures through Cortex Xpanse for external attack surface visibility.
  name: Attack Surface Management
- description: Automated security scanning of Terraform, CloudFormation, Kubernetes, and other IaC templates for misconfigurations before deployment.
  name: Infrastructure as Code Security
- description: End-to-end visibility into application performance and user experience across SASE connections with Autonomous DEM.
  name: Digital Experience Monitoring
- description: Comprehensive threat intelligence through Threat Vault, WildFire malware analysis, DNS Security, and Unit 42 research for proactive defense.
  name: Threat Intelligence
- description: Hierarchical tenant management with delegated administration, aggregate monitoring, and shared policy for MSSPs and large enterprises.
  name: Multi-Tenant Management
finops:
- has_sources: true
  method: generated
  name: Palo Alto Networks Finops
  primary_unit: ''
  service_category: Cybersecurity
  slug: palo-alto-networks-finops
  template: false
image: /assets/icons/palo-alto-networks.png
json_schemas:
- name: BPACheck
  property_count: 10
  slug: aiops-ngfw-bpa-api-bpa-check
- name: BPAReport
  property_count: 10
  slug: aiops-ngfw-bpa-api-bpa-report
- name: BPARequest
  property_count: 3
  slug: aiops-ngfw-bpa-api-bpa-request
- name: BPARequestStatus
  property_count: 7
  slug: aiops-ngfw-bpa-api-bpa-request-status
- name: AgentScore
  property_count: 11
  slug: autonomous-dem-api-agent-score
- name: ApplicationScore
  property_count: 13
  slug: autonomous-dem-api-application-score
- name: MonitoredAgent
  property_count: 9
  slug: autonomous-dem-api-monitored-agent
- name: MonitoredApplication
  property_count: 8
  slug: autonomous-dem-api-monitored-application
- name: PerformanceMetric
  property_count: 9
  slug: autonomous-dem-api-performance-metric
- name: TestResult
  property_count: 11
  slug: autonomous-dem-api-test-result
- name: attr_based_filter
  property_count: 3
  slug: cloud-identity-engine-api-attr_based_filter
- name: check_group_membership
  property_count: 6
  slug: cloud-identity-engine-api-check_group_membership
- name: check_user_in_particular_group
  property_count: 7
  slug: cloud-identity-engine-api-check_user_in_particular_group
- name: domain_param
  property_count: 1
  slug: cloud-identity-engine-api-domain_param
- name: fetch_all_users_attrs
  property_count: 5
  slug: cloud-identity-engine-api-fetch_all_users_attrs
- name: group_filter
  property_count: 3
  slug: cloud-identity-engine-api-group_filter
- name: list_all_groups_in_domain
  property_count: 5
  slug: cloud-identity-engine-api-list_all_groups_in_domain
- name: list_all_users_in_domain
  property_count: 5
  slug: cloud-identity-engine-api-list_all_users_in_domain
- name: list_groups_user_belongs_to
  property_count: 4
  slug: cloud-identity-engine-api-list_groups_user_belongs_to
- name: list_specific_groups
  property_count: 6
  slug: cloud-identity-engine-api-list_specific_groups
- name: list_specific_users
  property_count: 6
  slug: cloud-identity-engine-api-list_specific_users
- name: list_users_in_particular_group
  property_count: 5
  slug: cloud-identity-engine-api-list_users_in_particular_group
- name: pagination_params
  property_count: 2
  slug: cloud-identity-engine-api-pagination_params
- name: FirewallRequest
  property_count: 2
  slug: cloud-ngfw-api-firewall-request
- name: Firewall
  property_count: 3
  slug: cloud-ngfw-api-firewall
- name: FirewallSummary
  property_count: 4
  slug: cloud-ngfw-api-firewall-summary
- name: FqdnListRequest
  property_count: 2
  slug: cloud-ngfw-api-fqdn-list-request
- name: FqdnList
  property_count: 3
  slug: cloud-ngfw-api-fqdn-list
- name: FqdnListSummary
  property_count: 1
  slug: cloud-ngfw-api-fqdn-list-summary
- name: PrefixListRequest
  property_count: 2
  slug: cloud-ngfw-api-prefix-list-request
- name: PrefixList
  property_count: 3
  slug: cloud-ngfw-api-prefix-list
- name: PrefixListSummary
  property_count: 1
  slug: cloud-ngfw-api-prefix-list-summary
- name: ResponseStatus
  property_count: 2
  slug: cloud-ngfw-api-response-status
- name: RuleDestination
  property_count: 5
  slug: cloud-ngfw-api-rule-destination
- name: RuleSource
  property_count: 4
  slug: cloud-ngfw-api-rule-source
- name: RuleStackRequest
  property_count: 2
  slug: cloud-ngfw-api-rule-stack-request
- name: RuleStack
  property_count: 3
  slug: cloud-ngfw-api-rule-stack
- name: RuleStackSummary
  property_count: 3
  slug: cloud-ngfw-api-rule-stack-summary
- name: SecurityRuleRequest
  property_count: 2
  slug: cloud-ngfw-api-security-rule-request
- name: SecurityRule
  property_count: 2
  slug: cloud-ngfw-api-security-rule
- name: SecurityRuleSummary
  property_count: 3
  slug: cloud-ngfw-api-security-rule-summary
- name: Alert
  property_count: 17
  slug: cortex-xdr-api-alert
- name: AuditLog
  property_count: 9
  slug: cortex-xdr-api-audit-log
- name: Endpoint
  property_count: 20
  slug: cortex-xdr-api-endpoint
- name: Filter
  property_count: 3
  slug: cortex-xdr-api-filter
- name: IncidentDetail
  property_count: 28
  slug: cortex-xdr-api-incident-detail
- name: Incident
  property_count: 21
  slug: cortex-xdr-api-incident
- name: SortOrder
  property_count: 2
  slug: cortex-xdr-api-sort-order
- name: Cortex XDR Incident
  property_count: 21
  slug: cortex-xdr-incident
- name: AlertPayload
  property_count: 10
  slug: cortex-xdr-webhooks-alert-payload
- name: IncidentPayload
  property_count: 10
  slug: cortex-xdr-webhooks-incident-payload
- name: AsmIncident
  property_count: 14
  slug: cortex-xpanse-api-asm-incident
- name: AssetInternetExposureDetail
  property_count: 17
  slug: cortex-xpanse-api-asset-internet-exposure-detail
- name: AssetInternetExposure
  property_count: 13
  slug: cortex-xpanse-api-asset-internet-exposure
- name: AttackSurfaceRule
  property_count: 10
  slug: cortex-xpanse-api-attack-surface-rule
- name: AuditLog
  property_count: 9
  slug: cortex-xpanse-api-audit-log
- name: ExposedService
  property_count: 13
  slug: cortex-xpanse-api-exposed-service
- name: Filter
  property_count: 3
  slug: cortex-xpanse-api-filter
- name: OwnedIpRange
  property_count: 10
  slug: cortex-xpanse-api-owned-ip-range
- name: SortOrder
  property_count: 2
  slug: cortex-xpanse-api-sort-order
- name: Alert
  property_count: 12
  slug: cortex-xsiam-api-alert
- name: Asset
  property_count: 10
  slug: cortex-xsiam-api-asset
- name: AuditLog
  property_count: 9
  slug: cortex-xsiam-api-audit-log
- name: Endpoint
  property_count: 14
  slug: cortex-xsiam-api-endpoint
- name: Filter
  property_count: 3
  slug: cortex-xsiam-api-filter
- name: Incident
  property_count: 15
  slug: cortex-xsiam-api-incident
- name: SortOrder
  property_count: 2
  slug: cortex-xsiam-api-sort-order
- name: EventDataPayload
  property_count: 8
  slug: cortex-xsiam-data-ingestion-event-data-payload
- name: LogDataPayload
  property_count: 8
  slug: cortex-xsiam-data-ingestion-log-data-payload
- name: XdrDataPayload
  property_count: 8
  slug: cortex-xsiam-data-ingestion-xdr-data-payload
- name: CreateEntryRequest
  property_count: 4
  slug: cortex-xsoar-api-create-entry-request
- name: CreateIncidentRequest
  property_count: 10
  slug: cortex-xsoar-api-create-incident-request
- name: Entry
  property_count: 9
  slug: cortex-xsoar-api-entry
- name: Incident
  property_count: 20
  slug: cortex-xsoar-api-incident
- name: IncidentSearchRequest
  property_count: 5
  slug: cortex-xsoar-api-incident-search-request
- name: IncidentSearchResponse
  property_count: 3
  slug: cortex-xsoar-api-incident-search-response
- name: IntegrationInstance
  property_count: 8
  slug: cortex-xsoar-api-integration-instance
- name: Integration
  property_count: 9
  slug: cortex-xsoar-api-integration
- name: Investigation
  property_count: 9
  slug: cortex-xsoar-api-investigation
- name: Playbook
  property_count: 8
  slug: cortex-xsoar-api-playbook
- name: UpdateIncidentRequest
  property_count: 9
  slug: cortex-xsoar-api-update-incident-request
- name: Cortex XSOAR Integration Manifest
  property_count: 11
  slug: cortex-xsoar-integration-manifest
- name: ContentSnippet
  property_count: 5
  slug: dlp-api-content-snippet
- name: DataPattern
  property_count: 9
  slug: dlp-api-data-pattern
- name: DLPIncident
  property_count: 18
  slug: dlp-api-dlp-incident
- name: IncidentSummary
  property_count: 8
  slug: dlp-api-incident-summary
- name: DomainDetail
  property_count: 10
  slug: dns-security-api-domain-detail
- name: NetworkStats
  property_count: 8
  slug: dns-security-api-network-stats
- name: EmailAttachment
  property_count: 6
  slug: email-dlp-api-email-attachment
- name: EmailDLPIncident
  property_count: 15
  slug: email-dlp-api-email-dlp-incident
- name: EmailRecipient
  property_count: 3
  slug: email-dlp-api-email-recipient
- name: CreateTicketRequest
  property_count: 8
  slug: identity-security-posture-management-api-create-ticket-request
- name: DownloadCsvRequest
  property_count: 3
  slug: identity-security-posture-management-api-download-csv-request
- name: Feature
  property_count: 0
  slug: identity-security-posture-management-api-feature
- name: FeatureState
  property_count: 2
  slug: identity-security-posture-management-api-feature-state
- name: IdpInfo
  property_count: 3
  slug: identity-security-posture-management-api-idp-info
- name: Instant
  property_count: 0
  slug: identity-security-posture-management-api-instant
- name: ListResponseIdpInfo
  property_count: 2
  slug: identity-security-posture-management-api-list-response-idp-info
- name: ListResponseMapStringObject
  property_count: 2
  slug: identity-security-posture-management-api-list-response-map-string-object
- name: ListResponseMfaActivity
  property_count: 2
  slug: identity-security-posture-management-api-list-response-mfa-activity
- name: ListResponseSaaSAccount
  property_count: 2
  slug: identity-security-posture-management-api-list-response-saa-s-account
- name: ListResponseSaaSActivity
  property_count: 2
  slug: identity-security-posture-management-api-list-response-saa-s-activity
- name: ListResponseSaaSInstanceInfo
  property_count: 2
  slug: identity-security-posture-management-api-list-response-saa-s-instance-info
- name: ListResponseTicket
  property_count: 2
  slug: identity-security-posture-management-api-list-response-ticket
- name: MfaActivityCountByAppType
  property_count: 3
  slug: identity-security-posture-management-api-mfa-activity-count-by-app-type
- name: MfaActivity
  property_count: 18
  slug: identity-security-posture-management-api-mfa-activity
- name: RemediationRequest
  property_count: 1
  slug: identity-security-posture-management-api-remediation-request
- name: SaaSAccount
  property_count: 28
  slug: identity-security-posture-management-api-saa-s-account
- name: SaaSActivity
  property_count: 15
  slug: identity-security-posture-management-api-saa-s-activity
- name: SaaSInstanceInfo
  property_count: 3
  slug: identity-security-posture-management-api-saa-s-instance-info
- name: Ticket
  property_count: 12
  slug: identity-security-posture-management-api-ticket
- name: UnlinkTicketRequest
  property_count: 3
  slug: identity-security-posture-management-api-unlink-ticket-request
- name: Alert
  property_count: 11
  slug: iot-security-api-alert
- name: AssetReport
  property_count: 7
  slug: iot-security-api-asset-report
- name: Device
  property_count: 18
  slug: iot-security-api-device
- name: DeviceTag
  property_count: 5
  slug: iot-security-api-device-tag
- name: PolicyRecommendation
  property_count: 10
  slug: iot-security-api-policy-recommendation
- name: Vulnerability
  property_count: 10
  slug: iot-security-api-vulnerability
- name: AccountGroupMetadataViewModel
  property_count: 3
  slug: palo-alto-networks-account-group-metadata-view-model
- name: AccountGroupModel
  property_count: 9
  slug: palo-alto-networks-account-group-model
- name: AccountGroupViewModel
  property_count: 12
  slug: palo-alto-networks-account-group-view-model
- name: ActionPlanApiRequest
  property_count: 4
  slug: palo-alto-networks-action-plan-api-request
- name: ActionPlanRelatedAlertsResponse
  property_count: 5
  slug: palo-alto-networks-action-plan-related-alerts-response
- name: ActionPlan
  property_count: 21
  slug: palo-alto-networks-action-plan
- name: ActionPlanSuggestResponse
  property_count: 7
  slug: palo-alto-networks-action-plan-suggest-response
- name: AddressList
  property_count: 4
  slug: palo-alto-networks-address-list
- name: AddressRequest
  property_count: 7
  slug: palo-alto-networks-address-request
- name: Address
  property_count: 10
  slug: palo-alto-networks-address
- name: addresses
  property_count: 4
  slug: palo-alto-networks-addresses
- name: agent-profiles
  property_count: 16
  slug: palo-alto-networks-agent-profiles
- name: AIProfile
  property_count: 6
  slug: palo-alto-networks-aiprofile
- name: Alert_3
  property_count: 11
  slug: palo-alto-networks-alert-3
- name: AlertFilterSuggestion
  property_count: 36
  slug: palo-alto-networks-alert-filter-suggestion
- name: AlertModel
  property_count: 24
  slug: palo-alto-networks-alert-model
- name: Alert
  property_count: 17
  slug: palo-alto-networks-alert
- name: AnalysisReport
  property_count: 1
  slug: palo-alto-networks-analysis-report
- name: api.ResolveImagesReq
  property_count: 1
  slug: palo-alto-networks-api-resolve-images-req
- name: api.ResolveImagesResp
  property_count: 1
  slug: palo-alto-networks-api-resolve-images-resp
- name: ApiStats
  property_count: 2
  slug: palo-alto-networks-api-stats
- name: api.User
  property_count: 7
  slug: palo-alto-networks-api-user
- name: ApplicationPage
  property_count: 5
  slug: palo-alto-networks-application-page
- name: Application
  property_count: 7
  slug: palo-alto-networks-application
- name: applications
  property_count: 29
  slug: palo-alto-networks-applications
- name: Asset_2
  property_count: 12
  slug: palo-alto-networks-asset-2
- name: AssetDTO
  property_count: 17
  slug: palo-alto-networks-asset-dto
- name: AssetInternetExposureDetail
  property_count: 17
  slug: palo-alto-networks-asset-internet-exposure-detail
- name: AssetInternetExposure
  property_count: 13
  slug: palo-alto-networks-asset-internet-exposure
- name: AssetReport
  property_count: 7
  slug: palo-alto-networks-asset-report
- name: Asset
  property_count: 10
  slug: palo-alto-networks-asset
- name: AttackDetailResponseSchema
  property_count: 26
  slug: palo-alto-networks-attack-detail-response-schema
- name: AttackMultiTurnDetailResponseSchema
  property_count: 26
  slug: palo-alto-networks-attack-multi-turn-detail-response-schema
- name: AuditEvent
  property_count: 40
  slug: palo-alto-networks-audit-event
- name: authentication-settings
  property_count: 3
  slug: palo-alto-networks-authentication-settings
- name: BaseReportGenerationConfigApiModel
  property_count: 17
  slug: palo-alto-networks-base-report-generation-config-api-model
- name: BrowserSession
  property_count: 9
  slug: palo-alto-networks-browser-session
- name: BrowserUser
  property_count: 6
  slug: palo-alto-networks-browser-user
- name: CatalogApplication
  property_count: 6
  slug: palo-alto-networks-catalog-application
- name: CatalogConfig
  property_count: 17
  slug: palo-alto-networks-catalog-config
- name: categories
  property_count: 1
  slug: palo-alto-networks-categories
- name: ChangePasswordRequest
  property_count: 1
  slug: palo-alto-networks-change-password-request
- name: check_user_in_particular_group_2
  property_count: 7
  slug: palo-alto-networks-check-user-in-particular-group-2
- name: check_user_in_particular_group
  property_count: 7
  slug: palo-alto-networks-check-user-in-particular-group
- name: CicdRunsFilters
  property_count: 19
  slug: palo-alto-networks-cicd-runs-filters
- name: CIScan
  property_count: 5
  slug: palo-alto-networks-ciscan
- name: CodeError
  property_count: 15
  slug: palo-alto-networks-code-error
- name: CommonControlProfiles
  property_count: 3
  slug: palo-alto-networks-common-control-profiles
- name: common.DaemonSetOptions
  property_count: 30
  slug: palo-alto-networks-common-daemon-set-options
- name: Config
  property_count: 25
  slug: palo-alto-networks-config
- name: Container
  property_count: 11
  slug: palo-alto-networks-container
- name: CountFilterRequest
  property_count: 1
  slug: palo-alto-networks-count-filter-request
- name: CreateManagedTenantRequest
  property_count: 8
  slug: palo-alto-networks-create-managed-tenant-request
- name: CreatePolicyGroupResponse
  property_count: 3
  slug: palo-alto-networks-create-policy-group-response
- name: create_sites_request
  property_count: 1
  slug: palo-alto-networks-create-sites-request
- name: CreateTenantGroupRequest
  property_count: 2
  slug: palo-alto-networks-create-tenant-group-request
- name: CreateTicketRequest
  property_count: 8
  slug: palo-alto-networks-create-ticket-request
- name: CreateUserAccessKeyResponseModel
  property_count: 2
  slug: palo-alto-networks-create-user-access-key-response-model
- name: DataSecurityAlert
  property_count: 14
  slug: palo-alto-networks-data-security-alert
- name: defender.Defender
  property_count: 31
  slug: palo-alto-networks-defender-defender
- name: Defender
  property_count: 8
  slug: palo-alto-networks-defender
- name: DefenderSummary
  property_count: 5
  slug: palo-alto-networks-defender-summary
- name: DeleteResponse
  property_count: 1
  slug: palo-alto-networks-delete-response
- name: Device_2
  property_count: 18
  slug: palo-alto-networks-device-2
- name: Device
  property_count: 41
  slug: palo-alto-networks-device
- name: devices-put
  property_count: 5
  slug: palo-alto-networks-devices-put
- name: devices
  property_count: 41
  slug: palo-alto-networks-devices
- name: DownloadCsvRequest
  property_count: 3
  slug: palo-alto-networks-download-csv-request
- name: DynamicJobReportSchema
  property_count: 7
  slug: palo-alto-networks-dynamic-job-report-schema
- name: EnterpriseSettingsRequestModel
  property_count: 12
  slug: palo-alto-networks-enterprise-settings-request-model
- name: EventsCreateIntegrationRequest
  property_count: 4
  slug: palo-alto-networks-events-create-integration-request
- name: EventsIntegrationModel
  property_count: 10
  slug: palo-alto-networks-events-integration-model
- name: EventsTestIntegrationRequest
  property_count: 3
  slug: palo-alto-networks-events-test-integration-request
- name: EventsUpdateIntegrationRequest
  property_count: 4
  slug: palo-alto-networks-events-update-integration-request
- name: ExposedService
  property_count: 13
  slug: palo-alto-networks-exposed-service
- name: FeatureState
  property_count: 2
  slug: palo-alto-networks-feature-state
- name: FilterModel
  property_count: 9
  slug: palo-alto-networks-filter-model
- name: Filter
  property_count: 3
  slug: palo-alto-networks-filter
- name: FormLoginRequest
  property_count: 2
  slug: palo-alto-networks-form-login-request
- name: FormLoginResponse
  property_count: 3
  slug: palo-alto-networks-form-login-response
- name: ForwardingStatus
  property_count: 3
  slug: palo-alto-networks-forwarding-status
- name: GetErrorsFilters
  property_count: 14
  slug: palo-alto-networks-get-errors-filters
- name: GetErrorsInFileWithFilters
  property_count: 15
  slug: palo-alto-networks-get-errors-in-file-with-filters
- name: Host
  property_count: 12
  slug: palo-alto-networks-host
- name: identity.ProviderSettings
  property_count: 13
  slug: palo-alto-networks-identity-provider-settings
- name: identity.SamlSettings
  property_count: 13
  slug: palo-alto-networks-identity-saml-settings
- name: Image
  property_count: 13
  slug: palo-alto-networks-image
- name: ImpactedAssetsResponse
  property_count: 5
  slug: palo-alto-networks-impacted-assets-response
- name: IncidentSummary
  property_count: 8
  slug: palo-alto-networks-incident-summary
- name: IncidentsCountRequest
  property_count: 2
  slug: palo-alto-networks-incidents-count-request
- name: int
  property_count: 0
  slug: palo-alto-networks-int
- name: InterconnectRequest
  property_count: 11
  slug: palo-alto-networks-interconnect-request
- name: IPPoolRequest
  property_count: 2
  slug: palo-alto-networks-ippool-request
- name: JiraIntegrationRequest
  property_count: 7
  slug: palo-alto-networks-jira-integration-request
- name: JiraIntegration
  property_count: 7
  slug: palo-alto-networks-jira-integration
- name: JobAbortResponseSchema
  property_count: 2
  slug: palo-alto-networks-job-abort-response-schema
- name: JobCreateRequestSchema
  property_count: 6
  slug: palo-alto-networks-job-create-request-schema
- name: JobListResponseSchema
  property_count: 2
  slug: palo-alto-networks-job-list-response-schema
- name: JobResponseSchema
  property_count: 23
  slug: palo-alto-networks-job-response-schema
- name: Job
  property_count: 8
  slug: palo-alto-networks-job
- name: job_status
  property_count: 5
  slug: palo-alto-networks-job-status
- name: jobs-response
  property_count: 1
  slug: palo-alto-networks-jobs-response
- name: jobs
  property_count: 16
  slug: palo-alto-networks-jobs
- name: LegacySuppression
  property_count: 4
  slug: palo-alto-networks-legacy-suppression
- name: LicenseInfo
  property_count: 5
  slug: palo-alto-networks-license-info
- name: Root Type for license
  property_count: 0
  slug: palo-alto-networks-license
- name: list_groups_user_belongs_to_2
  property_count: 4
  slug: palo-alto-networks-list-groups-user-belongs-to-2
- name: list_groups_user_belongs_to
  property_count: 4
  slug: palo-alto-networks-list-groups-user-belongs-to
- name: ListResponseIdpInfo
  property_count: 2
  slug: palo-alto-networks-list-response-idp-info
- name: ListResponseMfaActivity
  property_count: 2
  slug: palo-alto-networks-list-response-mfa-activity
- name: ListResponseSaaSAccount
  property_count: 2
  slug: palo-alto-networks-list-response-saa-saccount
- name: ListResponseSaaSActivity
  property_count: 2
  slug: palo-alto-networks-list-response-saa-sactivity
- name: ListResponseSaaSInstanceInfo
  property_count: 2
  slug: palo-alto-networks-list-response-saa-sinstance-info
- name: ListResponseTicket
  property_count: 2
  slug: palo-alto-networks-list-response-ticket
- name: list_specific_groups
  property_count: 6
  slug: palo-alto-networks-list-specific-groups
- name: list_users_in_particular_group
  property_count: 5
  slug: palo-alto-networks-list-users-in-particular-group
- name: locations
  property_count: 0
  slug: palo-alto-networks-locations
- name: LogForwardingProfileRequest
  property_count: 4
  slug: palo-alto-networks-log-forwarding-profile-request
- name: LogForwardingProfile
  property_count: 8
  slug: palo-alto-networks-log-forwarding-profile
- name: log-forwarding-profiles
  property_count: 4
  slug: palo-alto-networks-log-forwarding-profiles
- name: ManagedDevice
  property_count: 7
  slug: palo-alto-networks-managed-device
- name: ManagedTenantDetailedResponse
  property_count: 20
  slug: palo-alto-networks-managed-tenant-detailed-response
- name: ManagedTenantResponse
  property_count: 19
  slug: palo-alto-networks-managed-tenant-response
- name: ManagedTenantsResponse
  property_count: 2
  slug: palo-alto-networks-managed-tenants-response
- name: MappingRequest
  property_count: 5
  slug: palo-alto-networks-mapping-request
- name: MfaActivityCountByAppType
  property_count: 3
  slug: palo-alto-networks-mfa-activity-count-by-app-type
- name: mobile-agent-global-settings
  property_count: 2
  slug: palo-alto-networks-mobile-agent-global-settings
- name: mobile-agent-infrastructure-settings
  property_count: 7
  slug: palo-alto-networks-mobile-agent-infrastructure-settings
- name: MonitoredApplication
  property_count: 8
  slug: palo-alto-networks-monitored-application
- name: MsspLicenseInfoResponse
  property_count: 7
  slug: palo-alto-networks-mssp-license-info-response
- name: MsspLicensePoolsResponse
  property_count: 2
  slug: palo-alto-networks-mssp-license-pools-response
- name: MsspLicenseUsageRequestObject
  property_count: 4
  slug: palo-alto-networks-mssp-license-usage-request-object
- name: MsspLicenseUsageResponse
  property_count: 2
  slug: palo-alto-networks-mssp-license-usage-response
- name: MsspListUserResponse
  property_count: 2
  slug: palo-alto-networks-mssp-list-user-response
- name: MsspResponse
  property_count: 6
  slug: palo-alto-networks-mssp-response
- name: MsspUserRequest
  property_count: 3
  slug: palo-alto-networks-mssp-user-request
- name: MsspUserResponse
  property_count: 5
  slug: palo-alto-networks-mssp-user-response
- name: MtNotificationList
  property_count: 0
  slug: palo-alto-networks-mt-notification-list
- name: NotifListApiReqBody
  property_count: 3
  slug: palo-alto-networks-notif-list-api-req-body
- name: NotifStateChangeApiBody
  property_count: 2
  slug: palo-alto-networks-notif-state-change-api-body
- name: objects-applications
  property_count: 29
  slug: palo-alto-networks-objects-applications
- name: OnboardAppRequest
  property_count: 3
  slug: palo-alto-networks-onboard-app-request
- name: OnboardedApp
  property_count: 8
  slug: palo-alto-networks-onboarded-app
- name: OperationAckRequest
  property_count: 3
  slug: palo-alto-networks-operation-ack-request
- name: OperationResponse
  property_count: 13
  slug: palo-alto-networks-operation-response
- name: OperationsResponse
  property_count: 2
  slug: palo-alto-networks-operations-response
- name: PageInfo
  property_count: 2
  slug: palo-alto-networks-page-info
- name: PhysicalConnectionEntry
  property_count: 7
  slug: palo-alto-networks-physical-connection-entry
- name: PolicyGroupRequest
  property_count: 2
  slug: palo-alto-networks-policy-group-request
- name: PolicyGroupResponse
  property_count: 4
  slug: palo-alto-networks-policy-group-response
- name: PolicyGroupsListResponse
  property_count: 2
  slug: palo-alto-networks-policy-groups-list-response
- name: PrismaAccessLocation
  property_count: 6
  slug: palo-alto-networks-prisma-access-location
- name: profile-input
  property_count: 7
  slug: palo-alto-networks-profile-input
- name: profile-item
  property_count: 1
  slug: palo-alto-networks-profile-item
- name: profiles
  property_count: 4
  slug: palo-alto-networks-profiles
- name: RdsRepoInfo_2
  property_count: 43
  slug: palo-alto-networks-rds-repo-info-2
- name: RdsRepoInfo
  property_count: 29
  slug: palo-alto-networks-rds-repo-info
- name: RegistryConfig
  property_count: 8
  slug: palo-alto-networks-registry-config
- name: RemediationRequest
  property_count: 1
  slug: palo-alto-networks-remediation-request
- name: RemoteNetworkRequest
  property_count: 6
  slug: palo-alto-networks-remote-network-request
- name: RemoteNetwork
  property_count: 11
  slug: palo-alto-networks-remote-network
- name: RemoteNetworksIpsecTunnelSet
  property_count: 2
  slug: palo-alto-networks-remote-networks-ipsec-tunnel-set
- name: RemoteNetworksReadResult
  property_count: 5
  slug: palo-alto-networks-remote-networks-read-result
- name: RemoteNetworksResponse
  property_count: 3
  slug: palo-alto-networks-remote-networks-response
- name: remote-networks
  property_count: 12
  slug: palo-alto-networks-remote-networks
- name: RepoInfo
  property_count: 38
  slug: palo-alto-networks-repo-info
- name: ReportGenerationConfigApiModel_2
  property_count: 17
  slug: palo-alto-networks-report-generation-config-api-model-2
- name: ReportGenerationConfigApiModel
  property_count: 17
  slug: palo-alto-networks-report-generation-config-api-model
- name: RepositoriesResponse
  property_count: 12
  slug: palo-alto-networks-repositories-response
- name: Repository_2
  property_count: 12
  slug: palo-alto-networks-repository-2
- name: Root Type for role
  property_count: 6
  slug: palo-alto-networks-role
- name: ScanReport
  property_count: 9
  slug: palo-alto-networks-scan-report
- name: ScanRequest
  property_count: 3
  slug: palo-alto-networks-scan-request
- name: ScanResponse
  property_count: 8
  slug: palo-alto-networks-scan-response
- name: Scan
  property_count: 12
  slug: palo-alto-networks-scan
- name: ScanStatus
  property_count: 8
  slug: palo-alto-networks-scan-status
- name: ScopeConfig
  property_count: 6
  slug: palo-alto-networks-scope-config
- name: SeamlessLoginResponse
  property_count: 2
  slug: palo-alto-networks-seamless-login-response
- name: SearchResult
  property_count: 3
  slug: palo-alto-networks-search-result
- name: SecurityRule
  property_count: 17
  slug: palo-alto-networks-security-rule
- name: services
  property_count: 5
  slug: palo-alto-networks-services
- name: SetAssetCriticalityRequest
  property_count: 2
  slug: palo-alto-networks-set-asset-criticality-request
- name: SettingsEntry
  property_count: 2
  slug: palo-alto-networks-settings-entry
- name: shared.AppEmbeddedEmbedRequest
  property_count: 5
  slug: palo-alto-networks-shared-app-embedded-embed-request
- name: -_shared.AppEmbeddedRuntimeProfile
  property_count: 0
  slug: palo-alto-networks-shared-app-embedded-runtime-profile
- name: -_shared.ContainerScanResult
  property_count: 0
  slug: palo-alto-networks-shared-container-scan-result
- name: shared.DefenderInstallBundle
  property_count: 2
  slug: palo-alto-networks-shared-defender-install-bundle
- name: -_shared.HostInfo
  property_count: 0
  slug: palo-alto-networks-shared-host-info
- name: -_shared.ImageScanResult
  property_count: 0
  slug: palo-alto-networks-shared-image-scan-result
- name: shared.License
  property_count: 11
  slug: palo-alto-networks-shared-license
- name: -_shared.RegistryScanProgress
  property_count: 0
  slug: palo-alto-networks-shared-registry-scan-progress
- name: shared.RegistryScanRequest
  property_count: 5
  slug: palo-alto-networks-shared-registry-scan-request
- name: shared.RegistrySpecification
  property_count: 26
  slug: palo-alto-networks-shared-registry-specification
- name: shared.ScanSettings
  property_count: 15
  slug: palo-alto-networks-shared-scan-settings
- name: shared.ServerlessLayerBundleRequest
  property_count: 4
  slug: palo-alto-networks-shared-serverless-layer-bundle-request
- name: Site
  property_count: 10
  slug: palo-alto-networks-site
- name: site_with_claims
  property_count: 2
  slug: palo-alto-networks-site-with-claims
- name: SortOrder
  property_count: 2
  slug: palo-alto-networks-sort-order
- name: StackMappingPlanTypesListResponse
  property_count: 2
  slug: palo-alto-networks-stack-mapping-plan-types-list-response
- name: StaticJobReportSchema
  property_count: 9
  slug: palo-alto-networks-static-job-report-schema
- name: StreamDetailResponseSchema
  property_count: 21
  slug: palo-alto-networks-stream-detail-response-schema
- name: -_string
  property_count: 0
  slug: palo-alto-networks-string
- name: SubmitActionsRequest
  property_count: 6
  slug: palo-alto-networks-submit-actions-request
- name: SuppressionCreate
  property_count: 0
  slug: palo-alto-networks-suppression-create
- name: Suppression
  property_count: 9
  slug: palo-alto-networks-suppression
- name: SuppressionsJustifications
  property_count: 1
  slug: palo-alto-networks-suppressions-justifications
- name: TenantGroupPolicyGroupMapRequest
  property_count: 1
  slug: palo-alto-networks-tenant-group-policy-group-map-request
- name: TenantGroupPolicyGroupMappingsResponse
  property_count: 1
  slug: palo-alto-networks-tenant-group-policy-group-mappings-response
- name: TenantGroupResponse
  property_count: 5
  slug: palo-alto-networks-tenant-group-response
- name: TenantGroupsResponse
  property_count: 2
  slug: palo-alto-networks-tenant-groups-response
- name: ThroughputRequest
  property_count: 3
  slug: palo-alto-networks-throughput-request
- name: Ticket
  property_count: 12
  slug: palo-alto-networks-ticket
- name: TokenRefreshResponse
  property_count: 1
  slug: palo-alto-networks-token-refresh-response
- name: TrendRequest
  property_count: 3
  slug: palo-alto-networks-trend-request
- name: tunnel-profiles
  property_count: 8
  slug: palo-alto-networks-tunnel-profiles
- name: types.ComplianceStats
  property_count: 5
  slug: palo-alto-networks-types-compliance-stats
- name: types.EventStats
  property_count: 20
  slug: palo-alto-networks-types-event-stats
- name: types.ImageScanOptions
  property_count: 2
  slug: palo-alto-networks-types-image-scan-options
- name: types.LicenseStats
  property_count: 15
  slug: palo-alto-networks-types-license-stats
- name: types.RegistryWebhookRequest
  property_count: 5
  slug: palo-alto-networks-types-registry-webhook-request
- name: types.Trends
  property_count: 3
  slug: palo-alto-networks-types-trends
- name: types.VulnImpactedResources
  property_count: 9
  slug: palo-alto-networks-types-vuln-impacted-resources
- name: UpdateManagedTenantRequest
  property_count: 4
  slug: palo-alto-networks-update-managed-tenant-request
- name: updateRepositoriesBody
  property_count: 3
  slug: palo-alto-networks-update-repositories-body
- name: update_site_request
  property_count: 3
  slug: palo-alto-networks-update-site-request
- name: UpdateTenantGroupRequest
  property_count: 2
  slug: palo-alto-networks-update-tenant-group-request
- name: UsageReport
  property_count: 7
  slug: palo-alto-networks-usage-report
- name: User_2
  property_count: 6
  slug: palo-alto-networks-user-2
- name: UserAccessKeyDetailResponseModel
  property_count: 10
  slug: palo-alto-networks-user-access-key-detail-response-model
- name: UserAccessKeyRequestModel
  property_count: 3
  slug: palo-alto-networks-user-access-key-request-model
- name: UserAccessKeyResponseModel
  property_count: 3
  slug: palo-alto-networks-user-access-key-response-model
- name: UserActivity
  property_count: 8
  slug: palo-alto-networks-user-activity
- name: User
  property_count: 12
  slug: palo-alto-networks-user
- name: ValidateTokenRequest
  property_count: 1
  slug: palo-alto-networks-validate-token-request
- name: ValidateTokenResponse
  property_count: 1
  slug: palo-alto-networks-validate-token-response
- name: VlanAttachmentRequest
  property_count: 12
  slug: palo-alto-networks-vlan-attachment-request
- name: ZTNAApplicationRequest
  property_count: 7
  slug: palo-alto-networks-ztnaapplication-request
- name: ZTNAApplication
  property_count: 9
  slug: palo-alto-networks-ztnaapplication
- name: Palo Alto Networks Security Advisory
  property_count: 3
  slug: palo-alto-security-advisory
- name: AddressGroup
  property_count: 5
  slug: pan-os-rest-api-address-group
- name: Address
  property_count: 7
  slug: pan-os-rest-api-address
- name: CommitStatus
  property_count: 3
  slug: pan-os-rest-api-commit-status
- name: NatRule
  property_count: 12
  slug: pan-os-rest-api-nat-rule
- name: PanOsResponse
  property_count: 3
  slug: pan-os-rest-api-pan-os-response
- name: QosRule
  property_count: 11
  slug: pan-os-rest-api-qos-rule
- name: SecurityRule
  property_count: 17
  slug: pan-os-rest-api-security-rule
- name: ServiceGroup
  property_count: 3
  slug: pan-os-rest-api-service-group
- name: Service
  property_count: 4
  slug: pan-os-rest-api-service
- name: Tag
  property_count: 3
  slug: pan-os-rest-api-tag
- name: VirtualSystem
  property_count: 3
  slug: pan-os-rest-api-virtual-system
- name: PAN-OS Security Rule
  property_count: 20
  slug: pan-os-security-rule
- name: IKEGateway
  property_count: 8
  slug: prisma-access-api-ike-gateway
- name: IPSecTunnel
  property_count: 6
  slug: prisma-access-api-ip-sec-tunnel
- name: JobStatus
  property_count: 8
  slug: prisma-access-api-job-status
- name: MobileAgentInfrastructureSettings
  property_count: 6
  slug: prisma-access-api-mobile-agent-infrastructure-settings
- name: RemoteNetwork
  property_count: 8
  slug: prisma-access-api-remote-network
- name: SecurityRule
  property_count: 18
  slug: prisma-access-api-security-rule
- name: ServiceConnection
  property_count: 8
  slug: prisma-access-api-service-connection
- name: BrowserDeploymentRequest
  property_count: 5
  slug: prisma-access-browser-api-browser-deployment-request
- name: BrowserDeployment
  property_count: 8
  slug: prisma-access-browser-api-browser-deployment
- name: BrowserPolicyRequest
  property_count: 7
  slug: prisma-access-browser-api-browser-policy-request
- name: BrowserPolicy
  property_count: 10
  slug: prisma-access-browser-api-browser-policy
- name: BrowserSession
  property_count: 9
  slug: prisma-access-browser-api-browser-session
- name: BrowserUser
  property_count: 6
  slug: prisma-access-browser-api-browser-user
- name: ManagedDevice
  property_count: 7
  slug: prisma-access-browser-api-managed-device
- name: UsageReport
  property_count: 7
  slug: prisma-access-browser-api-usage-report
- name: CustomQuery
  property_count: 2
  slug: prisma-access-insights-api-custom-query
- name: DataResourceQuery
  property_count: 5
  slug: prisma-access-insights-api-data-resource-query
- name: DataResourceResponse
  property_count: 4
  slug: prisma-access-insights-api-data-resource-response
- name: ExportJobResponse
  property_count: 3
  slug: prisma-access-insights-api-export-job-response
- name: ExportJobStatus
  property_count: 5
  slug: prisma-access-insights-api-export-job-status
- name: QueryFilter
  property_count: 2
  slug: prisma-access-insights-api-query-filter
- name: TimeRange
  property_count: 3
  slug: prisma-access-insights-api-time-range
- name: AttackCategory
  property_count: 6
  slug: prisma-airs-ai-red-teaming-api-attack-category
- name: ScanReport
  property_count: 9
  slug: prisma-airs-ai-red-teaming-api-scan-report
- name: ScanRequest
  property_count: 4
  slug: prisma-airs-ai-red-teaming-api-scan-request
- name: Scan
  property_count: 12
  slug: prisma-airs-ai-red-teaming-api-scan
- name: ScanTargetRequest
  property_count: 7
  slug: prisma-airs-ai-red-teaming-api-scan-target-request
- name: ScanTarget
  property_count: 8
  slug: prisma-airs-ai-red-teaming-api-scan-target
- name: VulnerabilityFinding
  property_count: 9
  slug: prisma-airs-ai-red-teaming-api-vulnerability-finding
- name: AIProfile
  property_count: 6
  slug: prisma-airs-api-ai-profile
- name: ContentScanResult
  property_count: 4
  slug: prisma-airs-api-content-scan-result
- name: ScanContent
  property_count: 2
  slug: prisma-airs-api-scan-content
- name: ScanRequest
  property_count: 3
  slug: prisma-airs-api-scan-request
- name: ScanResponse
  property_count: 8
  slug: prisma-airs-api-scan-response
- name: CodeError
  property_count: 15
  slug: prisma-cloud-code-security-api-code-error
- name: Fix
  property_count: 12
  slug: prisma-cloud-code-security-api-fix
- name: Repository
  property_count: 12
  slug: prisma-cloud-code-security-api-repository
- name: ScanIntegration
  property_count: 6
  slug: prisma-cloud-code-security-api-scan-integration
- name: ScanStatus
  property_count: 8
  slug: prisma-cloud-code-security-api-scan-status
- name: Suppression
  property_count: 9
  slug: prisma-cloud-code-security-api-suppression
- name: CIScan
  property_count: 5
  slug: prisma-cloud-compute-api-ci-scan
- name: ComplianceIssue
  property_count: 5
  slug: prisma-cloud-compute-api-compliance-issue
- name: CompliancePolicy
  property_count: 1
  slug: prisma-cloud-compute-api-compliance-policy
- name: Container
  property_count: 11
  slug: prisma-cloud-compute-api-container
- name: Defender
  property_count: 8
  slug: prisma-cloud-compute-api-defender
- name: DefenderSummary
  property_count: 5
  slug: prisma-cloud-compute-api-defender-summary
- name: Host
  property_count: 12
  slug: prisma-cloud-compute-api-host
- name: Image
  property_count: 13
  slug: prisma-cloud-compute-api-image
- name: RegistryConfig
  property_count: 8
  slug: prisma-cloud-compute-api-registry-config
- name: RuntimePolicy
  property_count: 1
  slug: prisma-cloud-compute-api-runtime-policy
- name: VulnerabilityPolicy
  property_count: 1
  slug: prisma-cloud-compute-api-vulnerability-policy
- name: Vulnerability
  property_count: 10
  slug: prisma-cloud-compute-api-vulnerability
- name: AlertFilter
  property_count: 3
  slug: prisma-cloud-cspm-api-alert-filter
- name: Alert
  property_count: 9
  slug: prisma-cloud-cspm-api-alert
- name: CloudAccount
  property_count: 6
  slug: prisma-cloud-cspm-api-cloud-account
- name: ComplianceStandard
  property_count: 8
  slug: prisma-cloud-cspm-api-compliance-standard
- name: PolicyInput
  property_count: 8
  slug: prisma-cloud-cspm-api-policy-input
- name: Policy
  property_count: 11
  slug: prisma-cloud-cspm-api-policy
- name: Report
  property_count: 7
  slug: prisma-cloud-cspm-api-report
- name: SearchResult
  property_count: 3
  slug: prisma-cloud-cspm-api-search-result
- name: TimeRange
  property_count: 2
  slug: prisma-cloud-cspm-api-time-range
- name: Classification
  property_count: 9
  slug: prisma-cloud-dspm-api-classification
- name: DataAsset
  property_count: 12
  slug: prisma-cloud-dspm-api-data-asset
- name: DataRisk
  property_count: 16
  slug: prisma-cloud-dspm-api-data-risk
- name: DataSecurityAlert
  property_count: 14
  slug: prisma-cloud-dspm-api-data-security-alert
- name: DataStore
  property_count: 15
  slug: prisma-cloud-dspm-api-data-store
- name: DSPMPolicy
  property_count: 10
  slug: prisma-cloud-dspm-api-dspm-policy
- name: ChangePasswordRequest
  property_count: 1
  slug: prisma-cloud-mssp-api-change-password-request
- name: ContactInfo
  property_count: 3
  slug: prisma-cloud-mssp-api-contact-info
- name: CreateManagedTenantRequest
  property_count: 8
  slug: prisma-cloud-mssp-api-create-managed-tenant-request
- name: CreateMsspRequest
  property_count: 4
  slug: prisma-cloud-mssp-api-create-mssp-request
- name: CreatePolicyGroupResponse
  property_count: 3
  slug: prisma-cloud-mssp-api-create-policy-group-response
- name: CreateTenantGroupRequest
  property_count: 2
  slug: prisma-cloud-mssp-api-create-tenant-group-request
- name: FormLoginRequest
  property_count: 2
  slug: prisma-cloud-mssp-api-form-login-request
- name: FormLoginResponse
  property_count: 3
  slug: prisma-cloud-mssp-api-form-login-response
- name: JwkResponse
  property_count: 6
  slug: prisma-cloud-mssp-api-jwk-response
- name: JwksResponse
  property_count: 1
  slug: prisma-cloud-mssp-api-jwks-response
- name: LicenseInfo
  property_count: 2
  slug: prisma-cloud-mssp-api-license-info
- name: LicensePoolInfo
  property_count: 9
  slug: prisma-cloud-mssp-api-license-pool-info
- name: ManagedTenantDetailedResponse
  property_count: 20
  slug: prisma-cloud-mssp-api-managed-tenant-detailed-response
- name: ManagedTenantLicenseResponse
  property_count: 6
  slug: prisma-cloud-mssp-api-managed-tenant-license-response
- name: ManagedTenantResponse
  property_count: 19
  slug: prisma-cloud-mssp-api-managed-tenant-response
- name: ManagedTenantsResponse
  property_count: 2
  slug: prisma-cloud-mssp-api-managed-tenants-response
- name: ModuleInfoRequest
  property_count: 3
  slug: prisma-cloud-mssp-api-module-info-request
- name: ModuleInfo
  property_count: 5
  slug: prisma-cloud-mssp-api-module-info
- name: MsspLicenseInfoResponse
  property_count: 7
  slug: prisma-cloud-mssp-api-mssp-license-info-response
- name: MsspLicensePoolRequest
  property_count: 5
  slug: prisma-cloud-mssp-api-mssp-license-pool-request
- name: MsspLicensePoolResponse
  property_count: 9
  slug: prisma-cloud-mssp-api-mssp-license-pool-response
- name: MsspLicensePoolsResponse
  property_count: 2
  slug: prisma-cloud-mssp-api-mssp-license-pools-response
- name: MsspLicenseUsageRequestObject
  property_count: 4
  slug: prisma-cloud-mssp-api-mssp-license-usage-request-object
- name: MsspLicenseUsageResponse
  property_count: 2
  slug: prisma-cloud-mssp-api-mssp-license-usage-response
- name: MsspListUserResponse
  property_count: 2
  slug: prisma-cloud-mssp-api-mssp-list-user-response
- name: MsspResponse
  property_count: 6
  slug: prisma-cloud-mssp-api-mssp-response
- name: MsspUserRequest
  property_count: 3
  slug: prisma-cloud-mssp-api-mssp-user-request
- name: MsspUserResponse
  property_count: 5
  slug: prisma-cloud-mssp-api-mssp-user-response
- name: OperationAckRequest
  property_count: 3
  slug: prisma-cloud-mssp-api-operation-ack-request
- name: OperationResponse
  property_count: 13
  slug: prisma-cloud-mssp-api-operation-response
- name: OperationsResponse
  property_count: 2
  slug: prisma-cloud-mssp-api-operations-response
- name: PolicyGroupInfo
  property_count: 3
  slug: prisma-cloud-mssp-api-policy-group-info
- name: PolicyGroupListResponse
  property_count: 4
  slug: prisma-cloud-mssp-api-policy-group-list-response
- name: PolicyGroupRequest
  property_count: 2
  slug: prisma-cloud-mssp-api-policy-group-request
- name: PolicyGroupResponse
  property_count: 4
  slug: prisma-cloud-mssp-api-policy-group-response
- name: PolicyGroupsListResponse
  property_count: 2
  slug: prisma-cloud-mssp-api-policy-groups-list-response
- name: RecurString
  property_count: 2
  slug: prisma-cloud-mssp-api-recur-string
- name: RelativeTimeDuration
  property_count: 2
  slug: prisma-cloud-mssp-api-relative-time-duration
- name: RelativeTimeRangeConfig
  property_count: 4
  slug: prisma-cloud-mssp-api-relative-time-range-config
- name: ScheduleTaskRequest
  property_count: 2
  slug: prisma-cloud-mssp-api-schedule-task-request
- name: SeamlessLoginResponse
  property_count: 2
  slug: prisma-cloud-mssp-api-seamless-login-response
- name: StackMappingPlanTypesListResponse
  property_count: 2
  slug: prisma-cloud-mssp-api-stack-mapping-plan-types-list-response
- name: StackMappingResponse
  property_count: 3
  slug: prisma-cloud-mssp-api-stack-mapping-response
- name: Task
  property_count: 9
  slug: prisma-cloud-mssp-api-task
- name: TenantChangeResponse
  property_count: 5
  slug: prisma-cloud-mssp-api-tenant-change-response
- name: TenantGroupLicenseInfo
  property_count: 4
  slug: prisma-cloud-mssp-api-tenant-group-license-info
- name: TenantGroupMappingDetails
  property_count: 4
  slug: prisma-cloud-mssp-api-tenant-group-mapping-details
- name: TenantGroupPolicyGroupMapRequest
  property_count: 1
  slug: prisma-cloud-mssp-api-tenant-group-policy-group-map-request
- name: TenantGroupPolicyGroupMappingResponse
  property_count: 3
  slug: prisma-cloud-mssp-api-tenant-group-policy-group-mapping-response
- name: TenantGroupPolicyGroupMapping
  property_count: 2
  slug: prisma-cloud-mssp-api-tenant-group-policy-group-mapping
- name: TenantGroupPolicyGroupMappingsResponse
  property_count: 1
  slug: prisma-cloud-mssp-api-tenant-group-policy-group-mappings-response
- name: TenantGroupResponse
  property_count: 5
  slug: prisma-cloud-mssp-api-tenant-group-response
- name: TenantGroupsResponse
  property_count: 2
  slug: prisma-cloud-mssp-api-tenant-groups-response
- name: TenantIds
  property_count: 2
  slug: prisma-cloud-mssp-api-tenant-ids
- name: TenantLicenseUsage
  property_count: 9
  slug: prisma-cloud-mssp-api-tenant-license-usage
- name: TenantUpdate
  property_count: 4
  slug: prisma-cloud-mssp-api-tenant-update
- name: TimeRangeConfigObject
  property_count: 3
  slug: prisma-cloud-mssp-api-time-range-config-object
- name: ToNowTimeRangeConfig
  property_count: 4
  slug: prisma-cloud-mssp-api-to-now-time-range-config
- name: TokenRefreshResponse
  property_count: 1
  slug: prisma-cloud-mssp-api-token-refresh-response
- name: UpdateManagedTenantRequest
  property_count: 4
  slug: prisma-cloud-mssp-api-update-managed-tenant-request
- name: UpdateMsspRequest
  property_count: 2
  slug: prisma-cloud-mssp-api-update-mssp-request
- name: UpdateTenantGroupRequest
  property_count: 2
  slug: prisma-cloud-mssp-api-update-tenant-group-request
- name: V1Response
  property_count: 0
  slug: prisma-cloud-mssp-api-v1-response
- name: ValidateTokenRequest
  property_count: 1
  slug: prisma-cloud-mssp-api-validate-token-request
- name: ValidateTokenResponse
  property_count: 1
  slug: prisma-cloud-mssp-api-validate-token-response
- name: Prisma Cloud Policy
  property_count: 18
  slug: prisma-cloud-policy
- name: AlertPayload
  property_count: 11
  slug: prisma-cloud-webhooks-alert-payload
- name: Alarm
  property_count: 12
  slug: prisma-sd-wan-api-alarm
- name: ApplicationUsage
  property_count: 7
  slug: prisma-sd-wan-api-application-usage
- name: LANNetwork
  property_count: 9
  slug: prisma-sd-wan-api-lan-network
- name: PathRule
  property_count: 10
  slug: prisma-sd-wan-api-path-rule
- name: QoSRule
  property_count: 11
  slug: prisma-sd-wan-api-qo-s-rule
- name: SiteMetric
  property_count: 7
  slug: prisma-sd-wan-api-site-metric
- name: Site
  property_count: 10
  slug: prisma-sd-wan-api-site
- name: WANInterface
  property_count: 12
  slug: prisma-sd-wan-api-wan-interface
- name: Application
  property_count: 7
  slug: saas-security-api-application
- name: Asset
  property_count: 12
  slug: saas-security-api-asset
- name: Incident
  property_count: 13
  slug: saas-security-api-incident
- name: LogForwardingSettings
  property_count: 2
  slug: saas-security-api-log-forwarding-settings
- name: UserActivity
  property_count: 8
  slug: saas-security-api-user-activity
- name: User
  property_count: 6
  slug: saas-security-api-user
- name: NetworkSliceRequest
  property_count: 5
  slug: sase-5g-api-network-slice-request
- name: NetworkSlice
  property_count: 10
  slug: sase-5g-api-network-slice
- name: SecurityMetrics5G
  property_count: 8
  slug: sase-5g-api-security-metrics5-g
- name: SecurityPolicy5GRequest
  property_count: 8
  slug: sase-5g-api-security-policy5-g-request
- name: SecurityPolicy5G
  property_count: 11
  slug: sase-5g-api-security-policy5-g
- name: Tenant5GRequest
  property_count: 4
  slug: sase-5g-api-tenant5-g-request
- name: Tenant5G
  property_count: 7
  slug: sase-5g-api-tenant5-g
- name: CountFilterRequest
  property_count: 1
  slug: sase-5g-monitor-api-count-filter-request
- name: IncidentsCountRequest
  property_count: 2
  slug: sase-5g-monitor-api-incidents-count-request
- name: MappingRequest
  property_count: 5
  slug: sase-5g-monitor-api-mapping-request
- name: ThroughputRequest
  property_count: 3
  slug: sase-5g-monitor-api-throughput-request
- name: TrendRequest
  property_count: 3
  slug: sase-5g-monitor-api-trend-request
- name: AggregationQuery
  property_count: 7
  slug: sase-aggregate-monitoring-api-aggregation-query
- name: AggregationResponse
  property_count: 5
  slug: sase-aggregate-monitoring-api-aggregation-response
- name: TenantSummary
  property_count: 5
  slug: sase-aggregate-monitoring-api-tenant-summary
- name: BandwidthAllocation
  property_count: 5
  slug: sase-config-orchestration-api-bandwidth-allocation
- name: IPsecTunnel
  property_count: 3
  slug: sase-config-orchestration-api-i-psec-tunnel
- name: IKEGatewayConfig
  property_count: 5
  slug: sase-config-orchestration-api-ike-gateway-config
- name: IKEGateway
  property_count: 5
  slug: sase-config-orchestration-api-ike-gateway
- name: OnboardingStatus
  property_count: 6
  slug: sase-config-orchestration-api-onboarding-status
- name: PrismaAccessLocation
  property_count: 6
  slug: sase-config-orchestration-api-prisma-access-location
- name: RemoteNetworkRequest
  property_count: 6
  slug: sase-config-orchestration-api-remote-network-request
- name: RemoteNetwork
  property_count: 11
  slug: sase-config-orchestration-api-remote-network
- name: AccessPolicyRequest
  property_count: 4
  slug: sase-iam-api-access-policy-request
- name: AccessPolicy
  property_count: 7
  slug: sase-iam-api-access-policy
- name: Role
  property_count: 5
  slug: sase-iam-api-role
- name: ServiceAccountCredentials
  property_count: 6
  slug: sase-iam-api-service-account-credentials
- name: ServiceAccountRequest
  property_count: 4
  slug: sase-iam-api-service-account-request
- name: ServiceAccount
  property_count: 8
  slug: sase-iam-api-service-account
- name: ServiceAccountUpdate
  property_count: 2
  slug: sase-iam-api-service-account-update
- name: Bandwidth
  property_count: 0
  slug: sase-multitenant-interconnect-api-bandwidth
- name: CloudProvider
  property_count: 0
  slug: sase-multitenant-interconnect-api-cloud-provider
- name: ConnectionType
  property_count: 0
  slug: sase-multitenant-interconnect-api-connection-type
- name: DedicatedVlanAttachmentDetailsEntry
  property_count: 2
  slug: sase-multitenant-interconnect-api-dedicated-vlan-attachment-details-entry
- name: InterconnectRequest
  property_count: 11
  slug: sase-multitenant-interconnect-api-interconnect-request
- name: InterconnectUsage
  property_count: 0
  slug: sase-multitenant-interconnect-api-interconnect-usage
- name: IPBlockEntry
  property_count: 3
  slug: sase-multitenant-interconnect-api-ip-block-entry
- name: IPBlockType
  property_count: 0
  slug: sase-multitenant-interconnect-api-ip-block-type
- name: IPPoolRequest
  property_count: 2
  slug: sase-multitenant-interconnect-api-ip-pool-request
- name: IPProvider
  property_count: 0
  slug: sase-multitenant-interconnect-api-ip-provider
- name: PhysicalConnectionEntry
  property_count: 7
  slug: sase-multitenant-interconnect-api-physical-connection-entry
- name: PhysicalInterconnectLinkType
  property_count: 0
  slug: sase-multitenant-interconnect-api-physical-interconnect-link-type
- name: SessionInitializationMode
  property_count: 0
  slug: sase-multitenant-interconnect-api-session-initialization-mode
- name: SettingsEntry
  property_count: 2
  slug: sase-multitenant-interconnect-api-settings-entry
- name: StackType
  property_count: 0
  slug: sase-multitenant-interconnect-api-stack-type
- name: VlanAttachmentCustomIpAddress
  property_count: 2
  slug: sase-multitenant-interconnect-api-vlan-attachment-custom-ip-address
- name: VlanAttachmentRequest
  property_count: 12
  slug: sase-multitenant-interconnect-api-vlan-attachment-request
- name: EmailChannelDetails
  property_count: 1
  slug: sase-multitenant-notifications-api-email-channel-details
- name: EmailDetails
  property_count: 2
  slug: sase-multitenant-notifications-api-email-details
- name: MtNotifAggKey
  property_count: 5
  slug: sase-multitenant-notifications-api-mt-notif-agg-key
- name: MtNotificationList
  property_count: 0
  slug: sase-multitenant-notifications-api-mt-notification-list
- name: MtNotification
  property_count: 11
  slug: sase-multitenant-notifications-api-mt-notification
- name: NotifCategoryDetail
  property_count: 3
  slug: sase-multitenant-notifications-api-notif-category-detail
- name: NotifChannel
  property_count: 5
  slug: sase-multitenant-notifications-api-notif-channel
- name: NotifFilter
  property_count: 2
  slug: sase-multitenant-notifications-api-notif-filter
- name: NotifListApiReqBody
  property_count: 3
  slug: sase-multitenant-notifications-api-notif-list-api-req-body
- name: NotifProfileList
  property_count: 0
  slug: sase-multitenant-notifications-api-notif-profile-list
- name: NotifProfile
  property_count: 11
  slug: sase-multitenant-notifications-api-notif-profile
- name: NotifReadState
  property_count: 0
  slug: sase-multitenant-notifications-api-notif-read-state
- name: NotifStateChangeApiBody
  property_count: 2
  slug: sase-multitenant-notifications-api-notif-state-change-api-body
- name: NotifSubCategoryDetail
  property_count: 3
  slug: sase-multitenant-notifications-api-notif-sub-category-detail
- name: NotifTypeDetail
  property_count: 2
  slug: sase-multitenant-notifications-api-notif-type-detail
- name: SortBy
  property_count: 2
  slug: sase-multitenant-notifications-api-sort-by
- name: WebhookChannelDetails
  property_count: 3
  slug: sase-multitenant-notifications-api-webhook-channel-details
- name: AnnouncementNotification
  property_count: 9
  slug: sase-notifications-announcement-notification
- name: CertificateExpiryNotification
  property_count: 11
  slug: sase-notifications-certificate-expiry-notification
- name: DataplaneUpgradeNotification
  property_count: 10
  slug: sase-notifications-dataplane-upgrade-notification
- name: IncidentDetail
  property_count: 9
  slug: sase-notifications-incident-detail
- name: IncidentNotification
  property_count: 10
  slug: sase-notifications-incident-notification
- name: ServiceInfo
  property_count: 3
  slug: sase-notifications-service-info
- name: TenantContext
  property_count: 3
  slug: sase-notifications-tenant-context
- name: AllocationEntry
  property_count: 4
  slug: sase-subscription-api-allocation-entry
- name: AllocationRequest
  property_count: 1
  slug: sase-subscription-api-allocation-request
- name: Entitlement
  property_count: 5
  slug: sase-subscription-api-entitlement
- name: SubscriptionEntitlements
  property_count: 4
  slug: sase-subscription-api-subscription-entitlements
- name: Subscription
  property_count: 11
  slug: sase-subscription-api-subscription
- name: TenantServiceGroupRequest
  property_count: 6
  slug: sase-tenancy-api-tenant-service-group-request
- name: TenantServiceGroup
  property_count: 11
  slug: sase-tenancy-api-tenant-service-group
- name: TenantServiceGroupUpdate
  property_count: 3
  slug: sase-tenancy-api-tenant-service-group-update
- name: Advisory
  property_count: 15
  slug: security-advisory-api-advisory
- name: AffectedProduct
  property_count: 2
  slug: security-advisory-api-affected-product
- name: Product
  property_count: 2
  slug: security-advisory-api-product
- name: CatalogApp
  property_count: 6
  slug: sspm-api-catalog-app
- name: JiraIntegrationRequest
  property_count: 7
  slug: sspm-api-jira-integration-request
- name: JiraIntegration
  property_count: 7
  slug: sspm-api-jira-integration
- name: OnboardAppRequest
  property_count: 3
  slug: sspm-api-onboard-app-request
- name: OnboardedApp
  property_count: 8
  slug: sspm-api-onboarded-app
- name: PostureCheck
  property_count: 11
  slug: sspm-api-posture-check
- name: AddressGroupList
  property_count: 4
  slug: strata-cloud-manager-api-address-group-list
- name: AddressGroupRequest
  property_count: 5
  slug: strata-cloud-manager-api-address-group-request
- name: AddressGroup
  property_count: 7
  slug: strata-cloud-manager-api-address-group
- name: AddressList
  property_count: 4
  slug: strata-cloud-manager-api-address-list
- name: AddressRequest
  property_count: 7
  slug: strata-cloud-manager-api-address-request
- name: Address
  property_count: 10
  slug: strata-cloud-manager-api-address
- name: DeleteResponse
  property_count: 1
  slug: strata-cloud-manager-api-delete-response
- name: Job
  property_count: 8
  slug: strata-cloud-manager-api-job
- name: NatRuleList
  property_count: 4
  slug: strata-cloud-manager-api-nat-rule-list
- name: NatRuleRequest
  property_count: 11
  slug: strata-cloud-manager-api-nat-rule-request
- name: NatRule
  property_count: 15
  slug: strata-cloud-manager-api-nat-rule
- name: SecurityRuleList
  property_count: 4
  slug: strata-cloud-manager-api-security-rule-list
- name: SecurityRuleRequest
  property_count: 15
  slug: strata-cloud-manager-api-security-rule-request
- name: SecurityRule
  property_count: 18
  slug: strata-cloud-manager-api-security-rule
- name: ServiceList
  property_count: 4
  slug: strata-cloud-manager-api-service-list
- name: ServiceRequest
  property_count: 4
  slug: strata-cloud-manager-api-service-request
- name: Service
  property_count: 6
  slug: strata-cloud-manager-api-service
- name: AuthLogPayload
  property_count: 17
  slug: strata-logging-forwarding-auth-log-payload
- name: ThreatLogPayload
  property_count: 24
  slug: strata-logging-forwarding-threat-log-payload
- name: TrafficLogPayload
  property_count: 30
  slug: strata-logging-forwarding-traffic-log-payload
- name: UrlLogPayload
  property_count: 19
  slug: strata-logging-forwarding-url-log-payload
- name: WildfireLogPayload
  property_count: 19
  slug: strata-logging-forwarding-wildfire-log-payload
- name: EmailDestinationRequest
  property_count: 6
  slug: strata-logging-service-api-email-destination-request
- name: EmailDestination
  property_count: 8
  slug: strata-logging-service-api-email-destination
- name: ForwardingStatus
  property_count: 3
  slug: strata-logging-service-api-forwarding-status
- name: HTTPSDestinationRequest
  property_count: 6
  slug: strata-logging-service-api-https-destination-request
- name: HTTPSDestination
  property_count: 7
  slug: strata-logging-service-api-https-destination
- name: LogForwardingProfileRequest
  property_count: 4
  slug: strata-logging-service-api-log-forwarding-profile-request
- name: LogForwardingProfile
  property_count: 8
  slug: strata-logging-service-api-log-forwarding-profile
- name: SyslogDestinationRequest
  property_count: 7
  slug: strata-logging-service-api-syslog-destination-request
- name: SyslogDestination
  property_count: 9
  slug: strata-logging-service-api-syslog-destination
- name: ApiStats
  property_count: 2
  slug: threat-vault-api-api-stats
- name: AtpReportList
  property_count: 5
  slug: threat-vault-api-atp-report-list
- name: AtpReport
  property_count: 6
  slug: threat-vault-api-atp-report
- name: ReleaseNote
  property_count: 7
  slug: threat-vault-api-release-note
- name: ReleaseNotesList
  property_count: 5
  slug: threat-vault-api-release-notes-list
- name: ThreatHistoryEntry
  property_count: 5
  slug: threat-vault-api-threat-history-entry
- name: ThreatHistoryList
  property_count: 5
  slug: threat-vault-api-threat-history-list
- name: ThreatList
  property_count: 6
  slug: threat-vault-api-threat-list
- name: ThreatSignature
  property_count: 16
  slug: threat-vault-api-threat-signature
- name: AnalysisReport
  property_count: 1
  slug: wildfire-api-analysis-report
- name: BulkVerdictResponse
  property_count: 1
  slug: wildfire-api-bulk-verdict-response
- name: SandboxReport
  property_count: 6
  slug: wildfire-api-sandbox-report
- name: SubmitResponse
  property_count: 1
  slug: wildfire-api-submit-response
- name: VerdictResponse
  property_count: 1
  slug: wildfire-api-verdict-response
- name: ConnectorGroupRequest
  property_count: 3
  slug: ztna-connector-api-connector-group-request
- name: ConnectorGroup
  property_count: 6
  slug: ztna-connector-api-connector-group
- name: ConnectorRequest
  property_count: 3
  slug: ztna-connector-api-connector-request
- name: Connector
  property_count: 10
  slug: ztna-connector-api-connector
- name: FQDNRuleRequest
  property_count: 5
  slug: ztna-connector-api-fqdn-rule-request
- name: FQDNRule
  property_count: 7
  slug: ztna-connector-api-fqdn-rule
- name: LicenseInfo
  property_count: 5
  slug: ztna-connector-api-license-info
- name: SubnetRuleRequest
  property_count: 4
  slug: ztna-connector-api-subnet-rule-request
- name: SubnetRule
  property_count: 6
  slug: ztna-connector-api-subnet-rule
- name: ZTNAApplicationRequest
  property_count: 7
  slug: ztna-connector-api-ztna-application-request
- name: ZTNAApplication
  property_count: 9
  slug: ztna-connector-api-ztna-application
json_structures:
- name: Aiops Ngfw Bpa Api Bpa Check Structure
  property_count: 10
  slug: aiops-ngfw-bpa-api-bpa-check-structure
- name: Aiops Ngfw Bpa Api Bpa Report Structure
  property_count: 10
  slug: aiops-ngfw-bpa-api-bpa-report-structure
- name: Aiops Ngfw Bpa Api Bpa Request Status Structure
  property_count: 7
  slug: aiops-ngfw-bpa-api-bpa-request-status-structure
- name: Aiops Ngfw Bpa Api Bpa Request Structure
  property_count: 3
  slug: aiops-ngfw-bpa-api-bpa-request-structure
- name: Autonomous Dem Api Agent Score Structure
  property_count: 11
  slug: autonomous-dem-api-agent-score-structure
- name: Autonomous Dem Api Application Score Structure
  property_count: 13
  slug: autonomous-dem-api-application-score-structure
- name: Autonomous Dem Api Monitored Agent Structure
  property_count: 9
  slug: autonomous-dem-api-monitored-agent-structure
- name: Autonomous Dem Api Monitored Application Structure
  property_count: 8
  slug: autonomous-dem-api-monitored-application-structure
- name: Autonomous Dem Api Performance Metric Structure
  property_count: 9
  slug: autonomous-dem-api-performance-metric-structure
- name: Autonomous Dem Api Test Result Structure
  property_count: 11
  slug: autonomous-dem-api-test-result-structure
- name: Cloud Identity Engine Api Attr_Based_Filter Structure
  property_count: 3
  slug: cloud-identity-engine-api-attr_based_filter-structure
- name: Cloud Identity Engine Api Check_Group_Membership Structure
  property_count: 1
  slug: cloud-identity-engine-api-check_group_membership-structure
- name: Cloud Identity Engine Api Check_User_In_Particular_Group Structure
  property_count: 2
  slug: cloud-identity-engine-api-check_user_in_particular_group-structure
- name: Cloud Identity Engine Api Domain_Param Structure
  property_count: 1
  slug: cloud-identity-engine-api-domain_param-structure
- name: Cloud Identity Engine Api Fetch_All_Users_Attrs Structure
  property_count: 2
  slug: cloud-identity-engine-api-fetch_all_users_attrs-structure
- name: Cloud Identity Engine Api Group_Filter Structure
  property_count: 3
  slug: cloud-identity-engine-api-group_filter-structure
- name: Cloud Identity Engine Api List_All_Groups_In_Domain Structure
  property_count: 2
  slug: cloud-identity-engine-api-list_all_groups_in_domain-structure
- name: Cloud Identity Engine Api List_All_Users_In_Domain Structure
  property_count: 2
  slug: cloud-identity-engine-api-list_all_users_in_domain-structure
- name: Cloud Identity Engine Api List_Groups_User_Belongs_To Structure
  property_count: 1
  slug: cloud-identity-engine-api-list_groups_user_belongs_to-structure
- name: Cloud Identity Engine Api List_Specific_Groups Structure
  property_count: 2
  slug: cloud-identity-engine-api-list_specific_groups-structure
- name: Cloud Identity Engine Api List_Specific_Users Structure
  property_count: 1
  slug: cloud-identity-engine-api-list_specific_users-structure
- name: Cloud Identity Engine Api List_Users_In_Particular_Group Structure
  property_count: 2
  slug: cloud-identity-engine-api-list_users_in_particular_group-structure
- name: Cloud Identity Engine Api Pagination_Params Structure
  property_count: 2
  slug: cloud-identity-engine-api-pagination_params-structure
- name: Cloud Ngfw Api Firewall Request Structure
  property_count: 2
  slug: cloud-ngfw-api-firewall-request-structure
- name: Cloud Ngfw Api Firewall Structure
  property_count: 3
  slug: cloud-ngfw-api-firewall-structure
- name: Cloud Ngfw Api Firewall Summary Structure
  property_count: 4
  slug: cloud-ngfw-api-firewall-summary-structure
- name: Cloud Ngfw Api Fqdn List Request Structure
  property_count: 2
  slug: cloud-ngfw-api-fqdn-list-request-structure
- name: Cloud Ngfw Api Fqdn List Structure
  property_count: 3
  slug: cloud-ngfw-api-fqdn-list-structure
- name: Cloud Ngfw Api Fqdn List Summary Structure
  property_count: 1
  slug: cloud-ngfw-api-fqdn-list-summary-structure
- name: Cloud Ngfw Api Prefix List Request Structure
  property_count: 2
  slug: cloud-ngfw-api-prefix-list-request-structure
- name: Cloud Ngfw Api Prefix List Structure
  property_count: 3
  slug: cloud-ngfw-api-prefix-list-structure
- name: Cloud Ngfw Api Prefix List Summary Structure
  property_count: 1
  slug: cloud-ngfw-api-prefix-list-summary-structure
- name: Cloud Ngfw Api Response Status Structure
  property_count: 2
  slug: cloud-ngfw-api-response-status-structure
- name: Cloud Ngfw Api Rule Destination Structure
  property_count: 5
  slug: cloud-ngfw-api-rule-destination-structure
- name: Cloud Ngfw Api Rule Source Structure
  property_count: 4
  slug: cloud-ngfw-api-rule-source-structure
- name: Cloud Ngfw Api Rule Stack Request Structure
  property_count: 2
  slug: cloud-ngfw-api-rule-stack-request-structure
- name: Cloud Ngfw Api Rule Stack Structure
  property_count: 3
  slug: cloud-ngfw-api-rule-stack-structure
- name: Cloud Ngfw Api Rule Stack Summary Structure
  property_count: 3
  slug: cloud-ngfw-api-rule-stack-summary-structure
- name: Cloud Ngfw Api Security Rule Request Structure
  property_count: 2
  slug: cloud-ngfw-api-security-rule-request-structure
- name: Cloud Ngfw Api Security Rule Structure
  property_count: 2
  slug: cloud-ngfw-api-security-rule-structure
- name: Cloud Ngfw Api Security Rule Summary Structure
  property_count: 3
  slug: cloud-ngfw-api-security-rule-summary-structure
- name: Cortex Xdr Api Alert Structure
  property_count: 17
  slug: cortex-xdr-api-alert-structure
- name: Cortex Xdr Api Audit Log Structure
  property_count: 9
  slug: cortex-xdr-api-audit-log-structure
- name: Cortex Xdr Api Endpoint Structure
  property_count: 20
  slug: cortex-xdr-api-endpoint-structure
- name: Cortex Xdr Api Filter Structure
  property_count: 3
  slug: cortex-xdr-api-filter-structure
- name: Cortex Xdr Api Incident Detail Structure
  property_count: 0
  slug: cortex-xdr-api-incident-detail-structure
- name: Cortex Xdr Api Incident Structure
  property_count: 21
  slug: cortex-xdr-api-incident-structure
- name: Cortex Xdr Api Sort Order Structure
  property_count: 2
  slug: cortex-xdr-api-sort-order-structure
- name: Cortex Xdr Incident Structure
  property_count: 21
  slug: cortex-xdr-incident-structure
- name: Cortex Xdr Webhooks Alert Payload Structure
  property_count: 10
  slug: cortex-xdr-webhooks-alert-payload-structure
- name: Cortex Xdr Webhooks Incident Payload Structure
  property_count: 10
  slug: cortex-xdr-webhooks-incident-payload-structure
- name: Cortex Xpanse Api Asm Incident Structure
  property_count: 14
  slug: cortex-xpanse-api-asm-incident-structure
- name: Cortex Xpanse Api Asset Internet Exposure Detail Structure
  property_count: 0
  slug: cortex-xpanse-api-asset-internet-exposure-detail-structure
- name: Cortex Xpanse Api Asset Internet Exposure Structure
  property_count: 13
  slug: cortex-xpanse-api-asset-internet-exposure-structure
- name: Cortex Xpanse Api Attack Surface Rule Structure
  property_count: 10
  slug: cortex-xpanse-api-attack-surface-rule-structure
- name: Cortex Xpanse Api Audit Log Structure
  property_count: 9
  slug: cortex-xpanse-api-audit-log-structure
- name: Cortex Xpanse Api Exposed Service Structure
  property_count: 13
  slug: cortex-xpanse-api-exposed-service-structure
- name: Cortex Xpanse Api Filter Structure
  property_count: 3
  slug: cortex-xpanse-api-filter-structure
- name: Cortex Xpanse Api Owned Ip Range Structure
  property_count: 10
  slug: cortex-xpanse-api-owned-ip-range-structure
- name: Cortex Xpanse Api Sort Order Structure
  property_count: 2
  slug: cortex-xpanse-api-sort-order-structure
- name: Cortex Xsiam Api Alert Structure
  property_count: 12
  slug: cortex-xsiam-api-alert-structure
- name: Cortex Xsiam Api Asset Structure
  property_count: 10
  slug: cortex-xsiam-api-asset-structure
- name: Cortex Xsiam Api Audit Log Structure
  property_count: 9
  slug: cortex-xsiam-api-audit-log-structure
- name: Cortex Xsiam Api Endpoint Structure
  property_count: 14
  slug: cortex-xsiam-api-endpoint-structure
- name: Cortex Xsiam Api Filter Structure
  property_count: 3
  slug: cortex-xsiam-api-filter-structure
- name: Cortex Xsiam Api Incident Structure
  property_count: 15
  slug: cortex-xsiam-api-incident-structure
- name: Cortex Xsiam Api Sort Order Structure
  property_count: 2
  slug: cortex-xsiam-api-sort-order-structure
- name: Cortex Xsiam Data Ingestion Event Data Payload Structure
  property_count: 8
  slug: cortex-xsiam-data-ingestion-event-data-payload-structure
- name: Cortex Xsiam Data Ingestion Log Data Payload Structure
  property_count: 8
  slug: cortex-xsiam-data-ingestion-log-data-payload-structure
- name: Cortex Xsiam Data Ingestion Xdr Data Payload Structure
  property_count: 8
  slug: cortex-xsiam-data-ingestion-xdr-data-payload-structure
- name: Cortex Xsoar Api Create Entry Request Structure
  property_count: 4
  slug: cortex-xsoar-api-create-entry-request-structure
- name: Cortex Xsoar Api Create Incident Request Structure
  property_count: 10
  slug: cortex-xsoar-api-create-incident-request-structure
- name: Cortex Xsoar Api Entry Structure
  property_count: 9
  slug: cortex-xsoar-api-entry-structure
- name: Cortex Xsoar Api Incident Search Request Structure
  property_count: 5
  slug: cortex-xsoar-api-incident-search-request-structure
- name: Cortex Xsoar Api Incident Search Response Structure
  property_count: 3
  slug: cortex-xsoar-api-incident-search-response-structure
- name: Cortex Xsoar Api Incident Structure
  property_count: 20
  slug: cortex-xsoar-api-incident-structure
- name: Cortex Xsoar Api Integration Instance Structure
  property_count: 8
  slug: cortex-xsoar-api-integration-instance-structure
- name: Cortex Xsoar Api Integration Structure
  property_count: 9
  slug: cortex-xsoar-api-integration-structure
- name: Cortex Xsoar Api Investigation Structure
  property_count: 9
  slug: cortex-xsoar-api-investigation-structure
- name: Cortex Xsoar Api Playbook Structure
  property_count: 8
  slug: cortex-xsoar-api-playbook-structure
- name: Cortex Xsoar Api Update Incident Request Structure
  property_count: 9
  slug: cortex-xsoar-api-update-incident-request-structure
- name: Cortex Xsoar Integration Manifest Structure
  property_count: 11
  slug: cortex-xsoar-integration-manifest-structure
- name: Dlp Api Content Snippet Structure
  property_count: 5
  slug: dlp-api-content-snippet-structure
- name: Dlp Api Data Pattern Structure
  property_count: 9
  slug: dlp-api-data-pattern-structure
- name: Dlp Api Dlp Incident Structure
  property_count: 18
  slug: dlp-api-dlp-incident-structure
- name: Dlp Api Incident Summary Structure
  property_count: 8
  slug: dlp-api-incident-summary-structure
- name: Dns Security Api Domain Detail Structure
  property_count: 10
  slug: dns-security-api-domain-detail-structure
- name: Dns Security Api Network Stats Structure
  property_count: 8
  slug: dns-security-api-network-stats-structure
- name: Email Dlp Api Email Attachment Structure
  property_count: 6
  slug: email-dlp-api-email-attachment-structure
- name: Email Dlp Api Email Dlp Incident Structure
  property_count: 15
  slug: email-dlp-api-email-dlp-incident-structure
- name: Email Dlp Api Email Recipient Structure
  property_count: 3
  slug: email-dlp-api-email-recipient-structure
- name: Identity Security Posture Management Api Create Ticket Request Structure
  property_count: 8
  slug: identity-security-posture-management-api-create-ticket-request-structure
- name: Identity Security Posture Management Api Download Csv Request Structure
  property_count: 3
  slug: identity-security-posture-management-api-download-csv-request-structure
- name: Identity Security Posture Management Api Feature State Structure
  property_count: 2
  slug: identity-security-posture-management-api-feature-state-structure
- name: Identity Security Posture Management Api Feature Structure
  property_count: 0
  slug: identity-security-posture-management-api-feature-structure
- name: Identity Security Posture Management Api Idp Info Structure
  property_count: 3
  slug: identity-security-posture-management-api-idp-info-structure
- name: Identity Security Posture Management Api Instant Structure
  property_count: 0
  slug: identity-security-posture-management-api-instant-structure
- name: Identity Security Posture Management Api List Response Idp Info Structure
  property_count: 2
  slug: identity-security-posture-management-api-list-response-idp-info-structure
- name: Identity Security Posture Management Api List Response Map String Object Structure
  property_count: 2
  slug: identity-security-posture-management-api-list-response-map-string-object-structure
- name: Identity Security Posture Management Api List Response Mfa Activity Structure
  property_count: 2
  slug: identity-security-posture-management-api-list-response-mfa-activity-structure
- name: Identity Security Posture Management Api List Response Saa S Account Structure
  property_count: 2
  slug: identity-security-posture-management-api-list-response-saa-s-account-structure
- name: Identity Security Posture Management Api List Response Saa S Activity Structure
  property_count: 2
  slug: identity-security-posture-management-api-list-response-saa-s-activity-structure
- name: Identity Security Posture Management Api List Response Saa S Instance Info Structure
  property_count: 2
  slug: identity-security-posture-management-api-list-response-saa-s-instance-info-structure
- name: Identity Security Posture Management Api List Response Ticket Structure
  property_count: 2
  slug: identity-security-posture-management-api-list-response-ticket-structure
- name: Identity Security Posture Management Api Mfa Activity Count By App Type Structure
  property_count: 3
  slug: identity-security-posture-management-api-mfa-activity-count-by-app-type-structure
- name: Identity Security Posture Management Api Mfa Activity Structure
  property_count: 18
  slug: identity-security-posture-management-api-mfa-activity-structure
- name: Identity Security Posture Management Api Remediation Request Structure
  property_count: 1
  slug: identity-security-posture-management-api-remediation-request-structure
- name: Identity Security Posture Management Api Saa S Account Structure
  property_count: 28
  slug: identity-security-posture-management-api-saa-s-account-structure
- name: Identity Security Posture Management Api Saa S Activity Structure
  property_count: 15
  slug: identity-security-posture-management-api-saa-s-activity-structure
- name: Identity Security Posture Management Api Saa S Instance Info Structure
  property_count: 3
  slug: identity-security-posture-management-api-saa-s-instance-info-structure
- name: Identity Security Posture Management Api Ticket Structure
  property_count: 12
  slug: identity-security-posture-management-api-ticket-structure
- name: Identity Security Posture Management Api Unlink Ticket Request Structure
  property_count: 3
  slug: identity-security-posture-management-api-unlink-ticket-request-structure
- name: Iot Security Api Alert Structure
  property_count: 11
  slug: iot-security-api-alert-structure
- name: Iot Security Api Asset Report Structure
  property_count: 7
  slug: iot-security-api-asset-report-structure
- name: Iot Security Api Device Structure
  property_count: 18
  slug: iot-security-api-device-structure
- name: Iot Security Api Device Tag Structure
  property_count: 5
  slug: iot-security-api-device-tag-structure
- name: Iot Security Api Policy Recommendation Structure
  property_count: 10
  slug: iot-security-api-policy-recommendation-structure
- name: Iot Security Api Vulnerability Structure
  property_count: 10
  slug: iot-security-api-vulnerability-structure
- name: Palo Alto Security Advisory Structure
  property_count: 3
  slug: palo-alto-security-advisory-structure
- name: Pan Os Rest Api Address Group Structure
  property_count: 5
  slug: pan-os-rest-api-address-group-structure
- name: Pan Os Rest Api Address Structure
  property_count: 7
  slug: pan-os-rest-api-address-structure
- name: Pan Os Rest Api Commit Status Structure
  property_count: 3
  slug: pan-os-rest-api-commit-status-structure
- name: Pan Os Rest Api Nat Rule Structure
  property_count: 12
  slug: pan-os-rest-api-nat-rule-structure
- name: Pan Os Rest Api Pan Os Response Structure
  property_count: 3
  slug: pan-os-rest-api-pan-os-response-structure
- name: Pan Os Rest Api Qos Rule Structure
  property_count: 11
  slug: pan-os-rest-api-qos-rule-structure
- name: Pan Os Rest Api Security Rule Structure
  property_count: 17
  slug: pan-os-rest-api-security-rule-structure
- name: Pan Os Rest Api Service Group Structure
  property_count: 3
  slug: pan-os-rest-api-service-group-structure
- name: Pan Os Rest Api Service Structure
  property_count: 4
  slug: pan-os-rest-api-service-structure
- name: Pan Os Rest Api Tag Structure
  property_count: 3
  slug: pan-os-rest-api-tag-structure
- name: Pan Os Rest Api Virtual System Structure
  property_count: 3
  slug: pan-os-rest-api-virtual-system-structure
- name: Pan Os Security Rule Structure
  property_count: 20
  slug: pan-os-security-rule-structure
- name: Prisma Access Api Ike Gateway Structure
  property_count: 8
  slug: prisma-access-api-ike-gateway-structure
- name: Prisma Access Api Ip Sec Tunnel Structure
  property_count: 6
  slug: prisma-access-api-ip-sec-tunnel-structure
- name: Prisma Access Api Job Status Structure
  property_count: 8
  slug: prisma-access-api-job-status-structure
- name: Prisma Access Api Mobile Agent Infrastructure Settings Structure
  property_count: 6
  slug: prisma-access-api-mobile-agent-infrastructure-settings-structure
- name: Prisma Access Api Remote Network Structure
  property_count: 8
  slug: prisma-access-api-remote-network-structure
- name: Prisma Access Api Security Rule Structure
  property_count: 18
  slug: prisma-access-api-security-rule-structure
- name: Prisma Access Api Service Connection Structure
  property_count: 8
  slug: prisma-access-api-service-connection-structure
- name: Prisma Access Browser Api Browser Deployment Request Structure
  property_count: 5
  slug: prisma-access-browser-api-browser-deployment-request-structure
- name: Prisma Access Browser Api Browser Deployment Structure
  property_count: 8
  slug: prisma-access-browser-api-browser-deployment-structure
- name: Prisma Access Browser Api Browser Policy Request Structure
  property_count: 7
  slug: prisma-access-browser-api-browser-policy-request-structure
- name: Prisma Access Browser Api Browser Policy Structure
  property_count: 10
  slug: prisma-access-browser-api-browser-policy-structure
- name: Prisma Access Browser Api Browser Session Structure
  property_count: 9
  slug: prisma-access-browser-api-browser-session-structure
- name: Prisma Access Browser Api Browser User Structure
  property_count: 6
  slug: prisma-access-browser-api-browser-user-structure
- name: Prisma Access Browser Api Managed Device Structure
  property_count: 7
  slug: prisma-access-browser-api-managed-device-structure
- name: Prisma Access Browser Api Usage Report Structure
  property_count: 7
  slug: prisma-access-browser-api-usage-report-structure
- name: Prisma Access Insights Api Custom Query Structure
  property_count: 2
  slug: prisma-access-insights-api-custom-query-structure
- name: Prisma Access Insights Api Data Resource Query Structure
  property_count: 5
  slug: prisma-access-insights-api-data-resource-query-structure
- name: Prisma Access Insights Api Data Resource Response Structure
  property_count: 4
  slug: prisma-access-insights-api-data-resource-response-structure
- name: Prisma Access Insights Api Export Job Response Structure
  property_count: 3
  slug: prisma-access-insights-api-export-job-response-structure
- name: Prisma Access Insights Api Export Job Status Structure
  property_count: 5
  slug: prisma-access-insights-api-export-job-status-structure
- name: Prisma Access Insights Api Query Filter Structure
  property_count: 2
  slug: prisma-access-insights-api-query-filter-structure
- name: Prisma Access Insights Api Time Range Structure
  property_count: 3
  slug: prisma-access-insights-api-time-range-structure
- name: Prisma Airs Ai Red Teaming Api Attack Category Structure
  property_count: 6
  slug: prisma-airs-ai-red-teaming-api-attack-category-structure
- name: Prisma Airs Ai Red Teaming Api Scan Report Structure
  property_count: 9
  slug: prisma-airs-ai-red-teaming-api-scan-report-structure
- name: Prisma Airs Ai Red Teaming Api Scan Request Structure
  property_count: 4
  slug: prisma-airs-ai-red-teaming-api-scan-request-structure
- name: Prisma Airs Ai Red Teaming Api Scan Structure
  property_count: 12
  slug: prisma-airs-ai-red-teaming-api-scan-structure
- name: Prisma Airs Ai Red Teaming Api Scan Target Request Structure
  property_count: 7
  slug: prisma-airs-ai-red-teaming-api-scan-target-request-structure
- name: Prisma Airs Ai Red Teaming Api Scan Target Structure
  property_count: 8
  slug: prisma-airs-ai-red-teaming-api-scan-target-structure
- name: Prisma Airs Ai Red Teaming Api Vulnerability Finding Structure
  property_count: 9
  slug: prisma-airs-ai-red-teaming-api-vulnerability-finding-structure
- name: Prisma Airs Api Ai Profile Structure
  property_count: 6
  slug: prisma-airs-api-ai-profile-structure
- name: Prisma Airs Api Content Scan Result Structure
  property_count: 4
  slug: prisma-airs-api-content-scan-result-structure
- name: Prisma Airs Api Scan Content Structure
  property_count: 2
  slug: prisma-airs-api-scan-content-structure
- name: Prisma Airs Api Scan Request Structure
  property_count: 3
  slug: prisma-airs-api-scan-request-structure
- name: Prisma Airs Api Scan Response Structure
  property_count: 8
  slug: prisma-airs-api-scan-response-structure
- name: Prisma Cloud Code Security Api Code Error Structure
  property_count: 15
  slug: prisma-cloud-code-security-api-code-error-structure
- name: Prisma Cloud Code Security Api Fix Structure
  property_count: 12
  slug: prisma-cloud-code-security-api-fix-structure
- name: Prisma Cloud Code Security Api Repository Structure
  property_count: 12
  slug: prisma-cloud-code-security-api-repository-structure
- name: Prisma Cloud Code Security Api Scan Integration Structure
  property_count: 6
  slug: prisma-cloud-code-security-api-scan-integration-structure
- name: Prisma Cloud Code Security Api Scan Status Structure
  property_count: 8
  slug: prisma-cloud-code-security-api-scan-status-structure
- name: Prisma Cloud Code Security Api Suppression Structure
  property_count: 9
  slug: prisma-cloud-code-security-api-suppression-structure
- name: Prisma Cloud Compute Api Ci Scan Structure
  property_count: 5
  slug: prisma-cloud-compute-api-ci-scan-structure
- name: Prisma Cloud Compute Api Compliance Issue Structure
  property_count: 5
  slug: prisma-cloud-compute-api-compliance-issue-structure
- name: Prisma Cloud Compute Api Compliance Policy Structure
  property_count: 1
  slug: prisma-cloud-compute-api-compliance-policy-structure
- name: Prisma Cloud Compute Api Container Structure
  property_count: 11
  slug: prisma-cloud-compute-api-container-structure
- name: Prisma Cloud Compute Api Defender Structure
  property_count: 8
  slug: prisma-cloud-compute-api-defender-structure
- name: Prisma Cloud Compute Api Defender Summary Structure
  property_count: 5
  slug: prisma-cloud-compute-api-defender-summary-structure
- name: Prisma Cloud Compute Api Host Structure
  property_count: 12
  slug: prisma-cloud-compute-api-host-structure
- name: Prisma Cloud Compute Api Image Structure
  property_count: 13
  slug: prisma-cloud-compute-api-image-structure
- name: Prisma Cloud Compute Api Registry Config Structure
  property_count: 8
  slug: prisma-cloud-compute-api-registry-config-structure
- name: Prisma Cloud Compute Api Runtime Policy Structure
  property_count: 1
  slug: prisma-cloud-compute-api-runtime-policy-structure
- name: Prisma Cloud Compute Api Vulnerability Policy Structure
  property_count: 1
  slug: prisma-cloud-compute-api-vulnerability-policy-structure
- name: Prisma Cloud Compute Api Vulnerability Structure
  property_count: 10
  slug: prisma-cloud-compute-api-vulnerability-structure
- name: Prisma Cloud Cspm Api Alert Filter Structure
  property_count: 3
  slug: prisma-cloud-cspm-api-alert-filter-structure
- name: Prisma Cloud Cspm Api Alert Structure
  property_count: 9
  slug: prisma-cloud-cspm-api-alert-structure
- name: Prisma Cloud Cspm Api Cloud Account Structure
  property_count: 6
  slug: prisma-cloud-cspm-api-cloud-account-structure
- name: Prisma Cloud Cspm Api Compliance Standard Structure
  property_count: 8
  slug: prisma-cloud-cspm-api-compliance-standard-structure
- name: Prisma Cloud Cspm Api Policy Input Structure
  property_count: 8
  slug: prisma-cloud-cspm-api-policy-input-structure
- name: Prisma Cloud Cspm Api Policy Structure
  property_count: 11
  slug: prisma-cloud-cspm-api-policy-structure
- name: Prisma Cloud Cspm Api Report Structure
  property_count: 7
  slug: prisma-cloud-cspm-api-report-structure
- name: Prisma Cloud Cspm Api Search Result Structure
  property_count: 3
  slug: prisma-cloud-cspm-api-search-result-structure
- name: Prisma Cloud Cspm Api Time Range Structure
  property_count: 2
  slug: prisma-cloud-cspm-api-time-range-structure
- name: Prisma Cloud Dspm Api Classification Structure
  property_count: 9
  slug: prisma-cloud-dspm-api-classification-structure
- name: Prisma Cloud Dspm Api Data Asset Structure
  property_count: 12
  slug: prisma-cloud-dspm-api-data-asset-structure
- name: Prisma Cloud Dspm Api Data Risk Structure
  property_count: 16
  slug: prisma-cloud-dspm-api-data-risk-structure
- name: Prisma Cloud Dspm Api Data Security Alert Structure
  property_count: 14
  slug: prisma-cloud-dspm-api-data-security-alert-structure
- name: Prisma Cloud Dspm Api Data Store Structure
  property_count: 15
  slug: prisma-cloud-dspm-api-data-store-structure
- name: Prisma Cloud Dspm Api Dspm Policy Structure
  property_count: 10
  slug: prisma-cloud-dspm-api-dspm-policy-structure
- name: Prisma Cloud Mssp Api Change Password Request Structure
  property_count: 1
  slug: prisma-cloud-mssp-api-change-password-request-structure
- name: Prisma Cloud Mssp Api Contact Info Structure
  property_count: 3
  slug: prisma-cloud-mssp-api-contact-info-structure
- name: Prisma Cloud Mssp Api Create Managed Tenant Request Structure
  property_count: 8
  slug: prisma-cloud-mssp-api-create-managed-tenant-request-structure
- name: Prisma Cloud Mssp Api Create Mssp Request Structure
  property_count: 4
  slug: prisma-cloud-mssp-api-create-mssp-request-structure
- name: Prisma Cloud Mssp Api Create Policy Group Response Structure
  property_count: 3
  slug: prisma-cloud-mssp-api-create-policy-group-response-structure
- name: Prisma Cloud Mssp Api Create Tenant Group Request Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-create-tenant-group-request-structure
- name: Prisma Cloud Mssp Api Form Login Request Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-form-login-request-structure
- name: Prisma Cloud Mssp Api Form Login Response Structure
  property_count: 3
  slug: prisma-cloud-mssp-api-form-login-response-structure
- name: Prisma Cloud Mssp Api Jwk Response Structure
  property_count: 6
  slug: prisma-cloud-mssp-api-jwk-response-structure
- name: Prisma Cloud Mssp Api Jwks Response Structure
  property_count: 1
  slug: prisma-cloud-mssp-api-jwks-response-structure
- name: Prisma Cloud Mssp Api License Info Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-license-info-structure
- name: Prisma Cloud Mssp Api License Pool Info Structure
  property_count: 9
  slug: prisma-cloud-mssp-api-license-pool-info-structure
- name: Prisma Cloud Mssp Api Managed Tenant Detailed Response Structure
  property_count: 20
  slug: prisma-cloud-mssp-api-managed-tenant-detailed-response-structure
- name: Prisma Cloud Mssp Api Managed Tenant License Response Structure
  property_count: 6
  slug: prisma-cloud-mssp-api-managed-tenant-license-response-structure
- name: Prisma Cloud Mssp Api Managed Tenant Response Structure
  property_count: 19
  slug: prisma-cloud-mssp-api-managed-tenant-response-structure
- name: Prisma Cloud Mssp Api Managed Tenants Response Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-managed-tenants-response-structure
- name: Prisma Cloud Mssp Api Module Info Request Structure
  property_count: 3
  slug: prisma-cloud-mssp-api-module-info-request-structure
- name: Prisma Cloud Mssp Api Module Info Structure
  property_count: 5
  slug: prisma-cloud-mssp-api-module-info-structure
- name: Prisma Cloud Mssp Api Mssp License Info Response Structure
  property_count: 7
  slug: prisma-cloud-mssp-api-mssp-license-info-response-structure
- name: Prisma Cloud Mssp Api Mssp License Pool Request Structure
  property_count: 5
  slug: prisma-cloud-mssp-api-mssp-license-pool-request-structure
- name: Prisma Cloud Mssp Api Mssp License Pool Response Structure
  property_count: 9
  slug: prisma-cloud-mssp-api-mssp-license-pool-response-structure
- name: Prisma Cloud Mssp Api Mssp License Pools Response Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-mssp-license-pools-response-structure
- name: Prisma Cloud Mssp Api Mssp License Usage Request Object Structure
  property_count: 4
  slug: prisma-cloud-mssp-api-mssp-license-usage-request-object-structure
- name: Prisma Cloud Mssp Api Mssp License Usage Response Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-mssp-license-usage-response-structure
- name: Prisma Cloud Mssp Api Mssp List User Response Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-mssp-list-user-response-structure
- name: Prisma Cloud Mssp Api Mssp Response Structure
  property_count: 6
  slug: prisma-cloud-mssp-api-mssp-response-structure
- name: Prisma Cloud Mssp Api Mssp User Request Structure
  property_count: 3
  slug: prisma-cloud-mssp-api-mssp-user-request-structure
- name: Prisma Cloud Mssp Api Mssp User Response Structure
  property_count: 5
  slug: prisma-cloud-mssp-api-mssp-user-response-structure
- name: Prisma Cloud Mssp Api Operation Ack Request Structure
  property_count: 3
  slug: prisma-cloud-mssp-api-operation-ack-request-structure
- name: Prisma Cloud Mssp Api Operation Response Structure
  property_count: 13
  slug: prisma-cloud-mssp-api-operation-response-structure
- name: Prisma Cloud Mssp Api Operations Response Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-operations-response-structure
- name: Prisma Cloud Mssp Api Policy Group Info Structure
  property_count: 3
  slug: prisma-cloud-mssp-api-policy-group-info-structure
- name: Prisma Cloud Mssp Api Policy Group List Response Structure
  property_count: 4
  slug: prisma-cloud-mssp-api-policy-group-list-response-structure
- name: Prisma Cloud Mssp Api Policy Group Request Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-policy-group-request-structure
- name: Prisma Cloud Mssp Api Policy Group Response Structure
  property_count: 4
  slug: prisma-cloud-mssp-api-policy-group-response-structure
- name: Prisma Cloud Mssp Api Policy Groups List Response Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-policy-groups-list-response-structure
- name: Prisma Cloud Mssp Api Recur String Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-recur-string-structure
- name: Prisma Cloud Mssp Api Relative Time Duration Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-relative-time-duration-structure
- name: Prisma Cloud Mssp Api Relative Time Range Config Structure
  property_count: 0
  slug: prisma-cloud-mssp-api-relative-time-range-config-structure
- name: Prisma Cloud Mssp Api Schedule Task Request Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-schedule-task-request-structure
- name: Prisma Cloud Mssp Api Seamless Login Response Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-seamless-login-response-structure
- name: Prisma Cloud Mssp Api Stack Mapping Plan Types List Response Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-stack-mapping-plan-types-list-response-structure
- name: Prisma Cloud Mssp Api Stack Mapping Response Structure
  property_count: 3
  slug: prisma-cloud-mssp-api-stack-mapping-response-structure
- name: Prisma Cloud Mssp Api Task Structure
  property_count: 9
  slug: prisma-cloud-mssp-api-task-structure
- name: Prisma Cloud Mssp Api Tenant Change Response Structure
  property_count: 5
  slug: prisma-cloud-mssp-api-tenant-change-response-structure
- name: Prisma Cloud Mssp Api Tenant Group License Info Structure
  property_count: 4
  slug: prisma-cloud-mssp-api-tenant-group-license-info-structure
- name: Prisma Cloud Mssp Api Tenant Group Mapping Details Structure
  property_count: 4
  slug: prisma-cloud-mssp-api-tenant-group-mapping-details-structure
- name: Prisma Cloud Mssp Api Tenant Group Policy Group Map Request Structure
  property_count: 1
  slug: prisma-cloud-mssp-api-tenant-group-policy-group-map-request-structure
- name: Prisma Cloud Mssp Api Tenant Group Policy Group Mapping Response Structure
  property_count: 3
  slug: prisma-cloud-mssp-api-tenant-group-policy-group-mapping-response-structure
- name: Prisma Cloud Mssp Api Tenant Group Policy Group Mapping Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-tenant-group-policy-group-mapping-structure
- name: Prisma Cloud Mssp Api Tenant Group Policy Group Mappings Response Structure
  property_count: 1
  slug: prisma-cloud-mssp-api-tenant-group-policy-group-mappings-response-structure
- name: Prisma Cloud Mssp Api Tenant Group Response Structure
  property_count: 5
  slug: prisma-cloud-mssp-api-tenant-group-response-structure
- name: Prisma Cloud Mssp Api Tenant Groups Response Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-tenant-groups-response-structure
- name: Prisma Cloud Mssp Api Tenant Ids Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-tenant-ids-structure
- name: Prisma Cloud Mssp Api Tenant License Usage Structure
  property_count: 9
  slug: prisma-cloud-mssp-api-tenant-license-usage-structure
- name: Prisma Cloud Mssp Api Tenant Update Structure
  property_count: 4
  slug: prisma-cloud-mssp-api-tenant-update-structure
- name: Prisma Cloud Mssp Api Time Range Config Object Structure
  property_count: 3
  slug: prisma-cloud-mssp-api-time-range-config-object-structure
- name: Prisma Cloud Mssp Api To Now Time Range Config Structure
  property_count: 0
  slug: prisma-cloud-mssp-api-to-now-time-range-config-structure
- name: Prisma Cloud Mssp Api Token Refresh Response Structure
  property_count: 1
  slug: prisma-cloud-mssp-api-token-refresh-response-structure
- name: Prisma Cloud Mssp Api Update Managed Tenant Request Structure
  property_count: 4
  slug: prisma-cloud-mssp-api-update-managed-tenant-request-structure
- name: Prisma Cloud Mssp Api Update Mssp Request Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-update-mssp-request-structure
- name: Prisma Cloud Mssp Api Update Tenant Group Request Structure
  property_count: 2
  slug: prisma-cloud-mssp-api-update-tenant-group-request-structure
- name: Prisma Cloud Mssp Api V1 Response Structure
  property_count: 0
  slug: prisma-cloud-mssp-api-v1-response-structure
- name: Prisma Cloud Mssp Api Validate Token Request Structure
  property_count: 1
  slug: prisma-cloud-mssp-api-validate-token-request-structure
- name: Prisma Cloud Mssp Api Validate Token Response Structure
  property_count: 1
  slug: prisma-cloud-mssp-api-validate-token-response-structure
- name: Prisma Cloud Policy Structure
  property_count: 18
  slug: prisma-cloud-policy-structure
- name: Prisma Cloud Webhooks Alert Payload Structure
  property_count: 11
  slug: prisma-cloud-webhooks-alert-payload-structure
- name: Prisma Sd Wan Api Alarm Structure
  property_count: 12
  slug: prisma-sd-wan-api-alarm-structure
- name: Prisma Sd Wan Api Application Usage Structure
  property_count: 7
  slug: prisma-sd-wan-api-application-usage-structure
- name: Prisma Sd Wan Api Lan Network Structure
  property_count: 9
  slug: prisma-sd-wan-api-lan-network-structure
- name: Prisma Sd Wan Api Path Rule Structure
  property_count: 10
  slug: prisma-sd-wan-api-path-rule-structure
- name: Prisma Sd Wan Api Qo S Rule Structure
  property_count: 11
  slug: prisma-sd-wan-api-qo-s-rule-structure
- name: Prisma Sd Wan Api Site Metric Structure
  property_count: 7
  slug: prisma-sd-wan-api-site-metric-structure
- name: Prisma Sd Wan Api Site Structure
  property_count: 10
  slug: prisma-sd-wan-api-site-structure
- name: Prisma Sd Wan Api Wan Interface Structure
  property_count: 12
  slug: prisma-sd-wan-api-wan-interface-structure
- name: Saas Security Api Application Structure
  property_count: 7
  slug: saas-security-api-application-structure
- name: Saas Security Api Asset Structure
  property_count: 12
  slug: saas-security-api-asset-structure
- name: Saas Security Api Incident Structure
  property_count: 13
  slug: saas-security-api-incident-structure
- name: Saas Security Api Log Forwarding Settings Structure
  property_count: 2
  slug: saas-security-api-log-forwarding-settings-structure
- name: Saas Security Api User Activity Structure
  property_count: 8
  slug: saas-security-api-user-activity-structure
- name: Saas Security Api User Structure
  property_count: 6
  slug: saas-security-api-user-structure
- name: Sase 5G Api Network Slice Request Structure
  property_count: 5
  slug: sase-5g-api-network-slice-request-structure
- name: Sase 5G Api Network Slice Structure
  property_count: 10
  slug: sase-5g-api-network-slice-structure
- name: Sase 5G Api Security Metrics5 G Structure
  property_count: 8
  slug: sase-5g-api-security-metrics5-g-structure
- name: Sase 5G Api Security Policy5 G Request Structure
  property_count: 8
  slug: sase-5g-api-security-policy5-g-request-structure
- name: Sase 5G Api Security Policy5 G Structure
  property_count: 11
  slug: sase-5g-api-security-policy5-g-structure
- name: Sase 5G Api Tenant5 G Request Structure
  property_count: 4
  slug: sase-5g-api-tenant5-g-request-structure
- name: Sase 5G Api Tenant5 G Structure
  property_count: 7
  slug: sase-5g-api-tenant5-g-structure
- name: Sase 5G Monitor Api Count Filter Request Structure
  property_count: 1
  slug: sase-5g-monitor-api-count-filter-request-structure
- name: Sase 5G Monitor Api Incidents Count Request Structure
  property_count: 2
  slug: sase-5g-monitor-api-incidents-count-request-structure
- name: Sase 5G Monitor Api Mapping Request Structure
  property_count: 5
  slug: sase-5g-monitor-api-mapping-request-structure
- name: Sase 5G Monitor Api Throughput Request Structure
  property_count: 3
  slug: sase-5g-monitor-api-throughput-request-structure
- name: Sase 5G Monitor Api Trend Request Structure
  property_count: 3
  slug: sase-5g-monitor-api-trend-request-structure
- name: Sase Aggregate Monitoring Api Aggregation Query Structure
  property_count: 7
  slug: sase-aggregate-monitoring-api-aggregation-query-structure
- name: Sase Aggregate Monitoring Api Aggregation Response Structure
  property_count: 5
  slug: sase-aggregate-monitoring-api-aggregation-response-structure
- name: Sase Aggregate Monitoring Api Tenant Summary Structure
  property_count: 5
  slug: sase-aggregate-monitoring-api-tenant-summary-structure
- name: Sase Config Orchestration Api Bandwidth Allocation Structure
  property_count: 5
  slug: sase-config-orchestration-api-bandwidth-allocation-structure
- name: Sase Config Orchestration Api I Psec Tunnel Structure
  property_count: 3
  slug: sase-config-orchestration-api-i-psec-tunnel-structure
- name: Sase Config Orchestration Api Ike Gateway Config Structure
  property_count: 5
  slug: sase-config-orchestration-api-ike-gateway-config-structure
- name: Sase Config Orchestration Api Ike Gateway Structure
  property_count: 5
  slug: sase-config-orchestration-api-ike-gateway-structure
- name: Sase Config Orchestration Api Onboarding Status Structure
  property_count: 6
  slug: sase-config-orchestration-api-onboarding-status-structure
- name: Sase Config Orchestration Api Prisma Access Location Structure
  property_count: 6
  slug: sase-config-orchestration-api-prisma-access-location-structure
- name: Sase Config Orchestration Api Remote Network Request Structure
  property_count: 6
  slug: sase-config-orchestration-api-remote-network-request-structure
- name: Sase Config Orchestration Api Remote Network Structure
  property_count: 11
  slug: sase-config-orchestration-api-remote-network-structure
- name: Sase Iam Api Access Policy Request Structure
  property_count: 4
  slug: sase-iam-api-access-policy-request-structure
- name: Sase Iam Api Access Policy Structure
  property_count: 7
  slug: sase-iam-api-access-policy-structure
- name: Sase Iam Api Role Structure
  property_count: 5
  slug: sase-iam-api-role-structure
- name: Sase Iam Api Service Account Credentials Structure
  property_count: 6
  slug: sase-iam-api-service-account-credentials-structure
- name: Sase Iam Api Service Account Request Structure
  property_count: 4
  slug: sase-iam-api-service-account-request-structure
- name: Sase Iam Api Service Account Structure
  property_count: 8
  slug: sase-iam-api-service-account-structure
- name: Sase Iam Api Service Account Update Structure
  property_count: 2
  slug: sase-iam-api-service-account-update-structure
- name: Sase Multitenant Interconnect Api Bandwidth Structure
  property_count: 0
  slug: sase-multitenant-interconnect-api-bandwidth-structure
- name: Sase Multitenant Interconnect Api Cloud Provider Structure
  property_count: 0
  slug: sase-multitenant-interconnect-api-cloud-provider-structure
- name: Sase Multitenant Interconnect Api Connection Type Structure
  property_count: 0
  slug: sase-multitenant-interconnect-api-connection-type-structure
- name: Sase Multitenant Interconnect Api Dedicated Vlan Attachment Details Entry Structure
  property_count: 2
  slug: sase-multitenant-interconnect-api-dedicated-vlan-attachment-details-entry-structure
- name: Sase Multitenant Interconnect Api Interconnect Request Structure
  property_count: 11
  slug: sase-multitenant-interconnect-api-interconnect-request-structure
- name: Sase Multitenant Interconnect Api Interconnect Usage Structure
  property_count: 0
  slug: sase-multitenant-interconnect-api-interconnect-usage-structure
- name: Sase Multitenant Interconnect Api Ip Block Entry Structure
  property_count: 3
  slug: sase-multitenant-interconnect-api-ip-block-entry-structure
- name: Sase Multitenant Interconnect Api Ip Block Type Structure
  property_count: 0
  slug: sase-multitenant-interconnect-api-ip-block-type-structure
- name: Sase Multitenant Interconnect Api Ip Pool Request Structure
  property_count: 2
  slug: sase-multitenant-interconnect-api-ip-pool-request-structure
- name: Sase Multitenant Interconnect Api Ip Provider Structure
  property_count: 0
  slug: sase-multitenant-interconnect-api-ip-provider-structure
- name: Sase Multitenant Interconnect Api Physical Connection Entry Structure
  property_count: 7
  slug: sase-multitenant-interconnect-api-physical-connection-entry-structure
- name: Sase Multitenant Interconnect Api Physical Interconnect Link Type Structure
  property_count: 0
  slug: sase-multitenant-interconnect-api-physical-interconnect-link-type-structure
- name: Sase Multitenant Interconnect Api Session Initialization Mode Structure
  property_count: 0
  slug: sase-multitenant-interconnect-api-session-initialization-mode-structure
- name: Sase Multitenant Interconnect Api Settings Entry Structure
  property_count: 2
  slug: sase-multitenant-interconnect-api-settings-entry-structure
- name: Sase Multitenant Interconnect Api Stack Type Structure
  property_count: 0
  slug: sase-multitenant-interconnect-api-stack-type-structure
- name: Sase Multitenant Interconnect Api Vlan Attachment Custom Ip Address Structure
  property_count: 2
  slug: sase-multitenant-interconnect-api-vlan-attachment-custom-ip-address-structure
- name: Sase Multitenant Interconnect Api Vlan Attachment Request Structure
  property_count: 12
  slug: sase-multitenant-interconnect-api-vlan-attachment-request-structure
- name: Sase Multitenant Notifications Api Email Channel Details Structure
  property_count: 1
  slug: sase-multitenant-notifications-api-email-channel-details-structure
- name: Sase Multitenant Notifications Api Email Details Structure
  property_count: 2
  slug: sase-multitenant-notifications-api-email-details-structure
- name: Sase Multitenant Notifications Api Mt Notif Agg Key Structure
  property_count: 5
  slug: sase-multitenant-notifications-api-mt-notif-agg-key-structure
- name: Sase Multitenant Notifications Api Mt Notification List Structure
  property_count: 0
  slug: sase-multitenant-notifications-api-mt-notification-list-structure
- name: Sase Multitenant Notifications Api Mt Notification Structure
  property_count: 11
  slug: sase-multitenant-notifications-api-mt-notification-structure
- name: Sase Multitenant Notifications Api Notif Category Detail Structure
  property_count: 3
  slug: sase-multitenant-notifications-api-notif-category-detail-structure
- name: Sase Multitenant Notifications Api Notif Channel Structure
  property_count: 5
  slug: sase-multitenant-notifications-api-notif-channel-structure
- name: Sase Multitenant Notifications Api Notif Filter Structure
  property_count: 2
  slug: sase-multitenant-notifications-api-notif-filter-structure
- name: Sase Multitenant Notifications Api Notif List Api Req Body Structure
  property_count: 3
  slug: sase-multitenant-notifications-api-notif-list-api-req-body-structure
- name: Sase Multitenant Notifications Api Notif Profile List Structure
  property_count: 0
  slug: sase-multitenant-notifications-api-notif-profile-list-structure
- name: Sase Multitenant Notifications Api Notif Profile Structure
  property_count: 11
  slug: sase-multitenant-notifications-api-notif-profile-structure
- name: Sase Multitenant Notifications Api Notif Read State Structure
  property_count: 0
  slug: sase-multitenant-notifications-api-notif-read-state-structure
- name: Sase Multitenant Notifications Api Notif State Change Api Body Structure
  property_count: 2
  slug: sase-multitenant-notifications-api-notif-state-change-api-body-structure
- name: Sase Multitenant Notifications Api Notif Sub Category Detail Structure
  property_count: 3
  slug: sase-multitenant-notifications-api-notif-sub-category-detail-structure
- name: Sase Multitenant Notifications Api Notif Type Detail Structure
  property_count: 2
  slug: sase-multitenant-notifications-api-notif-type-detail-structure
- name: Sase Multitenant Notifications Api Sort By Structure
  property_count: 2
  slug: sase-multitenant-notifications-api-sort-by-structure
- name: Sase Multitenant Notifications Api Webhook Channel Details Structure
  property_count: 3
  slug: sase-multitenant-notifications-api-webhook-channel-details-structure
- name: Sase Notifications Announcement Notification Structure
  property_count: 9
  slug: sase-notifications-announcement-notification-structure
- name: Sase Notifications Certificate Expiry Notification Structure
  property_count: 11
  slug: sase-notifications-certificate-expiry-notification-structure
- name: Sase Notifications Dataplane Upgrade Notification Structure
  property_count: 10
  slug: sase-notifications-dataplane-upgrade-notification-structure
- name: Sase Notifications Incident Detail Structure
  property_count: 9
  slug: sase-notifications-incident-detail-structure
- name: Sase Notifications Incident Notification Structure
  property_count: 10
  slug: sase-notifications-incident-notification-structure
- name: Sase Notifications Service Info Structure
  property_count: 3
  slug: sase-notifications-service-info-structure
- name: Sase Notifications Tenant Context Structure
  property_count: 3
  slug: sase-notifications-tenant-context-structure
- name: Sase Subscription Api Allocation Entry Structure
  property_count: 4
  slug: sase-subscription-api-allocation-entry-structure
- name: Sase Subscription Api Allocation Request Structure
  property_count: 1
  slug: sase-subscription-api-allocation-request-structure
- name: Sase Subscription Api Entitlement Structure
  property_count: 5
  slug: sase-subscription-api-entitlement-structure
- name: Sase Subscription Api Subscription Entitlements Structure
  property_count: 4
  slug: sase-subscription-api-subscription-entitlements-structure
- name: Sase Subscription Api Subscription Structure
  property_count: 11
  slug: sase-subscription-api-subscription-structure
- name: Sase Tenancy Api Tenant Service Group Request Structure
  property_count: 6
  slug: sase-tenancy-api-tenant-service-group-request-structure
- name: Sase Tenancy Api Tenant Service Group Structure
  property_count: 11
  slug: sase-tenancy-api-tenant-service-group-structure
- name: Sase Tenancy Api Tenant Service Group Update Structure
  property_count: 3
  slug: sase-tenancy-api-tenant-service-group-update-structure
- name: Security Advisory Api Advisory Structure
  property_count: 15
  slug: security-advisory-api-advisory-structure
- name: Security Advisory Api Affected Product Structure
  property_count: 2
  slug: security-advisory-api-affected-product-structure
- name: Security Advisory Api Product Structure
  property_count: 2
  slug: security-advisory-api-product-structure
- name: Sspm Api Catalog App Structure
  property_count: 6
  slug: sspm-api-catalog-app-structure
- name: Sspm Api Jira Integration Request Structure
  property_count: 7
  slug: sspm-api-jira-integration-request-structure
- name: Sspm Api Jira Integration Structure
  property_count: 7
  slug: sspm-api-jira-integration-structure
- name: Sspm Api Onboard App Request Structure
  property_count: 3
  slug: sspm-api-onboard-app-request-structure
- name: Sspm Api Onboarded App Structure
  property_count: 8
  slug: sspm-api-onboarded-app-structure
- name: Sspm Api Posture Check Structure
  property_count: 11
  slug: sspm-api-posture-check-structure
- name: Strata Cloud Manager Api Address Group List Structure
  property_count: 4
  slug: strata-cloud-manager-api-address-group-list-structure
- name: Strata Cloud Manager Api Address Group Request Structure
  property_count: 5
  slug: strata-cloud-manager-api-address-group-request-structure
- name: Strata Cloud Manager Api Address Group Structure
  property_count: 7
  slug: strata-cloud-manager-api-address-group-structure
- name: Strata Cloud Manager Api Address List Structure
  property_count: 4
  slug: strata-cloud-manager-api-address-list-structure
- name: Strata Cloud Manager Api Address Request Structure
  property_count: 7
  slug: strata-cloud-manager-api-address-request-structure
- name: Strata Cloud Manager Api Address Structure
  property_count: 10
  slug: strata-cloud-manager-api-address-structure
- name: Strata Cloud Manager Api Delete Response Structure
  property_count: 1
  slug: strata-cloud-manager-api-delete-response-structure
- name: Strata Cloud Manager Api Job Structure
  property_count: 8
  slug: strata-cloud-manager-api-job-structure
- name: Strata Cloud Manager Api Nat Rule List Structure
  property_count: 4
  slug: strata-cloud-manager-api-nat-rule-list-structure
- name: Strata Cloud Manager Api Nat Rule Request Structure
  property_count: 11
  slug: strata-cloud-manager-api-nat-rule-request-structure
- name: Strata Cloud Manager Api Nat Rule Structure
  property_count: 15
  slug: strata-cloud-manager-api-nat-rule-structure
- name: Strata Cloud Manager Api Security Rule List Structure
  property_count: 4
  slug: strata-cloud-manager-api-security-rule-list-structure
- name: Strata Cloud Manager Api Security Rule Request Structure
  property_count: 15
  slug: strata-cloud-manager-api-security-rule-request-structure
- name: Strata Cloud Manager Api Security Rule Structure
  property_count: 18
  slug: strata-cloud-manager-api-security-rule-structure
- name: Strata Cloud Manager Api Service List Structure
  property_count: 4
  slug: strata-cloud-manager-api-service-list-structure
- name: Strata Cloud Manager Api Service Request Structure
  property_count: 4
  slug: strata-cloud-manager-api-service-request-structure
- name: Strata Cloud Manager Api Service Structure
  property_count: 6
  slug: strata-cloud-manager-api-service-structure
- name: Strata Logging Forwarding Auth Log Payload Structure
  property_count: 17
  slug: strata-logging-forwarding-auth-log-payload-structure
- name: Strata Logging Forwarding Threat Log Payload Structure
  property_count: 24
  slug: strata-logging-forwarding-threat-log-payload-structure
- name: Strata Logging Forwarding Traffic Log Payload Structure
  property_count: 30
  slug: strata-logging-forwarding-traffic-log-payload-structure
- name: Strata Logging Forwarding Url Log Payload Structure
  property_count: 19
  slug: strata-logging-forwarding-url-log-payload-structure
- name: Strata Logging Forwarding Wildfire Log Payload Structure
  property_count: 19
  slug: strata-logging-forwarding-wildfire-log-payload-structure
- name: Strata Logging Service Api Email Destination Request Structure
  property_count: 6
  slug: strata-logging-service-api-email-destination-request-structure
- name: Strata Logging Service Api Email Destination Structure
  property_count: 8
  slug: strata-logging-service-api-email-destination-structure
- name: Strata Logging Service Api Forwarding Status Structure
  property_count: 3
  slug: strata-logging-service-api-forwarding-status-structure
- name: Strata Logging Service Api Https Destination Request Structure
  property_count: 6
  slug: strata-logging-service-api-https-destination-request-structure
- name: Strata Logging Service Api Https Destination Structure
  property_count: 7
  slug: strata-logging-service-api-https-destination-structure
- name: Strata Logging Service Api Log Forwarding Profile Request Structure
  property_count: 4
  slug: strata-logging-service-api-log-forwarding-profile-request-structure
- name: Strata Logging Service Api Log Forwarding Profile Structure
  property_count: 8
  slug: strata-logging-service-api-log-forwarding-profile-structure
- name: Strata Logging Service Api Syslog Destination Request Structure
  property_count: 7
  slug: strata-logging-service-api-syslog-destination-request-structure
- name: Strata Logging Service Api Syslog Destination Structure
  property_count: 9
  slug: strata-logging-service-api-syslog-destination-structure
- name: Threat Vault Api Api Stats Structure
  property_count: 2
  slug: threat-vault-api-api-stats-structure
- name: Threat Vault Api Atp Report List Structure
  property_count: 5
  slug: threat-vault-api-atp-report-list-structure
- name: Threat Vault Api Atp Report Structure
  property_count: 6
  slug: threat-vault-api-atp-report-structure
- name: Threat Vault Api Release Note Structure
  property_count: 7
  slug: threat-vault-api-release-note-structure
- name: Threat Vault Api Release Notes List Structure
  property_count: 5
  slug: threat-vault-api-release-notes-list-structure
- name: Threat Vault Api Threat History Entry Structure
  property_count: 5
  slug: threat-vault-api-threat-history-entry-structure
- name: Threat Vault Api Threat History List Structure
  property_count: 5
  slug: threat-vault-api-threat-history-list-structure
- name: Threat Vault Api Threat List Structure
  property_count: 6
  slug: threat-vault-api-threat-list-structure
- name: Threat Vault Api Threat Signature Structure
  property_count: 16
  slug: threat-vault-api-threat-signature-structure
- name: Wildfire Api Analysis Report Structure
  property_count: 1
  slug: wildfire-api-analysis-report-structure
- name: Wildfire Api Bulk Verdict Response Structure
  property_count: 1
  slug: wildfire-api-bulk-verdict-response-structure
- name: Wildfire Api Sandbox Report Structure
  property_count: 6
  slug: wildfire-api-sandbox-report-structure
- name: Wildfire Api Submit Response Structure
  property_count: 1
  slug: wildfire-api-submit-response-structure
- name: Wildfire Api Verdict Response Structure
  property_count: 1
  slug: wildfire-api-verdict-response-structure
- name: Ztna Connector Api Connector Group Request Structure
  property_count: 3
  slug: ztna-connector-api-connector-group-request-structure
- name: Ztna Connector Api Connector Group Structure
  property_count: 6
  slug: ztna-connector-api-connector-group-structure
- name: Ztna Connector Api Connector Request Structure
  property_count: 3
  slug: ztna-connector-api-connector-request-structure
- name: Ztna Connector Api Connector Structure
  property_count: 10
  slug: ztna-connector-api-connector-structure
- name: Ztna Connector Api Fqdn Rule Request Structure
  property_count: 5
  slug: ztna-connector-api-fqdn-rule-request-structure
- name: Ztna Connector Api Fqdn Rule Structure
  property_count: 7
  slug: ztna-connector-api-fqdn-rule-structure
- name: Ztna Connector Api License Info Structure
  property_count: 5
  slug: ztna-connector-api-license-info-structure
- name: Ztna Connector Api Subnet Rule Request Structure
  property_count: 4
  slug: ztna-connector-api-subnet-rule-request-structure
- name: Ztna Connector Api Subnet Rule Structure
  property_count: 6
  slug: ztna-connector-api-subnet-rule-structure
- name: Ztna Connector Api Ztna Application Request Structure
  property_count: 7
  slug: ztna-connector-api-ztna-application-request-structure
- name: Ztna Connector Api Ztna Application Structure
  property_count: 9
  slug: ztna-connector-api-ztna-application-structure
jsonld:
- class_count: 4
  name: Palo Alto Aiops Ngfw Bpa Api Context
  property_count: 32
  slug: palo-alto-aiops-ngfw-bpa-api-context
- class_count: 6
  name: Palo Alto Autonomous Dem Api Context
  property_count: 39
  slug: palo-alto-autonomous-dem-api-context
- class_count: 13
  name: Palo Alto Cloud Identity Engine Api Context
  property_count: 12
  slug: palo-alto-cloud-identity-engine-api-context
- class_count: 16
  name: Palo Alto Cloud Ngfw Api Context
  property_count: 55
  slug: palo-alto-cloud-ngfw-api-context
- class_count: 7
  name: Palo Alto Cortex Xdr Api Context
  property_count: 66
  slug: palo-alto-cortex-xdr-api-context
- class_count: 1
  name: Palo Alto Cortex Xdr Context
  property_count: 32
  slug: palo-alto-cortex-xdr-context
- class_count: 2
  name: Palo Alto Cortex Xdr Webhooks Context
  property_count: 10
  slug: palo-alto-cortex-xdr-webhooks-context
- class_count: 8
  name: Palo Alto Cortex Xpanse Api Context
  property_count: 60
  slug: palo-alto-cortex-xpanse-api-context
- class_count: 8
  name: Palo Alto Cortex Xsiam Api Context
  property_count: 57
  slug: palo-alto-cortex-xsiam-api-context
- class_count: 3
  name: Palo Alto Cortex Xsiam Data Ingestion Context
  property_count: 8
  slug: palo-alto-cortex-xsiam-data-ingestion-context
- class_count: 11
  name: Palo Alto Cortex Xsoar Api Context
  property_count: 61
  slug: palo-alto-cortex-xsoar-api-context
- class_count: 2
  name: Palo Alto Cortex Xsoar Context
  property_count: 25
  slug: palo-alto-cortex-xsoar-context
- class_count: 4
  name: Palo Alto Dlp Api Context
  property_count: 55
  slug: palo-alto-dlp-api-context
- class_count: 2
  name: Palo Alto Dns Security Api Context
  property_count: 23
  slug: palo-alto-dns-security-api-context
- class_count: 3
  name: Palo Alto Email Dlp Api Context
  property_count: 25
  slug: palo-alto-email-dlp-api-context
- class_count: 19
  name: Palo Alto Identity Security Posture Management Api Context
  property_count: 66
  slug: palo-alto-identity-security-posture-management-api-context
- class_count: 6
  name: Palo Alto Iot Security Api Context
  property_count: 54
  slug: palo-alto-iot-security-api-context
- class_count: 0
  name: Palo Alto Networks Context
  property_count: 72
  slug: palo-alto-networks-context
- class_count: 63
  name: Palo Alto Networks Security Context
  property_count: 6
  slug: palo-alto-networks-security-context
- class_count: 3
  name: Palo Alto Pan Os Context
  property_count: 27
  slug: palo-alto-pan-os-context
- class_count: 12
  name: Palo Alto Pan Os Rest Api Context
  property_count: 57
  slug: palo-alto-pan-os-rest-api-context
- class_count: 7
  name: Palo Alto Prisma Access Api Context
  property_count: 56
  slug: palo-alto-prisma-access-api-context
- class_count: 8
  name: Palo Alto Prisma Access Browser Api Context
  property_count: 41
  slug: palo-alto-prisma-access-browser-api-context
- class_count: 7
  name: Palo Alto Prisma Access Insights Api Context
  property_count: 34
  slug: palo-alto-prisma-access-insights-api-context
- class_count: 7
  name: Palo Alto Prisma Airs Ai Red Teaming Api Context
  property_count: 45
  slug: palo-alto-prisma-airs-ai-red-teaming-api-context
- class_count: 5
  name: Palo Alto Prisma Airs Api Context
  property_count: 28
  slug: palo-alto-prisma-airs-api-context
- class_count: 6
  name: Palo Alto Prisma Cloud Code Security Api Context
  property_count: 53
  slug: palo-alto-prisma-cloud-code-security-api-context
- class_count: 12
  name: Palo Alto Prisma Cloud Compute Api Context
  property_count: 81
  slug: palo-alto-prisma-cloud-compute-api-context
- class_count: 3
  name: Palo Alto Prisma Cloud Context
  property_count: 28
  slug: palo-alto-prisma-cloud-context
- class_count: 9
  name: Palo Alto Prisma Cloud Cspm Api Context
  property_count: 49
  slug: palo-alto-prisma-cloud-cspm-api-context
- class_count: 6
  name: Palo Alto Prisma Cloud Dspm Api Context
  property_count: 50
  slug: palo-alto-prisma-cloud-dspm-api-context
- class_count: 66
  name: Palo Alto Prisma Cloud Mssp Api Context
  property_count: 124
  slug: palo-alto-prisma-cloud-mssp-api-context
- class_count: 1
  name: Palo Alto Prisma Cloud Webhooks Context
  property_count: 11
  slug: palo-alto-prisma-cloud-webhooks-context
- class_count: 8
  name: Palo Alto Prisma Sd Wan Api Context
  property_count: 59
  slug: palo-alto-prisma-sd-wan-api-context
- class_count: 6
  name: Palo Alto Saas Security Api Context
  property_count: 36
  slug: palo-alto-saas-security-api-context
- class_count: 7
  name: Palo Alto Sase 5G Api Context
  property_count: 34
  slug: palo-alto-sase-5g-api-context
- class_count: 5
  name: Palo Alto Sase 5G Monitor Api Context
  property_count: 17
  slug: palo-alto-sase-5g-monitor-api-context
- class_count: 3
  name: Palo Alto Sase Aggregate Monitoring Api Context
  property_count: 21
  slug: palo-alto-sase-aggregate-monitoring-api-context
- class_count: 8
  name: Palo Alto Sase Config Orchestration Api Context
  property_count: 34
  slug: palo-alto-sase-config-orchestration-api-context
- class_count: 7
  name: Palo Alto Sase Iam Api Context
  property_count: 17
  slug: palo-alto-sase-iam-api-context
- class_count: 8
  name: Palo Alto Sase Multitenant Interconnect Api Context
  property_count: 35
  slug: palo-alto-sase-multitenant-interconnect-api-context
- class_count: 14
  name: Palo Alto Sase Multitenant Notifications Api Context
  property_count: 49
  slug: palo-alto-sase-multitenant-notifications-api-context
- class_count: 7
  name: Palo Alto Sase Notifications Context
  property_count: 34
  slug: palo-alto-sase-notifications-context
- class_count: 5
  name: Palo Alto Sase Subscription Api Context
  property_count: 19
  slug: palo-alto-sase-subscription-api-context
- class_count: 3
  name: Palo Alto Sase Tenancy Api Context
  property_count: 11
  slug: palo-alto-sase-tenancy-api-context
- class_count: 3
  name: Palo Alto Security Advisory Api Context
  property_count: 22
  slug: palo-alto-security-advisory-api-context
- class_count: 6
  name: Palo Alto Security Advisory Context
  property_count: 32
  slug: palo-alto-security-advisory-context
- class_count: 6
  name: Palo Alto Sspm Api Context
  property_count: 36
  slug: palo-alto-sspm-api-context
- class_count: 17
  name: Palo Alto Strata Cloud Manager Api Context
  property_count: 51
  slug: palo-alto-strata-cloud-manager-api-context
- class_count: 5
  name: Palo Alto Strata Logging Forwarding Context
  property_count: 51
  slug: palo-alto-strata-logging-forwarding-context
- class_count: 9
  name: Palo Alto Strata Logging Service Api Context
  property_count: 29
  slug: palo-alto-strata-logging-service-api-context
- class_count: 9
  name: Palo Alto Threat Vault Api Context
  property_count: 50
  slug: palo-alto-threat-vault-api-context
- class_count: 6
  name: Palo Alto Wildfire Api Context
  property_count: 27
  slug: palo-alto-wildfire-api-context
- class_count: 11
  name: Palo Alto Ztna Connector Api Context
  property_count: 25
  slug: palo-alto-ztna-connector-api-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-09-16'
name: Palo Alto Networks
nav: Providers
network: true
overview: 'Palo Alto Networks publishes 599 API contracts indexed on the [APIs.io](https://apis.io/) network, including AddressGroups API, CloudAccounts API, DataAssets API, and 596 more. Tagged areas include Cloud Security, Cybersecurity, Firewall, Network Security, and SASE.


  The Palo Alto Networks catalog on APIs.io includes 5 event-driven AsyncAPI specifications, 54 JSON-LD contexts, and 5 Spectral governance rulesets.


  Palo Alto Networks'' developer surface includes authentication, developer portal, documentation, support, engineering blog, CLI, tooling, and 79 more developer resources.'
plans:
- name: Palo Alto Networks Plans Pricing
  plan_count: 1
  slug: palo-alto-networks-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Palo Alto Networks Rate Limits
  slug: palo-alto-networks-rate-limits
rules:
- authorship: generated
  effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Palo Alto Networks — asyncapi rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 7
  slug: palo-alto-networks-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Palo Alto Networks — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: palo-alto-networks-jsonschema-spectral-rules
- authorship: provider
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Palo Alto Networks — openapi rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: palo-alto-networks-openapi-spectral-rules
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Palo Alto Networks API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 4
  slug: palo-alto-networks-rules
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: Palo Alto Networks API Rules
  rule_count: 71
  severity_counts:
    error: 16
    hint: 0
    info: 24
    warn: 31
  slug: palo-alto-networks-spectral-rules
scopes:
- name: Palo Alto Networks Scopes
  scope_count: 1
  slug: palo-alto-networks-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: exemplar
  composite: 68.1
  coverage:
    artifact_dirs: 36
    catalog_earned: 73.0
    catalog_earned_first_party: 0.0
    catalog_gap: 42.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 45.5
    contract_quality: 78.0
    developer_ergonomics: 85.7
    discoverability: 78.6
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  open_source:
    applies: true
    score: 40.0
  previous_composite: 68.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 88.9
      derived: 0
      marker_coverage: 0.0
      total: 576
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: psd2
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/palo-alto-networks/palo-alto-networks-2026-06-20T191330.png
security:
- kind: authentication
  name: Palo Alto Networks Authentication
  slug: palo-alto-networks-authentication
  summary_line: apiKey/http/oauth2 · 13 schemes
- kind: domain-security
  name: Palo Alto Networks Domain Security
  slug: palo-alto-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 5
skills:
- name: palo-alto-networks-alerts-list-and-view
  slug: palo-alto-networks-alerts-list-and-view
- name: palo-alto-networks-create-and-test-integration
  slug: palo-alto-networks-create-and-test-integration
- name: palo-alto-networks-create-policy
  slug: palo-alto-networks-create-policy
- name: palo-alto-networks-list-and-detail-devices
  slug: palo-alto-networks-list-and-detail-devices
- name: palo-alto-networks-manage-users
  slug: palo-alto-networks-manage-users
slug: palo-alto-networks
solutions:
- description: Next-generation firewall platform including PAN-OS hardware and software firewalls, Panorama management, and Strata Cloud Manager.
  name: Strata Network Security Platform
- description: Cloud-native application protection platform with CSPM, CWPP, code security, DSPM, and CIEM for multi-cloud environments.
  name: Prisma Cloud
- description: Secure access service edge platform combining Prisma Access, SD-WAN, ZTNA, Autonomous DEM, and cloud SWG.
  name: Prisma SASE
- description: Security operations platform with Cortex XDR for detection and response, XSOAR for automation, and XSIAM for AI-driven SOC.
  name: Cortex SecOps
- description: AI runtime security platform for securing generative AI applications with API Intercept scanning and AI Red Teaming.
  name: Prisma AIRS
- description: Threat research and intelligence services including Threat Vault, WildFire malware analysis, DNS Security, and security advisory feeds.
  name: Unit 42 Threat Intelligence
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
use_cases:
- description: Automate alert triage, incident investigation, and response actions using Cortex XDR, XSOAR playbooks, and XSIAM correlation rules.
  name: SOC Automation
- description: Programmatically manage security policies, address objects, and NAT rules across PAN-OS firewalls and Panorama using REST or XML APIs.
  name: Firewall Policy Management
- description: Monitor and remediate cloud misconfigurations, compliance violations, and vulnerabilities across AWS, Azure, and GCP using Prisma Cloud APIs.
  name: Cloud Security Posture
- description: Query threat intelligence databases, submit suspicious files for analysis, and correlate IOCs across Threat Vault, WildFire, and DNS Security.
  name: Threat Hunting
- description: Automate Prisma Access remote network onboarding, SD-WAN site configuration, and ZTNA connector deployment using SASE platform APIs.
  name: SASE Deployment Automation
- description: Embed security scanning into CI/CD pipelines with Prisma Cloud code security APIs for IaC scanning, SCA, and secrets detection.
  name: DevSecOps Pipeline Integration
- description: Integrate Prisma AIRS API Intercept into AI application code to scan LLM prompts and responses for security threats in real time.
  name: AI Application Security
- description: Continuously assess cloud infrastructure against CIS benchmarks, PCI DSS, HIPAA, SOC 2, and custom compliance standards using Prisma Cloud.
  name: Compliance Monitoring
- description: Forward security logs from firewalls and cloud services to Splunk, QRadar, and other SIEMs using Strata Logging Service APIs.
  name: Log Forwarding and SIEM Integration
- description: Manage security across tenant hierarchies with aggregate monitoring, shared notifications, and delegated administration for MSSPs.
  name: Multi-Tenant Security Operations
website: https://www.paloaltonetworks.com
---
