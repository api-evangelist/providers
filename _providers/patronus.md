---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
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
- description: 'REST API for the Patronus platform: evaluate (run a built-in or custom evaluator), criteria, datasets, projects, experiments, and judge endpoints. Authentication via API key. Python SDK at patronus-ai'
  name: Patronus AI API
  slug: platform
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/patronus-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/patronus-ai-inc
- group: company
  title: ''
  type: Website
  url: https://www.patronus.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.patronus.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/patronus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/patronus-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/patronus-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.patronus.ai/blog
created: '2026-05-08'
description: Patronus AI is an AI evaluation platform offering automated evaluators (Lynx, Glider), guardrails, and experiment tracking for LLM and agentic applications. It exposes a REST API and Python/TypeScript SDKs.
finops:
- name: Patronus Finops
  service_category: AI Evaluation
  slug: patronus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/patronus.png
layout: provider
modified: '2026-05-08'
name: Patronus AI
nav: Providers
network: true
overview: 'Patronus AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Evaluation, GenAI, Guardrails, Hallucination Detection, and LLM.


  Patronus AI''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Patronus Plans Pricing
  plan_count: 2
  slug: patronus-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 2
  name: Patronus Rate Limits
  slug: patronus-rate-limits
score:
  band: emerging
  composite: 17.6
  delta: -2.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/patronus/refs/heads/main/screenshots/patronus-2026-06-20T191444.png
security:
- kind: domain-security
  name: Patronus Domain Security
  slug: patronus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: patronus
tags:
- AI Evaluation
- GenAI
- Guardrails
- Hallucination Detection
- LLM
- Agents
website: https://www.patronus.ai/
---
