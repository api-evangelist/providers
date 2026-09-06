---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 364
  human_in_the_loop: 21
  name: Extreme Networks Agentic Access
  operation_count: 628
  slug: extreme-networks-agentic-access
  summary_line: 628 operations · 364 acting · 21 human-in-the-loop
api_count: 1
apis:
- description: On-premises REST API gateway exposed by the ExtremeCloud IQ Controller (the wired and wireless campus controller). Provides programmatic access to controller configuration, sites, RF management, AP an
  name: ExtremeCloud IQ Controller REST API Gateway
  slug: extremecloud-iq-controller-rest-api
- description: 'Application Manager REST API for the ExtremeCloud IQ Controller, enabling visibility into Layer 7 application traffic, per-application policy, and per-application reporting on locally managed Extreme '
  name: ExtremeCloud IQ Controller Application Manager API
  slug: extremecloud-iq-controller-application-manager-api
- description: Ansible collection providing modules and roles to automate configuration and operations of Extreme Networks EXOS switches (e.g. ExtremeSwitching X-Series, Summit). Supports declarative network configu
  name: Ansible Network Collection for Extreme EXOS
  slug: ansible-extreme-exos
- description: Ansible collection for Extreme Networks VOSS (VSP Operating System) switches, including Fabric Engine devices. Provides modules for declarative configuration of VOSS-based platforms.
  name: Ansible Network Collection for Extreme VOSS
  slug: ansible-extreme-voss
- description: Ansible collection for Extreme Networks SLX-OS data center switches. Provides modules for declarative configuration and operational tasks on SLX platforms.
  name: Ansible Network Collection for Extreme SLX-OS
  slug: ansible-extreme-slxos
- description: Ansible collection for Extreme Networks NOS (Network Operating System) switches, supporting declarative configuration and automation workflows.
  name: Ansible Network Collection for Extreme NOS
  slug: ansible-extreme-nos
