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
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 525
  human_in_the_loop: 15
  name: Mist Agentic Access
  operation_count: 1050
  slug: mist-agentic-access
  summary_line: 1050 operations · 525 acting · 15 human-in-the-loop
api_count: 1
apis:
- description: 'Admin API calls can be used to create, manage or authenticate Mist administrators. To register administrators into an existing MSP account or Organization, please check: * [Invite Msp Admin](/#operati'
  name: Mist Admins API
  slug: mist-admins-api
- description: 'Login Endpoints when using Login/Password authentication, with or without 2FA. If the Login/Password authentication is successful, Mist will add a `csrftoken` cookie that must be added into the later '
  name: Mist Admins Login API
  slug: mist-admins-login-api
- description: 'A Mist account can be linked to OAuth2 providers: 1. First, login with your Mist account 2. Obtain the Authorization URL for Linking with [Get Oauth 2 Authorization Url for Login](/#operations/getOaut'
  name: Mist Admins Login - OAuth2 API
  slug: mist-admins-login-oauth2-api
- description: Logout Endpoints when using Login/Password authentication, with or without 2FA.
  name: Mist Admins Logout API
  slug: mist-admins-logout-api
- description: Admin Lookup API Call is mainly used by Web UIs to know if a user must be redirected to an SSO URL for login.
  name: Mist Admins Lookup API
  slug: mist-admins-lookup-api
- description: Endpoints used to trigger a password recovery and validate the token sent by email.
  name: Mist Admins Recover Password API
  slug: mist-admins-recover-password-api
- description: API Calls to retrieve constant values that can be used in different parts of the configuration
  name: Mist Constants Definitions API
  slug: mist-constants-definitions-api
- description: API Calls to retrieve the definitions of the Mist events. These definitions are providing example of the Webhook payloads
  name: Mist Constants Events API
  slug: mist-constants-events-api
- description: API Calls to retrieve the list of Hardware Models and their features
  name: Mist Constants Models API
  slug: mist-constants-models-api
