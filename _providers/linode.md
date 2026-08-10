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
- acting_count: 56
  human_in_the_loop: 2
  name: Linode Agentic Access
  operation_count: 116
  slug: linode-agentic-access
  summary_line: 116 operations · 56 acting · 2 human-in-the-loop
api_count: 23
apis:
- description: The Linode CLI is a command-line interface that wraps the Linode API v4, allowing developers and system administrators to manage Akamai Connected Cloud resources directly from the terminal. It support
  name: Linode CLI
  slug: cli
- description: The Linode Python SDK (linode_api4) is the official Python client library for interacting with the Linode API v4. It provides a Pythonic interface for managing all Akamai Connected Cloud resources inc
  name: Linode Python SDK
  slug: python-sdk
- description: The Linode Go SDK (linodego) is the official Go client library for the Linode API v4. It provides idiomatic Go interfaces for managing Akamai Connected Cloud infrastructure programmatically, including
  name: Linode Go SDK
  slug: go-sdk
- description: The Linode Terraform Provider enables infrastructure-as-code management of Akamai Connected Cloud resources using HashiCorp Terraform. It supports provisioning and managing compute instances, Kubernet
  name: Linode Terraform Provider
  slug: terraform-provider
- description: Manage your account settings, users, billing information, OAuth clients, service transfers, and payment methods.
  name: linode Account API
  slug: linode-account-api
- description: Manage Managed Database instances including MySQL and PostgreSQL clusters, backups, credentials, and maintenance windows.
  name: linode Databases API
  slug: linode-databases-api
- description: Manage DNS domains and their associated resource records including A, AAAA, CNAME, MX, TXT, SRV, CAA, and NS records.
  name: linode Domains API
  slug: linode-domains-api
- description: Manage custom images for deploying Linode instances, including creating images from disks, uploading images, and managing image metadata.
  name: linode Images API
  slug: linode-images-api
- description: Create and manage Linode compute instances, including configuration profiles, disks, backups, networking, migration, resize, and rebuild operations.
  name: linode Linode Instances API
  slug: linode-linode-instances-api
- description: Deploy and manage Kubernetes clusters, node pools, and cluster configurations through the Linode Kubernetes Engine.
  name: linode Linode Kubernetes Engine (LKE) API
  slug: linode-linode-kubernetes-engine-lke-api
- description: Manage Longview clients and subscriptions for system-level monitoring and metrics collection on Linode instances.
  name: linode Longview API
  slug: linode-longview-api
- description: Manage Linode Managed services including monitored contacts, credentials, issues, service monitors, and SSH access settings.
  name: linode Managed API
  slug: linode-managed-api
- description: Manage networking resources including IP addresses, IPv6 ranges and pools, firewalls, VLANs, and IP address sharing and assignment.
  name: linode Networking API
  slug: linode-networking-api
- description: Create and manage NodeBalancer load balancers, their configurations, and backend nodes for distributing traffic across Linode instances.
  name: linode NodeBalancers API
  slug: linode-nodebalancers-api
- description: Manage Object Storage buckets, access keys, clusters, and endpoints for S3-compatible object storage.
  name: linode Object Storage API
  slug: linode-object-storage-api
- description: Create and manage placement groups for controlling the physical placement of Linode instances within a data center.
  name: linode Placement Groups API
  slug: linode-placement-groups-api
- description: Manage your user profile settings, SSH keys, authorized applications, personal access tokens, and two-factor authentication.
  name: linode Profile API
  slug: linode-profile-api
- description: List available data center regions and their capabilities for deploying Linode services.
  name: linode Regions API
  slug: linode-regions-api
- description: Create and manage StackScripts for automating the deployment and configuration of Linode instances.
  name: linode StackScripts API
  slug: linode-stackscripts-api
- description: Create and manage support tickets and view replies for getting help from the Linode support team.
  name: linode Support API
  slug: linode-support-api
- description: The Tags API from linode — 2 operation(s) for tags.
  name: linode Tags API
  slug: linode-tags-api
- description: Create and manage Block Storage volumes that can be attached to Linode instances for persistent data storage.
  name: linode Volumes API
  slug: linode-volumes-api
