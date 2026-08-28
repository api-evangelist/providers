---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.2
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 198
  human_in_the_loop: 4
  name: Crusoe Agentic Access
  operation_count: 464
  slug: crusoe-agentic-access
  summary_line: 464 operations · 198 acting · 4 human-in-the-loop
api_count: 63
apis:
- description: OpenAI-compatible inference API from the Crusoe Intelligence Foundry. Send chat/completions and embeddings requests to Crusoe-hosted open models (DeepSeek, Llama, Gemma, GLM, Kimi, Nemotron and others
  name: Crusoe Managed Inference API
  slug: crusoe-managed-inference-api
- description: First-party, read-only Model Context Protocol server published by Crusoe as the npm package @crusoeai/cloud-mcp and as a downloadable Claude Desktop extension bundle. Runs over stdio, inherits credent
  name: Crusoe Cloud MCP Server
  slug: crusoe-cloud-mcp-server
- description: The Audit Logs API from Crusoe — 1 operation(s) for audit logs.
  name: Crusoe Audit Logs API
  slug: crusoe-audit-logs-api
- description: The AutoCluster Operations API from Crusoe — 2 operation(s) for autocluster operations.
  name: Crusoe AutoCluster Operations API
  slug: crusoe-autocluster-operations-api
- description: The AutoClusters API from Crusoe — 2 operation(s) for autoclusters.
  name: Crusoe Auto Clusters API
  slug: crusoe-autoclusters-api
- description: The Billing API from Crusoe — 3 operation(s) for billing.
  name: Crusoe Billing API
  slug: crusoe-billing-api
- description: The Capacities API from Crusoe — 1 operation(s) for capacities.
  name: Crusoe Capacities API
  slug: crusoe-capacities-api
- description: The Ccr API from Crusoe — 8 operation(s) for ccr.
  name: Crusoe Ccr API
  slug: crusoe-ccr-api
- description: The Container Registry API from Crusoe — 8 operation(s) for container registry.
  name: Crusoe Container Registry API
  slug: crusoe-container-registry-api
- description: The Custom Image Operations API from Crusoe — 2 operation(s) for custom image operations.
  name: Crusoe Custom Image Operations API
  slug: crusoe-custom-image-operations-api
- description: The CustomImages API from Crusoe — 3 operation(s) for customimages.
  name: Crusoe Custom Images API
  slug: crusoe-customimages-api
- description: The Disk Operations API from Crusoe — 2 operation(s) for disk operations.
  name: Crusoe Disk Operations API
  slug: crusoe-disk-operations-api
- description: The Disks API from Crusoe — 2 operation(s) for disks.
  name: Crusoe Disks API
  slug: crusoe-disks-api
- description: The Entities API from Crusoe — 1 operation(s) for entities.
  name: Crusoe Entities API
  slug: crusoe-entities-api
- description: The Feature Flags API from Crusoe — 1 operation(s) for feature flags.
  name: Crusoe Feature Flags API
  slug: crusoe-feature-flags-api
- description: The Foundry API from Crusoe — 16 operation(s) for foundry.
  name: Crusoe Foundry API
  slug: crusoe-foundry-api
- description: The IB Networks API from Crusoe — 2 operation(s) for ib networks.
  name: Crusoe IB Networks API
  slug: crusoe-ib-networks-api
- description: The IB Partitions API from Crusoe — 2 operation(s) for ib partitions.
  name: Crusoe IB Partitions API
  slug: crusoe-ib-partitions-api
- description: The Identities API from Crusoe — 1 operation(s) for identities.
  name: Crusoe Identities API
  slug: crusoe-identities-api
- description: The Images API from Crusoe — 2 operation(s) for images.
  name: Crusoe Images API
  slug: crusoe-images-api
- description: The Instance Groups API from Crusoe — 2 operation(s) for instance groups.
  name: Crusoe Instance Groups API
  slug: crusoe-instance-groups-api
- description: The Instance Templates API from Crusoe — 2 operation(s) for instance templates.
  name: Crusoe Instance Templates API
  slug: crusoe-instance-templates-api
- description: The Internal Load Balancer Operations API from Crusoe — 2 operation(s) for internal load balancer operations.
  name: Crusoe Internal Load Balancer Operations API
  slug: crusoe-internal-load-balancer-operations-api
- description: The Internal Load Balancers API from Crusoe — 2 operation(s) for internal load balancers.
  name: Crusoe Internal Load Balancers API
  slug: crusoe-internal-load-balancers-api
- description: The Kubernetes Cluster Operations API from Crusoe — 2 operation(s) for kubernetes cluster operations.
  name: Crusoe Kubernetes Cluster Operations API
  slug: crusoe-kubernetes-cluster-operations-api
- description: The Kubernetes Clusters API from Crusoe — 3 operation(s) for kubernetes clusters.
  name: Crusoe Kubernetes Clusters API
  slug: crusoe-kubernetes-clusters-api
- description: The Kubernetes Node Pool Operations API from Crusoe — 2 operation(s) for kubernetes node pool operations.
  name: Crusoe Kubernetes Node Pool Operations API
  slug: crusoe-kubernetes-node-pool-operations-api
- description: The Kubernetes Node Pools API from Crusoe — 5 operation(s) for kubernetes node pools.
  name: Crusoe Kubernetes Node Pools API
  slug: crusoe-kubernetes-node-pools-api
- description: The Kubernetes Support Access API from Crusoe — 1 operation(s) for kubernetes support access.
  name: Crusoe Kubernetes Support Access API
  slug: crusoe-kubernetes-support-access-api
- description: The Kubernetes Versions API from Crusoe — 1 operation(s) for kubernetes versions.
  name: Crusoe Kubernetes Versions API
  slug: crusoe-kubernetes-versions-api
- description: The LimitedUsageAPIKey API from Crusoe — 1 operation(s) for limitedusageapikey.
  name: Crusoe Limited Usage API Key API
  slug: crusoe-limitedusageapikey-api
- description: The Load Balancer Operations API from Crusoe — 2 operation(s) for load balancer operations.
  name: Crusoe Load Balancer Operations API
  slug: crusoe-load-balancer-operations-api
- description: The Load Balancers API from Crusoe — 2 operation(s) for load balancers.
  name: Crusoe Load Balancers API
  slug: crusoe-load-balancers-api
- description: The Locations API from Crusoe — 1 operation(s) for locations.
  name: Crusoe Locations API
  slug: crusoe-locations-api
- description: The MFA API from Crusoe — 1 operation(s) for mfa.
  name: Crusoe MFA API
  slug: crusoe-mfa-api
- description: The NVLink Domains API from Crusoe — 1 operation(s) for nvlink domains.
  name: Crusoe NVLink Domains API
  slug: crusoe-nvlink-domains-api
- description: The Observability API from Crusoe — 5 operation(s) for observability.
  name: Crusoe Observability API
  slug: crusoe-observability-api
- description: The Projects API from Crusoe — 2 operation(s) for projects.
  name: Crusoe Projects API
  slug: crusoe-projects-api
- description: The Quotas API from Crusoe — 2 operation(s) for quotas.
  name: Crusoe Quotas API
  slug: crusoe-quotas-api
- description: The Reservations API from Crusoe — 4 operation(s) for reservations.
  name: Crusoe Reservations API
  slug: crusoe-reservations-api
- description: The RoleBindings API from Crusoe — 2 operation(s) for rolebindings.
  name: Crusoe Role Bindings API
  slug: crusoe-rolebindings-api
- description: The Roles API from Crusoe — 1 operation(s) for roles.
  name: Crusoe Roles API
  slug: crusoe-roles-api
- description: The S3Buckets API from Crusoe — 7 operation(s) for s3buckets.
  name: Crusoe S3 Buckets API
  slug: crusoe-s3buckets-api
- description: The S3Keys API from Crusoe — 2 operation(s) for s3keys.
  name: Crusoe S3 Keys API
  slug: crusoe-s3keys-api
- description: The SCIM API from Crusoe — 4 operation(s) for scim.
  name: Crusoe SCIM API
  slug: crusoe-scim-api
- description: The Slurm Cluster Operations API from Crusoe — 2 operation(s) for slurm cluster operations.
  name: Crusoe Slurm Cluster Operations API
  slug: crusoe-slurm-cluster-operations-api
- description: The Slurm Clusters API from Crusoe — 2 operation(s) for slurm clusters.
  name: Crusoe Slurm Clusters API
  slug: crusoe-slurm-clusters-api
- description: The Slurm Nodeset Operations API from Crusoe — 2 operation(s) for slurm nodeset operations.
  name: Crusoe Slurm Nodeset Operations API
  slug: crusoe-slurm-nodeset-operations-api
- description: The Slurm Nodesets API from Crusoe — 2 operation(s) for slurm nodesets.
  name: Crusoe Slurm Nodesets API
  slug: crusoe-slurm-nodesets-api
- description: The Snapshot Operations API from Crusoe — 2 operation(s) for snapshot operations.
  name: Crusoe Snapshot Operations API
  slug: crusoe-snapshot-operations-api
- description: The Snapshots API from Crusoe — 2 operation(s) for snapshots.
  name: Crusoe Snapshots API
  slug: crusoe-snapshots-api
- description: The SSH Keys API from Crusoe — 1 operation(s) for ssh keys.
  name: Crusoe SSH Keys API
  slug: crusoe-ssh-keys-api
- description: The SSO API from Crusoe — 3 operation(s) for sso.
  name: Crusoe SSO API
  slug: crusoe-sso-api
- description: The Tokens API from Crusoe — 1 operation(s) for tokens.
  name: Crusoe Tokens API
  slug: crusoe-tokens-api
- description: The Usage API from Crusoe — 3 operation(s) for usage.
  name: Crusoe Usage API
  slug: crusoe-usage-api
- description: The VM Operations API from Crusoe — 2 operation(s) for vm operations.
  name: Crusoe VM Operations API
  slug: crusoe-vm-operations-api
- description: The VMs API from Crusoe — 6 operation(s) for vms.
  name: Crusoe V Ms API
  slug: crusoe-vms-api
- description: The VPC Firewall Rule Operations API from Crusoe — 2 operation(s) for vpc firewall rule operations.
  name: Crusoe VPC Firewall Rule Operations API
  slug: crusoe-vpc-firewall-rule-operations-api
- description: The VPC Firewall Rules API from Crusoe — 2 operation(s) for vpc firewall rules.
  name: Crusoe VPC Firewall Rules API
  slug: crusoe-vpc-firewall-rules-api
- description: The VPC Network Operations API from Crusoe — 2 operation(s) for vpc network operations.
  name: Crusoe VPC Network Operations API
  slug: crusoe-vpc-network-operations-api
- description: The VPC Networks API from Crusoe — 2 operation(s) for vpc networks.
  name: Crusoe VPC Networks API
  slug: crusoe-vpc-networks-api
- description: The VPC Subnet Operations API from Crusoe — 2 operation(s) for vpc subnet operations.
  name: Crusoe VPC Subnet Operations API
  slug: crusoe-vpc-subnet-operations-api
- description: The VPC Subnets API from Crusoe — 2 operation(s) for vpc subnets.
  name: Crusoe VPC Subnets API
  slug: crusoe-vpc-subnets-api
artifact_total: 132
asyncapis:
- description: ''
  name: Crusoe Webhooks
  slug: crusoe-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Crusoe Audit Logs API
  slug: open-crusoe-audit-logs-api
- collection_type: open
  name: Crusoe AutoCluster Operations API
  slug: open-crusoe-autocluster-operations-api
- collection_type: open
  name: Crusoe Auto Clusters API
  slug: open-crusoe-autoclusters-api
- collection_type: open
  name: Crusoe Billing API
  slug: open-crusoe-billing-api
- collection_type: open
  name: Crusoe Capacities API
  slug: open-crusoe-capacities-api
- collection_type: open
  name: Crusoe Ccr API
  slug: open-crusoe-ccr-api
- collection_type: open
  name: Crusoe Container Registry API
  slug: open-crusoe-container-registry-api
- collection_type: open
  name: Crusoe Custom Image Operations API
  slug: open-crusoe-custom-image-operations-api
- collection_type: open
  name: Crusoe Custom Images API
  slug: open-crusoe-customimages-api
- collection_type: open
  name: Crusoe Disk Operations API
  slug: open-crusoe-disk-operations-api
- collection_type: open
  name: Crusoe Disks API
  slug: open-crusoe-disks-api
- collection_type: open
  name: Crusoe Entities API
  slug: open-crusoe-entities-api
- collection_type: open
  name: Crusoe Feature Flags API
  slug: open-crusoe-feature-flags-api
- collection_type: open
  name: Crusoe Foundry API
  slug: open-crusoe-foundry-api
- collection_type: open
  name: Crusoe IB Networks API
  slug: open-crusoe-ib-networks-api
- collection_type: open
  name: Crusoe IB Partitions API
  slug: open-crusoe-ib-partitions-api
- collection_type: open
  name: Crusoe Identities API
  slug: open-crusoe-identities-api
- collection_type: open
  name: Crusoe Images API
  slug: open-crusoe-images-api
- collection_type: open
  name: Crusoe Instance Groups API
  slug: open-crusoe-instance-groups-api
- collection_type: open
  name: Crusoe Instance Templates API
  slug: open-crusoe-instance-templates-api
- collection_type: open
  name: Crusoe Internal Load Balancer Operations API
  slug: open-crusoe-internal-load-balancer-operations-api
- collection_type: open
  name: Crusoe Internal Load Balancers API
  slug: open-crusoe-internal-load-balancers-api
- collection_type: open
  name: Crusoe Kubernetes Cluster Operations API
  slug: open-crusoe-kubernetes-cluster-operations-api
- collection_type: open
  name: Crusoe Kubernetes Clusters API
  slug: open-crusoe-kubernetes-clusters-api
- collection_type: open
  name: Crusoe Kubernetes Node Pool Operations API
  slug: open-crusoe-kubernetes-node-pool-operations-api
- collection_type: open
  name: Crusoe Kubernetes Node Pools API
  slug: open-crusoe-kubernetes-node-pools-api
- collection_type: open
  name: Crusoe Kubernetes Support Access API
  slug: open-crusoe-kubernetes-support-access-api
- collection_type: open
  name: Crusoe Kubernetes Versions API
  slug: open-crusoe-kubernetes-versions-api
- collection_type: open
  name: Crusoe Limited Usage API Key API
  slug: open-crusoe-limitedusageapikey-api
- collection_type: open
  name: Crusoe Load Balancer Operations API
  slug: open-crusoe-load-balancer-operations-api
- collection_type: open
  name: Crusoe Load Balancers API
  slug: open-crusoe-load-balancers-api
- collection_type: open
  name: Crusoe Locations API
  slug: open-crusoe-locations-api
- collection_type: open
  name: Crusoe MFA API
  slug: open-crusoe-mfa-api
- collection_type: open
  name: Crusoe NVLink Domains API
  slug: open-crusoe-nvlink-domains-api
- collection_type: open
  name: Crusoe Observability API
  slug: open-crusoe-observability-api
- collection_type: open
  name: Crusoe Projects API
  slug: open-crusoe-projects-api
- collection_type: open
  name: Crusoe Quotas API
  slug: open-crusoe-quotas-api
- collection_type: open
  name: Crusoe Reservations API
  slug: open-crusoe-reservations-api
- collection_type: open
  name: Crusoe Role Bindings API
  slug: open-crusoe-rolebindings-api
- collection_type: open
  name: Crusoe Roles API
  slug: open-crusoe-roles-api
- collection_type: open
  name: Crusoe S3 Buckets API
  slug: open-crusoe-s3buckets-api
- collection_type: open
  name: Crusoe S3 Keys API
  slug: open-crusoe-s3keys-api
- collection_type: open
  name: Crusoe SCIM API
  slug: open-crusoe-scim-api
- collection_type: open
  name: Crusoe Slurm Cluster Operations API
  slug: open-crusoe-slurm-cluster-operations-api
- collection_type: open
  name: Crusoe Slurm Clusters API
  slug: open-crusoe-slurm-clusters-api
- collection_type: open
  name: Crusoe Slurm Nodeset Operations API
  slug: open-crusoe-slurm-nodeset-operations-api
- collection_type: open
  name: Crusoe Slurm Nodesets API
  slug: open-crusoe-slurm-nodesets-api
- collection_type: open
  name: Crusoe Snapshot Operations API
  slug: open-crusoe-snapshot-operations-api
- collection_type: open
  name: Crusoe Snapshots API
  slug: open-crusoe-snapshots-api
- collection_type: open
  name: Crusoe SSH Keys API
  slug: open-crusoe-ssh-keys-api
- collection_type: open
  name: Crusoe SSO API
  slug: open-crusoe-sso-api
- collection_type: open
  name: Crusoe Tokens API
  slug: open-crusoe-tokens-api
- collection_type: open
  name: Crusoe Usage API
  slug: open-crusoe-usage-api
- collection_type: open
  name: Crusoe VM Operations API
  slug: open-crusoe-vm-operations-api
- collection_type: open
  name: Crusoe V Ms API
  slug: open-crusoe-vms-api
- collection_type: open
  name: Crusoe VPC Firewall Rule Operations API
  slug: open-crusoe-vpc-firewall-rule-operations-api
- collection_type: open
  name: Crusoe VPC Firewall Rules API
  slug: open-crusoe-vpc-firewall-rules-api
- collection_type: open
  name: Crusoe VPC Network Operations API
  slug: open-crusoe-vpc-network-operations-api
- collection_type: open
  name: Crusoe VPC Networks API
  slug: open-crusoe-vpc-networks-api
- collection_type: open
  name: Crusoe VPC Subnet Operations API
  slug: open-crusoe-vpc-subnet-operations-api
- collection_type: open
  name: Crusoe VPC Subnets API
  slug: open-crusoe-vpc-subnets-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.crusoe.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.crusoe.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crusoecloud.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.crusoecloud.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.crusoecloud.com/quickstart/overview
- group: operate
  title: ''
  type: Support
  url: https://docs.crusoecloud.com/resources/support
- group: company
  title: ''
  type: Blog
  url: https://www.crusoe.ai/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crusoecloud
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crusoe.ai/cloud/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.crusoecloud.com/signup
- group: start
  title: ''
  type: Login
  url: https://console.crusoecloud.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.crusoe.ai/#terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.crusoe.ai/#cloud-privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crusoecloud.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/crusoe-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.crusoecloud.com/resources/deprecation_notices
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crusoe-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://www.crusoe.ai/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crusoe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/crusoe-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.crusoe.ai/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crusoe-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/crusoe-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/crusoe-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crusoe-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crusoe-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crusoe-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crusoe-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/crusoe-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/crusoe-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/crusoe-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/crusoe-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crusoe-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/crusoe-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crusoe-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crusoe-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/crusoe-cloud-api-gateway-v1-overlay.yaml
- group: operate
  title: ''
  type: SLA
  url: https://legal.crusoe.ai/#service-level-agreements
created: '2026-08-04'
description: Crusoe is a vertically integrated "AI factory" company that designs, builds, and operates energy-first AI infrastructure, and sells it as Crusoe Cloud — a GPU cloud for training, fine-tuning, and inference. The public developer surface is the Crusoe Cloud API Gateway, a REST API at api.cloud.crusoe.ai covering virtual machines, instance groups and templates, block storage disks and snapshots, S3-compatible object storage, custom images, a container registry, VPC networking and load balancers, InfiniBand partitions and NVLink domains, Crusoe Managed Kubernetes and Slurm clusters, capacity reservations, IAM role bindings, SCIM/SSO, quotas, audit logs, usage and billing. Alongside it, the Intelligence Foundry exposes an OpenAI-compatible Managed Inference API for serverless inference, serverless fine-tuning, and self-serve deployments of open models. Crusoe also ships a first-party CLI, a Terraform provider, a Go API client, and a read-only Crusoe Cloud MCP server for AI assistants.
  Founded 2018, headquartered in Denver, Colorado.
image: https://www.crusoe.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Crusoe MCP Server
  slug: crusoe-mcp-server
modified: '2026-08-04'
name: Crusoe
nav: Providers
network: true
overview: 'Crusoe publishes 61 APIs on the [APIs.io](https://apis.io/) network, including Audit Logs API, AutoCluster Operations API, Auto Clusters API, and 58 more. Tagged areas include AI Infrastructure, Cloud Computing, GPU Compute, Machine-Learning, and Inference.


  The Crusoe catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Crusoe''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
random_paper: 6
score:
  band: strong
  composite: 60.6
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 16.7
    contract_quality: 56.7
    developer_ergonomics: 73.2
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 55.3
  previous_composite: 60.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 61
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 48.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crusoe/refs/heads/main/screenshots/crusoe-2026-08-07T163934.png
security:
- kind: authentication
  name: Crusoe Authentication
  slug: crusoe-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Crusoe Domain Security
  slug: crusoe-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Crusoe Vulnerability Disclosure
  slug: crusoe-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Crusoe Trust Center
  slug: crusoe-trust-center
  summary_line: SOC 2 Type II, SOC 2 Type I, ISO 27001, ISO 42001, GDPR
slug: crusoe
tags:
- AI Infrastructure
- Cloud Computing
- GPU Compute
- Machine-Learning
- Inference
- Kubernetes
- Object Storage
- Infrastructure-as-a-Service
- Energy
- MCP
website: https://www.crusoe.ai/
---
