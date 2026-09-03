---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Juniper Networks Agentic Access
  operation_count: 81
  slug: juniper-networks-agentic-access
  summary_line: 81 operations · 27 acting
api_count: 5
apis:
- description: Python library for automating Junos devices using NETCONF.
  name: Junos PyEZ
  slug: junos-pyez
- baseURL: netconf://device:830
  baseurl_source: declared
  description: NETCONF-based XML API for programmatic access to Junos devices.
  name: Junos XML API
  slug: junos-xml-api
- description: Python-based tool for snapshot and verification of network device configurations.
  name: Juniper JSNAPy
  slug: juniper-jsnapy
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Alarm monitoring, acknowledgment, and notification configuration.
  name: Juniper Networks Alarms API
  slug: juniper-networks-alarms-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Network state anomaly detection and reporting.
  name: Juniper Networks Anomalies API
  slug: juniper-networks-anomalies-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: User login, logout, and token management.
  name: Juniper Networks Authentication API
  slug: juniper-networks-authentication-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: BGP router and peering configuration.
  name: Juniper Networks BGP Routers API
  slug: juniper-networks-bgp-routers-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Blueprint lifecycle management for data center network intent, including staging, commit, and deployment.
  name: Juniper Networks Blueprints API
  slug: juniper-networks-blueprints-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Wireless and wired client session monitoring and statistics.
  name: Juniper Networks Clients API
  slug: juniper-networks-clients-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Configuration management, templates, and deployment.
  name: Juniper Networks Configuration API
  slug: juniper-networks-configuration-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Design resources including logical devices, interface maps, rack types, templates, and config templates.
  name: Juniper Networks Design API
  slug: juniper-networks-design-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Device discovery, management, and monitoring operations.
  name: Juniper Networks Devices API
  slug: juniper-networks-devices-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Floating IP pool and association management.
  name: Juniper Networks Floating IPs API
  slug: juniper-networks-floating-ips-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Intent-Based Analytics probes and dashboards.
  name: Juniper Networks IBA API
  slug: juniper-networks-iba-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: AI-driven network insights, anomaly detection, and Marvis recommendations.
  name: Juniper Networks Insights API
  slug: juniper-networks-insights-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Device claiming, unclaiming, and inventory management.
  name: Juniper Networks Inventory API
  slug: juniper-networks-inventory-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Asynchronous job tracking and management.
  name: Juniper Networks Jobs API
  slug: juniper-networks-jobs-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Floor plan and map management for site RF planning.
  name: Juniper Networks Maps API
  slug: juniper-networks-maps-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Device and session monitoring operations.
  name: Juniper Networks Monitoring API
  slug: juniper-networks-monitoring-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Network address translation rule management.
  name: Juniper Networks NAT API
  slug: juniper-networks-nat-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Network policy rules for traffic control between virtual networks.
  name: Juniper Networks Network Policies API
  slug: juniper-networks-network-policies-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Organization-level settings, licenses, and inventory management.
  name: Juniper Networks Organizations API
  slug: juniper-networks-organizations-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Tenant project management.
  name: Juniper Networks Projects API
  slug: juniper-networks-projects-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Resource pool management for ASN, IP, and VNI allocation.
  name: Juniper Networks Resources API
  slug: juniper-networks-resources-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Script management and execution on managed devices.
  name: Juniper Networks Scripts API
  slug: juniper-networks-scripts-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Security group rules for workload micro-segmentation.
  name: Juniper Networks Security Groups API
  slug: juniper-networks-security-groups-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Security policy and zone management.
  name: Juniper Networks Security Policies API
  slug: juniper-networks-security-policies-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Network function service instance management.
  name: Juniper Networks Service Instances API
  slug: juniper-networks-service-instances-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Site creation, configuration, and management within organizations.
  name: Juniper Networks Sites API
  slug: juniper-networks-sites-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: System information and operational commands.
  name: Juniper Networks System API
  slug: juniper-networks-system-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Managed system (device) agent lifecycle and telemetry.
  name: Juniper Networks Systems API
  slug: juniper-networks-systems-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: User and role-based access control management.
  name: Juniper Networks Users API
  slug: juniper-networks-users-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Virtual network creation and management.
  name: Juniper Networks Virtual Networks API
  slug: juniper-networks-virtual-networks-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: IPsec VPN tunnel configuration.
  name: Juniper Networks VPN API
  slug: juniper-networks-vpn-api
