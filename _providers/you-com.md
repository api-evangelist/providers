---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-05'
api_count: 4
apis:
- description: The You.com Search API returns real-time web search results tailored for AI agents and LLMs, with controls for freshness, category, and result shape.
  name: You.com Search API
  slug: search-api
- description: The Contents API extracts clean, structured page content from one or many URLs, returning text suitable for downstream LLM consumption.
  name: You.com Contents API
  slug: contents-api
- description: The Research API orchestrates multi-step web research to produce ranked, cited responses to complex questions. It is benchmarked at the top of DeepSearchQA.
  name: You.com Research API
  slug: research-api
- description: The Finance Research API specializes in financial intelligence, returning sourced answers to investment and markets questions. Ranked first on FinSearchComp.
  name: You.com Finance Research API
  slug: finance-research-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/you-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/you-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://you.com
- group: docs
  title: ''
  type: Documentation
  url: https://you.com/docs
- group: company
  title: ''
  type: Blog
  url: https://you.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/YouCom
- group: commercial
  title: ''
  type: Pricing
  url: https://you.com/platform
- group: commercial
  title: ''
  type: TermsOfService
  url: https://about.you.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://about.you.com/privacy-policy/
- group: other
  title: ''
  type: X
  url: https://x.com/youdotcom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/youdotcom
created: '2026-05-23'
description: You.com runs an AI search and chat product alongside a developer platform that exposes web search APIs designed for AI systems, agents, and LLMs. The platform offers Search, Web Search, Contents, News, Smart, Research, and Finance Research APIs for grounding LLMs in real-time web data. You.com publishes benchmark wins on DeepSearchQA and FinSearchComp and targets 300ms p99 latency with 99.99% uptime and SOC 2 enterprise controls. APIs use X-API-Key authentication and a Python SDK is available. Free trial access is provided through the platform dashboard with enterprise options including zero data retention.
finops:
- name: You Com Finops
  service_category: API
  slug: you-com-finops
graphqls:
- description: You.com provides AI search and chat APIs. Their Smart API covers web search with AI-generated answers, custom AI assistants, code generation, summarization, and real-time news with citations.
  name: You.com GraphQL API
  slug: you-com-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/you-com.png
layout: provider
modified: '2026-05-23'
name: You.com
nav: Providers
network: true
overview: 'You.com publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Search, AI Search, LLMs, AI Agents, and Research.


  You.com''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: You Com Plans Pricing
  plan_count: 1
  slug: you-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: You Com Rate Limits
  slug: you-com-rate-limits
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 36.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: You Com Domain Security
  slug: you-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: You Com Vulnerability Disclosure
  slug: you-com-vulnerability-disclosure
  summary_line: disclosure policy published
slug: you-com
tags:
- Search
- AI Search
- LLMs
- AI Agents
- Research
- News
- Finance
- Web Index
- Real-Time
- SOC 2
website: https://you.com
---
