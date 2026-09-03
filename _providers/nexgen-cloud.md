---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-09-03'
api_count: 3
apis:
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: 'Access keys authenticate S3-compatible object storage operations. Each key has an access ID and a secret. Generate access keys via this API or in the console, then use them to sign requests to bucket '
  name: NexGen Cloud Access Keys API
  slug: nexgen-cloud-access-keys-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Service liveness check for the billing API. Use to confirm the billing service is reachable.
  name: NexGen Cloud Alive API
  slug: nexgen-cloud-alive-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: API keys authenticate requests to the Hyperstack API. Generate keys in the console; each key is server-side and scoped to a specific environment. Rotate keys periodically and revoke any key whose secr
  name: NexGen Cloud API Key API
  slug: nexgen-cloud-api-key-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Bulk role assignments for organization members.
  name: NexGen Cloud Assigning Member Role API
  slug: nexgen-cloud-assigning-member-role-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Auth endpoints manage organization tokens, including changing the active organization on the current token. Use these endpoints when an account spans multiple organizations and you need to scope subse
  name: NexGen Cloud Auth API
  slug: nexgen-cloud-auth-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: The auto-topup API from NexGen Cloud — 2 operation(s) for auto-topup.
  name: NexGen Cloud Auto Topup API
  slug: nexgen-cloud-auto-topup-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Pre-trained foundation models available in AI Studio. These endpoints let you list available models, retrieve pricing, and fetch details for a specific base model.
  name: NexGen Cloud Base Models API
  slug: nexgen-cloud-base-models-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Beta Access APIs
  name: NexGen Cloud beta access API
  slug: nexgen-cloud-beta-access-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Billing endpoints expose your account's billing history, current credit balance, payment history, and usage costs. Use these to reconcile spend, build internal cost reports, or trigger alerts when bal
  name: NexGen Cloud Billing API
  slug: nexgen-cloud-billing-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: A bucket is an S3-compatible object storage container. Buckets are region-scoped and accessed via standard S3 SDKs once you have access keys. Use these endpoints to list and delete buckets, bucket cre
  name: NexGen Cloud Buckets API
  slug: nexgen-cloud-buckets-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Calculate endpoints return billing-rate breakdowns for specific resources. Provide a resource type and ID to retrieve its hourly cost, including pre- and post-discount components.
  name: NexGen Cloud Calculate API
  slug: nexgen-cloud-calculate-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Webhook callback registrations on virtual machines and volumes for state-change notifications.
  name: NexGen Cloud Callbacks API
  slug: nexgen-cloud-callbacks-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Cluster Event APIs
  name: NexGen Cloud cluster events API
  slug: nexgen-cloud-cluster-events-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: A cluster is a managed Kubernetes cluster on Hyperstack, control plane + worker nodes preconfigured for GPU workloads. Clusters are region-scoped and can attach data volumes via Container Storage Inte
  name: NexGen Cloud Clusters API
  slug: nexgen-cloud-clusters-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Compliance APIs
  name: NexGen Cloud Compliance API
  slug: nexgen-cloud-compliance-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Conversation threads and message history for AI Studio chat sessions. These endpoints let you create conversations, send messages, retrieve message history, and delete conversation threads.
  name: NexGen Cloud Conversations API
  slug: nexgen-cloud-conversations-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Credit endpoints retrieve your account's current credit balance. Credits are consumed by resource usage and replenished via payments or vouchers.
  name: NexGen Cloud Credit API
  slug: nexgen-cloud-credit-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Customer contract endpoints retrieve negotiated pricing terms applied to your account. Contracts override standard pricebook rates for the resources they cover.
  name: NexGen Cloud Customer Contract API
  slug: nexgen-cloud-customer-contract-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Aggregate account-level metrics for the calling user, VM and resource counts, recent activity.
  name: NexGen Cloud Dashboard API
  slug: nexgen-cloud-dashboard-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Deployment endpoints manage scripts that run during virtual machine boot to install dependencies, configure services, or prepare GPU workloads. Attach a deployment script to a VM at launch; the script
  name: NexGen Cloud Deployment API
  slug: nexgen-cloud-deployment-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: User email preference management
  name: NexGen Cloud Email Opt In Out API
  slug: nexgen-cloud-email-opt-in-out-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: 'Email preference endpoints control which optional email notifications Hyperstack sends to your account. Use them to read your current preferences and change them, individually or all at once. See the '
  name: NexGen Cloud Email Preferences API
  slug: nexgen-cloud-email-preferences-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: An environment is a logical container for resources within a region. Use environments to separate development, staging, and production resources, or to isolate per-team workloads. Most resource endpoi
  name: NexGen Cloud Environment API
  slug: nexgen-cloud-environment-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: FIP exclusion endpoints manage which virtual machines are exempt from automatic floating-IP detachment policies.
  name: NexGen Cloud FIP Exclusions API
  slug: nexgen-cloud-fip-exclusions-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Firewall Attachments APIs
  name: NexGen Cloud Firewall Attachment API
  slug: nexgen-cloud-firewall-attachment-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: 'A firewall is a set of inbound and outbound rules scoped to an environment. Attach a firewall to one or more virtual machines or Kubernetes clusters to control which network traffic each resource can '
  name: NexGen Cloud Firewalls API
  slug: nexgen-cloud-firewalls-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: 'A flavor is a machine type, its CPU count, memory, and GPU configuration. Flavors are region-specific. List flavors before deploying a virtual machine to find one available in your target region with '
  name: NexGen Cloud Flavor API
  slug: nexgen-cloud-flavor-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: A floating IP is a static public IPv4 address that can be assigned to a virtual machine. Floating IPs persist across VM lifecycle events, detach from one VM and reattach to another to keep the address
  name: NexGen Cloud Floating IP API
  slug: nexgen-cloud-floating-ip-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: GPU model availability and stock per region.
  name: NexGen Cloud GPU API
  slug: nexgen-cloud-gpu-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Service liveness check for object storage. Use to confirm the object-storage service is reachable.
  name: NexGen Cloud Health API
  slug: nexgen-cloud-health-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: An image is the operating system disk a virtual machine boots from. Images include Ubuntu, Rocky Linux, and other distributions, with optional pre-installed CUDA or AI/ML frameworks. Images are region
  name: NexGen Cloud Image API
  slug: nexgen-cloud-image-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Text-to-image and image-to-image generation. Submit a generation or edit request, then poll the task endpoint to retrieve the resulting image. Use a presigned upload URL to supply a source image for e
  name: NexGen Cloud Image Generation API
  slug: nexgen-cloud-image-generation-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: OpenAI-compatible chat completions endpoint for running inference against deployed models. Use this endpoint to send prompts and receive generated responses.
  name: NexGen Cloud Inference API
  slug: nexgen-cloud-inference-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Invite endpoints add and manage users within an organization. Invite a user by email; they accept the invitation and gain access to the organization with the role you specified.
  name: NexGen Cloud Invite API
  slug: nexgen-cloud-invite-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: A keypair is an SSH public/private key pair used to authenticate into virtual machines after deployment. Generate the keypair locally, register the public key with Hyperstack, then reference the keypa
  name: NexGen Cloud Keypair API
  slug: nexgen-cloud-keypair-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Collections of your own documents that models can search at inference time.
  name: NexGen Cloud Knowledge Bases API
  slug: nexgen-cloud-knowledge-bases-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: User-deployed models and model aliases. These endpoints let you deploy and undeploy models, list available models, manage model aliases, and retrieve deployment details.
  name: NexGen Cloud Models API
  slug: nexgen-cloud-models-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: 'Organization endpoints manage organization-level metadata: name, members, and configuration. Most users belong to a single organization; multi-organization accounts use these endpoints to switch conte'
  name: NexGen Cloud Organization API
  slug: nexgen-cloud-organization-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Organization-level summary and resource usage metrics for the AI Studio account.
  name: NexGen Cloud Overview API
  slug: nexgen-cloud-overview-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Partner config fetch endpoint
  name: NexGen Cloud Partner Config API
  slug: nexgen-cloud-partner-config-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Payment endpoints initiate and retrieve payments. Use these to add funds to your account programmatically or to fetch receipts for reconciliation.
  name: NexGen Cloud Payment API
  slug: nexgen-cloud-payment-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Permission endpoints list the granular permissions defined by Hyperstack. Permissions compose into RBAC roles, which are assigned to organization members. List permissions to discover what's available
  name: NexGen Cloud Permission API
  slug: nexgen-cloud-permission-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Authorization policies that bind permissions to roles.
  name: NexGen Cloud Policy API
  slug: nexgen-cloud-policy-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Pricebook endpoints expose Hyperstack's pricing for compute, storage, and networking resources. Use these to estimate costs before deploying or to surface live pricing in your application.
  name: NexGen Cloud Pricebook API
  slug: nexgen-cloud-pricebook-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Saved virtual-machine deployment configurations that can be reused across new VMs.
  name: NexGen Cloud Profile API
  slug: nexgen-cloud-profile-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: RBAC role endpoints create, list, update, and delete custom roles. A role is a named bundle of permissions that you can assign to organization members. Built-in roles (`admin`, `member`, `viewer`) cov
  name: NexGen Cloud RBAC Role API
  slug: nexgen-cloud-rbac-role-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: A region is a geographic location where Hyperstack hosts compute and storage. Resources are region-scoped, virtual machines, volumes, snapshots, and firewalls all belong to exactly one region. List re
  name: NexGen Cloud Region API
  slug: nexgen-cloud-region-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Regions where object storage is available.
  name: NexGen Cloud Regions API
  slug: nexgen-cloud-regions-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Security Rule APIs
  name: NexGen Cloud Security Rules API
  slug: nexgen-cloud-security-rules-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Snapshot Events APIs
  name: NexGen Cloud snapshot events API
  slug: nexgen-cloud-snapshot-events-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: A snapshot is a point-in-time copy of a virtual machine or volume. Snapshots are stored in the same region as the source resource and can be used to clone, restore, or migrate state. Snapshot creation
  name: NexGen Cloud Snapshots API
  slug: nexgen-cloud-snapshots-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: GPU and CPU stock availability per flavor and region. Use before deployment to confirm capacity.
  name: NexGen Cloud Stock API
  slug: nexgen-cloud-stock-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Reusable system prompt templates for AI Studio deployments. These endpoints let you create, retrieve, update, and delete system prompts that can be applied to deployed models.
  name: NexGen Cloud System Prompts API
  slug: nexgen-cloud-system-prompts-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: A template is a saved virtual machine configuration that you can reuse to deploy identical VMs without re-specifying every parameter. Templates capture flavor, image, keypair, networking, and metadata
  name: NexGen Cloud Template API
  slug: nexgen-cloud-template-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Account-level user information and billing identity.
  name: NexGen Cloud User API
  slug: nexgen-cloud-user-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: User Consent endpoints record each user's grant or revoke decision for a given consent type (e.g. marketing communications, data-sharing terms). Use these endpoints to read what consent has been grant
  name: NexGen Cloud User Consent API
  slug: nexgen-cloud-user-consent-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: User Consent management
  name: NexGen Cloud User Consent Events API
  slug: nexgen-cloud-user-consent-events-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: User-specific configuration choices (profile preferences, defaults).
  name: NexGen Cloud User Detail Choice API
  slug: nexgen-cloud-user-detail-choice-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Permissions assigned to specific users in the calling organization.
  name: NexGen Cloud User Permission API
  slug: nexgen-cloud-user-permission-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: A virtual machine on Hyperstack is a single-tenant compute instance backed by dedicated GPU and CPU resources. Each VM runs in a region, attaches a root volume and optional data volumes, and is protec
  name: NexGen Cloud Virtual Machine API
  slug: nexgen-cloud-virtual-machine-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Virtual Machine Event APIs
  name: NexGen Cloud virtual machine events API
  slug: nexgen-cloud-virtual-machine-events-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Console-access URLs for connecting to a virtual machine over VNC.
  name: NexGen Cloud VNC URL API
  slug: nexgen-cloud-vnc-url-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: A volume is persistent block storage that attaches to a virtual machine. Volumes are region-scoped and can be detached and reattached to other VMs in the same region. Snapshots capture a point-in-time
  name: NexGen Cloud Volume API
  slug: nexgen-cloud-volume-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Volume attachment endpoints manage the binding between a volume and a virtual machine. A volume can be attached to one VM at a time. Detach a volume before attaching it elsewhere; the data persists on
  name: NexGen Cloud Volume Attachment API
  slug: nexgen-cloud-volume-attachment-api
