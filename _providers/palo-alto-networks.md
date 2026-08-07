---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.3
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 269
  human_in_the_loop: 5
  name: Palo Alto Networks Agentic Access
  operation_count: 526
  slug: palo-alto-networks-agentic-access
  summary_line: 526 operations · 269 acting · 5 human-in-the-loop
api_count: 482
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
- description: The 5G Deregistered Trend API from Palo Alto Networks — 1 operation(s) for 5g deregistered trend.
  name: Palo Alto Networks 5G Deregistered Trend API
  slug: palo-alto-networks-5g-deregistered-trend-api
- description: The 5G Network Interconnects and Bandwidth API from Palo Alto Networks — 1 operation(s) for 5g network interconnects and bandwidth.
  name: Palo Alto Networks 5G Network Interconnects and Bandwidth API
  slug: palo-alto-networks-5g-network-interconnects-and-bandwidth-api
- description: The 5G Registered Trend API from Palo Alto Networks — 1 operation(s) for 5g registered trend.
  name: Palo Alto Networks 5G Registered Trend API
  slug: palo-alto-networks-5g-registered-trend-api
- description: The 5G Unknown IPs Trend API from Palo Alto Networks — 1 operation(s) for 5g unknown ips trend.
  name: Palo Alto Networks 5G Unknown IPs Trend API
  slug: palo-alto-networks-5g-unknown-ips-trend-api
- description: Access policy management for role-based access control.
  name: Palo Alto Networks Access Policies API
  slug: palo-alto-networks-access-policies-api
- description: The Active Mappings API from Palo Alto Networks — 1 operation(s) for active mappings.
  name: Palo Alto Networks Active Mappings API
  slug: palo-alto-networks-active-mappings-api
- description: The Added and Cleared Mappings API from Palo Alto Networks — 1 operation(s) for added and cleared mappings.
  name: Palo Alto Networks Added and Cleared Mappings API
  slug: palo-alto-networks-added-and-cleared-mappings-api
- description: Address object management.
  name: Palo Alto Networks Addresses API
  slug: palo-alto-networks-addresses-api
- description: Address group management.
  name: Palo Alto Networks AddressGroups API
  slug: palo-alto-networks-addressgroups-api
- description: Query and retrieve PSIRT security advisories.
  name: Palo Alto Networks Advisories API
  slug: palo-alto-networks-advisories-api
- description: Monitored agent and endpoint inventory management.
  name: Palo Alto Networks Agents API
  slug: palo-alto-networks-agents-api
- description: Agent and endpoint experience score monitoring for tracking the health and experience of monitored user devices.
  name: Palo Alto Networks AgentScores API
  slug: palo-alto-networks-agentscores-api
- description: Multi-tenant aggregated data queries.
  name: Palo Alto Networks Aggregation Queries API
  slug: palo-alto-networks-aggregation-queries-api
- description: Alert retrieval and management.
  name: Palo Alto Networks Alerts API
  slug: palo-alto-networks-alerts-api
- description: The API Stats API from Palo Alto Networks — 1 operation(s) for api stats.
  name: Palo Alto Networks API Stats API
  slug: palo-alto-networks-api-stats-api
- description: SaaS application catalog and metadata.
  name: Palo Alto Networks App Catalog API
  slug: palo-alto-networks-app-catalog-api
- description: Monitored application inventory management.
  name: Palo Alto Networks Applications API
  slug: palo-alto-networks-applications-api
- description: Application experience score monitoring providing aggregated performance ratings for SaaS and internal applications.
  name: Palo Alto Networks ApplicationScores API
  slug: palo-alto-networks-applicationscores-api
- description: SaaS application onboarding and management.
  name: Palo Alto Networks Apps API
  slug: palo-alto-networks-apps-api
- description: Internet-exposed asset discovery and enumeration.
  name: Palo Alto Networks Assets API
  slug: palo-alto-networks-assets-api
- description: Advanced Threat Prevention detailed analysis reports and PCAP files.
  name: Palo Alto Networks ATP API
  slug: palo-alto-networks-atp-api
- description: Email attachment retrieval operations.
  name: Palo Alto Networks Attachments API
  slug: palo-alto-networks-attachments-api
- description: Available attack category reference data.
  name: Palo Alto Networks Attack Categories API
  slug: palo-alto-networks-attack-categories-api
- description: Attack surface rule configuration and management.
  name: Palo Alto Networks AttackSurfaceRules API
  slug: palo-alto-networks-attacksurfacerules-api
- description: Audit and management log retrieval.
  name: Palo Alto Networks Audit API
  slug: palo-alto-networks-audit-api
- description: Token-based authentication for API access.
  name: Palo Alto Networks Authentication API
  slug: palo-alto-networks-authentication-api
- description: Bandwidth allocation visibility.
  name: Palo Alto Networks Bandwidth API
  slug: palo-alto-networks-bandwidth-api
- description: Completed assessment report retrieval.
  name: Palo Alto Networks BPA Reports API
  slug: palo-alto-networks-bpa-reports-api
- description: Best Practice Assessment request submission and status tracking.
  name: Palo Alto Networks BPA Requests API
  slug: palo-alto-networks-bpa-requests-api
- description: The Catalog API from Palo Alto Networks — 1 operation(s) for catalog.
  name: Palo Alto Networks Catalog API
  slug: palo-alto-networks-catalog-api
- description: Data classification results and taxonomy operations.
  name: Palo Alto Networks Classifications API
  slug: palo-alto-networks-classifications-api
- description: Cloud account onboarding and management.
  name: Palo Alto Networks CloudAccounts API
  slug: palo-alto-networks-cloudaccounts-api
- description: Configuration commit operations.
  name: Palo Alto Networks Commit API
  slug: palo-alto-networks-commit-api
- description: Compliance posture and reporting.
  name: Palo Alto Networks Compliance API
  slug: palo-alto-networks-compliance-api
- description: Candidate configuration management and job tracking.
  name: Palo Alto Networks Configuration API
  slug: palo-alto-networks-configuration-api
- description: The Configured UE Mappings API from Palo Alto Networks — 1 operation(s) for configured ue mappings.
  name: Palo Alto Networks Configured UE Mappings API
  slug: palo-alto-networks-configured-ue-mappings-api
- description: Logical grouping of ZTNA connectors for high availability.
  name: Palo Alto Networks Connector Groups API
  slug: palo-alto-networks-connector-groups-api
- description: ZTNA connector lifecycle management.
  name: Palo Alto Networks Connectors API
  slug: palo-alto-networks-connectors-api
- description: Running container inventory and security posture.
  name: Palo Alto Networks Containers API
  slug: palo-alto-networks-containers-api
- description: Execute custom data resource queries with filters and aggregations
  name: Palo Alto Networks Custom Queries API
  slug: palo-alto-networks-custom-queries-api
- description: Export data resource results for external processing
  name: Palo Alto Networks Data Exports API
  slug: palo-alto-networks-data-exports-api
- description: Query Prisma Access deployment health and performance data resources
  name: Palo Alto Networks Data Resources API
  slug: palo-alto-networks-data-resources-api
- description: Data asset discovery and inventory operations.
  name: Palo Alto Networks DataAssets API
  slug: palo-alto-networks-dataassets-api
- description: Data pattern configuration and lookup operations.
  name: Palo Alto Networks DataPatterns API
  slug: palo-alto-networks-datapatterns-api
- description: Data store inventory and discovery operations.
  name: Palo Alto Networks DataStores API
  slug: palo-alto-networks-datastores-api
- description: Defender agent deployment and management.
  name: Palo Alto Networks Defenders API
  slug: palo-alto-networks-defenders-api
- description: Browser deployment configuration management.
  name: Palo Alto Networks Deployments API
  slug: palo-alto-networks-deployments-api
- description: The Device API from Palo Alto Networks — 2 operation(s) for device.
  name: Palo Alto Networks Device API
  slug: palo-alto-networks-device-api
- description: IoT and OT device discovery and profiling operations.
  name: Palo Alto Networks Devices API
  slug: palo-alto-networks-devices-api
- description: The Directory Sync Service API from Palo Alto Networks — 3 operation(s) for directory sync service.
  name: Palo Alto Networks Directory Sync Service API
  slug: palo-alto-networks-directory-sync-service-api
- description: Domain categorization and threat intelligence lookups.
  name: Palo Alto Networks Domains API
  slug: palo-alto-networks-domains-api
- description: Email forwarding destination management.
  name: Palo Alto Networks Email Destinations API
  slug: palo-alto-networks-email-destinations-api
- description: Endpoint management, isolation, and scanning.
  name: Palo Alto Networks Endpoints API
  slug: palo-alto-networks-endpoints-api
- description: Investigation entry (work note) management.
  name: Palo Alto Networks Entries API
  slug: palo-alto-networks-entries-api
- description: Code security errors and policy violations by branch.
  name: Palo Alto Networks Errors API
  slug: palo-alto-networks-errors-api
- description: Cloud NGFW firewall instance management.
  name: Palo Alto Networks Firewalls API
  slug: palo-alto-networks-firewalls-api
- description: Automated fix suggestions for pull requests.
  name: Palo Alto Networks Fixes API
  slug: palo-alto-networks-fixes-api
- description: FQDN-based access rules for ZTNA applications.
  name: Palo Alto Networks FQDN Rules API
  slug: palo-alto-networks-fqdn-rules-api
- description: FQDN list management for use in security rule destination criteria.
  name: Palo Alto Networks FQDNLists API
  slug: palo-alto-networks-fqdnlists-api
- description: Host machine security monitoring and vulnerability data.
  name: Palo Alto Networks Hosts API
  slug: palo-alto-networks-hosts-api
- description: HTTPS forwarding destination management.
  name: Palo Alto Networks HTTPS Destinations API
  slug: palo-alto-networks-https-destinations-api
- description: The IDP API from Palo Alto Networks — 9 operation(s) for idp.
  name: Palo Alto Networks IDP API
  slug: palo-alto-networks-idp-api
- description: IKE gateway configuration for establishing IPSec VPN tunnels to Prisma Access.
  name: Palo Alto Networks IKEGateways API
  slug: palo-alto-networks-ikegateways-api
- description: Container image vulnerability and compliance scan data.
  name: Palo Alto Networks Images API
  slug: palo-alto-networks-images-api
- description: Incident management and investigation.
  name: Palo Alto Networks Incidents API
  slug: palo-alto-networks-incidents-api
- description: The Incidents by Severity API from Palo Alto Networks — 1 operation(s) for incidents by severity.
  name: Palo Alto Networks Incidents by Severity API
  slug: palo-alto-networks-incidents-by-severity-api
- description: Data source configuration for log ingestion.
  name: Palo Alto Networks Ingestion API
  slug: palo-alto-networks-ingestion-api
- description: Integration and instance management.
  name: Palo Alto Networks Integrations API
  slug: palo-alto-networks-integrations-api
- description: The Interconnect API from Palo Alto Networks — 6 operation(s) for interconnect.
  name: Palo Alto Networks Interconnect API
  slug: palo-alto-networks-interconnect-api
- description: Investigation management.
  name: Palo Alto Networks Investigations API
  slug: palo-alto-networks-investigations-api
- description: The IP Pool API from Palo Alto Networks — 1 operation(s) for ip pool.
  name: Palo Alto Networks IP Pool API
  slug: palo-alto-networks-ip-pool-api
- description: Owned IP range management.
  name: Palo Alto Networks IPRanges API
  slug: palo-alto-networks-ipranges-api
- description: IPSec tunnel configuration for site-to-site VPN connectivity.
  name: Palo Alto Networks IPSecTunnels API
  slug: palo-alto-networks-ipsectunnels-api
- description: Asynchronous job status tracking.
  name: Palo Alto Networks Jobs API
  slug: palo-alto-networks-jobs-api
- description: LAN network configuration for defining local networks at SD-WAN sites.
  name: Palo Alto Networks LANNetworks API
  slug: palo-alto-networks-lannetworks-api
- description: ZTNA license and entitlement information.
  name: Palo Alto Networks Licenses API
  slug: palo-alto-networks-licenses-api
- description: Prisma Access location data.
  name: Palo Alto Networks Locations API
  slug: palo-alto-networks-locations-api
- description: Log forwarding profile management.
  name: Palo Alto Networks Log Forwarding Profiles API
  slug: palo-alto-networks-log-forwarding-profiles-api
- description: The Mappings Region API from Palo Alto Networks — 1 operation(s) for mappings region.
  name: Palo Alto Networks Mappings Region API
  slug: palo-alto-networks-mappings-region-api
