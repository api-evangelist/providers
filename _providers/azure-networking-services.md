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
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Azure Networking Services Agentic Access
  operation_count: 41
  slug: azure-networking-services-agentic-access
  summary_line: 41 operations · 14 acting
api_count: 2
apis:
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The LoadBalancers API from Azure Networking Services — 16 operation(s) for loadbalancers.
  name: Azure Networking Services LoadBalancers API
  slug: azure-networking-services-loadbalancers-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Subnets API from Azure Networking Services — 2 operation(s) for subnets.
  name: Azure Networking Services Subnets API
  slug: azure-networking-services-subnets-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Subscriptions API from Azure Networking Services — 6 operation(s) for subscriptions.
  name: Azure Networking Services Subscriptions API
  slug: azure-networking-services-subscriptions-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The VirtualNetworkPeerings API from Azure Networking Services — 2 operation(s) for virtualnetworkpeerings.
  name: Azure Networking Services VirtualNetworkPeerings API
  slug: azure-networking-services-virtualnetworkpeerings-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The VirtualNetworks API from Azure Networking Services — 3 operation(s) for virtualnetworks.
  name: Azure Networking Services VirtualNetworks API
  slug: azure-networking-services-virtualnetworks-api
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
- baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks
  baseurl_source: declared
  description: Operations for managing backend address pools that define the group of resources to receive load-balanced traffic.
  name: Azure Networking Backend Address Pools API
  slug: microsoft-azure-networking-backend-address-pools-api
- baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks
  baseurl_source: declared
  description: Operations for managing health probes that monitor the health status of backend resources.
  name: Azure Networking Load Balancer Probes API
  slug: microsoft-azure-networking-load-balancer-probes-api
- baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks
  baseurl_source: declared
  description: Operations for creating, updating, deleting, and listing Azure Load Balancer resources.
  name: Azure Networking Load Balancers API
  slug: microsoft-azure-networking-load-balancers-api
- baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks
  baseurl_source: declared
  description: Operations for managing load balancing rules that define how traffic is distributed to backend pool members.
  name: Azure Networking Load Balancing Rules API
  slug: microsoft-azure-networking-load-balancing-rules-api
- baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks
  baseurl_source: declared
  description: Operations operations
  name: Azure Networking Operations API
  slug: microsoft-azure-networking-operations-api
- baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks
  baseurl_source: declared
  description: Operations for managing subnets within a virtual network, including creation, configuration, and delegation.
  name: Azure Networking Subnets API
  slug: microsoft-azure-networking-subnets-api
- baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks
  baseurl_source: declared
  description: Operations for creating and managing peering connections between virtual networks.
  name: Azure Networking Virtual Network Peerings API
  slug: microsoft-azure-networking-virtual-network-peerings-api
- baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks
  baseurl_source: declared
  description: Operations for creating, updating, deleting, and listing Azure Virtual Networks within subscriptions and resource groups.
  name: Azure Networking Virtual Networks API
  slug: microsoft-azure-networking-virtual-networks-api
artifact_total: 215
collections:
- collection_type: postman
  name: NetworkManagementClient LoadBalancers API
  slug: postman-azure-networking-services-loadbalancers-api
- collection_type: postman
  name: NetworkManagementClient LoadBalancers Subnets API
  slug: postman-azure-networking-services-subnets-api
- collection_type: postman
  name: NetworkManagementClient LoadBalancers Subscriptions API
  slug: postman-azure-networking-services-subscriptions-api
- collection_type: postman
  name: NetworkManagementClient LoadBalancers VirtualNetworkPeerings API
  slug: postman-azure-networking-services-virtualnetworkpeerings-api
- collection_type: postman
  name: NetworkManagementClient LoadBalancers VirtualNetworks API
  slug: postman-azure-networking-services-virtualnetworks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NetworkManagementClient LoadBalancers API
  slug: open-azure-networking-services-loadbalancers-api
- collection_type: open
  name: NetworkManagementClient LoadBalancers Subnets API
  slug: open-azure-networking-services-subnets-api
- collection_type: open
  name: NetworkManagementClient LoadBalancers Subscriptions API
  slug: open-azure-networking-services-subscriptions-api