- baseURL: https://infrahub-api.nexgencloud.com/v1
  baseurl_source: declared
  description: Voucher endpoints redeem promotional codes to add credit to your account. Vouchers are single-use.
  name: NexGen Cloud Vouchers API
  slug: nexgen-cloud-vouchers-api
artifact_total: 72
asyncapis:
- description: ''
  name: Nexgen Cloud Webhooks
  slug: nexgen-cloud-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/nexgen-cloud-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nexgen-cloud-hyperstack-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nexgen-cloud-ai-studio-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.nexgencloud.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.hyperstack.cloud/docs/intro
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hyperstack.cloud/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hyperstack.cloud/docs/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hyperstack.cloud/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.hyperstack.cloud/docs/support
- group: company
  title: ''
  type: Blog
  url: https://www.hyperstack.cloud/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NexGenCloud
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hyperstack.cloud/gpu-pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.hyperstack.cloud/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hyperstack.cloud/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hyperstack.cloud/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hyperstack.cloud/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.hyperstack.cloud/docs/release-notes
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nexgen-cloud-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nexgen-cloud-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/nexgen-cloud-api-catalog.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nexgen-cloud-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/nexgen-cloud-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/nexgen-cloud-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nexgen-cloud-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nexgen-cloud-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nexgen-cloud-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nexgen-cloud-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nexgen-cloud-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nexgen-cloud-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nexgen-cloud-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nexgen-cloud-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nexgen-cloud-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/nexgen-cloud-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nexgen-cloud-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nexgen-cloud-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nexgen-cloud-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nexgen-cloud-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: NexGen Cloud Limited is a UK-headquartered AI cloud and GPU infrastructure provider. Its on-demand platform, Hyperstack, sells NVIDIA GPU and CPU virtual machines, managed Kubernetes clusters, block storage volumes, S3-compatible object storage and high-speed networking across three regions (CANADA-1, NORWAY-1, US-1), billed per minute. A second product, Hyperstack AI Studio, provides an OpenAI-compatible inference API over a catalog of third-party hosted text and image models, with playgrounds, system prompts, conversations and knowledge bases. The company also sells Secure Private Cloud, a single-tenant sovereign supercluster offering. Everything Hyperstack does in the console is available through a documented REST API at infrahub-api.nexgencloud.com, with official Python, Go, JavaScript and TypeScript SDKs, a Terraform provider, a Kubernetes CSI driver, a hosted read-only documentation MCP server and a self-hosted API MCP server.
image: https://www.hyperstack.cloud/hubfs/hyperstack_2023/home/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: NexGen Cloud MCP Server
  slug: nexgen-cloud-mcp-server
