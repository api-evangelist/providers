---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Annual comprehensive blood testing across 100+ biomarkers in 21 categories (hormones, longevity, immune, inflammation, nutrients, toxins) collected via Quest Diagnostics locations or at-home phlebotom
  name: Superpower Biomarker Testing
  slug: superpower-health-biomarker-testing
- description: Result interpretation surfaced as 17 health scores plus a biological age calculation derived from measured biomarkers and computed ratios/indices. Exposed only inside the member app; no documented pub
  name: Superpower Results & Health Scores
  slug: superpower-health-results-scores
- description: SuperpowerAI chat assistant that lets members explore their lab data and protocols with clinical context. A consumer feature only; no public chat or completion API is documented.
  name: Superpower AI Health Chat
  slug: superpower-health-ai-chat
- description: Personalized diet, lifestyle, and supplement action plans generated from a member's biomarkers and goals. In-app only; no documented public API for retrieving or managing plans.
  name: Superpower Action Plans
  slug: superpower-health-action-plans
- description: Inbound sync of wearable and health-app data (Oura, Whoop, Apple Health) plus uploaded past lab results and medical records. Superpower is reported to use the third-party Vital aggregator to ingest th
  name: Superpower Wearable & Records Sync
  slug: superpower-health-wearable-sync
artifact_total: 10
collections:
- collection_type: open
  name: Superpower
  slug: open-superpower-health
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superpower-health-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.superpower.com/blog
created: '2026-06-20'
description: Superpower is a consumer preventive-health and longevity membership that provides an annual comprehensive blood draw across 100+ biomarkers, AI-driven result interpretation, biological age scoring, personalized action plans, and a care team, delivered through web and mobile apps. As of the catalog date Superpower does not publish a public or partner developer API; this catalog documents the product surface honestly rather than fabricating endpoints.
finops:
- name: Superpower Health Finops
  service_category: Healthcare
  slug: superpower-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/superpower-health.png
layout: provider
modified: '2026-06-20'
name: Superpower
nav: Providers
network: true
overview: 'Superpower publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Biomarker Testing, Results & Health Scores, AI Health Chat, and 2 more. Tagged areas include Health, Longevity, Lab Testing, Biomarkers, and Preventive Health.


  Superpower''s developer surface includes engineering blog and 1 more developer resources.'
plans:
- name: Superpower Health Plans Pricing
  plan_count: 2
  slug: superpower-health-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Superpower Health Rate Limits
  slug: superpower-health-rate-limits
score:
  band: emerging
  composite: 21.9
  delta: -4.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 32.3
    developer_ergonomics: 2.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 26.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/superpower-health/refs/heads/main/screenshots/superpower-health-2026-06-20T194727.png
security:
- kind: domain-security
  name: Superpower Health Domain Security
  slug: superpower-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: superpower-health
tags:
- Health
- Longevity
- Lab Testing
- Biomarkers
- Preventive Health
- Consumer Health
- No Public API
---
