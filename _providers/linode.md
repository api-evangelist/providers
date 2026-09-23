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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 56
  human_in_the_loop: 2
  name: Linode Agentic Access
  operation_count: 116
  slug: linode-agentic-access
  summary_line: 116 operations · 56 acting · 2 human-in-the-loop
api_count: 2
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
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage your account settings, users, billing information, OAuth clients, service transfers, and payment methods.
  name: linode Account API
  slug: linode-account-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage Managed Database instances including MySQL and PostgreSQL clusters, backups, credentials, and maintenance windows.
  name: linode Databases API
  slug: linode-databases-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage DNS domains and their associated resource records including A, AAAA, CNAME, MX, TXT, SRV, CAA, and NS records.
  name: linode Domains API
  slug: linode-domains-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage custom images for deploying Linode instances, including creating images from disks, uploading images, and managing image metadata.
  name: linode Images API
  slug: linode-images-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage Linode compute instances, including configuration profiles, disks, backups, networking, migration, resize, and rebuild operations.
  name: linode Instances API
  slug: linode-linode-instances-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Deploy and manage Kubernetes clusters, node pools, and cluster configurations through the Linode Kubernetes Engine.
  name: linode Kubernetes Engine (LKE) API
  slug: linode-linode-kubernetes-engine-lke-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage Longview clients and subscriptions for system-level monitoring and metrics collection on Linode instances.
  name: linode Longview API
  slug: linode-longview-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage Linode Managed services including monitored contacts, credentials, issues, service monitors, and SSH access settings.
  name: linode Managed API
  slug: linode-managed-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage networking resources including IP addresses, IPv6 ranges and pools, firewalls, VLANs, and IP address sharing and assignment.
  name: linode Networking API
  slug: linode-networking-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage NodeBalancer load balancers, their configurations, and backend nodes for distributing traffic across Linode instances.
  name: linode NodeBalancers API
  slug: linode-nodebalancers-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage Object Storage buckets, access keys, clusters, and endpoints for S3-compatible object storage.
  name: linode Object Storage API
  slug: linode-object-storage-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage placement groups for controlling the physical placement of Linode instances within a data center.
  name: linode Placement Groups API
  slug: linode-placement-groups-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage your user profile settings, SSH keys, authorized applications, personal access tokens, and two-factor authentication.
  name: linode Profile API
  slug: linode-profile-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: List available data center regions and their capabilities for deploying Linode services.
  name: linode Regions API
  slug: linode-regions-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage StackScripts for automating the deployment and configuration of Linode instances.
  name: linode StackScripts API
  slug: linode-stackscripts-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage support tickets and view replies for getting help from the Linode support team.
  name: linode Support API
  slug: linode-support-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The Tags API from linode — 2 operation(s) for tags.
  name: linode Tags API
  slug: linode-tags-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage Block Storage volumes that can be attached to Linode instances for persistent data storage.
  name: linode Volumes API
  slug: linode-volumes-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage Virtual Private Clouds for isolated network environments and subnets for Linode instances.
  name: linode VPCs API
  slug: linode-vpcs-api
artifact_total: 181
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Linode API v4 Account API
  slug: open-linode-account-api
- collection_type: open
  name: Linode API v4
  slug: open-linode-api-v4
- collection_type: open
  name: Linode API v4 Account Databases API
  slug: open-linode-databases-api
- collection_type: open
  name: Linode API v4 Account Domains API
  slug: open-linode-domains-api
- collection_type: open
  name: Linode API v4 Account Images API
  slug: open-linode-images-api
- collection_type: open
  name: Linode API v4 Account Linode Instances API
  slug: open-linode-linode-instances-api
- collection_type: open
  name: Linode API v4 Account Linode Kubernetes Engine (LKE) API
  slug: open-linode-linode-kubernetes-engine-lke-api
- collection_type: open
  name: Linode API v4 Account Longview API
  slug: open-linode-longview-api
- collection_type: open
  name: Linode API v4 Account Managed API
  slug: open-linode-managed-api
- collection_type: open
  name: Linode API v4 Account Networking API
  slug: open-linode-networking-api
- collection_type: open
  name: Linode API v4 Account NodeBalancers API
  slug: open-linode-nodebalancers-api
- collection_type: open
  name: Linode API v4 Account Object Storage API
  slug: open-linode-object-storage-api
- collection_type: open
  name: Linode API v4 Account Placement Groups API
  slug: open-linode-placement-groups-api
- collection_type: open
  name: Linode API v4 Account Profile API
  slug: open-linode-profile-api
- collection_type: open
  name: Linode API v4 Account Regions API
  slug: open-linode-regions-api
- collection_type: open
  name: Linode API v4 Account StackScripts API
  slug: open-linode-stackscripts-api
- collection_type: open
  name: Linode API v4 Account Support API
  slug: open-linode-support-api
- collection_type: open
  name: Linode API v4 Account Tags API
  slug: open-linode-tags-api
- collection_type: open
  name: Linode API v4 Account Volumes API
  slug: open-linode-volumes-api