- collection_type: open
  name: NetworkManagementClient LoadBalancers VirtualNetworkPeerings API
  slug: open-azure-networking-services-virtualnetworkpeerings-api
- collection_type: open
  name: NetworkManagementClient LoadBalancers VirtualNetworks API
  slug: open-azure-networking-services-virtualnetworks-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Azure/azure-rest-api-specs/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Azure/azure-rest-api-specs/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Azure/azure-rest-api-specs/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Azure/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Azure/azure-rest-api-specs/blob/main/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Azure/azure-rest-api-specs/blob/main/LICENSE
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/azure-networking-services-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-networking-services/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-networking-services-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-networking-services-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-networking-services-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-networking-services-scopes.yml
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
  url: https://learn.microsoft.com/en-us/azure/networking/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/rest/api/azure/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/azure-networking-services/refs/heads/main/rules/azure-networking-services-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/azure-networking-services/refs/heads/main/vocabulary/azure-networking-services-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/azure-networking-services/refs/heads/main/json-ld/azure-networking-services-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=AzureNetworkingBlog
created: '2024-01-15'
description: A comprehensive collection of Azure networking APIs for managing virtual networks, load balancers, application gateways, VPN gateways, DNS, and other networking resources in the Microsoft Azure cloud.
examples:
- key_count: 1
  name: Azure Networking Services Address Space Example
  slug: azure-networking-services-address-space-example
- key_count: 3
  name: Azure Networking Services Backend Address Pool Example
  slug: azure-networking-services-backend-address-pool-example
- key_count: 5
  name: Azure Networking Services Backend Address Pool Properties Format Example
  slug: azure-networking-services-backend-address-pool-properties-format-example
- key_count: 3
  name: Azure Networking Services Delegation Example
  slug: azure-networking-services-delegation-example
- key_count: 1
  name: Azure Networking Services Dhcp Options Example
  slug: azure-networking-services-dhcp-options-example
- key_count: 4
  name: Azure Networking Services Frontend Ip Configuration Example
  slug: azure-networking-services-frontend-ip-configuration-example
- key_count: 9
  name: Azure Networking Services Frontend Ip Configuration Properties Format Example
  slug: azure-networking-services-frontend-ip-configuration-properties-format-example
- key_count: 3
  name: Azure Networking Services Inbound Nat Pool Example
  slug: azure-networking-services-inbound-nat-pool-example
- key_count: 8
  name: Azure Networking Services Inbound Nat Pool Properties Format Example
  slug: azure-networking-services-inbound-nat-pool-properties-format-example
- key_count: 3
  name: Azure Networking Services Inbound Nat Rule Example
  slug: azure-networking-services-inbound-nat-rule-example
- key_count: 2
  name: Azure Networking Services Inbound Nat Rule List Result Example
  slug: azure-networking-services-inbound-nat-rule-list-result-example
- key_count: 8
  name: Azure Networking Services Inbound Nat Rule Properties Format Example
  slug: azure-networking-services-inbound-nat-rule-properties-format-example
- key_count: 2
  name: Azure Networking Services Ip Address Availability Result Example
  slug: azure-networking-services-ip-address-availability-result-example
- key_count: 2
  name: Azure Networking Services Load Balancer Backend Address Pool List Result Example
  slug: azure-networking-services-load-balancer-backend-address-pool-list-result-example
- key_count: 1
  name: Azure Networking Services Load Balancer Example
  slug: azure-networking-services-load-balancer-example
- key_count: 2
  name: Azure Networking Services Load Balancer Frontend Ip Configuration List Result Example
  slug: azure-networking-services-load-balancer-frontend-ip-configuration-list-result-example
- key_count: 2
  name: Azure Networking Services Load Balancer List Result Example
  slug: azure-networking-services-load-balancer-list-result-example
- key_count: 2
  name: Azure Networking Services Load Balancer Load Balancing Rule List Result Example
  slug: azure-networking-services-load-balancer-load-balancing-rule-list-result-example
- key_count: 2
  name: Azure Networking Services Load Balancer Outbound Rule List Result Example
  slug: azure-networking-services-load-balancer-outbound-rule-list-result-example
- key_count: 2
  name: Azure Networking Services Load Balancer Probe List Result Example
  slug: azure-networking-services-load-balancer-probe-list-result-example
