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
- description: The Maxim REST API provides programmatic access to prompts, workflows, agents, datasets, evaluators, test runs, logging, tracing, models, alerts, and log repositories. It supports OpenTelemetry-compat
  name: Maxim AI API
  slug: maxim-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/maxim-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maxim-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getmaxim.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.getmaxim.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://www.getmaxim.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maximhq
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getmaxim.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getmaxim.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getmaxim.ai/privacy
- group: other
  title: ''
  type: X
  url: https://x.com/getmaximai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/maxim-ai
created: '2026-05-23'
description: Maxim AI is an end-to-end platform for the simulation, evaluation, and observability of AI agents and LLM applications. It provides distributed tracing, 50+ pre-built evaluators, offline and online evaluations, no-code agent and workflow builders, prompt versioning, dataset management, and real-time monitoring dashboards. Maxim targets engineering and quality teams shipping production AI features and is available as cloud-hosted SaaS, hybrid (VPC peering), or self-hosted (zero-touch VPC isolation). The company monetizes through tiered SaaS plans and enterprise licenses.
finops:
- name: Maxim Finops
  service_category: API
  slug: maxim-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maxim.png
layout: provider
modified: '2026-05-23'
name: Maxim AI
nav: Providers
network: true
overview: 'Maxim AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, LLM, Agents, Observability, and Evaluation.


  Maxim AI''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Maxim Plans Pricing
  plan_count: 1
  slug: maxim-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 2
  name: Maxim Rate Limits
  slug: maxim-rate-limits
score:
  band: emerging
  composite: 26.2
  delta: -2.3
  facets:
    commercial_clarity: 68.4
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 28.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 26.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maxim/refs/heads/main/screenshots/maxim-2026-06-20T185048.png
security:
- kind: domain-security
  name: Maxim Domain Security
  slug: maxim-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Maxim Trust Center
  slug: maxim-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: maxim
tags:
- Artificial Intelligence
- LLM
- Agents
- Observability
- Evaluation
- Simulation
- Tracing
- Prompts
- Datasets
- Monitoring
- Voice
- OpenTelemetry
website: https://www.getmaxim.ai
---
