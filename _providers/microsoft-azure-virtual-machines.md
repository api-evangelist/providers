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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Microsoft Azure Virtual Machines Agentic Access
  operation_count: 26
  slug: microsoft-azure-virtual-machines-agentic-access
  summary_line: 26 operations · 20 acting
api_count: 10
apis:
- description: REST API for creating and managing Azure Virtual Machine Scale Sets (VMSS). Enables deployment and management of groups of identical, load-balanced VMs that can automatically scale in response to dema
  name: Azure Virtual Machine Scale Sets REST API
  slug: azure-virtual-machine-scale-sets-rest-api
- description: REST API for managing Virtual Machine Extensions, which provide post-deployment configuration and automation tasks on Azure VMs. Extensions can install software, run scripts, configure diagnostics, an
  name: Azure Virtual Machine Extensions REST API
  slug: azure-virtual-machine-extensions-rest-api
- description: REST API for listing and querying available virtual machine images in Azure, including platform images, marketplace images, and custom images. Provides operations for listing publishers, offers, SKUs,
  name: Azure Virtual Machine Images REST API
  slug: azure-virtual-machine-images-rest-api
- description: REST API for listing available virtual machine sizes in a given Azure region. Returns the complete catalog of VM sizes with their resource specifications including number of vCPUs, memory, and disk ca
  name: Azure Virtual Machine Sizes REST API
  slug: azure-virtual-machine-sizes-rest-api
- description: REST API for executing scripts and commands on Azure Virtual Machines without requiring direct network connectivity. Useful for troubleshooting, running diagnostics, and performing administrative task
  name: Azure Virtual Machine Run Commands REST API
  slug: azure-virtual-machine-run-commands-rest-api
- description: REST API for creating and managing Availability Sets, which are logical groupings of VMs that distribute them across fault domains and update domains to provide high availability and resilience during
  name: Azure Availability Sets REST API
  slug: azure-availability-sets-rest-api
- description: REST API for creating and managing Proximity Placement Groups, which co-locate Azure resources within the same datacenter to achieve low network latency between virtual machines, scale sets, and other
  name: Azure Proximity Placement Groups REST API
  slug: azure-proximity-placement-groups-rest-api
- description: REST API for creating and managing Azure Dedicated Hosts, which provide physical servers dedicated to a single Azure subscription. Dedicated hosts give visibility and control over server-level infrast
  name: Azure Dedicated Hosts REST API
  slug: azure-dedicated-hosts-rest-api
- description: REST API for creating and managing Capacity Reservations, which allow you to reserve compute capacity in an Azure region or availability zone. Ensures that allocated capacity is available when you nee
  name: Azure Capacity Reservations REST API
  slug: azure-capacity-reservations-rest-api
- description: Operations for creating, updating, deleting, and managing the lifecycle of Azure Virtual Machines including power operations, patching, and diagnostics.
  name: Azure Virtual Machines Virtual Machines API
  slug: microsoft-azure-virtual-machines-virtual-machines-api
artifact_total: 58
collections:
- collection_type: postman
  name: Azure REST Virtual Machines API
  slug: postman-microsoft-azure-virtual-machines-virtual-machines-api
- collection_type: open
  name: Azure Virtual Machines REST API
  slug: open-azure-virtual-machines
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-virtual-machines/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-virtual-machines-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-virtual-machines-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-virtual-machines-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-virtual-machines-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/options/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Contact
  url: https://azure.microsoft.com/en-us/contact/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/virtual-machines/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/virtual-machines/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/virtual-machines/
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/virtual-machines
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com
- group: build
  title: ''
  type: SDKs
  url: https://azure.microsoft.com/en-us/downloads/
- group: build
  title: ''
  type: CLI Tools
  url: https://learn.microsoft.com/en-us/cli/azure/vm
- group: operate
  title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/azure/virtual-machines/quotas
- group: operate
  title: ''
  type: ChangeLog
  url: https://azure.microsoft.com/en-us/updates/?product=virtual-machines
- group: operate
  title: ''
  type: Community
  url: https://learn.microsoft.com/en-us/answers/tags/94/azure-virtual-machines
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-virtual-machines
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: build
  title: ''
  type: GitHub REST API Specs
  url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/compute/resource-manager
- group: learn
  title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/modules/intro-to-azure-virtual-machines/
- group: operate
  title: ''
  type: FAQ
  url: https://learn.microsoft.com/en-us/azure/virtual-machines/faq-for-disks
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/MicrosoftAzure
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://azure.microsoft.com/en-us/support/legal/sla/virtual-machines/
created: '2024-01-20'
description: Azure Virtual Machines (VMs) is one of several types of on-demand, scalable computing resources that Azure offers. VMs give you the flexibility of virtualization without having to buy and maintain physical hardware.
finops:
- name: Microsoft Azure Virtual Machines Finops
  service_category: Cloud Compute / IaaS
  slug: microsoft-azure-virtual-machines-finops
image: https://azure.microsoft.com/svghandler/virtual-machines/
json_schemas:
- name: ApiError
  property_count: 5
  slug: microsoft-azure-virtual-machines-apierror
- name: ApiErrorBase
  property_count: 3
  slug: microsoft-azure-virtual-machines-apierrorbase
- name: AttachDetachDataDisksRequest
  property_count: 2
  slug: microsoft-azure-virtual-machines-attachdetachdatadisksrequest
- name: CloudError
  property_count: 1
  slug: microsoft-azure-virtual-machines-clouderror
- name: DataDisk
  property_count: 7
  slug: microsoft-azure-virtual-machines-datadisk
- name: DiagnosticsProfile
  property_count: 1
  slug: microsoft-azure-virtual-machines-diagnosticsprofile
- name: HardwareProfile
  property_count: 1
  slug: microsoft-azure-virtual-machines-hardwareprofile
