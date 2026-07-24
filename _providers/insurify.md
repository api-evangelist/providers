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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: Consumer comparison platform pulling real-time quotes from 120+ carriers, with AI-powered declaration page scanning for policy upload and real-time price-drop alerts. No public API; carrier connectivi
  name: Insurify Consumer Marketplace
  slug: consumer-marketplace
- description: Evia (Expert Virtual Insurance Agent) is Insurify's AI agent for end-to-end insurance shopping over voice or chat. Returns bind-ready quotes in real time across 100+ carriers and tracks renewal cycles
  name: Evia AI Agent
  slug: evia-ai-agent
- description: Insurify's ChatGPT app, launched February 2026 as the first insurance app in OpenAI's app directory. Lets users browse, research, and compare car insurance directly inside ChatGPT, with full quoting h
  name: Insurify ChatGPT App
  slug: chatgpt-app
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/insurify-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/insurify
- group: company
  title: ''
  type: Website
  url: https://insurify.com/
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Insurify
- group: company
  title: ''
  type: Partnerships
  url: https://insurify.com/company/partnerships/
- group: commercial
  title: ''
  type: Plans
  url: plans/insurify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/insurify-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/insurify-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://insurify.com/sitemap-insights.xml
created: '2026-05-23'
description: Insurify is an insurance comparison marketplace licensed in all 50 U.S. states with real-time API integrations into 120+ carriers (500+ across the carrier network), covering auto, home, renters, pet, commercial auto, life, motorcycle, and travel. Consumers get side-by-side quotes in roughly two minutes and can buy online or through licensed agents. Insurify's Evia AI agent (Expert Virtual Insurance Agent) is a voice-and-chat agent that handles end-to-end shopping conversations with bind-ready quotes and renewal-cycle re-shopping. In February 2026 Insurify launched the insurance industry's first ChatGPT app via OpenAI's app library.
finops:
- name: Insurify Finops
  service_category: API
  slug: insurify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/insurify.png
layout: provider
modified: '2026-05-23'
name: Insurify
nav: Providers
network: true
overview: 'Insurify publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Marketplace, Comparison, AI Agents, and Auto.


  Insurify''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Insurify Plans Pricing
  plan_count: 1
  slug: insurify-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 2
  name: Insurify Rate Limits
  slug: insurify-rate-limits
score:
  band: emerging
  composite: 18.1
  delta: -0.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.0
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Insurify Domain Security
  slug: insurify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: insurify
tags:
- Insurance
- Marketplace
- Comparison
- AI Agents
- Auto
- Home
- Renters
- ChatGPT App
- Voice
- Carrier Integration
website: https://insurify.com/
---
