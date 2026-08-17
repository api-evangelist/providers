---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Infoblox Agentic Access
  operation_count: 31
  slug: infoblox-agentic-access
  summary_line: 31 operations · 13 acting
api_count: 21
apis:
- description: API for configuring DNS settings within the BloxOne platform. Manages DNS server configurations, views, ACLs, forwarding rules, and other DNS infrastructure settings through the Cloud Service Platform
  name: Infoblox BloxOne DNS Configuration API
  slug: infoblox-bloxone-dns-configuration-api
- description: API for managing DNS data records within the BloxOne platform. Provides endpoints for creating, reading, updating, and deleting DNS resource records including A, AAAA, CNAME, MX, TXT, and other record
  name: Infoblox BloxOne DNS Data API
  slug: infoblox-bloxone-dns-data-api
- description: API for IP address management and DHCP protocol features within the BloxOne platform. Provides visibility and provisioning tools to manage networking spaces, monitoring and reporting of IP address inf
  name: Infoblox BloxOne IPAM/DHCP API
  slug: infoblox-bloxone-ipamdhcp-api
- description: API for managing TSIG and other keys used in DDI operations within the BloxOne platform. Handles creation and management of authentication keys used for securing DNS zone transfers and dynamic updates
  name: Infoblox BloxOne DDI Keys API
  slug: infoblox-bloxone-ddi-keys-api
- description: API for managing anycast configurations within the BloxOne platform. Enables high availability configuration of Infoblox applications running on customer premises by managing anycast addressing and ro
  name: Infoblox BloxOne Anycast Configuration API
  slug: infoblox-bloxone-anycast-configuration-api
- description: API for managing BloxOne Cloud infrastructure components. Provides endpoints for managing on-premises hosts, service configurations, and infrastructure resources within the Infoblox Cloud Service Plat
  name: Infoblox BloxOne Infrastructure Management API
  slug: infoblox-bloxone-infrastructure-management-api
- description: API for provisioning and activating on-premises hosts within the BloxOne platform. Handles the host activation workflow including zero touch provisioning and bootstrap configuration for on-prem deploy
  name: Infoblox BloxOne Host Activation API
  slug: infoblox-bloxone-host-activation-api
- description: API for managing DNS Forwarding Proxy (DFP) configurations within BloxOne Threat Defense. Enforces DNS client-based security policies at remote sites by forwarding DNS queries through the Infoblox clo
  name: Infoblox BloxOne DNS Forwarding Proxy API
  slug: infoblox-bloxone-dns-forwarding-proxy-api
- description: API for managing BloxOne Threat Defense Cloud firewall policies and security lists. Provides visibility into infected and compromised devices on the network and allows management of security policies,
  name: Infoblox BloxOne Firewall API
  slug: infoblox-bloxone-firewall-api
- description: API for configuring BloxOne Threat Defense Cloud redirect behavior. Allows configuring traffic redirection to the Infoblox server or custom destinations when threats are detected, and manages redirect
  name: Infoblox BloxOne Redirect API
  slug: infoblox-bloxone-redirect-api
- description: API for managing software upgrade policies for BloxOne on-premises hosts. Allows scheduling and configuring software and configuration updates for deployed BloxOne infrastructure components.
  name: Infoblox BloxOne Upgrade Policy API
  slug: infoblox-bloxone-upgrade-policy-api
- description: 'API for threat intelligence, security analytics, and DNS firewall capabilities. Provides programmatic access to BloxOne Threat Defense features including security policy management, threat feeds, and '
  name: Infoblox Threat Defense API
  slug: infoblox-threat-defense-api
- description: 'Threat Intelligence Data Exchange (TIDE) API for submitting and retrieving threat indicators. Provides access to indicators of compromise in the TIDE database in multiple formats including JSON, XML, '
  name: Infoblox TIDE API
  slug: infoblox-tide-api
- description: Threat research API that provides contextual information from multiple sources simultaneously for a given indicator. Supports lookups on IPs, URLs, domains, hostnames, email addresses, and file hashes
  name: Infoblox Dossier API
  slug: infoblox-dossier-api
