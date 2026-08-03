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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 521
  human_in_the_loop: 15
  name: Mist Ai Agentic Access
  operation_count: 1037
  slug: mist-ai-agentic-access
  summary_line: 1037 operations · 521 acting · 15 human-in-the-loop
api_count: 211
apis:
- description: Mist exposes a WebSocket channel for real-time event subscriptions including device events, location updates, presence, RSSI, stats, and Marvis events. Clients authenticate with an API token and subsc
  name: Juniper Mist WebSocket Streaming API
  slug: juniper-mist-websocket-streaming
- description: Mist Webhooks deliver outbound HTTP POST notifications for events at the Organization or Site scope. Supported topics include audits, alarms, device events, client join/disconnect/sessions, Zone enter
  name: Juniper Mist Webhooks API
  slug: juniper-mist-webhooks
- description: 'Admin API calls can be used to create, manage or authenticate Mist administrators. To register administrators into an existing MSP account or Organization, please check: * [Invite Msp Admin](/#operati'
  name: Juniper Mist AI Admins API
  slug: mist-ai-admins-api
- description: 'Login Endpoints when using Login/Password authentication, with or without 2FA. If the Login/Password authentication is successful, Mist will add a `csrftoken` cookie that must be added into the later '
  name: Juniper Mist AI Admins Login API
  slug: mist-ai-admins-login-api
- description: 'A Mist account can be linked to OAuth2 providers: 1. First, login with your Mist account 2. Obtain the Authorization URL for Linking with [Get Oauth 2 Authorization Url for Login](/#operations/getOaut'
  name: Juniper Mist AI Admins Login - OAuth2 API
  slug: mist-ai-admins-login-oauth2-api
- description: Logout Endpoints when using Login/Password authentication, with or without 2FA.
  name: Juniper Mist AI Admins Logout API
  slug: mist-ai-admins-logout-api
- description: Admin Lookup API Call is mainly used by Web UIs to know if a user must be redirected to an SSO URL for login.
  name: Juniper Mist AI Admins Lookup API
  slug: mist-ai-admins-lookup-api
- description: Endpoints used to trigger a password recovery and validate the token sent by email.
  name: Juniper Mist AI Admins Recover Password API
  slug: mist-ai-admins-recover-password-api
- description: API Calls to retrieve constant values that can be used in different parts of the configuration
  name: Juniper Mist AI Constants Definitions API
  slug: mist-ai-constants-definitions-api
- description: API Calls to retrieve the definitions of the Mist events. These definitions are providing example of the Webhook payloads
  name: Juniper Mist AI Constants Events API
  slug: mist-ai-constants-events-api
- description: API Calls to retrieve the list of Hardware Models and their features
  name: Juniper Mist AI Constants Models API
  slug: mist-ai-constants-models-api
