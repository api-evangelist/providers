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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Consumer comparison platform pulling real-time quotes from 120+ carriers, with AI-powered declaration page scanning for policy upload and real-time price-drop alerts. No public API; carrier connectivi
  name: Insurify Consumer Marketplace
  slug: consumer-marketplace
artifact_total: 5
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
modified: '2026-07-25'
name: Insurify
nav: Providers
network: true
overview: 'Insurify publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Marketplace, Comparison, AI Agents, and Auto.


  Insurify''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Insurify Plans Pricing
  plan_count: 1
  slug: insurify-plans-pricing
random_paper: 144
rate_limits:
- limit_count: 2
  name: Insurify Rate Limits
  slug: insurify-rate-limits
score:
  band: emerging
  composite: 14.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 14.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
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
