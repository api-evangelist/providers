---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Fluidstack Agentic Access
  operation_count: 14
  slug: fluidstack-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 7
apis:
- description: The Clusters API from Fluidstack — 1 operation(s) for clusters.
  name: Fluidstack Clusters API
  slug: fluidstack-clusters-api
- description: The Instances API from Fluidstack — 2 operation(s) for instances.
  name: Fluidstack Instances API
  slug: fluidstack-instances-api
- description: The Invitations API from Fluidstack — 2 operation(s) for invitations.
  name: Fluidstack Invitations API
  slug: fluidstack-invitations-api
- description: The Members API from Fluidstack — 2 operation(s) for members.
  name: Fluidstack Members API
  slug: fluidstack-members-api
- description: The Organizations API from Fluidstack — 1 operation(s) for organizations.
  name: Fluidstack Organizations API
  slug: fluidstack-organizations-api
- description: The Regions API from Fluidstack — 1 operation(s) for regions.
  name: Fluidstack Regions API
  slug: fluidstack-regions-api
- description: The User API from Fluidstack — 2 operation(s) for user.
  name: Fluidstack User API
  slug: fluidstack-user-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Management Clusters API
  slug: open-fluidstack-clusters-api
- collection_type: open
  name: Management Clusters Instances API
  slug: open-fluidstack-instances-api
- collection_type: open
  name: Management Clusters Invitations API
  slug: open-fluidstack-invitations-api
- collection_type: open
  name: Management API
  slug: open-fluidstack-management-api
- collection_type: open
  name: Management Clusters Members API
  slug: open-fluidstack-members-api
- collection_type: open
  name: Management Clusters Organizations API
  slug: open-fluidstack-organizations-api
- collection_type: open
  name: Management Clusters Regions API
  slug: open-fluidstack-regions-api
- collection_type: open
  name: Management Clusters User API
  slug: open-fluidstack-user-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fluidstack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fluidstack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fluidstack-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.fluidstack.io
- group: start
  title: ''
  type: Portal
  url: https://docs.fluidstack.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fluidstack.io/getting-started/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fluidstack.io/getting-started/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fluidstack.io/projects/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fluidstack.io/kubernetes/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fluidstack.io/slurm/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fluidstack.io/lighthouse/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fluidstack.io/api-reference/management-api
- group: build
  title: ''
  type: SDKs
  url: https://docs.fluidstack.io/cli-reference/fluidctl
- group: company
  title: ''
  type: About
  url: https://www.fluidstack.io/about-us/about
- group: company
  title: ''
  type: Blog
  url: https://www.fluidstack.io/about-us/blog
- group: company
  title: ''
  type: Careers
  url: https://www.fluidstack.io/about-us/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.fluidstack.io/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fluidstack
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/fluidstackio
created: '2026-05-25'
description: Fluidstack is an AI cloud platform that builds and operates high-performance, single-tenant GPU clusters for top AI labs, governments, and enterprises. Founded in 2017 out of Oxford University and now headquartered in New York City, Fluidstack manages more than 100,000 GPUs across its global network and has been selected by customers including Anthropic, Meta, Mistral, Poolside, Black Forest Labs, and Character.AI. Its core offering combines on-demand bare-metal GPU clusters (including thousands of NVIDIA H200s with InfiniBand) with managed Kubernetes and managed Slurm orchestration layers, Lighthouse observability, and human-on-call site reliability. Fluidstack exposes a global REST Management API (api.atlas.fluidstack.io/api/v1alpha1) and the fluidctl CLI for managing organizations, projects, regions, clusters, instances, members, invitations, and SSH keys. The platform is GDPR, SOC 2 Type 2, and ISO 27001 certified, and was awarded ClusterMAX Gold by SemiAnalysis.
features:
- On-demand single-tenant GPU clusters with isolated hardware, network, and storage
- Immediate access to thousands of NVIDIA H200 GPUs with InfiniBand interconnect
- Managed Kubernetes — bare-metal container orchestration with NVIDIA operators and health checks
- Managed Slurm — bare-metal batch orchestration with user management and topology-aware scheduling
- Lighthouse observability and monitoring for GPU clusters
- Global Management API (v1alpha1) at api.atlas.fluidstack.io for clusters, instances, regions, members, invitations, and SSH keys
- fluidctl command-line tool with auth, capacity, instance-types, instances, kubernetes, projects, slurm commands
- Bearer token authentication with optional X-PROJECT-ID header scoping
- Custom data centers — selected by Anthropic to deliver capacity in New York and Texas
- Demonstrated rapid deployment — 2,500+ GPUs delivered to Poolside in 48 hours
- 100,000+ GPUs under management across the network
- 15-minute response SLA with direct engineer maintenance and audit logs
- GDPR, SOC 2 Type 2, and ISO 27001 certified
- ClusterMAX Gold awarded by SemiAnalysis (Nov 2025)
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fluidstack.png
layout: provider
modified: '2026-05-25'
name: Fluidstack
nav: Providers
network: true
overview: 'Fluidstack publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Clusters API, Instances API, Invitations API, and 4 more. Tagged areas include AI, Artificial Intelligence, GPU, Cloud, and Compute.


  Fluidstack''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 14 more developer resources.'
random_paper: 23
score:
  band: thin
  composite: 30.9
  delta: -0.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 53.9
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fluidstack/refs/heads/main/screenshots/fluidstack-2026-06-20T181337.png
security:
- kind: authentication
  name: Fluidstack Authentication
  slug: fluidstack-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fluidstack Domain Security
  slug: fluidstack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fluidstack
tags:
- AI
- Artificial Intelligence
- GPU
- Cloud
- Compute
- Infrastructure
- Machine Learning
- Foundation Models
- Training
- Inference
- Kubernetes
- Slurm
- Bare Metal
- NVIDIA
- InfiniBand
- Data Centers
website: https://www.fluidstack.io
---