- key_count: 9
  name: Azure Networking Services Load Balancer Properties Format Example
  slug: azure-networking-services-load-balancer-properties-format-example
- key_count: 1
  name: Azure Networking Services Load Balancer Sku Example
  slug: azure-networking-services-load-balancer-sku-example
- key_count: 3
  name: Azure Networking Services Load Balancing Rule Example
  slug: azure-networking-services-load-balancing-rule-example
- key_count: 11
  name: Azure Networking Services Load Balancing Rule Properties Format Example
  slug: azure-networking-services-load-balancing-rule-properties-format-example
- key_count: 1
  name: Azure Networking Services Network Intent Policy Configuration Example
  slug: azure-networking-services-network-intent-policy-configuration-example
- key_count: 1
  name: Azure Networking Services Network Intent Policy Example
  slug: azure-networking-services-network-intent-policy-example
- key_count: 0
  name: Azure Networking Services Network Interface Properties Format Example
  slug: azure-networking-services-network-interface-properties-format-example
- key_count: 3
  name: Azure Networking Services Outbound Rule Example
  slug: azure-networking-services-outbound-rule-example
- key_count: 7
  name: Azure Networking Services Outbound Rule Properties Format Example
  slug: azure-networking-services-outbound-rule-properties-format-example
- key_count: 2
  name: Azure Networking Services Prepare Network Policies Request Example
  slug: azure-networking-services-prepare-network-policies-request-example
- key_count: 3
  name: Azure Networking Services Probe Example
  slug: azure-networking-services-probe-example
- key_count: 7
  name: Azure Networking Services Probe Properties Format Example
  slug: azure-networking-services-probe-properties-format-example
- key_count: 5
  name: Azure Networking Services Resource Navigation Link Example
  slug: azure-networking-services-resource-navigation-link-example
- key_count: 3
  name: Azure Networking Services Resource Navigation Link Format Example
  slug: azure-networking-services-resource-navigation-link-format-example
- key_count: 2
  name: Azure Networking Services Resource Navigation Links List Result Example
  slug: azure-networking-services-resource-navigation-links-list-result-example
- key_count: 4
  name: Azure Networking Services Service Association Link Example
  slug: azure-networking-services-service-association-link-example
- key_count: 5
  name: Azure Networking Services Service Association Link Properties Format Example
  slug: azure-networking-services-service-association-link-properties-format-example
- key_count: 2
  name: Azure Networking Services Service Association Links List Result Example
  slug: azure-networking-services-service-association-links-list-result-example
- key_count: 3
  name: Azure Networking Services Service Delegation Properties Format Example
  slug: azure-networking-services-service-delegation-properties-format-example
- key_count: 3
  name: Azure Networking Services Service Endpoint Properties Format Example
  slug: azure-networking-services-service-endpoint-properties-format-example
- key_count: 2
  name: Azure Networking Services Subnet Example
  slug: azure-networking-services-subnet-example
- key_count: 2
  name: Azure Networking Services Subnet List Result Example
  slug: azure-networking-services-subnet-list-result-example
- key_count: 15
  name: Azure Networking Services Subnet Properties Format Example
  slug: azure-networking-services-subnet-properties-format-example
- key_count: 1
  name: Azure Networking Services Unprepare Network Policies Request Example
  slug: azure-networking-services-unprepare-network-policies-request-example
- key_count: 2
  name: Azure Networking Services Virtual Network Bgp Communities Example
  slug: azure-networking-services-virtual-network-bgp-communities-example
- key_count: 1
  name: Azure Networking Services Virtual Network Example
  slug: azure-networking-services-virtual-network-example
- key_count: 2
  name: Azure Networking Services Virtual Network List Result Example
  slug: azure-networking-services-virtual-network-list-result-example
- key_count: 2
  name: Azure Networking Services Virtual Network List Usage Result Example
  slug: azure-networking-services-virtual-network-list-usage-result-example
- key_count: 2
  name: Azure Networking Services Virtual Network Peering Example
  slug: azure-networking-services-virtual-network-peering-example
- key_count: 2
  name: Azure Networking Services Virtual Network Peering List Result Example
  slug: azure-networking-services-virtual-network-peering-list-result-example
- key_count: 7
  name: Azure Networking Services Virtual Network Peering Properties Format Example
  slug: azure-networking-services-virtual-network-peering-properties-format-example
