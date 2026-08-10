---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Microsoft Azure Networking Agentic Access
  operation_count: 28
  slug: microsoft-azure-networking-agentic-access
  summary_line: 28 operations · 11 acting
api_count: 25
apis:
- description: Distribute traffic across multiple virtual machines and services with Azure Load Balancer.
  name: Azure Load Balancer API
  slug: azure-load-balancer-api
- description: Web traffic load balancer with application-level routing and SSL termination.
  name: Azure Application Gateway API
  slug: azure-application-gateway-api
- description: Control network traffic to and from Azure resources with security rules.
  name: Azure Network Security Groups API
  slug: azure-network-security-groups-api
- description: Establish secure cross-premises connectivity between Azure and on-premises networks.
  name: Azure VPN Gateway API
  slug: azure-vpn-gateway-api
- description: DNS-based traffic load balancer for distributing traffic globally.
  name: Azure Traffic Manager API
  slug: azure-traffic-manager-api
- description: Create private connections between Azure datacenters and on-premises infrastructure.
  name: Azure ExpressRoute API
  slug: azure-expressroute-api
- description: Cloud-native network security service with built-in high availability.
  name: Azure Firewall API
  slug: azure-firewall-api
- description: Host DNS zones and manage DNS records using the Azure DNS REST API. Supports creating, updating, and deleting public DNS zones and record sets for domain name resolution within Azure-managed infrastru
  name: Azure DNS API
  slug: azure-dns-api
- description: Manage private DNS zones for name resolution within Azure virtual networks. Azure Private DNS provides a reliable and secure DNS service to manage and resolve domain names in a virtual network without
  name: Azure Private DNS API
  slug: azure-private-dns-api
- description: Global load balancer and application delivery network that provides fast, reliable, and secure access to web applications. Azure Front Door offers layer 7 load balancing, SSL offload, URL-based routin
  name: Azure Front Door API
  slug: azure-front-door-api
- description: Manage DDoS protection plans that provide enhanced DDoS mitigation capabilities for Azure Virtual Network resources. Azure DDoS Protection provides countermeasures against sophisticated DDoS threats w
  name: Azure DDoS Protection API
  slug: azure-ddos-protection-api
- description: Monitor, diagnose, and gain insights into network performance and health in Azure. Network Watcher provides tools for packet capture, connection troubleshooting, NSG flow logs, and network topology vi
  name: Azure Network Watcher API
  slug: azure-network-watcher-api
- description: Fully managed PaaS service that provides secure and seamless RDP and SSH connectivity to virtual machines directly through the Azure portal over TLS. Azure Bastion is deployed inside a virtual network
  name: Azure Bastion API
  slug: azure-bastion-api
- description: Simplify outbound-only internet connectivity for virtual networks. When configured on a subnet, all outbound connectivity uses specified static public IP addresses. NAT Gateway provides on-demand SNAT
  name: Azure NAT Gateway API
  slug: azure-nat-gateway-api
- description: Access Azure PaaS services and customer-owned services over a private endpoint in your virtual network. Azure Private Link eliminates data exposure to the public internet by keeping traffic on the Mic
  name: Azure Private Link API
  slug: azure-private-link-api
- description: Networking service that provides optimized and automated branch-to-branch connectivity through Azure. Virtual WAN brings together networking, security, and routing functionalities into a single operat
  name: Azure Virtual WAN API
  slug: azure-virtual-wan-api
- description: Cloud-native web application firewall service that provides centralized protection for web applications from common exploits and vulnerabilities. Azure WAF can be deployed with Application Gateway, Fr
  name: Azure Web Application Firewall API
  slug: azure-web-application-firewall-api
- description: Operations for managing backend address pools that define the group of resources to receive load-balanced traffic.
  name: Azure Networking Backend Address Pools API
  slug: microsoft-azure-networking-backend-address-pools-api
- description: Operations for managing health probes that monitor the health status of backend resources.
  name: Azure Networking Load Balancer Probes API
  slug: microsoft-azure-networking-load-balancer-probes-api
