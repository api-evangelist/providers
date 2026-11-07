---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Coreweave Agentic Access
  operation_count: 5
  slug: coreweave-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 2
apis:
- description: The CKS API provisions and manages CoreWeave Kubernetes Service clusters and node pools on bare-metal GPU and CPU hardware. It exposes operations for cluster lifecycle, node pool configuration, and ha
  name: CoreWeave Kubernetes Service API
  slug: cks-api
- description: The CoreWeave Inference API manages Deployments, Gateways, and Capacity Claims for serverless and dedicated AI inference. It is used to create, update, and route to managed model deployments backed by
  name: CoreWeave Inference API
  slug: inference-api
- description: The VPC API creates and manages Virtual Private Clouds on CoreWeave, including network configuration, routing, and isolation for CKS clusters and other compute resources.
  name: CoreWeave VPC API
  slug: vpc-api
- description: CoreWeave AI Object Storage (CAIOS) is an S3-compatible object storage service optimized for AI dataset and model storage. It supports standard S3 operations alongside CoreWeave-specific bucket and ac
  name: CoreWeave AI Object Storage API
  slug: object-storage-api
- description: The Sandbox Control Plane API provisions ephemeral compute sandboxes for short-lived, isolated workloads on CoreWeave infrastructure.
  name: CoreWeave Sandbox Control Plane API
  slug: sandbox-api
- baseURL: https://api.coreweave.com
  baseurl_source: spec
  description: CKS cluster lifecycle operations
  name: CoreWeave Clusters API
  slug: coreweave-clusters-api
artifact_total: 28
collections:
- collection_type: open
  name: CoreWeave Kubernetes Service (CKS) Clusters API
  slug: open-coreweave-clusters-api
- collection_type: open
  name: CoreWeave Kubernetes Service (CKS) API
  slug: open-coreweave
common:
- group: operate
  href: https://artifacts.apis.io/coreweave/rate-limits/coreweave-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coreweave-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/coreweave/finops/coreweave-finops.yml
  title: ''
  type: FinOps
  url: finops/coreweave-finops.yml
- group: commercial
  href: https://artifacts.apis.io/coreweave/plans/coreweave-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coreweave-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/coreweave/capabilities/coreweave-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/coreweave-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/coreweave/agentic-access/coreweave-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coreweave-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/coreweave/security/coreweave-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/coreweave-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/coreweave/security/coreweave-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coreweave-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/coreweave/authentication/coreweave-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coreweave-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.coreweave.com
- group: other
  title: ''
  type: Developer
  url: https://docs.coreweave.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coreweave.com
- group: start
  title: ''
  type: Portal
  url: https://cloud.coreweave.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coreweave.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.coreweave.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coreweave
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coreweave.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coreweave.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coreweave.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.coreweave.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coreweave
- group: other
  title: ''
  type: Terraform
  url: https://docs.coreweave.com/platform/terraform
- group: build
  title: ''
  type: SDKs
  url: https://github.com/coreweave/tensorizer
- group: build
  title: ''
  type: Examples
  url: https://github.com/coreweave/kubernetes-cloud
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.coreweave.com/llms.txt
created: '2026-05-23'
description: CoreWeave is a specialized GPU cloud purpose-built for AI workloads, offering managed Kubernetes (CKS), Slurm-on-Kubernetes (SUNK), dedicated and serverless inference, AI Object Storage, distributed VAST file storage, HPC InfiniBand interconnect, and a Sandbox product. CoreWeave's control plane is Kubernetes-native and exposes APIs for CKS clusters, Inference deployments and gateways, VPCs, Object Storage, and Sandbox control.
features:
- description: Managed Kubernetes on bare-metal GPU and CPU nodes for training, inference, and HPC.
  name: CoreWeave Kubernetes Service (CKS)
- description: Slurm running on Kubernetes for batch and burst training workloads alongside K8s services.
  name: SUNK
- description: Dedicated and serverless inference offerings with managed deployments, gateways, and capacity claims.
  name: CoreWeave Inference
- description: S3-compatible object storage purpose-built for AI dataset and model workloads.
  name: AI Object Storage
- description: High-performance VAST Data file storage for large-scale training pipelines.
  name: Dedicated VAST Storage
- description: InfiniBand-based HPC fabric with GPUDirect RDMA for multi-node training.
  name: HPC Interconnect
- description: Ephemeral compute sandboxes for short-lived, isolated workloads.
  name: CoreWeave Sandbox
finops:
- has_sources: true
  method: derived
  name: Coreweave Finops
  primary_unit: hour
  service_category: ''
  slug: coreweave-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coreweave.png
integrations:
- description: Native Kubernetes API surface across CKS clusters with standard kubectl and Helm workflows.
  name: Kubernetes
- description: Slurm workload manager integrated with Kubernetes through SUNK.
  name: Slurm
- description: Official CoreWeave Terraform provider for CKS clusters, VPCs, and object storage buckets.
  name: Terraform
- description: NVIDIA GPU Operator and InfiniBand fabric integration for accelerated workloads.
  name: NVIDIA GPU Operator
layout: provider
modified: '2026-05-23'
name: CoreWeave
nav: Providers
network: true
overview: 'CoreWeave publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Clusters API, and 5 more. Tagged areas include Artificial Intelligence, Cloud, GPU, HPC, and Inference.


  The CoreWeave catalog on APIs.io includes 1 Spectral governance ruleset.


  CoreWeave''s developer surface includes authentication, documentation, developer portal, pricing, engineering blog, support, code examples, and 17 more developer resources.'
plans:
- name: Coreweave Plans Pricing
  plan_count: 25
  slug: coreweave-plans-pricing
- name: Coreweave Price Estimates
  plan_count: 0
  slug: coreweave-price-estimates
random_paper: 1
rate_limits:
- limit_count: 2
  name: Coreweave Rate Limits
  slug: coreweave-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: CoreWeave API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: coreweave-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 57.9
    contract_governance: 13.6
    contract_quality: 41.8
    developer_ergonomics: 47.6
    discoverability: 64.3
    operational_transparency: 23.7
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 57.1
      total: 7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/coreweave/coreweave-2026-06-20T175029.png
security:
- kind: authentication
  name: Coreweave Authentication
  slug: coreweave-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Coreweave Domain Security
  slug: coreweave-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Coreweave Trust Center
  slug: coreweave-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: coreweave
tags:
- Artificial Intelligence
- Cloud
- GPU
- HPC
- Inference
- Kubernetes
- Machine Learning
- Storage
- Data Center
website: https://www.coreweave.com
---