- description: In a typical enterprise, a separate group of people, Installers, are responsible for install new devices. May it be a new installation (e.g. new stores), a replacement installation (e.g. replacing Cis
  name: Juniper Mist AI Installer API
  slug: mist-ai-installer-api
- description: An MSP Admin refers to a user who has access to the Juniper Mist managed service provider (MSP) portal and is responsible for managing and administering the network operations of multiple customer org
  name: Juniper Mist AI MSPs Admins API
  slug: mist-ai-msps-admins-api
- description: MSP (Managed Service Provider) contains multiple Organizations.
  name: Juniper Mist AI MSPs API
  slug: mist-ai-msps-api
- description: API Calls to locate a device across all the Organizations attached to the MSP account.
  name: Juniper Mist AI MSPs Inventory API
  slug: mist-ai-msps-inventory-api
- description: Licenses are a type of service or access that customers can purchase for various features or services offered by a company. Subscriptions can have different statuses, such as active, expired, exceeded
  name: Juniper Mist AI MSPs Licenses API
  slug: mist-ai-msps-licenses-api
- description: Manage the Mist portal logo at the MSP level. This logo will be displayed instead of the Juniper Mist Logo for all the Organizations attached to this MSP account.
  name: Juniper Mist AI MSPs Logo API
  slug: mist-ai-msps-logo-api
- description: Audit Logs are records of activities initiated by users, providing a history of actions such as accessing, creating, updating, or deleting resources or components at the MSP level. These logs allow su
  name: Juniper Mist AI MSPs Logs API
  slug: mist-ai-msps-logs-api
- description: Marvis is an AI-driven, interactive virtual network assistant that streamlines network operations, simplifies troubleshooting, and provides an enhanced user experience. It offers real-time network vis
  name: Juniper Mist AI MSPs Marvis API
  slug: mist-ai-msps-marvis-api
- description: Org Groups a way to group Organizations together based on certain criteria. They can be used for easier management and organization of multiple organizations within the MSP portal.
  name: Juniper Mist AI MSPs Org Groups API
  slug: mist-ai-msps-org-groups-api
- description: An organization usually represents a customer - which has inventories, licenses. An Organization can contain multiple sites. A site usually represents a deployment at the same location (a campus, an o
  name: Juniper Mist AI MSPs Orgs API
  slug: mist-ai-msps-orgs-api
- description: SLEs, or Service-Level Expectations, are metrics used to monitor and report on the user experience of a Wireless, Wired or Wan network. They are generated through data science and machine learning alg
  name: Juniper Mist AI MSPs SLEs API
  slug: mist-ai-msps-sles-api
- description: MSP SSO, or Single Sign-On, is a method of authentication that allows users to securely log in to multiple applications and websites with a single set of login credentials. It involves integrating the
  name: Juniper Mist AI MSPs SSO API
  slug: mist-ai-msps-sso-api
- description: MSP SSO roles refer to the different functions assigned to users within a Single Sign-On (SSO) system. These roles determine the tasks and actions that users can perform within the SSO system. There a
  name: Juniper Mist AI MSPs SSO Roles API
  slug: mist-ai-msps-sso-roles-api
- description: Support tickets are a means for users to seek assistance and resolve issues they encounter with a product or service. They allow users to communicate their problems or questions to the Juniper Mist su
  name: Juniper Mist AI MSPs Tickets API
  slug: mist-ai-msps-tickets-api
- description: 'An org admin, or organization administrator, is a user with administrative privileges within a specific organization. They have the authority to manage and oversee the operations and settings of that '
  name: Juniper Mist AI Orgs Admins API
  slug: mist-ai-orgs-admins-api
- description: The "Advanced Anti-Malware" feature in Sky ATP is a comprehensive security solution that leverages multiple techniques to detect and prevent malware attacks. Here are the key components of this featur
  name: Juniper Mist AI Orgs Advanced Anti Malware Profiles API
  slug: mist-ai-orgs-advanced-anti-malware-profiles-api
- description: An Alarm Template is a set of Alarm Rules that could be applied to one or more sites (while each site can only pick one Alarm Template), or to the whole org. Once created, the Alarm template must be a
  name: Juniper Mist AI Orgs Alarm Templates API
  slug: mist-ai-orgs-alarm-templates-api
- description: Alarms are triggered based on certain events. Alarms could be configured using an Alarm Template.
  name: Juniper Mist AI Orgs Alarms API
  slug: mist-ai-orgs-alarms-api
- description: 'Antivirus profiles are used to define the content to scan for any malware and the action to be taken when malware is detected. These profiles can be assigned to Content Security policies to scan Web, '
  name: Juniper Mist AI Orgs Antivirus Profiles API
  slug: mist-ai-orgs-antivirus-profiles-api
- description: AP Templates are defining Wi-Fi and AP settings that can be assigned to Access Points based on different types of rules. AP Templates must be assigned to one or multiple sites to be used.
  name: Juniper Mist AI Orgs AP Templates API
  slug: mist-ai-orgs-ap-templates-api
- description: An organization usually represents a customer - which has inventories, licenses. An Organization can contain multiple sites. A site usually represents a deployment at the same location (a campus, an o
  name: Juniper Mist AI Orgs API
  slug: mist-ai-orgs-api
- description: Org API token is a unique identifier used by an application to authenticate and access a service's API. These tokens are used to authenticate requests made to the API server and ensure secure access t
  name: Juniper Mist AI Orgs API Tokens API
  slug: mist-ai-orgs-api-tokens-api
- description: An Asset Filter is a feature that allows users to define specific criteria or conditions to filter and display only certain assets based on their attributes or properties. This requires the Asset Visi
  name: Juniper Mist AI Orgs Asset Filters API
  slug: mist-ai-orgs-asset-filters-api
- description: An Asset refers to any equipment or item that is being tracked and monitored using Bluetooth Low Energy (BLE) beacon tags. This requires the Asset Visibility subscription.
  name: Juniper Mist AI Orgs Assets API
  slug: mist-ai-orgs-assets-api
- description: API Calls to manage Organization Certificates. The certificates can be used bu Access Assurance, during the SSO/SAML Authentication, ...
  name: Juniper Mist AI Orgs Cert API
  slug: mist-ai-orgs-cert-api
- description: Marvis Invites can be generated for (and belongs to) an Org. They can be generated by an Admin of an Org and can be revoked at anytime. Marvis Clients are devices that have the Marvis Android Client i
  name: Juniper Mist AI Orgs Clients - Marvis API
  slug: mist-ai-orgs-clients-marvis-api
- description: NAC Clients are devices connected to the network and authenticated by Juniper Mist Access Assurance.
  name: Juniper Mist AI Orgs Clients - NAC API
  slug: mist-ai-orgs-clients-nac-api
- description: SDK Clients are devices that have installed an application using the Mist Software Development Kit (SDK). These clients can provide specific data and information that is not available without the inst
  name: Juniper Mist AI Orgs Clients - SDK API
  slug: mist-ai-orgs-clients-sdk-api
- description: WAN Clients are devices connected to a Juniper SRX or SSX gateway monitor or managed by Mist
  name: Juniper Mist AI Orgs Clients - Wan API
  slug: mist-ai-orgs-clients-wan-api
- description: Wired Clients are Wired devices connected to a Juniper switch monitored or managed by Mist.
  name: Juniper Mist AI Orgs Clients - Wired API
  slug: mist-ai-orgs-clients-wired-api
- description: Wireless Clients are Wi-Fi devices connected to a Juniper Mist Access Point.
  name: Juniper Mist AI Orgs Clients - Wireless API
  slug: mist-ai-orgs-clients-wireless-api
- description: CRLs, or Certificate Revocation Lists, are time-stamped lists that identify digital certificates that have been invalidated before their expiration date. They include information about the reasons for
  name: Juniper Mist AI Orgs CRL API
  slug: mist-ai-orgs-crl-api
- description: 'While Templates / RF Templates / Network Templates / Gateway Templates provides powerful ways to control how a Device\''s configuration is derived for a Site. There are cases where you\''d like another '
  name: Juniper Mist AI Orgs Device Profiles API
  slug: mist-ai-orgs-device-profiles-api
- description: API Calls specific to AOS (Aruba Operating System) devices
  name: Juniper Mist AI Orgs Devices - AOS API
  slug: mist-ai-orgs-devices-aos-api
- description: Devices are any Network device managed or monitored by Juniper Mist. It can be * Wireless Access Points * Juniper Switch (EX, QFX) * Juniper WAN Gateway (SRX, SSR) * Mist Edges * Other or 3rd party de
  name: Juniper Mist AI Orgs Devices API
  slug: mist-ai-orgs-devices-api
- description: API Call for 3rd party devices
  name: Juniper Mist AI Orgs Devices - Others API
  slug: mist-ai-orgs-devices-others-api
- description: API Calls specific to SSR devices
  name: Juniper Mist AI Orgs Devices - SSR API
  slug: mist-ai-orgs-devices-ssr-api
- description: Orgs Events are all the system level changes at the org level
  name: Juniper Mist AI Orgs Events API
  slug: mist-ai-orgs-events-api
- description: EVPN allows an alternative but more efficient LAN architecture utilizing VxLAN / MP-BGP - separating control plane (MAC / IP Learning) from forwarding plane. In our implementation, following the steps
  name: Juniper Mist AI Orgs EVPN Topologies API
  slug: mist-ai-orgs-evpn-topologies-api
- description: Gateway Template is applied to a site for gateway(s) in a site. When Templates are not used, Site Setting holds settings for multiple device types and they can differ to set device_type specific confi
  name: Juniper Mist AI Orgs Gateway Templates API
  slug: mist-ai-orgs-gateway-templates-api
- description: Guests are users who are accessing the wi-fi network as a temporary or non-permanent visitor.
  name: Juniper Mist AI Orgs Guests API
  slug: mist-ai-orgs-guests-api
- description: An IDP profile is a set of predefined rules and actions that determine how the Intrusion Detection and Prevention (IDP) system handles network traffic. It allows you to selectively enforce attack dete
  name: Juniper Mist AI Orgs IDP Profiles API
  slug: mist-ai-orgs-idp-profiles-api
- description: The integration between Mist and Cradlepoint allows users to utilize Cradlepoint 5G cellular adapters with Juniper's wired, wireless, and SD-WAN solutions driven by Mist AI. With this integration, use
  name: Juniper Mist AI Orgs Integration Cradlepoint API
  slug: mist-ai-orgs-integration-cradlepoint-api
- description: 'JSE stands for Juniper Secure Edge and it is a feature within the Mist UI that allows customers to configure Secure Cloud Connectors. With JSE, users can establish a tunnel via IPSEC protocol and use '
  name: Juniper Mist AI Orgs Integration JSE API
  slug: mist-ai-orgs-integration-jse-api
- description: The Juniper Integration can be used to synchronize Juniper Support Insights (JSI) information.
  name: Juniper Mist AI Orgs Integration Juniper API
  slug: mist-ai-orgs-integration-juniper-api
- description: Sky Advanced Threat Prevention (Sky ATP) is a cloud-based security designed to detect and mitigate advanced threats in real-time, ensuring the security and integrity of your network. The integration o
  name: Juniper Mist AI Orgs Integration SkyATP API
  slug: mist-ai-orgs-integration-skyatp-api
- description: 'In Zscaler UI: 1. add Partner Integration at https://admin.zscalerbeta.net/#administration/partner-integration 2. Add Partner Administrator Role at https://admin.zscalerbeta.net/#administration/role-m'
  name: Juniper Mist AI Orgs Integration Zscaler API
  slug: mist-ai-orgs-integration-zscaler-api
- description: The Org Inventory allows administrators to view and manage all devices registered (claimed) to the Organization.
  name: Juniper Mist AI Orgs Inventory API
  slug: mist-ai-orgs-inventory-api
- description: Juniper Support Insight is a free service provided to all Mist customers. You can adopt your devices via a few lines CLI commands. Allowing you to * get some basic information about the adopted device
  name: Juniper Mist AI Orgs JSI API
  slug: mist-ai-orgs-jsi-api
- description: Licenses are a type of service or access that customers can purchase for various features or services offered by a company. Subscriptions can have different statuses, such as active, expired, exceeded
  name: Juniper Mist AI Orgs Licenses API
  slug: mist-ai-orgs-licenses-api
- description: Linked Application are Third party applications linked to the Mist Organization. This is usually using OAuth2.0 or API integrations for a Cloud-to-Cloud Communication.
  name: Juniper Mist AI Orgs Linked Applications API
  slug: mist-ai-orgs-linked-applications-api
- description: Audit Logs are records of activities initiated by users, providing a history of actions such as accessing, creating, updating, or deleting resources or components at the Org level. These logs allow su
  name: Juniper Mist AI Orgs Logs API
  slug: mist-ai-orgs-logs-api
- description: These API Calls to import Site Maps at the Org level
  name: Juniper Mist AI Orgs Maps API
  slug: mist-ai-orgs-maps-api
- description: Marvis is an AI-driven, interactive virtual network assistant that streamlines network operations, simplifies troubleshooting, and provides an enhanced user experience. It offers real-time network vis
  name: Juniper Mist AI Orgs Marvis API
  slug: mist-ai-orgs-marvis-api
- description: Marvis Clients are devices that have the Marvis Android Client installed on them and are connected to a Juniper Mist AP. They provide detailed data and telemetry about the client's wireless connection
  name: Juniper Mist AI Orgs Marvis Invites API
  slug: mist-ai-orgs-marvis-invites-api
- description: 'A Mist Edge Cluster (MxCluster) is a group of Juniper Mist Edge devices that are configured to work together in order to provide high availability and load balancing for the tunneling of traffic from '
  name: Juniper Mist AI Orgs MxClusters API
  slug: mist-ai-orgs-mxclusters-api
- description: A Mist Edge (MxEdge) is a physical or virtual appliance that is deployed in a network to provide centralized data path for user traffic or as a RADIUS Proxy, which was traditionally performed by legac
  name: Juniper Mist AI Orgs MxEdges API
  slug: mist-ai-orgs-mxedges-api
- description: A Mist Tunnel (MxTunnel) is a configuration object that allows for the tunneling of user VLANs from the Access Points (APs) to a central point on the network. It specifies the VLAN IDs that need to be
  name: Juniper Mist AI Orgs MxTunnels API
  slug: mist-ai-orgs-mxtunnels-api
- description: By default, Mist is automatically retrieving the PKI CRL by using the CRL Distribution Point provided by Certification Authority. In case this information is not provided, or the CRL is not publicly a
  name: Juniper Mist AI Orgs NAC CRL API
  slug: mist-ai-orgs-nac-crl-api
- description: The NAC IDP allows users to integrate with various Identity Providers (IDPs) to enhance authentication and access control. Admins can configure identity providers such as microsoft EntraID, okta workf
  name: Juniper Mist AI Orgs NAC IDP API
  slug: mist-ai-orgs-nac-idp-api
- description: NAC Portals are for onboard Wireless and Wired client with 802.1X The NAC Portal is a web-based interface that allows users to authenticate and gain access to the network. It is typically used for gue
  name: Juniper Mist AI Orgs NAC Portals API
  slug: mist-ai-orgs-nac-portals-api
- description: The NAC Rules (or Auth Policies) are a set of rules that devices and users must fulfill in order to gain access to the network and use network resources. Juniper Mist Access Assurance evaluates authen
  name: Juniper Mist AI Orgs NAC Rules API
  slug: mist-ai-orgs-nac-rules-api
- description: NAC Tags are the building blocks to compose nacrules. They can either appear in the "matching" / "not_matching" sections of a nacrule, in which case they play the role of classifiers, or they could ap
  name: Juniper Mist AI Orgs NAC Tags API
  slug: mist-ai-orgs-nac-tags-api
- description: A Network Template is a configuration template that allows for the consistent and standardized configuration of switches across an organization's network infrastructure. It includes settings such as r
  name: Juniper Mist AI Orgs Network Templates API
  slug: mist-ai-orgs-network-templates-api
- description: A Network refers to a group or segment of users that are defined for use across the entire organization.
  name: Juniper Mist AI Orgs Networks API
  slug: mist-ai-orgs-networks-api
- description: Premium Analytics is an advanced, cloud-based analytics service offered by Juniper Mist. It provides end-to-end network observability and allows users to gain unique insights into networking and locat
  name: Juniper Mist AI Orgs Premium Analytics API
  slug: mist-ai-orgs-premium-analytics-api
- description: PSK Self-Service Portals are for 1. **Wi-Fi users** who want to connect to a WLAN with personal PSK, they're told to connect to a URL where they can login (likely through company\u2019s SSO) and get t
  name: Juniper Mist AI Orgs Psk Portals API
  slug: mist-ai-orgs-psk-portals-api
- description: A multi PSK (Pre-Shared Key) is a feature that allows the use of multiple PSKs for securing network connections. It provides a simple and comprehensive way to onboard client devices without relying on
  name: Juniper Mist AI Orgs Psks API
  slug: mist-ai-orgs-psks-api
- description: API Calls to manage organization-level reports, such as E911 AP BSSID report exports.
  name: Juniper Mist AI Orgs Reports API
  slug: mist-ai-orgs-reports-api
- description: Rf Templates are a feature in Juniper Mist wireless assurance that allow for uniform radio configurations to be applied across all sites in an organization. These templates can be customized to includ
  name: Juniper Mist AI Orgs RF Templates API
  slug: mist-ai-orgs-rf-templates-api
- description: The Orgs SCEP API from Juniper Mist AI — 3 operation(s) for orgs scep.
  name: Juniper Mist AI Orgs SCEP API
  slug: mist-ai-orgs-scep-api
- description: SDK Invites can be generated for (and belongs to) an Org. They can be generated by an Admin of an Org and can be revoked at anytime.
  name: Juniper Mist AI Orgs SDK Invites API
  slug: mist-ai-orgs-sdk-invites-api
- description: The Orgs SDK Templates API from Juniper Mist AI — 2 operation(s) for orgs sdk templates.
  name: Juniper Mist AI Orgs SDK Templates API
  slug: mist-ai-orgs-sdk-templates-api
- description: Sky ATP Secintel Profile
  name: Juniper Mist AI Orgs SecIntel Profiles API
  slug: mist-ai-orgs-secintel-profiles-api
- description: 'Security Policy is designed to audit / catch discrepancies between "what''s intended to be running" versus "what''s actually running" in a network. Many big organizations have separated Security and IT '
  name: Juniper Mist AI Orgs Security Policies API
  slug: mist-ai-orgs-security-policies-api
- description: Services Policies are a security policy that defines who can access applications, they are used to control access to applications and ensure proper traffic management within a network. It determines t
  name: Juniper Mist AI Orgs Service Policies API
  slug: mist-ai-orgs-service-policies-api
- description: 'A Service refers to the applications that network users will connect to. These applications represent traffic destinations and are essential for defining network policies and security configurations. '
  name: Juniper Mist AI Orgs Services API
  slug: mist-ai-orgs-services-api
- description: API Calls to manage the Mist Organization Settings
  name: Juniper Mist AI Orgs Setting API
  slug: mist-ai-orgs-setting-api
- description: Site templates are pre-configured sets of attributes and settings that can be applied to one or more sites in a Mist Organization. These templates allow for quick and consistent configuration of sites
  name: Juniper Mist AI Orgs Site Templates API
  slug: mist-ai-orgs-site-templates-api
- description: Site groups are a group of sites under the same Org. It's many-to-many mapping to sites
  name: Juniper Mist AI Orgs Sitegroups API
  slug: mist-ai-orgs-sitegroups-api
- description: API Calls to Create or Get the Organization Sites. Use the [Site Settings](https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/setting/overview) to configure or update the Sit
  name: Juniper Mist AI Orgs Sites API
  slug: mist-ai-orgs-sites-api
- description: Org SLEs, or Service-Level Expectations, are metrics used to monitor and report on the user experience of a Wireless, Wired or Wan network. They are generated through data science and machine learning
  name: Juniper Mist AI Orgs SLEs API
  slug: mist-ai-orgs-sles-api
- description: Org SSO, or Single Sign-On, is a method of authentication that allows users to securely log in to multiple applications and websites with a single set of login credentials. It involves integrating the
  name: Juniper Mist AI Orgs SSO API
  slug: mist-ai-orgs-sso-api
- description: SSO roles refer to the different functions assigned to users within a Single Sign-On (SSO) system. These roles determine the tasks and actions that users can perform within the SSO system. There are t
  name: Juniper Mist AI Orgs SSO Roles API
  slug: mist-ai-orgs-sso-roles-api
- description: API Calls to retrieve statistics about the Mist Org and related items
  name: Juniper Mist AI Orgs Stats API
  slug: mist-ai-orgs-stats-api
- description: API Calls to retrieve statistics about the Assets at the Org level
  name: Juniper Mist AI Orgs Stats - Assets API
  slug: mist-ai-orgs-stats-assets-api
- description: API Calls to retrieve statistics about the BGP Peers (WAN Assurance)
  name: Juniper Mist AI Orgs Stats - BGP Peers API
  slug: mist-ai-orgs-stats-bgp-peers-api
- description: API Calls to retrieve statistics about the Mist Managed and Monitored Devices at the Org level By default, the API call only returns a subset of the available fields. Additional fields can be requeste
  name: Juniper Mist AI Orgs Stats - Devices API
  slug: mist-ai-orgs-stats-devices-api
- description: API Calls to retrieve statistics about the Mist Edges at the Org level
  name: Juniper Mist AI Orgs Stats - MxEdges API
  slug: mist-ai-orgs-stats-mxedges-api
- description: API Calls to retrieve statistics about OSPF peers at the Org level
  name: Juniper Mist AI Orgs Stats - Ospf API
  slug: mist-ai-orgs-stats-ospf-api
- description: API Calls to retrieve statistics about the Other/3rd party devices at the Org level
  name: Juniper Mist AI Orgs Stats - Other Devices API
  slug: mist-ai-orgs-stats-other-devices-api
- description: API Calls to retrieve statistics about the Wired Ports at the Org level
  name: Juniper Mist AI Orgs Stats - Ports API
  slug: mist-ai-orgs-stats-ports-api
- description: API Calls to retrieve statistics about the Organization Sites
  name: Juniper Mist AI Orgs Stats - Sites API
  slug: mist-ai-orgs-stats-sites-api
- description: API Calls to retrieve statistics about the Mist Tunnels at the Org level
  name: Juniper Mist AI Orgs Stats - Tunnels API
  slug: mist-ai-orgs-stats-tunnels-api
- description: API Calls to retrieve statistics about the VPN Peers (WAN Assurance)
  name: Juniper Mist AI Orgs Stats - VPN Peers API
  slug: mist-ai-orgs-stats-vpn-peers-api
- description: Support tickets are a means for users to seek assistance and resolve issues they encounter with a product or service. They allow users to communicate their problems or questions to the Juniper Mist su
  name: Juniper Mist AI Orgs Tickets API
  slug: mist-ai-orgs-tickets-api
- description: The Org UI Settings are used to configure the MArvis dashboards
  name: Juniper Mist AI Orgs UI Settings API
  slug: mist-ai-orgs-ui-settings-api
- description: NAC User MACs (Endpoints) provide a database of endpoints identified by their MAC addresses. They can be used assign each endpoint with various attributes, such as name, VLAN, role and client label. O
  name: Juniper Mist AI Orgs User MACs API
  slug: mist-ai-orgs-user-macs-api
- description: Vars endpoints are used to retrieve the list of Site Variables across all the Sites.
  name: Juniper Mist AI Orgs Vars API
  slug: mist-ai-orgs-vars-api
- description: VPNs endpoints are used to create the WAN Assurance Overlay configuration between a Hub and one or multiple WAN Edge Gateways. When configuring the Hub and Spokes from the Mist UI, the UI is automatic
  name: Juniper Mist AI Orgs VPNs API
  slug: mist-ai-orgs-vpns-api
- description: An Org Webhook is a configuration that allows real-time events and data from the Org to be pushed to a provided url. It enables the collection of information about various topics such as device events
  name: Juniper Mist AI Orgs Webhooks API
  slug: mist-ai-orgs-webhooks-api
- description: 'A WLAN template is a collection of WLAN policies, Tunneling Policies, and WxLAN policies. It is used for creating and managing WLAN configurations at an organizational level. WLAN templates allow for '
  name: Juniper Mist AI Orgs WLAN Templates API
  slug: mist-ai-orgs-wlan-templates-api
- description: An Org Wlan is a wireless local area network that is configured at the Org level and applied to a WLAN template. It allows for the creation and management of wireless network settings, such as SSIDs (
  name: Juniper Mist AI Orgs Wlans API
  slug: mist-ai-orgs-wlans-api
- description: ORg WxRules are a set of rules, restrictions, and settings that can be applied to WLANs within a specific WLAN Template. These policies determine how the devices and traffic are treated by the network
  name: Juniper Mist AI Orgs WxRules API
  slug: mist-ai-orgs-wxrules-api
- description: Wxtags are tags or groups that can be created and used within the Org. They are used to classify users and resources and can be applied to Access Points, WLAN configurations or WxRules within that sit
  name: Juniper Mist AI Orgs WxTags API
  slug: mist-ai-orgs-wxtags-api
- description: A WxLan Tunnel (WxTunnel) are used to create a secure connection between Juniper Mist Access Points and third-party VPN concentrators using protocols such as L2TPv3 or dmvpn. These tunnels allow for t
  name: Juniper Mist AI Orgs WxTunnels API
  slug: mist-ai-orgs-wxtunnels-api
- description: API calls related to the currently connected user account.
  name: Juniper Mist AI Self Account API
  slug: mist-ai-self-account-api
- description: API calls related to the alarm subscriptions for the currently connected user account.
  name: Juniper Mist AI Self Alarms API
  slug: mist-ai-self-alarms-api
- description: Like many other API providers, it's also possible to generate API Tokens to be used (in HTTP Header) for authentication. An API token ties to a Admin with equal or less privileges. **Notes:** * an API
  name: Juniper Mist AI Self API Token API
  slug: mist-ai-self-api-token-api
- description: API calls related to the audit logs subscriptions for the currently connected user account.
  name: Juniper Mist AI Self Audit Logs API
  slug: mist-ai-self-audit-logs-api
- description: API calls related to Two Factor Authentication for the currently connected user account.
  name: Juniper Mist AI Self MFA API
  slug: mist-ai-self-mfa-api
- description: 'A Mist account can be linked to OAuth2 providers: 1. First, login with your Mist account 2. Obtain the Authorization URL for Linking 3. Obtain the authorization code by clicking / going through Author'
  name: Juniper Mist AI Self OAuth2 API
  slug: mist-ai-self-oauth2-api
- description: The API Endpoints for the Advanced Anti Malware Profiles at the site level can be used to get the site derived profiles, meaning the org level configuration with the site variables resolved..
  name: Juniper Mist AI Sites Advanced Anti Malware Profiles API
  slug: mist-ai-sites-advanced-anti-malware-profiles-api
- description: Alarms are triggered based on certain events. Alarms could be configured using an [Orgs Alarm Template]($h/Orgs%20Alarm%20Templates/_overview).
  name: Juniper Mist AI Sites Alarms API
  slug: mist-ai-sites-alarms-api
- description: The Sites Anomaly API from Juniper Mist AI — 3 operation(s) for sites anomaly.
  name: Juniper Mist AI Sites Anomaly API
  slug: mist-ai-sites-anomaly-api
- description: The API Endpoints for the Antivirus Profiles at the site level can be used to get the site derived profiles, meaning the org level configuration with the site variables resolved..
  name: Juniper Mist AI Sites Antivirus Profiles API
  slug: mist-ai-sites-antivirus-profiles-api
- description: AP Templates are defining Wi-Fi and AP settings that can be assigned to Access Points based on different types of rules. Site AP Templates are created and managed at the site level and can only be ref
  name: Juniper Mist AI Sites AP Templates API
  slug: mist-ai-sites-ap-templates-api
- description: A site represents a project, a deployment. For MSP, it can be as small as a coffee shop or a five-star 600-room hotel. A site contains a set of Maps, Wlans, Policies, Zones.
  name: Juniper Mist AI Sites API
  slug: mist-ai-sites-api
- description: Applications contains a list of applications users are interested in monitoring / routing / policing
  name: Juniper Mist AI Sites Applications API
  slug: mist-ai-sites-applications-api
- description: An Asset Filter is a feature that allows users to define specific criteria or conditions to filter and display only certain assets based on their attributes or properties. Site Asset Filters are creat
  name: Juniper Mist AI Sites Asset Filters API
  slug: mist-ai-sites-asset-filters-api
- description: An Asset refers to any equipment or item that is being tracked and monitored using Bluetooth Low Energy (BLE) beacon tags. This requires the Asset Visibility subscription.
  name: Juniper Mist AI Sites Assets API
  slug: mist-ai-sites-assets-api
- description: Auto Map Assignment allows devices to be automatically assigned to maps based on their location data. These API calls can be used to manage, apply, and clear auto map assignments for devices at the si
  name: Juniper Mist AI Sites Auto Map Assignment API
  slug: mist-ai-sites-auto-map-assignment-api
- description: The Sites Beacons API from Juniper Mist AI — 2 operation(s) for sites beacons.
  name: Juniper Mist AI Sites Beacons API
  slug: mist-ai-sites-beacons-api
- description: NAC Clients are devices connected to the network and authenticated by Juniper Mist Access Assurance.
  name: Juniper Mist AI Sites Clients - NAC API
  slug: mist-ai-sites-clients-nac-api
- description: WAN Clients are devices connected to a Juniper SRX or SSX gateway monitor or managed by Mist
  name: Juniper Mist AI Sites Clients - Wan API
  slug: mist-ai-sites-clients-wan-api
- description: Wired Clients are Wired devices connected to a Juniper switch monitored or managed by Mist.
  name: Juniper Mist AI Sites Clients - Wired API
  slug: mist-ai-sites-clients-wired-api
- description: Wireless Clients are Wi-Fi devices connected to a Juniper Mist Access Point.
  name: Juniper Mist AI Sites Clients - Wireless API
  slug: mist-ai-sites-clients-wireless-api
- description: The API Endpoints for the Device Profiles at the site level can be used to get the site derived networks, meaning the org level configuration with the site variables resolved..
  name: Juniper Mist AI Sites Device Profiles API
  slug: mist-ai-sites-device-profiles-api
- description: Mist provides many ways (device_type specific template, site template, device profile, per-device) to configure devices for different kind of scenarios. The precedence goes from most specific to least
  name: Juniper Mist AI Sites Devices API
  slug: mist-ai-sites-devices-api
- description: API Call for 3rd party devices
  name: Juniper Mist AI Sites Devices - Others API
  slug: mist-ai-sites-devices-others-api
- description: API Calls specific to manage (form/delete) the SRX/SSR Clusters
  name: Juniper Mist AI Sites Devices - WAN Cluster API
  slug: mist-ai-sites-devices-wan-cluster-api
- description: API Calls specific to the Juniper Switches managed by Mist
  name: Juniper Mist AI Sites Devices - Wired API
  slug: mist-ai-sites-devices-wired-api
- description: API Calls specific to the Juniper Switches Virtual Chassis managed by Mist
  name: Juniper Mist AI Sites Devices - Wired - Virtual Chassis API
  slug: mist-ai-sites-devices-wired-virtual-chassis-api
- description: API Calls specific to the Mist Access Points
  name: Juniper Mist AI Sites Devices - Wireless API
  slug: mist-ai-sites-devices-wireless-api
- description: 'Site events are issues or incidents that affect site-assigned access points (aps) and radius, dhcp, and dns servers. They can be investigated and monitored using the insights dashboard in the juniper '
  name: Juniper Mist AI Sites Events API
  slug: mist-ai-sites-events-api
- description: EVPN allows an alternative but more efficient LAN architecture utilizing VxLAN / MP-BGP - separating control plane (MAC / IP Learning) from forwarding plane. In our implementation, following the steps
  name: Juniper Mist AI Sites EVPN Topologies API
  slug: mist-ai-sites-evpn-topologies-api
- description: The API Endpoints for the Gateway Templates at the site level can be used to get the site derived networks, meaning the org level configuration with the site variables resolved..
  name: Juniper Mist AI Sites Gateway Templates API
  slug: mist-ai-sites-gateway-templates-api
- description: Guests are users who are accessing the wi-fi network as a temporary or non-permanent visitor.
  name: Juniper Mist AI Sites Guests API
  slug: mist-ai-sites-guests-api
- description: The API Endpoints for the IDP Profiles at the site level can be used to get the site derived profiles, meaning the org level configuration with the site variables resolved..
  name: Juniper Mist AI Sites IDP Profiles API
  slug: mist-ai-sites-idp-profiles-api
- description: Insights is a feature that provides an overview of network experience across the entire site, access points, or clients. It offers useful information about current conditions, such as telemetry data f
  name: Juniper Mist AI Sites Insights API
  slug: mist-ai-sites-insights-api
- description: 'JSE stands for Juniper Secure Edge and it is a feature within the Mist UI that allows customers to configure Secure Cloud Connectors. With JSE, users can establish a tunnel via IPSEC protocol and use '
  name: Juniper Mist AI Sites JSE API
  slug: mist-ai-sites-jse-api
- description: The API Endpoints for the Licenses at the site level can be used to get license usages for a specific site.
  name: Juniper Mist AI Sites Licenses API
  slug: mist-ai-sites-licenses-api
- description: The Location Diagnostics allows users to retrieve and analyze coverage and performance data for mist access points (aps) and devices.
  name: Juniper Mist AI Sites Location API
  slug: mist-ai-sites-location-api
- description: Map Stacks are a way to group multiple maps together within a site, typically representing different floors or levels in a building. Map Stacks help organize and manage floorplans for multi-story buil
  name: Juniper Mist AI Sites Map Stacks API
  slug: mist-ai-sites-map-stacks-api
- description: A Site Map is a visual representation of the layout and structure of a location, such as a building or campus. It includes accurate information about the placement, positions, heights, and orientation
  name: Juniper Mist AI Sites Maps API
  slug: mist-ai-sites-maps-api
- description: '### AP Auto-Placement AP Auto-Placement is a feature in Juniper Mist wireless assurance that automatically determines and sets the positions of Access Points (APs) on a floorplan. It saves time and si'
  name: Juniper Mist AI Sites Maps - Auto-placement API
  slug: mist-ai-sites-maps-auto-placement-api
- description: The auto zones service is a map parsing service that uses map image data to suggest spaces to designate as location zones.
  name: Juniper Mist AI Sites Maps - Auto-Zone API
  slug: mist-ai-sites-maps-auto-zone-api
- description: MxEdges (Mist Edges) at the site level are deployed to tunnel traffic at each site due to network constraints or security concerns. They can be assigned to a specific site and configured to provide tu
  name: Juniper Mist AI Sites MxEdges API
  slug: mist-ai-sites-mxedges-api
- description: The NAC IDP allows users to integrate with various Identity Providers (IDPs) to enhance authentication and access control. Admins can configure identity providers such as microsoft EntraID, okta workf
  name: Juniper Mist AI Sites NAC Fingerprints API
  slug: mist-ai-sites-nac-fingerprints-api
- description: The API Endpoints for the Network Templates at the site level can be used to get the site derived networks, meaning the org level configuration with the site variables resolved.
  name: Juniper Mist AI Sites Network Templates API
  slug: mist-ai-sites-network-templates-api
- description: The API Endpoints for the Networks at the site level can be used to get the site derived networks, meaning the org level configuration with the site variables resolved.
  name: Juniper Mist AI Sites Networks API
  slug: mist-ai-sites-networks-api
- description: A multi PSK (Pre-Shared Key) is a feature that allows the use of multiple PSKs for securing network connections. It provides a simple and comprehensive way to onboard client devices without relying on
  name: Juniper Mist AI Sites Psks API
  slug: mist-ai-sites-psks-api
- description: The API Endpoints for the RF Templates at the site level can be used to get the site derived configuration, meaning the org level configuration with the site variables resolved..
  name: Juniper Mist AI Sites RF Templates API
  slug: mist-ai-sites-rf-templates-api
- description: Rf Diags is a feature in Juniper Mist location services that allows users to replay recorded sessions of the RF (radio frequency) environment. It enables users to gain an understanding of current issu
  name: Juniper Mist AI Sites Rfdiags API
  slug: mist-ai-sites-rfdiags-api
- description: 'Rogues are unauthorized wireless access points that are installed on a network without authorization. They can be connected to the LAN via an ethernet cable, similar to a pc, and are typically set up '
  name: Juniper Mist AI Sites Rogues API
  slug: mist-ai-sites-rogues-api
- description: RRM, or Radio Resource Management, is a tool used by large multi-site organizations to efficiently manage their RF spectrum. It involves making decisions on channel and power settings for access point
  name: Juniper Mist AI Sites RRM API
  slug: mist-ai-sites-rrm-api
- description: RSSI Zones are zones based on the RSSI (Received Signal Strength Indicator, i.e. the power of the signal received by the Access Points from the Wireless Clients).
  name: Juniper Mist AI Sites RSSI Zones API
  slug: mist-ai-sites-rssi-zones-api
- description: Sky ATP Secintel Profile
  name: Juniper Mist AI Sites SecIntel Profiles API
  slug: mist-ai-sites-secintel-profiles-api
- description: The API Endpoints for the Service Policies at the site level can be used to get the site derived configuration, meaning the merge between the site level configuration and the org level configuration.
  name: Juniper Mist AI Sites Service Policies API
  slug: mist-ai-sites-service-policies-api
- description: A Service represents an a traffic destination or an application that network users connect to. They are associated with users and networks and are used in application policies to permit or deny access
  name: Juniper Mist AI Sites Services API
  slug: mist-ai-sites-services-api
- description: Site settings refer to the configuration and management of of site within a Mist Organization. These settings include access point settings, firmware upgrade schedules, and various features such as lo
  name: Juniper Mist AI Sites Setting API
  slug: mist-ai-sites-setting-api
- description: The API Endpoints for the Site Templates at the site level can be used to get the site derived configuration, meaning the org level configuration with the site variables resolved..
  name: Juniper Mist AI Sites Site Templates API
  slug: mist-ai-sites-site-templates-api
- description: SkyATP is a cloud-based solution that provides advanced threat protection for network security. It allows security analysts to update their defense against new attack techniques in real-time and distr
  name: Juniper Mist AI Sites Skyatp API
  slug: mist-ai-sites-skyatp-api
- description: Site SLEs, or Service-Level Expectations, are metrics used to monitor and report on the user experience of a Wireless, Wired or Wan network. They are generated through data science and machine learnin
  name: Juniper Mist AI Sites SLEs API
  slug: mist-ai-sites-sles-api
- description: The Spectrum Analysis feature provides insights into the radio frequency environment, helping to identify interference and optimize wireless network performance. It allows users to monitor and analyze
  name: Juniper Mist AI Sites Spectrum Analysis API
  slug: mist-ai-sites-spectrum-analysis-api
- description: The stats are providing access to raw data about a specific type of entities.
  name: Juniper Mist AI Sites Stats API
  slug: mist-ai-sites-stats-api
- description: API Calls to retrieve the stats of the Applications used on side
  name: Juniper Mist AI Sites Stats - Apps API
  slug: mist-ai-sites-stats-apps-api
- description: The Sites Stats - Assets API from Juniper Mist AI — 7 operation(s) for sites stats - assets.
  name: Juniper Mist AI Sites Stats - Assets API
  slug: mist-ai-sites-stats-assets-api
- description: The Sites Stats - Beacons API from Juniper Mist AI — 1 operation(s) for sites stats - beacons.
  name: Juniper Mist AI Sites Stats - Beacons API
  slug: mist-ai-sites-stats-beacons-api
- description: API Calls to retrieve BGP Peers statistics of the Site Wen Edge Gateways at the Site level
  name: Juniper Mist AI Sites Stats - BGP Peers API
  slug: mist-ai-sites-stats-bgp-peers-api
- description: API Calls to retrieve the stats of the calls (Zoom/Teams) detected by Mist
  name: Juniper Mist AI Sites Stats - Calls API
  slug: mist-ai-sites-stats-calls-api
- description: SDK Clients are devices that have installed an application using the Mist Software Development Kit (SDK). These clients can provide specific data and information that is not available without the inst
  name: Juniper Mist AI Sites Stats - Clients SDK API
  slug: mist-ai-sites-stats-clients-sdk-api
- description: API Calls to retrieve the stats of the wireless clients detected (connected or not connected) on this site.
  name: Juniper Mist AI Sites Stats - Clients Wireless API
  slug: mist-ai-sites-stats-clients-wireless-api
- description: API Calls to retrieve statistics about the Mist Managed and Monitored Devices at the Site level
  name: Juniper Mist AI Sites Stats - Devices API
  slug: mist-ai-sites-stats-devices-api
- description: API Calls to retrieve statistics about the Discovered Switches at the Site level
  name: Juniper Mist AI Sites Stats - Discovered Switches API
  slug: mist-ai-sites-stats-discovered-switches-api
- description: API Calls to retrieve IoT Endpoint statistics for the current Site
  name: Juniper Mist AI Sites Stats - IoT Endpoints API
  slug: mist-ai-sites-stats-iot-endpoints-api
- description: API Calls to retrieve statistics about the Mist Edges at the Site level
  name: Juniper Mist AI Sites Stats - MxEdges API
  slug: mist-ai-sites-stats-mxedges-api
- description: API Calls to retrieve statistics about OSPF peers at the Site level
  name: Juniper Mist AI Sites Stats - Ospf API
  slug: mist-ai-sites-stats-ospf-api
- description: API Calls to retrieve statistics about the Wired Ports at the Site level
  name: Juniper Mist AI Sites Stats - Ports API
  slug: mist-ai-sites-stats-ports-api
- description: API Calls to retrieve WxRules statistics for the current Site
  name: Juniper Mist AI Sites Stats - WxRules API
  slug: mist-ai-sites-stats-wxrules-api
- description: API Calls to retrieve Zones statistics for the current Site
  name: Juniper Mist AI Sites Stats - Zones API
  slug: mist-ai-sites-stats-zones-api
- description: Synthetic Tests (Marvis Minis) are a feature of Juniper Networks' Mist platform, designed to proactively identify and resolve network issues before they impact users by simulating user connections and
  name: Juniper Mist AI Sites Synthetic Tests API
  slug: mist-ai-sites-synthetic-tests-api
- description: The Site UI Settings are used to configure the site Network and Analytics reports
  name: Juniper Mist AI Sites UI Settings API
  slug: mist-ai-sites-ui-settings-api
- description: A vBeacon is a virtual beacon that is created and configured on a floorplan and are configured with a name and message It is a Mist patented technology that provides proximity-related notifications to
  name: Juniper Mist AI Sites vBeacons API
  slug: mist-ai-sites-vbeacons-api
- description: API Calls to retrieve the list of Org VPNs configuration available for the Site
  name: Juniper Mist AI Sites VPNs API
  slug: mist-ai-sites-vpns-api
- description: API Calls to retrieve WAN Assurance statistics about the WAN Usage
  name: Juniper Mist AI Sites WAN Usages API
  slug: mist-ai-sites-wan-usages-api
- description: A Site Webhook is a configuration that allows real-time events and data from a specific site to be pushed to a provided url. It enables the collection of information about various topics such as devic
  name: Juniper Mist AI Sites Webhooks API
  slug: mist-ai-sites-webhooks-api
- description: A Site Wlan is a wireless local area network that is configured and applied to a specific site within an organization. It allows for the creation and management of wireless network settings, such as S
  name: Juniper Mist AI Sites Wlans API
  slug: mist-ai-sites-wlans-api
- description: Site WxRules are a set of rules, restrictions, and settings that can be applied to WLANs within a specific site. These policies determine how the devices and traffic are treated by the network and can
  name: Juniper Mist AI Sites WxRules API
  slug: mist-ai-sites-wxrules-api
- description: 'Wxtags are tags or groups that can be created and used within a specific site. They are used to classify users and resources and can be applied to Access Points, WLAN configurations or WxRules within '
  name: Juniper Mist AI Sites WxTags API
  slug: mist-ai-sites-wxtags-api
- description: A WxLan Tunnel (WxTunnel) are used to create a secure connection between Juniper Mist Access Points and third-party VPN concentrators using protocols such as L2TPv3 or dmvpn. These tunnels allow for t
  name: Juniper Mist AI Sites WxTunnels API
  slug: mist-ai-sites-wxtunnels-api
- description: A Zone is a custom area defined by a user on a floor plan. Zones can be used for capturing entry and exit events of clients, assets, and sdk clients, providing insights such as wait time and the numbe
  name: Juniper Mist AI Sites Zones API
  slug: mist-ai-sites-zones-api
- description: API Calls to use Devices Troubleshooting tools. Some API Calls can be used with any type of devices (Access Points, Switches and Gateways), and some others may be limited to some types of devices (e.g
  name: Juniper Mist AI Utilities Common API
  slug: mist-ai-utilities-common-api
- description: API Calls to use Devices Troubleshooting tools specific to Wired Assurance
  name: Juniper Mist AI Utilities LAN API
  slug: mist-ai-utilities-lan-api
- description: API Calls to use Devices Troubleshooting tools specific to Asset Tracking and User Management
  name: Juniper Mist AI Utilities Location API
  slug: mist-ai-utilities-location-api
- description: API Calls to use Devices Troubleshooting tools specific to Mx Edges
  name: Juniper Mist AI Utilities MxEdge API
  slug: mist-ai-utilities-mxedge-api
- description: API Calls to start, stop or managed Packet Captures at the device level
  name: Juniper Mist AI Utilities PCAPs API
  slug: mist-ai-utilities-pcaps-api
- description: API Calls used to manage device upgrades for a single device, at the site level or at the organization level.
  name: Juniper Mist AI Utilities Upgrade API
  slug: mist-ai-utilities-upgrade-api
- description: API Calls to use Devices Troubleshooting tools specific to WAN Assurance
  name: Juniper Mist AI Utilities WAN API
  slug: mist-ai-utilities-wan-api
- description: API Calls to use Devices Troubleshooting tools specific to Wireless Assurance
  name: Juniper Mist AI Utilities Wi-Fi API
  slug: mist-ai-utilities-wi-fi-api
artifact_total: 240
collections:
- collection_type: open
  name: Mist API
  slug: open-mist-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mist-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mist-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mist-ai-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.mist.com/
- group: start
  title: ''
  type: Portal
  url: https://www.juniper.net/us/en/solutions/ai-driven-enterprise.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.juniper.net/documentation/product/us/en/mist/
- group: docs
  title: ''
  type: Documentation
  url: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.juniper.net/documentation/us/en/software/mist/api/http/getting-started/how-to-get-started
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mist.com/
- group: operate
  title: ''
  type: Support
  url: https://www.mist.com/support/
- group: docs
  title: ''
  type: Documentation
  url: https://www.juniper.net/documentation/us/en/software/mist/mist-wireless/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.juniper.net/documentation/us/en/software/mist/mist-wired/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.juniper.net/documentation/us/en/software/mist/mist-wan-assurance/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.juniper.net/documentation/us/en/software/mist/mist-access-assurance/index.html
- group: learn
  title: ''
  type: Training
  url: https://learningportal.juniper.net/juniper/user_activity_info.aspx?id=11584
- group: operate
  title: ''
  type: Forums
  url: https://community.juniper.net/communities/community-home?CommunityKey=eef41fa9-dd0c-4eaf-93b6-94f08a0bf09a
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mistsys
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Mist-Automation-Programmability
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Juniper
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/mistsys/mist_openapi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Juniper/terraform-provider-mist
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Juniper/terraform-mist-modules
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mistsys/mist-vble-ios-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mistsys/mist-vble-android-sdk
- group: build
  title: ''
  type: Tools
  url: https://github.com/Mist-Automation-Programmability/mist_browser_extension
- group: build
  title: ''
  type: Tools
  url: https://github.com/Mist-Automation-Programmability/mist_psk
- group: build
  title: ''
  type: Tools
  url: https://github.com/Mist-Automation-Programmability/mist_switch_operator
- group: build
  title: ''
  type: Tools
  url: https://github.com/Mist-Automation-Programmability/mist_switch_converter
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Mist-Automation-Programmability/Mist-API-Cookbook
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Mist-Automation-Programmability/mist_websocket_examples
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.juniper.net/us/en/legal-notices.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.juniper.net/us/en/privacy-policy.html
- group: company
  title: ''
  type: Blog
  url: https://blogs.juniper.net/category/mist
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/juniper-mist-ai/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/JuniperNetworks
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/MistSystemsInc
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/mistsys/mist_openapi/blob/master/CHANGELOG.md
- group: docs
  title: ''
  type: Documentation
  url: https://www.juniper.net/documentation/us/en/software/mist/api/http/getting-started/regions
created: '2026-05-25T00:00:00.000Z'
description: Juniper Mist AI is the AI-driven enterprise networking platform that powers Juniper Networks' AI-Native Networking portfolio. Acquired by Juniper Networks in 2019, Mist pioneered cloud-native, microservices Wi-Fi and extended its AIOps approach across Wired Assurance (EX/QFX switches), WAN Assurance (SSR/SRX gateways), and Access Assurance (cloud NAC). The platform is anchored by Marvis — a conversational virtual network assistant — and the Mist Cloud API, an OpenAPI 3.1 surface of 736 paths and 2832 schemas served across 13 regional clouds (Global, EMEA, APAC, Federal). Real-time event flow ships over WebSocket subscriptions and outbound Webhooks; infrastructure-as-code is supported by an official Terraform provider; and indoor location is delivered through Virtual BLE with native iOS and Android SDKs.
features:
- AI-driven Wi-Fi Assurance with user-experience SLEs (Service Level Expectations) and proactive root-cause analysis
- AI-driven Wired Assurance for EX-series and QFX switches with port-level telemetry and SLEs
- AI-driven WAN Assurance for SSR and SRX-series Session Smart Routers with application-aware SLA monitoring
- Marvis Virtual Network Assistant — conversational AIOps with natural language queries and Marvis Actions
- Mist Access Assurance — cloud-delivered NAC with granular identity fingerprinting and zero-trust policy
- Premium Analytics — long-term retention dashboards across wireless, wired, and WAN with custom reports
- Mist Edge — on-premises tunnel terminator for L2/L3 roaming, RadSec proxy, and PoC handoff
- Indoor Location Services — Virtual Bluetooth LE (vBLE), zones, asset tracking, way-finding via mobile SDKs
- Microservices cloud-native architecture across 13 regional clouds (Global x5, EMEA x4, APAC x3, Federal)
- REST API with 736 paths and 2832 schemas covering the full configuration and telemetry surface
- WebSocket channels for real-time event streaming — device events, location, presence, RSSI, Marvis
- Outbound Webhooks with per-topic configuration (alarms, audits, device events, clients, zone enter/exit, occupancy)
- Per-Organization and per-User API tokens with optional 2FA and SSO (SAML 2.0, OAuth2)
- MSP (Managed Service Provider) tier for multi-org administration with logos, branding, and per-org licensing
- Org Groups for grouping organizations under common policies
- Org and Site templates — AP templates, RF templates, switch templates, gateway templates, alarm templates
- PSK Portals — pre-shared key self-service and admin lifecycle management
- PCAP cloud capture and AI-driven dynamic packet capture
- Marvis Actions for automated remediation recommendations
- Native integrations with Microsoft Intune, Jamf, Apple SSO, Google Workspace, Okta, Azure AD, ServiceNow
- Terraform provider (Juniper/mist) and reusable Terraform modules for IaC-driven network operations
- Mobile SDKs (iOS and Android) for indoor wayfinding and vBLE-based location applications
- Postman collection and OpenAPI 3.1 specification published in github.com/mistsys/mist_openapi
- Audit logs and webhook-based event streams for SIEM/SOAR integration
- Sky ATP (Secintel) profiles for Org and Site threat-intelligence enforcement
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mist-ai.png
layout: provider
modified: '2026-05-25'
name: Juniper Mist AI
nav: Providers
network: true
overview: 'Juniper Mist AI publishes 209 APIs on the [APIs.io](https://apis.io/) network, including Admins API, Admins Login API, Admins Login - OAuth2 API, and 206 more. Tagged areas include AI, AIOps, Artificial Intelligence, Networking, and Wi-Fi.


  Juniper Mist AI''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, training material, tooling, and 31 more developer resources.'
random_paper: 27
score:
  band: developing
  composite: 43.6
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 65.8
    developer_ergonomics: 60.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 209
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mist-ai/refs/heads/main/screenshots/mist-ai-2026-06-20T185612.png
security:
- kind: authentication
  name: Mist Ai Authentication
  slug: mist-ai-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Mist Ai Domain Security
  slug: mist-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mist-ai
tags:
- AI
- AIOps
- Artificial Intelligence
- Networking
- Wi-Fi
- Wireless LAN
- WAN
- SD-WAN
- Wired
- LAN
- Access Points
- Switches
- Routers
- Marvis
- NAC
- Access Assurance
- Location Services
- Bluetooth LE
- Indoor Location
- Cloud Networking
- Microservices
- Enterprise Networking
- AI Native Networking
website: https://www.mist.com/
---
