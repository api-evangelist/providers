---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Zhipu Ai Agentic Access
  operation_count: 14
  slug: zhipu-ai-agentic-access
  summary_line: 14 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.z.ai/api
  baseurl_source: declared
  description: The Agents API from Zhipu AI — 3 operation(s) for agents.
  name: Zhipu AI Agents API
  slug: zhipu-ai-agents-api
- baseURL: https://api.z.ai/api
  baseurl_source: declared
  description: The Tools API API from Zhipu AI — 1 operation(s) for tools api.
  name: Zhipu AI Tools API
  slug: zhipu-ai-tools-api-api
- baseURL: https://api.z.ai/api
  baseurl_source: declared
  description: The Paa S API from Zhipu AI — 10 operation(s) for paa s.
  name: Zhipu AI Paa S API
  slug: zhipu-ai-paa-s-api
artifact_total: 16
collections:
- collection_type: open
  name: Z.AI Agents API
  slug: open-zhipu-ai-agents-api
- collection_type: open
  name: Z.AI Agents Paas API
  slug: open-zhipu-ai-paas-api
- collection_type: open
  name: Z.AI Agents Tools API API
  slug: open-zhipu-ai-tools-api-api
- collection_type: open
  name: Z.AI API
  slug: open-zhipu-ai
common:
- group: other
  href: https://artifacts.apis.io/zhipu-ai/capabilities/zhipu-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/zhipu-ai-capability-edges.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.z.ai/guides/overview/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.zhipuai.cn/blog
- group: agent
  href: https://artifacts.apis.io/zhipu-ai/agentic-access/zhipu-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zhipu-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/zhipu-ai/security/zhipu-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zhipu-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/zhipu-ai/security/zhipu-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zhipu-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/zhipu-ai/authentication/zhipu-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zhipu-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zai-org
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zhipuai
- group: company
  title: ''
  type: Website
  url: https://www.zhipuai.cn/
- group: company
  title: ''
  type: AlternateWebsite
  url: https://z.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.z.ai
- group: commercial
  href: https://artifacts.apis.io/zhipu-ai/plans/zhipu-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zhipu-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/zhipu-ai/rate-limits/zhipu-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zhipu-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/zhipu-ai/finops/zhipu-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/zhipu-ai-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.z.ai/llms.txt
created: '2026-05-08'
description: Zhipu AI (Z.ai / BigModel) is a Chinese AI research lab and the developer of the GLM (General Language Model) family. The Z.ai open platform exposes chat completions, vision, image generation, video generation, web search, audio transcription, embeddings, fine-tuning, and agent APIs across the GLM-5, GLM-4.7, GLM-4.6, and GLM-4.5 model series.
finops:
- has_sources: true
  method: generated
  name: Zhipu Ai Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: zhipu-ai-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zhipu-ai.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.z.ai over HTTP.
  name: Zhipu AI MCP Server
  slug: zhipu-ai
modified: '2026-10-06'
name: Zhipu AI
nav: Providers
network: true
overview: 'Zhipu AI publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Agents API, Tools API, and Paa S API. Tagged areas include Artificial Intelligence, LLM, Inference, GLM, and ChatGLM.


  The Zhipu AI catalog on APIs.io includes 1 Spectral governance ruleset.


  Zhipu AI''s developer surface includes pricing, engineering blog, authentication, documentation, and 12 more developer resources.'
plans:
- name: Zhipu Ai Plans Pricing
  plan_count: 29
  slug: zhipu-ai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Zhipu Ai Rate Limits
  slug: zhipu-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Zhipu AI API Rules
  rule_count: 61
  severity_counts:
    error: 56
    hint: 0
    info: 2
    warn: 3
  slug: zhipu-ai-rules
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 55.3
    contract_governance: 13.6
    contract_quality: 53.5
    developer_ergonomics: 23.8
    discoverability: 75.0
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/zhipu-ai/zhipu-ai-2026-06-20T201901.png
security:
- kind: authentication
  name: Zhipu Ai Authentication
  slug: zhipu-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zhipu Ai Domain Security
  slug: zhipu-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zhipu Ai Vulnerability Disclosure
  slug: zhipu-ai-vulnerability-disclosure
  summary_line: no policy recorded
slug: zhipu-ai
tags:
- Artificial Intelligence
- LLM
- Inference
- GLM
- ChatGLM
- Multi-Modal
- Foundation Models
website: https://www.zhipuai.cn/
---