- key_count: 7
  name: Azure Networking Services Virtual Network Properties Format Example
  slug: azure-networking-services-virtual-network-properties-format-example
- key_count: 4
  name: Azure Networking Services Virtual Network Usage Example
  slug: azure-networking-services-virtual-network-usage-example
- key_count: 2
  name: Azure Networking Services Virtual Network Usage Name Example
  slug: azure-networking-services-virtual-network-usage-name-example
finops:
- name: Azure Networking Services Finops
  service_category: API
  slug: azure-networking-services-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-networking-services.png
json_schemas:
- name: AddressSpace
  property_count: 1
  slug: azure-networking-services-address-space
- name: BackendAddressPoolPropertiesFormat
  property_count: 5
  slug: azure-networking-services-backend-address-pool-properties-format
- name: BackendAddressPool
  property_count: 4
  slug: azure-networking-services-backend-address-pool
- name: Delegation
  property_count: 3
  slug: azure-networking-services-delegation
- name: DhcpOptions
  property_count: 1
  slug: azure-networking-services-dhcp-options
- name: FrontendIPConfigurationPropertiesFormat
  property_count: 11
  slug: azure-networking-services-frontend-ip-configuration-properties-format
- name: FrontendIPConfiguration
  property_count: 5
  slug: azure-networking-services-frontend-ip-configuration
- name: InboundNatPoolPropertiesFormat
  property_count: 9
  slug: azure-networking-services-inbound-nat-pool-properties-format
- name: InboundNatPool
  property_count: 4
  slug: azure-networking-services-inbound-nat-pool
- name: InboundNatRuleListResult
  property_count: 2
  slug: azure-networking-services-inbound-nat-rule-list-result
- name: InboundNatRulePropertiesFormat
  property_count: 9
  slug: azure-networking-services-inbound-nat-rule-properties-format
- name: InboundNatRule
  property_count: 4
  slug: azure-networking-services-inbound-nat-rule
- name: IPAddressAvailabilityResult
  property_count: 2
  slug: azure-networking-services-ip-address-availability-result
- name: LoadBalancerBackendAddressPoolListResult
  property_count: 2
  slug: azure-networking-services-load-balancer-backend-address-pool-list-result
- name: LoadBalancerFrontendIPConfigurationListResult
  property_count: 2
  slug: azure-networking-services-load-balancer-frontend-ip-configuration-list-result
- name: LoadBalancerListResult
  property_count: 2
  slug: azure-networking-services-load-balancer-list-result
- name: LoadBalancerLoadBalancingRuleListResult
  property_count: 2
  slug: azure-networking-services-load-balancer-load-balancing-rule-list-result
- name: LoadBalancerOutboundRuleListResult
  property_count: 2
  slug: azure-networking-services-load-balancer-outbound-rule-list-result
- name: LoadBalancerProbeListResult
  property_count: 2
  slug: azure-networking-services-load-balancer-probe-list-result
- name: LoadBalancerPropertiesFormat
  property_count: 9
  slug: azure-networking-services-load-balancer-properties-format
- name: LoadBalancer
  property_count: 3
  slug: azure-networking-services-load-balancer
- name: LoadBalancerSku
  property_count: 1
  slug: azure-networking-services-load-balancer-sku
- name: LoadBalancingRulePropertiesFormat
  property_count: 12
  slug: azure-networking-services-load-balancing-rule-properties-format
- name: LoadBalancingRule
  property_count: 4
  slug: azure-networking-services-load-balancing-rule
- name: NetworkIntentPolicyConfiguration
  property_count: 2
  slug: azure-networking-services-network-intent-policy-configuration
- name: NetworkIntentPolicy
  property_count: 1
  slug: azure-networking-services-network-intent-policy
- name: NetworkInterfacePropertiesFormat
  property_count: 0
  slug: azure-networking-services-network-interface-properties-format
- name: OutboundRulePropertiesFormat
  property_count: 7
  slug: azure-networking-services-outbound-rule-properties-format
- name: OutboundRule
  property_count: 4
  slug: azure-networking-services-outbound-rule
- name: PrepareNetworkPoliciesRequest
  property_count: 2
  slug: azure-networking-services-prepare-network-policies-request
