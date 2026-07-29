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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The core smolagents Python library providing CodeAgent and ToolCallingAgent classes for building AI agents that write Python code or structured JSON to call tools and orchestrate multi-agent systems. '
  name: smolagents Python Library
  slug: smolagents-python-library
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/smolagents-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smolagents-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://huggingface.co/smolagents
- group: docs
  title: ''
  type: Documentation
  url: https://huggingface.co/docs/smolagents/en/index
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/huggingface
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/huggingface/smolagents
- group: company
  title: ''
  type: Blog
  url: https://huggingface.co/blog/smolagents
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/huggingface/smolagents/releases
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/smolagents/
- group: commercial
  title: ''
  type: Pricing
  url: https://huggingface.co/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.huggingface.co
- group: other
  title: ''
  type: X
  url: https://x.com/huggingface
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/huggingface
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/smolagents/refs/heads/main/plans/smolagents-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/smolagents/refs/heads/main/rate-limits/smolagents-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/smolagents/refs/heads/main/finops/smolagents-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://huggingface.co/blog/feed.xml
- group: company
  title: ''
  type: Blog
  url: https://raw.githubusercontent.com/api-evangelist/smolagents/refs/heads/main/blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/smolagents/refs/heads/main/json-ld/smolagents-context.jsonld
created: '2026-06-12'
description: 'smolagents is an open-source Python library developed by Hugging Face that enables developers to build and run powerful AI agents with minimal code. The library provides two primary agent paradigms: CodeAgent, which writes actions as Python code snippets for maximum expressiveness and composability, and ToolCallingAgent, which uses structured JSON for reliable and safe tool interactions. smolagents is model-agnostic, supporting Hugging Face Inference Providers, local Transformers, Ollama, LiteLLM (100+ LLMs), Azure OpenAI, Amazon Bedrock, and MLX models. Hub integration allows teams to share and load agents and tools as Gradio Spaces, and multi-agent orchestration enables hierarchical systems where manager agents coordinate specialized sub-agents.'
finops:
- name: Smolagents Finops
  service_category: ''
  slug: smolagents-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smolagents.png
jsonld:
- class_count: 3
  name: Smolagents Context
  property_count: 13
  slug: smolagents-context
layout: provider
modified: '2026-06-12'
name: smolagents
nav: Providers
network: true
overview: 'smolagents publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Multi-Agent, Python, Code Generation, and LLM.


  The smolagents catalog on APIs.io includes 1 JSON-LD context.


  smolagents'' developer surface includes documentation, engineering blog, changelog, pricing, and 15 more developer resources.'
plans:
- name: Smolagents Plans Pricing
  plan_count: 5
  slug: smolagents-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 21
  name: Smolagents Rate Limits
  slug: smolagents-rate-limits
score:
  band: thin
  composite: 31.1
  delta: -3.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 34.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smolagents/refs/heads/main/screenshots/smolagents-2026-06-20T194059.png
security:
- kind: domain-security
  name: Smolagents Domain Security
  slug: smolagents-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Smolagents Vulnerability Disclosure
  slug: smolagents-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: smolagents
tags:
- AI Agents
- Multi-Agent
- Python
- Code Generation
- LLM
- Hugging Face
- Open Source
- Machine Learning
website: https://huggingface.co/smolagents
---