- description: Ansible collection for Extreme Fabric Engine, used to automate Shortest Path Bridging (SPB) fabric configuration across Extreme VSP and ERS platforms.
  name: Ansible Network Collection for Extreme Fabric Engine
  slug: ansible-extreme-fabric-engine
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: ExtremeCloud IQ Account
  name: Extreme Networks Account API
  slug: extreme-networks-account-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: API Token Management and 3rd Party API Connections
  name: Extreme Networks Administration API
  slug: extreme-networks-administration-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: ExtremeCloud IQ AFC Feature.
  name: Extreme Networks AFC API
  slug: extreme-networks-afc-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: ExtremeCloud IQ generated alerts and events
  name: Extreme Networks Alert API
  slug: extreme-networks-alert-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Application management and application metrics
  name: Extreme Networks Application API
  slug: extreme-networks-application-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: User login & logout
  name: Extreme Networks Authentication API
  slug: extreme-networks-authentication-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: API token and permissions
  name: Extreme Networks Authorization API
  slug: extreme-networks-authorization-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: The clients associate to the devices of ExtremeCloud IQ
  name: Extreme Networks Client API
  slug: extreme-networks-client-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: The details of client associate to the devices of ExtremeCloud IQ
  name: Extreme Networks Client - Details API
  slug: extreme-networks-client-details-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: AD/LDAP/RADIUS/RADSEC/CWP/...
  name: Extreme Networks Configuration - Authentication API
  slug: extreme-networks-configuration-authentication-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: VLAN Profile/DHCP Server/...
  name: Extreme Networks Configuration - Basic API
  slug: extreme-networks-configuration-basic-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Certificate
  name: Extreme Networks Configuration - Certificate API
  slug: extreme-networks-configuration-certificate-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Push configuration to devices
  name: Extreme Networks Configuration - Deployment API
  slug: extreme-networks-configuration-deployment-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Tunnel Concentrator Service, Network service
  name: Extreme Networks Configuration - Network API
  slug: extreme-networks-configuration-network-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: SSID/User Profile/Classification Rule/CCG/Radio Profile/...
  name: Extreme Networks Configuration - Policy API
  slug: extreme-networks-configuration-policy-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: User Group/End User/PCG/PPSK Classification
  name: Extreme Networks Configuration - User Management API
  slug: extreme-networks-configuration-user-management-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: The Copilot Anomalies API
  name: Extreme Networks Copilot - Anomalies API
  slug: extreme-networks-copilot-anomalies-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: The Copilot Connectivity Experience API
  name: Extreme Networks Copilot - Connectivity Experience API
  slug: extreme-networks-copilot-connectivity-experience-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Device 360
  name: Extreme Networks D360 API
  slug: extreme-networks-d360-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Device and client health and status/dashboard
  name: Extreme Networks Dashboard API
  slug: extreme-networks-dashboard-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Client dashboard
  name: Extreme Networks Dashboard - Wired Client Health API
  slug: extreme-networks-dashboard-wired-client-health-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Device dashboard
  name: Extreme Networks Dashboard - Wired Device Health API
  slug: extreme-networks-dashboard-wired-device-health-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Wired Usage and Capacity
  name: Extreme Networks Dashboard - Wired Usage and Capacity API
  slug: extreme-networks-dashboard-wired-usage-and-capacity-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Client dashboard
  name: Extreme Networks Dashboard - Wireless Client Health API
  slug: extreme-networks-dashboard-wireless-client-health-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Device dashboard
  name: Extreme Networks Dashboard - Wireless Device Health API
  slug: extreme-networks-dashboard-wireless-device-health-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Usage and capacity dashboard
  name: Extreme Networks Dashboard - Wireless Usage and Capacity API
  slug: extreme-networks-dashboard-wireless-usage-and-capacity-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: 'Supported device platforms: Cloud Engine, IQ Engine, WiNG, VOSS, EXOS...'
  name: Extreme Networks Device API
  slug: extreme-networks-device-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: The ExtremeLocation and Analytics API
  name: Extreme Networks Essentials - ExtremeLocation API
  slug: extreme-networks-essentials-extremelocation-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Geo View
  name: Extreme Networks Geo-View API
  slug: extreme-networks-geo-view-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Hierarchical ExtremeCloud IQ
  name: Extreme Networks HIQ API
  slug: extreme-networks-hiq-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Hierarchical locations and floor plan
  name: Extreme Networks Location API
  slug: extreme-networks-location-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Access all kinds of logs in ExtremeCloud IQ
  name: Extreme Networks Log API
  slug: extreme-networks-log-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Metadata - Country/...
  name: Extreme Networks Misc API
  slug: extreme-networks-misc-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Unified configuration management for wireless and wired network devices
  name: Extreme Networks Network Policy API
  slug: extreme-networks-network-policy-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: The network scorecard containing device, client, network, Wi-Fi, services health of the selected location.
  name: Extreme Networks Network Scorecard API
  slug: extreme-networks-network-scorecard-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: The NG Reports - On Demand Analytics and Scheduled Reporting
  name: Extreme Networks NG Reports API
  slug: extreme-networks-ng-reports-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: The NG Reports - Scheduled Reporting
  name: Extreme Networks NG Scheduled Reports API
  slug: extreme-networks-ng-scheduled-reports-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Push events/logs to users via Webhook, Email, SMS, etc.
  name: Extreme Networks Notification API
  slug: extreme-networks-notification-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Long-Running Operations (LRO) management for asynchronous APIs
  name: Extreme Networks Operation API
  slug: extreme-networks-operation-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Packet capture sessions in ExtremeCloud IQ
  name: Extreme Networks PacketCaptures API
  slug: extreme-networks-packetcaptures-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: RTT sessions in ExtremeCloud IQ
  name: Extreme Networks RTTS API
  slug: extreme-networks-rtts-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Switch Inspector Panel
  name: Extreme Networks Switch Inspector Panel API
  slug: extreme-networks-switch-inspector-panel-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Thread Networks in ExtremeCloud IQ
  name: Extreme Networks Thread API
  slug: extreme-networks-thread-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: The Universal Compute Platform (UCP) API
  name: Extreme Networks Universal Compute Platform API
  slug: extreme-networks-universal-compute-platform-api
- baseURL: https://api.extremecloudiq.com
  baseurl_source: declared
  description: Local and external user management in ExtremeCloud IQ account
  name: Extreme Networks User API
  slug: extreme-networks-user-api
artifact_total: 102
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ExtremeCloud IQ Account API
  slug: open-extreme-networks-account-api
- collection_type: open
  name: ExtremeCloud IQ Account Administration API
  slug: open-extreme-networks-administration-api
- collection_type: open
  name: ExtremeCloud IQ Account AFC API
  slug: open-extreme-networks-afc-api
- collection_type: open
  name: ExtremeCloud IQ Account Alert API
  slug: open-extreme-networks-alert-api
- collection_type: open
  name: ExtremeCloud IQ Account Application API
  slug: open-extreme-networks-application-api
- collection_type: open
  name: ExtremeCloud IQ Account Authentication API
  slug: open-extreme-networks-authentication-api
- collection_type: open
  name: ExtremeCloud IQ Account Authorization API
  slug: open-extreme-networks-authorization-api
- collection_type: open
  name: ExtremeCloud IQ Account Client API
  slug: open-extreme-networks-client-api
