---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.8
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Live GPU cloud price comparison across the whole market, as a REST API and MCP server.
  name: FastGPU API
  slug: fastgpu-api
- baseURL: https://fastgpu.co
  baseurl_source: spec
  description: Match an AI workload to the cheapest live GPU that can run it. No key required.
  name: FastGPU Matching API
  slug: fastgpu-matching-api
- baseURL: https://fastgpu.co
  baseurl_source: spec
  description: Live GPU rental prices, cheapest first. /api/v1/gpus needs no key.
  name: FastGPU Prices API
  slug: fastgpu-prices-api
- baseURL: https://fastgpu.co
  baseurl_source: spec
  description: Launch and manage GPUs through FastGPU (API key required).
  name: FastGPU Router API
  slug: fastgpu-router-api
artifact_total: 8
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fastgpu/refs/heads/main/rules/fastgpu-rules.yml
  title: ''
  type: Spectral
  url: rules/fastgpu-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fastgpu/refs/heads/main/vocabulary/fastgpu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fastgpu-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fastgpu/refs/heads/main/conformance/fastgpu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fastgpu-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fastgpu/refs/heads/main/plans/fastgpu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fastgpu-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fastgpu/refs/heads/main/errors/fastgpu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fastgpu-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fastgpu/refs/heads/main/llms/fastgpu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fastgpu-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fastgpu/refs/heads/main/a2a/fastgpu-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/fastgpu-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fastgpu/refs/heads/main/mcp/fastgpu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fastgpu-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fastgpu/refs/heads/main/hosts/fastgpu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fastgpu-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fastgpu/refs/heads/main/vendors/fastgpu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fastgpu-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fastgpu.co/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fastgpu.co/legal/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fastgpu/refs/heads/main/security/fastgpu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fastgpu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fastgpu.co
- group: docs
  title: ''
  type: Documentation
  url: https://fastgpu.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://fastgpu.co/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://fastgpu.co/pricing
- group: company
  title: ''
  type: Blog
  url: https://fastgpu.co/blog
- group: operate
  title: ''
  type: Support
  url: https://fastgpu.co/support
created: '2026-10-12'
description: FastGPU provides a broker service offering live cloud GPU rental pricing and availability across major providers such as RunPod, Vast.ai, Lambda, AWS, Azure, and GCP. It aggregates real-time market data, enabling users to compare costs, reserve capacity, and integrate pricing into FinOps tools via a RESTful API and a streaming MCP endpoint. The platform also includes a workload matcher to align GPU resources with AI model requirements, supporting developers and enterprises in optimizing compute spend.
image: https://fastgpu.co/opengraph-image
layout: provider
mcp_servers:
- description: Remote MCP server at fastgpu.co.
  name: FastGPU MCP Server
  slug: fastgpu-mcp-yml
modified: '2026-10-12'
name: FastGPU
nav: Providers
network: true
overview: 'FastGPU publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Matching API, Prices API, Router API, and 1 more. Tagged areas include Company, GPU, Cloud, Pricing, and Artificial Intelligence.


  The FastGPU catalog on APIs.io includes 1 Spectral governance ruleset.


  FastGPU''s developer surface includes documentation, API reference, pricing, engineering blog, support, and 14 more developer resources.'
plans:
- name: Fastgpu Plans Pricing
  plan_count: 2
  slug: fastgpu-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: FastGPU API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: fastgpu-rules
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 19.7
    contract_quality: 50.6
    developer_ergonomics: 23.8
    discoverability: 66.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Fastgpu Domain Security
  slug: fastgpu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fastgpu
tags:
- Company
- GPU
- Cloud
- Pricing
- Artificial Intelligence
website: https://fastgpu.co
---
