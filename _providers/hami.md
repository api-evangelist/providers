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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-09-14'
api_count: 2
apis:
- description: The HAMi WebUI backend API. Four gRPC services — Card, Node, Container and Monitor — expose cluster accelerator inventory, node inventory, GPU-consuming workloads and Prometheus-backed range/instant/s
  name: HAMi WebUI API
  slug: hami-webui-api
- baseURL: https://project-hami.io
  baseurl_source: declared
  description: The machine-readable discovery surface of the HAMi documentation website, described by a first-party OpenAPI 3.1.0 document that the site advertises as the service-desc of its RFC 9727 API catalog. Fo
  name: HAMi Website Discovery API
  slug: hami-website-discovery-api
artifact_total: 7
common:
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
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/well-known/hami-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hami-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/llms/hami-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hami-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/packages/hami-packages.yml
  title: ''
  type: Packages
  url: packages/hami-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/conformance/hami-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hami-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/errors/hami-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hami-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/lifecycle/hami-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hami-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/changelog/hami-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hami-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/conventions/hami-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hami-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/data-model/hami-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hami-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/authentication/hami-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hami-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/security/hami-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hami-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/security/hami-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hami-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/security/hami-security-insights.yml
  title: ''
  type: X-SecurityInsights
  url: security/hami-security-insights.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/rate-limits/hami-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hami-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/plans/hami-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hami-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/mcp/hami-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/hami-mcp.yml
created: '2025-01-01'
description: 'HAMi (Heterogeneous AI Computing Virtualization Middleware) is a CNCF incubating open-source project that brings device sharing, memory and core isolation, and topology-aware scheduling to heterogeneous AI accelerators on Kubernetes. It lets several containers share one physical GPU or NPU with hard memory limits and enforced compute quotas, across NVIDIA, Huawei Ascend, Cambricon MLU, Hygon DCU, Enflame GCU, Iluvatar, Moore Threads, MetaX, Kunlunxin and Vastai devices. HAMi ships a scheduler, a device plugin, an in-container enforcement library (HAMi-core/libvgpu), a DRA driver, and HAMi WebUI — an observability dashboard whose backend exposes a gRPC and grpc-gateway REST API over cluster GPU, node, workload and Prometheus-backed monitoring data. The project also publishes a machine-readable discovery surface on its documentation site: an RFC 9727 API catalog, an OpenAPI 3.1 service description, an Agent Skills discovery index, and Content-Signal directives in robots.txt.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hami.png
layout: provider
modified: '2026-09-12'
name: HAMi
nav: Providers
network: true
overview: 'HAMi publishes 1 API on the [APIs.io](https://apis.io/) network: Website Discovery API. Tagged areas include AI Computing, CNCF, GPU Virtualization, Kubernetes, and GPU Sharing.


  HAMi''s developer surface includes documentation, engineering blog, getting-started guide, support, changelog, authentication, and 23 more developer resources.'
plans:
- name: Hami Plans Pricing
  plan_count: 0
  slug: hami-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Hami Rate Limits
  slug: hami-rate-limits
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 37.4
    developer_ergonomics: 57.1
    discoverability: 68.5
    operational_transparency: 34.2
  previous_composite: 38.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/hami/refs/heads/main/screenshots/hami-2026-06-20T182500.png
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
  summary_line: disclosure policy published
slug: hami
tags:
- AI Computing
- CNCF
- GPU Virtualization
- Kubernetes
- GPU Sharing
- Scheduling
- Open-Source
- Infrastructure
- Observability
- Heterogeneous Computing
website: https://www.project-hami.io/
---