- description: In a typical enterprise, a separate group of people, Installers, are responsible for install new devices. May it be a new installation (e.g. new stores), a replacement installation (e.g. replacing Cis
  name: Mist Installer API
  slug: mist-installer-api
- description: An MSP Admin refers to a user who has access to the Juniper Mist managed service provider (MSP) portal and is responsible for managing and administering the network operations of multiple customer org
  name: Mist MSPs Admins API
  slug: mist-msps-admins-api
- description: MSP (Managed Service Provider) contains multiple Organizations.
  name: Mist MSPs API
  slug: mist-msps-api
- description: API Calls to locate a device across all the Organizations attached to the MSP account.
  name: Mist MSPs Inventory API
  slug: mist-msps-inventory-api
- description: Licenses are a type of service or access that customers can purchase for various features or services offered by a company. Subscriptions can have different statuses, such as active, expired, exceeded
  name: Mist MSPs Licenses API
  slug: mist-msps-licenses-api
- description: Manage the Mist portal logo at the MSP level. This logo will be displayed instead of the Juniper Mist Logo for all the Organizations attached to this MSP account.
  name: Mist MSPs Logo API
  slug: mist-msps-logo-api
- description: Audit Logs are records of activities initiated by users, providing a history of actions such as accessing, creating, updating, or deleting resources or components at the MSP level. These logs allow su
  name: Mist MSPs Logs API
  slug: mist-msps-logs-api
- description: Marvis is an AI-driven, interactive virtual network assistant that streamlines network operations, simplifies troubleshooting, and provides an enhanced user experience. It offers real-time network vis
  name: Mist MSPs Marvis API
  slug: mist-msps-marvis-api
- description: Org Groups a way to group Organizations together based on certain criteria. They can be used for easier management and organization of multiple organizations within the MSP portal.
  name: Mist MSPs Org Groups API
  slug: mist-msps-org-groups-api
- description: An organization usually represents a customer - which has inventories, licenses. An Organization can contain multiple sites. A site usually represents a deployment at the same location (a campus, an o
  name: Mist MSPs Orgs API
  slug: mist-msps-orgs-api
- description: SLEs, or Service-Level Expectations, are metrics used to monitor and report on the user experience of a Wireless, Wired or Wan network. They are generated through data science and machine learning alg
  name: Mist MSPs SLEs API
  slug: mist-msps-sles-api
- description: MSP SSO, or Single Sign-On, is a method of authentication that allows users to securely log in to multiple applications and websites with a single set of login credentials. It involves integrating the
  name: Mist MSPs SSO API
  slug: mist-msps-sso-api
- description: MSP SSO roles refer to the different functions assigned to users within a Single Sign-On (SSO) system. These roles determine the tasks and actions that users can perform within the SSO system. There a
  name: Mist MSPs SSO Roles API
  slug: mist-msps-sso-roles-api
- description: Support tickets are a means for users to seek assistance and resolve issues they encounter with a product or service. They allow users to communicate their problems or questions to the Juniper Mist su
  name: Mist MSPs Tickets API
  slug: mist-msps-tickets-api
- description: 'An org admin, or organization administrator, is a user with administrative privileges within a specific organization. They have the authority to manage and oversee the operations and settings of that '
  name: Mist Orgs Admins API
  slug: mist-orgs-admins-api
- description: The "Advanced Anti-Malware" feature in Sky ATP is a comprehensive security solution that leverages multiple techniques to detect and prevent malware attacks. Here are the key components of this featur
  name: Mist Orgs Advanced Anti Malware Profiles API
  slug: mist-orgs-advanced-anti-malware-profiles-api
- description: An Alarm Template is a set of Alarm Rules that could be applied to one or more sites (while each site can only pick one Alarm Template), or to the whole org. Once created, the Alarm template must be a
  name: Mist Orgs Alarm Templates API
  slug: mist-orgs-alarm-templates-api
- description: Alarms are triggered based on certain events. Alarms could be configured using an Alarm Template.
  name: Mist Orgs Alarms API
  slug: mist-orgs-alarms-api
- description: 'Antivirus profiles are used to define the content to scan for any malware and the action to be taken when malware is detected. These profiles can be assigned to Content Security policies to scan Web, '
  name: Mist Orgs Antivirus Profiles API
  slug: mist-orgs-antivirus-profiles-api
- description: AP Templates are defining Wi-Fi and AP settings that can be assigned to Access Points based on different types of rules. AP Templates must be assigned to one or multiple sites to be used.
  name: Mist Orgs AP Templates API
  slug: mist-orgs-ap-templates-api
- description: An organization usually represents a customer - which has inventories, licenses. An Organization can contain multiple sites. A site usually represents a deployment at the same location (a campus, an o
  name: Mist Orgs API
  slug: mist-orgs-api
- description: Org API token is a unique identifier used by an application to authenticate and access a service's API. These tokens are used to authenticate requests made to the API server and ensure secure access t
  name: Mist Orgs API Tokens API
  slug: mist-orgs-api-tokens-api
- description: An Asset Filter is a feature that allows users to define specific criteria or conditions to filter and display only certain assets based on their attributes or properties. This requires the Asset Visi
  name: Mist Orgs Asset Filters API
  slug: mist-orgs-asset-filters-api
- description: An Asset refers to any equipment or item that is being tracked and monitored using Bluetooth Low Energy (BLE) beacon tags. This requires the Asset Visibility subscription.
  name: Mist Orgs Assets API
  slug: mist-orgs-assets-api
- description: API Calls to manage Organization Certificates. The certificates can be used bu Access Assurance, during the SSO/SAML Authentication, ...
  name: Mist Orgs Cert API
  slug: mist-orgs-cert-api
- description: Marvis Invites can be generated for (and belongs to) an Org. They can be generated by an Admin of an Org and can be revoked at anytime. Marvis Clients are devices that have the Marvis Android Client i
  name: Mist Orgs Clients - Marvis API
  slug: mist-orgs-clients-marvis-api
- description: NAC Clients are devices connected to the network and authenticated by Juniper Mist Access Assurance.
  name: Mist Orgs Clients - NAC API
  slug: mist-orgs-clients-nac-api
- description: SDK Clients are devices that have installed an application using the Mist Software Development Kit (SDK). These clients can provide specific data and information that is not available without the inst
  name: Mist Orgs Clients - SDK API
  slug: mist-orgs-clients-sdk-api
- description: WAN Clients are devices connected to a Juniper SRX or SSX gateway monitor or managed by Mist
  name: Mist Orgs Clients - Wan API
  slug: mist-orgs-clients-wan-api
- description: Wired Clients are Wired devices connected to a Juniper switch monitored or managed by Mist.
  name: Mist Orgs Clients - Wired API
  slug: mist-orgs-clients-wired-api
- description: Wireless Clients are Wi-Fi devices connected to a Juniper Mist Access Point.
  name: Mist Orgs Clients - Wireless API
  slug: mist-orgs-clients-wireless-api
- description: CRLs, or Certificate Revocation Lists, are time-stamped lists that identify digital certificates that have been invalidated before their expiration date. They include information about the reasons for
  name: Mist Orgs CRL API
  slug: mist-orgs-crl-api
- description: 'While Templates / RF Templates / Network Templates / Gateway Templates provides powerful ways to control how a Device\''s configuration is derived for a Site. There are cases where you\''d like another '
  name: Mist Orgs Device Profiles API
  slug: mist-orgs-device-profiles-api
- description: API Calls specific to AOS (Aruba Operating System) devices
  name: Mist Orgs Devices - AOS API
  slug: mist-orgs-devices-aos-api
- description: Devices are any Network device managed or monitored by Juniper Mist. It can be * Wireless Access Points * Juniper Switch (EX, QFX) * Juniper WAN Gateway (SRX, SSR) * Mist Edges * Other or 3rd party de
  name: Mist Orgs Devices API
  slug: mist-orgs-devices-api
- description: API Call for 3rd party devices
  name: Mist Orgs Devices - Others API
  slug: mist-orgs-devices-others-api
- description: API Calls specific to SSR devices
  name: Mist Orgs Devices - SSR API
  slug: mist-orgs-devices-ssr-api
- description: Orgs Events are all the system level changes at the org level
  name: Mist Orgs Events API
  slug: mist-orgs-events-api
- description: EVPN allows an alternative but more efficient LAN architecture utilizing VxLAN / MP-BGP - separating control plane (MAC / IP Learning) from forwarding plane. In our implementation, following the steps
  name: Mist Orgs EVPN Topologies API
  slug: mist-orgs-evpn-topologies-api
- description: Gateway Template is applied to a site for gateway(s) in a site. When Templates are not used, Site Setting holds settings for multiple device types and they can differ to set device_type specific confi
  name: Mist Orgs Gateway Templates API
  slug: mist-orgs-gateway-templates-api
- description: Guests are users who are accessing the wi-fi network as a temporary or non-permanent visitor.
  name: Mist Orgs Guests API
  slug: mist-orgs-guests-api
- description: An IDP profile is a set of predefined rules and actions that determine how the Intrusion Detection and Prevention (IDP) system handles network traffic. It allows you to selectively enforce attack dete
  name: Mist Orgs IDP Profiles API
  slug: mist-orgs-idp-profiles-api
- description: The integration between Mist and Cradlepoint allows users to utilize Cradlepoint 5G cellular adapters with Juniper's wired, wireless, and SD-WAN solutions driven by Mist AI. With this integration, use
  name: Mist Orgs Integration Cradlepoint API
  slug: mist-orgs-integration-cradlepoint-api
- description: 'JSE stands for Juniper Secure Edge and it is a feature within the Mist UI that allows customers to configure Secure Cloud Connectors. With JSE, users can establish a tunnel via IPSec protocol and use '
  name: Mist Orgs Integration JSE API
  slug: mist-orgs-integration-jse-api
- description: The Juniper Integration can be used to synchronize Juniper Support Insights (JSI) information.
  name: Mist Orgs Integration Juniper API
  slug: mist-orgs-integration-juniper-api
- description: Sky Advanced Threat Prevention (Sky ATP) is a cloud-based security designed to detect and mitigate advanced threats in real-time, ensuring the security and integrity of your network. The integration o
  name: Mist Orgs Integration SkyATP API
  slug: mist-orgs-integration-skyatp-api
- description: 'In Zscaler UI: 1. add Partner Integration at https://admin.zscalerbeta.net/#administration/partner-integration 2. Add Partner Administrator Role at https://admin.zscalerbeta.net/#administration/role-m'
  name: Mist Orgs Integration Zscaler API
  slug: mist-orgs-integration-zscaler-api
- description: The Org Inventory allows administrators to view and manage all devices registered (claimed) to the Organization.
  name: Mist Orgs Inventory API
  slug: mist-orgs-inventory-api
- description: Juniper Support Insight is a free service provided to all Mist customers. You can adopt your devices via a few lines CLI commands. Allowing you to * get some basic information about the adopted device
  name: Mist Orgs JSI API
  slug: mist-orgs-jsi-api
- description: Licenses are a type of service or access that customers can purchase for various features or services offered by a company. Subscriptions can have different statuses, such as active, expired, exceeded
  name: Mist Orgs Licenses API
  slug: mist-orgs-licenses-api
- description: Linked Application are Third party applications linked to the Mist Organization. This is usually using OAuth2.0 or API integrations for a Cloud-to-Cloud Communication.
  name: Mist Orgs Linked Applications API
  slug: mist-orgs-linked-applications-api
- description: Audit Logs are records of activities initiated by users, providing a history of actions such as accessing, creating, updating, or deleting resources or components at the Org level. These logs allow su
  name: Mist Orgs Logs API
  slug: mist-orgs-logs-api
- description: These API Calls to import Site Maps at the Org level
  name: Mist Orgs Maps API
  slug: mist-orgs-maps-api
- description: Marvis is an AI-driven, interactive virtual network assistant that streamlines network operations, simplifies troubleshooting, and provides an enhanced user experience. It offers real-time network vis
  name: Mist Orgs Marvis API
  slug: mist-orgs-marvis-api
- description: Marvis Clients are devices that have the Marvis Android Client installed on them and are connected to a Juniper Mist AP. They provide detailed data and telemetry about the client's wireless connection
  name: Mist Orgs Marvis Invites API
  slug: mist-orgs-marvis-invites-api
- description: 'A Mist Edge Cluster (MxCluster) is a group of Juniper Mist Edge devices that are configured to work together in order to provide high availability and load balancing for the tunneling of traffic from '
  name: Mist Orgs MxClusters API
  slug: mist-orgs-mxclusters-api
- description: A Mist Edge (MxEdge) is a physical or virtual appliance that is deployed in a network to provide centralized data path for user traffic or as a RADIUS Proxy, which was traditionally performed by legac
  name: Mist Orgs MxEdges API
  slug: mist-orgs-mxedges-api
- description: A Mist Tunnel (MxTunnel) is a configuration object that allows for the tunneling of user VLANs from the Access Points (APs) to a central point on the network. It specifies the VLAN IDs that need to be
  name: Mist Orgs MxTunnels API
  slug: mist-orgs-mxtunnels-api
- description: By default, Mist is automatically retrieving the PKI CRL by using the CRL Distribution Point provided by Certification Authority. In case this information is not provided, or the CRL is not publicly a
  name: Mist Orgs NAC CRL API
  slug: mist-orgs-nac-crl-api
- description: The NAC IDP allows users to integrate with various Identity Providers (IDPs) to enhance authentication and access control. Admins can configure identity providers such as microsoft EntraID, okta workf
  name: Mist Orgs NAC IDP API
  slug: mist-orgs-nac-idp-api
- description: NAC Portals are for onboard Wireless and Wired client with 802.1X The NAC Portal is a web-based interface that allows users to authenticate and gain access to the network. It is typically used for gue
  name: Mist Orgs NAC Portals API
  slug: mist-orgs-nac-portals-api
- description: The NAC Rules (or Auth Policies) are a set of rules that devices and users must fulfill in order to gain access to the network and use network resources. Juniper Mist Access Assurance evaluates authen
  name: Mist Orgs NAC Rules API
  slug: mist-orgs-nac-rules-api
- description: NAC Tags are the building blocks to compose nacrules. They can either appear in the "matching" / "not_matching" sections of a nacrule, in which case they play the role of classifiers, or they could ap
  name: Mist Orgs NAC Tags API
  slug: mist-orgs-nac-tags-api
- description: A Network Template is a configuration template that allows for the consistent and standardized configuration of switches across an organization's network infrastructure. It includes settings such as R
  name: Mist Orgs Network Templates API
  slug: mist-orgs-network-templates-api
- description: A Network refers to a group or segment of users that are defined for use across the entire organization.
  name: Mist Orgs Networks API
  slug: mist-orgs-networks-api
- description: Premium Analytics is an advanced, cloud-based analytics service offered by Juniper Mist. It provides end-to-end network observability and allows users to gain unique insights into networking and locat
  name: Mist Orgs Premium Analytics API
  slug: mist-orgs-premium-analytics-api
- description: PSK Self-Service Portals are for 1. **Wi-Fi users** who want to connect to a WLAN with personal PSK, they're told to connect to a URL where they can login (likely through company\u2019s SSO) and get t
  name: Mist Orgs Psk Portals API
  slug: mist-orgs-psk-portals-api
- description: A multi PSK (Pre-Shared Key) is a feature that allows the use of multiple PSKs for securing network connections. It provides a simple and comprehensive way to onboard client devices without relying on
  name: Mist Orgs Psks API
  slug: mist-orgs-psks-api
- description: API Calls to manage organization-level reports, such as E911 AP BSSID report exports.
  name: Mist Orgs Reports API
  slug: mist-orgs-reports-api
- description: Rf Templates are a feature in Juniper Mist wireless assurance that allow for uniform radio configurations to be applied across all sites in an organization. These templates can be customized to includ
  name: Mist Orgs RF Templates API
  slug: mist-orgs-rf-templates-api
- description: The Orgs SCEP API from Mist — 3 operation(s) for orgs scep.
  name: Mist Orgs SCEP API
  slug: mist-orgs-scep-api
- description: SDK Invites can be generated for (and belongs to) an Org. They can be generated by an Admin of an Org and can be revoked at anytime.
  name: Mist Orgs SDK Invites API
  slug: mist-orgs-sdk-invites-api
- description: The Orgs SDK Templates API from Mist — 2 operation(s) for orgs sdk templates.
  name: Mist Orgs SDK Templates API
  slug: mist-orgs-sdk-templates-api
- description: Sky ATP Secintel Profile
  name: Mist Orgs SecIntel Profiles API
  slug: mist-orgs-secintel-profiles-api
- description: 'Security Policy is designed to audit / catch discrepancies between "what''s intended to be running" versus "what''s actually running" in a network. Many big organizations have separated Security and IT '
  name: Mist Orgs Security Policies API
  slug: mist-orgs-security-policies-api
- description: Services Policies are a security policy that defines who can access applications, they are used to control access to applications and ensure proper traffic management within a network. It determines t
  name: Mist Orgs Service Policies API
  slug: mist-orgs-service-policies-api
- description: 'A Service refers to the applications that network users will connect to. These applications represent traffic destinations and are essential for defining network policies and security configurations. '
  name: Mist Orgs Services API
  slug: mist-orgs-services-api
- description: API Calls to manage the Mist Organization Settings
  name: Mist Orgs Setting API
  slug: mist-orgs-setting-api
- description: Site templates are pre-configured sets of attributes and settings that can be applied to one or more sites in a Mist Organization. These templates allow for quick and consistent configuration of sites
  name: Mist Orgs Site Templates API
  slug: mist-orgs-site-templates-api
- description: Site groups are a group of sites under the same Org. It's many-to-many mapping to sites
  name: Mist Orgs Sitegroups API
  slug: mist-orgs-sitegroups-api
- description: API Calls to Create or Get the Organization Sites. Use the [Site Settings](https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/setting/overview) to configure or update the Sit
  name: Mist Orgs Sites API
  slug: mist-orgs-sites-api
- description: Org SLEs, or Service-Level Expectations, are metrics used to monitor and report on the user experience of a Wireless, Wired or Wan network. They are generated through data science and machine learning
  name: Mist Orgs SLEs API
  slug: mist-orgs-sles-api
- description: Org SSO, or Single Sign-On, is a method of authentication that allows users to securely log in to multiple applications and websites with a single set of login credentials. It involves integrating the
  name: Mist Orgs SSO API
  slug: mist-orgs-sso-api
- description: SSO roles refer to the different functions assigned to users within a Single Sign-On (SSO) system. These roles determine the tasks and actions that users can perform within the SSO system. There are t
  name: Mist Orgs SSO Roles API
  slug: mist-orgs-sso-roles-api
- description: API Calls to retrieve statistics about the Mist Org and related items
  name: Mist Orgs Stats API
  slug: mist-orgs-stats-api
- description: API Calls to retrieve statistics about the Assets at the Org level
  name: Mist Orgs Stats - Assets API
  slug: mist-orgs-stats-assets-api
- description: API Calls to retrieve statistics about the BGP Peers (WAN Assurance)
  name: Mist Orgs Stats - BGP Peers API
  slug: mist-orgs-stats-bgp-peers-api
- description: API Calls to retrieve statistics about the Mist Managed and Monitored Devices at the Org level By default, the API call only returns a subset of the available fields. Additional fields can be requeste
  name: Mist Orgs Stats - Devices API
  slug: mist-orgs-stats-devices-api
- description: The Orgs Stats - Marvis Clients API from Mist — 2 operation(s) for orgs stats - marvis clients.
  name: Mist Orgs Stats - Marvis Clients API
  slug: mist-orgs-stats-marvis-clients-api
- description: API Calls to retrieve statistics about the Mist Edges at the Org level
  name: Mist Orgs Stats - MxEdges API
  slug: mist-orgs-stats-mxedges-api
- description: API Calls to retrieve statistics about OSPF peers at the Org level
  name: Mist Orgs Stats - Ospf API
  slug: mist-orgs-stats-ospf-api
- description: API Calls to retrieve statistics about the Other/3rd party devices at the Org level
  name: Mist Orgs Stats - Other Devices API
  slug: mist-orgs-stats-other-devices-api
- description: API Calls to retrieve statistics about the Wired Ports at the Org level
  name: Mist Orgs Stats - Ports API
  slug: mist-orgs-stats-ports-api
- description: API Calls to retrieve statistics about the Organization Sites
  name: Mist Orgs Stats - Sites API
  slug: mist-orgs-stats-sites-api
- description: API Calls to retrieve statistics about the Mist Tunnels at the Org level
  name: Mist Orgs Stats - Tunnels API
  slug: mist-orgs-stats-tunnels-api
- description: API Calls to retrieve statistics about the VPN Peers (WAN Assurance)
  name: Mist Orgs Stats - VPN Peers API
  slug: mist-orgs-stats-vpn-peers-api
- description: Support tickets are a means for users to seek assistance and resolve issues they encounter with a product or service. They allow users to communicate their problems or questions to the Juniper Mist su
  name: Mist Orgs Tickets API
  slug: mist-orgs-tickets-api
- description: The Org UI Settings are used to configure the MArvis dashboards
  name: Mist Orgs UI Settings API
  slug: mist-orgs-ui-settings-api
- description: NAC User MACs (Endpoints) provide a database of endpoints identified by their MAC addresses. They can be used assign each endpoint with various attributes, such as name, VLAN, role and client label. O
  name: Mist Orgs User MACs API
  slug: mist-orgs-user-macs-api
- description: Vars endpoints are used to retrieve the list of Site Variables across all the Sites.
  name: Mist Orgs Vars API
  slug: mist-orgs-vars-api
- description: VPNs endpoints are used to create the WAN Assurance Overlay configuration between a Hub and one or multiple WAN Edge Gateways. When configuring the Hub and Spokes from the Mist UI, the UI is automatic
  name: Mist Orgs VPNs API
  slug: mist-orgs-vpns-api
- description: An Org Webhook is a configuration that allows real-time events and data from the Org to be pushed to a provided url. It enables the collection of information about various topics such as device events
  name: Mist Orgs Webhooks API
  slug: mist-orgs-webhooks-api
- description: 'A WLAN template is a collection of WLAN policies, Tunneling Policies, and WxLAN policies. It is used for creating and managing WLAN configurations at an organizational level. WLAN templates allow for '
  name: Mist Orgs WLAN Templates API
  slug: mist-orgs-wlan-templates-api
- description: An Org Wlan is a wireless local area network that is configured at the Org level and applied to a WLAN template. It allows for the creation and management of wireless network settings, such as SSIDs (
  name: Mist Orgs Wlans API
  slug: mist-orgs-wlans-api
- description: ORg WxRules are a set of rules, restrictions, and settings that can be applied to WLANs within a specific WLAN Template. These policies determine how the devices and traffic are treated by the network
  name: Mist Orgs WxRules API
  slug: mist-orgs-wxrules-api
- description: Wxtags are tags or groups that can be created and used within the Org. They are used to classify users and resources and can be applied to Access Points, WLAN configurations or WxRules within that sit
  name: Mist Orgs WxTags API
  slug: mist-orgs-wxtags-api
- description: A WxLan Tunnel (WxTunnel) are used to create a secure connection between Juniper Mist Access Points and third-party VPN concentrators using protocols such as L2TPv3 or dmvpn. These tunnels allow for t
  name: Mist Orgs WxTunnels API
  slug: mist-orgs-wxtunnels-api
- description: API calls related to the currently connected user account.
  name: Mist Self Account API
  slug: mist-self-account-api
- description: API calls related to the alarm subscriptions for the currently connected user account.
  name: Mist Self Alarms API
  slug: mist-self-alarms-api
- description: Like many other API providers, it's also possible to generate API Tokens to be used (in HTTP Header) for authentication. An API token ties to a Admin with equal or less privileges. **Notes:** * an API
  name: Mist Self API Token API
  slug: mist-self-api-token-api
- description: API calls related to the audit logs subscriptions for the currently connected user account.
  name: Mist Self Audit Logs API
  slug: mist-self-audit-logs-api
- description: API calls related to Two Factor Authentication for the currently connected user account.
  name: Mist Self MFA API
  slug: mist-self-mfa-api
- description: 'A Mist account can be linked to OAuth2 providers: 1. First, login with your Mist account 2. Obtain the Authorization URL for Linking 3. Obtain the authorization code by clicking / going through Author'
  name: Mist Self OAuth2 API
  slug: mist-self-oauth2-api
- description: The API Endpoints for the Advanced Anti Malware Profiles at the site level can be used to get the site derived profiles, meaning the org level configuration with the site variables resolved..
  name: Mist Sites Advanced Anti Malware Profiles API
  slug: mist-sites-advanced-anti-malware-profiles-api
- description: Alarms are triggered based on certain events. Alarms could be configured using an [Orgs Alarm Template]($h/Orgs%20Alarm%20Templates/_overview).
  name: Mist Sites Alarms API
  slug: mist-sites-alarms-api
- description: The Sites Anomaly API from Mist — 3 operation(s) for sites anomaly.
  name: Mist Sites Anomaly API
  slug: mist-sites-anomaly-api
- description: The API Endpoints for the Antivirus Profiles at the site level can be used to get the site derived profiles, meaning the org level configuration with the site variables resolved..
  name: Mist Sites Antivirus Profiles API
  slug: mist-sites-antivirus-profiles-api
- description: AP Templates are defining Wi-Fi and AP settings that can be assigned to Access Points based on different types of rules. Site AP Templates are created and managed at the site level and can only be ref
  name: Mist Sites AP Templates API
  slug: mist-sites-ap-templates-api
- description: A site represents a project, a deployment. For MSP, it can be as small as a coffee shop or a five-star 600-room hotel. A site contains a set of Maps, Wlans, Policies, Zones.
  name: Mist Sites API
  slug: mist-sites-api
- description: Applications contains a list of applications users are interested in monitoring / routing / policing
  name: Mist Sites Applications API
  slug: mist-sites-applications-api
- description: An Asset Filter is a feature that allows users to define specific criteria or conditions to filter and display only certain assets based on their attributes or properties. Site Asset Filters are creat
  name: Mist Sites Asset Filters API
  slug: mist-sites-asset-filters-api
- description: An Asset refers to any equipment or item that is being tracked and monitored using Bluetooth Low Energy (BLE) beacon tags. This requires the Asset Visibility subscription.
  name: Mist Sites Assets API
  slug: mist-sites-assets-api
- description: Auto Map Assignment allows devices to be automatically assigned to maps based on their location data. These API calls can be used to manage, apply, and clear auto map assignments for devices at the si
  name: Mist Sites Auto Map Assignment API
  slug: mist-sites-auto-map-assignment-api
- description: The Sites Beacons API from Mist — 2 operation(s) for sites beacons.
  name: Mist Sites Beacons API
  slug: mist-sites-beacons-api
- description: NAC Clients are devices connected to the network and authenticated by Juniper Mist Access Assurance.
  name: Mist Sites Clients - NAC API
  slug: mist-sites-clients-nac-api
- description: WAN Clients are devices connected to a Juniper SRX or SSX gateway monitor or managed by Mist
  name: Mist Sites Clients - Wan API
  slug: mist-sites-clients-wan-api
- description: Wired Clients are Wired devices connected to a Juniper switch monitored or managed by Mist.
  name: Mist Sites Clients - Wired API
  slug: mist-sites-clients-wired-api
- description: Wireless Clients are Wi-Fi devices connected to a Juniper Mist Access Point.
  name: Mist Sites Clients - Wireless API
  slug: mist-sites-clients-wireless-api
- description: The API Endpoints for the Device Profiles at the site level can be used to get the site derived networks, meaning the org level configuration with the site variables resolved..
  name: Mist Sites Device Profiles API
  slug: mist-sites-device-profiles-api
- description: Mist provides many ways (device_type specific template, site template, device profile, per-device) to configure devices for different kind of scenarios. The precedence goes from most specific to least
  name: Mist Sites Devices API
  slug: mist-sites-devices-api
- description: API Call for 3rd party devices
  name: Mist Sites Devices - Others API
  slug: mist-sites-devices-others-api
- description: API Calls specific to manage (form/delete) the SRX/SSR Clusters
  name: Mist Sites Devices - WAN Cluster API
  slug: mist-sites-devices-wan-cluster-api
- description: API Calls specific to the Juniper Switches managed by Mist
  name: Mist Sites Devices - Wired API
  slug: mist-sites-devices-wired-api
- description: API Calls specific to the Juniper Switches Virtual Chassis managed by Mist
  name: Mist Sites Devices - Wired - Virtual Chassis API
  slug: mist-sites-devices-wired-virtual-chassis-api
- description: API Calls specific to the Mist Access Points
  name: Mist Sites Devices - Wireless API
  slug: mist-sites-devices-wireless-api
- description: 'Site events are issues or incidents that affect site-assigned access points (aps) and radius, dhcp, and dns servers. They can be investigated and monitored using the insights dashboard in the juniper '
  name: Mist Sites Events API
  slug: mist-sites-events-api
- description: EVPN allows an alternative but more efficient LAN architecture utilizing VxLAN / MP-BGP - separating control plane (MAC / IP Learning) from forwarding plane. In our implementation, following the steps
  name: Mist Sites EVPN Topologies API
  slug: mist-sites-evpn-topologies-api
- description: The API Endpoints for the Gateway Templates at the site level can be used to get the site derived networks, meaning the org level configuration with the site variables resolved..
  name: Mist Sites Gateway Templates API
  slug: mist-sites-gateway-templates-api
- description: Guests are users who are accessing the wi-fi network as a temporary or non-permanent visitor.
  name: Mist Sites Guests API
  slug: mist-sites-guests-api
- description: The API Endpoints for the IDP Profiles at the site level can be used to get the site derived profiles, meaning the org level configuration with the site variables resolved..
  name: Mist Sites IDP Profiles API
  slug: mist-sites-idp-profiles-api
- description: Insights is a feature that provides an overview of network experience across the entire site, access points, or clients. It offers useful information about current conditions, such as telemetry data f
  name: Mist Sites Insights API
  slug: mist-sites-insights-api
- description: 'JSE stands for Juniper Secure Edge and it is a feature within the Mist UI that allows customers to configure Secure Cloud Connectors. With JSE, users can establish a tunnel via IPSec protocol and use '
  name: Mist Sites JSE API
  slug: mist-sites-jse-api
- description: The API Endpoints for the Licenses at the site level can be used to get license usages for a specific site.
  name: Mist Sites Licenses API
  slug: mist-sites-licenses-api
- description: The Location Diagnostics allows users to retrieve and analyze coverage and performance data for mist access points (aps) and devices.
  name: Mist Sites Location API
  slug: mist-sites-location-api
- description: Map Stacks are a way to group multiple maps together within a site, typically representing different floors or levels in a building. Map Stacks help organize and manage floorplans for multi-story buil
  name: Mist Sites Map Stacks API
  slug: mist-sites-map-stacks-api
- description: A Site Map is a visual representation of the layout and structure of a location, such as a building or campus. It includes accurate information about the placement, positions, heights, and orientation
  name: Mist Sites Maps API
  slug: mist-sites-maps-api
- description: '### AP Auto-Placement AP Auto-Placement is a feature in Juniper Mist wireless assurance that automatically determines and sets the positions of Access Points (APs) on a floorplan. It saves time and si'
  name: Mist Sites Maps - Auto-placement API
  slug: mist-sites-maps-auto-placement-api
- description: The auto zones service is a map parsing service that uses map image data to suggest spaces to designate as location zones.
  name: Mist Sites Maps - Auto-Zone API
  slug: mist-sites-maps-auto-zone-api
- description: Marvis Config Actions are config changes injected by Marvis into network devices. These actions can be searched, counted, deleted, and given feedback.
  name: Mist Sites Marvis Configs API
  slug: mist-sites-marvis-configs-api
- description: MxEdges (Mist Edges) at the site level are deployed to tunnel traffic at each site due to network constraints or security concerns. They can be assigned to a specific site and configured to provide tu
  name: Mist Sites MxEdges API
  slug: mist-sites-mxedges-api
- description: The NAC IDP allows users to integrate with various Identity Providers (IDPs) to enhance authentication and access control. Admins can configure identity providers such as microsoft EntraID, okta workf
  name: Mist Sites NAC Fingerprints API
  slug: mist-sites-nac-fingerprints-api
- description: The API Endpoints for the Network Templates at the site level can be used to get the site derived networks, meaning the org level configuration with the site variables resolved.
  name: Mist Sites Network Templates API
  slug: mist-sites-network-templates-api
- description: The API Endpoints for the Networks at the site level can be used to get the site derived networks, meaning the org level configuration with the site variables resolved.
  name: Mist Sites Networks API
  slug: mist-sites-networks-api
- description: A multi PSK (Pre-Shared Key) is a feature that allows the use of multiple PSKs for securing network connections. It provides a simple and comprehensive way to onboard client devices without relying on
  name: Mist Sites Psks API
  slug: mist-sites-psks-api
- description: The API Endpoints for the RF Templates at the site level can be used to get the site derived configuration, meaning the org level configuration with the site variables resolved..
  name: Mist Sites RF Templates API
  slug: mist-sites-rf-templates-api
- description: Rf Diags is a feature in Juniper Mist location services that allows users to replay recorded sessions of the RF (radio frequency) environment. It enables users to gain an understanding of current issu
  name: Mist Sites Rfdiags API
  slug: mist-sites-rfdiags-api
- description: 'Rogues are unauthorized wireless access points that are installed on a network without authorization. They can be connected to the LAN via an ethernet cable, similar to a pc, and are typically set up '
  name: Mist Sites Rogues API
  slug: mist-sites-rogues-api
- description: RRM, or Radio Resource Management, is a tool used by large multi-site organizations to efficiently manage their RF spectrum. It involves making decisions on channel and power settings for access point
  name: Mist Sites RRM API
  slug: mist-sites-rrm-api
- description: RSSI Zones are zones based on the RSSI (Received Signal Strength Indicator, i.e. the power of the signal received by the Access Points from the Wireless Clients).
  name: Mist Sites RSSI Zones API
  slug: mist-sites-rssi-zones-api
- description: Sky ATP Secintel Profile
  name: Mist Sites SecIntel Profiles API
  slug: mist-sites-secintel-profiles-api
- description: The API Endpoints for the Service Policies at the site level can be used to get the site derived configuration, meaning the merge between the site level configuration and the org level configuration.
  name: Mist Sites Service Policies API
  slug: mist-sites-service-policies-api
- description: A Service represents an a traffic destination or an application that network users connect to. They are associated with users and networks and are used in application policies to permit or deny access
  name: Mist Sites Services API
  slug: mist-sites-services-api
- description: Site settings refer to the configuration and management of of site within a Mist Organization. These settings include access point settings, firmware upgrade schedules, and various features such as lo
  name: Mist Sites Setting API
  slug: mist-sites-setting-api
- description: The API Endpoints for the Site Templates at the site level can be used to get the site derived configuration, meaning the org level configuration with the site variables resolved..
  name: Mist Sites Site Templates API
  slug: mist-sites-site-templates-api
- description: SkyATP is a cloud-based solution that provides advanced threat protection for network security. It allows security analysts to update their defense against new attack techniques in real-time and distr
  name: Mist Sites Skyatp API
  slug: mist-sites-skyatp-api
- description: Site SLEs, or Service-Level Expectations, are metrics used to monitor and report on the user experience of a Wireless, Wired or Wan network. They are generated through data science and machine learnin
  name: Mist Sites SLEs API
  slug: mist-sites-sles-api
- description: The Spectrum Analysis feature provides insights into the radio frequency environment, helping to identify interference and optimize wireless network performance. It allows users to monitor and analyze
  name: Mist Sites Spectrum Analysis API
  slug: mist-sites-spectrum-analysis-api
- description: The stats are providing access to raw data about a specific type of entities.
  name: Mist Sites Stats API
  slug: mist-sites-stats-api
- description: API Calls to retrieve the stats of the Applications used on side
  name: Mist Sites Stats - Apps API
  slug: mist-sites-stats-apps-api
- description: The Sites Stats - Assets API from Mist — 7 operation(s) for sites stats - assets.
  name: Mist Sites Stats - Assets API
  slug: mist-sites-stats-assets-api
- description: The Sites Stats - Beacons API from Mist — 1 operation(s) for sites stats - beacons.
  name: Mist Sites Stats - Beacons API
  slug: mist-sites-stats-beacons-api
- description: API Calls to retrieve BGP Peers statistics of the Site Wen Edge Gateways at the Site level
  name: Mist Sites Stats - BGP Peers API
  slug: mist-sites-stats-bgp-peers-api
- description: API Calls to retrieve the stats of the calls (Zoom/Teams) detected by Mist
  name: Mist Sites Stats - Calls API
  slug: mist-sites-stats-calls-api
- description: SDK Clients are devices that have installed an application using the Mist Software Development Kit (SDK). These clients can provide specific data and information that is not available without the inst
  name: Mist Sites Stats - Clients SDK API
  slug: mist-sites-stats-clients-sdk-api
- description: API Calls to retrieve the stats of the wireless clients detected (connected or not connected) on this site.
  name: Mist Sites Stats - Clients Wireless API
  slug: mist-sites-stats-clients-wireless-api
- description: API Calls to retrieve statistics about the Mist Managed and Monitored Devices at the Site level
  name: Mist Sites Stats - Devices API
  slug: mist-sites-stats-devices-api
- description: API Calls to retrieve statistics about the Discovered Switches at the Site level
  name: Mist Sites Stats - Discovered Switches API
  slug: mist-sites-stats-discovered-switches-api
- description: API Calls to retrieve IoT Endpoint statistics for the current Site
  name: Mist Sites Stats - IoT Endpoints API
  slug: mist-sites-stats-iot-endpoints-api
- description: API Calls to retrieve statistics about the Mist Edges at the Site level
  name: Mist Sites Stats - MxEdges API
  slug: mist-sites-stats-mxedges-api
- description: API Calls to retrieve statistics about OSPF peers at the Site level
  name: Mist Sites Stats - Ospf API
  slug: mist-sites-stats-ospf-api
- description: API Calls to retrieve statistics about the Wired Ports at the Site level
  name: Mist Sites Stats - Ports API
  slug: mist-sites-stats-ports-api
- description: API Calls to retrieve WxRules statistics for the current Site
  name: Mist Sites Stats - WxRules API
  slug: mist-sites-stats-wxrules-api
- description: API Calls to retrieve Zones statistics for the current Site
  name: Mist Sites Stats - Zones API
  slug: mist-sites-stats-zones-api
- description: Synthetic Tests (Marvis Minis) are a feature of Juniper Networks' Mist platform, designed to proactively identify and resolve network issues before they impact users by simulating user connections and
  name: Mist Sites Synthetic Tests API
  slug: mist-sites-synthetic-tests-api
- description: The Site UI Settings are used to configure the site Network and Analytics reports
  name: Mist Sites UI Settings API
  slug: mist-sites-ui-settings-api
- description: A vBeacon is a virtual beacon that is created and configured on a floorplan and are configured with a name and message It is a Mist patented technology that provides proximity-related notifications to
  name: Mist Sites vBeacons API
  slug: mist-sites-vbeacons-api
- description: API Calls to retrieve the list of Org VPNs configuration available for the Site
  name: Mist Sites VPNs API
  slug: mist-sites-vpns-api
- description: API Calls to retrieve WAN Assurance statistics about the WAN Usage
  name: Mist Sites WAN Usages API
  slug: mist-sites-wan-usages-api
- description: A Site Webhook is a configuration that allows real-time events and data from a specific site to be pushed to a provided url. It enables the collection of information about various topics such as devic
  name: Mist Sites Webhooks API
  slug: mist-sites-webhooks-api
- description: A Site Wlan is a wireless local area network that is configured and applied to a specific site within an organization. It allows for the creation and management of wireless network settings, such as S
  name: Mist Sites Wlans API
  slug: mist-sites-wlans-api
- description: Site WxRules are a set of rules, restrictions, and settings that can be applied to WLANs within a specific site. These policies determine how the devices and traffic are treated by the network and can
  name: Mist Sites WxRules API
  slug: mist-sites-wxrules-api
- description: 'Wxtags are tags or groups that can be created and used within a specific site. They are used to classify users and resources and can be applied to Access Points, WLAN configurations or WxRules within '
  name: Mist Sites WxTags API
  slug: mist-sites-wxtags-api
- description: A WxLan Tunnel (WxTunnel) are used to create a secure connection between Juniper Mist Access Points and third-party VPN concentrators using protocols such as L2TPv3 or dmvpn. These tunnels allow for t
  name: Mist Sites WxTunnels API
  slug: mist-sites-wxtunnels-api
- description: A Zone is a custom area defined by a user on a floor plan. Zones can be used for capturing entry and exit events of clients, assets, and sdk clients, providing insights such as wait time and the numbe
  name: Mist Sites Zones API
  slug: mist-sites-zones-api
- description: API Calls to use Devices Troubleshooting tools. Some API Calls can be used with any type of devices (Access Points, Switches and Gateways), and some others may be limited to some types of devices (e.g
  name: Mist Utilities Common API
  slug: mist-utilities-common-api
- description: API Calls to use Devices Troubleshooting tools specific to Wired Assurance
  name: Mist Utilities LAN API
  slug: mist-utilities-lan-api
- description: API Calls to use Devices Troubleshooting tools specific to Asset Tracking and User Management
  name: Mist Utilities Location API
  slug: mist-utilities-location-api
- description: API Calls to use Devices Troubleshooting tools specific to Mx Edges
  name: Mist Utilities MxEdge API
  slug: mist-utilities-mxedge-api
- description: API Calls to start, stop or managed Packet Captures at the device level
  name: Mist Utilities PCAPs API
  slug: mist-utilities-pcaps-api
- description: API Calls used to manage device upgrades for a single device, at the site level or at the organization level.
  name: Mist Utilities Upgrade API
  slug: mist-utilities-upgrade-api
- description: API Calls to use Devices Troubleshooting tools specific to WAN Assurance
  name: Mist Utilities WAN API
  slug: mist-utilities-wan-api
- description: API Calls to use Devices Troubleshooting tools specific to Wireless Assurance
  name: Mist Utilities Wi-Fi API
  slug: mist-utilities-wi-fi-api
- description: The Mist API API from Mist — 0 operation(s) for mist api.
  name: Mist Mist API
  slug: mist-mist-api-api
artifact_total: 430
asyncapis:
- description: ''
  name: Mist Webhooks
  slug: mist-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mist Admins API
  slug: open-mist-admins-api
- collection_type: open
  name: Mist Admins Admins Login API
  slug: open-mist-admins-login-api
- collection_type: open
  name: Mist Admins Admins Login - OAuth2 API
  slug: open-mist-admins-login-oauth2-api
- collection_type: open
  name: Mist Admins Admins Logout API
  slug: open-mist-admins-logout-api
- collection_type: open
  name: Mist Admins Admins Lookup API
  slug: open-mist-admins-lookup-api
- collection_type: open
  name: Mist Admins Admins Recover Password API
  slug: open-mist-admins-recover-password-api
- collection_type: open
  name: Mist Admins Constants Definitions API
  slug: open-mist-constants-definitions-api
- collection_type: open
  name: Mist Admins Constants Events API
  slug: open-mist-constants-events-api
- collection_type: open
  name: Mist Admins Constants Models API
  slug: open-mist-constants-models-api
- collection_type: open
  name: Mist Admins Installer API
  slug: open-mist-installer-api
- collection_type: open
  name: Mist Admins MSPs Admins API
  slug: open-mist-msps-admins-api
- collection_type: open
  name: Mist Admins MSPs API
  slug: open-mist-msps-api
- collection_type: open
  name: Mist Admins MSPs Inventory API
  slug: open-mist-msps-inventory-api
- collection_type: open
  name: Mist Admins MSPs Licenses API
  slug: open-mist-msps-licenses-api
- collection_type: open
  name: Mist Admins MSPs Logo API
  slug: open-mist-msps-logo-api
- collection_type: open
  name: Mist Admins MSPs Logs API
  slug: open-mist-msps-logs-api
- collection_type: open
  name: Mist Admins MSPs Marvis API
  slug: open-mist-msps-marvis-api
- collection_type: open
  name: Mist Admins MSPs Org Groups API
  slug: open-mist-msps-org-groups-api
- collection_type: open
  name: Mist Admins MSPs Orgs API
  slug: open-mist-msps-orgs-api
- collection_type: open
  name: Mist Admins MSPs SLEs API
  slug: open-mist-msps-sles-api
- collection_type: open
  name: Mist Admins MSPs SSO API
  slug: open-mist-msps-sso-api
- collection_type: open
  name: Mist Admins MSPs SSO Roles API
  slug: open-mist-msps-sso-roles-api
- collection_type: open
  name: Mist Admins MSPs Tickets API
  slug: open-mist-msps-tickets-api
- collection_type: open
  name: Mist Admins Orgs Admins API
  slug: open-mist-orgs-admins-api
- collection_type: open
  name: Mist Admins Orgs Advanced Anti Malware Profiles API
  slug: open-mist-orgs-advanced-anti-malware-profiles-api
- collection_type: open
  name: Mist Admins Orgs Alarm Templates API
  slug: open-mist-orgs-alarm-templates-api
- collection_type: open
  name: Mist Admins Orgs Alarms API
  slug: open-mist-orgs-alarms-api
- collection_type: open
  name: Mist Admins Orgs Antivirus Profiles API
  slug: open-mist-orgs-antivirus-profiles-api
- collection_type: open
  name: Mist Admins Orgs AP Templates API
  slug: open-mist-orgs-ap-templates-api
- collection_type: open
  name: Mist Admins Orgs API Tokens API
  slug: open-mist-orgs-api-tokens-api
- collection_type: open
  name: Mist Admins Orgs API
  slug: open-mist-orgs-api
- collection_type: open
  name: Mist Admins Orgs Asset Filters API
  slug: open-mist-orgs-asset-filters-api
- collection_type: open
  name: Mist Admins Orgs Assets API
  slug: open-mist-orgs-assets-api
- collection_type: open
  name: Mist Admins Orgs Cert API
  slug: open-mist-orgs-cert-api
- collection_type: open
  name: Mist Admins Orgs Clients - Marvis API
  slug: open-mist-orgs-clients-marvis-api
- collection_type: open
  name: Mist Admins Orgs Clients - NAC API
  slug: open-mist-orgs-clients-nac-api
- collection_type: open
  name: Mist Admins Orgs Clients - SDK API
  slug: open-mist-orgs-clients-sdk-api
- collection_type: open
  name: Mist Admins Orgs Clients - Wan API
  slug: open-mist-orgs-clients-wan-api
- collection_type: open
  name: Mist Admins Orgs Clients - Wired API
  slug: open-mist-orgs-clients-wired-api
- collection_type: open
  name: Mist Admins Orgs Clients - Wireless API
  slug: open-mist-orgs-clients-wireless-api
- collection_type: open
  name: Mist Admins Orgs CRL API
  slug: open-mist-orgs-crl-api
- collection_type: open
  name: Mist Admins Orgs Device Profiles API
  slug: open-mist-orgs-device-profiles-api
- collection_type: open
  name: Mist Admins Orgs Devices - AOS API
  slug: open-mist-orgs-devices-aos-api
- collection_type: open
  name: Mist Admins Orgs Devices API
  slug: open-mist-orgs-devices-api
- collection_type: open
  name: Mist Admins Orgs Devices - Others API
  slug: open-mist-orgs-devices-others-api
- collection_type: open
  name: Mist Admins Orgs Devices - SSR API
  slug: open-mist-orgs-devices-ssr-api
- collection_type: open
  name: Mist Admins Orgs Events API
  slug: open-mist-orgs-events-api
- collection_type: open
  name: Mist Admins Orgs EVPN Topologies API
  slug: open-mist-orgs-evpn-topologies-api
- collection_type: open
  name: Mist Admins Orgs Gateway Templates API
  slug: open-mist-orgs-gateway-templates-api
- collection_type: open
  name: Mist Admins Orgs Guests API
  slug: open-mist-orgs-guests-api
- collection_type: open
  name: Mist Admins Orgs IDP Profiles API
  slug: open-mist-orgs-idp-profiles-api
- collection_type: open
  name: Mist Admins Orgs Integration Cradlepoint API
  slug: open-mist-orgs-integration-cradlepoint-api
- collection_type: open
  name: Mist Admins Orgs Integration JSE API
  slug: open-mist-orgs-integration-jse-api
- collection_type: open
  name: Mist Admins Orgs Integration Juniper API
  slug: open-mist-orgs-integration-juniper-api
- collection_type: open
  name: Mist Admins Orgs Integration SkyATP API
  slug: open-mist-orgs-integration-skyatp-api
- collection_type: open
  name: Mist Admins Orgs Integration Zscaler API
  slug: open-mist-orgs-integration-zscaler-api
- collection_type: open
  name: Mist Admins Orgs Inventory API
  slug: open-mist-orgs-inventory-api
- collection_type: open
  name: Mist Admins Orgs JSI API
  slug: open-mist-orgs-jsi-api
- collection_type: open
  name: Mist Admins Orgs Licenses API
  slug: open-mist-orgs-licenses-api
- collection_type: open
  name: Mist Admins Orgs Linked Applications API
  slug: open-mist-orgs-linked-applications-api
- collection_type: open
  name: Mist Admins Orgs Logs API
  slug: open-mist-orgs-logs-api
- collection_type: open
  name: Mist Admins Orgs Maps API
  slug: open-mist-orgs-maps-api
- collection_type: open
  name: Mist Admins Orgs Marvis API
  slug: open-mist-orgs-marvis-api
- collection_type: open
  name: Mist Admins Orgs Marvis Invites API
  slug: open-mist-orgs-marvis-invites-api
- collection_type: open
  name: Mist Admins Orgs MxClusters API
  slug: open-mist-orgs-mxclusters-api
- collection_type: open
  name: Mist Admins Orgs MxEdges API
  slug: open-mist-orgs-mxedges-api
- collection_type: open
  name: Mist Admins Orgs MxTunnels API
  slug: open-mist-orgs-mxtunnels-api
- collection_type: open
  name: Mist Admins Orgs NAC CRL API
  slug: open-mist-orgs-nac-crl-api
- collection_type: open
  name: Mist Admins Orgs NAC IDP API
  slug: open-mist-orgs-nac-idp-api
- collection_type: open
  name: Mist Admins Orgs NAC Portals API
  slug: open-mist-orgs-nac-portals-api
- collection_type: open
  name: Mist Admins Orgs NAC Rules API
  slug: open-mist-orgs-nac-rules-api
- collection_type: open
  name: Mist Admins Orgs NAC Tags API
  slug: open-mist-orgs-nac-tags-api
- collection_type: open
  name: Mist Admins Orgs Network Templates API
  slug: open-mist-orgs-network-templates-api
- collection_type: open
  name: Mist Admins Orgs Networks API
  slug: open-mist-orgs-networks-api
- collection_type: open
  name: Mist Admins Orgs Premium Analytics API
  slug: open-mist-orgs-premium-analytics-api
- collection_type: open
  name: Mist Admins Orgs Psk Portals API
  slug: open-mist-orgs-psk-portals-api
- collection_type: open
  name: Mist Admins Orgs Psks API
  slug: open-mist-orgs-psks-api
- collection_type: open
  name: Mist Admins Orgs Reports API
  slug: open-mist-orgs-reports-api
- collection_type: open
  name: Mist Admins Orgs RF Templates API
  slug: open-mist-orgs-rf-templates-api
- collection_type: open
  name: Mist Admins Orgs SCEP API
  slug: open-mist-orgs-scep-api
- collection_type: open
  name: Mist Admins Orgs SDK Invites API
  slug: open-mist-orgs-sdk-invites-api
- collection_type: open
  name: Mist Admins Orgs SDK Templates API
  slug: open-mist-orgs-sdk-templates-api
- collection_type: open
  name: Mist Admins Orgs SecIntel Profiles API
  slug: open-mist-orgs-secintel-profiles-api
- collection_type: open
  name: Mist Admins Orgs Security Policies API
  slug: open-mist-orgs-security-policies-api
- collection_type: open
  name: Mist Admins Orgs Service Policies API
  slug: open-mist-orgs-service-policies-api
- collection_type: open
  name: Mist Admins Orgs Services API
  slug: open-mist-orgs-services-api
- collection_type: open
  name: Mist Admins Orgs Setting API
  slug: open-mist-orgs-setting-api
- collection_type: open
  name: Mist Admins Orgs Site Templates API
  slug: open-mist-orgs-site-templates-api
- collection_type: open
  name: Mist Admins Orgs Sitegroups API
  slug: open-mist-orgs-sitegroups-api
- collection_type: open
  name: Mist Admins Orgs Sites API
  slug: open-mist-orgs-sites-api
- collection_type: open
  name: Mist Admins Orgs SLEs API
  slug: open-mist-orgs-sles-api
- collection_type: open
  name: Mist Admins Orgs SSO API
  slug: open-mist-orgs-sso-api
- collection_type: open
  name: Mist Admins Orgs SSO Roles API
  slug: open-mist-orgs-sso-roles-api
- collection_type: open
  name: Mist Admins Orgs Stats API
  slug: open-mist-orgs-stats-api
- collection_type: open
  name: Mist Admins Orgs Stats - Assets API
  slug: open-mist-orgs-stats-assets-api
- collection_type: open
  name: Mist Admins Orgs Stats - BGP Peers API
  slug: open-mist-orgs-stats-bgp-peers-api
- collection_type: open
  name: Mist Admins Orgs Stats - Devices API
  slug: open-mist-orgs-stats-devices-api
- collection_type: open
  name: Mist Admins Orgs Stats - Marvis Clients API
  slug: open-mist-orgs-stats-marvis-clients-api
- collection_type: open
  name: Mist Admins Orgs Stats - MxEdges API
  slug: open-mist-orgs-stats-mxedges-api
- collection_type: open
  name: Mist Admins Orgs Stats - Ospf API
  slug: open-mist-orgs-stats-ospf-api
- collection_type: open
  name: Mist Admins Orgs Stats - Other Devices API
  slug: open-mist-orgs-stats-other-devices-api
- collection_type: open
  name: Mist Admins Orgs Stats - Ports API
  slug: open-mist-orgs-stats-ports-api
- collection_type: open
  name: Mist Admins Orgs Stats - Sites API
  slug: open-mist-orgs-stats-sites-api
- collection_type: open
  name: Mist Admins Orgs Stats - Tunnels API
  slug: open-mist-orgs-stats-tunnels-api
- collection_type: open
  name: Mist Admins Orgs Stats - VPN Peers API
  slug: open-mist-orgs-stats-vpn-peers-api
- collection_type: open
  name: Mist Admins Orgs Tickets API
  slug: open-mist-orgs-tickets-api
- collection_type: open
  name: Mist Admins Orgs UI Settings API
  slug: open-mist-orgs-ui-settings-api
- collection_type: open
  name: Mist Admins Orgs User MACs API
  slug: open-mist-orgs-user-macs-api
- collection_type: open
  name: Mist Admins Orgs Vars API
  slug: open-mist-orgs-vars-api
- collection_type: open
  name: Mist Admins Orgs VPNs API
  slug: open-mist-orgs-vpns-api
- collection_type: open
  name: Mist Admins Orgs Webhooks API
  slug: open-mist-orgs-webhooks-api
- collection_type: open
  name: Mist Admins Orgs WLAN Templates API
  slug: open-mist-orgs-wlan-templates-api
- collection_type: open
  name: Mist Admins Orgs Wlans API
  slug: open-mist-orgs-wlans-api
- collection_type: open
  name: Mist Admins Orgs WxRules API
  slug: open-mist-orgs-wxrules-api
- collection_type: open
  name: Mist Admins Orgs WxTags API
  slug: open-mist-orgs-wxtags-api
- collection_type: open
  name: Mist Admins Orgs WxTunnels API
  slug: open-mist-orgs-wxtunnels-api
- collection_type: open
  name: Mist Admins Self Account API
  slug: open-mist-self-account-api
- collection_type: open
  name: Mist Admins Self Alarms API
  slug: open-mist-self-alarms-api
- collection_type: open
  name: Mist Admins Self API Token API
  slug: open-mist-self-api-token-api
- collection_type: open
  name: Mist Admins Self Audit Logs API
  slug: open-mist-self-audit-logs-api
- collection_type: open
  name: Mist Admins Self MFA API
  slug: open-mist-self-mfa-api
- collection_type: open
  name: Mist Admins Self OAuth2 API
  slug: open-mist-self-oauth2-api
- collection_type: open
  name: Mist Admins Sites Advanced Anti Malware Profiles API
  slug: open-mist-sites-advanced-anti-malware-profiles-api
- collection_type: open
  name: Mist Admins Sites Alarms API
  slug: open-mist-sites-alarms-api
- collection_type: open
  name: Mist Admins Sites Anomaly API
  slug: open-mist-sites-anomaly-api
- collection_type: open
  name: Mist Admins Sites Antivirus Profiles API
  slug: open-mist-sites-antivirus-profiles-api
- collection_type: open
  name: Mist Admins Sites AP Templates API
  slug: open-mist-sites-ap-templates-api
- collection_type: open
  name: Mist Admins Sites API
  slug: open-mist-sites-api
- collection_type: open
  name: Mist Admins Sites Applications API
  slug: open-mist-sites-applications-api
- collection_type: open
  name: Mist Admins Sites Asset Filters API
  slug: open-mist-sites-asset-filters-api
- collection_type: open
  name: Mist Admins Sites Assets API
  slug: open-mist-sites-assets-api
- collection_type: open
  name: Mist Admins Sites Auto Map Assignment API
  slug: open-mist-sites-auto-map-assignment-api
- collection_type: open
  name: Mist Admins Sites Beacons API
  slug: open-mist-sites-beacons-api
- collection_type: open
  name: Mist Admins Sites Clients - NAC API
  slug: open-mist-sites-clients-nac-api
- collection_type: open
  name: Mist Admins Sites Clients - Wan API
  slug: open-mist-sites-clients-wan-api
- collection_type: open
  name: Mist Admins Sites Clients - Wired API
  slug: open-mist-sites-clients-wired-api
- collection_type: open
  name: Mist Admins Sites Clients - Wireless API
  slug: open-mist-sites-clients-wireless-api
- collection_type: open
  name: Mist Admins Sites Device Profiles API
  slug: open-mist-sites-device-profiles-api
- collection_type: open
  name: Mist Admins Sites Devices API
  slug: open-mist-sites-devices-api
- collection_type: open
  name: Mist Admins Sites Devices - Others API
  slug: open-mist-sites-devices-others-api
- collection_type: open
  name: Mist Admins Sites Devices - WAN Cluster API
  slug: open-mist-sites-devices-wan-cluster-api
- collection_type: open
  name: Mist Admins Sites Devices - Wired API
  slug: open-mist-sites-devices-wired-api
- collection_type: open
  name: Mist Admins Sites Devices - Wired - Virtual Chassis API
  slug: open-mist-sites-devices-wired-virtual-chassis-api
- collection_type: open
  name: Mist Admins Sites Devices - Wireless API
  slug: open-mist-sites-devices-wireless-api
- collection_type: open
  name: Mist Admins Sites Events API
  slug: open-mist-sites-events-api
- collection_type: open
  name: Mist Admins Sites EVPN Topologies API
  slug: open-mist-sites-evpn-topologies-api
- collection_type: open
  name: Mist Admins Sites Gateway Templates API
  slug: open-mist-sites-gateway-templates-api
- collection_type: open
  name: Mist Admins Sites Guests API
  slug: open-mist-sites-guests-api
- collection_type: open
  name: Mist Admins Sites IDP Profiles API
  slug: open-mist-sites-idp-profiles-api
- collection_type: open
  name: Mist Admins Sites Insights API
  slug: open-mist-sites-insights-api
- collection_type: open
  name: Mist Admins Sites JSE API
  slug: open-mist-sites-jse-api
- collection_type: open
  name: Mist Admins Sites Licenses API
  slug: open-mist-sites-licenses-api
- collection_type: open
  name: Mist Admins Sites Location API
  slug: open-mist-sites-location-api
- collection_type: open
  name: Mist Admins Sites Map Stacks API
  slug: open-mist-sites-map-stacks-api
- collection_type: open
  name: Mist Admins Sites Maps API
  slug: open-mist-sites-maps-api
- collection_type: open
  name: Mist Admins Sites Maps - Auto-placement API
  slug: open-mist-sites-maps-auto-placement-api
- collection_type: open
  name: Mist Admins Sites Maps - Auto-Zone API
  slug: open-mist-sites-maps-auto-zone-api
- collection_type: open
  name: Mist Admins Sites Marvis Configs API
  slug: open-mist-sites-marvis-configs-api
- collection_type: open
  name: Mist Admins Sites MxEdges API
  slug: open-mist-sites-mxedges-api
- collection_type: open
  name: Mist Admins Sites NAC Fingerprints API
  slug: open-mist-sites-nac-fingerprints-api
- collection_type: open
  name: Mist Admins Sites Network Templates API
  slug: open-mist-sites-network-templates-api
- collection_type: open
  name: Mist Admins Sites Networks API
  slug: open-mist-sites-networks-api
- collection_type: open
  name: Mist Admins Sites Psks API
  slug: open-mist-sites-psks-api
- collection_type: open
  name: Mist Admins Sites RF Templates API
  slug: open-mist-sites-rf-templates-api
- collection_type: open
  name: Mist Admins Sites Rfdiags API
  slug: open-mist-sites-rfdiags-api
- collection_type: open
  name: Mist Admins Sites Rogues API
  slug: open-mist-sites-rogues-api
- collection_type: open
  name: Mist Admins Sites RRM API
  slug: open-mist-sites-rrm-api
- collection_type: open
  name: Mist Admins Sites RSSI Zones API
  slug: open-mist-sites-rssi-zones-api
- collection_type: open
  name: Mist Admins Sites SecIntel Profiles API
  slug: open-mist-sites-secintel-profiles-api
- collection_type: open
  name: Mist Admins Sites Service Policies API
  slug: open-mist-sites-service-policies-api
- collection_type: open
  name: Mist Admins Sites Services API
  slug: open-mist-sites-services-api
- collection_type: open
  name: Mist Admins Sites Setting API
  slug: open-mist-sites-setting-api
- collection_type: open
  name: Mist Admins Sites Site Templates API
  slug: open-mist-sites-site-templates-api
- collection_type: open
  name: Mist Admins Sites Skyatp API
  slug: open-mist-sites-skyatp-api
- collection_type: open
  name: Mist Admins Sites SLEs API
  slug: open-mist-sites-sles-api
- collection_type: open
  name: Mist Admins Sites Spectrum Analysis API
  slug: open-mist-sites-spectrum-analysis-api
- collection_type: open
  name: Mist Admins Sites Stats API
  slug: open-mist-sites-stats-api
- collection_type: open
  name: Mist Admins Sites Stats - Apps API
  slug: open-mist-sites-stats-apps-api
- collection_type: open
  name: Mist Admins Sites Stats - Assets API
  slug: open-mist-sites-stats-assets-api
- collection_type: open
  name: Mist Admins Sites Stats - Beacons API
  slug: open-mist-sites-stats-beacons-api
- collection_type: open
  name: Mist Admins Sites Stats - BGP Peers API
  slug: open-mist-sites-stats-bgp-peers-api
- collection_type: open
  name: Mist Admins Sites Stats - Calls API
  slug: open-mist-sites-stats-calls-api
- collection_type: open
  name: Mist Admins Sites Stats - Clients SDK API
  slug: open-mist-sites-stats-clients-sdk-api
- collection_type: open
  name: Mist Admins Sites Stats - Clients Wireless API
  slug: open-mist-sites-stats-clients-wireless-api
- collection_type: open
  name: Mist Admins Sites Stats - Devices API
  slug: open-mist-sites-stats-devices-api
- collection_type: open
  name: Mist Admins Sites Stats - Discovered Switches API
  slug: open-mist-sites-stats-discovered-switches-api
- collection_type: open
  name: Mist Admins Sites Stats - IoT Endpoints API
  slug: open-mist-sites-stats-iot-endpoints-api
- collection_type: open
  name: Mist Admins Sites Stats - MxEdges API
  slug: open-mist-sites-stats-mxedges-api
- collection_type: open
  name: Mist Admins Sites Stats - Ospf API
  slug: open-mist-sites-stats-ospf-api
- collection_type: open
  name: Mist Admins Sites Stats - Ports API
  slug: open-mist-sites-stats-ports-api
- collection_type: open
  name: Mist Admins Sites Stats - WxRules API
  slug: open-mist-sites-stats-wxrules-api
- collection_type: open
  name: Mist Admins Sites Stats - Zones API
  slug: open-mist-sites-stats-zones-api
- collection_type: open
  name: Mist Admins Sites Synthetic Tests API
  slug: open-mist-sites-synthetic-tests-api
- collection_type: open
  name: Mist Admins Sites UI Settings API
  slug: open-mist-sites-ui-settings-api
- collection_type: open
  name: Mist Admins Sites vBeacons API
  slug: open-mist-sites-vbeacons-api
- collection_type: open
  name: Mist Admins Sites VPNs API
  slug: open-mist-sites-vpns-api
- collection_type: open
  name: Mist Admins Sites WAN Usages API
  slug: open-mist-sites-wan-usages-api
- collection_type: open
  name: Mist Admins Sites Webhooks API
  slug: open-mist-sites-webhooks-api
- collection_type: open
  name: Mist Admins Sites Wlans API
  slug: open-mist-sites-wlans-api
- collection_type: open
  name: Mist Admins Sites WxRules API
  slug: open-mist-sites-wxrules-api
- collection_type: open
  name: Mist Admins Sites WxTags API
  slug: open-mist-sites-wxtags-api
- collection_type: open
  name: Mist Admins Sites WxTunnels API
  slug: open-mist-sites-wxtunnels-api
- collection_type: open
  name: Mist Admins Sites Zones API
  slug: open-mist-sites-zones-api
- collection_type: open
  name: Mist Admins Utilities Common API
  slug: open-mist-utilities-common-api
- collection_type: open
  name: Mist Admins Utilities LAN API
  slug: open-mist-utilities-lan-api
- collection_type: open
  name: Mist Admins Utilities Location API
  slug: open-mist-utilities-location-api
- collection_type: open
  name: Mist Admins Utilities MxEdge API
  slug: open-mist-utilities-mxedge-api
- collection_type: open
  name: Mist Admins Utilities PCAPs API
  slug: open-mist-utilities-pcaps-api
- collection_type: open
  name: Mist Admins Utilities Upgrade API
  slug: open-mist-utilities-upgrade-api
- collection_type: open
  name: Mist Admins Utilities WAN API
  slug: open-mist-utilities-wan-api
- collection_type: open
  name: Mist Admins Utilities Wi-Fi API
  slug: open-mist-utilities-wi-fi-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/juniper-networks/
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/mist-capability-edges.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.juniper.net/documentation/us/en/software/mist/automation-integration/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mist.com/documentation/category/api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.juniper.net/documentation/us/en/software/mist/api/http/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mist.com/documentation/category/getting-started-api/
- group: operate
  title: ''
  type: Support
  url: https://support.mist.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mistsys
- group: start
  title: ''
  type: Login
  url: https://manage.mist.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.juniper.net/us/en/privacy-policy.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/juniper-mist/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mist.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://www.juniper.net/documentation/us/en/software/mist/automation-integration/topics/task/create-token-for-rest-api.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/mist-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/mist-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/mist-openapi-overlay.yaml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mist-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mist-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mist-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mist-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mist-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mist-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mist-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/mist-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mist-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mist-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mist-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mist-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mist-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mist-domain-security.yml
created: '2026-07-17'
description: Mist (Mist Systems), acquired by Juniper Networks and now Juniper Mist, is an AI-driven cloud platform for wireless, wired, and WAN networking. The Juniper Mist Cloud API is a RESTful HTTPS/JSON API organized around an Org -> Site -> Device hierarchy, giving programmatic access to configuration, inventory, client analytics (SLE), the Marvis virtual network assistant, location services, and real-time event webhooks. Mist was an early Lightspeed Venture Partners portfolio company (seed, 2014) before its Juniper acquisition.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mist.png
layout: provider
mcp_servers:
- description: ''
  name: Mist MCP Server
  slug: mist-mcp-server
modified: '2026-07-20'
name: Mist
nav: Providers
network: true
overview: 'Mist publishes 212 APIs on the [APIs.io](https://apis.io/) network, including Admins API, Admins Login API, Admins Login - OAuth2 API, and 209 more. Tagged areas include Company, Networking, Wireless, Wi-Fi, and Cloud Management.


  The Mist catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mist''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, and 25 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 2
  name: Mist Rate Limits
  slug: mist-rate-limits
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 70.1
    developer_ergonomics: 58.9
    discoverability: 51.9
    governance: 4.5
    operational_transparency: 71.1
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 211
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mist/refs/heads/main/screenshots/mist-2026-08-07T183800.png
security:
- kind: authentication
  name: Mist Authentication
  slug: mist-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Mist Domain Security
  slug: mist-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mist
tags:
- Company
- Networking
- Wireless
- Wi-Fi
- Cloud Management
- Artificial Intelligence
- Network Automation
- Location Services
- Webhook
- Juniper
website: https://www.juniper.net/documentation/us/en/software/mist/automation-integration/
---
