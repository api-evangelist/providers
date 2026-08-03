---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 21
  human_in_the_loop: 1
  name: Lambda Labs Agentic Access
  operation_count: 37
  slug: lambda-labs-agentic-access
  summary_line: 37 operations · 21 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: The Lambda Cloud API is the REST control plane for launching, listing, starting, stopping, and terminating GPU instances, managing SSH keys, firewalls, filesystems, images, and instance types. It supp
  name: Lambda Cloud API
  slug: cloud-api
- description: Lambda 1-Click Clusters provision interconnected clusters of 16 to 2,000+ NVIDIA H100 SXM or B200 GPUs for short-duration distributed training workloads. The product is exposed through the Lambda Clou
  name: Lambda 1-Click Clusters
  slug: 1-click-clusters
- description: Lambda Cloud Filesystems provide persistent, sharable storage attached to on-demand instances for datasets and checkpoints. Filesystems are managed through the Cloud API and console.
  name: Lambda Cloud Filesystems
  slug: filesystems
- description: Lambda Inference API is an OpenAI-compatible REST gateway at https://api.lambda.ai/v1 that serves hosted open-source language models (Llama, DeepSeek, Hermes, Qwen, and others) behind the standard Ope
  name: Lambda Inference API
  slug: inference-api
- description: The Audit Events API from Lambda — 1 operation(s) for audit events.
  name: Lambda Audit Events API
  slug: lambda-labs-audit-events-api
- description: The Fabric API from Lambda — 2 operation(s) for fabric.
  name: Lambda Fabric API
  slug: lambda-labs-fabric-api
- description: The Filesystems API from Lambda — 3 operation(s) for filesystems.
  name: Lambda Filesystems API
  slug: lambda-labs-filesystems-api
- description: The Firewalls API from Lambda — 4 operation(s) for firewalls.
  name: Lambda Firewalls API
  slug: lambda-labs-firewalls-api
- description: The Images API from Lambda — 1 operation(s) for images.
  name: Lambda Images API
  slug: lambda-labs-images-api
- description: The Instances API from Lambda — 6 operation(s) for instances.
  name: Lambda Instances API
  slug: lambda-labs-instances-api
- description: The Regions API from Lambda — 1 operation(s) for regions.
  name: Lambda Regions API
  slug: lambda-labs-regions-api
- description: The SSH keys API from Lambda — 2 operation(s) for ssh keys.
  name: Lambda SSH keys API
  slug: lambda-labs-ssh-keys-api
- description: The Lambda Support Ticketing API is currently in beta. Contact support to enable access.
  name: Lambda Support Tickets API
  slug: lambda-labs-support-tickets-api
artifact_total: 32
asyncapis:
- description: AsyncAPI 2.6 description of the Lambda (formerly Lambda Labs) **Inference API** chat completion streaming surface. The Lambda Inference API is an OpenAI-compatible REST gateway hosted at `https://api.
  name: Lambda Inference API Chat Completions Streaming (HTTP + SSE)
  slug: lambda-labs-asyncapi
collections:
- collection_type: open
  name: Lambda Cloud API
  slug: open-lambda-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lambda-labs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lambda-labs-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lambda-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lambda-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lambda-labs-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://lambda.ai
- group: other
  title: ''
  type: Developer
  url: https://docs.lambda.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lambda.ai
- group: start
  title: ''
  type: Portal
  url: https://cloud.lambda.ai
- group: start
  title: ''
  type: Signup
  url: https://cloud.lambda.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://cloud.lambda.ai/login
- group: commercial
  title: ''
  type: Pricing
  url: https://lambda.ai/service/gpu-cloud
- group: company
  title: ''
  type: Blog
  url: https://lambda.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lambda.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lambda.ai/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://lambda.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LambdaLabsML
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lambda-labs
- group: build
  title: ''
  type: SDKs
  url: https://lambda.ai/lambda-stack-deep-learning-software
- group: other
  title: ''
  type: GPUs
  url: ''
created: '2026-05-23'
description: Lambda (formerly Lambda Labs) is a GPU cloud provider offering on-demand NVIDIA GPU instances, 1-Click Clusters of 16-2,000+ interconnected H100 and B200 GPUs, long-term reserved Hyperplane capacity, filesystems, firewalls, and SSH key management. Lambda Cloud is accessed via a REST control-plane API, the web console, and SDKs/CLI tooling.
features:
- description: Self-serve, first-come access to 1x, 2x, 4x, and 8x NVIDIA GPU virtual machines billed per-hour with no egress fees.
  name: On-Demand GPU Instances
- description: Pre-configured clusters of 16-2,000+ interconnected H100 SXM or B200 GPUs for distributed training.
  name: 1-Click Clusters
- description: Long-term reserved GPU clusters sold via direct sales engagement for sustained training workloads.
  name: Hyperplane Reserved Capacity
- description: Pre-installed CUDA, cuDNN, PyTorch, and TensorFlow software stack across all Lambda Cloud instances.
  name: Lambda Stack
- description: Persistent, sharable storage attached to on-demand instances for datasets and checkpoints.
  name: Filesystems
finops:
- name: Lambda Labs Finops
  service_category: API
  slug: lambda-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lambda-labs.png
integrations:
- description: Reference workflows and templates for serving and training Hugging Face models on Lambda Cloud.
  name: Hugging Face
- description: PyTorch ships pre-installed via Lambda Stack on all instances.
  name: PyTorch
- description: TensorFlow ships pre-installed via Lambda Stack on all instances.
  name: TensorFlow
layout: provider
modified: '2026-05-29'
name: Lambda
nav: Providers
network: true
overview: 'Lambda publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Inference API, Audit Events API, Fabric API, and 7 more. Tagged areas include AI, Cloud, Clusters, Compute, and GPU.


  The Lambda catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Lambda''s developer surface includes authentication, documentation, developer portal, signup flow, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Lambda Labs Plans Pricing
  plan_count: 1
  slug: lambda-labs-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 2
  name: Lambda Labs Rate Limits
  slug: lambda-labs-rate-limits
rules:
- name: Lambda API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: lambda-labs-asyncapi-spectral-rules
score:
  band: strong
  composite: 56.6
  delta: 0.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 68.6
    developer_ergonomics: 41.3
    discoverability: 64.8
    governance: 41.7
    operational_transparency: 26.3
  previous_composite: 56.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lambda-labs/refs/heads/main/screenshots/lambda-labs-2026-06-20T184251.png
security:
- kind: authentication
  name: Lambda Labs Authentication
  slug: lambda-labs-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Lambda Labs Domain Security
  slug: lambda-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lambda Labs Vulnerability Disclosure
  slug: lambda-labs-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Lambda Labs Trust Center
  slug: lambda-labs-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017
slug: lambda-labs
tags:
- AI
- Cloud
- Clusters
- Compute
- GPU
- Inference
- Machine Learning
website: https://lambda.ai
---
