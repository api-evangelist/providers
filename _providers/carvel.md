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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.2
  scored_at: '2026-09-05'
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
artifact_total: 13
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
  url: https://carvel.dev/shared/docs/latest/
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
- group: operate
  title: ''
  type: RoadMap
  url: https://github.com/carvel-dev/carvel/blob/develop/ROADMAP.md
- group: auth
  title: ''
  type: Security
  url: https://carvel.dev/shared/docs/latest/security-policy/
- group: other
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/carvel-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/carvel-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carvel-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/carvel-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/carvel-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/carvel-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/carvel-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/carvel-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/carvel-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/carvel-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/carvel-vulnerability-disclosure.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/carvel-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/carvel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/carvel-rate-limits.yml
created: '2026-03-26'
description: Carvel is a set of reliable, single-purpose, composable command-line tools that help build, configure, and deploy applications to Kubernetes. The toolset includes ytt for YAML templating, kapp for application lifecycle management, kbld for immutable image references, imgpkg for OCI bundling, vendir for vendored configuration, and kapp-controller for GitOps-style continuous delivery.
finops:
- name: Carvel Finops
  service_category: API
  slug: carvel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carvel.png
layout: provider
modified: '2026-09-05'
name: Carvel
nav: Providers
network: true
overview: 'Carvel publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CLI, Configuration, Containers, Deployment, and GitOps.


  Carvel''s developer surface includes documentation, engineering blog, CLI, changelog, authentication, sandbox, and 25 more developer resources.'
plans:
- name: Carvel Plans Pricing
  plan_count: 0
  slug: carvel-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Carvel Rate Limits
  slug: carvel-rate-limits
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 44.0
    catalog_earned_first_party: 6.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.1
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 34.7
    developer_ergonomics: 36.9
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 100.0
  previous_composite: 26.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/carvel/refs/heads/main/screenshots/carvel-2026-06-20T174027.png
security:
- kind: authentication
  name: Carvel Authentication
  slug: carvel-authentication
  summary_line: delegated-kubernetes-rbac/registry-credentials · 3 schemes
- kind: domain-security
  name: Carvel Domain Security
  slug: carvel-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Carvel Vulnerability Disclosure
  slug: carvel-vulnerability-disclosure
  summary_line: contact published
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