- name: ProbePropertiesFormat
  property_count: 7
  slug: azure-networking-services-probe-properties-format
- name: Probe
  property_count: 4
  slug: azure-networking-services-probe
- name: ResourceNavigationLinkFormat
  property_count: 3
  slug: azure-networking-services-resource-navigation-link-format
- name: ResourceNavigationLink
  property_count: 5
  slug: azure-networking-services-resource-navigation-link
- name: ResourceNavigationLinksListResult
  property_count: 2
  slug: azure-networking-services-resource-navigation-links-list-result
- name: ServiceAssociationLinkPropertiesFormat
  property_count: 5
  slug: azure-networking-services-service-association-link-properties-format
- name: ServiceAssociationLink
  property_count: 4
  slug: azure-networking-services-service-association-link
- name: ServiceAssociationLinksListResult
  property_count: 2
  slug: azure-networking-services-service-association-links-list-result
- name: ServiceDelegationPropertiesFormat
  property_count: 3
  slug: azure-networking-services-service-delegation-properties-format
- name: ServiceEndpointPropertiesFormat
  property_count: 3
  slug: azure-networking-services-service-endpoint-properties-format
- name: SubnetListResult
  property_count: 2
  slug: azure-networking-services-subnet-list-result
- name: SubnetPropertiesFormat
  property_count: 17
  slug: azure-networking-services-subnet-properties-format
- name: Subnet
  property_count: 3
  slug: azure-networking-services-subnet
- name: TransportProtocol
  property_count: 0
  slug: azure-networking-services-transport-protocol
- name: UnprepareNetworkPoliciesRequest
  property_count: 1
  slug: azure-networking-services-unprepare-network-policies-request
- name: VirtualNetworkBgpCommunities
  property_count: 2
  slug: azure-networking-services-virtual-network-bgp-communities
- name: VirtualNetworkListResult
  property_count: 2
  slug: azure-networking-services-virtual-network-list-result
- name: VirtualNetworkListUsageResult
  property_count: 2
  slug: azure-networking-services-virtual-network-list-usage-result
- name: VirtualNetworkPeeringListResult
  property_count: 2
  slug: azure-networking-services-virtual-network-peering-list-result
- name: VirtualNetworkPeeringPropertiesFormat
  property_count: 8
  slug: azure-networking-services-virtual-network-peering-properties-format
- name: VirtualNetworkPeering
  property_count: 3
  slug: azure-networking-services-virtual-network-peering
- name: VirtualNetworkPropertiesFormat
  property_count: 10
  slug: azure-networking-services-virtual-network-properties-format
- name: VirtualNetwork
  property_count: 2
  slug: azure-networking-services-virtual-network
- name: VirtualNetworkUsageName
  property_count: 2
  slug: azure-networking-services-virtual-network-usage-name
- name: VirtualNetworkUsage
  property_count: 5
  slug: azure-networking-services-virtual-network-usage
json_structures:
- name: Azure Networking Services Address Space Structure
  property_count: 1
  slug: azure-networking-services-address-space-structure
- name: Azure Networking Services Backend Address Pool Properties Format Structure
  property_count: 5
  slug: azure-networking-services-backend-address-pool-properties-format-structure
- name: Azure Networking Services Backend Address Pool Structure
  property_count: 4
  slug: azure-networking-services-backend-address-pool-structure
- name: Azure Networking Services Delegation Structure
  property_count: 3
  slug: azure-networking-services-delegation-structure
- name: Azure Networking Services Dhcp Options Structure
  property_count: 1
  slug: azure-networking-services-dhcp-options-structure
- name: Azure Networking Services Frontend Ip Configuration Properties Format Structure
  property_count: 11
  slug: azure-networking-services-frontend-ip-configuration-properties-format-structure
- name: Azure Networking Services Frontend Ip Configuration Structure
  property_count: 5
  slug: azure-networking-services-frontend-ip-configuration-structure
- name: Azure Networking Services Inbound Nat Pool Properties Format Structure
  property_count: 9
  slug: azure-networking-services-inbound-nat-pool-properties-format-structure
- name: Azure Networking Services Inbound Nat Pool Structure
  property_count: 4
  slug: azure-networking-services-inbound-nat-pool-structure