- description: Operations for creating, updating, deleting, and listing Azure Load Balancer resources.
  name: Azure Networking Load Balancers API
  slug: microsoft-azure-networking-load-balancers-api
- description: Operations for managing load balancing rules that define how traffic is distributed to backend pool members.
  name: Azure Networking Load Balancing Rules API
  slug: microsoft-azure-networking-load-balancing-rules-api
- description: Operations operations
  name: Azure Networking Operations API
  slug: microsoft-azure-networking-operations-api
- description: Operations for managing subnets within a virtual network, including creation, configuration, and delegation.
  name: Azure Networking Subnets API
  slug: microsoft-azure-networking-subnets-api
- description: Operations for creating and managing peering connections between virtual networks.
  name: Azure Networking Virtual Network Peerings API
  slug: microsoft-azure-networking-virtual-network-peerings-api
- description: Operations for creating, updating, deleting, and listing Azure Virtual Networks within subscriptions and resource groups.
  name: Azure Networking Virtual Networks API
  slug: microsoft-azure-networking-virtual-networks-api
artifact_total: 69
collections:
- collection_type: postman
  name: Azure Networking Azure Load Balancer Backend Address Pools API
  slug: postman-microsoft-azure-networking-backend-address-pools-api
- collection_type: postman
  name: Azure Networking Azure Load Balancer Backend Address Pools Load Balancer Probes API
  slug: postman-microsoft-azure-networking-load-balancer-probes-api
- collection_type: postman
  name: Azure Networking Azure Load Balancer Backend Address Pools Load Balancers API
  slug: postman-microsoft-azure-networking-load-balancers-api
- collection_type: postman
  name: Azure Networking Azure Load Balancer Backend Address Pools Load Balancing Rules API
  slug: postman-microsoft-azure-networking-load-balancing-rules-api
- collection_type: postman
  name: Azure Networking Azure Load Balancer Backend Address Pools Operations API
  slug: postman-microsoft-azure-networking-operations-api
- collection_type: postman
  name: Azure Networking Azure Load Balancer Backend Address Pools Subnets API
  slug: postman-microsoft-azure-networking-subnets-api
- collection_type: postman
  name: Azure Networking Azure Load Balancer Backend Address Pools Virtual Network Peerings API
  slug: postman-microsoft-azure-networking-virtual-network-peerings-api
- collection_type: postman
  name: Azure Networking Azure Load Balancer Backend Address Pools Virtual Networks API
  slug: postman-microsoft-azure-networking-virtual-networks-api
- collection_type: open
  name: Azure Networking Azure Load Balancer API
  slug: open-azure-networking-load-balancer
- collection_type: open
  name: Azure Networking Azure Virtual Networks API
  slug: open-azure-networking-virtual-networks
- collection_type: open
  name: Azure Virtual Network REST API
  slug: open-microsoft-azure-networking
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-networking/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-networking-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-networking-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-networking-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-networking-scopes.yml
- group: start
  title: ''
  type: X-portal
  url: https://portal.azure.com
- group: operate
  title: ''
  type: X-support
  url: https://azure.microsoft.com/en-us/support/
- group: operate
  title: ''
  type: X-status
  url: https://status.azure.com/
- group: company
  title: ''
  type: X-blog
  url: https://azure.microsoft.com/en-us/blog/topics/networking/
- group: commercial
  title: ''
  type: X-terms-of-service
  url: https://azure.microsoft.com/en-us/support/legal/
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/networking/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/networking/fundamentals/networking-overview
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/azure/developer/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Azure/azure-rest-api-specs
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-virtual-network
- group: operate
  title: ''
  type: ChangeLog
  url: https://azure.microsoft.com/en-us/updates/?query=networking
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com/#home
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
created: '2024-01-15'
description: A collection of Azure Networking APIs for managing virtual networks, load balancers, application gateways, and network security.
finops:
- name: Microsoft Azure Networking Finops
  service_category: Cloud Networking
  slug: microsoft-azure-networking-finops
image: https://azure.microsoft.com/svghandler/azure-networking.svg
json_schemas:
- name: AddressSpace
  property_count: 1
  slug: microsoft-azure-networking-addressspace
