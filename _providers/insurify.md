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
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
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
random_paper: 7
rate_limits:
- limit_count: 2
  name: Insurify Rate Limits
  slug: insurify-rate-limits
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 13.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Homes
- Renters
- ChatGPT App
- Voice
- Carrier Integration
website: https://insurify.com/
---
