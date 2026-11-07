---
access_model:
  confidence: low
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: true
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: NVIDIA provides developer APIs for GPU computing, AI/ML model training and inference, and graphics. The platform includes APIs for CUDA, TensorRT, Omniverse, and cloud GPU services.
  name: NVIDIA Developer API
  slug: nvidia-developer
artifact_total: 29
common:
- group: commercial
  href: https://artifacts.apis.io/nvidia/plans/nvidia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nvidia-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/nvidia/rate-limits/nvidia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nvidia-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/nvidia/finops/nvidia-finops.yml
  title: ''
  type: FinOps
  url: finops/nvidia-finops.yml
- group: auth
  href: https://artifacts.apis.io/nvidia/security/nvidia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nvidia-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NVIDIA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nvidia
- group: company
  title: ''
  type: Website
  url: https://www.nvidia.com
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.nvidia.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://developer.nvidia.com/blog/feed
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/augtera-networks/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/cumulus-networks/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/deci-ai/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/deepmap/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/excelero-storage/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/icerasemi/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/lepton-ai/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/runai/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/swiftstack/
created: '2026-03-21'
description: Nvidia is a Fortune 500 company that provides developer APIs and integration capabilities through its developer platform. NVIDIA provides developer APIs for GPU computing, AI/ML model training and inference, and graphics. The platform includes APIs for CUDA, TensorRT, Omniverse, and cloud GPU services.
finops:
- has_sources: true
  method: generated
  name: Nvidia Finops
  primary_unit: gpu
  service_category: AI Infrastructure
  slug: nvidia-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nvidia.png
layout: provider
modified: '2026-08-21'
name: Nvidia
nav: Providers
network: true
overview: 'Nvidia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GPU, Artificial Intelligence, Machine Learning, Computing, and Graphics.


  Nvidia''s developer surface includes engineering blog and 17 more developer resources.'
plans:
- name: Nvidia Plans Pricing
  plan_count: 5
  slug: nvidia-plans-pricing
press:
- date: ''
  title: NVIDIA Corporation - News - Press Release Details
  url: https://investor.nvidia.com/news/press-release-details/
- date: ''
  title: Latest News | NVIDIA Newsroom
  url: https://nvidianews.nvidia.com/news/latest
- date: ''
  title: NVIDIA and Corning Announce Long-Term Partnership to ...
  url: https://nvidianews.nvidia.com/news/nvidia-and-corning-announce-long-term-partnership-to-strengthen-us-manufacturing-for-ai-infrastructure
- date: ''
  title: NVIDIA Third-Party Press Release and Blog Guidelines
  url: https://www.nvidia.com/en-us/about-nvidia/pr-guidelines/
- date: ''
  title: Dell AI Factory with NVIDIA Delivers Proven Path to ...
  url: https://www.dell.com/en-us/dt/corporate/newsroom/announcements/detailpage.press-releases~usa~2026~03~dell-ai-factory-with-nvidia-delivers-proven-path-to-enterprise-ai-roi.htm
random_paper: 11
rate_limits:
- limit_count: 3
  name: Nvidia Rate Limits
  slug: nvidia-rate-limits
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.3
    operational_transparency: 10.5
  previous_composite: 11.9
  provenance:
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nvidia/nvidia-2026-06-20T190538.png
security:
- kind: domain-security
  name: Nvidia Domain Security
  slug: nvidia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 60
skills:
- name: doca-aes-gcm
  slug: doca-aes-gcm
- name: doca-argp
  slug: doca-argp
- name: doca-argus
  slug: doca-argus
- name: doca-bare-metal-deployment
  slug: doca-bare-metal-deployment
- name: doca-bench-extension
  slug: doca-bench-extension
- name: doca-bench
  slug: doca-bench
- name: doca-bf3-deployment
  slug: doca-bf3-deployment
- name: doca-bf4-deployment
  slug: doca-bf4-deployment
- name: doca-caps
  slug: doca-caps
- name: doca-collectx-deployment
  slug: doca-collectx-deployment
- name: doca-comch
  slug: doca-comch
- name: doca-comm-channel-admin
  slug: doca-comm-channel-admin
- name: doca-common
  slug: doca-common
- name: doca-compress
  slug: doca-compress
- name: doca-container-deployment
  slug: doca-container-deployment
- name: doca-debug
  slug: doca-debug
- name: doca-devemu
  slug: doca-devemu
- name: doca-dma
  slug: doca-dma
- name: doca-dms
  slug: doca-dms
- name: doca-dpa-hl-tracer
  slug: doca-dpa-hl-tracer
- name: doca-dpa
  slug: doca-dpa
- name: doca-dpdk-bridge
  slug: doca-dpdk-bridge
- name: doca-erasure-coding
  slug: doca-erasure-coding
- name: doca-eth
  slug: doca-eth
slug: nvidia
tags:
- GPU
- Artificial Intelligence
- Machine Learning
- Computing
- Graphics
- Fortune 1000
website: https://www.nvidia.com
---