- baseURL: https://<apstra-server>/api
  baseurl_source: declared
  description: Wireless LAN configuration including SSIDs, security, and VLAN assignment.
  name: Juniper Networks WLANs API
  slug: juniper-networks-wlans-api
artifact_total: 130
asyncapis:
- description: Junos Telemetry Interface provides real-time streaming telemetry from Juniper Networks devices using gRPC or UDP protocols. JTI pushes operational data from Junos devices at configured intervals, repl
  name: Junos Telemetry Interface (JTI) Streaming
  slug: juniper-networks-junos-telemetry-asyncapi
- description: Juniper Mist delivers real-time webhook notifications for network events, device state changes, alarms, audits, and client activity. Webhooks are configured at the organization or site level through t
  name: Juniper Mist Webhooks
  slug: juniper-networks-mist-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms API
  slug: open-juniper-networks-alarms-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Anomalies API
  slug: open-juniper-networks-anomalies-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking API
  slug: open-juniper-networks-apstra
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Authentication API
  slug: open-juniper-networks-authentication-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms BGP Routers API
  slug: open-juniper-networks-bgp-routers-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Blueprints API
  slug: open-juniper-networks-blueprints-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Clients API
  slug: open-juniper-networks-clients-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Configuration API
  slug: open-juniper-networks-configuration-api
- collection_type: open
  name: Juniper Networks Juniper Contrail Networking REST API
  slug: open-juniper-networks-contrail
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Design API
  slug: open-juniper-networks-design-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Devices API
  slug: open-juniper-networks-devices-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Floating IPs API
  slug: open-juniper-networks-floating-ips-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms IBA API
  slug: open-juniper-networks-iba-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Insights API
  slug: open-juniper-networks-insights-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Inventory API
  slug: open-juniper-networks-inventory-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Jobs API
  slug: open-juniper-networks-jobs-api
- collection_type: open
  name: Juniper Networks Junos Space Network Management Platform REST API
  slug: open-juniper-networks-junos-space
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Maps API
  slug: open-juniper-networks-maps-api
- collection_type: open
  name: Juniper Networks Juniper Mist Cloud API
  slug: open-juniper-networks-mist
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Monitoring API
  slug: open-juniper-networks-monitoring-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms NAT API
  slug: open-juniper-networks-nat-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Network Policies API
  slug: open-juniper-networks-network-policies-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Organizations API
  slug: open-juniper-networks-organizations-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Projects API
  slug: open-juniper-networks-projects-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Resources API
  slug: open-juniper-networks-resources-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Scripts API
  slug: open-juniper-networks-scripts-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Security Groups API
  slug: open-juniper-networks-security-groups-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Security Policies API
  slug: open-juniper-networks-security-policies-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Service Instances API
  slug: open-juniper-networks-service-instances-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Sites API
  slug: open-juniper-networks-sites-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms System API
  slug: open-juniper-networks-system-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Systems API
  slug: open-juniper-networks-systems-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Users API
  slug: open-juniper-networks-users-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms Virtual Networks API
  slug: open-juniper-networks-virtual-networks-api
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms VPN API
  slug: open-juniper-networks-vpn-api
- collection_type: open
  name: Juniper Networks Juniper vSRX REST API
  slug: open-juniper-networks-vsrx
- collection_type: open
  name: Juniper Networks Juniper Apstra Intent-Based Networking Alarms WLANs API
  slug: open-juniper-networks-wlans-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/juniper-networks-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/juniper-networks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/juniper-networks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/juniper-networks-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/juniper-networks
