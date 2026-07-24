---
access_model:
  confidence: high
  label: Free trial · Self-serve signup
  onboarding: self-serve
  pricing: free-trial
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Nutanix Agentic Access
  operation_count: 54
  slug: nutanix-agentic-access
  summary_line: 54 operations · 31 acting
api_count: 21
apis:
- description: The next-generation v4 API for managing the Nutanix Cloud Platform through Prism Central with GA SDKs for Python, Java, Go, and JavaScript. The v4 API is now the recommended version for production env
  name: Nutanix Prism Central API V4
  slug: prism-central-v4
- description: API for managing Kubernetes clusters through Nutanix Karbon, including cluster lifecycle, upgrades, and configuration.
  name: Nutanix Karbon API
  slug: karbon
- description: REST API for Nutanix Database Service (NDB) providing database-as-a-service capabilities for PostgreSQL, MySQL, SQL Server, Oracle, and MongoDB.
  name: Nutanix Database Service API
  slug: ndb
- description: REST API for Nutanix Cloud Clusters (NC2), enabling creation and management of Nutanix clusters on AWS and Azure public clouds.
  name: Nutanix Cloud Clusters API
  slug: nc2
- description: API for Nutanix Cloud Manager Self-Service (formerly Calm), enabling automation of application deployment and lifecycle management through blueprints and runbooks.
  name: Nutanix NCM Self-Service API
  slug: ncm-self-service
- description: API for Foundation and Foundation Central, enabling automated cluster deployment and remote node imaging.
  name: Nutanix Foundation API
  slug: foundation
- description: Retrieve and manage cluster alerts for monitoring health and operational events.
  name: Nutanix Alerts API
  slug: nutanix-alerts-api
- description: Manage categories and category values used for tagging and organizing resources across the Nutanix environment.
  name: Nutanix Categories API
  slug: nutanix-categories-api
- description: Retrieve and manage Nutanix cluster configurations and metadata across the Prism Central deployment.
  name: Nutanix Clusters API
  slug: nutanix-clusters-api
- description: Retrieve information about physical hosts in the Nutanix cluster infrastructure.
  name: Nutanix Hosts API
  slug: nutanix-hosts-api
- description: Manage disk images distributed across clusters for VM provisioning, including ISO and disk image uploads.
  name: Nutanix Images API
  slug: nutanix-images-api
- description: Manage Flow microsegmentation policies that control network traffic between VMs based on categories.
  name: Nutanix Network Security Rules API
  slug: nutanix-network-security-rules-api
- description: Manage projects that define resource quotas, user access, and infrastructure boundaries for self-service consumption.
  name: Nutanix Projects API
  slug: nutanix-projects-api
- description: Manage protection domains that define groups of VMs and volume groups for data protection and disaster recovery.
  name: Nutanix Protection Domains API
  slug: nutanix-protection-domains-api
- description: Manage VM snapshots for point-in-time recovery of virtual machines.
  name: Nutanix Snapshots API
  slug: nutanix-snapshots-api
- description: Manage storage containers that provide logical storage partitions within the Nutanix distributed storage fabric.
  name: Nutanix Storage Containers API
  slug: nutanix-storage-containers-api
- description: Manage storage pools which represent groups of physical disks used for storing data across the cluster.
  name: Nutanix Storage Pools API
  slug: nutanix-storage-pools-api
- description: Manage AHV network subnets including VLAN and overlay network configurations.
  name: Nutanix Subnets API
  slug: nutanix-subnets-api
- description: Manage virtual disks including disk statistics and configuration within the cluster.
  name: Nutanix Virtual Disks API
  slug: nutanix-virtual-disks-api
- description: Manage virtual machines including creation, update, deletion, and power state operations through the intent-based API model.
  name: Nutanix VMs API
  slug: nutanix-vms-api
- description: Manage webhook listeners that receive event notifications from the Nutanix platform.
  name: Nutanix Webhooks API
  slug: nutanix-webhooks-api
artifact_total: 49
collections:
- collection_type: open
  name: Nutanix Prism Central API v3
  slug: open-nutanix-prism-central-v3
- collection_type: open
  name: Nutanix Prism Element API v2
  slug: open-nutanix-prism-element-v2
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nutanix-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nutanix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nutanix-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nutanix
- group: company
  title: ''
  type: Website
  url: https://www.nutanix.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.nutanix.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.nutanix.dev/nutanix-api-user-guide/
