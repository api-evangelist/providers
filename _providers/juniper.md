---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 581
  human_in_the_loop: 16
  name: Juniper Agentic Access
  operation_count: 1200
  slug: juniper-agentic-access
  summary_line: 1200 operations · 581 acting · 16 human-in-the-loop
api_count: 6
apis:
- description: Python library for automating Junos devices using NETCONF.
  name: Junos PyEZ (Python API)
  slug: junos-pyez-python-api
- description: Python-based snapshot and test framework for Junos devices.
  name: JSNAPy API
  slug: jsnapy-api
- baseURL: https://{atp_server}/api/v1
  baseurl_source: declared
  description: Allowlist and blocklist management
  name: Juniper Networks Allowlists and Blocklists API
  slug: juniper-allowlists-and-blocklists-api
- baseURL: https://{contrail_controller}:8082
  baseurl_source: declared
  description: Analytics and operational data
  name: Juniper Networks Analytics API
  slug: juniper-analytics-api
- baseURL: https://{space_server}/api/space
  baseurl_source: declared
  description: Audit trail and logging
  name: Juniper Networks Audit Logs API
  slug: juniper-audit-logs-api
- baseURL: https://{apstra_server}/api
  baseurl_source: declared
  description: Login and token management
  name: Juniper Networks Authentication API
  slug: juniper-authentication-api
- baseURL: https://{contrail_controller}:8082
  baseurl_source: declared
  description: BGP router management
  name: Juniper Networks BGP Routers API
  slug: juniper-bgp-routers-api
- baseURL: https://{apstra_server}/api
  baseurl_source: declared
  description: Data center blueprint management
  name: Juniper Networks Blueprints API
  slug: juniper-blueprints-api
- baseURL: https://api.mist.com/api/v1
  baseurl_source: declared
  description: Client session and statistics tracking
  name: Juniper Networks Clients API
  slug: juniper-clients-api
- baseURL: https://{apstra_server}/api
  baseurl_source: declared
  description: Configuration template management
  name: Juniper Networks Configlets API
  slug: juniper-configlets-api
- baseURL: https://{device_ip}:3443
  baseurl_source: declared
  description: Device configuration operations
  name: Juniper Networks Configuration API
  slug: juniper-configuration-api
- baseURL: https://{apstra_server}/api
  baseurl_source: declared
  description: Connectivity template management
  name: Juniper Networks Connectivity Templates API
  slug: juniper-connectivity-templates-api
- baseURL: https://{apstra_server}/api
  baseurl_source: declared
  description: Design elements including rack types, templates, and logical devices
  name: Juniper Networks Design API
  slug: juniper-design-api
- baseURL: https://{space_server}/api/space
  baseurl_source: declared
  description: Device discovery and management
  name: Juniper Networks Devices API
  slug: juniper-devices-api
- baseURL: https://{atp_server}/api/v1
  baseurl_source: declared
  description: Enrolled SRX device management
  name: Juniper Networks Enrolled Devices API
  slug: juniper-enrolled-devices-api
- baseURL: https://{atp_server}/api/v1
  baseurl_source: declared
  description: Malware analysis and file submission
  name: Juniper Networks File Analysis API
  slug: juniper-file-analysis-api
- baseURL: https://{contrail_controller}:8082
  baseurl_source: declared
  description: Floating IP management
  name: Juniper Networks Floating IPs API
  slug: juniper-floating-ips-api
- baseURL: https://{atp_server}/api/v1
  baseurl_source: declared
  description: IoC management and lookup
  name: Juniper Networks Indicators of Compromise API
  slug: juniper-indicators-of-compromise-api
- baseURL: https://api.mist.com/api/v1
  baseurl_source: declared
  description: AI-driven analytics and insights
  name: Juniper Networks Insights API
  slug: juniper-insights-api
- baseURL: https://{apstra_server}/api
  baseurl_source: declared
  description: Intent-based analytics and anomaly detection
  name: Juniper Networks Intent Checks API
  slug: juniper-intent-checks-api
- baseURL: https://api.mist.com/api/v1
  baseurl_source: declared
  description: Device inventory management
  name: Juniper Networks Inventory API
  slug: juniper-inventory-api
- baseURL: https://{space_server}/api/space
  baseurl_source: declared
  description: Asynchronous job management
  name: Juniper Networks Jobs API
  slug: juniper-jobs-api
- baseURL: https://api.mist.com/api/v1
  baseurl_source: declared
  description: Floorplan and map management
  name: Juniper Networks Maps API
  slug: juniper-maps-api
- baseURL: https://{contrail_controller}:8082
  baseurl_source: declared
  description: IP Address Management
  name: Juniper Networks Network IPAM API
  slug: juniper-network-ipam-api
- baseURL: https://{contrail_controller}:8082
  baseurl_source: declared
  description: Network policy management
  name: Juniper Networks Network Policies API
  slug: juniper-network-policies-api
- baseURL: https://{device_ip}:3443
  baseurl_source: declared
  description: Operational data retrieval
  name: Juniper Networks Operational API
  slug: juniper-operational-api
- baseURL: https://api.mist.com/api/v1
  baseurl_source: declared
  description: Organization-level management
  name: Juniper Networks Organizations API
  slug: juniper-organizations-api
- baseURL: https://{contrail_controller}:8082
  baseurl_source: declared
  description: Project (tenant) management
  name: Juniper Networks Projects API
  slug: juniper-projects-api
- baseURL: https://{atp_server}/api/v1
  baseurl_source: declared
  description: Threat and activity reports
  name: Juniper Networks Reports API
  slug: juniper-reports-api
- baseURL: https://{apstra_server}/api
  baseurl_source: declared
  description: Resource pool management (ASN, IP, VNI pools)
  name: Juniper Networks Resources API
  slug: juniper-resources-api
- baseURL: https://api.mist.com/api/v1
  baseurl_source: declared
  description: Radio frequency templates
  name: Juniper Networks RF Templates API
  slug: juniper-rf-templates-api
- baseURL: https://{contrail_controller}:8082
  baseurl_source: declared
  description: Routing instance management
  name: Juniper Networks Routing Instances API
  slug: juniper-routing-instances-api
- baseURL: https://{device_ip}:3443
  baseurl_source: declared
  description: Execute Junos RPC commands
  name: Juniper Networks RPC API
  slug: juniper-rpc-api
- baseURL: https://{space_server}/api/space
  baseurl_source: declared
  description: Script bundle management and execution
  name: Juniper Networks Scripts API
  slug: juniper-scripts-api
- baseURL: https://{contrail_controller}:8082
  baseurl_source: declared
  description: Security group and firewall rule management
  name: Juniper Networks Security Groups API
  slug: juniper-security-groups-api
- baseURL: https://api.mist.com/api/v1
  baseurl_source: declared
  description: Operations for the authenticated user account
  name: Juniper Networks Self API
  slug: juniper-self-api
- baseURL: https://{contrail_controller}:8082
  baseurl_source: declared
  description: Service chaining and service instances
  name: Juniper Networks Service Instances API
  slug: juniper-service-instances-api
- baseURL: https://api.mist.com/api/v1
  baseurl_source: declared
  description: Logical grouping of sites
  name: Juniper Networks Site Groups API
  slug: juniper-site-groups-api
- baseURL: https://api.mist.com/api/v1
  baseurl_source: declared
  description: Site-level management
  name: Juniper Networks Sites API
  slug: juniper-sites-api
- baseURL: https://{space_server}/api/space
  baseurl_source: declared
  description: Software image management and deployment
  name: Juniper Networks Software Management API
  slug: juniper-software-management-api
- baseURL: https://{apstra_server}/api
  baseurl_source: declared
  description: Managed system agents and device management
  name: Juniper Networks Systems API
  slug: juniper-systems-api
- baseURL: https://{space_server}/api/space
  baseurl_source: declared
  description: The Tag Management API from Juniper Networks — 1 operation(s) for tag management.
  name: Juniper Networks Tag Management API
  slug: juniper-tag-management-api
- baseURL: https://{atp_server}/api/v1
  baseurl_source: declared
  description: Threat feed and intelligence data
  name: Juniper Networks Threat Intelligence API
  slug: juniper-threat-intelligence-api
- baseURL: https://{space_server}/api/space
  baseurl_source: declared
  description: User and role management
  name: Juniper Networks Users API
  slug: juniper-users-api
- baseURL: https://{apstra_server}/api
  baseurl_source: declared
  description: Virtual network and routing zone management
  name: Juniper Networks Virtual Networks API
  slug: juniper-virtual-networks-api
- baseURL: https://api.mist.com/api/v1
  baseurl_source: declared
  description: SD-WAN edge device management
  name: Juniper Networks WAN Edges API
  slug: juniper-wan-edges-api
- baseURL: https://api.mist.com/api/v1
  baseurl_source: declared
  description: Webhook configuration for event notifications
  name: Juniper Networks Webhooks API
  slug: juniper-webhooks-api