- group: design
  title: ''
  type: JSONLD
  url: json-ld/juniper-networks-context.jsonld
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.juniper.net/
- group: operate
  title: ''
  type: Support
  url: https://support.juniper.net/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Juniper
- group: operate
  title: ''
  type: Community
  url: https://community.juniper.net/
- group: learn
  title: ''
  type: Training
  url: https://learningportal.juniper.net/
- group: company
  title: ''
  type: Website
  url: https://www.juniper.net/
- group: docs
  title: ''
  type: Documentation
  url: https://www.juniper.net/documentation/
- group: company
  title: ''
  type: Blog
  url: https://blogs.juniper.net/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.juniper.net/
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
created: '2024'
description: APIs and developer resources for Juniper Networks networking products and services.
finops:
- name: Juniper Networks Finops
  service_category: Networking / SDN / Security
  slug: juniper-networks-finops
image: https://www.juniper.net/content/dam/juniper/images/logos/juniper-networks-logo.png
json_schemas:
- name: Admin
  property_count: 4
  slug: juniper-networks-admin
- name: Alarm
  property_count: 7
  slug: juniper-networks-alarm
- name: Anomaly
  property_count: 7
  slug: juniper-networks-anomaly
- name: ApiToken
  property_count: 4
  slug: juniper-networks-apitoken
- name: Juniper Apstra Blueprint
  property_count: 12
  slug: juniper-networks-apstra-blueprint
- name: AsnPool
  property_count: 4
  slug: juniper-networks-asnpool
- name: Blueprint
  property_count: 6
  slug: juniper-networks-blueprint
- name: BlueprintSummary
  property_count: 7
  slug: juniper-networks-blueprintsummary
- name: ClientStat
  property_count: 13
  slug: juniper-networks-clientstat
- name: Configlet
  property_count: 5
  slug: juniper-networks-configlet
- name: Juniper Contrail Virtual Network
  property_count: 15
  slug: juniper-networks-contrail-virtual-network
- name: Device
  property_count: 10
  slug: juniper-networks-device
- name: Error
  property_count: 1
  slug: juniper-networks-error
- name: FlowSession
  property_count: 13
  slug: juniper-networks-flowsession
- name: IbaProbe
  property_count: 6
  slug: juniper-networks-ibaprobe
- name: InterfaceMap
  property_count: 5
  slug: juniper-networks-interfacemap
- name: InventoryItem
  property_count: 7
  slug: juniper-networks-inventoryitem
- name: IpPool
  property_count: 3
  slug: juniper-networks-ippool
- name: IpsecVpn
  property_count: 7
  slug: juniper-networks-ipsecvpn
- name: Job
  property_count: 9
  slug: juniper-networks-job
- name: Junos Security Policy Rule
  property_count: 7
  slug: juniper-networks-junos-security-policy
- name: LogicalDevice
  property_count: 3
  slug: juniper-networks-logicaldevice
- name: Map
  property_count: 7
  slug: juniper-networks-map
- name: MarvisAction
  property_count: 6
  slug: juniper-networks-marvisaction
- name: Juniper Mist Device
  property_count: 19
  slug: juniper-networks-mist-device
- name: Juniper Mist Site
  property_count: 14
  slug: juniper-networks-mist-site
- name: NatRuleSet
  property_count: 4
  slug: juniper-networks-natruleset
- name: NetworkPolicy
  property_count: 3
  slug: juniper-networks-networkpolicy
- name: ObjectRef
  property_count: 3
  slug: juniper-networks-objectref
- name: Organization
  property_count: 7
  slug: juniper-networks-organization
- name: RackType
  property_count: 6
  slug: juniper-networks-racktype
- name: Script
  property_count: 5
  slug: juniper-networks-script
- name: SecurityGroup
  property_count: 3
  slug: juniper-networks-securitygroup