modified: '2026-08-26'
name: NexGen Cloud
nav: Providers
network: true
overview: 'NexGen Cloud publishes 65 APIs on the [APIs.io](https://apis.io/) network, including Access Keys API, Alive API, API Key API, and 62 more. Tagged areas include Company, Cloud, GPU, Artificial Intelligence, and Machine-Learning.


  The NexGen Cloud catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  NexGen Cloud''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Nexgen Cloud Plans Pricing
  plan_count: 4
  slug: nexgen-cloud-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Nexgen Cloud Rate Limits
  slug: nexgen-cloud-rate-limits
score:
  band: exemplar
  composite: 66.9
  coverage:
    artifact_dirs: 23
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 69.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 63.2
  previous_composite: 66.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 65
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nexgen-cloud/refs/heads/main/screenshots/nexgen-cloud-2026-09-02T150747.png
security:
- kind: authentication
  name: Nexgen Cloud Authentication
  slug: nexgen-cloud-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Nexgen Cloud Domain Security
  slug: nexgen-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Nexgen Cloud Trust Center
  slug: nexgen-cloud-trust-center
  summary_line: SOC 2, ISO 27001
slug: nexgen-cloud
tags:
- Company
- Cloud
- GPU
- Artificial Intelligence
- Machine-Learning
- Infrastructure
- Compute
- Kubernetes
- Storage
- Inference
- Virtual Machines
- Sovereign AI
website: https://www.nexgencloud.com/
---
