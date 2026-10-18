---
access_model:
  confidence: medium
  gated: private
  gated_source:
  - tag:No Public API
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://superpower.com
  baseurl_source: spec
  description: Annual comprehensive blood testing across 100+ biomarkers in 21 categories (hormones, longevity, immune, inflammation, nutrients, toxins) collected via Quest Diagnostics locations or at-home phlebotom
  name: Superpower Biomarker Testing
  provenance: unpublished
  slug: superpower-health-biomarker-testing
- baseURL: https://superpower.com
  baseurl_source: spec
  description: Result interpretation surfaced as 17 health scores plus a biological age calculation derived from measured biomarkers and computed ratios/indices. Exposed only inside the member app; no documented pub
  name: Superpower Results & Health Scores
  provenance: unpublished
  slug: superpower-health-results-scores
- baseURL: https://superpower.com
  baseurl_source: spec
  description: SuperpowerAI chat assistant that lets members explore their lab data and protocols with clinical context. A consumer feature only; no public chat or completion API is documented.
  name: Superpower AI Health Chat
  provenance: unpublished
  slug: superpower-health-ai-chat
- baseURL: https://superpower.com
  baseurl_source: spec
  description: Personalized diet, lifestyle, and supplement action plans generated from a member's biomarkers and goals. In-app only; no documented public API for retrieving or managing plans.
  name: Superpower Action Plans
  provenance: unpublished
  slug: superpower-health-action-plans
- baseURL: https://superpower.com
  baseurl_source: spec
  description: Inbound sync of wearable and health-app data (Oura, Whoop, Apple Health) plus uploaded past lab results and medical records. Superpower is reported to use the third-party Vital aggregator to ingest th
  name: Superpower Wearable & Records Sync
  provenance: unpublished
  slug: superpower-health-wearable-sync
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Superpower
  slug: open-superpower-health
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/superpower-health/refs/heads/main/plans/superpower-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/superpower-health-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/superpower-health/refs/heads/main/rate-limits/superpower-health-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/superpower-health-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/superpower-health/refs/heads/main/finops/superpower-health-finops.yml
  title: ''
  type: FinOps
  url: finops/superpower-health-finops.yml
- group: company
  title: ''
  type: Website
  url: https://superpower.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/superpower-health/refs/heads/main/security/superpower-health-domain-security.yml
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
- has_sources: true
  method: generated
  name: Superpower Health Finops
  primary_unit: ''
  service_category: Healthcare
  slug: superpower-health-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/superpower-health.png
layout: provider
modified: '2026-09-16'
name: Superpower
nav: Providers
network: true
overview: 'Superpower publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Biomarker Testing, Results & Health Scores, and AI Health Chat. Tagged areas include Health, Longevity, Lab Testing, Biomarkers, and Preventive Health.


  Superpower''s developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Superpower Health Plans Pricing
  plan_count: 2
  slug: superpower-health-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Superpower Health Rate Limits
  slug: superpower-health-rate-limits
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 25.1
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 21.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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
website: https://superpower.com
---