- description: Create and manage Virtual Private Clouds for isolated network environments and subnets for Linode instances.
  name: linode VPCs API
  slug: linode-vpcs-api
artifact_total: 159
collections:
- collection_type: open
  name: Linode API v4
  slug: open-linode-api-v4
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/linode-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linode-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linode-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/linode-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/linode
- group: design
  title: ''
  type: JSONLD
  url: json-ld/linode-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/linode-instance-schema.json
description: Linode is a cloud hosting provider offering virtual private servers, managed databases, object storage, Kubernetes, and other infrastructure-as-a-service products to developers and businesses.
features:
- Nanode 1 GB at $5/mo (smallest plan)
- Shared CPU 4 GB at $20/mo (most popular)
- Dedicated CPU 4 GB at $36/mo
- High Memory from $60/mo
- GPU (NVIDIA Blackwell) from ~$1.50/hr
- Distributed Compute Regions (200+ edge locations)
- Hourly billing capped at monthly rate
- 'API v4: 800 req/2-min default'
- 'Linode create/boot: 25 req/min'
- 'Object Storage (S3-compatible): $5/250 GB'
- 'NodeBalancer (load balancer): $10/mo'
- 'Backups: $2-$60/mo'
- 'Linode Kubernetes Engine (LKE): control plane free'
- Managed Databases (Postgres, MySQL, MongoDB)
- Personal access tokens (PATs)
- Now Akamai Cloud Computing (Linode brand retired)
finops:
- name: Linode Finops
  service_category: Cloud Compute
  slug: linode-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linode.png
json_schemas:
- name: Account
  property_count: 14
  slug: linode-account
- name: Backup
  property_count: 8
  slug: linode-backup
- name: BackupResponse
  property_count: 2
  slug: linode-backupresponse
- name: Database
  property_count: 13
  slug: linode-database
- name: DatabaseRequest
  property_count: 2
  slug: linode-databaserequest
- name: Domain
  property_count: 13
  slug: linode-domain
- name: DomainRecord
  property_count: 9
  slug: linode-domainrecord
- name: DomainRecordRequest
  property_count: 7
  slug: linode-domainrecordrequest
- name: DomainRequest
  property_count: 5
  slug: linode-domainrequest
- name: Event
  property_count: 9
  slug: linode-event
- name: Firewall
  property_count: 7
  slug: linode-firewall
- name: FirewallRequest
  property_count: 3
  slug: linode-firewallrequest
- name: FirewallRule
  property_count: 6
  slug: linode-firewallrule
- name: FirewallUpdateRequest
  property_count: 3
  slug: linode-firewallupdaterequest
- name: Image
  property_count: 11
  slug: linode-image
- name: ImageRequest
  property_count: 3
  slug: linode-imagerequest
- name: ImageUpdateRequest
  property_count: 2
  slug: linode-imageupdaterequest
- name: Linode Instance
  property_count: 16
  slug: linode-instance
- name: Invoice
  property_count: 6
  slug: linode-invoice
- name: IPAddress
  property_count: 9
  slug: linode-ipaddress
- name: IPv6Address
  property_count: 5
  slug: linode-ipv6address
- name: IPv6Range
  property_count: 3
  slug: linode-ipv6range
- name: KubernetesVersion
  property_count: 1
  slug: linode-kubernetesversion
- name: Linode
  property_count: 17
  slug: linode-linode
- name: LinodeIPAddresses
  property_count: 2
  slug: linode-linodeipaddresses
- name: LinodeRebuildRequest
  property_count: 7
  slug: linode-linoderebuildrequest
- name: LinodeRequest
  property_count: 14
  slug: linode-linoderequest
- name: LinodeUpdateRequest
  property_count: 4
  slug: linode-linodeupdaterequest
- name: LKECluster
  property_count: 9
  slug: linode-lkecluster
- name: LKEClusterRequest
  property_count: 6
  slug: linode-lkeclusterrequest
- name: LKEClusterUpdateRequest
  property_count: 4
  slug: linode-lkeclusterupdaterequest
