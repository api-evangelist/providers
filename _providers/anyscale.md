---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.1
  scored_at: '2026-09-03'
api_count: 10
apis:
- description: Manages Anyscale Workspaces - cloud-hosted, GPU-backed development environments preconfigured with Ray for interactive development and debugging.
  name: Anyscale Workspaces API
  slug: anyscale-workspaces-api
- description: Submits, monitors, and manages Ray Jobs - one-off or scheduled batch runs of Python applications on managed Ray clusters.
  name: Anyscale Jobs API
  slug: anyscale-jobs-api
- description: Deploys and manages production Ray Serve applications as long-running, autoscaling, multi-version services with traffic-shifted rollouts and HTTP/gRPC ingress.
  name: Anyscale Services API
  slug: anyscale-services-api
- description: Provisions and manages Ray clusters - autoscaling fleets of CPU / GPU nodes underlying Workspaces, Jobs, and Services.
  name: Anyscale Clusters API
  slug: anyscale-clusters-api
- description: Defines reusable compute templates (head node type, worker types, autoscaling, AWS/GCP region) for clusters, workspaces, jobs, and services.
  name: Anyscale Compute Configs API
  slug: anyscale-compute-configs-api
- description: Builds, tags, and manages container images that bundle Python, system, and Ray dependencies for reproducible runtime environments.
  name: Anyscale Container Images API
  slug: anyscale-container-images-api
- description: Manages Hosted and Bring-Your-Own-Cloud (BYOC) cloud connections to AWS and GCP accounts where Anyscale provisions Ray clusters.
  name: Anyscale Clouds API
  slug: anyscale-clouds-api
- description: Groups workspaces, jobs, services, and resources into projects with shared access controls, dashboards, and quotas.
  name: Anyscale Projects API
  slug: anyscale-projects-api
- description: Manages organizations, users, roles, IAM, and billing relationships at the tenancy level.
  name: Anyscale Organizations API
  slug: anyscale-organizations-api
- description: Retrieves cluster, job, and service logs, metrics, and Ray dashboard data for observability and debugging.
  name: Anyscale Logs and Monitoring API
  slug: anyscale-logs-api
artifact_total: 16
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/anyscale-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anyscale-domain-security.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://docs.anyscale.com/agent-skills
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anyscale
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/joinanyscale
- group: company
  title: ''
  type: Website
  url: https://www.anyscale.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anyscale.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/anyscale-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/anyscale-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/anyscale-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.anyscale.com/llms.txt
created: '2026-05-08'
description: Anyscale provides a managed Ray platform for distributed Python, ML training, and large-scale inference. Built by the creators of Ray, the Anyscale Platform API and CLI expose programmatic control over workspaces, jobs, services, clusters, compute configurations, container images, and clouds (Hosted and Bring-Your-Own-Cloud).
finops:
- name: Anyscale Finops
  service_category: AI and Machine Learning
  slug: anyscale-finops
graphqls:
- description: Anyscale is a managed Ray platform for distributed AI compute. Their Endpoints API provides OpenAI-compatible access to open-source LLMs (Llama, Mistral), fine-tuning, and deployment.
  name: Anyscale GraphQL API
  slug: anyscale-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anyscale.png
layout: provider
modified: '2026-05-08'
name: Anyscale
nav: Providers
network: true
overview: 'Anyscale publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Distributed Computing, Ray, ML Platform, and Inference.


  Anyscale''s developer surface includes documentation and 10 more developer resources.'
plans:
- name: Anyscale Plans Pricing
  plan_count: 3
  slug: anyscale-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Anyscale Rate Limits
  slug: anyscale-rate-limits
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 16.7
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 26.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anyscale/refs/heads/main/screenshots/anyscale-2026-06-20T172029.png
security:
- kind: domain-security
  name: Anyscale Domain Security
  slug: anyscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Anyscale Trust Center
  slug: anyscale-trust-center
  summary_line: trust center published
slug: anyscale
tags:
- Artificial Intelligence
- Distributed Computing
- Ray
- ML Platform
- Inference
- GPU
website: https://www.anyscale.com/
---
