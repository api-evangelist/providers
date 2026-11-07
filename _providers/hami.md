---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The HAMi WebUI backend API. Four gRPC services — Card, Node, Container and Monitor — expose cluster accelerator inventory, node inventory, GPU-consuming workloads and Prometheus-backed range/instant/s
  name: HAMi WebUI API
  slug: hami-webui-api
- baseURL: http://{hami-webui-host}:8000
  baseurl_source: declared
  description: The Robots.txt API from HAMi — 1 operation(s) for robots.txt.
  name: HAMi Robots.txt API
  slug: hami-robots-txt-api
- baseURL: http://{hami-webui-host}:8000
  baseurl_source: declared
  description: The .well Known API from HAMi — 3 operation(s) for .well known.
  name: HAMi .well Known API
  slug: hami-well-known-api
artifact_total: 12
common:
- group: other
  href: https://artifacts.apis.io/hami/overlays/hami-website-discovery-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hami-website-discovery-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.project-hami.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Project-HAMi/HAMi
- group: docs
  title: ''
  type: Documentation
  url: https://project-hami.io/docs/
- group: company
  title: ''
  type: Blog
  url: https://project-hami.io/blog/rss.xml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://project-hami.io/docs/category/developer-guide
- group: start
  title: ''
  type: GettingStarted
  url: https://project-hami.io/docs/get-started/deploy-with-helm
- group: operate
  title: ''
  type: Support
  url: https://project-hami.io/community
- group: operate
  title: ''
  type: Roadmap
  url: https://project-hami.io/docs/contributor/roadmap
- group: operate
  title: ''
  type: ChangeLog
  url: https://project-hami.io/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lfprojects.org/policies/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lfprojects.org/policies/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://github.com/Project-HAMi/HAMi/blob/master/SECURITY.md
- group: agent
  href: https://artifacts.apis.io/hami/well-known/hami-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hami-well-known.yml
- group: agent
  href: https://artifacts.apis.io/hami/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/hami/llms/hami-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hami-llms.txt
- group: build
  href: https://artifacts.apis.io/hami/packages/hami-packages.yml
  title: ''
  type: Packages
  url: packages/hami-packages.yml
- group: design
  href: https://artifacts.apis.io/hami/conformance/hami-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hami-conformance.yml
- group: design
  href: https://artifacts.apis.io/hami/errors/hami-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hami-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hami/lifecycle/hami-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hami-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/hami/changelog/hami-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hami-changelog.yml
- group: design
  href: https://artifacts.apis.io/hami/conventions/hami-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hami-conventions.yml
- group: design
  href: https://artifacts.apis.io/hami/data-model/hami-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hami-data-model.yml
- group: auth
  href: https://artifacts.apis.io/hami/authentication/hami-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hami-authentication.yml
- group: auth
  href: https://artifacts.apis.io/hami/security/hami-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hami-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/hami/security/hami-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hami-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hami/security/hami-security-insights.yml
  title: ''
  type: X-SecurityInsights
  url: security/hami-security-insights.yml
- group: operate
  href: https://artifacts.apis.io/hami/rate-limits/hami-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hami-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/hami/plans/hami-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hami-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/hami/mcp/hami-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/hami-mcp.yml
created: '2025-01-01'
description: 'HAMi (Heterogeneous AI Computing Virtualization Middleware) is a CNCF incubating open-source project that brings device sharing, memory and core isolation, and topology-aware scheduling to heterogeneous AI accelerators on Kubernetes. It lets several containers share one physical GPU or NPU with hard memory limits and enforced compute quotas, across NVIDIA, Huawei Ascend, Cambricon MLU, Hygon DCU, Enflame GCU, Iluvatar, Moore Threads, MetaX, Kunlunxin and Vastai devices. HAMi ships a scheduler, a device plugin, an in-container enforcement library (HAMi-core/libvgpu), a DRA driver, and HAMi WebUI — an observability dashboard whose backend exposes a gRPC and grpc-gateway REST API over cluster GPU, node, workload and Prometheus-backed monitoring data. The project also publishes a machine-readable discovery surface on its documentation site: an RFC 9727 API catalog, an OpenAPI 3.1 service description, an Agent Skills discovery index, and Content-Signal directives in robots.txt.'
finops:
- has_sources: true
  method: derived
  name: Hami Finops
  primary_unit: ''
  service_category: ''
  slug: hami-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hami.png
layout: provider
modified: '2026-09-12'
name: HAMi
nav: Providers
network: true
overview: 'HAMi publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Robots.txt API, .well Known API, and 1 more. Tagged areas include AI Computing, CNCF, GPU Virtualization, Kubernetes, and GPU Sharing.


  The HAMi catalog on APIs.io includes 1 Spectral governance ruleset.


  HAMi''s developer surface includes documentation, engineering blog, getting-started guide, support, changelog, authentication, and 24 more developer resources.'
plans:
- name: Hami Plans Pricing
  plan_count: 0
  slug: hami-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Hami Rate Limits
  slug: hami-rate-limits
rules:
- authorship: generated
  effective_rule_count: 65
  extends:
  - spectral:oas
  name: HAMi API Rules
  rule_count: 24
  severity_counts:
    error: 22
    hint: 0
    info: 1
    warn: 1
  slug: hami-rules
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 42.9
    developer_ergonomics: 57.1
    discoverability: 66.1
    operational_transparency: 34.2
  previous_composite: 42.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/hami/hami-2026-06-20T182500.png
security:
- kind: authentication
  name: Hami Authentication
  slug: hami-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hami Domain Security
  slug: hami-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Hami Vulnerability Disclosure
  slug: hami-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 2
skills:
- name: k8s-debug-pending-pod
  slug: hami-k8s-debug-gpu-pod
- name: hami_vgpu_metrics_summarizer
  slug: hami-vgpu-metrics-summary
slug: hami
tags:
- AI Computing
- CNCF
- GPU Virtualization
- Kubernetes
- GPU Sharing
- Scheduling
- Open Source
- Infrastructure
- Observability
- Heterogeneous Computing
website: https://www.project-hami.io/
---
