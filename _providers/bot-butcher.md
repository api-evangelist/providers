---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bot Butcher Agentic Access
  operation_count: 2
  slug: bot-butcher-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: Submit contact form data to Bot Butcher and receive a JSON classification result indicating whether the message is spam or legitimate. The AI model classifies each message within the context of your s
  name: Bot Butcher Classification API
  slug: bot-butcher-classification-api
- description: Submit and retrieve classified messages.
  name: Bot Butcher Classification API
  slug: bot-butcher-classification-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bot Butcher Classification API
  slug: open-bot-butcher-classification-api
- collection_type: open
  name: Bot Butcher Classification API
  slug: open-bot-butcher
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bot-butcher-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bot-butcher-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bot-butcher-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://botbutcher.com/
- group: docs
  title: ''
  type: Documentation
  url: https://botbutcher.com/
created: '2025-01-07'
description: Bot Butcher is an AI-powered spam detection API that uses a fine-tuned large language model to classify contact form submissions as spam or legitimate messages. The service analyzes messages within the context of what each website is about, providing context-aware classification with 99% reported accuracy. It supports multi-tenant architectures and is designed for enterprise scalability across vertical SaaS and website builder platforms.
finops:
- name: Bot Butcher Finops
  service_category: API
  slug: bot-butcher-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bot-butcher.png
layout: provider
modified: '2026-04-21'
name: Bot Butcher
nav: Providers
network: true
overview: 'Bot Butcher publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Classification API, and 1 more. Tagged areas include Bots, Spam Detection, Contact Forms, AI Classification, and Security.


  Bot Butcher''s developer surface includes authentication, documentation, and 3 more developer resources.'
plans:
- name: Bot Butcher Plans Pricing
  plan_count: 3
  slug: bot-butcher-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 5
  name: Bot Butcher Rate Limits
  slug: bot-butcher-rate-limits
score:
  band: thin
  composite: 28.0
  delta: -0.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 54.5
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 28.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bot-butcher/refs/heads/main/screenshots/bot-butcher-2026-06-20T173615.png
security:
- kind: authentication
  name: Bot Butcher Authentication
  slug: bot-butcher-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bot Butcher Domain Security
  slug: bot-butcher-domain-security
  summary_line: TLSv1.3
slug: bot-butcher
tags:
- Bots
- Spam Detection
- Contact Forms
- AI Classification
- Security
website: https://botbutcher.com/
---