- collection_type: open
  name: ExtremeCloud IQ Account Client - Details API
  slug: open-extreme-networks-client-details-api
- collection_type: open
  name: ExtremeCloud IQ Account Configuration - Authentication API
  slug: open-extreme-networks-configuration-authentication-api
- collection_type: open
  name: ExtremeCloud IQ Account Configuration - Basic API
  slug: open-extreme-networks-configuration-basic-api
- collection_type: open
  name: ExtremeCloud IQ Account Configuration - Certificate API
  slug: open-extreme-networks-configuration-certificate-api
- collection_type: open
  name: ExtremeCloud IQ Account Configuration - Deployment API
  slug: open-extreme-networks-configuration-deployment-api
- collection_type: open
  name: ExtremeCloud IQ Account Configuration - Network API
  slug: open-extreme-networks-configuration-network-api
- collection_type: open
  name: ExtremeCloud IQ Account Configuration - Policy API
  slug: open-extreme-networks-configuration-policy-api
- collection_type: open
  name: ExtremeCloud IQ Account Configuration - User Management API
  slug: open-extreme-networks-configuration-user-management-api
- collection_type: open
  name: ExtremeCloud IQ Account Copilot - Anomalies API
  slug: open-extreme-networks-copilot-anomalies-api
- collection_type: open
  name: ExtremeCloud IQ Account Copilot - Connectivity Experience API
  slug: open-extreme-networks-copilot-connectivity-experience-api
- collection_type: open
  name: ExtremeCloud IQ Account D360 API
  slug: open-extreme-networks-d360-api
- collection_type: open
  name: ExtremeCloud IQ Account Dashboard API
  slug: open-extreme-networks-dashboard-api
- collection_type: open
  name: ExtremeCloud IQ Account Dashboard - Wired Client Health API
  slug: open-extreme-networks-dashboard-wired-client-health-api
- collection_type: open
  name: ExtremeCloud IQ Account Dashboard - Wired Device Health API
  slug: open-extreme-networks-dashboard-wired-device-health-api
- collection_type: open
  name: ExtremeCloud IQ Account Dashboard - Wired Usage and Capacity API
  slug: open-extreme-networks-dashboard-wired-usage-and-capacity-api
- collection_type: open
  name: ExtremeCloud IQ Account Dashboard - Wireless Client Health API
  slug: open-extreme-networks-dashboard-wireless-client-health-api
- collection_type: open
  name: ExtremeCloud IQ Account Dashboard - Wireless Device Health API
  slug: open-extreme-networks-dashboard-wireless-device-health-api
- collection_type: open
  name: ExtremeCloud IQ Account Dashboard - Wireless Usage and Capacity API
  slug: open-extreme-networks-dashboard-wireless-usage-and-capacity-api
- collection_type: open
  name: ExtremeCloud IQ Account Device API
  slug: open-extreme-networks-device-api
- collection_type: open
  name: ExtremeCloud IQ Account Essentials - ExtremeLocation API
  slug: open-extreme-networks-essentials-extremelocation-api
- collection_type: open
  name: ExtremeCloud IQ Account Geo-View API
  slug: open-extreme-networks-geo-view-api
- collection_type: open
  name: ExtremeCloud IQ Account HIQ API
  slug: open-extreme-networks-hiq-api
- collection_type: open
  name: ExtremeCloud IQ Account Location API
  slug: open-extreme-networks-location-api
- collection_type: open
  name: ExtremeCloud IQ Account Log API
  slug: open-extreme-networks-log-api
- collection_type: open
  name: ExtremeCloud IQ Account Misc API
  slug: open-extreme-networks-misc-api
- collection_type: open
  name: ExtremeCloud IQ Account Network Policy API
  slug: open-extreme-networks-network-policy-api
- collection_type: open
  name: ExtremeCloud IQ Account Network Scorecard API
  slug: open-extreme-networks-network-scorecard-api
- collection_type: open
  name: ExtremeCloud IQ Account NG Reports API
  slug: open-extreme-networks-ng-reports-api
- collection_type: open
  name: ExtremeCloud IQ Account NG Scheduled Reports API
  slug: open-extreme-networks-ng-scheduled-reports-api
- collection_type: open
  name: ExtremeCloud IQ Account Notification API
  slug: open-extreme-networks-notification-api
- collection_type: open
  name: ExtremeCloud IQ Account Operation API
  slug: open-extreme-networks-operation-api
- collection_type: open
  name: ExtremeCloud IQ Account PacketCaptures API
  slug: open-extreme-networks-packetcaptures-api
