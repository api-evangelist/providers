---
name: Azure Load Balancer
description: Azure Load Balancer is a high-performance, low-latency layer-4 load balancing service for distributing inbound and outbound network traffic across virtual machines and other Azure resources. It supports public and internal load balancers, health probes, NAT rules, and HA scenarios.
image: https://azure.microsoft.com/svghandler/load-balancer/
url: https://azure.microsoft.com/en-us/services/load-balancer/
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - Azure
  - High Availability
  - Layer 4
  - Load Balancing
  - Network
apis:
  - name: Azure Load Balancer REST API
    description: Azure Load Balancer REST API provides management of layer-4 load balancers for distributing network traffic across virtual machines. It supports configuring frontend IPs, backend pools, health probes, load balancing rules, and inbound NAT rules.
    image: https://azure.microsoft.com/svghandler/load-balancer/
    humanURL: https://learn.microsoft.com/en-us/rest/api/load-balancer/
    baseURL: https://management.azure.com
    tags:
      - High Availability
      - Layer 4
      - Load Balancing
      - Network
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/load-balancer/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/load-balancer/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/rest/api/azure/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-portal
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/load-balancer/
      - type: SDK
        url: https://learn.microsoft.com/en-us/python/api/overview/azure/network
        title: Python SDK
      - type: SDK
        url: https://learn.microsoft.com/en-us/dotnet/api/overview/azure/resourcemanager.network-readme
        title: .NET SDK
    contact:
      - type: Support
        url: https://azure.microsoft.com/en-us/support/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/load-balancer/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/load-balancer/
  - type: StatusPage
    url: https://status.azure.com/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: TermsOfService
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Features
    data:
      - name: Layer-4 Load Balancing
        description: Distribute TCP and UDP traffic across virtual machines and resources with high performance and low latency.
      - name: Public and Internal Load Balancers
        description: Support both public-facing and internal load balancing scenarios for diverse network architectures.
      - name: Health Probes
        description: Monitor backend instance health with configurable TCP, HTTP, and HTTPS probes for automatic failover.
      - name: NAT Rules
        description: Configure inbound NAT rules to forward traffic to specific backend instances on designated ports.
      - name: High Availability Ports
        description: Load balance all TCP and UDP flows on all ports simultaneously for network virtual appliance scenarios.
      - name: Cross-Region Load Balancing
        description: Distribute traffic across Azure regions for global high availability and disaster recovery.
  - type: UseCases
    data:
      - name: Web Application High Availability
        description: Distribute traffic across multiple web servers for improved reliability and uptime.
      - name: VM Scale Set Load Balancing
        description: Automatically balance traffic across virtual machine scale sets with auto-scaling capabilities.
      - name: Network Virtual Appliance Distribution
        description: Distribute traffic across multiple firewall or NVA instances using HA ports.
  - type: Integrations
    data:
      - name: Azure Virtual Machines
        description: Distribute network traffic across pools of Azure virtual machines.
      - name: Azure Virtual Machine Scale Sets
        description: Integrate with VMSS for automatic scaling and load distribution.
      - name: Azure Monitor
        description: Monitor load balancer health, performance metrics, and diagnostic logs.
---