- name: SecurityPolicy
  property_count: 3
  slug: juniper-networks-securitypolicy
- name: SecurityZone
  property_count: 5
  slug: juniper-networks-securityzone
- name: Site
  property_count: 12
  slug: juniper-networks-site
- name: System
  property_count: 8
  slug: juniper-networks-system
- name: SystemAlarm
  property_count: 5
  slug: juniper-networks-systemalarm
- name: SystemInfo
  property_count: 6
  slug: juniper-networks-systeminfo
- name: Template
  property_count: 5
  slug: juniper-networks-template
- name: User
  property_count: 7
  slug: juniper-networks-user
- name: VirtualNetwork
  property_count: 8
  slug: juniper-networks-virtualnetwork
- name: VirtualNetworkRef
  property_count: 3
  slug: juniper-networks-virtualnetworkref
- name: VniPool
  property_count: 3
  slug: juniper-networks-vnipool
- name: Wlan
  property_count: 11
  slug: juniper-networks-wlan
json_structures:
- name: Juniper Networks Structure
  property_count: 0
  slug: juniper-networks-structure
jsonld:
- class_count: 85
  name: Juniper Networks Context
  property_count: 8
  slug: juniper-networks-context
layout: provider
modified: '2026-05-19'
name: Juniper Networks
nav: Providers
network: true
overview: 'Juniper Networks publishes 33 APIs on the [APIs.io](https://apis.io/) network, including Junos XML API, Alarms API, Anomalies API, and 30 more. Tagged areas include Automation, Cloud, Data-Center, Enterprise, and Networking.


  The Juniper Networks catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Juniper Networks'' developer surface includes authentication, support, GitHub presence, training material, documentation, engineering blog, YouTube channel, and 12 more developer resources.'
plans:
- name: Juniper Networks Plans Pricing
  plan_count: 1
  slug: juniper-networks-plans-pricing
press:
- date: '2026-05-25'
  title: Hewlett Packard Enterprise closes acquisition of Juniper ...
  url: https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html
- date: '2026-05-25'
  title: HPE to Acquire Juniper Networks to Accelerate AI-Driven ...
  url: https://www.businesswire.com/news/home/20240109534304/en/HPE-to-Acquire-Juniper-Networks-to-Accelerate-AI-Driven-Innovation
- date: '2026-05-25'
  title: HPE to Acquire Juniper Networks to Accelerate AI-driven ...
  url: https://www.hpcwire.com/bigdatawire/this-just-in/hpe-to-acquire-juniper-networks-to-accelerate-ai-driven-innovation/
- date: '2026-05-25'
  title: Juniper Networks, Now Part of HPE – Leading the ...
  url: https://www.juniper.net/us/en.html
- date: '2026-05-25'
  title: Hewlett Packard Enterprise
  url: https://www.facebook.com/HewlettPackardEnterprise/posts/you-showed-up-in-the-comments-the-quotes-and-the-threads-since-hpes-juniper-acqu/1191246859707387/
random_paper: 2
rate_limits:
- limit_count: 1
  name: Juniper Networks Rate Limits
  slug: juniper-networks-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Juniper Networks API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: juniper-networks-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Juniper Networks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: juniper-networks-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 13.6
    contract_quality: 71.1
    developer_ergonomics: 40.5
    discoverability: 66.7
    governance: 13.6
    operational_transparency: 18.4
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 31.3
      derived: 0
      marker_coverage: 0.0
      total: 32
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/juniper-networks/refs/heads/main/screenshots/juniper-networks-2026-06-20T183831.png
security:
- kind: authentication
  name: Juniper Networks Authentication
  slug: juniper-networks-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Juniper Networks Domain Security
  slug: juniper-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: juniper-networks
tags:
- Automation
- Cloud
- Data-Center
- Enterprise
- Networking
- SDN
- Security
- Fortune 1000
website: https://www.juniper.net/
---