- name: Azure Networking Services Inbound Nat Rule List Result Structure
  property_count: 2
  slug: azure-networking-services-inbound-nat-rule-list-result-structure
- name: Azure Networking Services Inbound Nat Rule Properties Format Structure
  property_count: 9
  slug: azure-networking-services-inbound-nat-rule-properties-format-structure
- name: Azure Networking Services Inbound Nat Rule Structure
  property_count: 4
  slug: azure-networking-services-inbound-nat-rule-structure
- name: Azure Networking Services Ip Address Availability Result Structure
  property_count: 2
  slug: azure-networking-services-ip-address-availability-result-structure
- name: Azure Networking Services Load Balancer Backend Address Pool List Result Structure
  property_count: 2
  slug: azure-networking-services-load-balancer-backend-address-pool-list-result-structure
- name: Azure Networking Services Load Balancer Frontend Ip Configuration List Result Structure
  property_count: 2
  slug: azure-networking-services-load-balancer-frontend-ip-configuration-list-result-structure
- name: Azure Networking Services Load Balancer List Result Structure
  property_count: 2
  slug: azure-networking-services-load-balancer-list-result-structure
- name: Azure Networking Services Load Balancer Load Balancing Rule List Result Structure
  property_count: 2
  slug: azure-networking-services-load-balancer-load-balancing-rule-list-result-structure
- name: Azure Networking Services Load Balancer Outbound Rule List Result Structure
  property_count: 2
  slug: azure-networking-services-load-balancer-outbound-rule-list-result-structure
- name: Azure Networking Services Load Balancer Probe List Result Structure
  property_count: 2
  slug: azure-networking-services-load-balancer-probe-list-result-structure
- name: Azure Networking Services Load Balancer Properties Format Structure
  property_count: 9
  slug: azure-networking-services-load-balancer-properties-format-structure
- name: Azure Networking Services Load Balancer Sku Structure
  property_count: 1
  slug: azure-networking-services-load-balancer-sku-structure
- name: Azure Networking Services Load Balancer Structure
  property_count: 3
  slug: azure-networking-services-load-balancer-structure
- name: Azure Networking Services Load Balancing Rule Properties Format Structure
  property_count: 12
  slug: azure-networking-services-load-balancing-rule-properties-format-structure
- name: Azure Networking Services Load Balancing Rule Structure
  property_count: 4
  slug: azure-networking-services-load-balancing-rule-structure
- name: Azure Networking Services Network Intent Policy Configuration Structure
  property_count: 2
  slug: azure-networking-services-network-intent-policy-configuration-structure
- name: Azure Networking Services Network Intent Policy Structure
  property_count: 1
  slug: azure-networking-services-network-intent-policy-structure
- name: Azure Networking Services Network Interface Properties Format Structure
  property_count: 0
  slug: azure-networking-services-network-interface-properties-format-structure
- name: Azure Networking Services Outbound Rule Properties Format Structure
  property_count: 7
  slug: azure-networking-services-outbound-rule-properties-format-structure
- name: Azure Networking Services Outbound Rule Structure
  property_count: 4
  slug: azure-networking-services-outbound-rule-structure
- name: Azure Networking Services Prepare Network Policies Request Structure
  property_count: 2
  slug: azure-networking-services-prepare-network-policies-request-structure
- name: Azure Networking Services Probe Properties Format Structure
  property_count: 7
  slug: azure-networking-services-probe-properties-format-structure
- name: Azure Networking Services Probe Structure
  property_count: 4
  slug: azure-networking-services-probe-structure
- name: Azure Networking Services Resource Navigation Link Format Structure
  property_count: 3
  slug: azure-networking-services-resource-navigation-link-format-structure
- name: Azure Networking Services Resource Navigation Link Structure
  property_count: 5
  slug: azure-networking-services-resource-navigation-link-structure
- name: Azure Networking Services Resource Navigation Links List Result Structure
  property_count: 2
  slug: azure-networking-services-resource-navigation-links-list-result-structure
- name: Azure Networking Services Service Association Link Properties Format Structure
  property_count: 5
  slug: azure-networking-services-service-association-link-properties-format-structure
- name: Azure Networking Services Service Association Link Structure
  property_count: 4
  slug: azure-networking-services-service-association-link-structure