- group: build
  title: ''
  type: SDKs
  url: https://www.nutanix.dev/sdk_reference/
- group: docs
  title: ''
  type: Reference
  url: https://www.nutanix.dev/api_references/
- group: build
  title: ''
  type: Code Samples
  url: https://www.nutanix.dev/code_samples/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.nutanix.dev/api-versions/
- group: company
  title: ''
  type: Blog
  url: https://www.nutanix.dev/blog/
- group: operate
  title: ''
  type: Community
  url: https://next.nutanix.com/
- group: operate
  title: ''
  type: Support
  url: https://www.nutanix.com/support-services/product-support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nutanix.com/
- group: start
  title: ''
  type: Login
  url: https://my.nutanix.com/
- group: start
  title: ''
  type: Signup
  url: https://my.nutanix.com/page/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nutanix
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.nutanix.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nutanix.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nutanix.com/legal/privacy-notice
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.nutanix.com/llms.txt
created: '2025-03-14'
description: Nutanix is a hyper-converged infrastructure solution that integrates compute, virtualization, storage, networking, and security to power enterprise applications. Nutanix provides public APIs for managing and automating infrastructure including Prism Central, Prism Element, Karbon Kubernetes, Nutanix Database Service (NDB), Cloud Clusters (NC2), NCM Self-Service, and the GA v4 API platform.
finops:
- name: Nutanix Finops
  service_category: Hybrid Cloud Infrastructure
  slug: nutanix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nutanix.png
json_schemas:
- name: Cluster
  property_count: 7
  slug: nutanix-cluster
- name: ClusterIntentResponse
  property_count: 3
  slug: nutanix-clusterintentresponse
- name: ClusterListResponse
  property_count: 3
  slug: nutanix-clusterlistresponse
- name: EntityMetadata
  property_count: 6
  slug: nutanix-entitymetadata
- name: Host
  property_count: 11
  slug: nutanix-host
- name: ImageIntentInput
  property_count: 2
  slug: nutanix-imageintentinput
- name: ImageListResponse
  property_count: 3
  slug: nutanix-imagelistresponse
- name: ListMetadata
  property_count: 6
  slug: nutanix-listmetadata
- name: PaginationMetadata
  property_count: 5
  slug: nutanix-paginationmetadata
- name: Reference
  property_count: 3
  slug: nutanix-reference
- name: StorageContainer
  property_count: 8
  slug: nutanix-storagecontainer
- name: StorageContainerInput
  property_count: 5
  slug: nutanix-storagecontainerinput
- name: SubnetIntentInput
  property_count: 2
  slug: nutanix-subnetintentinput
- name: SubnetListResponse
  property_count: 3
  slug: nutanix-subnetlistresponse
- name: VmIntentInput
  property_count: 2
  slug: nutanix-vmintentinput
- name: VmIntentResponse
  property_count: 3
  slug: nutanix-vmintentresponse
- name: VmListResponse
  property_count: 3
  slug: nutanix-vmlistresponse
- name: VmSpec
  property_count: 4
  slug: nutanix-vmspec
json_structures:
- name: Nutanix Structure
  property_count: 0
  slug: nutanix-structure
layout: provider
modified: '2026-05-19'
name: Nutanix
nav: Providers
network: true
overview: 'Nutanix publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Categories API, Clusters API, and 12 more. Tagged areas include Cloud Management, Hyperconverged, Infrastructure, Virtualization, and Kubernetes.


  The Nutanix catalog on APIs.io includes 1 Spectral governance ruleset.


  Nutanix''s developer surface includes authentication, documentation, getting-started guide, changelog, engineering blog, support, signup flow, and 15 more developer resources.'
plans:
- name: Nutanix Plans Pricing
  plan_count: 5
  slug: nutanix-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Nutanix Rate Limits
  slug: nutanix-rate-limits
rules:
- name: Nutanix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: nutanix-jsonschema-spectral-rules
score:
  band: strong
  composite: 65.8
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 59.5
    developer_ergonomics: 58.7
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 68.4
  previous_composite: 65.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nutanix/refs/heads/main/screenshots/nutanix-2026-06-20T190530.png
security:
- kind: authentication
  name: Nutanix Authentication
  slug: nutanix-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nutanix Domain Security
  slug: nutanix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nutanix
tags:
- Cloud Management
- Hyperconverged
- Infrastructure
- Virtualization
- Kubernetes
- Database
website: https://www.nutanix.com
---
