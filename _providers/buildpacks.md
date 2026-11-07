---
access_model:
  confidence: high
  label: Free open source · no account, no plans
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - license
  - probe
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Buildpack API is the contract between a buildpack and the lifecycle. It defines the detect and build executables, layers, build-plan provisions and requirements, and image extension lifecycle that
  name: Buildpack API Specification
  slug: buildpack-api
- description: The Platform API is the contract between the CNB lifecycle and a platform such as pack, kpack, or a CI runner. It defines how builders, stacks, run images, and inputs are passed to the lifecycle phase
  name: Platform API Specification
  slug: platform-api
- description: The Distribution API specifies how buildpacks and builders are packaged as OCI artifacts, signed, and distributed through OCI registries. It also covers how meta-buildpacks compose other buildpacks an
  name: Distribution API Specification
  slug: distribution-api
- description: pack is the reference command-line interface for Cloud Native Buildpacks. It implements the Platform API to build OCI images from source on a developer's workstation, manages builders and buildpack pa
  name: pack CLI
  slug: pack-cli
- description: The CNB Lifecycle is the reference implementation of the Buildpack and Platform APIs. It runs the detect, analyze, restore, build, export, and rebase phases used by all CNB platforms to produce reprod
  name: CNB Lifecycle
  slug: lifecycle
- description: The Cloud Native Buildpacks registry indexes published buildpacks for discovery and reuse. It mirrors metadata for buildpack packages stored in OCI registries and exposes a browseable catalog at regis
  name: Buildpack Registry
  slug: registry
- baseURL: https://{kubernetes-apiserver}/apis/kpack.io/v1alpha1
  baseurl_source: declared
  description: The kpack API from Cloud Native Buildpacks — 25 operation(s) for kpack.
  name: Cloud Native Buildpacks Kpack API
  slug: buildpacks-kpack-api
artifact_total: 26
common:
- group: other
  href: https://artifacts.apis.io/buildpacks/capabilities/buildpacks-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/buildpacks-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/buildpacks/skills/buildpacks-build-an-image-with-kpack.md
  title: ''
  type: AgentSkill
  url: skills/buildpacks-build-an-image-with-kpack.md
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/buildpacks/spec/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/buildpacks/spec/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/buildpacks/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/buildpacks/spec/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/buildpacks/spec/blob/main/LICENSE
- group: auth
  href: https://artifacts.apis.io/buildpacks/security/buildpacks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildpacks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildpacks.io
- group: docs
  title: ''
  type: Documentation
  url: https://buildpacks.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/buildpacks
- group: company
  title: ''
  type: Blog
  url: https://medium.com/buildpacks
- group: company
  title: ''
  type: BlogRSS
  url: https://medium.com/feed/buildpacks
- group: operate
  title: ''
  type: Community
  url: https://buildpacks.io/community/
- group: start
  title: ''
  type: Registry
  url: https://registry.buildpacks.io/
- group: docs
  title: ''
  type: Specification
  url: https://github.com/buildpacks/spec/blob/main/buildpack.md
- group: other
  title: ''
  type: MailingList
  url: https://lists.cncf.io/g/cncf-buildpacks/join
- group: operate
  title: ''
  type: Slack
  url: https://slack.cncf.io
- group: other
  title: ''
  type: CNCF
  url: https://www.cncf.io/projects/buildpacks/
- group: other
  title: ''
  type: DevStats
  url: https://buildpacks.devstats.cncf.io/
- group: build
  href: https://artifacts.apis.io/buildpacks/packages/buildpacks-packages.yml
  title: ''
  type: Packages
  url: packages/buildpacks-packages.yml
- group: build
  href: https://artifacts.apis.io/buildpacks/packages/buildpacks-packages.yml
  title: ''
  type: SDKs
  url: packages/buildpacks-packages.yml
- group: build
  href: https://artifacts.apis.io/buildpacks/cli/buildpacks-cli.yml
  title: ''
  type: CLI
  url: cli/buildpacks-cli.yml