- baseURL: https://api.mist.com/api/v1
  baseurl_source: declared
  description: Wireless LAN configuration
  name: Juniper Networks WLANs API
  slug: juniper-wlans-api
- description: Python library for automating Junos devices using NETCONF.
  name: Junos PyEZ
  slug: junos-pyez
- description: NETCONF-based XML API for programmatic access to Junos devices.
  name: Junos XML API
  slug: junos-xml-api
- description: Python-based tool for snapshot and verification of network device configurations.
  name: Juniper JSNAPy
  slug: juniper-jsnapy
- description: 'Streaming telemetry from Junos and Junos EVO devices to a collector over gRPC (gNMI and native sensors) or UDP. The contract is a per-release set of Protocol Buffer definitions that Juniper publishes '
  name: Junos Telemetry Interface (JTI)
  slug: juniper-junos-telemetry-interface
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'Admin API calls can be used to create, manage or authenticate Mist administrators. To register administrators into an existing MSP account or Organization, please check: * [Invite Msp Admin]($e/MSPs%2'
  name: Juniper Networks Admins API
  slug: juniper-admins-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'Login Endpoints when using Login/Password authentication, with or without 2FA. If the Login/Password authentication is successful, Mist will add a `csrftoken` cookie that must be added into the later '
  name: Juniper Networks Admins Login API
  slug: juniper-admins-login-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'A Mist account can be linked to OAuth2 providers: 1. First, login with your Mist account 2. Obtain the Authorization URL for Linking with [Get Oauth 2 Authorization Url for Login]($e/Admins%20Login%20'
  name: Juniper Networks Admins Login - OAuth2 API
  slug: juniper-admins-login-oauth2-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Logout Endpoints when using Login/Password authentication, with or without 2FA.
  name: Juniper Networks Admins Logout API
  slug: juniper-admins-logout-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Admin Lookup API Call is mainly used by Web UIs to know if a user must be redirected to an SSO URL for login.
  name: Juniper Networks Admins Lookup API
  slug: juniper-admins-lookup-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Endpoints used to trigger a password recovery and validate the token sent by email.
  name: Juniper Networks Admins Recover Password API
  slug: juniper-admins-recover-password-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve constant values that can be used in different parts of the configuration
  name: Juniper Networks Constants Definitions API
  slug: juniper-constants-definitions-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve the definitions of the Mist events. These definitions are providing example of the Webhook payloads
  name: Juniper Networks Constants Events API
  slug: juniper-constants-events-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve the list of Hardware Models and their features
  name: Juniper Networks Constants Models API
  slug: juniper-constants-models-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: In a typical enterprise, a separate group of people, Installers, are responsible for install new devices. May it be a new installation (e.g. new stores), a replacement installation (e.g. replacing Cis
  name: Juniper Networks Installer API
  slug: juniper-installer-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: An MSP Admin refers to a user who has access to the Juniper Mist managed service provider (MSP) portal and is responsible for managing and administering the network operations of multiple customer org
  name: Juniper Networks MSPs Admins API
  slug: juniper-msps-admins-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: MSP (Managed Service Provider) contains multiple Organizations.
  name: Juniper Networks MSPs API
  slug: juniper-msps-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to locate a device across all the Organizations attached to the MSP account.
  name: Juniper Networks MSPs Inventory API
  slug: juniper-msps-inventory-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Licenses are a type of service or access that customers can purchase for various features or services offered by a company. Subscriptions can have different statuses, such as active, expired, exceeded
  name: Juniper Networks MSPs Licenses API
  slug: juniper-msps-licenses-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Manage the Mist portal logo at the MSP level. This logo will be displayed instead of the Juniper Mist Logo for all the Organizations attached to this MSP account.
  name: Juniper Networks MSPs Logo API
  slug: juniper-msps-logo-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Audit Logs are records of activities initiated by users, providing a history of actions such as accessing, creating, updating, or deleting resources or components at the MSP level. These logs allow su
  name: Juniper Networks MSPs Logs API
  slug: juniper-msps-logs-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Marvis is an AI-driven, interactive virtual network assistant that streamlines network operations, simplifies troubleshooting, and provides an enhanced user experience. It offers real-time network vis
  name: Juniper Networks MSPs Marvis API
  slug: juniper-msps-marvis-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Org Groups a way to group Organizations together based on certain criteria. They can be used for easier management and organization of multiple organizations within the MSP portal.
  name: Juniper Networks MSPs Org Groups API
  slug: juniper-msps-org-groups-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: An organization usually represents a customer - which has inventories, licenses. An Organization can contain multiple sites. A site usually represents a deployment at the same location (a campus, an o
  name: Juniper Networks MSPs Orgs API
  slug: juniper-msps-orgs-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: SLEs, or Service-Level Expectations, are metrics used to monitor and report on the user experience of a Wireless, Wired or Wan network. They are generated through data science and machine learning alg
  name: Juniper Networks MSPs SLEs API
  slug: juniper-msps-sles-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: MSP SSO, or Single Sign-On, is a method of authentication that allows users to securely log in to multiple applications and websites with a single set of login credentials. It involves integrating the
  name: Juniper Networks MSPs SSO API
  slug: juniper-msps-sso-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: MSP SSO roles refer to the different functions assigned to users within a Single Sign-On (SSO) system. These roles determine the tasks and actions that users can perform within the SSO system. There a
  name: Juniper Networks MSPs SSO Roles API
  slug: juniper-msps-sso-roles-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Support tickets are a means for users to seek assistance and resolve issues they encounter with a product or service. They allow users to communicate their problems or questions to the Juniper Mist su
  name: Juniper Networks MSPs Tickets API
  slug: juniper-msps-tickets-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'An org admin, or organization administrator, is a user with administrative privileges within a specific organization. They have the authority to manage and oversee the operations and settings of that '
  name: Juniper Networks Orgs Admins API
  slug: juniper-orgs-admins-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The "Advanced Anti-Malware" feature in Sky ATP is a comprehensive security solution that leverages multiple techniques to detect and prevent malware attacks. Here are the key components of this featur
  name: Juniper Networks Orgs Advanced Anti Malware Profiles API
  slug: juniper-orgs-advanced-anti-malware-profiles-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: An Alarm Template is a set of Alarm Rules that could be applied to one or more sites (while each site can only pick one Alarm Template), or to the whole org. Once created, the Alarm template must be a
  name: Juniper Networks Orgs Alarm Templates API
  slug: juniper-orgs-alarm-templates-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Alarms are triggered based on certain events. Alarms could be configured using an Alarm Template.
  name: Juniper Networks Orgs Alarms API
  slug: juniper-orgs-alarms-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'Antivirus profiles are used to define the content to scan for any malware and the action to be taken when malware is detected. These profiles can be assigned to Content Security policies to scan Web, '
  name: Juniper Networks Orgs Antivirus Profiles API
  slug: juniper-orgs-antivirus-profiles-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: AP Templates are defining Wi-Fi and AP settings that can be assigned to Access Points based on different types of rules. AP Templates must be assigned to one or multiple sites to be used.
  name: Juniper Networks Orgs AP Templates API
  slug: juniper-orgs-ap-templates-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: An organization usually represents a customer - which has inventories, licenses. An Organization can contain multiple sites. A site usually represents a deployment at the same location (a campus, an o
  name: Juniper Networks Orgs API
  slug: juniper-orgs-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Org API token is a unique identifier used by an application to authenticate and access a service's API. These tokens are used to authenticate requests made to the API server and ensure secure access t
  name: Juniper Networks Orgs API Tokens API
  slug: juniper-orgs-api-tokens-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: An Asset Filter is a feature that allows users to define specific criteria or conditions to filter and display only certain assets based on their attributes or properties. This requires the Asset Visi
  name: Juniper Networks Orgs Asset Filters API
  slug: juniper-orgs-asset-filters-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: An Asset refers to any equipment or item that is being tracked and monitored using Bluetooth Low Energy (BLE) beacon tags. This requires the Asset Visibility subscription.
  name: Juniper Networks Orgs Assets API
  slug: juniper-orgs-assets-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to manage Organization Certificates. The certificates can be used bu Access Assurance, during the SSO/SAML Authentication, ...
  name: Juniper Networks Orgs Cert API
  slug: juniper-orgs-cert-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Marvis Invites can be generated for (and belongs to) an Org. They can be generated by an Admin of an Org and can be revoked at anytime. Marvis Clients are devices that have the Marvis Android Client i
  name: Juniper Networks Orgs Clients - Marvis API
  slug: juniper-orgs-clients-marvis-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: NAC Clients are devices connected to the network and authenticated by Juniper Mist Access Assurance.
  name: Juniper Networks Orgs Clients - NAC API
  slug: juniper-orgs-clients-nac-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: SDK Clients are devices that have installed an application using the Mist Software Development Kit (SDK). These clients can provide specific data and information that is not available without the inst
  name: Juniper Networks Orgs Clients - SDK API
  slug: juniper-orgs-clients-sdk-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: WAN Clients are devices connected to a Juniper SRX or SSX gateway monitor or managed by Mist
  name: Juniper Networks Orgs Clients - Wan API
  slug: juniper-orgs-clients-wan-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Wired Clients are Wired devices connected to a Juniper switch monitored or managed by Mist.
  name: Juniper Networks Orgs Clients - Wired API
  slug: juniper-orgs-clients-wired-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Wireless Clients are Wi-Fi devices connected to a Juniper Mist Access Point.
  name: Juniper Networks Orgs Clients - Wireless API
  slug: juniper-orgs-clients-wireless-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: CRLs, or Certificate Revocation Lists, are time-stamped lists that identify digital certificates that have been invalidated before their expiration date. They include information about the reasons for
  name: Juniper Networks Orgs CRL API
  slug: juniper-orgs-crl-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'While Templates / RF Templates / Network Templates / Gateway Templates provides powerful ways to control how a Device\''s configuration is derived for a Site. There are cases where you\''d like another '
  name: Juniper Networks Orgs Device Profiles API
  slug: juniper-orgs-device-profiles-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls specific to AOS-CX (Aruba Operating System - CX) devices
  name: Juniper Networks Orgs Devices - AOSCX API
  slug: juniper-orgs-devices-aoscx-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Devices are any Network device managed or monitored by Juniper Mist. It can be * Wireless Access Points * Juniper Switch (EX, QFX) * Juniper WAN Gateway (SRX, SSR) * Mist Edges * Other or 3rd party de
  name: Juniper Networks Orgs Devices API
  slug: juniper-orgs-devices-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls specific to EdgeConnect devices
  name: Juniper Networks Orgs Devices - EdgeConnect API
  slug: juniper-orgs-devices-edgeconnect-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Call for 3rd party devices
  name: Juniper Networks Orgs Devices - Others API
  slug: juniper-orgs-devices-others-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls specific to SSR devices
  name: Juniper Networks Orgs Devices - SSR API
  slug: juniper-orgs-devices-ssr-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Orgs Events are all the system level changes at the org level
  name: Juniper Networks Orgs Events API
  slug: juniper-orgs-events-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: EVPN allows an alternative but more efficient LAN architecture utilizing VxLAN / MP-BGP - separating control plane (MAC / IP Learning) from forwarding plane. In our implementation, following the steps
  name: Juniper Networks Orgs EVPN Topologies API
  slug: juniper-orgs-evpn-topologies-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Gateway Template is applied to a site for gateway(s) in a site. When Templates are not used, Site Setting holds settings for multiple device types and they can differ to set device_type specific confi
  name: Juniper Networks Orgs Gateway Templates API
  slug: juniper-orgs-gateway-templates-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Guests are users who are accessing the wi-fi network as a temporary or non-permanent visitor.
  name: Juniper Networks Orgs Guests API
  slug: juniper-orgs-guests-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: An IDP profile is a set of predefined rules and actions that determine how the Intrusion Detection and Prevention (IDP) system handles network traffic. It allows you to selectively enforce attack dete
  name: Juniper Networks Orgs IDP Profiles API
  slug: juniper-orgs-idp-profiles-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The integration between Mist and Cradlepoint allows users to utilize Cradlepoint 5G cellular adapters with Juniper's wired, wireless, and SD-WAN solutions driven by Mist AI. With this integration, use
  name: Juniper Networks Orgs Integration Cradlepoint API
  slug: juniper-orgs-integration-cradlepoint-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'JSE stands for Juniper Secure Edge and it is a feature within the Mist UI that allows customers to configure Secure Cloud Connectors. With JSE, users can establish a tunnel via IPSec protocol and use '
  name: Juniper Networks Orgs Integration JSE API
  slug: juniper-orgs-integration-jse-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The Juniper Integration can be used to synchronize Juniper Support Insights (JSI) information.
  name: Juniper Networks Orgs Integration Juniper API
  slug: juniper-orgs-integration-juniper-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Sky Advanced Threat Prevention (Sky ATP) is a cloud-based security designed to detect and mitigate advanced threats in real-time, ensuring the security and integrity of your network. The integration o
  name: Juniper Networks Orgs Integration SkyATP API
  slug: juniper-orgs-integration-skyatp-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'In Zscaler UI: 1. add Partner Integration at https://admin.zscalerbeta.net/#administration/partner-integration 2. Add Partner Administrator Role at https://admin.zscalerbeta.net/#administration/role-m'
  name: Juniper Networks Orgs Integration Zscaler API
  slug: juniper-orgs-integration-zscaler-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The Org Inventory allows administrators to view and manage all devices registered (claimed) to the Organization.
  name: Juniper Networks Orgs Inventory API
  slug: juniper-orgs-inventory-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Juniper Support Insight is a free service provided to all Mist customers. You can adopt your devices via a few lines CLI commands. Allowing you to * get some basic information about the adopted device
  name: Juniper Networks Orgs JSI API
  slug: juniper-orgs-jsi-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Licenses are a type of service or access that customers can purchase for various features or services offered by a company. Subscriptions can have different statuses, such as active, expired, exceeded
  name: Juniper Networks Orgs Licenses API
  slug: juniper-orgs-licenses-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Linked Application are Third party applications linked to the Mist Organization. This is usually using OAuth2.0 or API integrations for a Cloud-to-Cloud Communication.
  name: Juniper Networks Orgs Linked Applications API
  slug: juniper-orgs-linked-applications-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Audit Logs are records of activities initiated by users, providing a history of actions such as accessing, creating, updating, or deleting resources or components at the Org level. These logs allow su
  name: Juniper Networks Orgs Logs API
  slug: juniper-orgs-logs-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: These API Calls to import Site Maps at the Org level
  name: Juniper Networks Orgs Maps API
  slug: juniper-orgs-maps-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Marvis is an AI-driven, interactive virtual network assistant that streamlines network operations, simplifies troubleshooting, and provides an enhanced user experience. It offers real-time network vis
  name: Juniper Networks Orgs Marvis API
  slug: juniper-orgs-marvis-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Marvis Clients are devices that have the Marvis Android Client installed on them and are connected to a Juniper Mist AP. They provide detailed data and telemetry about the client's wireless connection
  name: Juniper Networks Orgs Marvis Invites API
  slug: juniper-orgs-marvis-invites-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'A Mist Edge Cluster (MxCluster) is a group of Juniper Mist Edge devices that are configured to work together in order to provide high availability and load balancing for the tunneling of traffic from '
  name: Juniper Networks Orgs MxClusters API
  slug: juniper-orgs-mxclusters-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: A Mist Edge (MxEdge) is a physical or virtual appliance that is deployed in a network to provide centralized data path for user traffic or as a RADIUS Proxy, which was traditionally performed by legac
  name: Juniper Networks Orgs MxEdges API
  slug: juniper-orgs-mxedges-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: A Mist Tunnel (MxTunnel) is a configuration object that allows for the tunneling of user VLANs from the Access Points (APs) to a central point on the network. It specifies the VLAN IDs that need to be
  name: Juniper Networks Orgs MxTunnels API
  slug: juniper-orgs-mxtunnels-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: By default, Mist is automatically retrieving the PKI CRL by using the CRL Distribution Point provided by Certification Authority. In case this information is not provided, or the CRL is not publicly a
  name: Juniper Networks Orgs NAC CRL API
  slug: juniper-orgs-nac-crl-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The NAC IDP allows users to integrate with various Identity Providers (IDPs) to enhance authentication and access control. Admins can configure identity providers such as microsoft EntraID, okta workf
  name: Juniper Networks Orgs NAC IDP API
  slug: juniper-orgs-nac-idp-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: NAC Portals are for onboard Wireless and Wired client with 802.1X The NAC Portal is a web-based interface that allows users to authenticate and gain access to the network. It is typically used for gue
  name: Juniper Networks Orgs NAC Portals API
  slug: juniper-orgs-nac-portals-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The NAC Rules (or Auth Policies) are a set of rules that devices and users must fulfill in order to gain access to the network and use network resources. Juniper Mist Access Assurance evaluates authen
  name: Juniper Networks Orgs NAC Rules API
  slug: juniper-orgs-nac-rules-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: NAC Tags are the building blocks to compose nacrules. They can either appear in the "matching" / "not_matching" sections of a nacrule, in which case they play the role of classifiers, or they could ap
  name: Juniper Networks Orgs NAC Tags API
  slug: juniper-orgs-nac-tags-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: A Network Template is a configuration template that allows for the consistent and standardized configuration of switches across an organization's network infrastructure. It includes settings such as R
  name: Juniper Networks Orgs Network Templates API
  slug: juniper-orgs-network-templates-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: A Network refers to a group or segment of users that are defined for use across the entire organization.
  name: Juniper Networks Orgs Networks API
  slug: juniper-orgs-networks-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Premium Analytics is an advanced, cloud-based analytics service offered by Juniper Mist. It provides end-to-end network observability and allows users to gain unique insights into networking and locat
  name: Juniper Networks Orgs Premium Analytics API
  slug: juniper-orgs-premium-analytics-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: PSK Self-Service Portals are for 1. **Wi-Fi users** who want to connect to a WLAN with personal PSK, they're told to connect to a URL where they can login (likely through company\u2019s SSO) and get t
  name: Juniper Networks Orgs Psk Portals API
  slug: juniper-orgs-psk-portals-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: A multi PSK (Pre-Shared Key) is a feature that allows the use of multiple PSKs for securing network connections. It provides a simple and comprehensive way to onboard client devices without relying on
  name: Juniper Networks Orgs Psks API
  slug: juniper-orgs-psks-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to manage organization-level reports, such as E911 AP BSSID report exports.
  name: Juniper Networks Orgs Reports API
  slug: juniper-orgs-reports-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Rf Templates are a feature in Juniper Mist wireless assurance that allow for uniform radio configurations to be applied across all sites in an organization. These templates can be customized to includ
  name: Juniper Networks Orgs RF Templates API
  slug: juniper-orgs-rf-templates-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The Orgs SCEP API from Juniper Networks — 3 operation(s) for orgs scep.
  name: Juniper Networks Orgs SCEP API
  slug: juniper-orgs-scep-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: SDK Invites can be generated for (and belongs to) an Org. They can be generated by an Admin of an Org and can be revoked at anytime.
  name: Juniper Networks Orgs SDK Invites API
  slug: juniper-orgs-sdk-invites-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The Orgs SDK Templates API from Juniper Networks — 2 operation(s) for orgs sdk templates.
  name: Juniper Networks Orgs SDK Templates API
  slug: juniper-orgs-sdk-templates-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Sky ATP Secintel Profile
  name: Juniper Networks Orgs SecIntel Profiles API
  slug: juniper-orgs-secintel-profiles-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'Security Policy is designed to audit / catch discrepancies between "what''s intended to be running" versus "what''s actually running" in a network. Many big organizations have separated Security and IT '
  name: Juniper Networks Orgs Security Policies API
  slug: juniper-orgs-security-policies-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Services Policies are a security policy that defines who can access applications, they are used to control access to applications and ensure proper traffic management within a network. It determines t
  name: Juniper Networks Orgs Service Policies API
  slug: juniper-orgs-service-policies-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'A Service refers to the applications that network users will connect to. These applications represent traffic destinations and are essential for defining network policies and security configurations. '
  name: Juniper Networks Orgs Services API
  slug: juniper-orgs-services-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to manage the Mist Organization Settings
  name: Juniper Networks Orgs Setting API
  slug: juniper-orgs-setting-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Site templates are pre-configured sets of attributes and settings that can be applied to one or more sites in a Mist Organization. These templates allow for quick and consistent configuration of sites
  name: Juniper Networks Orgs Site Templates API
  slug: juniper-orgs-site-templates-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Site groups are a group of sites under the same Org. It's many-to-many mapping to sites
  name: Juniper Networks Orgs Sitegroups API
  slug: juniper-orgs-sitegroups-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to Create or Get the Organization Sites. Use the [Site Settings](https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/setting/overview) to configure or update the Sit
  name: Juniper Networks Orgs Sites API
  slug: juniper-orgs-sites-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Org SLEs, or Service-Level Expectations, are metrics used to monitor and report on the user experience of a Wireless, Wired or Wan network. They are generated through data science and machine learning
  name: Juniper Networks Orgs SLEs API
  slug: juniper-orgs-sles-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Org SSO, or Single Sign-On, is a method of authentication that allows users to securely log in to multiple applications and websites with a single set of login credentials. It involves integrating the
  name: Juniper Networks Orgs SSO API
  slug: juniper-orgs-sso-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: SSO roles refer to the different functions assigned to users within a Single Sign-On (SSO) system. These roles determine the tasks and actions that users can perform within the SSO system. There are t
  name: Juniper Networks Orgs SSO Roles API
  slug: juniper-orgs-sso-roles-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about the Mist Org and related items
  name: Juniper Networks Orgs Stats API
  slug: juniper-orgs-stats-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about the Assets at the Org level
  name: Juniper Networks Orgs Stats - Assets API
  slug: juniper-orgs-stats-assets-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about the BGP Peers (WAN Assurance)
  name: Juniper Networks Orgs Stats - BGP Peers API
  slug: juniper-orgs-stats-bgp-peers-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about the Mist Managed and Monitored Devices at the Org level By default, the API call only returns a subset of the available fields. Additional fields can be requeste
  name: Juniper Networks Orgs Stats - Devices API
  slug: juniper-orgs-stats-devices-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about Marvis Clients at the Org level
  name: Juniper Networks Orgs Stats - Marvis Clients API
  slug: juniper-orgs-stats-marvis-clients-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about the Mist Edges at the Org level
  name: Juniper Networks Orgs Stats - MxEdges API
  slug: juniper-orgs-stats-mxedges-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about OSPF peers at the Org level
  name: Juniper Networks Orgs Stats - Ospf API
  slug: juniper-orgs-stats-ospf-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about the Other/3rd party devices at the Org level
  name: Juniper Networks Orgs Stats - Other Devices API
  slug: juniper-orgs-stats-other-devices-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about the Wired Ports at the Org level
  name: Juniper Networks Orgs Stats - Ports API
  slug: juniper-orgs-stats-ports-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about the Organization Sites
  name: Juniper Networks Orgs Stats - Sites API
  slug: juniper-orgs-stats-sites-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about the Mist Tunnels at the Org level
  name: Juniper Networks Orgs Stats - Tunnels API
  slug: juniper-orgs-stats-tunnels-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about the VPN Peers (WAN Assurance)
  name: Juniper Networks Orgs Stats - VPN Peers API
  slug: juniper-orgs-stats-vpn-peers-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Support tickets are a means for users to seek assistance and resolve issues they encounter with a product or service. They allow users to communicate their problems or questions to the Juniper Mist su
  name: Juniper Networks Orgs Tickets API
  slug: juniper-orgs-tickets-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The Org UI Settings are used to configure the MArvis dashboards
  name: Juniper Networks Orgs UI Settings API
  slug: juniper-orgs-ui-settings-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: NAC User MACs (Endpoints) provide a database of endpoints identified by their MAC addresses. They can be used assign each endpoint with various attributes, such as name, VLAN, role and client label. O
  name: Juniper Networks Orgs User MACs API
  slug: juniper-orgs-user-macs-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Vars endpoints are used to retrieve the list of Site Variables across all the Sites.
  name: Juniper Networks Orgs Vars API
  slug: juniper-orgs-vars-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: VPNs endpoints are used to create the WAN Assurance Overlay configuration between a Hub and one or multiple WAN Edge Gateways. When configuring the Hub and Spokes from the Mist UI, the UI is automatic
  name: Juniper Networks Orgs VPNs API
  slug: juniper-orgs-vpns-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: An Org Webhook is a configuration that allows real-time events and data from the Org to be pushed to a provided url. It enables the collection of information about various topics such as device events
  name: Juniper Networks Orgs Webhooks API
  slug: juniper-orgs-webhooks-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'A WLAN template is a collection of WLAN policies, Tunneling Policies, and WxLAN policies. It is used for creating and managing WLAN configurations at an organizational level. WLAN templates allow for '
  name: Juniper Networks Orgs WLAN Templates API
  slug: juniper-orgs-wlan-templates-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: An Org Wlan is a wireless local area network that is configured at the Org level and applied to a WLAN template. It allows for the creation and management of wireless network settings, such as SSIDs (
  name: Juniper Networks Orgs Wlans API
  slug: juniper-orgs-wlans-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: ORg WxRules are a set of rules, restrictions, and settings that can be applied to WLANs within a specific WLAN Template. These policies determine how the devices and traffic are treated by the network
  name: Juniper Networks Orgs WxRules API
  slug: juniper-orgs-wxrules-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Wxtags are tags or groups that can be created and used within the Org. They are used to classify users and resources and can be applied to Access Points, WLAN configurations or WxRules within that sit
  name: Juniper Networks Orgs WxTags API
  slug: juniper-orgs-wxtags-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: A WxLan Tunnel (WxTunnel) are used to create a secure connection between Juniper Mist Access Points and third-party VPN concentrators using protocols such as L2TPv3 or dmvpn. These tunnels allow for t
  name: Juniper Networks Orgs WxTunnels API
  slug: juniper-orgs-wxtunnels-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API calls related to the currently connected user account.
  name: Juniper Networks Self Account API
  slug: juniper-self-account-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API calls related to the alarm subscriptions for the currently connected user account.
  name: Juniper Networks Self Alarms API
  slug: juniper-self-alarms-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Like many other API providers, it's also possible to generate API Tokens to be used (in HTTP Header) for authentication. An API token ties to a Admin with equal or less privileges. **Notes:** * an API
  name: Juniper Networks Self API Token API
  slug: juniper-self-api-token-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API calls related to the audit logs subscriptions for the currently connected user account.
  name: Juniper Networks Self Audit Logs API
  slug: juniper-self-audit-logs-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API calls related to Two Factor Authentication for the currently connected user account.
  name: Juniper Networks Self MFA API
  slug: juniper-self-mfa-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'A Mist account can be linked to OAuth2 providers: 1. First, login with your Mist account 2. Obtain the Authorization URL for Linking 3. Obtain the authorization code by clicking / going through Author'
  name: Juniper Networks Self OAuth2 API
  slug: juniper-self-oauth2-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The API Endpoints for the Advanced Anti Malware Profiles at the site level can be used to get the site derived profiles, meaning the org level configuration with the site variables resolved..
  name: Juniper Networks Sites Advanced Anti Malware Profiles API
  slug: juniper-sites-advanced-anti-malware-profiles-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Alarms are triggered based on certain events. Alarms could be configured using an [Orgs Alarm Template]($h/Orgs%20Alarm%20Templates/_overview).
  name: Juniper Networks Sites Alarms API
  slug: juniper-sites-alarms-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The Sites Anomaly API from Juniper Networks — 3 operation(s) for sites anomaly.
  name: Juniper Networks Sites Anomaly API
  slug: juniper-sites-anomaly-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The API Endpoints for the Antivirus Profiles at the site level can be used to get the site derived profiles, meaning the org level configuration with the site variables resolved..
  name: Juniper Networks Sites Antivirus Profiles API
  slug: juniper-sites-antivirus-profiles-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: AP Templates are defining Wi-Fi and AP settings that can be assigned to Access Points based on different types of rules. Site AP Templates are created and managed at the site level and can only be ref
  name: Juniper Networks Sites AP Templates API
  slug: juniper-sites-ap-templates-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Applications contains a list of applications users are interested in monitoring / routing / policing
  name: Juniper Networks Sites Applications API
  slug: juniper-sites-applications-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: An Asset Filter is a feature that allows users to define specific criteria or conditions to filter and display only certain assets based on their attributes or properties. Site Asset Filters are creat
  name: Juniper Networks Sites Asset Filters API
  slug: juniper-sites-asset-filters-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: An Asset refers to any equipment or item that is being tracked and monitored using Bluetooth Low Energy (BLE) beacon tags. This requires the Asset Visibility subscription.
  name: Juniper Networks Sites Assets API
  slug: juniper-sites-assets-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Auto Map Assignment allows devices to be automatically assigned to maps based on their location data. These API calls can be used to manage, apply, and clear auto map assignments for devices at the si
  name: Juniper Networks Sites Auto Map Assignment API
  slug: juniper-sites-auto-map-assignment-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The Sites Beacons API from Juniper Networks — 2 operation(s) for sites beacons.
  name: Juniper Networks Sites Beacons API
  slug: juniper-sites-beacons-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: NAC Clients are devices connected to the network and authenticated by Juniper Mist Access Assurance.
  name: Juniper Networks Sites Clients - NAC API
  slug: juniper-sites-clients-nac-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: WAN Clients are devices connected to a Juniper SRX or SSX gateway monitor or managed by Mist
  name: Juniper Networks Sites Clients - Wan API
  slug: juniper-sites-clients-wan-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Wired Clients are Wired devices connected to a Juniper switch monitored or managed by Mist.
  name: Juniper Networks Sites Clients - Wired API
  slug: juniper-sites-clients-wired-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Wireless Clients are Wi-Fi devices connected to a Juniper Mist Access Point.
  name: Juniper Networks Sites Clients - Wireless API
  slug: juniper-sites-clients-wireless-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The API Endpoints for the Device Profiles at the site level can be used to get the site derived networks, meaning the org level configuration with the site variables resolved..
  name: Juniper Networks Sites Device Profiles API
  slug: juniper-sites-device-profiles-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Mist provides many ways (device_type specific template, site template, device profile, per-device) to configure devices for different kind of scenarios. The precedence goes from most specific to least
  name: Juniper Networks Sites Devices API
  slug: juniper-sites-devices-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Call for 3rd party devices
  name: Juniper Networks Sites Devices - Others API
  slug: juniper-sites-devices-others-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls specific to manage (form/delete) the SRX/SSR Clusters
  name: Juniper Networks Sites Devices - WAN Cluster API
  slug: juniper-sites-devices-wan-cluster-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls specific to the Juniper Switches managed by Mist
  name: Juniper Networks Sites Devices - Wired API
  slug: juniper-sites-devices-wired-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls specific to the Juniper Switches Virtual Chassis managed by Mist
  name: Juniper Networks Sites Devices - Wired - Virtual Chassis API
  slug: juniper-sites-devices-wired-virtual-chassis-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls specific to the Mist Access Points
  name: Juniper Networks Sites Devices - Wireless API
  slug: juniper-sites-devices-wireless-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'Site events are issues or incidents that affect site-assigned access points (aps) and radius, dhcp, and dns servers. They can be investigated and monitored using the insights dashboard in the juniper '
  name: Juniper Networks Sites Events API
  slug: juniper-sites-events-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: EVPN allows an alternative but more efficient LAN architecture utilizing VxLAN / MP-BGP - separating control plane (MAC / IP Learning) from forwarding plane. In our implementation, following the steps
  name: Juniper Networks Sites EVPN Topologies API
  slug: juniper-sites-evpn-topologies-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The API Endpoints for the Gateway Templates at the site level can be used to get the site derived networks, meaning the org level configuration with the site variables resolved..
  name: Juniper Networks Sites Gateway Templates API
  slug: juniper-sites-gateway-templates-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Guests are users who are accessing the wi-fi network as a temporary or non-permanent visitor.
  name: Juniper Networks Sites Guests API
  slug: juniper-sites-guests-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The API Endpoints for the IDP Profiles at the site level can be used to get the site derived profiles, meaning the org level configuration with the site variables resolved..
  name: Juniper Networks Sites IDP Profiles API
  slug: juniper-sites-idp-profiles-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Insights is a feature that provides an overview of network experience across the entire site, access points, or clients. It offers useful information about current conditions, such as telemetry data f
  name: Juniper Networks Sites Insights API
  slug: juniper-sites-insights-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'JSE stands for Juniper Secure Edge and it is a feature within the Mist UI that allows customers to configure Secure Cloud Connectors. With JSE, users can establish a tunnel via IPSec protocol and use '
  name: Juniper Networks Sites JSE API
  slug: juniper-sites-jse-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The API Endpoints for the Licenses at the site level can be used to get license usages for a specific site.
  name: Juniper Networks Sites Licenses API
  slug: juniper-sites-licenses-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The Location Diagnostics allows users to retrieve and analyze coverage and performance data for mist access points (aps) and devices.
  name: Juniper Networks Sites Location API
  slug: juniper-sites-location-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Map Stacks are a way to group multiple maps together within a site, typically representing different floors or levels in a building. Map Stacks help organize and manage floorplans for multi-story buil
  name: Juniper Networks Sites Map Stacks API
  slug: juniper-sites-map-stacks-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: A Site Map is a visual representation of the layout and structure of a location, such as a building or campus. It includes accurate information about the placement, positions, heights, and orientation
  name: Juniper Networks Sites Maps API
  slug: juniper-sites-maps-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: '### AP Auto-Placement AP Auto-Placement is a feature in Juniper Mist wireless assurance that automatically determines and sets the positions of Access Points (APs) on a floorplan. It saves time and si'
  name: Juniper Networks Sites Maps - Auto-placement API
  slug: juniper-sites-maps-auto-placement-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The auto zones service is a map parsing service that uses map image data to suggest spaces to designate as location zones.
  name: Juniper Networks Sites Maps - Auto-Zone API
  slug: juniper-sites-maps-auto-zone-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Marvis Config Actions are config changes injected by Marvis into network devices. These actions can be searched, counted, deleted, and given feedback.
  name: Juniper Networks Sites Marvis Configs API
  slug: juniper-sites-marvis-configs-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: MxEdges (Mist Edges) at the site level are deployed to tunnel traffic at each site due to network constraints or security concerns. They can be assigned to a specific site and configured to provide tu
  name: Juniper Networks Sites MxEdges API
  slug: juniper-sites-mxedges-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The NAC IDP allows users to integrate with various Identity Providers (IDPs) to enhance authentication and access control. Admins can configure identity providers such as microsoft EntraID, okta workf
  name: Juniper Networks Sites NAC Fingerprints API
  slug: juniper-sites-nac-fingerprints-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The API Endpoints for the Network Templates at the site level can be used to get the site derived networks, meaning the org level configuration with the site variables resolved.
  name: Juniper Networks Sites Network Templates API
  slug: juniper-sites-network-templates-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The API Endpoints for the Networks at the site level can be used to get the site derived networks, meaning the org level configuration with the site variables resolved.
  name: Juniper Networks Sites Networks API
  slug: juniper-sites-networks-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: A multi PSK (Pre-Shared Key) is a feature that allows the use of multiple PSKs for securing network connections. It provides a simple and comprehensive way to onboard client devices without relying on
  name: Juniper Networks Sites Psks API
  slug: juniper-sites-psks-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The API Endpoints for the RF Templates at the site level can be used to get the site derived configuration, meaning the org level configuration with the site variables resolved..
  name: Juniper Networks Sites RF Templates API
  slug: juniper-sites-rf-templates-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Rf Diags is a feature in Juniper Mist location services that allows users to replay recorded sessions of the RF (radio frequency) environment. It enables users to gain an understanding of current issu
  name: Juniper Networks Sites Rfdiags API
  slug: juniper-sites-rfdiags-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'Rogues are unauthorized wireless access points that are installed on a network without authorization. They can be connected to the LAN via an ethernet cable, similar to a pc, and are typically set up '
  name: Juniper Networks Sites Rogues API
  slug: juniper-sites-rogues-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: RRM, or Radio Resource Management, is a tool used by large multi-site organizations to efficiently manage their RF spectrum. It involves making decisions on channel and power settings for access point
  name: Juniper Networks Sites RRM API
  slug: juniper-sites-rrm-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: RSSI Zones are zones based on the RSSI (Received Signal Strength Indicator, i.e. the power of the signal received by the Access Points from the Wireless Clients).
  name: Juniper Networks Sites RSSI Zones API
  slug: juniper-sites-rssi-zones-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Sky ATP Secintel Profile
  name: Juniper Networks Sites SecIntel Profiles API
  slug: juniper-sites-secintel-profiles-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The API Endpoints for the Service Policies at the site level can be used to get the site derived configuration, meaning the merge between the site level configuration and the org level configuration.
  name: Juniper Networks Sites Service Policies API
  slug: juniper-sites-service-policies-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: A Service represents an a traffic destination or an application that network users connect to. They are associated with users and networks and are used in application policies to permit or deny access
  name: Juniper Networks Sites Services API
  slug: juniper-sites-services-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Site settings refer to the configuration and management of of site within a Mist Organization. These settings include access point settings, firmware upgrade schedules, and various features such as lo
  name: Juniper Networks Sites Setting API
  slug: juniper-sites-setting-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The API Endpoints for the Site Templates at the site level can be used to get the site derived configuration, meaning the org level configuration with the site variables resolved..
  name: Juniper Networks Sites Site Templates API
  slug: juniper-sites-site-templates-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: SkyATP is a cloud-based solution that provides advanced threat protection for network security. It allows security analysts to update their defense against new attack techniques in real-time and distr
  name: Juniper Networks Sites Skyatp API
  slug: juniper-sites-skyatp-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Site SLEs, or Service-Level Expectations, are metrics used to monitor and report on the user experience of a Wireless, Wired or Wan network. They are generated through data science and machine learnin
  name: Juniper Networks Sites SLEs API
  slug: juniper-sites-sles-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The Spectrum Analysis feature provides insights into the radio frequency environment, helping to identify interference and optimize wireless network performance. It allows users to monitor and analyze
  name: Juniper Networks Sites Spectrum Analysis API
  slug: juniper-sites-spectrum-analysis-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The stats are providing access to raw data about a specific type of entities.
  name: Juniper Networks Sites Stats API
  slug: juniper-sites-stats-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve the stats of the Applications used on side
  name: Juniper Networks Sites Stats - Apps API
  slug: juniper-sites-stats-apps-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The Sites Stats - Assets API from Juniper Networks — 7 operation(s) for sites stats - assets.
  name: Juniper Networks Sites Stats - Assets API
  slug: juniper-sites-stats-assets-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The Sites Stats - Beacons API from Juniper Networks — 1 operation(s) for sites stats - beacons.
  name: Juniper Networks Sites Stats - Beacons API
  slug: juniper-sites-stats-beacons-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve BGP Peers statistics of the Site Wen Edge Gateways at the Site level
  name: Juniper Networks Sites Stats - BGP Peers API
  slug: juniper-sites-stats-bgp-peers-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve the stats of the calls (Zoom/Teams) detected by Mist
  name: Juniper Networks Sites Stats - Calls API
  slug: juniper-sites-stats-calls-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: SDK Clients are devices that have installed an application using the Mist Software Development Kit (SDK). These clients can provide specific data and information that is not available without the inst
  name: Juniper Networks Sites Stats - Clients SDK API
  slug: juniper-sites-stats-clients-sdk-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve the stats of the wireless clients detected (connected or not connected) on this site.
  name: Juniper Networks Sites Stats - Clients Wireless API
  slug: juniper-sites-stats-clients-wireless-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about the Mist Managed and Monitored Devices at the Site level
  name: Juniper Networks Sites Stats - Devices API
  slug: juniper-sites-stats-devices-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about the Discovered Switches at the Site level
  name: Juniper Networks Sites Stats - Discovered Switches API
  slug: juniper-sites-stats-discovered-switches-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve IoT Endpoint statistics for the current Site
  name: Juniper Networks Sites Stats - IoT Endpoints API
  slug: juniper-sites-stats-iot-endpoints-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about the Mist Edges at the Site level
  name: Juniper Networks Sites Stats - MxEdges API
  slug: juniper-sites-stats-mxedges-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about OSPF peers at the Site level
  name: Juniper Networks Sites Stats - Ospf API
  slug: juniper-sites-stats-ospf-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve statistics about the Wired Ports at the Site level
  name: Juniper Networks Sites Stats - Ports API
  slug: juniper-sites-stats-ports-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve WxRules statistics for the current Site
  name: Juniper Networks Sites Stats - WxRules API
  slug: juniper-sites-stats-wxrules-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve Zones statistics for the current Site
  name: Juniper Networks Sites Stats - Zones API
  slug: juniper-sites-stats-zones-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Synthetic Tests (Marvis Minis) are a feature of Juniper Networks' Mist platform, designed to proactively identify and resolve network issues before they impact users by simulating user connections and
  name: Juniper Networks Sites Synthetic Tests API
  slug: juniper-sites-synthetic-tests-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: The Site UI Settings are used to configure the site Network and Analytics reports
  name: Juniper Networks Sites UI Settings API
  slug: juniper-sites-ui-settings-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: A vBeacon is a virtual beacon that is created and configured on a floorplan and are configured with a name and message It is a Mist patented technology that provides proximity-related notifications to
  name: Juniper Networks Sites vBeacons API
  slug: juniper-sites-vbeacons-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve the list of Org VPNs configuration available for the Site
  name: Juniper Networks Sites VPNs API
  slug: juniper-sites-vpns-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to retrieve WAN Assurance statistics about the WAN Usage
  name: Juniper Networks Sites WAN Usages API
  slug: juniper-sites-wan-usages-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: A Site Webhook is a configuration that allows real-time events and data from a specific site to be pushed to a provided url. It enables the collection of information about various topics such as devic
  name: Juniper Networks Sites Webhooks API
  slug: juniper-sites-webhooks-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: A Site Wlan is a wireless local area network that is configured and applied to a specific site within an organization. It allows for the creation and management of wireless network settings, such as S
  name: Juniper Networks Sites Wlans API
  slug: juniper-sites-wlans-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: Site WxRules are a set of rules, restrictions, and settings that can be applied to WLANs within a specific site. These policies determine how the devices and traffic are treated by the network and can
  name: Juniper Networks Sites WxRules API
  slug: juniper-sites-wxrules-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: 'Wxtags are tags or groups that can be created and used within a specific site. They are used to classify users and resources and can be applied to Access Points, WLAN configurations or WxRules within '
  name: Juniper Networks Sites WxTags API
  slug: juniper-sites-wxtags-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: A WxLan Tunnel (WxTunnel) are used to create a secure connection between Juniper Mist Access Points and third-party VPN concentrators using protocols such as L2TPv3 or dmvpn. These tunnels allow for t
  name: Juniper Networks Sites WxTunnels API
  slug: juniper-sites-wxtunnels-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: A Zone is a custom area defined by a user on a floor plan. Zones can be used for capturing entry and exit events of clients, assets, and sdk clients, providing insights such as wait time and the numbe
  name: Juniper Networks Sites Zones API
  slug: juniper-sites-zones-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to use Devices Troubleshooting tools. Some API Calls can be used with any type of devices (Access Points, Switches and Gateways), and some others may be limited to some types of devices (e.g
  name: Juniper Networks Utilities Common API
  slug: juniper-utilities-common-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to use Devices Troubleshooting tools specific to Wired Assurance
  name: Juniper Networks Utilities LAN API
  slug: juniper-utilities-lan-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to use Devices Troubleshooting tools specific to Asset Tracking and User Management
  name: Juniper Networks Utilities Location API
  slug: juniper-utilities-location-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to use Devices Troubleshooting tools specific to Mx Edges
  name: Juniper Networks Utilities MxEdge API
  slug: juniper-utilities-mxedge-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to start, stop or managed Packet Captures at the device level
  name: Juniper Networks Utilities PCAPs API
  slug: juniper-utilities-pcaps-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls used to manage device upgrades for a single device, at the site level or at the organization level.
  name: Juniper Networks Utilities Upgrade API
  slug: juniper-utilities-upgrade-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to use Devices Troubleshooting tools specific to WAN Assurance
  name: Juniper Networks Utilities WAN API
  slug: juniper-utilities-wan-api
- baseURL: netconf://[device-ip]:830
  baseurl_source: declared
  description: API Calls to use Devices Troubleshooting tools specific to Wireless Assurance
  name: Juniper Networks Utilities Wi-Fi API
  slug: juniper-utilities-wi-fi-api
artifact_total: 405
asyncapis:
- description: ''
  name: Juniper Mist Webhooks
  slug: juniper-mist-webhooks
collections:
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists API
  slug: open-juniper-allowlists-and-blocklists-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Analytics API
  slug: open-juniper-analytics-api
- collection_type: open
  name: Juniper Networks Juniper Apstra API
  slug: open-juniper-apstra
- collection_type: open
  name: Juniper Networks Juniper Advanced Threat Prevention (ATP) Cloud API
  slug: open-juniper-atp-cloud
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Audit Logs API
  slug: open-juniper-audit-logs-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Authentication API
  slug: open-juniper-authentication-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists BGP Routers API
  slug: open-juniper-bgp-routers-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Blueprints API
  slug: open-juniper-blueprints-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Clients API
  slug: open-juniper-clients-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Configlets API
  slug: open-juniper-configlets-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Configuration API
  slug: open-juniper-configuration-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Connectivity Templates API
  slug: open-juniper-connectivity-templates-api
- collection_type: open
  name: Juniper Networks Juniper Contrail Networking API
  slug: open-juniper-contrail
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Design API
  slug: open-juniper-design-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Devices API
  slug: open-juniper-devices-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Enrolled Devices API
  slug: open-juniper-enrolled-devices-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists File Analysis API
  slug: open-juniper-file-analysis-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Floating IPs API
  slug: open-juniper-floating-ips-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Indicators of Compromise API
  slug: open-juniper-indicators-of-compromise-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Insights API
  slug: open-juniper-insights-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Intent Checks API
  slug: open-juniper-intent-checks-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Inventory API
  slug: open-juniper-inventory-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Jobs API
  slug: open-juniper-jobs-api
- collection_type: open
  name: Juniper Networks Junos REST API
  slug: open-juniper-junos-rest-api
- collection_type: open
  name: Juniper Networks Junos Space Network Management Platform API
  slug: open-juniper-junos-space
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Maps API
  slug: open-juniper-maps-api
- collection_type: open
  name: Juniper Networks Juniper Mist API
  slug: open-juniper-mist
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Network IPAM API
  slug: open-juniper-network-ipam-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Network Policies API
  slug: open-juniper-network-policies-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Operational API
  slug: open-juniper-operational-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Organizations API
  slug: open-juniper-organizations-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Projects API
  slug: open-juniper-projects-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Reports API
  slug: open-juniper-reports-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Resources API
  slug: open-juniper-resources-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists RF Templates API
  slug: open-juniper-rf-templates-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Routing Instances API
  slug: open-juniper-routing-instances-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists RPC API
  slug: open-juniper-rpc-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Scripts API
  slug: open-juniper-scripts-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Security Groups API
  slug: open-juniper-security-groups-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Self API
  slug: open-juniper-self-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Service Instances API
  slug: open-juniper-service-instances-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Site Groups API
  slug: open-juniper-site-groups-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Sites API
  slug: open-juniper-sites-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Software Management API
  slug: open-juniper-software-management-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Systems API
  slug: open-juniper-systems-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Tag Management API
  slug: open-juniper-tag-management-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Threat Intelligence API
  slug: open-juniper-threat-intelligence-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Users API
  slug: open-juniper-users-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Virtual Networks API
  slug: open-juniper-virtual-networks-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists WAN Edges API
  slug: open-juniper-wan-edges-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists Webhooks API
  slug: open-juniper-webhooks-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Allowlists and Blocklists WLANs API
  slug: open-juniper-wlans-api
common:
- group: commercial
  href: https://artifacts.apis.io/juniper/finops/juniper-finops.yml
  title: ''
  type: FinOps
  url: finops/juniper-finops.yml
- group: other
  href: https://artifacts.apis.io/juniper/capabilities/juniper-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/juniper-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/juniper/agentic-access/juniper-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/juniper-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/juniper/security/juniper-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/juniper-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/juniper/authentication/juniper-authentication.yml
  title: ''
  type: Authentication
  url: authentication/juniper-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/juniper-networks
- group: company
  title: ''
  type: Website
  url: https://www.juniper.net/
- group: docs
  title: ''
  type: Documentation
  url: https://www.juniper.net/documentation/
- group: operate
  title: ''
  type: Support
  url: https://support.juniper.net/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Juniper
- group: operate
  title: ''
  type: Community
  url: https://community.juniper.net/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.juniper.net/us/en/legal-notices.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.juniper.net/us/en/privacy-policy.html
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/JuniperNetworks
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/juniper
- group: design
  href: https://artifacts.apis.io/juniper/json-ld/juniper-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/juniper-context.jsonld
- group: docs
  href: https://artifacts.apis.io/juniper/json-schema/juniper-network-device.json
  title: ''
  type: JSONSchema
  url: json-schema/juniper-network-device.json
- group: docs
  href: https://artifacts.apis.io/juniper/json-schema/juniper-virtual-network.json
  title: ''
  type: JSONSchema
  url: json-schema/juniper-virtual-network.json
- group: docs
  href: https://artifacts.apis.io/juniper/json-schema/juniper-security-threat.json
  title: ''
  type: JSONSchema
  url: json-schema/juniper-security-threat.json
- group: docs
  href: https://artifacts.apis.io/juniper/json-schema/juniper-site.json
  title: ''
  type: JSONSchema
  url: json-schema/juniper-site.json
- group: docs
  href: https://artifacts.apis.io/juniper/json-schema/juniper-blueprint.json
  title: ''
  type: JSONSchema
  url: json-schema/juniper-blueprint.json
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Juniper/junos-mcp-server
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.juniper.net/documentation/us/en/software/mist/api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.juniper.net/documentation/us/en/software/mist/api/http/guides/overview/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.juniper.net/documentation/us/en/software/mist/api/http/getting-started/how-to-get-started
- group: agent
  href: https://artifacts.apis.io/juniper/llms/juniper-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/juniper-llms.txt
- group: build
  href: https://artifacts.apis.io/juniper/packages/juniper-packages.yml
  title: ''
  type: Packages
  url: packages/juniper-packages.yml
- group: build
  href: https://artifacts.apis.io/juniper/packages/juniper-packages.yml
  title: ''
  type: SDKs
  url: packages/juniper-packages.yml
- group: build
  href: https://artifacts.apis.io/juniper/cli/juniper-cli.yml
  title: ''
  type: CLI
  url: cli/juniper-cli.yml
- group: agent
  href: https://artifacts.apis.io/juniper/mcp/juniper-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/juniper-mcp.yml
- group: build
  href: https://artifacts.apis.io/juniper/mcp/juniper-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/juniper-tool-crosswalk.yml
- group: design
  href: https://artifacts.apis.io/juniper/asyncapi/juniper-mist-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/juniper-mist-webhooks.yml
- group: other
  href: https://artifacts.apis.io/juniper/grpc/_index.yml
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: design
  href: https://artifacts.apis.io/juniper/conventions/juniper-conventions.yml
  title: ''
  type: Conventions
  url: conventions/juniper-conventions.yml
- group: design
  href: https://artifacts.apis.io/juniper/errors/juniper-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/juniper-problem-types.yml
- group: design
  href: https://artifacts.apis.io/juniper/lifecycle/juniper-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/juniper-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://mist.statuspage.io/
- group: operate
  href: https://artifacts.apis.io/juniper/changelog/juniper-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/juniper-changelog.yml
- group: design
  href: https://artifacts.apis.io/juniper/conformance/juniper-conformance.yml
  title: ''
  type: Conformance
  url: conformance/juniper-conformance.yml
- group: design
  href: https://artifacts.apis.io/juniper/data-model/juniper-data-model.yml
  title: ''
  type: DataModel
  url: data-model/juniper-data-model.yml
- group: auth
  href: https://artifacts.apis.io/juniper/security/juniper-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/juniper-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.juniper.net/us/en/report-a-security-vulnerability.html
- group: agent
  href: https://artifacts.apis.io/juniper/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/juniper/overlays/juniper-mist-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/juniper-mist-api-overlay.yaml
- group: commercial
  href: https://artifacts.apis.io/juniper/plans/juniper-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/juniper-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/juniper/rate-limits/juniper-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/juniper-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://community.juniper.net/browse/blogs
created: 2024-01-15 00:00:00+00:00
description: Juniper Networks (an HPE company since 2025) builds AI-native networking, routing, switching and security for service providers, enterprises and public-sector organizations. Its programmable surface spans the Mist cloud API (1,059 REST operations), Apstra data-center automation, Junos device automation over NETCONF/YANG, Junos Telemetry Interface gRPC streaming, and three first-party MCP servers.
finops:
- has_sources: true
  method: derived
  name: Juniper Finops
  primary_unit: ''
  service_category: ''
  slug: juniper-finops
  template: true
image: https://www.juniper.net/content/dam/www/assets/images/juniper-networks-logo.png
json_schemas:
- name: Admin
  property_count: 10
  slug: juniper-admin
- name: Alarm
  property_count: 4
  slug: juniper-alarm
- name: AnalysisResult
  property_count: 12
  slug: juniper-analysisresult
- name: Anomaly
  property_count: 8
  slug: juniper-anomaly
- name: ApiToken
  property_count: 5
  slug: juniper-apitoken
- name: AsnPool
  property_count: 6
  slug: juniper-asnpool
- name: AuditEvent
  property_count: 6
  slug: juniper-auditevent
- name: BgpPeer
  property_count: 10
  slug: juniper-bgppeer
- name: Blueprint
  property_count: 10
  slug: juniper-blueprint
- name: Juniper Apstra Blueprint
  property_count: 16
  slug: juniper-blueprint
- name: BlueprintNode
  property_count: 7
  slug: juniper-blueprintnode
- name: ChassisModule
  property_count: 7
  slug: juniper-chassismodule
- name: ClientStats
  property_count: 16
  slug: juniper-clientstats
- name: ConfigFile
  property_count: 5
  slug: juniper-configfile
- name: Configlet
  property_count: 3
  slug: juniper-configlet
- name: ConnectivityTemplate
  property_count: 4
  slug: juniper-connectivitytemplate
- name: DesignTemplate
  property_count: 7
  slug: juniper-designtemplate
- name: Device
  property_count: 11
  slug: juniper-device
- name: DeviceStats
  property_count: 11
  slug: juniper-devicestats
- name: DomainReputation
  property_count: 6
  slug: juniper-domainreputation
- name: EnrolledDevice
  property_count: 9
  slug: juniper-enrolleddevice
- name: Error
  property_count: 1
  slug: juniper-error
- name: FileVerdict
  property_count: 8
  slug: juniper-fileverdict
- name: IbaDashboard
  property_count: 6
  slug: juniper-ibadashboard
- name: IdPerms
  property_count: 6
  slug: juniper-idperms
- name: Indicator
  property_count: 9
  slug: juniper-indicator
- name: InterfaceMap
  property_count: 5
  slug: juniper-interfacemap
- name: InventoryDevice
  property_count: 10
  slug: juniper-inventorydevice
- name: IpPool
  property_count: 6
  slug: juniper-ippool
- name: IpReputation
  property_count: 7
  slug: juniper-ipreputation
- name: Job
  property_count: 7
  slug: juniper-job
- name: ListEntry
  property_count: 6
  slug: juniper-listentry
- name: LldpNeighbor
  property_count: 5
  slug: juniper-lldpneighbor
- name: LogicalDevice
  property_count: 3
  slug: juniper-logicaldevice
- name: ManagedSystem
  property_count: 7
  slug: juniper-managedsystem
- name: Map
  property_count: 10
  slug: juniper-map
- name: Juniper Network Device
  property_count: 18
  slug: juniper-network-device
- name: NetworkIpam
  property_count: 5
  slug: juniper-networkipam
- name: NetworkPolicy
  property_count: 4
  slug: juniper-networkpolicy
- name: Organization
  property_count: 7
  slug: juniper-organization
- name: OrgStats
  property_count: 5
  slug: juniper-orgstats
- name: PhysicalInterface
  property_count: 10
  slug: juniper-physicalinterface
- name: Privilege
  property_count: 5
  slug: juniper-privilege
- name: Project
  property_count: 5
  slug: juniper-project
- name: RackType
  property_count: 6
  slug: juniper-racktype
- name: ResourceRef
  property_count: 3
  slug: juniper-resourceref
- name: RfTemplate
  property_count: 6
  slug: juniper-rftemplate
- name: Role
  property_count: 3
  slug: juniper-role
- name: RouteTable
  property_count: 5
  slug: juniper-routetable
- name: Script
  property_count: 5
  slug: juniper-script
- name: Juniper Security Threat
  property_count: 14
  slug: juniper-security-threat
- name: SecurityGroup
  property_count: 4
  slug: juniper-securitygroup
- name: SecurityZone
  property_count: 7
  slug: juniper-securityzone
- name: ServiceInstance
  property_count: 5
  slug: juniper-serviceinstance
- name: Site
  property_count: 11
  slug: juniper-site
- name: Juniper Site
  property_count: 17
  slug: juniper-site
- name: SiteGroup
  property_count: 6
  slug: juniper-sitegroup
- name: SiteInsights
  property_count: 2
  slug: juniper-siteinsights
- name: SiteStats
  property_count: 5
  slug: juniper-sitestats
- name: SoftwarePackage
  property_count: 6
  slug: juniper-softwarepackage
- name: SystemAgent
  property_count: 8
  slug: juniper-systemagent
- name: Tag
  property_count: 4
  slug: juniper-tag
- name: ThreatFeed
  property_count: 7
  slug: juniper-threatfeed
- name: ThreatReport
  property_count: 4
  slug: juniper-threatreport
- name: UrlReputation
  property_count: 5
  slug: juniper-urlreputation
- name: User
  property_count: 6
  slug: juniper-user
- name: Juniper Virtual Network
  property_count: 16
  slug: juniper-virtual-network
- name: VirtualNetwork
  property_count: 10
  slug: juniper-virtualnetwork
- name: VniPool
  property_count: 6
  slug: juniper-vnipool
- name: VnUve
  property_count: 1
  slug: juniper-vnuve
- name: WanEdge
  property_count: 8
  slug: juniper-wanedge
- name: Webhook
  property_count: 11
  slug: juniper-webhook
- name: Wlan
  property_count: 13
  slug: juniper-wlan
json_structures:
- name: Juniper Structure
  property_count: 0
  slug: juniper-structure
jsonld:
- class_count: 0
  name: Juniper Context
  property_count: 8
  slug: juniper-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: 'Juniper ships THREE first-party MCP servers, and every one of them is software you run yourself. None is a hosted endpoint an agent can reach today: junos-mcp-server and yams are stdio/self-hosted-HTT'
  name: MCP server manifest (3 first-party servers, all local-stdio)
  slug: mcp-server-manifest-3-first-party-servers-all-local-stdio
modified: '2026-09-18'
name: Juniper Networks
nav: Providers
network: true
overview: 'Juniper Networks publishes 263 API contracts indexed on the [APIs.io](https://apis.io/) network, including Allowlists and Blocklists API, Analytics API, Audit Logs API, and 260 more. Tagged areas include Artificial Intelligence, Automation, Cloud, Enterprise, and Networking.


  The Juniper Networks catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Juniper Networks'' developer surface includes authentication, documentation, support, YouTube channel, Stack Overflow tag, API reference, getting-started guide, and 40 more developer resources.'
plans:
- name: Juniper Plans Pricing
  plan_count: 0
  slug: juniper-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Juniper Rate Limits
  slug: juniper-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Juniper Networks — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: juniper-jsonschema-spectral-rules
score:
  band: strong
  composite: 58.7
  coverage:
    artifact_dirs: 35
    catalog_earned: 56.3
    catalog_earned_first_party: 8.0
    catalog_gap: 58.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 14.4
    contract_quality: 66.2
    developer_ergonomics: 68.5
    discoverability: 83.3
    operational_transparency: 73.7
  previous_composite: 58.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 257
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/juniper/juniper-2026-06-20T183833.png
security:
- kind: authentication
  name: Juniper Authentication
  slug: juniper-authentication
  summary_line: apiKey/http · 6 schemes
- kind: domain-security
  name: Juniper Domain Security
  slug: juniper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Juniper Vulnerability Disclosure
  slug: juniper-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Juniper Trust Center
  slug: juniper-trust-center
  summary_line: trust center published
skill_count: 3
skills:
- name: juniper-mist-device-upgrade
  slug: juniper-mist-device-upgrade
- name: juniper-mist-site-onboard
  slug: juniper-mist-site-onboard
- name: juniper-mist-webhook-subscribe
  slug: juniper-mist-webhook-subscribe
slug: juniper
tags:
- Artificial Intelligence
- Automation
- Cloud
- Enterprise
- Networking
- SDN
- Security
- Fortune 1000
website: https://www.juniper.net/
---
