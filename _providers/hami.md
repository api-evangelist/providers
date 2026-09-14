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
  title: ''
  type: WellKnown
  url: well-known/hami-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hami-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/hami-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hami-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hami-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hami-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hami-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hami-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hami-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hami-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hami-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hami-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: X-SecurityInsights
  url: security/hami-security-insights.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hami-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hami-plans-pricing.yml
- group: agent
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
- Open Source
- Infrastructure
- Observability
- Heterogeneous Computing
website: https://www.project-hami.io/
---