- name: LongviewClient
  property_count: 7
  slug: linode-longviewclient
- name: LongviewClientRequest
  property_count: 1
  slug: linode-longviewclientrequest
- name: ManagedService
  property_count: 13
  slug: linode-managedservice
- name: ManagedServiceRequest
  property_count: 8
  slug: linode-managedservicerequest
- name: NodeBalancer
  property_count: 11
  slug: linode-nodebalancer
- name: NodeBalancerRequest
  property_count: 4
  slug: linode-nodebalancerrequest
- name: NodeBalancerUpdateRequest
  property_count: 3
  slug: linode-nodebalancerupdaterequest
- name: NodePool
  property_count: 5
  slug: linode-nodepool
- name: NodePoolRequest
  property_count: 3
  slug: linode-nodepoolrequest
- name: ObjectStorageBucket
  property_count: 6
  slug: linode-objectstoragebucket
- name: ObjectStorageEndpointList
  property_count: 1
  slug: linode-objectstorageendpointlist
- name: ObjectStorageKey
  property_count: 6
  slug: linode-objectstoragekey
- name: ObjectStorageKeyRequest
  property_count: 2
  slug: linode-objectstoragekeyrequest
- name: PaginatedConfigList
  property_count: 0
  slug: linode-paginatedconfiglist
- name: PaginatedDatabaseEngineList
  property_count: 0
  slug: linode-paginateddatabaseenginelist
- name: PaginatedDatabaseList
  property_count: 0
  slug: linode-paginateddatabaselist
- name: PaginatedDatabaseTypeList
  property_count: 0
  slug: linode-paginateddatabasetypelist
- name: PaginatedDiskList
  property_count: 0
  slug: linode-paginateddisklist
- name: PaginatedDomainList
  property_count: 0
  slug: linode-paginateddomainlist
- name: PaginatedDomainRecordList
  property_count: 0
  slug: linode-paginateddomainrecordlist
- name: PaginatedEventList
  property_count: 0
  slug: linode-paginatedeventlist
- name: PaginatedFirewallList
  property_count: 0
  slug: linode-paginatedfirewalllist
- name: PaginatedImageList
  property_count: 0
  slug: linode-paginatedimagelist
- name: PaginatedInvoiceList
  property_count: 0
  slug: linode-paginatedinvoicelist
- name: PaginatedIPAddressList
  property_count: 0
  slug: linode-paginatedipaddresslist
- name: PaginatedKernelList
  property_count: 0
  slug: linode-paginatedkernellist
- name: PaginatedLinodeList
  property_count: 0
  slug: linode-paginatedlinodelist
- name: PaginatedLinodeTypeList
  property_count: 0
  slug: linode-paginatedlinodetypelist
- name: PaginatedLKEClusterList
  property_count: 0
  slug: linode-paginatedlkeclusterlist
- name: PaginatedLongviewClientList
  property_count: 0
  slug: linode-paginatedlongviewclientlist
- name: PaginatedManagedContactList
  property_count: 0
  slug: linode-paginatedmanagedcontactlist
- name: PaginatedManagedIssueList
  property_count: 0
  slug: linode-paginatedmanagedissuelist
- name: PaginatedManagedServiceList
  property_count: 0
  slug: linode-paginatedmanagedservicelist
- name: PaginatedNodeBalancerConfigList
  property_count: 0
  slug: linode-paginatednodebalancerconfiglist
- name: PaginatedNodeBalancerList
  property_count: 0
  slug: linode-paginatednodebalancerlist
- name: PaginatedNodePoolList
  property_count: 0
  slug: linode-paginatednodepoollist
- name: PaginatedObjectStorageBucketList
  property_count: 0
  slug: linode-paginatedobjectstoragebucketlist
- name: PaginatedObjectStorageKeyList
  property_count: 0
  slug: linode-paginatedobjectstoragekeylist
- name: PaginatedPaymentList
  property_count: 0
  slug: linode-paginatedpaymentlist
- name: PaginatedPlacementGroupList
  property_count: 0
  slug: linode-paginatedplacementgrouplist
- name: PaginatedRegionList
  property_count: 0
  slug: linode-paginatedregionlist