- name: BackendAddressPool
  property_count: 3
  slug: microsoft-azure-networking-backendaddresspool
- name: BackendAddressPoolListResult
  property_count: 2
  slug: microsoft-azure-networking-backendaddresspoollistresult
- name: DhcpOptions
  property_count: 1
  slug: microsoft-azure-networking-dhcpoptions
- name: ErrorResponse
  property_count: 1
  slug: microsoft-azure-networking-errorresponse
- name: FrontendIPConfiguration
  property_count: 3
  slug: microsoft-azure-networking-frontendipconfiguration
- name: InboundNatRule
  property_count: 3
  slug: microsoft-azure-networking-inboundnatrule
- name: LoadBalancer
  property_count: 7
  slug: microsoft-azure-networking-loadbalancer
- name: LoadBalancerListResult
  property_count: 2
  slug: microsoft-azure-networking-loadbalancerlistresult
- name: LoadBalancerLoadBalancingRuleListResult
  property_count: 2
  slug: microsoft-azure-networking-loadbalancerloadbalancingrulelistresult
- name: LoadBalancerProbeListResult
  property_count: 2
  slug: microsoft-azure-networking-loadbalancerprobelistresult
- name: LoadBalancingRule
  property_count: 3
  slug: microsoft-azure-networking-loadbalancingrule
- name: Operation
  property_count: 3
  slug: microsoft-azure-networking-operation
- name: OperationList
  property_count: 2
  slug: microsoft-azure-networking-operationlist
- name: OutboundRule
  property_count: 3
  slug: microsoft-azure-networking-outboundrule
- name: Probe
  property_count: 3
  slug: microsoft-azure-networking-probe
- name: Resource
  property_count: 6
  slug: microsoft-azure-networking-resource
- name: ResourceList
  property_count: 2
  slug: microsoft-azure-networking-resourcelist
- name: Subnet
  property_count: 3
  slug: microsoft-azure-networking-subnet
- name: SubnetListResult
  property_count: 2
  slug: microsoft-azure-networking-subnetlistresult
- name: VirtualNetwork
  property_count: 6
  slug: microsoft-azure-networking-virtualnetwork
- name: VirtualNetworkListResult
  property_count: 2
  slug: microsoft-azure-networking-virtualnetworklistresult
- name: VirtualNetworkPeering
  property_count: 3
  slug: microsoft-azure-networking-virtualnetworkpeering
- name: VirtualNetworkPeeringListResult
  property_count: 2
  slug: microsoft-azure-networking-virtualnetworkpeeringlistresult
json_structures:
- name: Microsoft Azure Networking Structure
  property_count: 0
  slug: microsoft-azure-networking-structure
layout: provider
modified: '2026-05-19'
name: Azure Networking
nav: Providers
network: true
overview: 'Azure Networking publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Backend Address Pools API, Load Balancer Probes API, Load Balancers API, and 5 more. Tagged areas include Azure, Cloud, Infrastructure, Microsoft, and Networking.


  The Azure Networking catalog on APIs.io includes 1 Spectral governance ruleset.


  Azure Networking''s developer surface includes authentication, developer portal, documentation, getting-started guide, Stack Overflow tag, changelog, pricing, and 16 more developer resources.'
plans:
- name: Microsoft Azure Networking Plans Pricing
  plan_count: 11
  slug: microsoft-azure-networking-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 7
  name: Microsoft Azure Networking Rate Limits
  slug: microsoft-azure-networking-rate-limits
rules:
- name: Azure Networking API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-azure-networking-jsonschema-spectral-rules
scopes:
- name: Microsoft Azure Networking Scopes
  scope_count: 1
  slug: microsoft-azure-networking-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 60.5
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 61.6
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 60.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-networking/refs/heads/main/screenshots/microsoft-azure-networking-2026-06-20T185429.png
security:
- kind: authentication
  name: Microsoft Azure Networking Authentication
  slug: microsoft-azure-networking-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Networking Domain Security
  slug: microsoft-azure-networking-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-networking
tags:
- Azure
- Cloud
- Infrastructure
- Microsoft
- Networking
website: https://portal.azure.com
---
