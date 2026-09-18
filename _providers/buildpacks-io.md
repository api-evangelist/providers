---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Buildpacks Io Agentic Access
  operation_count: 3
  slug: buildpacks-io-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: The Buildpack API (currently 0.12) defines the contract between an individual buildpack and the lifecycle. It specifies the on-disk layout of a buildpack (buildpack.toml, bin/detect, bin/build), the b
  name: Buildpack Specification
  slug: buildpack-spec
- description: The Platform API (currently 0.15) defines how platforms (pack, kpack, Tekton Pipelines, GitLab Auto DevOps, CircleCI Orb, Project Piper) orchestrate the lifecycle. Specifies the lifecycle binary surfa
  name: Platform Specification
  slug: platform-spec
- description: The Distribution API (currently 0.3) defines how buildpacks, extensions, and builders are packaged as OCI artifacts and published to OCI registries. Covers labels (io.buildpacks.buildpack.api, io.buil
  name: Distribution Specification
  slug: distribution-spec
- description: Image extensions emit Dockerfile snippets applied by the `extender` lifecycle binary to the build and/or run image. Share the buildpack surface (extension.toml, bin/detect, bin/generate) but produce D
  name: Image Extension Specification
  slug: image-extension-spec
- description: The Project Descriptor extension defines project.toml — the optional app-root file letting developers declare their builder image, include/exclude globs, buildpack overrides (pre/group/post), and buil
  name: Project Descriptor (project.toml)
  slug: project-descriptor-spec
- description: The Service Bindings extension specifies how external service credentials and configuration are surfaced to detect and build under $CNB_PLATFORM_DIR/bindings/. Aligns with the Service Binding Specific
  name: Service Bindings Extension
  slug: service-bindings-spec
- baseURL: https://registry.buildpacks.io/api/v1
  baseurl_source: declared
  description: Retrieve buildpack version metadata
  name: buildpacks-io Buildpacks API
  slug: buildpacks-io-buildpacks-api
- baseURL: https://registry.buildpacks.io/api/v1
  baseurl_source: declared
  description: Search the buildpack registry by keyword
  name: buildpacks-io Search API
  slug: buildpacks-io-search-api
artifact_total: 48
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cloud Native Registry Buildpacks API
  slug: open-buildpacks-io-buildpacks-api
- collection_type: open
  name: Cloud Native Registry Buildpacks Search API
  slug: open-buildpacks-io-search-api
- collection_type: open
  name: Cloud Native Buildpacks Registry API
  slug: open-buildpacks-registry-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.buildpacks.io/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/buildpacks/registry-index/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/buildpacks/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/buildpacks/.github/blob/main/CONTRIBUTING.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/agentic-access/buildpacks-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/buildpacks-io-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/security/buildpacks-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildpacks-io-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://buildpacks.io
- group: docs
  title: ''
  type: Documentation
  url: https://buildpacks.io/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://buildpacks.io/docs/for-app-developers/concepts/
- group: docs
  title: ''
  type: Documentation
  url: https://buildpacks.io/docs/for-app-developers/
- group: docs
  title: ''
  type: Documentation
  url: https://buildpacks.io/docs/for-buildpack-authors/
- group: docs
  title: ''
  type: Documentation
  url: https://buildpacks.io/docs/for-platform-operators/
- group: docs
  title: ''
  type: Documentation
  url: https://buildpacks.io/docs/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://buildpacks.io/docs/app-journey
- group: operate
  title: ''
  type: Community
  url: https://buildpacks.io/community/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/buildpacks
- group: learn
  title: ''
  type: VideoChannel
  url: https://www.youtube.com/@buildpacks
- group: other
  title: ''
  type: SocialMedia
  url: https://twitter.com/buildpacks_io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/buildpacks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/buildpacks-community
- group: other
  title: ''
  type: Repository
  url: https://github.com/buildpacks/spec
- group: other
  title: ''
  type: Repository
  url: https://github.com/buildpacks/rfcs
- group: other
  title: ''
  type: Repository
  url: https://github.com/buildpacks/community
- group: other
  title: ''
  type: Governance
  url: https://github.com/buildpacks/community/blob/main/GOVERNANCE.md
- group: operate
  title: ''
  type: RoadMap
  url: https://github.com/buildpacks/community/blob/main/ROADMAP.md
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/buildpacks/community/blob/main/TEAMS.md
- group: other
  title: ''
  type: CaseStudies
  url: https://github.com/buildpacks/community/blob/main/ADOPTERS.md
- group: build
  title: ''
  type: Tools
  url: https://github.com/buildpacks/pack
- group: build
  title: ''
  type: Tools
  url: https://github.com/buildpacks/lifecycle
- group: other
  title: ''
  type: ContainerImage
  url: https://hub.docker.com/r/buildpacksio/lifecycle
- group: build
  title: ''
  type: SDKs
  url: https://github.com/buildpacks/libcnb
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/buildpacks/samples
- group: build
  title: ''
  type: Tools
  url: https://github.com/buildpacks/github-actions
- group: build
  title: ''
  type: Tools
  url: https://github.com/buildpacks/pack-orb
- group: build
  title: ''
  type: Tools
  url: https://github.com/buildpacks-community/kpack
- group: other
  title: ''
  type: Repository
  url: https://github.com/buildpacks/registry-index
- group: other
  title: ''
  type: Repository
  url: https://github.com/buildpacks/registry-api
- group: start
  title: ''
  type: Portal
  url: https://registry.buildpacks.io
- group: other
  title: ''
  type: Analytics
  url: https://buildpacks.devstats.cncf.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cncf.io/projects/buildpacks/
- group: other
  title: ''
  type: MailingList
  url: https://lists.cncf.io/g/cncf-buildpacks
- group: operate
  title: ''
  type: Forums
  url: https://slack.cncf.io
- group: operate
  title: ''
  type: Forums
  url: https://github.com/buildpacks/community/discussions
- group: operate
  title: ''
  type: Forums
  url: https://stackoverflow.com/questions/tagged/buildpack
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/vocabulary/buildpacks-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buildpacks-io-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/rules/buildpacks-io-rules.yml
  title: ''
  type: SpectralRules
  url: rules/buildpacks-io-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/json-ld/buildpacks-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buildpacks-io-context.jsonld
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/packages/buildpacks-io-packages.yml
  title: ''
  type: Packages
  url: packages/buildpacks-io-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/packages/buildpacks-io-packages.yml
  title: ''
  type: SDKs
  url: packages/buildpacks-io-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/cli/buildpacks-io-cli.yml
  title: ''
  type: CLI
  url: cli/buildpacks-io-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/llms/buildpacks-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buildpacks-io-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/mcp/buildpacks-io-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/buildpacks-io-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/conformance/buildpacks-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buildpacks-io-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/conformance/buildpacks-io-conformance.yml
  title: ''
  type: Compliance
  url: conformance/buildpacks-io-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/errors/buildpacks-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/buildpacks-io-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/lifecycle/buildpacks-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/buildpacks-io-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/lifecycle/buildpacks-io-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/buildpacks-io-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/changelog/buildpacks-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/buildpacks-io-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/authentication/buildpacks-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/buildpacks-io-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/conventions/buildpacks-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/buildpacks-io-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/data-model/buildpacks-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buildpacks-io-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/plans/buildpacks-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buildpacks-io-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/rate-limits/buildpacks-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/buildpacks-io-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/security/buildpacks-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/buildpacks-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/buildpacks/.github/blob/main/SECURITY.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/well-known/buildpacks-io-well-known.yml
  title: ''
  type: X-WellKnownProbe
  url: well-known/buildpacks-io-well-known.yml
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/buildpacks/registry-api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linuxfoundation.org/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://buildpacks.io/features
- group: docs
  title: ''
  type: Documentation
  url: https://buildpacks.io/history
created: '2026-05-25'
description: Cloud Native Buildpacks (CNB) is a CNCF Graduated project (graduated 2026-07-17) that transforms application source code into OCI images that can run on any cloud. The v3 specification — Buildpack API 0.12, Platform API 0.15, and Distribution API 0.3 — defines a modular, vendor-neutral contract between buildpacks, builders, lifecycles, and platforms. CNB consolidates a decade of production experience from Heroku and Pivotal/Cloud Foundry and provides the reference lifecycle (buildpacksio/lifecycle), the `pack` CLI, language bindings (libcnb in Go/Rust/.NET), the Kubernetes-native `kpack` platform, the public community registry at registry.buildpacks.io, and an open RFC-driven governance model.
examples:
- key_count: 15
  name: Buildpacks Registry Version Example
  slug: buildpacks-registry-version-example
- key_count: 2
  name: Buildpacks Registry Versions List Example
  slug: buildpacks-registry-versions-list-example
features:
- Buildpack API 0.12 — modular detect/build contract producing OCI layers without Dockerfiles
- Platform API 0.15 — lifecycle orchestration surface (analyze, detect, restore, extend, build, export, rebase, launch)
- Distribution API 0.3 — OCI-packaged buildpacks, extensions, and builders
- Image extensions — Dockerfile snippets applied by the `extender` for base-image customization
- Project Descriptor (project.toml) — declarative app-side build configuration
- Build plan with provides/requires reconciliation across composite (meta) buildpacks
- Per-layer caching with launch/build/cache types in `<layer>.toml`
- Rebase — swap run image base layers in seconds without rebuilding app layers
- Targets (os/arch/distros) replacing the legacy stacks model since Buildpack API 0.12
- Per-layer SBOM emission in CycloneDX, SPDX, and Syft formats; aggregated into io.buildpacks.build.metadata
- Standard OCI image labels (io.buildpacks.lifecycle.metadata, io.buildpacks.build.metadata, io.buildpacks.project.metadata, io.buildpacks.rebasable)
- Reference lifecycle distributed as buildpacksio/lifecycle Docker image
- Reference CLI `pack` (v0.40.9, August 2026) implementing the Platform Interface Specification
- Public community registry at registry.buildpacks.io with `pack buildpack register/pull/yank`
- Language bindings via libcnb (Go) and libcnb.rs (Rust, maintained by Heroku at github.com/heroku/libcnb.rs)
- Kubernetes-native platform via kpack with Image/Builder/Stack CRDs
- CI integrations — GitHub Actions, CircleCI Orb, GitLab Auto DevOps, Tekton, Project Piper
- Multi-arch builders (linux/amd64, linux/arm64, windows) selected via target reconciliation
- Service Bindings extension aligned with the Service Binding Specification for Kubernetes
- Vendor-neutral CNCF Graduated project (accepted 2018-10-03, incubating 2020-11-18, graduated 2026-07-17) with public RFC process
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/buildpacks-io.png
json_schemas:
- name: Buildpack Build Plan
  property_count: 3
  slug: buildpacks-build-plan
- name: buildpack.toml
  property_count: 6
  slug: buildpacks-buildpack-toml
- name: launch.toml
  property_count: 3
  slug: buildpacks-launch-toml
- name: project.toml (Project Descriptor)
  property_count: 2
  slug: buildpacks-project-toml
json_structures:
- name: Buildpacks Io Structure
  property_count: 0
  slug: buildpacks-io-structure
jsonld:
- class_count: 21
  name: Buildpacks Io Context
  property_count: 10
  slug: buildpacks-io-context
layout: provider
modified: '2026-09-17'
name: Buildpacks Io
nav: Providers
network: true
overview: 'Buildpacks Io publishes 2 APIs on the [APIs.io](https://apis.io/) network: buildpacks-io Buildpacks API and buildpacks-io Search API. Tagged areas include Cloud Native Buildpacks, Container Images, Build Automation, CNCF, and Open-Source.


  The Buildpacks Io catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Buildpacks Io''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, tooling, code examples, CLI, and 64 more developer resources.'
plans:
- name: Buildpacks Io Plans Pricing
  plan_count: 0
  slug: buildpacks-io-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Buildpacks Io Rate Limits
  slug: buildpacks-io-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Buildpacks Io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: buildpacks-io-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Buildpacks Io API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: buildpacks-io-rules
score:
  band: developing
  composite: 53.7
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.5
    catalog_earned_first_party: 0.0
    catalog_gap: 52.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 13.7
  facets:
    access_clarity: 18.4
    contract_governance: 47.0
    contract_quality: 72.1
    developer_ergonomics: 73.2
    discoverability: 59.3
    operational_transparency: 44.7
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/buildpacks-io/refs/heads/main/screenshots/buildpacks-io-2026-06-20T173753.png
security:
- kind: authentication
  name: Buildpacks Io Authentication
  slug: buildpacks-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Buildpacks Io Domain Security
  slug: buildpacks-io-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Buildpacks Io Vulnerability Disclosure
  slug: buildpacks-io-vulnerability-disclosure
  summary_line: Hackerone
slug: buildpacks-io
tags:
- Cloud Native Buildpacks
- Container Images
- Build Automation
- CNCF
- Open-Source
- Developer Tools
- OCI
- Specification
- Supply Chain
- Registry
website: https://www.buildpacks.io/
---