- group: design
  href: https://artifacts.apis.io/buildpacks/conventions/buildpacks-conventions.yml
  title: ''
  type: Conventions
  url: conventions/buildpacks-conventions.yml
- group: design
  href: https://artifacts.apis.io/buildpacks/conventions/buildpacks-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/buildpacks-conventions.yml
- group: auth
  href: https://artifacts.apis.io/buildpacks/authentication/buildpacks-authentication.yml
  title: ''
  type: Authentication
  url: authentication/buildpacks-authentication.yml
- group: design
  href: https://artifacts.apis.io/buildpacks/errors/buildpacks-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/buildpacks-problem-types.yml
- group: design
  href: https://artifacts.apis.io/buildpacks/lifecycle/buildpacks-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/buildpacks-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/buildpacks/lifecycle/buildpacks-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/buildpacks-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/buildpacks/changelog/buildpacks-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/buildpacks-changelog.yml
- group: design
  href: https://artifacts.apis.io/buildpacks/conformance/buildpacks-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buildpacks-conformance.yml
- group: auth
  href: https://artifacts.apis.io/buildpacks/conformance/buildpacks-conformance.yml
  title: ''
  type: Compliance
  url: conformance/buildpacks-conformance.yml
- group: design
  href: https://artifacts.apis.io/buildpacks/data-model/buildpacks-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buildpacks-data-model.yml
- group: auth
  href: https://artifacts.apis.io/buildpacks/security/buildpacks-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/buildpacks-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/buildpacks/security/buildpacks-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/buildpacks-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/buildpacks/security/buildpacks-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/buildpacks-trust-center.yml
- group: agent
  href: https://artifacts.apis.io/buildpacks/llms/buildpacks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buildpacks-llms.txt
- group: other
  href: https://artifacts.apis.io/buildpacks/overlays/buildpacks-kpack-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/buildpacks-kpack-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/buildpacks/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/buildpacks/plans/buildpacks-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buildpacks-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/buildpacks/rate-limits/buildpacks-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/buildpacks-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/buildpacks/finops/buildpacks-finops.yml
  title: ''
  type: FinOps
  url: finops/buildpacks-finops.yml
- group: docs
  href: https://artifacts.apis.io/buildpacks/openapi/_original/buildpacks-kpack-swagger.json
  title: ''
  type: OpenAPI
  url: openapi/_original/buildpacks-kpack-swagger.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://buildpacks.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://buildpacks.io/docs/reference/spec/
- group: start
  title: ''
  type: GettingStarted
  url: https://buildpacks.io/docs/app-journey
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linuxfoundation.org/privacy/
- group: operate
  title: ''
  type: Support
  url: https://buildpacks.io/community/
- group: other
  title: ''
  type: x-RFCs
  url: https://github.com/buildpacks/rfcs
created: '2025-01-01'
description: 'Cloud Native Buildpacks (CNBs) transform application source code into OCI-compliant container images that can run on any cloud, without requiring Dockerfiles. Initiated by Pivotal and Heroku in January 2018, CNB joined the CNCF as a Sandbox project in October 2018 and GRADUATED on 11 August 2026, the foundation''s highest maturity tier. It is licensed Apache-2.0. CNB is primarily a specification project: three independently versioned contracts — Buildpack API 0.12, Platform API 0.15 and Distribution API 0.3 — plus reference implementations (the pack CLI and the lifecycle). It centralizes container expertise through composable buildpacks, enables layer rebasing for efficient OS updates, and generates Software Bills of Materials in CycloneDX, SPDX and Syft formats. The pack CLI, the kpack Kubernetes operator and the public Buildpack Registry API are the primary integration points.'
features:
- features:
  - Source-to-Image Conversion
  - Builder Selection
  - Environment Variable Injection
  - Volume Mount Support
  - Cache Integration
  name: pack build
  url: https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/cli/
