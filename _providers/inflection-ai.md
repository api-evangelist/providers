---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Inflection Ai Agentic Access
  operation_count: 1
  slug: inflection-ai-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 3
apis:
- description: Enterprise inference API serving Inflection's empathic conversational foundation models (Inflection-2.5 series and successors). Accepts chat message arrays, context, and parameters and returns assista
  name: Inflection Conversational API
  slug: conversational-api
- description: Interactive playground inside the developer portal for testing prompts against Inflection models before integrating against the Conversational API.
  name: Inflection Developer Playground
  slug: playground
- description: The Inference API from Inflection AI — 1 operation(s) for inference.
  name: Inflection AI Inference API
  slug: inflection-ai-inference-api
artifact_total: 10
collections:
- collection_type: open
  name: Inflection AI API
  slug: open-inflection-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/inflection-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inflection-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inflection-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://inflection.ai/
- group: other
  title: ''
  type: Enterprise
  url: https://inflection.ai/enterprise
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.inflection.ai/
- group: other
  title: ''
  type: Pi
  url: https://pi.ai/
- group: company
  title: ''
  type: Blog
  url: https://inflection.ai/blog
- group: company
  title: ''
  type: Press
  url: https://inflection.ai/press
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inflection-ai/
- group: other
  title: ''
  type: X
  url: https://x.com/inflectionAI
created: '2026-05-23'
description: Inflection AI was founded in 2022 by Mustafa Suleyman, Reid Hoffman, and Karen Simonyan to build the consumer assistant Pi, backed by Inflection-1, Inflection-2, and Inflection-2.5 foundation models. In March 2024 Microsoft licensed Inflection's technology for roughly $650M and hired most of the founding team into its new AI division, after which Inflection pivoted to an enterprise AI lab under CEO Sean White. Today the company markets its Inflection-2.5 series and successors to enterprise customers through a Conversational API that integrates Inflection models into business applications. A developer portal is published at developers.inflection.ai with a dashboard, docs, API keys, playground, and usage metering.
finops:
- name: Inflection Ai Finops
  service_category: API
  slug: inflection-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/inflection-ai.png
layout: provider
modified: '2026-05-23'
name: Inflection AI
nav: Providers
network: true
overview: 'Inflection AI publishes 1 API on the [APIs.io](https://apis.io/) network: Inference API. Tagged areas include AI, Foundation Models, LLM, Conversational AI, and Enterprise AI.


  Inflection AI''s developer surface includes authentication, engineering blog, and 9 more developer resources.'
plans:
- name: Inflection Ai Plans Pricing
  plan_count: 1
  slug: inflection-ai-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 2
  name: Inflection Ai Rate Limits
  slug: inflection-ai-rate-limits
score:
  band: thin
  composite: 33.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 52.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inflection-ai/refs/heads/main/screenshots/inflection-ai-2026-06-20T183333.png
security:
- kind: authentication
  name: Inflection Ai Authentication
  slug: inflection-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Inflection Ai Domain Security
  slug: inflection-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: inflection-ai
tags:
- AI
- Foundation Models
- LLM
- Conversational AI
- Enterprise AI
- Pi
- Inflection-2.5
- Inference
- Empathic AI
website: https://inflection.ai/
---
