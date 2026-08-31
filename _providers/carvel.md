---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 7
apis:
- description: ytt is a templating tool that understands YAML structure, letting you use familiar YAML constructs and Python-like language (Starlark) to template Kubernetes configuration. Supports overlays, data val
  name: ytt
  slug: ytt
- description: kapp is a CLI tool that installs, upgrades, and deletes multiple Kubernetes resources as a single application. It provides change set previews, resource ordering, and convergence detection for predict
  name: kapp
  slug: kapp
- description: kbld builds or references container images in Kubernetes configuration in an immutable way by resolving image tags to digests and optionally building images from source during the deployment pipeline.
  name: kbld
  slug: kbld
- description: imgpkg bundles and distributes application configuration and container images as OCI artifacts via Docker registries, enabling relocation across registries including air-gapped environments.
  name: imgpkg
  slug: imgpkg
- description: vendir declaratively states what files should be in a directory, syncing from upstream sources such as Git repositories, HTTP archives, Helm charts, and OCI images. Enables reproducible vendored confi
  name: vendir
  slug: vendir
- description: kapp-controller is a Kubernetes controller that provides GitOps-style continuous delivery for applications and packages using Carvel tools. It introduces PackageRepository, Package, PackageInstall, an
  name: kapp-controller
  slug: kapp-controller
- description: secretgen-controller provides CRDs to generate Kubernetes Secrets, export and import secrets across namespaces, and manage certificate and password creation declaratively.
  name: secretgen-controller
  slug: secretgen-controller
artifact_total: 11
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/carvel-dev/ytt/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/carvel-dev/ytt/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/carvel-dev/ytt/blob/develop/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/carvel-dev/ytt/blob/develop/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/carvel-dev/ytt/blob/develop/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/carvel-dev/ytt/blob/develop/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carvel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carvel.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://carvel.dev/docs/latest/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carvel-dev
- group: company
  title: ''
  type: Blog
  url: https://carvel.dev/blog/
- group: operate
  title: ''
  type: Slack
  url: https://kubernetes.slack.com/archives/CH8KCCKA5
- group: operate
  title: ''
  type: Community
  url: https://carvel.dev/community/
created: '2026-03-26'
description: Carvel is a set of reliable, single-purpose, composable command-line tools that help build, configure, and deploy applications to Kubernetes. The toolset includes ytt for YAML templating, kapp for application lifecycle management, kbld for immutable image references, imgpkg for OCI bundling, vendir for vendored configuration, and kapp-controller for GitOps-style continuous delivery.
finops:
- name: Carvel Finops
  service_category: API
  slug: carvel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carvel.png
layout: provider
modified: '2026-04-23'
name: Carvel
nav: Providers
network: true
overview: 'Carvel publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CLI, Configuration, Containers, Deployment, and GitOps.


  Carvel''s developer surface includes documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Carvel Plans Pricing
  plan_count: 3
  slug: carvel-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Carvel Rate Limits
  slug: carvel-rate-limits
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 8.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 18.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/carvel/refs/heads/main/screenshots/carvel-2026-06-20T174027.png
security:
- kind: domain-security
  name: Carvel Domain Security
  slug: carvel-domain-security
  summary_line: TLSv1.3 · HSTS
slug: carvel
tags:
- CLI
- Configuration
- Containers
- Deployment
- GitOps
- Kubernetes
- Package Management
- Templating
website: https://carvel.dev/
---
