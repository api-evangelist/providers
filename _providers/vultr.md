---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 182
  human_in_the_loop: 11
  name: Vultr Agentic Access
  operation_count: 334
  slug: vultr-agentic-access
  summary_line: 334 operations · 182 acting · 11 human-in-the-loop
api_count: 6
apis:
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Read-only information about your [user account](https://my.vultr.com/settings/#settingsprofile) and [billing](https://my.vultr.com/billing/#billinghistory) information.
  name: Vultr Account API
  slug: vultr-account-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: '[One-Click](https://www.vultr.com/features/one-click-apps/) and [Marketplace](https://www.vultr.com/marketplace/) Applications are ready-to-run with minimal configuration. We have an extensive [docume'
  name: Vultr Application API
  slug: vultr-application-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: A backup is a scheduled, automatic, point-in-time image of an instance. We do not stop the instance when taking a backup. Booting from a backup is similar to rebooting after a non-graceful restart. [S
  name: Vultr Backup API
  slug: vultr-backup-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: '[Bare Metal](https://www.vultr.com/products/bare-metal/) servers give you access to the underlying physical hardware in a single-tenant environment without a virtualization layer.'
  name: Vultr Baremetal API
  slug: vultr-baremetal-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Read-only [billing](https://my.vultr.com/billing/#billinghistory) information for your [user account](https://my.vultr.com/settings/#settingsprofile).
  name: Vultr Billing API
  slug: vultr-billing-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: '[Block Storage](https://www.vultr.com/products/block-storage/) volumes are highly-available, redundant, SSD backed, and expandable from 10 GB to 10,000 GB. Block storage volumes can be formatted with '
  name: Vultr Block API
  slug: vultr-block-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Store and manage public and private container images for rapid deployment to Vultr Managed Kubernetes.
  name: Vultr Container Registry API
  slug: vultr-container-registry-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: 'Vultr offers [free DNS hosting](https://www.vultr.com/docs/introduction-to-vultr-dns) for customers'' domains. The nameservers are on an AnyCAST network and ensure fast DNS resolution. When you manage '
  name: Vultr Dns API
  slug: vultr-dns-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: 'Vultr offers a [web-based firewall](https://www.vultr.com/docs/vultr-firewall) solution to protect one or more compute instances. [Firewall groups](https://my.vultr.com/firewall/) can manage multiple '
  name: Vultr Firewall API
  slug: vultr-firewall-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Manage temporary role assumptions
  name: Vultr IAM Assumed Roles API
  slug: vultr-iam-assumed-roles-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: View available IAM endpoint-to-action mappings
  name: Vultr IAM Endpoint Actions API
  slug: vultr-iam-endpoint-actions-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Non-SCIM group management endpoints
  name: Vultr IAM Groups API
  slug: vultr-iam-groups-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Endpoints for managing IAM policies within an organization
  name: Vultr IAM Policies API
  slug: vultr-iam-policies-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Manage direct policy attachments to groups
  name: Vultr IAM Policy-Group Mappings API
  slug: vultr-iam-policy-group-mappings-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Manage direct policy attachments to users
  name: Vultr IAM Policy-User Mappings API
  slug: vultr-iam-policy-user-mappings-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Manage role assignments to groups
  name: Vultr IAM Role-Group Mappings API
  slug: vultr-iam-role-group-mappings-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Manage the attachment and detachment of IAM policies to roles
  name: Vultr IAM Role-Policy Mappings API
  slug: vultr-iam-role-policy-mappings-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Manage trust relationships between roles
  name: Vultr IAM Role Trusts API
  slug: vultr-iam-role-trusts-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Manage role assignments to users
  name: Vultr IAM Role-User Mappings API
  slug: vultr-iam-role-user-mappings-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Endpoints for managing IAM roles within an organization
  name: Vultr IAM Roles API
  slug: vultr-iam-roles-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Vultr [Cloud instances](https://www.vultr.com/products/cloud-compute/) can be [deployed](https://my.vultr.com/) with your preferred operating system or pre-installed application in seconds. [High Freq
  name: Vultr Instances API
  slug: vultr-instances-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: '[Upload](https://www.vultr.com/features/upload-iso/) and boot instances from your ISO, or choose one from our [public ISO library](https://my.vultr.com/iso/public/). See our [ISO documentation](https:'
  name: Vultr Iso API
  slug: vultr-iso-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Vultr Kubernetes Engine is a managed Kubernetes offering.
  name: Vultr Kubernetes API
  slug: vultr-kubernetes-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: '[Load Balancers](https://www.vultr.com/docs/vultr-load-balancers) sit in front of your application and distribute incoming traffic across multiple Instances. When you control the load balancer via the'
  name: Vultr Load Balancer API
  slug: vultr-load-balancer-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Endpoints for viewing logs and for managing an audit logs subscription
  name: Vultr Logs API
  slug: vultr-logs-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: '[Vultr Managed Databases](https://www.vultr.com/docs/vultr-managed-databases/) is a managed database offering supporting MySQL, PostgreSQL, FerretDB + PostgreSQL, and Redis.'
  name: Vultr Managed Databases API
  slug: vultr-managed-databases-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Manage invitations for users to join organizations
  name: Vultr Organization Invitations API
  slug: vultr-organization-invitations-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Manage users inside organizations (membership, roles, suspensions)
  name: Vultr Organization Membership Management API
  slug: vultr-organization-membership-management-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Manage organizations
  name: Vultr Organizations API
  slug: vultr-organizations-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: We have a wide range of [operating systems](https://www.vultr.com/features/operating-systems/) available to deploy server instances. You can also [upload an ISO](#tag/iso) or choose from our public IS
  name: Vultr Os API
  slug: vultr-os-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: A Plan is a particular configuration of vCPU, RAM, SSD, and bandwidth to deploy an [Instance](#tag/instances). Not all Plans are available in all [Regions](#tag/region). You can browse plans in the [C
  name: Vultr Plans API
  slug: vultr-plans-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: '[Private Networks](https://www.vultr.com/docs/configuring-private-network) are fully isolated networks accessible only by instances on your account. Each private network is only available in one Regio'
  name: Vultr private Networks API
  slug: vultr-private-networks-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Instances can be deployed in many [Regions](https://www.vultr.com/features/datacenter-locations/) on multiple continents. Choose any of our worldwide locations to deploy servers near your office or cu
  name: Vultr Region API
  slug: vultr-region-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: IP addresses can be [reserved](https://my.vultr.com/network/) and moved between [instances](#tag/instances). Reserved IPs can also be used as [floating addresses](https://www.vultr.com/docs/high-avail
  name: Vultr Reserved Ip API
  slug: vultr-reserved-ip-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: '[Object Storage](https://www.vultr.com/docs/vultr-object-storage) is S3 API compatible. Objects uploaded to object storage can be accessed privately or publicly on the web. Object storage supports a v'
  name: Vultr S3 API
  slug: vultr-s3-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: SCIM 2.0 compliant endpoints for managing groups
  name: Vultr SCIM Groups API
  slug: vultr-scim-groups-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Manage SCIM enablement and tokens for organizations
  name: Vultr SCIM Settings API
  slug: vultr-scim-settings-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: SCIM 2.0 compliant endpoints for managing users
  name: Vultr SCIM Users API
  slug: vultr-scim-users-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: A snapshot is a point-in-time image of an instance. We do not stop the instance when taking a snapshot. Booting from a snapshot is similar to rebooting after a non-graceful restart. Snapshots are phys
  name: Vultr Snapshot API
  slug: vultr-snapshot-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: You can add [SSH keys](https://www.vultr.com/docs/how-do-i-generate-ssh-keys/) to your [account](https://my.vultr.com/settings/#settingssshkeys), which can be copied to new instances when first deploy
  name: Vultr Ssh API
  slug: vultr-ssh-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: 'Vultr allows you to assign [two types of scripts to a server](https://www.vultr.com/docs/vultr-startup-scripts-quickstart-guide). Boot scripts configure new deployments, and PXE scripts automatically '
  name: Vultr Startup API
  slug: vultr-startup-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Endpoints for viewing user-specific IAM resources (groups, roles, policies)
  name: Vultr User Resources API
  slug: vultr-user-resources-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Vultr supports [multiple users](https://my.vultr.com/settings/#settingsusers) in each account, and each user has [individual access permissions](https://my.vultr.com/users/manage/?USERID=new). Users h
  name: Vultr Users API
  slug: vultr-users-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: '[VPCs](https://www.vultr.com/docs/how-to-create-a-vultr-virtual-private-cloud-vpc/) are fully isolated networks accessible only by instances on your account. Each VPC is only available in one region a'
  name: Vultr VPC2 API
  slug: vultr-vpc2-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: '[VPCs](https://www.vultr.com/docs/how-to-create-a-vultr-virtual-private-cloud-vpc/) are fully isolated networks accessible only by instances on your account. Each VPC is only available in one region a'
  name: Vultr VPCs API
  slug: vultr-vpcs-api
- baseURL: https://api.vultr.com/v2
  baseurl_source: declared
  description: Sub-accounts are separate Vultr accounts that are directly linked to your account. These accounts function similarly to normal Vultr accounts with some additional billing and administrative features a
  name: Vultr Sub Account API
  slug: vultr-sub-account-api
artifact_total: 71
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/rate-limits/vultr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vultr-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/agentic-access/vultr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vultr-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/rules/vultr-rules.yml
  title: ''
  type: Spectral
  url: rules/vultr-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/json-ld/vultr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vultr-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/vocabulary/vultr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vultr-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/data-model/vultr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vultr-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/errors/vultr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vultr-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/conformance/vultr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vultr-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/llms/vultr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vultr-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/well-known/vultr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vultr-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/hosts/vultr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vultr-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/vendors/vultr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vultr-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/packages/vultr-packages.yml
  title: ''
  type: SDKs
  url: packages/vultr-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/packages/vultr-packages.yml
  title: ''
  type: Packages
  url: packages/vultr-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vultr.com/inference-cookbook/rocm/getting-started/first-deployment
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/authentication/vultr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vultr-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/security/vultr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vultr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vultr.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vultr.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vultr
- group: company
  title: ''
  type: Blog
  url: https://blogs.vultr.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.vultr.com/platform/api-opensource-changelog
- group: build
  title: ''
  type: CLI
  url: https://docs.vultr.com/reference/vultr-cli
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vultr/refs/heads/main/mcp/vultr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/vultr-mcp.yml
created: '2026-10-13'
description: Vultr is a global cloud infrastructure provider offering Cloud Compute, Bare Metal, GPU, Kubernetes (VKE), Managed Databases, S3-compatible Object Storage, Block Storage, networking (VPC, load balancers, DNS, firewalls) and Serverless Inference across worldwide regions. Everything in the customer portal is scriptable through the RESTful Vultr API v2 at api.vultr.com/v2 (Bearer API key, cursor pagination), with a separate IAM & SCIM Management API, an official hosted MCP server at mcp.vultr.com, a first-party CLI and SDKs in Go, Node, Python, PHP, Ruby, Java and C#.
json_schemas:
- name: AssumedRoleSession
  property_count: 10
  slug: vultr-assumed-role-session
- name: baremetal
  property_count: 22
  slug: vultr-baremetal
- name: create_baremetal_request
  property_count: 21
  slug: vultr-create-baremetal-request
- name: create_database_request
  property_count: 15
  slug: vultr-create-database-request
- name: create_instance_request
  property_count: 29
  slug: vultr-create-instance-request
- name: ExtendedLog
  property_count: 21
  slug: vultr-extended-log
- name: firewall-rule
  property_count: 9
  slug: vultr-firewall-rule
- name: instance
  property_count: 27
  slug: vultr-instance
- name: loadbalancer
  property_count: 13
  slug: vultr-loadbalancer
- name: log-meta
  property_count: 5
  slug: vultr-log-meta
- name: log
  property_count: 6
  slug: vultr-log
- name: object-storage
  property_count: 9
  slug: vultr-object-storage
- name: RoleTrust
  property_count: 10
  slug: vultr-role-trust
- name: SCIMUser
  property_count: 11
  slug: vultr-scimuser
- name: update_advanced_options_request
  property_count: 44
  slug: vultr-update-advanced-options-request
- name: update_database_request
  property_count: 14
  slug: vultr-update-database-request
- name: update_instance_request
  property_count: 22
  slug: vultr-update-instance-request
- name: vke-cluster
  property_count: 11
  slug: vultr-vke-cluster
jsonld:
- class_count: 120
  name: Vultr Context
  property_count: 305
  slug: vultr-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.vultr.com requiring OAuth.
  name: Vultr MCP Server
  slug: vultr-mcp-server
modified: '2026-10-13'
name: Vultr
nav: Providers
network: true
overview: 'Vultr publishes 46 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Application API, Backup API, and 43 more. Tagged areas include Company, Cloud, Infrastructure, Compute, and Object Storage.


  The Vultr catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Vultr''s developer surface includes getting-started guide, authentication, documentation, engineering blog, changelog, CLI, and 18 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 1
  name: Vultr Rate Limits
  slug: vultr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Vultr API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 3
  slug: vultr-rules
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 71.8
    catalog_earned_first_party: 8.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 66.3
    developer_ergonomics: 50.0
    discoverability: 76.7
    operational_transparency: 42.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 46
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Vultr Authentication
  slug: vultr-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vultr Domain Security
  slug: vultr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vultr
tags:
- Company
- Cloud
- Infrastructure
- Compute
- Object Storage
- Kubernetes
- Database
- GPU
- MCP
website: https://www.vultr.com
---
