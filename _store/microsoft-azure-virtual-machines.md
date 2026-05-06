---
name: Azure Virtual Machines
description: Azure Virtual Machines (VMs) is one of several types of on-demand, scalable computing resources that Azure offers. VMs give you the flexibility of virtualization without having to buy and maintain physical hardware.
image: https://azure.microsoft.com/svghandler/virtual-machines/
tags:
  - Cloud Computing
  - Compute
  - IaaS
  - Infrastructure
  - Virtual Machines
created: '2024-01-20'
modified: '2026-04-28'
url: https://azure.microsoft.com/en-us/services/virtual-machines/
specificationVersion: '0.18'
apis:
  - name: Azure Virtual Machines REST API
    description: REST API for creating and managing Azure Virtual Machines. Provides operations for provisioning, starting, stopping, deallocating, restarting, reimaging, capturing, and deleting virtual machines, as well as managing data disks, extensions, patching, and run commands.
    image: https://azure.microsoft.com/svghandler/virtual-machines/
    humanURL: https://learn.microsoft.com/en-us/azure/virtual-machines/
    baseURL: https://management.azure.com
    tags:
      - Compute
      - REST API
      - Virtual Machines
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/compute/virtual-machines
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2023-09-01/virtualMachines.json
      - type: Swagger
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2023-09-01/virtualMachines.json
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/virtual-machines/
      - type: SLA
        url: https://azure.microsoft.com/en-us/support/legal/sla/virtual-machines/
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/virtual-machines/overview
      - type: Tutorials
        url: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/tutorial-manage-vm
      - type: SDKs
        url: https://azure.microsoft.com/en-us/downloads/
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/compute/virtual-machines?view=rest-compute-2025-04-01
      - type: Authentication
        url: https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-managed-identities-work-vm
      - type: Quickstart
        url: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli
      - type: Rate Limits
        url: https://learn.microsoft.com/en-us/azure/virtual-machines/quotas
      - type: SDK - Python
        url: https://learn.microsoft.com/en-us/python/api/overview/azure/compute
      - type: SDK - .NET
        url: https://www.nuget.org/packages/Microsoft.Azure.Management.Compute
      - type: SDK - JavaScript
        url: https://www.npmjs.com/package/@azure/arm-compute
      - type: SDK - Go
        url: https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/arm/compute
  - name: Azure Virtual Machine Scale Sets REST API
    description: REST API for creating and managing Azure Virtual Machine Scale Sets (VMSS). Enables deployment and management of groups of identical, load-balanced VMs that can automatically scale in response to demand or a defined schedule.
    image: https://azure.microsoft.com/svghandler/virtual-machines/
    humanURL: https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/
    baseURL: https://management.azure.com
    tags:
      - Autoscaling
      - Load Balancing
      - Virtual Machine Scale Sets
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/compute/virtual-machine-scale-sets
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/compute/virtual-machine-scale-sets?view=rest-compute-2025-04-01
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/quick-create-portal
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/virtual-machine-scale-sets/
      - type: FAQ
        url: https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-faq
  - name: Azure Virtual Machine Extensions REST API
    description: REST API for managing Virtual Machine Extensions, which provide post-deployment configuration and automation tasks on Azure VMs. Extensions can install software, run scripts, configure diagnostics, and integrate with monitoring and security tools.
    image: https://azure.microsoft.com/svghandler/virtual-machines/
    humanURL: https://learn.microsoft.com/en-us/azure/virtual-machines/extensions/overview
    baseURL: https://management.azure.com
    tags:
      - Automation
      - Configuration
      - Extensions
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/compute/virtual-machine-extensions
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/compute/virtual-machine-extensions?view=rest-compute-2025-04-01
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/virtual-machines/extensions/overview
  - name: Azure Virtual Machine Images REST API
    description: REST API for listing and querying available virtual machine images in Azure, including platform images, marketplace images, and custom images. Provides operations for listing publishers, offers, SKUs, and image versions by region.
    image: https://azure.microsoft.com/svghandler/virtual-machines/
    humanURL: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/cli-ps-findimage
    baseURL: https://management.azure.com
    tags:
      - Images
      - Marketplace
      - VM Images
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/compute/virtual-machine-images
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/compute/virtual-machine-images?view=rest-compute-2025-04-01
  - name: Azure Virtual Machine Sizes REST API
    description: REST API for listing available virtual machine sizes in a given Azure region. Returns the complete catalog of VM sizes with their resource specifications including number of vCPUs, memory, and disk capacity.
    image: https://azure.microsoft.com/svghandler/virtual-machines/
    humanURL: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview
    baseURL: https://management.azure.com
    tags:
      - Capacity
      - SKUs
      - VM Sizes
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/compute/virtual-machine-sizes
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/compute/virtual-machine-sizes/list?view=rest-compute-2025-04-01
  - name: Azure Virtual Machine Run Commands REST API
    description: REST API for executing scripts and commands on Azure Virtual Machines without requiring direct network connectivity. Useful for troubleshooting, running diagnostics, and performing administrative tasks remotely via the Azure management plane.
    image: https://azure.microsoft.com/svghandler/virtual-machines/
    humanURL: https://learn.microsoft.com/en-us/azure/virtual-machines/run-command-overview
    baseURL: https://management.azure.com
    tags:
      - Diagnostics
      - Run Commands
      - Scripting
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/compute/virtual-machine-run-commands
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/compute/virtual-machine-run-commands/list-by-virtual-machine?view=rest-compute-2025-04-01
  - name: Azure Availability Sets REST API
    description: REST API for creating and managing Availability Sets, which are logical groupings of VMs that distribute them across fault domains and update domains to provide high availability and resilience during planned and unplanned maintenance events.
    image: https://azure.microsoft.com/svghandler/virtual-machines/
    humanURL: https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview
    baseURL: https://management.azure.com
    tags:
      - Availability Sets
      - Fault Domains
      - High Availability
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/compute/availability-sets
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/compute/availability-sets?view=rest-compute-2024-07-01
  - name: Azure Proximity Placement Groups REST API
    description: REST API for creating and managing Proximity Placement Groups, which co-locate Azure resources within the same datacenter to achieve low network latency between virtual machines, scale sets, and other compute resources.
    image: https://azure.microsoft.com/svghandler/virtual-machines/
    humanURL: https://learn.microsoft.com/en-us/azure/virtual-machines/co-location
    baseURL: https://management.azure.com
    tags:
      - Co-Location
      - Low Latency
      - Proximity Placement Groups
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/compute/proximity-placement-groups
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/compute/proximity-placement-groups/list-by-subscription?view=rest-compute-2025-02-01
  - name: Azure Dedicated Hosts REST API
    description: REST API for creating and managing Azure Dedicated Hosts, which provide physical servers dedicated to a single Azure subscription. Dedicated hosts give visibility and control over server-level infrastructure to help address compliance and regulatory requirements.
    image: https://azure.microsoft.com/svghandler/virtual-machines/
    humanURL: https://learn.microsoft.com/en-us/azure/virtual-machines/dedicated-hosts
    baseURL: https://management.azure.com
    tags:
      - Compliance
      - Dedicated Hosts
      - Isolation
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/compute/dedicated-host-groups
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/compute/dedicated-host-groups/list-by-resource-group?view=rest-compute-2024-11-04
  - name: Azure Capacity Reservations REST API
    description: REST API for creating and managing Capacity Reservations, which allow you to reserve compute capacity in an Azure region or availability zone. Ensures that allocated capacity is available when you need to deploy virtual machines without relying on spot or on-demand availability.
    image: https://azure.microsoft.com/svghandler/virtual-machines/
    humanURL: https://learn.microsoft.com/en-us/azure/virtual-machines/capacity-reservation-overview
    baseURL: https://management.azure.com
    tags:
      - Capacity Reservations
      - Planning
      - Reserved Capacity
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/virtual-machines/capacity-reservation-overview
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/virtual-machines/capacity-reservation-group-share
common:
  - type: Portal
    url: https://portal.azure.com
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios
  - type: Status
    url: https://status.azure.com/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/options/
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Contact
    url: https://azure.microsoft.com/en-us/contact/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/virtual-machines/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/virtual-machines/overview
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/virtual-machines/
  - type: Website
    url: https://azure.microsoft.com/en-us/products/virtual-machines
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/free
  - type: Login
    url: https://portal.azure.com
  - type: SDKs
    url: https://azure.microsoft.com/en-us/downloads/
  - type: CLI Tools
    url: https://learn.microsoft.com/en-us/cli/azure/vm
  - type: Rate Limits
    url: https://learn.microsoft.com/en-us/azure/virtual-machines/quotas
  - type: Change Log
    url: https://azure.microsoft.com/en-us/updates/?product=virtual-machines
  - type: Community
    url: https://learn.microsoft.com/en-us/answers/tags/94/azure-virtual-machines
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/azure-virtual-machines
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: GitHub REST API Specs
    url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/compute/resource-manager
  - type: Training
    url: https://learn.microsoft.com/en-us/training/modules/intro-to-azure-virtual-machines/
  - type: FAQ
    url: https://learn.microsoft.com/en-us/azure/virtual-machines/faq-for-disks
  - type: YouTube
    url: https://www.youtube.com/c/MicrosoftAzure
  - type: SLA
    url: https://azure.microsoft.com/en-us/support/legal/sla/virtual-machines/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
