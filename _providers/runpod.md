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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 22
  human_in_the_loop: 2
  name: Runpod Agentic Access
  operation_count: 37
  slug: runpod-agentic-access
  summary_line: 37 operations · 22 acting · 2 human-in-the-loop
api_count: 10
apis:
- description: The RunPod GraphQL API provides programmatic access to Pods, templates, and Serverless endpoints via GraphQL queries and mutations. It is the original control-plane interface and is still supported al
  name: RunPod GraphQL API
  slug: graphql-api
- description: RunPod Serverless provides pay-as-you-go inference endpoints with autoscaling workers, queue-based and load-balanced endpoint types, FlashBoot cold-start optimization, and per-second billing. Each end
  name: RunPod Serverless
  slug: serverless
- description: The Billing API from RunPod — 3 operation(s) for billing.
  name: RunPod Billing API
  slug: runpod-billing-api
- description: The Containerregistryauth API from RunPod — 2 operation(s) for containerregistryauth.
  name: RunPod Containerregistryauth API
  slug: runpod-containerregistryauth-api
- description: The Docs API from RunPod — 1 operation(s) for docs.
  name: RunPod Docs API
  slug: runpod-docs-api
- description: The Endpoints API from RunPod — 3 operation(s) for endpoints.
  name: RunPod Endpoints API
  slug: runpod-endpoints-api
- description: The Networkvolumes API from RunPod — 3 operation(s) for networkvolumes.
  name: RunPod Networkvolumes API
  slug: runpod-networkvolumes-api
- description: The Openapi.json API from RunPod — 1 operation(s) for openapi.json.
  name: RunPod Openapi.json API
  slug: runpod-openapi-json-api
- description: The Pods API from RunPod — 7 operation(s) for pods.
  name: RunPod Pods API
  slug: runpod-pods-api
- description: The Templates API from RunPod — 3 operation(s) for templates.
  name: RunPod Templates API
  slug: runpod-templates-api
artifact_total: 27
collections:
- collection_type: open
  name: Runpod REST API
  slug: open-runpod
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/runpod-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/runpod-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runpod-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/runpod-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://runpod.io
- group: other
  title: ''
  type: Developer
  url: https://docs.runpod.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.runpod.io
- group: start
  title: ''
  type: Portal
  url: https://console.runpod.io
- group: start
  title: ''
  type: Signup
  url: https://www.runpod.io/console/signup
- group: start
  title: ''
  type: Login
  url: https://www.runpod.io/console/signin
- group: commercial
  title: ''
  type: Pricing
  url: https://www.runpod.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.runpod.io
- group: operate
  title: ''
  type: StatusPage
  url: https://uptime.runpod.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.runpod.io/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.runpod.io/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/runpod
- group: operate
  title: ''
  type: Support
  url: https://www.runpod.io/contact
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.runpod.io/changelog
- group: build
  title: ''
  type: SDKs
  url: https://github.com/runpod/runpod-python
- group: build
  title: ''
  type: CLI
  url: https://github.com/runpod/runpodctl
- group: other
  title: ''
  type: Terraform
  url: https://github.com/runpod/pulumi-runpod
- group: other
  title: ''
  type: GPUs
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.runpod.io/llms.txt
created: '2026-05-23'
description: RunPod is a managed GPU cloud and serverless inference platform offering on-demand and persistent GPU Pods, autoscaling Serverless endpoints, network volumes, container templates, and a REST + GraphQL control plane for provisioning H100, H200, B200, A100, L40S, and consumer RTX GPUs. RunPod targets AI/ML developers who need flexible, per-second-billed GPU compute for training, fine-tuning, and inference workloads.
features:
- description: Persistent on-demand GPU instances with SSH, JupyterLab, and VSCode access, billed per-second across a wide range of NVIDIA SKUs.
  name: GPU Pods
- description: Autoscaling, queue-based inference endpoints with FlashBoot cold-start optimization and pay-per-request billing.
  name: Serverless Endpoints
- description: Persistent, portable storage that can be attached to Pods and Serverless workers across datacenters.
  name: Network Volumes
- description: Reusable Pod and endpoint configurations bundling container images, hardware specs, and network settings.
  name: Templates
- description: Pre-built Serverless workers for deploying open-source LLMs with vLLM in a single click.
  name: vLLM Quick Deploy
finops:
- name: Runpod Finops
  service_category: API
  slug: runpod-finops
graphqls:
- description: The RunPod GraphQL API provides programmatic access to Pods, templates, and Serverless endpoints via GraphQL queries and mutations. It is the original control-plane interface and is still supported al
  name: RunPod GraphQL API
  slug: runpod-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/runpod.png
integrations:
- description: Bring-your-own container support for any Docker image on Pods and Serverless workers.
  name: Docker
- description: Direct deployment of Hugging Face models via vLLM Quick Deploy and ready-made templates.
  name: Hugging Face
- description: Infrastructure-as-code provisioning of RunPod resources via the official Pulumi provider.
  name: Pulumi
layout: provider
modified: '2026-05-23'
name: RunPod
nav: Providers
network: true
overview: 'RunPod publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Containerregistryauth API, Docs API, and 5 more. Tagged areas include AI, Cloud, Compute, GPU, and Inference.


  RunPod''s developer surface includes authentication, documentation, developer portal, signup flow, pricing, engineering blog, support, and 15 more developer resources.'
plans:
- name: Runpod Plans Pricing
  plan_count: 1
  slug: runpod-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 2
  name: Runpod Rate Limits
  slug: runpod-rate-limits
score:
  band: developing
  composite: 56.2
  delta: 3.2
  facets:
    commercial_clarity: 81.6
    contract_quality: 51.3
    developer_ergonomics: 47.8
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 53.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/runpod/refs/heads/main/screenshots/runpod-2026-06-20T193259.png
security:
- kind: authentication
  name: Runpod Authentication
  slug: runpod-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Runpod Domain Security
  slug: runpod-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Runpod Trust Center
  slug: runpod-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: runpod
tags:
- AI
- Cloud
- Compute
- GPU
- Inference
- Machine Learning
- Serverless
website: https://runpod.io
---