- name: Azure Networking Services Service Association Links List Result Structure
  property_count: 2
  slug: azure-networking-services-service-association-links-list-result-structure
- name: Azure Networking Services Service Delegation Properties Format Structure
  property_count: 3
  slug: azure-networking-services-service-delegation-properties-format-structure
- name: Azure Networking Services Service Endpoint Properties Format Structure
  property_count: 3
  slug: azure-networking-services-service-endpoint-properties-format-structure
- name: Azure Networking Services Subnet List Result Structure
  property_count: 2
  slug: azure-networking-services-subnet-list-result-structure
- name: Azure Networking Services Subnet Properties Format Structure
  property_count: 17
  slug: azure-networking-services-subnet-properties-format-structure
- name: Azure Networking Services Subnet Structure
  property_count: 3
  slug: azure-networking-services-subnet-structure
- name: Azure Networking Services Transport Protocol Structure
  property_count: 0
  slug: azure-networking-services-transport-protocol-structure
- name: Azure Networking Services Unprepare Network Policies Request Structure
  property_count: 1
  slug: azure-networking-services-unprepare-network-policies-request-structure
- name: Azure Networking Services Virtual Network Bgp Communities Structure
  property_count: 2
  slug: azure-networking-services-virtual-network-bgp-communities-structure
- name: Azure Networking Services Virtual Network List Result Structure
  property_count: 2
  slug: azure-networking-services-virtual-network-list-result-structure
- name: Azure Networking Services Virtual Network List Usage Result Structure
  property_count: 2
  slug: azure-networking-services-virtual-network-list-usage-result-structure
- name: Azure Networking Services Virtual Network Peering List Result Structure
  property_count: 2
  slug: azure-networking-services-virtual-network-peering-list-result-structure
- name: Azure Networking Services Virtual Network Peering Properties Format Structure
  property_count: 8
  slug: azure-networking-services-virtual-network-peering-properties-format-structure
- name: Azure Networking Services Virtual Network Peering Structure
  property_count: 3
  slug: azure-networking-services-virtual-network-peering-structure
- name: Azure Networking Services Virtual Network Properties Format Structure
  property_count: 10
  slug: azure-networking-services-virtual-network-properties-format-structure
- name: Azure Networking Services Virtual Network Structure
  property_count: 2
  slug: azure-networking-services-virtual-network-structure
- name: Azure Networking Services Virtual Network Usage Name Structure
  property_count: 2
  slug: azure-networking-services-virtual-network-usage-name-structure
- name: Azure Networking Services Virtual Network Usage Structure
  property_count: 5
  slug: azure-networking-services-virtual-network-usage-structure
jsonld:
- class_count: 21
  name: Azure Networking Services Context
  property_count: 36
  slug: azure-networking-services-context
layout: provider
modified: '2026-05-19'
name: Azure Networking Services
nav: Providers
network: true
overview: 'Azure Networking Services publishes 13 APIs on the [APIs.io](https://apis.io/) network, including LoadBalancers API, Subnets API, Subscriptions API, and 10 more. Tagged areas include Azure, Cloud, Infrastructure, Microsoft, and Networking.


  The Azure Networking Services catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Azure Networking Services'' developer surface includes Stack Overflow tag, changelog, pricing, signup flow, authentication, developer portal, documentation, and 32 more developer resources.'
plans:
- name: Azure Networking Services Plans Pricing
  plan_count: 3
  slug: azure-networking-services-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Azure Networking Services Rate Limits
  slug: azure-networking-services-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Azure Networking Services API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: azure-networking-services-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Azure Networking Services API Rules
  rule_count: 18
  severity_counts:
    error: 5
    hint: 0
    info: 4
    warn: 9
  slug: azure-networking-services-spectral-rules
scopes:
- name: Azure Networking Services Scopes
  scope_count: 1
  slug: azure-networking-services-scopes
  summary_line: 1 scope · implicit
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-networking-services/refs/heads/main/screenshots/azure-networking-services-2026-06-20T172903.png
security:
- kind: authentication
  name: Azure Networking Services Authentication
  slug: azure-networking-services-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Azure Networking Services Domain Security
  slug: azure-networking-services-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azure-networking-services
tags:
- Azure
- Cloud
- Infrastructure
- Microsoft
- Networking
website: https://www.microsoft.com/
---