- features:
  - Create Custom Builders
  - Inspect Builder Contents
  - Trust Builder Configuration
  - Suggest Default Builders
  name: pack builder
  url: https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/cli/
- features:
  - Update Base Image Layers
  - No Source Rebuild Required
  - Fast Security Patching
  name: pack rebase
  url: https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/cli/
- features:
  - Software Bill of Materials
  - Dependency Inventory
  - Security Auditing
  - License Tracking
  name: pack sbom download
  url: https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/cli/
- features:
  - Community Buildpack Discovery
  - Namespace Registration
  - Version Tracking
  - Verified Buildpacks
  name: Buildpack Registry
  url: https://registry.buildpacks.io/
finops:
- has_sources: true
  method: derived
  name: Buildpacks Finops
  primary_unit: ''
  service_category: ''
  slug: buildpacks-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/buildpacks.png
layout: provider
modified: '2026-09-16'
name: Cloud Native Buildpacks
nav: Providers
network: true
overview: 'Cloud Native Buildpacks publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Kpack API, and 6 more. Tagged areas include Cloud Native Buildpacks, Build Tools, CI/CD, Cloud-Native, and CNCF.


  The Cloud Native Buildpacks catalog on APIs.io includes 1 Spectral governance ruleset.


  Cloud Native Buildpacks'' developer surface includes documentation, engineering blog, CLI, authentication, changelog, API reference, getting-started guide, and 42 more developer resources.'
plans:
- name: Buildpacks Plans Pricing
  plan_count: 0
  slug: buildpacks-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Buildpacks Rate Limits
  slug: buildpacks-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Cloud Native Buildpacks API Rules
  rule_count: 42
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 5
  slug: buildpacks-rules
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 31.8
    contract_quality: 42.0
    developer_ergonomics: 73.2
    discoverability: 64.3
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 65.0
  previous_composite: 49.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/buildpacks/buildpacks-2026-06-20T173752.png
security:
- kind: authentication
  name: Buildpacks Authentication
  slug: buildpacks-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Buildpacks Domain Security
  slug: buildpacks-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Buildpacks Vulnerability Disclosure
  slug: buildpacks-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Buildpacks Trust Center
  slug: buildpacks-trust-center
  summary_line: trust center published
skill_count: 2
skills:
- name: build-an-image-with-kpack
  slug: buildpacks-build-an-image-with-kpack
- name: publish-a-buildpack-to-the-registry
  slug: buildpacks-publish-a-buildpack-to-the-registry
slug: buildpacks
tags:
- Cloud Native Buildpacks
- Build Tools
- CI/CD
- Cloud-Native
- CNCF
- Container Images
- Containers
- OCI
- Open Source
use_cases:
- features:
  - No Dockerfile Required
  - Automatic Dependency Detection
  - Multi-Language Support
  - Reproducible Builds
  - ARM Container Support
  - Windows Container Support
  name: App Developer Image Building
  url: https://buildpacks.io/docs/for-app-developers/
- features:
  - CI/CD Pipeline Integration
  - pack CLI Integration
  - kpack Kubernetes Operator
  - Tekton Pipeline Support
  - CircleCI Integration
  - GitLab CI Integration
  - Custom Builder Creation
  name: Platform Operator Integration
  url: https://buildpacks.io/docs/for-platform-operators/
- features:
  - Custom Language Support
  - Framework-Specific Buildpacks
  - Buildpack Packaging
  - Registry Distribution
  - Extension Authoring
  - Composable Buildpack Groups
  name: Buildpack Authoring
  url: https://buildpacks.io/docs/for-buildpack-authors/
- features:
  - Layer Rebasing
  - Base Image Updates Without Rebuild
  - Minimal Rebuild Surface
  - Stack Switching
  name: OS-Level Security Patching
  url: https://buildpacks.io/docs/reference/spec/platform-api/
website: https://buildpacks.io
---
