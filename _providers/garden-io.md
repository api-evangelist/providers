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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 9
apis:
- description: Open-source command-line tool and engine that turns a Garden project configuration into a graph of Build, Deploy, Test, and Run actions and executes them locally or against remote Kubernetes clusters.
  name: Garden Core CLI
  slug: cli
- description: Provider that connects Garden to remote Kubernetes clusters for builds (in-cluster), deploys (manifests, kustomize, helm), tests, and runs. The primary integration surface for production-like environm
  name: Garden Kubernetes Provider
  slug: kubernetes-provider
- description: Provider optimized for local Kubernetes distributions (minikube, kind, k3s, Docker Desktop) so developers can run the same Garden project against a workstation cluster.
  name: Garden Local Kubernetes Provider
  slug: local-kubernetes-provider
- description: Provider for building, tagging, and publishing OCI container images used by other Garden actions.
  name: Garden Container Provider
  slug: container-provider
- description: Provider that runs arbitrary local commands as part of the Garden action graph, used for scripts, tooling, and shelling out to systems Garden does not natively model.
  name: Garden Exec Provider
  slug: exec-provider
- description: Provider that builds Java container images using Jib without a Docker daemon, integrated into the Garden action graph.
  name: Garden Jib Provider
  slug: jib-provider
- description: Provider that lets Garden invoke Terraform stacks as part of an environment, wiring outputs into downstream Garden actions.
  name: Garden Terraform Provider
  slug: terraform-provider
- description: Provider that lets Garden invoke Pulumi programs as part of an environment, wiring outputs into downstream Garden actions.
  name: Garden Pulumi Provider
  slug: pulumi-provider
- description: Hosted Garden control plane providing remote container builds, ephemeral preview environments, team-wide caching, secrets management, RBAC, SSO, audit logging, and dashboards on top of Garden Core. Pr
  name: Garden Cloud / Enterprise
  slug: cloud
artifact_total: 13
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/garden-io/garden/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/garden-io/garden/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/garden-io/garden/blob/main/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/garden-io/garden/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/garden-io/garden/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/garden-io-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/garden-io
- group: company
  title: ''
  type: Website
  url: https://garden.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.garden.io/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/garden-io
- group: commercial
  title: ''
  type: Plans
  url: plans/garden-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/garden-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/garden-io-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.garden.io/llms.txt
created: '2026-05-23'
description: Garden is an open-source Kubernetes-native development and CI/CD platform. Garden Core, a declarative CLI and engine, models a project as a graph of Build, Deploy, Test, and Run actions powered by pluggable providers (kubernetes, local-kubernetes, container, exec, jib, helm, terraform, pulumi). Garden Cloud / Garden Enterprise add a hosted control plane for remote container builds, ephemeral preview environments, team dashboards, team-wide caching, secrets, RBAC, audit, and SSO. The CLI integrates with any CI system and IDE; teams use Garden to standardize how dev, preview, staging, and prod environments are built and deployed.
finops:
- name: Garden Io Finops
  service_category: API
  slug: garden-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/garden-io.png
layout: provider
modified: '2026-05-23'
name: Garden
nav: Providers
network: true
overview: 'Garden publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Kubernetes, Developer Tools, CI/CD, Platform Engineering, and DevOps.


  Garden''s developer surface includes documentation, GitHub presence, and 12 more developer resources.'
plans:
- name: Garden Io Plans Pricing
  plan_count: 1
  slug: garden-io-plans-pricing
random_paper: 141
rate_limits:
- limit_count: 2
  name: Garden Io Rate Limits
  slug: garden-io-rate-limits
score:
  band: emerging
  composite: 22.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 22.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/garden-io/refs/heads/main/screenshots/garden-io-2026-06-20T181648.png
security:
- kind: domain-security
  name: Garden Io Domain Security
  slug: garden-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: garden-io
tags:
- Kubernetes
- Developer Tools
- CI/CD
- Platform Engineering
- DevOps
- Preview Environments
website: https://garden.io/
---