- collection_type: open
  name: ExtremeCloud IQ Account RTTS API
  slug: open-extreme-networks-rtts-api
- collection_type: open
  name: ExtremeCloud IQ Account Switch Inspector Panel API
  slug: open-extreme-networks-switch-inspector-panel-api
- collection_type: open
  name: ExtremeCloud IQ Account Thread API
  slug: open-extreme-networks-thread-api
- collection_type: open
  name: ExtremeCloud IQ Account Universal Compute Platform API
  slug: open-extreme-networks-universal-compute-platform-api
- collection_type: open
  name: ExtremeCloud IQ Account User API
  slug: open-extreme-networks-user-api
- collection_type: open
  name: ExtremeCloud IQ API
  slug: open-extremecloud-iq
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/extreme-networks-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/extremenetworks/ansible_collections.extreme.exos/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/extremenetworks/ansible_collections.extreme.exos/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/extreme-networks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/extreme-networks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/extreme-networks-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.extremenetworks.com/
- group: other
  title: ''
  type: Platform
  url: https://www.extremenetworks.com/platform-one
- group: other
  title: ''
  type: CloudPlatform
  url: https://www.extremecloudiq.com/
- group: other
  title: ''
  type: Products
  url: https://www.extremenetworks.com/products
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.extremecloudiq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://extremecloudiq.com/api-docs/api-reference.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/extremenetworks
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.extremenetworks.com/
- group: operate
  title: ''
  type: Support
  url: https://www.extremenetworks.com/support
- group: operate
  title: ''
  type: Community
  url: https://community.extremenetworks.com/
- group: company
  title: ''
  type: Blog
  url: https://www.extremenetworks.com/resources/blogs
- group: company
  title: ''
  type: Newsroom
  url: https://www.extremenetworks.com/company/newsroom
- group: company
  title: ''
  type: Careers
  url: https://www.extremenetworks.com/company/careers
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.extremenetworks.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.extremenetworks.com/company/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.extremenetworks.com/company/legal/privacy/
- group: auth
  title: ''
  type: Trust
  url: https://www.extremenetworks.com/company/trust/
- group: operate
  title: ''
  type: Status
  url: https://status.extremecloudiq.com/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ExtremeNetworks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/extreme-networks
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/ExtremeNetworks
created: '2026-05-25'
description: 'Extreme Networks (NASDAQ: EXTR) is a Morrisville, North Carolina–headquartered enterprise networking company that provides cloud-managed wired switching, Wi-Fi 6E/Wi-Fi 7 wireless access, SD-WAN, and integrated network security for education, healthcare, government, retail, manufacturing, and large venues. Its flagship platform is Extreme Platform ONE, an AI-driven networking platform that unifies wired, wireless, and security operations, built on top of ExtremeCloud IQ — the company''s multi-tenant, cloud-managed network management system. ExtremeCloud IQ exposes a comprehensive OpenAPI 3.0 REST API at api.extremecloudiq.com covering authentication, device lifecycle, network policy, client and application analytics, alerts, dashboards, SD-WAN, Copilot connectivity experience, packet captures, and hierarchical multi-organization management, with official SDKs in Python, Java, Go, JavaScript, and C#. Extreme also publishes Ansible collections for EXOS, VOSS, SLXOS, NOS, and
  Fabric Engine for declarative on-box switch configuration, a public Postman collection of 400+ requests, and a portfolio of on-prem REST gateways for ExtremeCloud IQ Controller (campus wireless controller) and Application Manager.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/extreme-networks.png
layout: provider
modified: '2026-05-25'
name: Extreme Networks
nav: Providers
network: true
overview: 'Extreme Networks publishes 45 APIs on the [APIs.io](https://apis.io/) network, including Account API, Administration API, AFC API, and 42 more. Tagged areas include Networking, Wireless, Wired, Switching, and Wi-Fi.


  Extreme Networks'' developer surface includes authentication, API reference, GitHub presence, documentation, support, engineering blog, status page, and 20 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 29.0
    catalog_earned_first_party: 0.0
    catalog_gap: 86.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 57.2
    developer_ergonomics: 59.5
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 45
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/extreme-networks/refs/heads/main/screenshots/extreme-networks-2026-06-20T180950.png
security:
- kind: authentication
  name: Extreme Networks Authentication
  slug: extreme-networks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Extreme Networks Domain Security
  slug: extreme-networks-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: extreme-networks
tags:
- Networking
- Wireless
- Wired
- Switching
- Wi-Fi
- Wi-Fi 7
- Cloud Management
- SD-WAN
- Network Security
- Network Management
- AI Networking
- Enterprise
website: https://www.extremenetworks.com/
---
