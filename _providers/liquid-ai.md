---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Hosted inference and customization API for the LFM family. Includes Liquid Playground and LEAP customization/deployment platform. LFM models also distributed on Hugging Face and via OpenRouter for hos
  name: Liquid AI Platform API
  slug: platform
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liquid-ai-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Liquid4All
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/liquid-ai-inc
- group: company
  title: ''
  type: Website
  url: https://www.liquid.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.liquid.ai/
- group: other
  title: ''
  type: HuggingFace
  url: https://huggingface.co/LiquidAI
- group: commercial
  title: ''
  type: Plans
  url: plans/liquid-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/liquid-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/liquid-ai-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.liquid.ai/llms.txt
created: '2026-05-08'
description: Liquid AI is an MIT spinoff developing Liquid Foundation Models (LFMs) - a new class of generative models based on liquid neural networks. Offers LFM2 (2.6B / 8B-A1B / 24B-A2B) and LFM2.5 (350M / 1.2B variants) with text, vision, audio, and thinking modes. The LEAP platform enables LFM customization and on-device deployment.
finops:
- name: Liquid Ai Finops
  service_category: AI
  slug: liquid-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/liquid-ai.png
layout: provider
modified: '2026-05-08'
name: Liquid AI
nav: Providers
network: true
overview: 'Liquid AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, LLM, Inference, Foundation Models, and Liquid Networks.


  Liquid AI''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Liquid Ai Plans Pricing
  plan_count: 1
  slug: liquid-ai-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Liquid Ai Rate Limits
  slug: liquid-ai-rate-limits
score:
  band: emerging
  composite: 13.2
  delta: -0.1
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liquid-ai/refs/heads/main/screenshots/liquid-ai-2026-06-20T184556.png
security:
- kind: domain-security
  name: Liquid Ai Domain Security
  slug: liquid-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: liquid-ai
tags:
- AI
- LLM
- Inference
- Foundation Models
- Liquid Networks
- Edge AI
- On-Device
website: https://www.liquid.ai/
---