- description: Detailed network performance metrics providing granular visibility into each segment of the user-to-application connection.
  name: Palo Alto Networks Metrics API
  slug: palo-alto-networks-metrics-api
- description: Mobile user agent infrastructure settings for GlobalProtect remote user connectivity.
  name: Palo Alto Networks MobileAgent API
  slug: palo-alto-networks-mobileagent-api
- description: Site performance metrics, application usage data, and alarm monitoring.
  name: Palo Alto Networks Monitoring API
  slug: palo-alto-networks-monitoring-api
- description: The MSSP Account Management API from Palo Alto Networks — 4 operation(s) for mssp account management.
  name: Palo Alto Networks MSSP Account Management API
  slug: palo-alto-networks-mssp-account-management-api
- description: The Mssp License Endpoints API from Palo Alto Networks — 2 operation(s) for mssp license endpoints.
  name: Palo Alto Networks Mssp License Endpoints API
  slug: palo-alto-networks-mssp-license-endpoints-api
- description: The MSSP Managed Tenant Lifecycle Endpoints API from Palo Alto Networks — 3 operation(s) for mssp managed tenant lifecycle endpoints.
  name: Palo Alto Networks MSSP Managed Tenant Lifecycle Endpoints API
  slug: palo-alto-networks-mssp-managed-tenant-lifecycle-endpoints-api
- description: The MSSP Operations Retry API from Palo Alto Networks — 1 operation(s) for mssp operations retry.
  name: Palo Alto Networks MSSP Operations Retry API
  slug: palo-alto-networks-mssp-operations-retry-api
- description: NAT policy rule management.
  name: Palo Alto Networks NATRules API
  slug: palo-alto-networks-natrules-api
- description: 5G network slice configuration and management.
  name: Palo Alto Networks Network Slices API
  slug: palo-alto-networks-network-slices-api
- description: The NotificationProfiles API from Palo Alto Networks — 6 operation(s) for notificationprofiles.
  name: Palo Alto Networks NotificationProfiles API
  slug: palo-alto-networks-notificationprofiles-api
- description: The Notifications API from Palo Alto Networks — 4 operation(s) for notifications.
  name: Palo Alto Networks Notifications API
  slug: palo-alto-networks-notifications-api
- description: Address objects, address groups, service objects, service groups, and tag management.
  name: Palo Alto Networks Objects API
  slug: palo-alto-networks-objects-api
- description: Remote network onboarding status.
  name: Palo Alto Networks Onboarding API
  slug: palo-alto-networks-onboarding-api
- description: Path policy rule management for controlling traffic steering decisions across available WAN links.
  name: Palo Alto Networks PathRules API
  slug: palo-alto-networks-pathrules-api
- description: The Physical Connection API from Palo Alto Networks — 2 operation(s) for physical connection.
  name: Palo Alto Networks Physical Connection API
  slug: palo-alto-networks-physical-connection-api
- description: Playbook listing and execution.
  name: Palo Alto Networks Playbooks API
  slug: palo-alto-networks-playbooks-api
- description: Security policy recommendation operations.
  name: Palo Alto Networks Policies API
  slug: palo-alto-networks-policies-api
- description: 'APIs to interact with the MSSP Backend Service # Authentication'
  name: Palo Alto Networks Policy Group Lifecycle Endpoints API
  slug: palo-alto-networks-policy-group-lifecycle-endpoints-api
- description: 'APIs to interact with the MSSP Backend Service # Authentication'
  name: Palo Alto Networks Policy Group to Tenant Group Management API
  slug: palo-alto-networks-policy-group-to-tenant-group-management-api
- description: Security posture check results and remediation status.
  name: Palo Alto Networks Posture Checks API
  slug: palo-alto-networks-posture-checks-api
- description: IP prefix list management for use in security rule source and destination criteria.
  name: Palo Alto Networks PrefixLists API
  slug: palo-alto-networks-prefixlists-api
- description: Query affected products referenced in security advisories.
  name: Palo Alto Networks Products API
  slug: palo-alto-networks-products-api
- description: Retrieve AI security profiles that define which detection categories are enabled, sensitivity thresholds, and actions to take when threats are detected.
  name: Palo Alto Networks Profiles API
  slug: palo-alto-networks-profiles-api
- description: The Proxy Endpoint Provider API from Palo Alto Networks — 1 operation(s) for proxy endpoint provider.
  name: Palo Alto Networks Proxy Endpoint Provider API
  slug: palo-alto-networks-proxy-endpoint-provider-api
- description: Quality of Service rule management for traffic prioritization across WAN links.
  name: Palo Alto Networks QoSRules API
  slug: palo-alto-networks-qosrules-api
- description: Email recipient retrieval operations.
  name: Palo Alto Networks Recipients API
  slug: palo-alto-networks-recipients-api
- description: The Registered UE Mappings API from Palo Alto Networks — 1 operation(s) for registered ue mappings.
  name: Palo Alto Networks Registered UE Mappings API
  slug: palo-alto-networks-registered-ue-mappings-api
- description: Registry image scanning configuration and results.
  name: Palo Alto Networks Registry API
  slug: palo-alto-networks-registry-api
- description: Content release notes for PAN-OS content updates.
  name: Palo Alto Networks ReleaseNotes API
  slug: palo-alto-networks-releasenotes-api
- description: Remote network IPsec tunnel management.
  name: Palo Alto Networks Remote Networks API
  slug: palo-alto-networks-remote-networks-api
- description: Remote network configuration for connecting branch offices and data centers to Prisma Access via IPSec tunnels.
  name: Palo Alto Networks RemoteNetworks API
  slug: palo-alto-networks-remotenetworks-api
- description: Retrieve detailed analysis reports and supporting files.
  name: Palo Alto Networks Report API
  slug: palo-alto-networks-report-api
- description: DLP reporting and summary operations.
  name: Palo Alto Networks Reports API
  slug: palo-alto-networks-reports-api
- description: VCS repository onboarding and management.
  name: Palo Alto Networks Repositories API
  slug: palo-alto-networks-repositories-api
- description: Data security risk identification and management.
  name: Palo Alto Networks Risks API
  slug: palo-alto-networks-risks-api
- description: Available IAM roles and their permissions.
  name: Palo Alto Networks Roles API
  slug: palo-alto-networks-roles-api
- description: Rule stack management. Rule stacks contain the security policy applied to Cloud NGFW instances.
  name: Palo Alto Networks RuleStacks API
  slug: palo-alto-networks-rulestacks-api
- description: The SaaS Instance API from Palo Alto Networks — 7 operation(s) for saas instance.
  name: Palo Alto Networks SaaS Instance API
  slug: palo-alto-networks-saas-instance-api
- description: 'Scan AI prompts and responses for security threats. Supports synchronous scans that block until analysis is complete, asynchronous scans that return a scan ID for later retrieval, and batch scans for '
  name: Palo Alto Networks Scan API
  slug: palo-alto-networks-scan-api
- description: Vulnerability scan lifecycle management.
  name: Palo Alto Networks Scans API
  slug: palo-alto-networks-scans-api
- description: Script execution and results retrieval.
  name: Palo Alto Networks Scripts API
  slug: palo-alto-networks-scripts-api
- description: RQL-based resource and configuration search.
  name: Palo Alto Networks Search API
  slug: palo-alto-networks-search-api
- description: 5G security policy management.
  name: Palo Alto Networks Security Policies API
  slug: palo-alto-networks-security-policies-api
- description: Security rules within rule stacks.
  name: Palo Alto Networks SecurityRules API
  slug: palo-alto-networks-securityrules-api
- description: Service account management and credential generation.
  name: Palo Alto Networks Service Accounts API
  slug: palo-alto-networks-service-accounts-api
- description: Service connection management for providing access to internal resources through Prisma Access.
  name: Palo Alto Networks ServiceConnections API
  slug: palo-alto-networks-serviceconnections-api
- description: The Services API from Palo Alto Networks — 1 operation(s) for services.
  name: Palo Alto Networks Services API
  slug: palo-alto-networks-services-api
- description: Log forwarding and configuration settings.
  name: Palo Alto Networks Settings API
  slug: palo-alto-networks-settings-api
- description: SD-WAN site management for branch offices, data centers, and remote locations.
  name: Palo Alto Networks Sites API
  slug: palo-alto-networks-sites-api
- description: The Sse API from Palo Alto Networks — 2 operation(s) for sse.
  name: Palo Alto Networks Sse API
  slug: palo-alto-networks-sse-api
- description: The Stack Details Endpoint API from Palo Alto Networks — 1 operation(s) for stack details endpoint.
  name: Palo Alto Networks Stack Details Endpoint API
  slug: palo-alto-networks-stack-details-endpoint-api
- description: Network access and DNS query statistics.
  name: Palo Alto Networks Statistics API
  slug: palo-alto-networks-statistics-api
- description: API usage statistics.
  name: Palo Alto Networks Stats API
  slug: palo-alto-networks-stats-api
- description: File, URL, and link submission for malware analysis.
  name: Palo Alto Networks Submit API
  slug: palo-alto-networks-submit-api
- description: Subnet-based access rules for ZTNA network segments.
  name: Palo Alto Networks Subnet Rules API
  slug: palo-alto-networks-subnet-rules-api
- description: Subscription and license management.
  name: Palo Alto Networks Subscriptions API
  slug: palo-alto-networks-subscriptions-api
- description: Suppression rules for managing policy violations.
  name: Palo Alto Networks Suppressions API
  slug: palo-alto-networks-suppressions-api
- description: Syslog forwarding destination management.
  name: Palo Alto Networks Syslog Destinations API
  slug: palo-alto-networks-syslog-destinations-api
- description: AI scan target definition and management.
  name: Palo Alto Networks Targets API
  slug: palo-alto-networks-targets-api
- description: The Tenant Group Lifecycle Endpoints API from Palo Alto Networks — 2 operation(s) for tenant group lifecycle endpoints.
  name: Palo Alto Networks Tenant Group Lifecycle Endpoints API
  slug: palo-alto-networks-tenant-group-lifecycle-endpoints-api
- description: Tenant Service Group lifecycle management and hierarchy queries.
  name: Palo Alto Networks Tenant Service Groups API
  slug: palo-alto-networks-tenant-service-groups-api
- description: Multi-tenant 5G configuration management.
  name: Palo Alto Networks Tenants API
  slug: palo-alto-networks-tenants-api
- description: Synthetic test results for proactive monitoring of application reachability and performance from user endpoints.
  name: Palo Alto Networks Tests API
  slug: palo-alto-networks-tests-api
- description: Threat signature lookup and metadata retrieval.
  name: Palo Alto Networks Threats API
  slug: palo-alto-networks-threats-api
- description: The Throughput Trend API from Palo Alto Networks — 1 operation(s) for throughput trend.
  name: Palo Alto Networks Throughput Trend API
  slug: palo-alto-networks-throughput-trend-api
- description: The Total Number of Configured Users API from Palo Alto Networks — 1 operation(s) for total number of configured users.
  name: Palo Alto Networks Total Number of Configured Users API
  slug: palo-alto-networks-total-number-of-configured-users-api
- description: The Total Proxies API from Palo Alto Networks — 1 operation(s) for total proxies.
  name: Palo Alto Networks Total Proxies API
  slug: palo-alto-networks-total-proxies-api
- description: The Total Tenants API from Palo Alto Networks — 1 operation(s) for total tenants.
  name: Palo Alto Networks Total Tenants API
  slug: palo-alto-networks-total-tenants-api
- description: The UE IP Region API from Palo Alto Networks — 1 operation(s) for ue ip region.
  name: Palo Alto Networks UE IP Region API
  slug: palo-alto-networks-ue-ip-region-api
- description: The UE Mappings API from Palo Alto Networks — 1 operation(s) for ue mappings.
  name: Palo Alto Networks UE Mappings API
  slug: palo-alto-networks-ue-mappings-api
- description: The Unknown IP Regions API from Palo Alto Networks — 1 operation(s) for unknown ip regions.
  name: Palo Alto Networks Unknown IP  Regions API
  slug: palo-alto-networks-unknown-ip-regions-api
- description: The Unknown UE Mappings API from Palo Alto Networks — 1 operation(s) for unknown ue mappings.
  name: Palo Alto Networks Unknown UE Mappings API
  slug: palo-alto-networks-unknown-ue-mappings-api
- description: The User Authentication API from Palo Alto Networks — 2 operation(s) for user authentication.
  name: Palo Alto Networks User Authentication API
  slug: palo-alto-networks-user-authentication-api
- description: The User Management API from Palo Alto Networks — 5 operation(s) for user management.
  name: Palo Alto Networks User Management API
  slug: palo-alto-networks-user-management-api
