---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-05'
api_count: 6
apis:
- description: 'The Nebius Compute API provisions and manages virtual machines and GPU clusters with NVIDIA GPUs and InfiniBand interconnect for ML and AI workloads. Exposed over gRPC and accessed through the nebius '
  name: Nebius Compute API
  slug: compute-api
- description: The Managed Kubernetes API provisions Kubernetes clusters with GPU and InfiniBand support for distributed training and inference workloads.
  name: Nebius Managed Kubernetes API
  slug: kubernetes-api
- description: The Nebius Storage API exposes AWS S3-compatible object storage for ML/AI datasets and model artifacts.
  name: Nebius Storage API
  slug: storage-api
- description: The Nebius Identity and Access Management API controls users, service accounts, projects, and resource-level access policies.
  name: Nebius IAM API
  slug: iam-api
- description: The Managed Applications API deploys and manages JupyterLab, vLLM, Open WebUI, MLflow, and other ready-made apps on Nebius infrastructure.
  name: Nebius Managed Applications API
  slug: mk8s-applications-api
- description: Nebius Token Factory is the AI model inference platform offering OpenAI-compatible endpoints for serving open-source LLMs on Nebius GPU infrastructure.
  name: Nebius Token Factory
  slug: token-factory
artifact_total: 23
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nebius-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nebius-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nebius.com
- group: other
  title: ''
  type: Developer
  url: https://docs.nebius.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nebius.com
- group: start
  title: ''
  type: Portal
  url: https://console.nebius.com
- group: commercial
  title: ''
  type: Pricing
  url: https://nebius.com/prices
- group: company
  title: ''
  type: Blog
  url: https://nebius.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nebius
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nebius.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nebius.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://nebius.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nebius
- group: build
  title: ''
  type: SDKs
  url: https://github.com/nebius/gosdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/nebius/js-sdk
- group: other
  title: ''
  type: Terraform
  url: https://github.com/nebius/terraform-provider-nebius
- group: build
  title: ''
  type: Examples
  url: https://github.com/nebius/nebius-solution-library
- group: build
  title: ''
  type: Examples
  url: https://github.com/nebius/soperator
- group: other
  title: ''
  type: GPUs
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.nebius.com/llms.txt
created: '2026-05-23'
description: Nebius is an AI-focused cloud platform spun out of Yandex, offering NVIDIA GPU virtual machines and clusters (GB300, GB200, B300, B200, H200, H100) connected over InfiniBand, managed Kubernetes and Slurm (Soperator), S3-compatible storage, managed PostgreSQL, container registry, MLflow, JupyterLab, vLLM, and the Token Factory inference platform. Nebius exposes a gRPC control plane API, a Terraform provider, a nebius CLI, and Go and TypeScript SDKs.
features:
- description: Virtual machines and clusters with NVIDIA GB300, GB200, B300, B200, H200, and H100 GPUs.
  name: GPU Compute
- description: High-bandwidth InfiniBand interconnect for large-scale distributed training.
  name: InfiniBand Networking
- description: Kubernetes clusters with GPU and InfiniBand support.
  name: Managed Kubernetes
- description: Slurm workload manager running on Kubernetes via the open-source Soperator project.
  name: Slurm via Soperator
- description: Object storage optimized for ML datasets and model artifacts.
  name: S3-Compatible Storage
- description: One-click JupyterLab, vLLM, Open WebUI, and MLflow deployments.
  name: Managed Applications
- description: OpenAI-compatible inference endpoints for open-source LLMs.
  name: Token Factory
finops:
- name: Nebius Finops
  service_category: API
  slug: nebius-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nebius.png
integrations:
- description: Official Terraform provider for Nebius infrastructure.
  name: Terraform
- description: Standard Kubernetes API across managed clusters.
  name: Kubernetes
- description: Slurm workload manager via the open-source Soperator project.
  name: Slurm
- description: Managed MLflow for experiment tracking.
  name: MLflow
- description: Managed PostgreSQL database clusters.
  name: PostgreSQL
layout: provider
modified: '2026-05-23'
name: Nebius
nav: Providers
network: true
overview: 'Nebius publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Cloud, Compute, GPU, and HPC.


  Nebius'' developer surface includes documentation, developer portal, pricing, engineering blog, support, code examples, and 13 more developer resources.'
plans:
- name: Nebius Plans Pricing
  plan_count: 1
  slug: nebius-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Nebius Rate Limits
  slug: nebius-rate-limits
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 54.0
    catalog_earned_first_party: 0.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 28.6
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 25.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nebius/refs/heads/main/screenshots/nebius-2026-06-20T190119.png
security:
- kind: domain-security
  name: Nebius Domain Security
  slug: nebius-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nebius Vulnerability Disclosure
  slug: nebius-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nebius
tags:
- Artificial Intelligence
- Cloud
- Compute
- GPU
- HPC
- Inference
- Kubernetes
- Machine-Learning
- Storage
website: https://nebius.com
---
