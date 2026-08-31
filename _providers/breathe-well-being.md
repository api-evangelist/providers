---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/breathe-well-being-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.breathewellbeing.in/
created: '2026-07-17'
description: 'Breathe Well-being is an India-based digital therapeutics and chronic-care company focused on Type 2 diabetes reversal and management. Through a mobile app (Android/iOS) it pairs continuous health coaching, personalized nutrition and lifestyle plans, medical supervision, and progress tracking to help members reduce blood sugar, lose weight, and lower medication dependence. Founded by Aditya Kaicker and Rohan Verma, the company is backed by Accel and Y Combinator (Series A, 2021). It operates as a direct-to-consumer health program rather than an API provider: as of this enrichment pass it publishes no public developer portal, API documentation, OpenAPI specification, SDKs, or /.well-known discovery surface (paths return the SPA lander fallback). This profile captures the company identity and its probed domain-security posture.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/breathe-well-being.png
layout: provider
modified: '2026-07-18'
name: Breathe Well-being
nav: Providers
network: true
overview: Breathe Well-being is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Digital Therapeutics, Diabetes, and Chronic Care.
random_paper: 10
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/breathe-well-being/refs/heads/main/screenshots/breathe-well-being-2026-07-25T203747.png
security:
- kind: domain-security
  name: Breathe Well Being Domain Security
  slug: breathe-well-being-domain-security
  summary_line: TLSv1.3 · DMARC
slug: breathe-well-being
tags:
- Company
- Healthcare
- Digital Therapeutics
- Diabetes
- Chronic Care
- Wellness
- Mobile App
- India
website: https://www.breathewellbeing.in/
---