- description: Browser user management and session visibility.
  name: Palo Alto Networks Users API
  slug: palo-alto-networks-users-api
- description: Retrieve analysis verdicts by file hash.
  name: Palo Alto Networks Verdict API
  slug: palo-alto-networks-verdict-api
- description: The Vlan Attachment API from Palo Alto Networks — 4 operation(s) for vlan attachment.
  name: Palo Alto Networks Vlan Attachment API
  slug: palo-alto-networks-vlan-attachment-api
- description: Device vulnerability tracking operations.
  name: Palo Alto Networks Vulnerabilities API
  slug: palo-alto-networks-vulnerabilities-api
- description: WAN interface configuration for defining upstream connectivity including ISP links, MPLS circuits, and LTE connections.
  name: Palo Alto Networks WANInterfaces API
  slug: palo-alto-networks-waninterfaces-api
- description: XQL (Extended Query Language) query execution.
  name: Palo Alto Networks XQL API
  slug: palo-alto-networks-xql-api
- description: This API provides access to the Autonomous Digital Experience Management timeseries data. All responses are aggregates over a period of time specified by the start, end, or timerange query parameters.
  name: Palo Alto Networks ADEM data API
  slug: palo-alto-networks-adem-data-api
- description: This Open API spec file was created on May 06, 2026. © 2026 Palo Alto Networks, Inc. Palo Alto Networks is a registered trademark of Palo Alto Networks. A list of our trademarks can be found at [https
  name: Palo Alto Networks Prisma Browser Management Console Public API
  slug: palo-alto-networks-prisma-browser-management-console-public-api
- description: Manages standard data resources.
  name: Palo Alto Networks Data Resource
  slug: palo-alto-networks-data-resource
- description: Manages custom data resources.
  name: Palo Alto Networks Data Resource - Custom
  slug: palo-alto-networks-data-resource-custom
- description: Export data resources.
  name: Palo Alto Networks Data Resource Export
  slug: palo-alto-networks-data-resource-export
- description: The Open API specification file represents the APIs available for Prisma Access Insights 3.0. The Prisma Access Insights 3.0 APIs allow you to query your Prisma Access tenant for the health of your Pr
  name: Palo Alto Networks 3.0 APIs
  slug: palo-alto-networks-30-apis
- description: 'Manages [address objects](https://docs.paloaltonetworks.com/network-security/security-policy/objects/addresses). These allow you to reuse the same object as a source or destination address across all '
  name: Palo Alto Networks Address Management
  slug: palo-alto-networks-address-management
- description: Manages [address groups](https://docs.paloaltonetworks.com/network-security/security-policy/objects/address-groups) that simplify the creation of policy rules. Testing.
  name: Palo Alto Networks Address Group Management
  slug: palo-alto-networks-address-group-management
- description: Manages [anti-spyware profiles](https://docs.paloaltonetworks.com/network-security/security-policy/security-profiles/security-profile-anti-spyware).
  name: Palo Alto Networks Anti-Spyware Profiles
  slug: palo-alto-networks-anti-spyware-profiles
- description: Manages [anti-spyware](https://docs.paloaltonetworks.com/network-security/security-policy/objects/custom-objects/spyware-and-vulnerability) signatures.
  name: Palo Alto Networks Anti-Spyware Signatures
  slug: palo-alto-networks-anti-spyware-signatures
- description: Manages application filters.
  name: Palo Alto Networks Application Filter Management
  slug: palo-alto-networks-application-filter-management
- description: Manages [application groups](https://docs.paloaltonetworks.com/network-security/security-policy/objects/application-groups).
  name: Palo Alto Networks Application Group Management
  slug: palo-alto-networks-application-group-management
- description: Manages application override rules.
  name: Palo Alto Networks Application Override Rules
  slug: palo-alto-networks-application-override-rules
- description: Manages [applications](https://docs.paloaltonetworks.com/network-security/security-policy/objects/applications).
  name: Palo Alto Networks Application Management
  slug: palo-alto-networks-application-management
- description: Manages authentication portals.
  name: Palo Alto Networks Authentication Portals
  slug: palo-alto-networks-authentication-portals
- description: Manages [authentication](https://docs.paloaltonetworks.com/network-security/security-policy/objects/authentication) profiles.
  name: Palo Alto Networks Authentication Profiles
  slug: palo-alto-networks-authentication-profiles
- description: Manages [authentication](https://docs.paloaltonetworks.com/network-security/security-policy/objects/authentication) rules.
  name: Palo Alto Networks Authentication Rules
  slug: palo-alto-networks-authentication-rules
- description: Manages [authentication](https://docs.paloaltonetworks.com/network-security/security-policy/objects/authentication) sequences.
  name: Palo Alto Networks Authentication Sequences
  slug: palo-alto-networks-authentication-sequences
- description: Manages [automatic tag actions](https://docs.paloaltonetworks.com/network-security/security-policy/objects/auto-tag-actions).
  name: Palo Alto Networks Auto Tag Actions
  slug: palo-alto-networks-auto-tag-actions
- description: Manages bandwidth allocations.
  name: Palo Alto Networks Bandwidth Allocations
  slug: palo-alto-networks-bandwidth-allocations
- description: Manages certificates profiles.
  name: Palo Alto Networks Certificate Profiles
  slug: palo-alto-networks-certificate-profiles
- description: Manages certificates.
  name: Palo Alto Networks Certificate Management
  slug: palo-alto-networks-certificate-management
- description: Use these APIs to load, save, and push service configurations.
  name: Palo Alto Networks Manage Prisma Access Configurations
  slug: palo-alto-networks-manage-prisma-access-configurations
- description: Manages [decryption](https://docs.paloaltonetworks.com/network-security/security-policy/objects/decryption-profile) exclusions.
  name: Palo Alto Networks Decryption Exclusion Management
  slug: palo-alto-networks-decryption-exclusion-management
- description: Manages [decryption profiles](https://docs.paloaltonetworks.com/network-security/security-policy/objects/decryption-profile).
  name: Palo Alto Networks Decryption Profile Management
  slug: palo-alto-networks-decryption-profile-management
- description: Manages [decryption](https://docs.paloaltonetworks.com/network-security/security-policy/objects/decryption-profile) rules.
  name: Palo Alto Networks Decryption Rule Management
  slug: palo-alto-networks-decryption-rule-management
- description: Manages [DNS security profiles](https://docs.paloaltonetworks.com/network-security/security-policy/security-profiles/security-profile-dns-security)
  name: Palo Alto Networks DNS Security Profiles
  slug: palo-alto-networks-dns-security-profiles
- description: Manages [Dynamic User Groups](https://docs.paloaltonetworks.com/network-security/security-policy/objects/dynamic-user-groups).
  name: Palo Alto Networks Dynamic User Group Management
  slug: palo-alto-networks-dynamic-user-group-management
- description: Manages [External Dynamic Lists](https://docs.paloaltonetworks.com/network-security/security-policy/objects/external-dynamic-lists).
  name: Palo Alto Networks External Dynamic List Management
  slug: palo-alto-networks-external-dynamic-list-management
- description: Manages [file blocking profiles](https://docs.paloaltonetworks.com/network-security/security-policy/security-profiles/security-profile-file-blocking)
  name: Palo Alto Networks File Blocking Profiles
  slug: palo-alto-networks-file-blocking-profiles
- description: Manages [HIP objects](https://docs.paloaltonetworks.com/network-security/security-policy/objects/hip-objects).
  name: Palo Alto Networks HIP Object Management
  slug: palo-alto-networks-hip-object-management
- description: Manages [HIP Profiles](https://docs.paloaltonetworks.com/network-security/security-policy/objects/hip-profiles).
  name: Palo Alto Networks HIP Profile Management
  slug: palo-alto-networks-hip-profile-management
- description: Manages HTTP header profiles
  name: Palo Alto Networks HTTP Header Profiles
  slug: palo-alto-networks-http-header-profiles
- description: Manages Internet Key Exchange (IKE) Crypto Profiles, which specify protocols and algorithms for identification, authentication, and encryption (IKEv1 or IKEv2, Phase 1).
  name: Palo Alto Networks IKE Crypto Profile Management
  slug: palo-alto-networks-ike-crypto-profile-management
- description: Manages Internet Key Exchange (IKE) Gateway network profiles, which specify the configuration information necessary to perform IKE protocol negotiation with a peer gateway. This is the Phase 1 portion
  name: Palo Alto Networks IKE Gateway Management
  slug: palo-alto-networks-ike-gateway-management
- description: Manages [shared infrastructure settings](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/prisma-access-service-infrastructure/set-up-the-prisma-access-service-
  name: Palo Alto Networks Shared Infrastructure Settings
  slug: palo-alto-networks-shared-infrastructure-settings
- description: Manages [internal DNS servers](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/prisma-access-service-infrastructure/dns).
  name: Palo Alto Networks Internal DNS Servers
  slug: palo-alto-networks-internal-dns-servers
- description: Manages IPSec Crypto Profiles.
  name: Palo Alto Networks IPSec Crypto Profile Management
  slug: palo-alto-networks-ipsec-crypto-profile-management
- description: Manages IPSec tunnel configurations, which allow you to authenticate and/or encrypt the data (IP packets) as they traverse across the tunnel.
  name: Palo Alto Networks IPSec Tunnel Management
  slug: palo-alto-networks-ipsec-tunnel-management
- description: Manages Kerberos server profiles.
  name: Palo Alto Networks Kerberos Server Profiles
  slug: palo-alto-networks-kerberos-server-profiles
- description: Manages LDAP server profiles.
  name: Palo Alto Networks LDAP Server Profiles
  slug: palo-alto-networks-ldap-server-profiles
- description: Retrieve licensing information.
  name: Palo Alto Networks Manage licenses
  slug: palo-alto-networks-manage-licenses
- description: Manages local user groups.
  name: Palo Alto Networks Local User Groups
  slug: palo-alto-networks-local-user-groups
- description: Manages local users.
  name: Palo Alto Networks Local User Managment
  slug: palo-alto-networks-local-user-managment
- description: Retrieve all Prisma Access locations.
  name: Palo Alto Networks Retrieve Prisma Access Locations
  slug: palo-alto-networks-retrieve-prisma-access-locations
- description: Manages multi-factor authentication servers.
  name: Palo Alto Networks Multi-Factor Authentication Servers
  slug: palo-alto-networks-multi-factor-authentication-servers
- description: Manages your mobile agent configuration.
  name: Palo Alto Networks Mobile Agent
  slug: palo-alto-networks-mobile-agent
- description: Manages OCSP responders.
  name: Palo Alto Networks OCSP Responder Management
  slug: palo-alto-networks-ocsp-responder-management
- description: Manages [Profile Groups](https://docs.paloaltonetworks.com/network-security/security-policy/security-profiles/security-profile-groups)
  name: Palo Alto Networks Profile Group Management
  slug: palo-alto-networks-profile-group-management
- description: Manages Quality of Service policy rules.
  name: Palo Alto Networks Quality of Service Policy Rules
  slug: palo-alto-networks-quality-of-service-policy-rules
- description: Manages IPSec tunnel configurations, which allow you to authenticate and/or encrypt the data (IP packets) as they traverse across the tunnel.
  name: Palo Alto Networks Quality of Service Profile Management
  slug: palo-alto-networks-quality-of-service-profile-management
- description: Manages [quarantined devices](https://docs.paloaltonetworks.com/network-security/security-policy/objects/quarantine-device-lists).
  name: Palo Alto Networks Quarantined Device Management
  slug: palo-alto-networks-quarantined-device-management
- description: Manages Radius server profiles.
  name: Palo Alto Networks Radius Server Profiles
  slug: palo-alto-networks-radius-server-profiles
- description: Manages [Regions](https://docs.paloaltonetworks.com/network-security/security-policy/objects/regions).
  name: Palo Alto Networks Region Management
  slug: palo-alto-networks-region-management
- description: Manages Remote Networks.
  name: Palo Alto Networks Remote Network Management
  slug: palo-alto-networks-remote-network-management
- description: Manages SAML server profiles.
  name: Palo Alto Networks SAML Server Profiles
  slug: palo-alto-networks-saml-server-profiles
- description: Manages SCEP profiles.
  name: Palo Alto Networks SCEP Management
  slug: palo-alto-networks-scep-management
- description: Manages [schedules](https://docs.paloaltonetworks.com/network-security/security-policy/objects/schedules).
  name: Palo Alto Networks Schedule Management
  slug: palo-alto-networks-schedule-management
- description: Manages [security rules](https://docs.paloaltonetworks.com/network-security/security-policy/security-rules)
  name: Palo Alto Networks Security Rule Management
  slug: palo-alto-networks-security-rule-management
- description: Manages service connection groups.
  name: Palo Alto Networks Service Connection Groups
  slug: palo-alto-networks-service-connection-groups
- description: Manages [service connections](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/prisma-access-service-connections).
  name: Palo Alto Networks Service Connections
  slug: palo-alto-networks-service-connections
- description: Manages [service groups](https://docs.paloaltonetworks.com/network-security/security-policy/objects/service-groups). Add service objects to a group using the object's name.
  name: Palo Alto Networks Service Groups Management
  slug: palo-alto-networks-service-groups-management
- description: Manages [service objects](https://docs.paloaltonetworks.com/network-security/security-policy/objects/services), which are used to identify network services that applications can or can not use. Networ
  name: Palo Alto Networks Services Management
  slug: palo-alto-networks-services-management
- description: Manages Terminal Access Controller Access-Control System (TACACS) server profiles.
  name: Palo Alto Networks TACACS Server Profiles
  slug: palo-alto-networks-tacacs-server-profiles
- description: Manages [tags](https://docs.paloaltonetworks.com/network-security/security-policy/objects/tags).
  name: Palo Alto Networks Tag Management
  slug: palo-alto-networks-tag-management
- description: Manages TLS Service profiles.
  name: Palo Alto Networks TLS Service Profile Management
  slug: palo-alto-networks-tls-service-profile-management
- description: Manages [traffic steering](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/prisma-access-service-connections/traffic-forwarding) for service connections.
  name: Palo Alto Networks Traffic Steering Rules
  slug: palo-alto-networks-traffic-steering-rules
- description: Manages trusted certificate authorities.
  name: Palo Alto Networks Trusted Certificate Authority Management
  slug: palo-alto-networks-trusted-certificate-authority-management
- description: Manages [URL access](https://docs.paloaltonetworks.com/network-security/security-policy/security-profiles/security-profile-url-filtering) profiles.
  name: Palo Alto Networks URL Access Profiles
  slug: palo-alto-networks-url-access-profiles
- description: Manages [URL Categories](https://docs.paloaltonetworks.com/network-security/security-policy/objects/custom-objects/url-category)
  name: Palo Alto Networks URL Category Management
  slug: palo-alto-networks-url-category-management
- description: Manages [URL Filtering](https://docs.paloaltonetworks.com/network-security/security-policy/security-profiles/security-profile-url-filtering) Categories
  name: Palo Alto Networks URL Filtering Category Management
  slug: palo-alto-networks-url-filtering-category-management
- description: Manages [Vulnerability protection profiles](https://docs.paloaltonetworks.com/network-security/security-policy/security-profiles/security-profile-vulnerability-protection)
  name: Palo Alto Networks Vulnerability Protection Profiles
  slug: palo-alto-networks-vulnerability-protection-profiles
- description: Manages [Vulnerability protection signatures](https://docs.paloaltonetworks.com/network-security/security-policy/objects/custom-objects/spyware-and-vulnerability)
  name: Palo Alto Networks Vulnerability Protection Signatures
  slug: palo-alto-networks-vulnerability-protection-signatures
- description: Manages [WildFire antivirus profiles](https://docs.paloaltonetworks.com/network-security/security-policy/security-profiles/security-profile-wildfire)
  name: Palo Alto Networks WildFire Antivirus Profiles
  slug: palo-alto-networks-wildfire-antivirus-profiles
- description: ZTNA Connector Restful API Specification This Open API spec file was created on March 25, 2026. © 2026 Palo Alto Networks, Inc. Palo Alto Networks is a registered trademark of Palo Alto Networks. A li
  name: Palo Alto Networks ZTNA Connector Restful API
  slug: palo-alto-networks-ztna-connector-restful-api
- description: Action Plan Management APIs
  name: Palo Alto Networks Action Plan Management APIs
  slug: palo-alto-networks-action-plan-management-apis
- description: Programmatically request Best Practice Assessment Data for both free and premium instances of AIOps.
  name: Palo Alto Networks Best Practice Assessment Report APIs
  slug: palo-alto-networks-best-practice-assessment-report-apis
- description: To get email notifications whenever critical issues occur on your network, you can configure Cortex Data Lake to send notifications to an email destination.
  name: Palo Alto Networks Email Profiles
  slug: palo-alto-networks-email-profiles
- description: 'To meet your long-term storage, reporting and monitoring, or legal and compliance needs, you can configure Cortex Data Lake to forward logs to an HTTPS server or to the following SIEMs: - Splunk HTTP '
  name: Palo Alto Networks HTTPS Profiles
  slug: palo-alto-networks-https-profiles
- description: To meet your long-term storage, reporting and monitoring, or legal and compliance needs, you can configure Cortex Data Lake to forward all logs or a subset of logs to a syslog receiver.
  name: Palo Alto Networks Syslog Profiles
  slug: palo-alto-networks-syslog-profiles
- description: Cloud NGFW for AWS supports local and global rulestacks. The Local Account Administrator manages local rulestacks. The AWS Firewall Manager Administrator manages the global rulestacks across the NGFWs
  name: Palo Alto Networks Associate Rulestacks to NGFW
  slug: palo-alto-networks-associate-rulestacks-to-ngfw
- description: 'There are two types of rulestacks: - **Local rulestack**-Consists of local rules and manages them. A local account administrator can associate local rulestacks to an NGFW in their AWS account. - **Glo'
  name: Palo Alto Networks Manage Association Rulestacks
  slug: palo-alto-networks-manage-association-rulestacks
- description: Cloud NGFW uses certificates to access an intelligent feed and to enable outbound decryption. These certificates are stored in the [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/late
  name: Palo Alto Networks Manage Certificate Objects
  slug: palo-alto-networks-manage-certificate-objects
- description: 'Allows you to identify specific file types that you want to block. ### Permission Policies | Action | Local Firewall Administrator | Local Rulestack Administrator | Global Rulestack Administrator| | -'
  name: Palo Alto Networks Manage File Blocking Action
  slug: palo-alto-networks-manage-file-blocking-action
- description: Address objects with type Fully Qualified Domain Name (FQDN). An FQDN object provides further ease of use because DNS provides the FQDN resolution to the IP addresses instead of you needing to know th
  name: Palo Alto Networks Manage FQDN List
  slug: palo-alto-networks-manage-fqdn-list
- description: An intelligent feed, also called an external dynamic list, is a list that you or third-parties can host on an external web server. You can specify the Intelligence Feed as the source or destination of
  name: Palo Alto Networks Manage Intelligent Feed
  slug: palo-alto-networks-manage-intelligent-feed
- description: Log entries contain properties, activities, or behaviors associated with the logged event, such as the application type or the IP address of an attacker. Cloud NGFW can captures threat, traffic, and d
  name: Palo Alto Networks Manage Log Profiles
  slug: palo-alto-networks-manage-log-profiles
- description: Generate JSON Web Token (JWT) to get programmatic access and authenticate API calls.
  name: Palo Alto Networks Manage API Tokens
  slug: palo-alto-networks-manage-api-tokens
- description: Cloud NGFW uses certificates to access an intelligent feed and to enable outbound decryption. These certificates are stored in the [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/late
  name: Palo Alto Networks Manage Certificate Objects (CLOUDNGFW)
  slug: palo-alto-networks-manage-certificate-objects-cloudngfw
- description: Manage commits for rulestacks.
  name: Palo Alto Networks Manage Rulestack Commits
  slug: palo-alto-networks-manage-rulestack-commits
- description: Palo Alto Networks provides a set of predefined URL filtering categories. You can also specify your own URL filtering categories using a customer URL category object. For example, create a custom list
  name: Palo Alto Networks Manage Custom URL Categories
  slug: palo-alto-networks-manage-custom-url-categories
- description: File blocking actions allow you to identify specific file types that you want to block.
  name: Palo Alto Networks Manage File Blocking Actions
  slug: palo-alto-networks-manage-file-blocking-actions
- description: For Fully Qualified Domain Name (FQDN) address objects, DNS provides the FQDN resolution to the IP addresses eliminating the need to manually update them every time you resolve a new IP address. These
  name: Palo Alto Networks Manage FQDN Lists
  slug: palo-alto-networks-manage-fqdn-lists
- description: An intelligent feed, also called an external dynamic list, is a list that you or third-parties can host on an external web server. You can specify the Intelligence Feed as the source or destination of
  name: Palo Alto Networks Manage Intelligent Feeds
  slug: palo-alto-networks-manage-intelligent-feeds
- description: Cloud NGFW for AWS can captures and logs threat, traffic, and decryption profiles. These log entries contain properties, activities, or behaviors associated with an event. For example, application typ
  name: Palo Alto Networks Manage Log Profiles (CLOUDNGFW)
  slug: palo-alto-networks-manage-log-profiles-cloudngfw
- description: Add and modify the user IAM rules and permission policies required to expand or reduce their access and permissions. You can also delete a user. And individual users can view their roles and change th
  name: Palo Alto Networks Manage Cloud NGFW
  slug: palo-alto-networks-manage-cloud-ngfw
- description: The V2 API provides enhanced operations for managing Cloud NGFW resources. This version introduces new features and improvements for firewall management, including support for managing firewalls by ID
  name: Palo Alto Networks Manage Cloud NGFW (V2)
  slug: palo-alto-networks-manage-cloud-ngfw-v2
- description: 'Apply tags to help search and filter your Cloud NGFW resources. ### Permission Policies | Action | Local Firewall Administrator | Local Rulestack Administrator | Global Rulestack Administrator | | ---'
  name: Palo Alto Networks Manage Cloud NGFW Tags
  slug: palo-alto-networks-manage-cloud-ngfw-tags
- description: Use predefined URL categories in security rules to block or allow access to websites.
  name: Palo Alto Networks Manage Predefined URL Categories
  slug: palo-alto-networks-manage-predefined-url-categories
- description: A prefix list allows you to group specific IP addresses that require the same policy enforcement. A prefix list can contain one or more IP addresses or IP netmask in the CIDR notation.
  name: Palo Alto Networks Manage Prefix Lists
  slug: palo-alto-networks-manage-prefix-lists
- description: Rulestacks defines access control (App-ID, URL Filtering) and threat prevention behavior of Cloud NGFW resources. A Cloud NGFW resource uses your rulestack definitions to protect the traffic by a two-
  name: Palo Alto Networks Manage Rulestacks
  slug: palo-alto-networks-manage-rulestacks
- description: 'Apply tags to help search and filter your rulestack resources. ### Permission Policies | Action | Local Firewall Administrator | Local Rulestack Administrator | Global Rulestack Administrator | | ----'
  name: Palo Alto Networks Manage Rulestack Tags
  slug: palo-alto-networks-manage-rulestack-tags
- description: Security rules determine whether to block or allow a session based on traffic attributes such as the source and destination IP address, source and destination FQDNs, or the application. For more infor
  name: Palo Alto Networks Manage Security Rules
  slug: palo-alto-networks-manage-security-rules
- description: Subscribe to Cloud NGFW to start creating your first user; a tenant administrator. A tenant administrator is the highest level of user in the Cloud NGFW service. It provides the ability to add AWS acc
  name: Palo Alto Networks Manage Subscription
  slug: palo-alto-networks-manage-subscription
- description: Use predefined URL categories in security rules to block or allow access to websites.
  name: Palo Alto Networks Manage Predefined URL Categories (CLOUDNGFW)
  slug: palo-alto-networks-manage-predefined-url-categories-cloudngfw
- description: 'A prefix list allows you to group specific IP addresses that require the same policy enforcement. A prefix list can contain one or more IP addresses or IP netmask in CIDR notation. ### Permission Poli'
  name: Palo Alto Networks Manage Prefix List
  slug: palo-alto-networks-manage-prefix-list
- description: Security rules determine whether to block or allow a session based on traffic attributes such as the source and destination IP address, source and destination FQDNs, or the application. All traffic pa
  name: Palo Alto Networks Manage Security Rules (CLOUDNGFW)
  slug: palo-alto-networks-manage-security-rules-cloudngfw
- description: Cloud NGFW requires you to onboard an AWS account to create and manage the resources required by Cloud NGFW. The Cloud NGFW service uses a CloudFormation template (CFT) stack to create these roles nee
  name: Palo Alto Networks User Onboarding using Link Account
  slug: palo-alto-networks-user-onboarding-using-link-account
- description: A link account is an unverified account used to onboard an AWS account to the Cloud NGFW service based on your input. A link account is required to run the Cloud Formation Template (CFT). >**Note:** Y
  name: Palo Alto Networks User Onboarding using Link Account (CLOUDNGFW)
  slug: palo-alto-networks-user-onboarding-using-link-account-cloudngfw
- description: The Cloud NGFW for AWS uses a Cloud Formation Template (CFT) stack to onboard an AWS account and create the roles needed to access the resources in your AWS environment.
  name: Palo Alto Networks User Onboarding using Endpoint Role
  slug: palo-alto-networks-user-onboarding-using-endpoint-role
- description: Cloud NGFW requires you to onboard an AWS account to create and manage the resources required by Cloud NGFW. The Cloud NGFW service uses a CloudFormation Template (CFT) stack to create these roles nee
  name: Palo Alto Networks User Onboarding using Endpoint Role (CLOUDNGFW)
  slug: palo-alto-networks-user-onboarding-using-endpoint-role-cloudngfw
- description: The CheckovVersion endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud CheckovVersion API Overview
  slug: palo-alto-networks-prisma-cloud-checkovversion-api-overview
- description: The CI/CD endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud CI/CD API Overview
  slug: palo-alto-networks-prisma-cloud-cicd-api-overview
- description: The CodeFixes endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud Code Fixes API Overview
  slug: palo-alto-networks-prisma-cloud-code-fixes-api-overview
- description: The Application Security Dashboard endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud Application Security Dashboard API Overview
  slug: palo-alto-networks-prisma-cloud-application-security-dashboard-api-overview
- description: The Development Pipeline endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud Development Pipeline API Overview
  slug: palo-alto-networks-prisma-cloud-development-pipeline-api-overview
- description: The Errors endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud Code Errors API Overview
  slug: palo-alto-networks-prisma-cloud-code-errors-api-overview
- description: The Packages endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud Packages API Overview
  slug: palo-alto-networks-prisma-cloud-packages-api-overview
- description: The Packages Alerts endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud Packages Alerts API Overview
  slug: palo-alto-networks-prisma-cloud-packages-alerts-api-overview
- description: The Policies endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud Policies API Overview
  slug: palo-alto-networks-prisma-cloud-policies-api-overview
- description: The Remediations endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud Remediations API Overview
  slug: palo-alto-networks-prisma-cloud-remediations-api-overview
- description: The Repositories endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud Repositories API Overview
  slug: palo-alto-networks-prisma-cloud-repositories-api-overview
- description: The Repository endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud Repository API Overview
  slug: palo-alto-networks-prisma-cloud-repository-api-overview
- description: Build swagger-compliant REST APIs using TypeScript and Node
  name: Palo Alto Networks TSOA
  slug: palo-alto-networks-tsoa
- description: The Rules endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud Rules API Overview
  slug: palo-alto-networks-prisma-cloud-rules-api-overview
- description: The SBOM endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud SBOM API Overview
  slug: palo-alto-networks-prisma-cloud-sbom-api-overview
- description: The Scans endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud Scans API Overview
  slug: palo-alto-networks-prisma-cloud-scans-api-overview
- description: The Suppressions endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud Suppressions API Overview
  slug: palo-alto-networks-prisma-cloud-suppressions-api-overview
- description: The Tag Rules endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud Tag Rules API Overview
  slug: palo-alto-networks-prisma-cloud-tag-rules-api-overview
- description: The Technologies endpoints are listed below.
  name: Palo Alto Networks Prisma Cloud Technologies API Overview
  slug: palo-alto-networks-prisma-cloud-technologies-api-overview
- description: Prisma Cloud Compute API, published by Palo Alto Networks.
  name: Palo Alto Networks Prisma Cloud Compute API
  slug: palo-alto-networks-prisma-cloud-compute-api
- description: Prisma Cloud Compute API, published by Palo Alto Networks.
  name: Palo Alto Networks Prisma Cloud Compute API (COMPUTE)
  slug: palo-alto-networks-prisma-cloud-compute-api-compute
- description: Access Keys are a secure way to enable programmatic access to the Prisma Cloud API. By default, only the System Admin has API access and can enable API access for other administrators. If you have API
  name: Palo Alto Networks Prisma Cloud Access Keys API Overview
  slug: palo-alto-networks-prisma-cloud-access-keys-api-overview
- description: You can use Account Groups to combine access to multiple cloud accounts with similar or different applications that span multiple divisions or business units, so that you can manage administrative acc
  name: Palo Alto Networks Prisma Cloud Account Groups API Overview
  slug: palo-alto-networks-prisma-cloud-account-groups-api-overview
- description: The Adoption Advisor API provides visibility into which Prisma Cloud capabilities you have adopted and helps you uncover security capabilities that you not have yet explored.
  name: Palo Alto Networks Prisma Adoption Advisor API Overview
  slug: palo-alto-networks-prisma-adoption-advisor-api-overview
- description: Alert rules define what policy violations trigger alerts for cloud accounts within the selected account group and where to send the alert notifications. Alert rules give you a lot of flexibility in ho
  name: Palo Alto Networks Prisma Cloud Alert Rules API Overview
  slug: palo-alto-networks-prisma-cloud-alert-rules-api-overview
- description: 'Prisma Cloud generates an alert when it detects a violation in a policy that is included in an active alert rule. You can use the API requests to manage alerts, including listing or viewing, snoozing '
  name: Palo Alto Networks Prisma Cloud Alerts API Overview
  slug: palo-alto-networks-prisma-cloud-alerts-api-overview
- description: REST interface for Alerts 2.0.
  name: Palo Alto Networks Alerts 2.0 API
  slug: palo-alto-networks-alerts-20-api
- description: On-demand Alert Notification APIs (Alerts side), published by Palo Alto Networks.
  name: Palo Alto Networks On-demand Alert Notification APIs (Alerts side)
  slug: palo-alto-networks-on-demand-alert-notification-apis-alerts-side
- description: Set the enterprise level settings to build standard training models for anomaly detection, alert disposition, and some other global settings such as the timeout before the user is locked out for inact
  name: Palo Alto Networks Prisma Cloud Anomaly Settings and Trusted List API Overview
  slug: palo-alto-networks-prisma-cloud-anomaly-settings-and-trusted-list-api-overview
- description: OpenAPI definition, published by Palo Alto Networks.
  name: Palo Alto Networks OpenAPI definition
  slug: palo-alto-networks-openapi-definition
- description: AppDNA API Specs, published by Palo Alto Networks.
  name: Palo Alto Networks AppDNA API Specs
  slug: palo-alto-networks-appdna-api-specs
- description: 'When you delete an asset in a cloud account that is onboarded on Prisma Cloud, the asset is marked as deleted. After 90 days, the configuration details of the deleted assets are archived. You can use '
  name: Palo Alto Networks Prisma Cloud Archived Assets API Overview
  slug: palo-alto-networks-prisma-cloud-archived-assets-api-overview
- description: The Asset Explorer APIs enable you to list resource information filters, autocomplete suggestions for resource information filter, and list resource scan information.
  name: Palo Alto Networks Prisma Cloud Asset Explorer API Overview
  slug: palo-alto-networks-prisma-cloud-asset-explorer-api-overview
- description: The Asset Inventory APIs provide up-to-date information of all cloud assets that you are monitoring through Prisma Cloud. You can request inventory data, list available filters to narrow inventory req
  name: Palo Alto Networks Prisma Cloud Asset Inventory API Overview
  slug: palo-alto-networks-prisma-cloud-asset-inventory-api-overview
- description: APIs to query data from Unified Asset Inventory (UAI)
  name: Palo Alto Networks APIs to query unified asset
  slug: palo-alto-networks-apis-to-query-unified-asset
- description: The Asset Relationship Type Management APIs enable you to list information about Prisma cloud asset relationship type definitions and asset relationship definitions
  name: Palo Alto Networks Prisma Cloud Asset Relationship Type Manager Definition Overview
  slug: palo-alto-networks-prisma-cloud-asset-relationship-type-manager-definition-overview
- description: As part of compliance requirement for organizations, companies need to demonstrate they are pro-actively tracking security issues and taking steps to remediate issues as they occur. Prisma Cloud Audit
  name: Palo Alto Networks Prisma Cloud Audit Logs API Overview
  slug: palo-alto-networks-prisma-cloud-audit-logs-api-overview
- description: REST APIs of audit log service which manages user audit logs for actions on Prisma Cloud
  name: Palo Alto Networks Audit log service
  slug: palo-alto-networks-audit-log-service
- description: 'Platform: Reporting Service, published by Palo Alto Networks.'
  name: 'Palo Alto Networks Platform: Reporting Service'
  slug: palo-alto-networks-platform-reporting-service
- description: OpenAPI definition, published by Palo Alto Networks.
  name: Palo Alto Networks OpenAPI definition (CSPM)
  slug: palo-alto-networks-openapi-definition-cspm
- description: Prisma Cloud REST API Doc, published by Palo Alto Networks.
  name: Palo Alto Networks Prisma Cloud REST API Doc
  slug: palo-alto-networks-prisma-cloud-rest-api-doc
- description: To monitor the resources on your AWS cloud infrastructure, you must first add your AWS accounts to Prisma Cloud. When you add your cloud account to Prisma Cloud, the API integration between AWS and Pr
  name: Palo Alto Networks AWS Cloud Accounts API Overview
  slug: palo-alto-networks-aws-cloud-accounts-api-overview
- description: APIs for cloudAccount ops
  name: Palo Alto Networks Cloud Accounts API
  slug: palo-alto-networks-cloud-accounts-api
- description: pcs-code-to-cloud API, published by Palo Alto Networks.
  name: Palo Alto Networks pcs-code-to-cloud API
  slug: palo-alto-networks-pcs-code-to-cloud-api
- description: 'Platform: Entitlement Service., published by Palo Alto Networks.'
  name: 'Palo Alto Networks Platform: Entitlement Service.'
  slug: palo-alto-networks-platform-entitlement-service
- description: pcs-command-center API, published by Palo Alto Networks.
  name: Palo Alto Networks pcs-command-center API
  slug: palo-alto-networks-pcs-command-center-api
- description: The Compliance Posture API methods provide information related to your compliance posture across various compliance standards. The filters available through the API enable you to view your status acro
  name: Palo Alto Networks Prisma Cloud Compliance Posture API Overview
  slug: palo-alto-networks-prisma-cloud-compliance-posture-api-overview
- description: You can create your own custom compliance standards that are tailored to your own business needs, standards, and organizational policies. When defining a custom compliance standard, you can add requir
  name: Palo Alto Networks Prisma Cloud Compliance Standards API Overview
  slug: palo-alto-networks-prisma-cloud-compliance-standards-api-overview
- description: Access Keys are a secure way to enable programmatic access to the Prisma Cloud API. By default, only the System Admin has API access and can enable API access for other administrators. If you have API
  name: Palo Alto Networks Prisma Cloud Access Keys API Overview (CSPM)
  slug: palo-alto-networks-prisma-cloud-access-keys-api-overview-cspm
- description: The Data Security capabilities on Prisma Cloud enable you to discover and classify data stored in AWS S3 buckets and protect accidental exposure, misuse, or sharing of sensitive data. The data dashboa
  name: Palo Alto Networks Prisma Cloud Data Security Dashboard API Overview
  slug: palo-alto-networks-prisma-cloud-data-security-dashboard-api-overview
- description: The Data Security capabilities on Prisma Cloud enable you to discover and classify data stored in AWS S3 buckets and protect accidental exposure, misuse, or sharing of sensitive data. The data invento
  name: Palo Alto Networks Prisma Cloud Data Security Inventory API Overview
  slug: palo-alto-networks-prisma-cloud-data-security-inventory-api-overview
- description: config-service API, published by Palo Alto Networks.
  name: Palo Alto Networks config-service API
  slug: palo-alto-networks-config-service-api
- description: Prisma Cloud Data Security enables you to discover and classify data stored in AWS S3 buckets and protect accidental exposure, misuse, or sharing of sensitive data. You can use the data security setti
  name: Palo Alto Networks Prisma Cloud Data Security Settings API Overview
  slug: palo-alto-networks-prisma-cloud-data-security-settings-api-overview
- description: OpenAPI definition, published by Palo Alto Networks.
  name: Palo Alto Networks OpenAPI definition (CSPM) (cspm/EventBridgeMicroService)
  slug: palo-alto-networks-openapi-definition-cspm-cspmeventbridgemicroservice
- description: Prisma Cloud identity and access management (IAM) security integrates with the identity provider (IdP) service Okta to ingest single sign-on (SSO) data for the effective permissions calculation in the
  name: Palo Alto Networks IAM IDP Security API Overview
  slug: palo-alto-networks-iam-idp-security-api-overview
- description: 'Prisma Cloud identity and access management (IAM) security provides: * Visiblity&mdash;Query all relevant IAM entities * Gonvernance&mdash;Monitor your cloud environment for overly-used permissions * '
  name: Palo Alto Networks IAM Security API Overview
  slug: palo-alto-networks-iam-security-api-overview
- description: OpenAPI definition, published by Palo Alto Networks.
  name: Palo Alto Networks OpenAPI definition (CSPM) (cspm/IAMV2MicroService)
  slug: palo-alto-networks-openapi-definition-cspm-cspmiamv2microservice
- description: 'With multiple out-of-the-box integration options, you can integrate Prisma Cloud into security workflows and technologies that already exist in your organization. **Note**: For Prisma Cloud integratio'
  name: Palo Alto Networks Prisma Cloud External Integrations API
  slug: palo-alto-networks-prisma-cloud-external-integrations-api
- description: With Prisma Cloud service’s multiple out-of-the-box integration options, you can integrate Prisma Cloud into existing security workflows and technologies of your organization. You can use [Integration
  name: Palo Alto Networks Prisma Cloud Integration API Overview
  slug: palo-alto-networks-prisma-cloud-integration-api-overview
- description: Manage a list of trusted IP addresses with respect to alerts and a list of trusted login IP addresses.
  name: Palo Alto Networks Prisma Cloud IP Allow List API Overview
  slug: palo-alto-networks-prisma-cloud-ip-allow-list-api-overview
- description: The Prisma Cloud License endpoints enable you to query your Prisma Cloud usage.
  name: Palo Alto Networks Prisma Cloud License API Overview
  slug: palo-alto-networks-prisma-cloud-license-api-overview
- description: 'For secure access to the Prisma Cloud REST API, you need a Prisma Cloud API access key. An access key includes an Access Key ID and a Secret Key. After you use Prisma Cloud to generate an access key, '
  name: Palo Alto Networks Prisma Cloud Login API Overview
  slug: palo-alto-networks-prisma-cloud-login-api-overview
- description: 'Notification templates allow you to configure notifications about the Prisma Cloud alerts to: * Email * ServiceNow * Jira'
  name: Palo Alto Networks Prisma Cloud Notification Template V1 API
  slug: palo-alto-networks-prisma-cloud-notification-template-v1-api
- description: You can use the AWS S3 Flow Logs API for AWS S3 onboarding for organization and standalone accounts on all supported stacks.
  name: Palo Alto Networks Prisma Cloud AWS S3 Flow Logs Overview
  slug: palo-alto-networks-prisma-cloud-aws-s3-flow-logs-overview
- description: Authentication and RBAC API's, published by Palo Alto Networks.
  name: Palo Alto Networks Authentication and RBAC API's
  slug: palo-alto-networks-authentication-and-rbac-apis
- description: OpenAPI definition, published by Palo Alto Networks.
  name: Palo Alto Networks OpenAPI definition (CSPM) (cspm/pia-openapi)
  slug: palo-alto-networks-openapi-definition-cspm-cspmpia-openapi
- description: A policy is a set of one or more constraints or conditions that must be adhered to. Prisma Cloud provides predefined policies for configurations and access controls that adhere to established security
  name: Palo Alto Networks Prisma Cloud User Policy API Overview
  slug: palo-alto-networks-prisma-cloud-user-policy-api-overview
- description: 'Creating compliance reports is the best way to monitor your cloud accounts across all cloud types and ensure that you are adhering to all compliance standards. You can create compliance reports based '
  name: Palo Alto Networks Prisma Cloud Reports API Overview
  slug: palo-alto-networks-prisma-cloud-reports-api-overview
- description: '### Where Do I Find the RRN For My Resource? Where Do I Find the RRN For My Resource?\n\nYou can find the RRN for a resource in the URL when you navigate to **Data Inventory > {Total Objects} > {Objec'
  name: Palo Alto Networks Prisma Cloud Resource Explorer API Overview
  slug: palo-alto-networks-prisma-cloud-resource-explorer-api-overview
- description: A Resource List is a way to identify resources that are assigned with a specific tag or label.
  name: Palo Alto Networks Prisma Cloud Resource Lists API Overview
  slug: palo-alto-networks-prisma-cloud-resource-lists-api-overview
- description: Satellite Management APIs, published by Palo Alto Networks.
  name: Palo Alto Networks Satellite Management APIs
  slug: palo-alto-networks-satellite-management-apis
- description: The Search Manager APIs enable you to manage your recent and saved Resource Query Language (RQL) queries.
  name: Palo Alto Networks Prisma Cloud Search Manager API Overview
  slug: palo-alto-networks-prisma-cloud-search-manager-api-overview
- description: You can use the Resource Query Language (RQL) to perform configuration checks across cloud services as well as gain real-time insights into user and network events to gain security visibility and crea
  name: Palo Alto Networks Prisma Cloud RQL APIs
  slug: palo-alto-networks-prisma-cloud-rql-apis
- description: Manage enterprise settings such as a user inactivity timeout, user attribution for alerts, and global settings for policies and alerts.
  name: Palo Alto Networks Prisma Cloud Enterprise Settings API Overview
  slug: palo-alto-networks-prisma-cloud-enterprise-settings-api-overview
- description: Quickly check if Prisma Cloud is available.
  name: Palo Alto Networks Prisma Cloud System API Overview
  slug: palo-alto-networks-prisma-cloud-system-api-overview
- description: Manage your Prisma Cloud user profiles.
  name: Palo Alto Networks Prisma Cloud User Profile API Overview
  slug: palo-alto-networks-prisma-cloud-user-profile-api-overview
- description: Manage your Prisma Cloud user roles.
  name: Palo Alto Networks Prisma Cloud User Roles API Overview
  slug: palo-alto-networks-prisma-cloud-user-roles-api-overview
- description: UVE Dashboard Widgets
  name: Palo Alto Networks UVE Doc
  slug: palo-alto-networks-uve-doc
- description: OpenAPI definition, published by Palo Alto Networks.
  name: Palo Alto Networks OpenAPI definition (CSPM) (cspm/UVERemediationMicroservice)
  slug: palo-alto-networks-openapi-definition-cspm-cspmuveremediationmicroservice
- description: UVE Search
  name: Palo Alto Networks UVE Doc (CSPM)
  slug: palo-alto-networks-uve-doc-cspm
- description: These APIs are used to fetch the data from some of the widgets that are used to create custom dashboard.
  name: Palo Alto Networks Prisma Cloud Widgets API
  slug: palo-alto-networks-prisma-cloud-widgets-api
- description: Prisma Cloud Compute API, published by Palo Alto Networks.
  name: Palo Alto Networks Prisma Cloud Compute API (CWPP)
  slug: palo-alto-networks-prisma-cloud-compute-api-cwpp
- description: Prisma Cloud Compute API, published by Palo Alto Networks.
  name: Palo Alto Networks Prisma Cloud Compute API (CWPP) (cwpp/openapi-34-04-145-saas)
  slug: palo-alto-networks-prisma-cloud-compute-api-cwpp-cwppopenapi-34-04-145-saas
- description: Manage data patterns used for detecting sensitive information such as PII, financial data, healthcare information, and custom patterns. Create, update, and configure detection patterns with various te
  name: Palo Alto Networks Data Patterns API v2
  slug: palo-alto-networks-data-patterns-api-v2
- description: Create and manage data profiles that define collections of data patterns for incident detection. Organize multiple data patterns into logical profiles for comprehensive data protection strategies.
  name: Palo Alto Networks Data Profiles API v2
  slug: palo-alto-networks-data-profiles-api-v2
- description: Create and manage custom dictionaries for data pattern matching and detection. Build domain-specific dictionaries to enhance detection accuracy for industry-specific sensitive information.
  name: Palo Alto Networks Dictionaries API v2
  slug: palo-alto-networks-dictionaries-api-v2
- description: DLP Public API
  name: Palo Alto Networks public dlp apis
  slug: palo-alto-networks-public-dlp-apis
- description: Manage document type classifications for enhanced document scanning and categorization. Define custom document types to improve detection accuracy and enable type-specific DLP policies.
  name: Palo Alto Networks Document Types API v2
  slug: palo-alto-networks-document-types-api-v2
- description: Manage Exact Data Matching (EDM) datasets for precise detection of sensitive content. Upload and maintain EDM datasets containing specific sensitive data such as customer lists, employee records, or f
  name: Palo Alto Networks EDM Datasets API v2
  slug: palo-alto-networks-edm-datasets-api-v2
- description: Manage endpoint DLP policies for controlling data loss prevention on endpoint devices. Create, update, retrieve, and delete policies that define DLP rules and actions for endpoint protection.
  name: Palo Alto Networks Endpoint Policies API v2
  slug: palo-alto-networks-endpoint-policies-api-v2
- description: Beta Incidents API providing advanced incident management features including paginated retrieval, comprehensive filtering and sorting, batch incident updates, and signed URL generation for secure inci
  name: Palo Alto Networks Incidents API (Beta)
  slug: palo-alto-networks-incidents-api-beta
- description: Manage and retrieve DLP incidents across v1 and v2 endpoints. This API group provides comprehensive incident lifecycle management including retrieval with advanced filtering, assignment management, no
  name: Palo Alto Networks Incidents API (DLP)
  slug: palo-alto-networks-incidents-api-dlp
- description: Optical Character Recognition (OCR) enablement APIs for enhanced document scanning and text extraction capabilities. Enable OCR processing to detect sensitive information in scanned documents and imag
  name: Palo Alto Networks OCR Enablement API v2
  slug: palo-alto-networks-ocr-enablement-api-v2
- description: Manage peripheral device configurations and policies for DLP protection. Configure USB devices, printers, and other peripherals to enforce DLP policies and prevent unauthorized data transfers.
  name: Palo Alto Networks Peripherals API v2
  slug: palo-alto-networks-peripherals-api-v2
- description: Retrieve and analyze DLP scan reports containing comprehensive metadata and detection information about files and payloads. Reports provide detailed insights into pattern matches, detection techniques
  name: Palo Alto Networks Reports API (DLP)
  slug: palo-alto-networks-reports-api-dlp
- description: dnssec.public_api, published by Palo Alto Networks.
  name: Palo Alto Networks dnssec.public_api
  slug: palo-alto-networks-dnssecpublic-api
- description: Dig Security public API, published by Palo Alto Networks.
  name: Palo Alto Networks Dig Security public API
  slug: palo-alto-networks-dig-security-public-api
- description: 'Programmatically request [Email incidents](https://docs.paloaltonetworks.com/enterprise-dlp/enterprise-dlp-admin/configure-enterprise-dlp/email-dlp/how-does-email-dlp-work) as an additional vector of '
  name: Palo Alto Networks Email DLP APIs
  slug: palo-alto-networks-email-dlp-apis
- description: Please refer [IoT Public API Authentication](/iot/api/iot-public-api-new) to know how to get API Bearer token<br/>
  name: Palo Alto Networks IoT Public API Overview
  slug: palo-alto-networks-iot-public-api-overview
- description: 'APIs to interact with the MSSP Backend Service # Authentication'
  name: 'Palo Alto Networks Prisma Cloud: Managed Security Service Provider (MSSP)'
  slug: palo-alto-networks-prisma-cloud-managed-security-service-provider-mssp
- description: OpenAPI Specification for Prisma AIRS AI Runtime API Management Service
  name: Palo Alto Networks Prisma AIRS API Management service
  slug: palo-alto-networks-prisma-airs-api-management-service
- description: Model Security Data Plane API - Execute scans and manage model data This Open API spec file was created on May 04, 2026. © 2026 Palo Alto Networks, Inc. Palo Alto Networks is a registered trademark of
  name: Palo Alto Networks Prisma AIRS AI Model Security API
  slug: palo-alto-networks-prisma-airs-ai-model-security-api
- description: Use the Model Security Data Plane API to execute scans and manage your model data securely. This Open API spec file was created on February 24, 2026. © 2026 Palo Alto Networks, Inc. Palo Alto Networks
  name: Palo Alto Networks Prisma AIRS AI Model Security API (PRISMA-AIRS-MODEL-SECURITY)
  slug: palo-alto-networks-prisma-airs-ai-model-security-api-prisma-airs-model-security
- description: Configure and manage security groups and rules for AI/ML model scanning using the Model Security Management API. This Open API spec file was created on February 24, 2026. © 2026 Palo Alto Networks, In
  name: Palo Alto Networks Prisma AIRS AI Security Model API
  slug: palo-alto-networks-prisma-airs-ai-security-model-api
- description: Red Teaming Data Plane API - Data processing and scanning services for AI/ML model security. © 2025 Palo Alto Networks, Inc
  name: Palo Alto Networks Prisma AIRS Red Teaming Dataplane API
  slug: palo-alto-networks-prisma-airs-red-teaming-dataplane-api
- description: Red Teaming Management API - Configure and manage security groups and rules for AI/ML model scanning. © 2025 Palo Alto Networks, Inc
  name: Palo Alto Networks Prisma AIRS Red Teaming Management API
  slug: palo-alto-networks-prisma-airs-red-teaming-management-api
- description: OpenAPI spec for AIRT Network Channels © 2025 Palo Alto Networks, Inc This Open API spec file was created on April 14, 2026. © 2026 Palo Alto Networks, Inc. Palo Alto Networks is a registered trademar
  name: Palo Alto Networks Prisma AIRS Red Teaming - Network Channel API
  slug: palo-alto-networks-prisma-airs-red-teaming-network-channel-api
- description: 'This Open API spec file represents the APIs available for the Prisma AIRS AI Runtime: API Intercept. These APIs use the API key authentication and base URL. To use the APIs, you must first activate an'
  name: Palo Alto Networks Prisma AIRS AI Runtime API Intercept
  slug: palo-alto-networks-prisma-airs-ai-runtime-api-intercept
- description: This service is used to obtain access tokens, and inspect user information found on the access token.
  name: Palo Alto Networks Authentication Service API
  slug: palo-alto-networks-authentication-service-api
- description: To create a Remote Network that is part of Prisma Access, Configuration Orchestration APIs enable you to configure Remote Network tunnels directly. Prisma Access Configuration Orchestration API’s prov
  name: Palo Alto Networks Configuration Orchestration API
  slug: palo-alto-networks-configuration-orchestration-api
- description: Access policies describe what actions a user or service account can take. These are role-based, where each [role](/sase/api/iam/roles) is defined by a collection of one or more [permissions](/sase/api
  name: Palo Alto Networks Access Policies
  slug: palo-alto-networks-access-policies
- description: Manage [custom roles](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/add-custom-roles). When you create a custom role, you can use p
  name: Palo Alto Networks Custom Roles
  slug: palo-alto-networks-custom-roles
- description: A single permission identifies an action that can be taken when you [grant a permission](/sase/api/iam/accesspolicies) to a user or service account. Permissions identify the resource to which the perm
  name: Palo Alto Networks Permissions
  slug: palo-alto-networks-permissions
- description: Manage permission sets. Permission sets are intended to be used when creating custom roles that grant UI access to a user.
  name: Palo Alto Networks Permission Sets
  slug: palo-alto-networks-permission-sets
- description: Roles are used to identify a collection of [permissions](/sase/api/iam/permissions) that are granted to a user or service account. Roles are assigned to a user or service account using [access policie
  name: Palo Alto Networks Roles
  slug: palo-alto-networks-roles
- description: Service accounts are used to obtain authentication tokens. As such, their use is required only for API access to Prisma SASE services. You apply one or more [access policies](/sase/api/iam/accesspolic
  name: Palo Alto Networks Service Accounts
  slug: palo-alto-networks-service-accounts
- description: Create Palo Alto Networks SSO accounts, and verify login accounts. A [login account](/sase/docs/user-accounts#log-in-accounts), as well as an [access policy](/sase/api/iam/accesspolicies), is required
  name: Palo Alto Networks User Accounts
  slug: palo-alto-networks-user-accounts
- description: Endpoint to retrieve Identity Posture Security information This Open API spec file was created on July 01, 2025. © 2025 Palo Alto Networks, Inc. Palo Alto Networks is a registered trademark of Palo Al
  name: Palo Alto Networks Incident Security Service Posture Management API
  slug: palo-alto-networks-incident-security-service-posture-management-api
- description: The SASE 5G Management Service provides the administrative framework required to provision, configure, and oversee 5G security infrastructure within the Strata Cloud Manager (SCM) ecosystem. Architect
  name: Palo Alto Networks SASE 5G Manage Service API
  slug: palo-alto-networks-sase-5g-manage-service-api
- description: The SASE 5G Monitoring Service provides real-time visibility and technical telemetry for enterprise 5G infrastructure within the Strata Cloud Manager (SCM) ecosystem. Technical leads and network analy
  name: Palo Alto Networks SASE 5G Monitor Service API
  slug: palo-alto-networks-sase-5g-monitor-service-api
- description: 'These APIs provide the administrative tools necessary to configure and manage the lifecycle of Service Provider (SP) Interconnects and virtual VlanAttachments within the management plane. They enable '
  name: Palo Alto Networks SP Interconnect Manage APIs
  slug: palo-alto-networks-sp-interconnect-manage-apis
- description: These APIs deliver real-time visibility and performance analytics for all configured interconnect resources through the monitoring plane. They allow network teams to track health, bandwidth throughput
  name: Palo Alto Networks SP Interconnect Monitor APIs
  slug: palo-alto-networks-sp-interconnect-monitor-apis
- description: This Open API spec file represents the APIs available for [Palo Alto Networks Aggregate Monitoring](https://docs.paloaltonetworks.com/NEED-URL) APIs. After you have configured your tenants, these APIs
  name: Palo Alto Networks Aggreagate Monitoring APIs
  slug: palo-alto-networks-aggreagate-monitoring-apis
- description: Multi-Tenant Notifications API, published by Palo Alto Networks.
  name: Palo Alto Networks Multi-Tenant Notifications API
  slug: palo-alto-networks-multi-tenant-notifications-api
- description: The Prisma Browser for MSP API provides a suite of endpoints to automate the management of security services for the SMB market. This API allows developers to programmatically create and configure new
  name: Palo Alto Networks Prisma Browser for MSP API
  slug: palo-alto-networks-prisma-browser-for-msp-api
- description: '© 2025 Palo Alto Networks, Inc This Open API spec file was created on March 02, 2026. © 2026 Palo Alto Networks, Inc. Palo Alto Networks is a registered trademark of Palo Alto Networks. A list of our '
  name: Palo Alto Networks SSPM Management API
  slug: palo-alto-networks-sspm-management-api
- description: Manage application instances.
  name: Palo Alto Networks Instances
  slug: palo-alto-networks-instances
- description: Manage instance licenses.
  name: Palo Alto Networks Licenses
  slug: palo-alto-networks-licenses
- description: Manages tenant service groups.
  name: Palo Alto Networks Tenant Service Group
  slug: palo-alto-networks-tenant-service-group
- description: This service is used to obtain access tokens, and inspect user information found on the access token.
  name: Palo Alto Networks Authentication Service API (SCM)
  slug: palo-alto-networks-authentication-service-api-scm
- description: These APIs are used to define how Advanced DNS Security Resolver configurations are implemented.
  name: Palo Alto Networks Advanced DNS Security Resolver Configuration
  slug: palo-alto-networks-advanced-dns-security-resolver-configuration
- description: Cloud Dynamic User Groups (CDUG) API for managing dynamic user groups in the Directory Sync Service. This API provides endpoints for creating, updating, retrieving, and deleting Cloud Dynamic User Gro
  name: Palo Alto Networks CIE - Cloud Dynamic User Group CRUD Operations APIs Mounted on Strata Cloud Manager
  slug: palo-alto-networks-cie-cloud-dynamic-user-group-crud-operations-apis-mounted-on-strata-cloud-manager
- description: Use the CIE Directory Sync API to retrieve real-time user, group, and domain information from your connected directories. This guide provides the details needed to integrate identity-aware context int
  name: Palo Alto Networks CIE Directory Sync Service APIs Mounted on Strata Cloud Manager
  slug: palo-alto-networks-cie-directory-sync-service-apis-mounted-on-strata-cloud-manager
- description: These APIs are used for defining and managing identity services configurations within Strata Cloud Manager.
  name: Palo Alto Networks Identity Services
  slug: palo-alto-networks-identity-services
- description: These APIs are used for defining and managing network services configuration within Strata Cloud Manager.
  name: Palo Alto Networks Network Services
  slug: palo-alto-networks-network-services
- description: These APIs are used for defining and managing policy object configurations within Strata Cloud Manager.
  name: Palo Alto Networks Objects
  slug: palo-alto-networks-objects
- description: These APIs are used for Prisma Access and NGFW operations within Strata Cloud Manager.
  name: Palo Alto Networks Config Operations
  slug: palo-alto-networks-config-operations
- description: These APIs are used for defining and managing security services configurations within Strata Cloud Manager.
  name: Palo Alto Networks Security Services
  slug: palo-alto-networks-security-services
- description: These APIs are used to define how Strata Cloud Manager configurations are implemented.
  name: Palo Alto Networks Configuration Setup
  slug: palo-alto-networks-configuration-setup
- description: These APIs are used to define Strata Cloud Manager device onboarding workflows.
  name: Palo Alto Networks Device Onboarding
  slug: palo-alto-networks-device-onboarding
- description: Consolidates security and operational incidents from multiple PaloAlto Networks products into a unified management interface. Provides read-only access to search, filter, and analyze incident data acr
  name: Palo Alto Networks Unified Incident Framework APIs
  slug: palo-alto-networks-unified-incident-framework-apis
- description: These APIs are used for defining and managing device configurations within Strata Cloud Manager.
  name: Palo Alto Networks Device Settings
  slug: palo-alto-networks-device-settings
- description: These APIs can be used to retrieve operational data on your devices, for management and troubleshooting purposes.
  name: Palo Alto Networks Operations and Troubleshooting
  slug: palo-alto-networks-operations-and-troubleshooting
- description: Use the TLS Protect Cloud APIs to manage certificates, certificate requests, applications, machine identities, users, teams, event logs, and more. This Open API spec file was created on June 04, 2026.
  name: Palo Alto Networks TLS Protect Cloud API for Strata Cloud Manager
  slug: palo-alto-networks-tls-protect-cloud-api-for-strata-cloud-manager
- description: Create and manage compliance frameworks with scoring and benchmark monitoring.
  name: Palo Alto Networks Compliance Center API
  slug: palo-alto-networks-compliance-center-api
- description: 'This API provides comprehensive posture management capabilities including: - Custom posture check management (create, update, delete, clone, batch operations) - Config file upload for BPA (Best Practi'
  name: Palo Alto Networks Posture Management API
  slug: palo-alto-networks-posture-management-api
- description: These APIs are used for defining and managing Prisma Access Remote Network and Service Connection configurations within Strata Cloud Manager.
  name: Palo Alto Networks Network Deployment
  slug: palo-alto-networks-network-deployment
- description: These APIs are used for defining and managing Prisma Access GlobalProtect services within Strata Cloud Manager.
  name: Palo Alto Networks GlobalProtect
  slug: palo-alto-networks-globalprotect
- description: Access policies describe what actions a user or service account can take. These are role-based, where each [role](/scm/api/iam/roles) is defined by a collection of one or more [permissions](/scm/api/i
  name: Palo Alto Networks Access Policies (SCM)
  slug: palo-alto-networks-access-policies-scm
- description: Manage [custom roles](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/add-custom-roles). When you create a custom role, you can use p
  name: Palo Alto Networks Custom Roles (SCM)
  slug: palo-alto-networks-custom-roles-scm
- description: A single permission identifies an action that can be taken when you [grant a permission](/scm/api/iam/accesspolicies) to a user or service account. Permissions identify the resource to which the permi
  name: Palo Alto Networks Permissions (SCM)
  slug: palo-alto-networks-permissions-scm
- description: Manage permission sets. Permission sets are intended to be used when creating custom roles that grant UI access to a user.
  name: Palo Alto Networks Permission Sets (SCM)
  slug: palo-alto-networks-permission-sets-scm
- description: Roles are used to identify a collection of [permissions](/scm/api/iam/permissions) that are granted to a user or service account. Roles are assigned to a user or service account using [access policies
  name: Palo Alto Networks Roles (SCM)
  slug: palo-alto-networks-roles-scm
- description: Service accounts are used to obtain authentication tokens. As such, their use is required only for API access to Prisma SASE services. You apply one or more [access policies](/scm/api/iam/accesspolici
  name: Palo Alto Networks Service Accounts (SCM)
  slug: palo-alto-networks-service-accounts-scm
- description: Create Palo Alto Networks SSO accounts, and verify login accounts. A [login account](/scm/docs/user-accounts#log-in-accounts), as well as an [access policy](/scm/api/iam/accesspolicies), is required i
  name: Palo Alto Networks User Accounts (SCM)
  slug: palo-alto-networks-user-accounts-scm
- description: Manage application instances.
  name: Palo Alto Networks Instances (SCM)
  slug: palo-alto-networks-instances-scm
- description: Manages tenant service groups.
  name: Palo Alto Networks Tenant Service Group (SCM)
  slug: palo-alto-networks-tenant-service-group-scm
- description: List of APIs used to retrieve the Autonomous DEM status in Prisma SD-WAN.
  name: Palo Alto Networks ADEM
  slug: palo-alto-networks-adem
- description: List of APIs used to manage an application definition specific query, overrides, and version information.
  name: Palo Alto Networks Applications
  slug: palo-alto-networks-applications
- description: Query APIs used to retrieve audit logs.
  name: Palo Alto Networks Auditlogs
  slug: palo-alto-networks-auditlogs
- description: APIs to manage bulk site templates and deployments.
  name: Palo Alto Networks Bulk Configurations
  slug: palo-alto-networks-bulk-configurations
- description: List of APIs used to manage the bulk configuations query and metrics.
  name: Palo Alto Networks Bulk Operations
  slug: palo-alto-networks-bulk-operations
- description: List of APIs used to manage the cellular device, services, APN profiles, and modules.
  name: Palo Alto Networks Cellular
  slug: palo-alto-networks-cellular
- description: APIs to manage certificates and certificate authorities.
  name: Palo Alto Networks Certificates
  slug: palo-alto-networks-certificates
- description: List of APIs used to retrieve cloudblade configurations and status.
  name: Palo Alto Networks CloudBlades
  slug: palo-alto-networks-cloudblades
- description: List of APIs used to manage your device software to upgrade, retrieve available software images, and upgrade status information.
  name: Palo Alto Networks Device Configuration
  slug: palo-alto-networks-device-configuration
- description: List of APIs to read and configure switching capabilities.
  name: Palo Alto Networks Device Switch Config
  slug: palo-alto-networks-device-switch-config
- description: List of APIs used to manage the DHCP servers.
  name: Palo Alto Networks DHCP
  slug: palo-alto-networks-dhcp
- description: List of APIs used to manage the DNS services.
  name: Palo Alto Networks DNS Services
  slug: palo-alto-networks-dns-services
- description: List of APIs used to manage the event policy rules that inlcude managing of event correlation policy rules and sets and querying of the rules and sets.
  name: Palo Alto Networks Event Policy
  slug: palo-alto-networks-event-policy
- description: List of APIs used to retrieve events, manage the event policy rules that include managing of event correlation policy rules and sets and querying of the rules and sets.
  name: Palo Alto Networks Events
  slug: palo-alto-networks-events
- description: List of APIs used to retrieve IoT specific configuration like device IDs and more.
  name: Palo Alto Networks IoT
  slug: palo-alto-networks-iot
- description: List of APIs used to manage the IPFIX services.
  name: Palo Alto Networks IPFIX
  slug: palo-alto-networks-ipfix
- description: List of APIs used to retrieve SDWAN metrics such as badnwidth utilization, TCP transaction, application health, application performance, LQM, flows, interface & system metrics.
  name: Palo Alto Networks Metrics
  slug: palo-alto-networks-metrics
- description: APIs to retrieve monitoring insights, analytics, and distribution metrics for SD-WAN environments.
  name: Palo Alto Networks Monitoring
  slug: palo-alto-networks-monitoring
- description: List of APIs used to manage multicast specific configurations.
  name: Palo Alto Networks Multicast
  slug: palo-alto-networks-multicast
- description: List of APIs used to manage the NAT policy rules.
  name: Palo Alto Networks NAT Policy
  slug: palo-alto-networks-nat-policy
- description: List of APIs used to manage Network constructs in Prisma SD-WAN like WAN Networks, LAN Networks, Circuit labels, and Network Contexts. All these are used to define a circuit and create policies.
  name: Palo Alto Networks Network Constructs
  slug: palo-alto-networks-network-constructs
- description: List of APIs used to manage NTP.
  name: Palo Alto Networks NTP
  slug: palo-alto-networks-ntp
- description: List of APIs used to manage OSPF routing configurations.
  name: Palo Alto Networks OSPF
  slug: palo-alto-networks-ospf
- description: List of APIs used to manage the network path policy rules.
  name: Palo Alto Networks Path Policy
  slug: palo-alto-networks-path-policy
- description: List of APIs used to manage the original path policies rules.
  name: Palo Alto Networks Path Policy Original
  slug: palo-alto-networks-path-policy-original
- description: List of APIs used to manage performance management policy rules and rule sets.
  name: Palo Alto Networks Performance Management
  slug: palo-alto-networks-performance-management
- description: List of APIs used to manage performance policy.
  name: Palo Alto Networks Performance Policy
  slug: palo-alto-networks-performance-policy
- description: List of APIs used to manage Prisma Access configurations, networks, and connections.
  name: Palo Alto Networks Prisma Access Configs
  slug: palo-alto-networks-prisma-access-configs
- description: List of APIs used to manage the QoS policies.
  name: Palo Alto Networks QOS Policy
  slug: palo-alto-networks-qos-policy
- description: List of APIs used to manage and retrieve report files.
  name: Palo Alto Networks Reports
  slug: palo-alto-networks-reports
- description: List of APIs used to configure all routing contructs like, BGP configs, static routes, AS paths, and community lists.
  name: Palo Alto Networks Routing
  slug: palo-alto-networks-routing
- description: List of APIs used manage the SASE configurations.
  name: Palo Alto Networks SASE Fabric
  slug: palo-alto-networks-sase-fabric
- description: APIs to manage SD-WAN apps, status, and app acceleration.
  name: Palo Alto Networks SD-WAN Applications
  slug: palo-alto-networks-sd-wan-applications
- description: List of APIs used to manage your security policy rules that include security zones, element security zones, site security zones, global prefix filters, local prefix filters, security policy rule order
  name: Palo Alto Networks Security Policy
  slug: palo-alto-networks-security-policy
- description: List of APIs used to manage the DC groups, service endpoints and service mappings. It is used to classify sites (Data Centers) into DC groups and external service groups.
  name: Palo Alto Networks Service & DC Groups
  slug: palo-alto-networks-service-dc-groups
- description: List of APIs used to manage the Syslog servers.
  name: Palo Alto Networks Services
  slug: palo-alto-networks-services
- description: List of APIs used to manage your site specific configuration attributes, and HA configuration for both branch and data center sites.
  name: Palo Alto Networks Site Configuration
  slug: palo-alto-networks-site-configuration
- description: APIs to manage and query site snapshots.
  name: Palo Alto Networks Site Snapshots
  slug: palo-alto-networks-site-snapshots
- description: List of APIs that allow you to create customized site configuration templates that cater to your deployment requirements. This helps in efficiently deploying branches and data centers at scale.
  name: Palo Alto Networks Site Templates
  slug: palo-alto-networks-site-templates
- description: List of APIs used to manage SNMP.
  name: Palo Alto Networks SNMP
  slug: palo-alto-networks-snmp
- description: List of APIs used to manage your device software to upgrade, retrieve available software images, and upgrade status information.
  name: Palo Alto Networks Software Management
  slug: palo-alto-networks-software-management
- description: List of APIs used to manage the operators, IDPs, users, base roles, base permissions, password change, sign up, client roles, licenses, and incident management.
  name: Palo Alto Networks System Administration
  slug: palo-alto-networks-system-administration
- description: List of APIs used to manage the network topology, WAN Overlays, VPN Links, and Secure Fabric Links.
  name: Palo Alto Networks Topology
  slug: palo-alto-networks-topology
- description: List of APIs used to retrieve details about User & Group identity
  name: Palo Alto Networks User Groups
  slug: palo-alto-networks-user-groups
- description: The Advanced Threat Prevention API endpoints require an active subscription to the Advanced Threat Prevention security service. These endpoints can only be accessed using the API key associated with t
  name: Palo Alto Networks Advanced Threat Prevention
  slug: palo-alto-networks-advanced-threat-prevention
- description: 'The Threat Prevention API endpoints are available to customers with an active Threat Prevention or Advanced Threat Prevention subscription. List of Threat Prevention API endpoints: 1. Link to [Request'
  name: Palo Alto Networks Threat Prevention
  slug: palo-alto-networks-threat-prevention
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
artifact_total: 1889
asyncapis:
- description: Cortex XDR Webhooks provide real-time incident and alert notifications for security events detected across endpoints, networks, and cloud workloads. Webhooks are configured in Cortex XDR Settings > No
  name: Cortex XDR Webhooks
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/palo-alto-networks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/palo-alto-networks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/palo-alto-networks-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/palo-alto-networks-scopes.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-cortex-xdr-endpoint-isolation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-cortex-xdr-incident-triage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-cortex-xdr-script-remediation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-cortex-xdr-xql-hunt-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-cortex-xsiam-incident-hunt-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-cortex-xsoar-incident-response-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-iot-security-alert-remediation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-iot-security-device-risk-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-prisma-cloud-alert-triage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/palo-alto-networks-prisma-cloud-policy-lifecycle-workflow.yml
- group: design
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
  title: ''
  type: JSONLD
  url: json-ld/palo-alto-networks-security-context.jsonld
- group: docs
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
  title: ''
  type: SpectralRules
  url: rules/palo-alto-networks-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/palo-alto-networks-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/palo-alto-networks-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/PaloAltoNetworks/pan-mcp-relay
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
- name: Palo Alto Networks Finops
  service_category: Cybersecurity
  slug: palo-alto-networks-finops
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
  property_count: 1
  slug: cloud-identity-engine-api-check_group_membership
- name: check_user_in_particular_group
  property_count: 2
  slug: cloud-identity-engine-api-check_user_in_particular_group
- name: domain_param
  property_count: 1
  slug: cloud-identity-engine-api-domain_param
- name: fetch_all_users_attrs
  property_count: 2
  slug: cloud-identity-engine-api-fetch_all_users_attrs
- name: group_filter
  property_count: 3
  slug: cloud-identity-engine-api-group_filter
- name: list_all_groups_in_domain
  property_count: 2
  slug: cloud-identity-engine-api-list_all_groups_in_domain
- name: list_all_users_in_domain
  property_count: 2
  slug: cloud-identity-engine-api-list_all_users_in_domain
- name: list_groups_user_belongs_to
  property_count: 1
  slug: cloud-identity-engine-api-list_groups_user_belongs_to
- name: list_specific_groups
  property_count: 2
  slug: cloud-identity-engine-api-list_specific_groups
- name: list_specific_users
  property_count: 1
  slug: cloud-identity-engine-api-list_specific_users
- name: list_users_in_particular_group
  property_count: 2
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
  property_count: 0
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
  property_count: 0
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
  property_count: 0
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
  property_count: 0
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
modified: '2026-05-19'
name: Palo Alto Networks
nav: Providers
network: true
overview: 'Palo Alto Networks publishes 473 APIs on the [APIs.io](https://apis.io/) network, including 5G Deregistered Trend API, 5G Network Interconnects and Bandwidth API, 5G Registered Trend API, and 470 more. Tagged areas include Cloud Security, Cybersecurity, Firewall, Network Security, and SASE.


  The Palo Alto Networks catalog on APIs.io includes 5 event-driven AsyncAPI specifications, 54 JSON-LD contexts, and 3 Spectral governance rulesets.


  Palo Alto Networks'' developer surface includes authentication, developer portal, documentation, support, engineering blog, CLI, tooling, and 70 more developer resources.'
paper_is_own: true
plans:
- name: Palo Alto Networks Plans Pricing
  plan_count: 1
  slug: palo-alto-networks-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 2
  name: Palo Alto Networks Rate Limits
  slug: palo-alto-networks-rate-limits
rules:
- name: Palo Alto Networks API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 7
  slug: palo-alto-networks-asyncapi-spectral-rules
- name: Palo Alto Networks API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: palo-alto-networks-jsonschema-spectral-rules
- name: Palo Alto Networks API Rules
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
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 81.5
    developer_ergonomics: 69.6
    discoverability: 74.1
    governance: 62.5
    operational_transparency: 68.4
  previous_composite: 68.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 94.6
      derived: 0
      marker_coverage: 100.0
      total: 314
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/screenshots/palo-alto-networks-2026-06-20T191330.png
security:
- kind: authentication
  name: Palo Alto Networks Authentication
  slug: palo-alto-networks-authentication
  summary_line: apiKey/http/oauth2 · 13 schemes
- kind: domain-security
  name: Palo Alto Networks Domain Security
  slug: palo-alto-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
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