- name: PaginatedSSHKeyList
  property_count: 0
  slug: linode-paginatedsshkeylist
- name: PaginatedStackScriptList
  property_count: 0
  slug: linode-paginatedstackscriptlist
- name: PaginatedSubnetList
  property_count: 0
  slug: linode-paginatedsubnetlist
- name: PaginatedSupportTicketList
  property_count: 0
  slug: linode-paginatedsupportticketlist
- name: PaginatedTagList
  property_count: 0
  slug: linode-paginatedtaglist
- name: PaginatedTokenList
  property_count: 0
  slug: linode-paginatedtokenlist
- name: PaginatedUserList
  property_count: 0
  slug: linode-paginateduserlist
- name: PaginatedVLANList
  property_count: 0
  slug: linode-paginatedvlanlist
- name: PaginatedVolumeList
  property_count: 0
  slug: linode-paginatedvolumelist
- name: PaginatedVPCList
  property_count: 0
  slug: linode-paginatedvpclist
- name: Pagination
  property_count: 3
  slug: linode-pagination
- name: Payment
  property_count: 3
  slug: linode-payment
- name: PaymentRequest
  property_count: 1
  slug: linode-paymentrequest
- name: PlacementGroup
  property_count: 7
  slug: linode-placementgroup
- name: PlacementGroupRequest
  property_count: 4
  slug: linode-placementgrouprequest
- name: Profile
  property_count: 8
  slug: linode-profile
- name: Region
  property_count: 7
  slug: linode-region
- name: SSHKey
  property_count: 4
  slug: linode-sshkey
- name: SSHKeyRequest
  property_count: 2
  slug: linode-sshkeyrequest
- name: StackScript
  property_count: 12
  slug: linode-stackscript
- name: StackScriptRequest
  property_count: 6
  slug: linode-stackscriptrequest
- name: Subnet
  property_count: 6
  slug: linode-subnet
- name: SubnetRequest
  property_count: 2
  slug: linode-subnetrequest
- name: SupportTicket
  property_count: 8
  slug: linode-supportticket
- name: SupportTicketRequest
  property_count: 8
  slug: linode-supportticketrequest
- name: Tag
  property_count: 1
  slug: linode-tag
- name: TagRequest
  property_count: 5
  slug: linode-tagrequest
- name: Token
  property_count: 6
  slug: linode-token
- name: TokenRequest
  property_count: 3
  slug: linode-tokenrequest
- name: User
  property_count: 5
  slug: linode-user
- name: UserRequest
  property_count: 3
  slug: linode-userrequest
- name: Volume
  property_count: 11
  slug: linode-volume
- name: VolumeRequest
  property_count: 5
  slug: linode-volumerequest
- name: VolumeUpdateRequest
  property_count: 2
  slug: linode-volumeupdaterequest
- name: VPC
  property_count: 7
  slug: linode-vpc
- name: VPCRequest
  property_count: 4
  slug: linode-vpcrequest
- name: VPCUpdateRequest
  property_count: 2
  slug: linode-vpcupdaterequest
json_structures:
- name: Linode Structure
  property_count: 0
  slug: linode-structure
jsonld:
- class_count: 0
  name: Linode Context
  property_count: 12
  slug: linode-context
layout: provider
modified: '2026-05-19'
name: linode
nav: Providers
network: true
overview: 'linode publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Account API, Databases API, Domains API, and 16 more.


  The linode catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  linode''s developer surface includes authentication and 6 more developer resources.'
plans:
- name: Linode Plans Pricing
  plan_count: 6
  slug: linode-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 3
  name: Linode Rate Limits
  slug: linode-rate-limits
rules:
- name: linode API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: linode-jsonschema-spectral-rules
scopes:
- name: Linode Scopes
  scope_count: 28
  slug: linode-scopes
  summary_line: 28 scopes · authorizationCode
score:
  band: developing
  composite: 44.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 71.3
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/screenshots/linode-2026-06-20T184550.png
security:
- kind: authentication
  name: Linode Authentication
  slug: linode-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Linode Domain Security
  slug: linode-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: linode
---