- name: ImageReference
  property_count: 6
  slug: microsoft-azure-virtual-machines-imagereference
- name: InstanceViewStatus
  property_count: 5
  slug: microsoft-azure-virtual-machines-instanceviewstatus
- name: LinuxConfiguration
  property_count: 4
  slug: microsoft-azure-virtual-machines-linuxconfiguration
- name: LinuxPatchSettings
  property_count: 2
  slug: microsoft-azure-virtual-machines-linuxpatchsettings
- name: ManagedDiskParameters
  property_count: 2
  slug: microsoft-azure-virtual-machines-manageddiskparameters
- name: NetworkInterfaceReference
  property_count: 2
  slug: microsoft-azure-virtual-machines-networkinterfacereference
- name: NetworkProfile
  property_count: 1
  slug: microsoft-azure-virtual-machines-networkprofile
- name: OSDisk
  property_count: 7
  slug: microsoft-azure-virtual-machines-osdisk
- name: OSProfile
  property_count: 5
  slug: microsoft-azure-virtual-machines-osprofile
- name: Plan
  property_count: 4
  slug: microsoft-azure-virtual-machines-plan
- name: RetrieveBootDiagnosticsDataResult
  property_count: 2
  slug: microsoft-azure-virtual-machines-retrievebootdiagnosticsdataresult
- name: RunCommandInput
  property_count: 3
  slug: microsoft-azure-virtual-machines-runcommandinput
- name: RunCommandResult
  property_count: 1
  slug: microsoft-azure-virtual-machines-runcommandresult
- name: StorageProfile
  property_count: 3
  slug: microsoft-azure-virtual-machines-storageprofile
- name: SubResource
  property_count: 1
  slug: microsoft-azure-virtual-machines-subresource
- name: VirtualMachine
  property_count: 9
  slug: microsoft-azure-virtual-machines-virtualmachine
- name: VirtualMachineAssessPatchesResult
  property_count: 6
  slug: microsoft-azure-virtual-machines-virtualmachineassesspatchesresult
- name: VirtualMachineCaptureParameters
  property_count: 3
  slug: microsoft-azure-virtual-machines-virtualmachinecaptureparameters
- name: VirtualMachineCaptureResult
  property_count: 5
  slug: microsoft-azure-virtual-machines-virtualmachinecaptureresult
- name: VirtualMachineIdentity
  property_count: 3
  slug: microsoft-azure-virtual-machines-virtualmachineidentity
- name: VirtualMachineInstallPatchesParameters
  property_count: 2
  slug: microsoft-azure-virtual-machines-virtualmachineinstallpatchesparameters
- name: VirtualMachineInstallPatchesResult
  property_count: 8
  slug: microsoft-azure-virtual-machines-virtualmachineinstallpatchesresult
- name: VirtualMachineInstanceView
  property_count: 6
  slug: microsoft-azure-virtual-machines-virtualmachineinstanceview
- name: VirtualMachineListResult
  property_count: 2
  slug: microsoft-azure-virtual-machines-virtualmachinelistresult
- name: VirtualMachineProperties
  property_count: 17
  slug: microsoft-azure-virtual-machines-virtualmachineproperties
- name: VirtualMachineSize
  property_count: 6
  slug: microsoft-azure-virtual-machines-virtualmachinesize
- name: VirtualMachineSizeListResult
  property_count: 1
  slug: microsoft-azure-virtual-machines-virtualmachinesizelistresult
- name: VirtualMachineUpdate
  property_count: 4
  slug: microsoft-azure-virtual-machines-virtualmachineupdate
- name: WindowsConfiguration
  property_count: 4
  slug: microsoft-azure-virtual-machines-windowsconfiguration
- name: WindowsPatchSettings
  property_count: 3
  slug: microsoft-azure-virtual-machines-windowspatchsettings
json_structures:
- name: Microsoft Azure Virtual Machines Structure
  property_count: 0
  slug: microsoft-azure-virtual-machines-structure
layout: provider
modified: '2026-05-19'
name: Azure Virtual Machines
nav: Providers
network: true
overview: 'Azure Virtual Machines publishes 1 API on the [APIs.io](https://apis.io/) network: Virtual Machines API. Tagged areas include Cloud Computing, Compute, IaaS, Infrastructure, and Virtual Machines.


  The Azure Virtual Machines catalog on APIs.io includes 1 Spectral governance ruleset.


  Azure Virtual Machines'' developer surface includes authentication, developer portal, engineering blog, support, documentation, getting-started guide, pricing, and 24 more developer resources.'
plans:
- name: Microsoft Azure Virtual Machines Plans Pricing
  plan_count: 10
  slug: microsoft-azure-virtual-machines-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 16
  name: Microsoft Azure Virtual Machines Rate Limits
  slug: microsoft-azure-virtual-machines-rate-limits
rules:
- name: Azure Virtual Machines API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-azure-virtual-machines-jsonschema-spectral-rules
scopes:
- name: Microsoft Azure Virtual Machines Scopes
  scope_count: 1
  slug: microsoft-azure-virtual-machines-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 62.3
  delta: -2.1
  facets:
    commercial_clarity: 84.2
    contract_quality: 40.3
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 64.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-virtual-machines/refs/heads/main/screenshots/microsoft-azure-virtual-machines-2026-06-20T185443.png
security:
- kind: authentication
  name: Microsoft Azure Virtual Machines Authentication
  slug: microsoft-azure-virtual-machines-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Virtual Machines Domain Security
  slug: microsoft-azure-virtual-machines-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-virtual-machines
tags:
- Cloud Computing
- Compute
- IaaS
- Infrastructure
- Virtual Machines
website: https://azure.microsoft.com/en-us/products/virtual-machines
---