- collection_type: open
  name: Linode API v4 Account VPCs API
  slug: open-linode-vpcs-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/agentic-access/linode-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/linode-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/security/linode-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/linode-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/authentication/linode-authentication.yml
  title: ''
  type: Authentication
  url: authentication/linode-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/scopes/linode-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/linode-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/linode
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/json-ld/linode-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/linode-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/json-schema/linode-instance-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/linode-instance-schema.json
- group: company
  title: ''
  type: Website
  url: https://www.linode.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://techdocs.akamai.com/linode-api/reference/api
- group: docs
  title: ''
  type: Documentation
  url: https://techdocs.akamai.com/linode-api/
- group: docs
  title: ''
  type: APIReference
  url: https://techdocs.akamai.com/linode-api/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://techdocs.akamai.com/linode-api/reference/get-started
- group: start
  title: ''
  type: SignUp
  url: https://login.linode.com/signup
- group: start
  title: ''
  type: Login
  url: https://login.linode.com/login
- group: start
  title: ''
  type: Console
  url: https://cloud.linode.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linode
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/linode/linode-api-openapi
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/linode/linode-cli/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/linode/linode-api-openapi/blob/main/LICENSE
- group: operate
  title: ''
  type: StatusPage
  url: https://status.linode.com/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/packages/linode-packages.yml
  title: ''
  type: Packages
  url: packages/linode-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/packages/linode-packages.yml
  title: ''
  type: SDKs
  url: packages/linode-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/well-known/linode-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/linode-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/well-known/linode-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/linode-api-catalog.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/mcp/linode-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/linode-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/mcp/linode-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/linode-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/llms/linode-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/linode-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/conformance/linode-conformance.yml
  title: ''
  type: Conformance
  url: conformance/linode-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/errors/linode-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/linode-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/lifecycle/linode-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/linode-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/lifecycle/linode-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/linode-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/security/linode-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/linode-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/security/linode-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/linode-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/conventions/linode-conventions.yml
  title: ''
  type: Conventions
  url: conventions/linode-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/changelog/linode-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/linode-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/cli/linode-cli.yml
  title: ''
  type: CLI
  url: cli/linode-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/data-model/linode-data-model.yml
  title: ''
  type: DataModel
  url: data-model/linode-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/plans/linode-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/linode-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/rate-limits/linode-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/linode-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/finops/linode-finops.yml
  title: ''
  type: FinOps
  url: finops/linode-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/vocabulary/linode-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/linode-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/json-structure/linode-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/linode-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/rules/linode-jsonschema-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/linode-jsonschema-spectral-rules.yml
created: '2026-05-04'
description: 'Linode — operating as Akamai Cloud since Akamai''s acquisition, with the Linode brand retained on the API, the CLI and the developer surface — is a cloud infrastructure provider offering virtual compute instances, GPU and accelerated plans, managed Kubernetes (LKE), S3-compatible Object Storage, Block Storage volumes, NodeBalancers, VPCs, Cloud Firewalls, managed MySQL/PostgreSQL/Valkey databases and DNS hosting. The Linode API v4 is a single cohesive REST surface at api.linode.com/v4 covering all of it: 358 paths and 539 operations in the first-party OpenAPI, documented at techdocs.akamai.com, with a generated CLI, first-party SDKs in Python, Go and TypeScript, a Terraform provider and an official read-only MCP server. Its price book is published as an unauthenticated API, so a stack can be costed with no account at all.'
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
mcp_servers:
- description: Akamai publishes one official Model Context Protocol server for Akamai Cloud — the product formerly and still widely known as Linode — at akamai-developers/akamai-cloud-mcp. It is read-only by constru
  name: Akamai Cloud MCP Server
  slug: akamai-cloud-mcp-server
modified: '2026-09-17'
name: Linode
nav: Providers
network: true
overview: 'Linode publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Account API, Databases API, Domains API, and 16 more. Tagged areas include Cloud Computing, Infrastructure-as-a-Service, Virtual Machines, Kubernetes, and Object Storage.


  The Linode catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Linode''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, developer console, changelog, and 37 more developer resources.'
plans:
- name: Linode Plans Pricing
  plan_count: 7
  slug: linode-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 12
  name: Linode Rate Limits
  slug: linode-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Linode API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: linode-jsonschema-spectral-rules
scopes:
- name: Linode Scopes
  scope_count: 30
  slug: linode-scopes
  summary_line: 30 scopes · authorizationCode
score:
  band: strong
  composite: 55.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 80.3
    catalog_earned_first_party: 24.0
    catalog_gap: 34.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 29.5
    contract_quality: 67.4
    developer_ergonomics: 28.0
    discoverability: 75.9
    operational_transparency: 84.2
  previous_composite: 55.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 11.1
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
- kind: vulnerability-disclosure
  name: Linode Vulnerability Disclosure
  slug: linode-vulnerability-disclosure
  summary_line: Hackerone
slug: linode
tags:
- Cloud Computing
- Infrastructure-as-a-Service
- Virtual Machines
- Kubernetes
- Object Storage
- Block Storage
- DNS
- Managed Database
- Networking
- GPU
- Load Balancer
- Developer Tools
website: https://www.linode.com/
---