- description: RESTful API for the Infoblox NetMRI network change and configuration management platform. Enables automation of network device provisioning, security compliance checks, configuration management, and n
  name: Infoblox NetMRI API
  slug: infoblox-netmri-api
- description: Operations for managing DHCP ranges, fixed addresses, leases, and DHCP option configurations.
  name: Infoblox DHCP API
  slug: infoblox-dhcp-api
- description: Operations for managing DNS resource records including A, AAAA, CNAME, MX, PTR, TXT, SRV, and NS records.
  name: Infoblox DNS Records API
  slug: infoblox-dns-records-api
- description: Operations for managing authoritative DNS zones, delegated zones, forward zones, and stub zones.
  name: Infoblox DNS Zones API
  slug: infoblox-dns-zones-api
- description: Operations for managing Grid members, properties, and services.
  name: Infoblox Grid API
  slug: infoblox-grid-api
- description: Operations for managing IP addresses, querying address utilization, and performing next available IP lookups.
  name: Infoblox IP Address Management API
  slug: infoblox-ip-address-management-api
- description: Operations for managing IPv4 and IPv6 networks, network containers, and network views.
  name: Infoblox Networks API
  slug: infoblox-networks-api
artifact_total: 74
collections:
- collection_type: postman
  name: Infoblox WAPI (Web API) DHCP API
  slug: postman-infoblox-dhcp-api
- collection_type: postman
  name: Infoblox WAPI (Web API) DHCP DNS Records API
  slug: postman-infoblox-dns-records-api
- collection_type: postman
  name: Infoblox WAPI (Web API) DHCP DNS Zones API
  slug: postman-infoblox-dns-zones-api
- collection_type: postman
  name: Infoblox WAPI (Web API) DHCP Grid API
  slug: postman-infoblox-grid-api
- collection_type: postman
  name: Infoblox WAPI (Web API) DHCP IP Address Management API
  slug: postman-infoblox-ip-address-management-api
- collection_type: postman
  name: Infoblox WAPI (Web API) DHCP Networks API
  slug: postman-infoblox-networks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Infoblox WAPI (Web API) DHCP API
  slug: open-infoblox-dhcp-api
- collection_type: open
  name: Infoblox WAPI (Web API) DHCP DNS Records API
  slug: open-infoblox-dns-records-api
- collection_type: open
  name: Infoblox WAPI (Web API) DHCP DNS Zones API
  slug: open-infoblox-dns-zones-api
- collection_type: open
  name: Infoblox WAPI (Web API) DHCP Grid API
  slug: open-infoblox-grid-api
- collection_type: open
  name: Infoblox WAPI (Web API) DHCP IP Address Management API
  slug: open-infoblox-ip-address-management-api
- collection_type: open
  name: Infoblox WAPI (Web API) DHCP Networks API
  slug: open-infoblox-networks-api
- collection_type: open
  name: Infoblox WAPI (Web API)
  slug: open-infoblox-wapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/infoblox/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/infoblox-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/infoblox-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infoblox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/infoblox-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/infoblox
- group: start
  title: ''
  type: Portal
  url: https://www.infoblox.com/developer-portal/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.infoblox.com/developer-portal/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.infoblox.com/
- group: company
  title: ''
  type: Blog
  url: https://blogs.infoblox.com/
- group: operate
  title: ''
  type: Community
  url: https://community.infoblox.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.infoblox.com/
- group: operate
  title: ''
  type: Support
  url: https://www.infoblox.com/support/
- group: company
  title: ''
  type: Website
  url: https://www.infoblox.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.infoblox.com/company/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.infoblox.com/company/legal/website-terms-and-conditions/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infobloxopen
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.infoblox.com/space/BloxOneInfrastructure/332366018/BloxOne+Release+Notes
- group: start
  title: ''
  type: Console
  url: https://csp.infoblox.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://infoblox.com/llms.txt
created: '2024-01-15'
description: Infoblox is a networking and cybersecurity company providing DDI (DNS, DHCP, and IPAM) solutions and protective DNS-layer security services. Its product portfolio spans the Universal DDI suite for unified hybrid and multi-cloud network services, NIOS DDI for on-premises deployments, NIOS-X as a Service, Threat Defense for DNS-layer security, threat intelligence (TIDE) and research (Dossier), and NetMRI for network change and configuration management.
finops:
- name: Infoblox Finops
  service_category: Network Services + Security
  slug: infoblox-finops
