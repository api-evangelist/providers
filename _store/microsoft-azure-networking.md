---
name: Azure Networking
description: A collection of Azure Networking APIs for managing virtual networks, load balancers, application gateways, and network security.
image: https://azure.microsoft.com/svghandler/azure-networking.svg
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - Azure
  - Cloud
  - Infrastructure
  - Microsoft
  - Networking
apis:
  - name: Azure Virtual Networks API
    description: Manage Azure Virtual Networks (VNets) including subnets, peering, and network configurations.
    image: https://azure.microsoft.com/svghandler/virtual-network.svg
    humanURL: https://azure.microsoft.com/en-us/services/virtual-network/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks
    tags:
      - Peering
      - Subnets
      - Virtual Networks
      - Vnet
    properties:
      - type: X-documentation
        url: https://docs.microsoft.com/en-us/rest/api/virtualnetwork/
      - type: X-openapi
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/network/resource-manager/Microsoft.Network/stable/2023-05-01/virtualNetwork.json
      - type: X-pricing
        url: https://azure.microsoft.com/en-us/pricing/details/virtual-network/
      - type: X-authentication
        url: https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/virtual-network/quickstart-create-virtual-network
  - name: Azure Load Balancer API
    description: Distribute traffic across multiple virtual machines and services with Azure Load Balancer.
    image: https://azure.microsoft.com/svghandler/load-balancer.svg
    humanURL: https://azure.microsoft.com/en-us/services/load-balancer/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers
    tags:
      - High Availability
      - Load Balancer
      - Traffic Distribution
    properties:
      - type: X-documentation
        url: https://docs.microsoft.com/en-us/rest/api/load-balancer/
      - type: X-openapi
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/network/resource-manager/Microsoft.Network/stable/2023-05-01/loadBalancer.json
      - type: X-pricing
        url: https://azure.microsoft.com/en-us/pricing/details/load-balancer/
      - type: X-authentication
        url: https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/load-balancer/
  - name: Azure Application Gateway API
    description: Web traffic load balancer with application-level routing and SSL termination.
    image: https://azure.microsoft.com/svghandler/application-gateway.svg
    humanURL: https://azure.microsoft.com/en-us/services/application-gateway/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways
    tags:
      - Application Gateway
      - Layer 7 Load Balancing
      - Ssl Termination
      - Web Application Firewall
    properties:
      - type: X-documentation
        url: https://docs.microsoft.com/en-us/rest/api/application-gateway/
      - type: X-openapi
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/network/resource-manager/Microsoft.Network/stable/2023-05-01/applicationGateway.json
      - type: X-pricing
        url: https://azure.microsoft.com/en-us/pricing/details/application-gateway/
      - type: X-authentication
        url: https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/application-gateway/
  - name: Azure Network Security Groups API
    description: Control network traffic to and from Azure resources with security rules.
    image: https://azure.microsoft.com/svghandler/network-security-groups.svg
    humanURL: https://azure.microsoft.com/en-us/services/network-security-groups/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityGroups
    tags:
      - Firewall
      - Network Security Groups
      - Nsg
      - Security
    properties:
      - type: X-documentation
        url: https://docs.microsoft.com/en-us/rest/api/virtualnetwork/networksecuritygroups
      - type: X-openapi
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/network/resource-manager/Microsoft.Network/stable/2023-05-01/networkSecurityGroup.json
      - type: X-pricing
        url: https://azure.microsoft.com/en-us/pricing/details/virtual-network/
      - type: X-authentication
        url: https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/networksecuritygroups
  - name: Azure VPN Gateway API
    description: Establish secure cross-premises connectivity between Azure and on-premises networks.
    image: https://azure.microsoft.com/svghandler/vpn-gateway.svg
    humanURL: https://azure.microsoft.com/en-us/services/vpn-gateway/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways
    tags:
      - Gateway
      - Hybrid Connectivity
      - Site-To-Site
      - Vpn
    properties:
      - type: X-documentation
        url: https://docs.microsoft.com/en-us/rest/api/network-gateway/
      - type: X-openapi
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/network/resource-manager/Microsoft.Network/stable/2023-05-01/virtualNetworkGateway.json
      - type: X-pricing
        url: https://azure.microsoft.com/en-us/pricing/details/vpn-gateway/
      - type: X-authentication
        url: https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/network-gateway/
  - name: Azure Traffic Manager API
    description: DNS-based traffic load balancer for distributing traffic globally.
    image: https://azure.microsoft.com/svghandler/traffic-manager.svg
    humanURL: https://azure.microsoft.com/en-us/services/traffic-manager/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles
    tags:
      - Dns
      - Failover
      - Global Load Balancing
      - Traffic Manager
    properties:
      - type: X-documentation
        url: https://docs.microsoft.com/en-us/rest/api/trafficmanager/
      - type: X-openapi
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/trafficmanager/resource-manager/Microsoft.Network/stable/2022-04-01/trafficmanager.json
      - type: X-pricing
        url: https://azure.microsoft.com/en-us/pricing/details/traffic-manager/
      - type: X-authentication
        url: https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/trafficmanager/
  - name: Azure ExpressRoute API
    description: Create private connections between Azure datacenters and on-premises infrastructure.
    image: https://azure.microsoft.com/svghandler/expressroute.svg
    humanURL: https://azure.microsoft.com/en-us/services/expressroute/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits
    tags:
      - Dedicated Connection
      - Expressroute
      - Hybrid
      - Private Connectivity
    properties:
      - type: X-documentation
        url: https://docs.microsoft.com/en-us/rest/api/expressroute/
      - type: X-openapi
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/network/resource-manager/Microsoft.Network/stable/2023-05-01/expressRouteCircuit.json
      - type: X-pricing
        url: https://azure.microsoft.com/en-us/pricing/details/expressroute/
      - type: X-authentication
        url: https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/expressroute/
  - name: Azure Firewall API
    description: Cloud-native network security service with built-in high availability.
    image: https://azure.microsoft.com/svghandler/azure-firewall.svg
    humanURL: https://azure.microsoft.com/en-us/services/azure-firewall/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/azureFirewalls
    tags:
      - Firewall
      - Network Security
      - Security
      - Threat Protection
    properties:
      - type: X-documentation
        url: https://docs.microsoft.com/en-us/rest/api/firewall/
      - type: X-openapi
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/network/resource-manager/Microsoft.Network/stable/2023-05-01/azureFirewall.json
      - type: X-pricing
        url: https://azure.microsoft.com/en-us/pricing/details/azure-firewall/
      - type: X-authentication
        url: https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/firewall/
  - name: Azure DNS API
    description: Host DNS zones and manage DNS records using the Azure DNS REST API. Supports creating, updating, and deleting public DNS zones and record sets for domain name resolution within Azure-managed infrastructure.
    image: https://azure.microsoft.com/svghandler/azure-networking.svg
    humanURL: https://learn.microsoft.com/en-us/azure/dns/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones
    tags:
      - DNS
      - Domain Name System
      - Records
      - Zones
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/dns/
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/dns/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
  - name: Azure Private DNS API
    description: Manage private DNS zones for name resolution within Azure virtual networks. Azure Private DNS provides a reliable and secure DNS service to manage and resolve domain names in a virtual network without needing a custom DNS solution.
    image: https://azure.microsoft.com/svghandler/azure-networking.svg
    humanURL: https://learn.microsoft.com/en-us/azure/dns/private-dns-overview
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones
    tags:
      - DNS
      - Name Resolution
      - Private DNS
      - Virtual Networks
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/dns/privatedns/private-zones
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
  - name: Azure Front Door API
    description: Global load balancer and application delivery network that provides fast, reliable, and secure access to web applications. Azure Front Door offers layer 7 load balancing, SSL offload, URL-based routing, and Web Application Firewall integration.
    image: https://azure.microsoft.com/svghandler/azure-networking.svg
    humanURL: https://learn.microsoft.com/en-us/azure/frontdoor/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors
    tags:
      - CDN
      - Front Door
      - Global Load Balancing
      - Web Application Firewall
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/frontdoor/
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/frontdoor/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
  - name: Azure DDoS Protection API
    description: Manage DDoS protection plans that provide enhanced DDoS mitigation capabilities for Azure Virtual Network resources. Azure DDoS Protection provides countermeasures against sophisticated DDoS threats with adaptive tuning, attack analytics, and alerting.
    image: https://azure.microsoft.com/svghandler/azure-networking.svg
    humanURL: https://learn.microsoft.com/en-us/azure/ddos-protection/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ddosProtectionPlans
    tags:
      - DDoS Protection
      - Network Security
      - Security
      - Threat Mitigation
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/ddos-protection-plans
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/ddos-protection/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
  - name: Azure Network Watcher API
    description: Monitor, diagnose, and gain insights into network performance and health in Azure. Network Watcher provides tools for packet capture, connection troubleshooting, NSG flow logs, and network topology visualization.
    image: https://azure.microsoft.com/svghandler/azure-networking.svg
    humanURL: https://learn.microsoft.com/en-us/azure/network-watcher/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers
    tags:
      - Diagnostics
      - Flow Logs
      - Network Monitoring
      - Packet Capture
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/network-watcher/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
  - name: Azure Bastion API
    description: Fully managed PaaS service that provides secure and seamless RDP and SSH connectivity to virtual machines directly through the Azure portal over TLS. Azure Bastion is deployed inside a virtual network and does not require a public IP on the target VM.
    image: https://azure.microsoft.com/svghandler/azure-networking.svg
    humanURL: https://learn.microsoft.com/en-us/azure/bastion/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/bastionHosts
    tags:
      - Bastion
      - RDP
      - Remote Access
      - Secure Connectivity
      - SSH
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/bastion-hosts
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/azure-bastion/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
  - name: Azure NAT Gateway API
    description: Simplify outbound-only internet connectivity for virtual networks. When configured on a subnet, all outbound connectivity uses specified static public IP addresses. NAT Gateway provides on-demand SNAT port allocation without the need for a load balancer or directly attached public IPs.
    image: https://azure.microsoft.com/svghandler/azure-networking.svg
    humanURL: https://learn.microsoft.com/en-us/azure/nat-gateway/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/natGateways
    tags:
      - IP Address Management
      - NAT Gateway
      - Outbound Connectivity
      - SNAT
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/nat-gateways
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/azure-nat-gateway/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
  - name: Azure Private Link API
    description: Access Azure PaaS services and customer-owned services over a private endpoint in your virtual network. Azure Private Link eliminates data exposure to the public internet by keeping traffic on the Microsoft global network.
    image: https://azure.microsoft.com/svghandler/azure-networking.svg
    humanURL: https://learn.microsoft.com/en-us/azure/private-link/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateLinkServices
    tags:
      - Network Isolation
      - Private Endpoint
      - Private Link
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/private-link-services
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/private-link/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
  - name: Azure Virtual WAN API
    description: Networking service that provides optimized and automated branch-to-branch connectivity through Azure. Virtual WAN brings together networking, security, and routing functionalities into a single operational interface including VPN, ExpressRoute, and point-to-site connectivity.
    image: https://azure.microsoft.com/svghandler/azure-networking.svg
    humanURL: https://learn.microsoft.com/en-us/azure/virtual-wan/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans
    tags:
      - Branch Connectivity
      - Hybrid Networking
      - SD-WAN
      - Virtual WAN
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/virtualwan/
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/virtual-wan/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
  - name: Azure Web Application Firewall API
    description: Cloud-native web application firewall service that provides centralized protection for web applications from common exploits and vulnerabilities. Azure WAF can be deployed with Application Gateway, Front Door, and CDN for layer 7 protection.
    image: https://azure.microsoft.com/svghandler/azure-networking.svg
    humanURL: https://learn.microsoft.com/en-us/azure/web-application-firewall/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ApplicationGatewayWebApplicationFirewallPolicies
    tags:
      - Application Protection
      - Security
      - WAF
      - Web Application Firewall
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/application-gateway/web-application-firewall-policies
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/web-application-firewall/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
common:
  - type: X-portal
    url: https://portal.azure.com
  - type: X-support
    url: https://azure.microsoft.com/en-us/support/
  - type: X-status
    url: https://status.azure.com/
  - type: X-blog
    url: https://azure.microsoft.com/en-us/blog/topics/networking/
  - type: X-terms-of-service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Portal
    url: https://portal.azure.com
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/networking/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/networking/fundamentals/networking-overview
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: SDKs
    url: https://learn.microsoft.com/en-us/azure/developer/
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: GitHubRepository
    url: https://github.com/Azure/azure-rest-api-specs
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/azure-virtual-network
  - type: Change Log
    url: https://azure.microsoft.com/en-us/updates/?query=networking
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/free/
  - type: Login
    url: https://portal.azure.com/#home
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://azure.microsoft.com
---
