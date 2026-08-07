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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Tensordock Agentic Access
  operation_count: 11
  slug: tensordock-agentic-access
  summary_line: 11 operations · 7 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: 'The original TensorDock Marketplace REST API (v0) for deploying, managing, starting, stopping, and deleting GPU virtual machines across the global marketplace of independent hardware hosts. Endpoints '
  name: TensorDock Marketplace API
  slug: tensordock-marketplace-api
- description: The current TensorDock Instances API (v2) at https://dashboard.tensordock.com/api/v2/instances for creating, listing, inspecting, starting, stopping, modifying, and deleting GPU and CPU virtual machin
  name: TensorDock Instances API
  slug: tensordock-instances-api
- description: The TensorDock Secrets API (v2) for managing SSH keys and generic secrets that are encrypted at rest and in transit and can be attached to instances at deploy time. Two secret types are supported — `S
  name: TensorDock Secrets API
  slug: tensordock-secrets-api
artifact_total: 42
collections:
- collection_type: postman
  name: TensorDock Instances API
  slug: postman-tensordock-instances-api
- collection_type: postman
  name: TensorDock Instances Secrets API
  slug: postman-tensordock-secrets-api
- collection_type: open
  name: TensorDock Instances API
  slug: open-tensordock-instances-api
- collection_type: open
  name: TensorDock Secrets API
  slug: open-tensordock-secrets-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tensordock/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tensordock-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tensordock-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tensordock-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.tensordock.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensordock.com
- group: docs
  title: ''
  type: Documentation
  url: https://dashboard.tensordock.com/api/docs
- group: docs
  title: ''
  type: Documentation
  url: https://documenter.getpostman.com/view/20973002/2s8YzMYRDc
- group: start
  title: ''
  type: GettingStarted
  url: https://dashboard.tensordock.com/api/docs/getting-started
- group: start
  title: ''
  type: Console
  url: https://dashboard.tensordock.com
- group: start
  title: ''
  type: Sandbox
  url: https://dashboard.tensordock.com/deploy
- group: start
  title: ''
  type: Sandbox
  url: https://dashboard.tensordock.com/deploy_cpu
- group: start
  title: ''
  type: Signup
  url: https://dashboard.tensordock.com/api
- group: company
  title: ''
  type: Blog
  url: https://blog.tensordock.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://tensordock.com/security
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensordock.com/legal-information/legal-information
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.tensordock.com/legal-information/terms-of-service-tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.tensordock.com/legal-information/tensordock-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.tensordock.com/legal-information/acceptable-use-policy-aup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensordock.com/legal-information/downtime-compensation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensordock.com/legal-information/taxes-vat-gst
- group: operate
  title: ''
  type: Support
  url: https://marketplace.tensordock.com/support
- group: operate
  title: ''
  type: Support
  url: https://marketplace.tensordock.com/faq
- group: operate
  title: ''
  type: Forums
  url: https://tensordock.userjot.com/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/TensorDock
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tensordock
- group: company
  title: ''
  type: Instagram
  url: https://instagram.com/tensordock
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCsCAK6krPmRe3Y7Hp5QHXQg
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/Xyzjjuj6zf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tensordock
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tensordock/tensordock-rs
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/tensordock/
- group: build
  title: ''
  type: Tools
  url: https://github.com/tensordock/dashboard-frontend-template
- group: build
  title: ''
  type: Tools
  url: https://github.com/tensordock/wireguard-manager
- group: build
  title: ''
  type: Tools
  url: https://github.com/tensordock/tensorblog
- group: build
  title: ''
  type: Tools
  url: https://github.com/tensordock/hosting-install
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensordock.com/virtual-machines/introduction-to-core-compute-vms
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensordock.com/virtual-machines/spot-instances
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensordock.com/virtual-machines/cloud-init
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensordock.com/virtual-machines/how-to-ssh-into-your-instance
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensordock.com/virtual-machines/how-to-rdp-into-your-instance
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensordock.com/whitelabel/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensordock.com/whitelabel/setting-up-a-storefront
- group: start
  title: ''
  type: Signup
  url: https://www.tensordock.com/host.html
- group: commercial
  title: ''
  type: Plans
  url: plans/tensordock-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tensordock-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tensordock-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://marketplace.tensordock.com
created: '2026-05-25'
description: TensorDock operates a global GPU cloud marketplace that connects independent hardware hosts with customers needing affordable on-demand and spot GPU compute. The platform exposes two REST APIs — the original Marketplace API (v0) at marketplace.tensordock.com and the newer Instances API (v2) at dashboard.tensordock.com — to deploy, manage, and scale virtual machines across 100+ locations in 20+ countries with 42+ GPU models ranging from consumer RTX cards to H100 SXM5. TensorDock targets AI startups, researchers, rendering shops, and gaming services that need cost-effective compute (advertised at up to 80% less than hyperscalers) without quotas or long-term commitments.
examples:
- key_count: 2
  name: Tensordock Create Instance Example
  slug: tensordock-create-instance-example
- key_count: 2
  name: Tensordock Create Secret Example
  slug: tensordock-create-secret-example
- key_count: 2
  name: Tensordock List Hostnodes Example
  slug: tensordock-list-hostnodes-example
- key_count: 2
  name: Tensordock List Instances Example
  slug: tensordock-list-instances-example
- key_count: 2
  name: Tensordock Spot Validate New Example
  slug: tensordock-spot-validate-new-example
features:
- GPU marketplace aggregating 30,000+ GPUs across 100+ locations in 20+ countries
- 42+ NVIDIA GPU models from consumer (RTX 3090/4090/5090) to data center (H100 SXM5, A100, V100, L40S, L4, RTX 6000 Ada, A6000)
- Per-microsecond billing with pay-as-you-go and reserved pricing on request
- On-demand virtual machines with KVM virtualization, root access, and dedicated GPU passthrough
- Spot/interruptible instances with custom bid pricing and soft-validate APIs
- Instant VMs (beta) with sub-30-second deployment from pre-configured templates
- Container deployment, scaling, and termination endpoints
- CPU-only Compute VMs from $0.012/vCPU/hour for transcoding and batch jobs
- Windows 10 and Linux (Ubuntu, Debian, CentOS) images plus custom cloud-init support
- Whitelabel storefront product for resellers and managed cloud providers
- Two REST APIs — Marketplace v0 (api_key + api_token, form parameters) and Instances v2 (Bearer token, JSON:API envelope)
- Secrets API (v2) with SSHKEY and GENERIC/SECRET types, encrypted at rest and in transit
- Hostnode discovery API listing all available GPU/CPU configurations per location
- 99.99% uptime SLA per host with agent-based monitoring and downtime compensation policy
- SSH access revoked from hosts and active monitoring for tenant isolation
- Postman collection covering Authorization, Hostnodes, Virtual Machines, Spot validation, Containers, and Billing endpoint groups
- Rust client wrapper (tensordock-rs) and community Python SDK
- 100 requests per minute per organization on the v2 API
- Customer balance, revenue, and monthly summary endpoints for host operators
finops:
- name: Tensordock Finops
  service_category: Compute
  slug: tensordock-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tensordock.png
json_schemas:
- name: TensorDock Hostnode
  property_count: 5
  slug: tensordock-hostnode
- name: TensorDock Instance
  property_count: 1
  slug: tensordock-instance
jsonld:
- class_count: 0
  name: Tensordock Context
  property_count: 9
  slug: tensordock-context
layout: provider
modified: '2026-05-25'
name: TensorDock
nav: Providers
network: true
overview: 'TensorDock publishes 3 APIs on the [APIs.io](https://apis.io/) network: Marketplace API, Instances API, and Secrets API. Tagged areas include GPU, Cloud, Marketplace, Compute, and Virtual Machines.


  The TensorDock catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TensorDock''s developer surface includes authentication, developer portal, documentation, getting-started guide, developer console, sandbox, signup flow, and 41 more developer resources.'
plans:
- name: Tensordock Plans Pricing
  plan_count: 6
  slug: tensordock-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 2
  name: Tensordock Rate Limits
  slug: tensordock-rate-limits
rules:
- name: TensorDock API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tensordock-jsonschema-spectral-rules
- name: TensorDock API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 5
  slug: tensordock-rules
score:
  band: strong
  composite: 62.7
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 69.8
    developer_ergonomics: 63.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 62.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tensordock/refs/heads/main/screenshots/tensordock-2026-06-20T195118.png
security:
- kind: authentication
  name: Tensordock Authentication
  slug: tensordock-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tensordock Domain Security
  slug: tensordock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tensordock
tags:
- GPU
- Cloud
- Marketplace
- Compute
- Virtual Machines
- AI
- Machine Learning
- Bare Metal
- Spot Instances
- Containers
website: https://www.tensordock.com
---