image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
json_schemas:
- name: DHCPLease
  property_count: 8
  slug: infoblox-dhcplease
- name: DHCPRange
  property_count: 7
  slug: infoblox-dhcprange
- name: DHCPRangeCreate
  property_count: 5
  slug: infoblox-dhcprangecreate
- name: Error
  property_count: 3
  slug: infoblox-error
- name: FixedAddress
  property_count: 6
  slug: infoblox-fixedaddress
- name: FixedAddressCreate
  property_count: 4
  slug: infoblox-fixedaddresscreate
- name: Grid
  property_count: 4
  slug: infoblox-grid
- name: IPv4Address
  property_count: 10
  slug: infoblox-ipv4address
- name: Member
  property_count: 5
  slug: infoblox-member
- name: Network
  property_count: 5
  slug: infoblox-network
- name: NetworkCreate
  property_count: 3
  slug: infoblox-networkcreate
- name: NetworkView
  property_count: 4
  slug: infoblox-networkview
- name: RecordA
  property_count: 9
  slug: infoblox-recorda
- name: RecordAAAA
  property_count: 6
  slug: infoblox-recordaaaa
- name: RecordAAAACreate
  property_count: 4
  slug: infoblox-recordaaaacreate
- name: RecordACreate
  property_count: 6
  slug: infoblox-recordacreate
- name: RecordAUpdate
  property_count: 6
  slug: infoblox-recordaupdate
- name: RecordCNAME
  property_count: 6
  slug: infoblox-recordcname
- name: RecordCNAMECreate
  property_count: 4
  slug: infoblox-recordcnamecreate
- name: RecordHost
  property_count: 5
  slug: infoblox-recordhost
- name: RecordHostCreate
  property_count: 4
  slug: infoblox-recordhostcreate
- name: RecordMX
  property_count: 6
  slug: infoblox-recordmx
- name: RecordMXCreate
  property_count: 5
  slug: infoblox-recordmxcreate
- name: RecordPTR
  property_count: 5
  slug: infoblox-recordptr
- name: RecordPTRCreate
  property_count: 4
  slug: infoblox-recordptrcreate
- name: RecordTXT
  property_count: 5
  slug: infoblox-recordtxt
- name: RecordTXTCreate
  property_count: 4
  slug: infoblox-recordtxtcreate
- name: ZoneAuth
  property_count: 6
  slug: infoblox-zoneauth
- name: ZoneAuthCreate
  property_count: 4
  slug: infoblox-zoneauthcreate
- name: ZoneForward
  property_count: 5
  slug: infoblox-zoneforward
json_structures:
- name: Infoblox Structure
  property_count: 0
  slug: infoblox-structure
layout: provider
modified: '2026-05-19'
name: Infoblox
nav: Providers
network: true
overview: 'Infoblox publishes 6 APIs on the [APIs.io](https://apis.io/) network, including DHCP API, DNS Records API, DNS Zones API, and 3 more. Tagged areas include Cloud, DDI, DHCP, DNS, and IPAM.


  The Infoblox catalog on APIs.io includes 1 Spectral governance ruleset.


  Infoblox''s developer surface includes authentication, developer portal, getting-started guide, documentation, engineering blog, support, changelog, and 13 more developer resources.'
plans:
- name: Infoblox Plans Pricing
  plan_count: 3
  slug: infoblox-plans-pricing
random_paper: 120
rate_limits:
- limit_count: 2
  name: Infoblox Rate Limits
  slug: infoblox-rate-limits
rules:
- name: Infoblox API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: infoblox-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.6
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 59.0
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infoblox/refs/heads/main/screenshots/infoblox-2026-06-20T183337.png
security:
- kind: authentication
  name: Infoblox Authentication
  slug: infoblox-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Infoblox Domain Security
  slug: infoblox-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Infoblox Trust Center
  slug: infoblox-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR, FIPS 140
slug: infoblox
tags:
- Cloud
- DDI
- DHCP
- DNS
- IPAM
- Network Management
- Security
- Threat Intelligence
website: https://www.infoblox.com/
---
