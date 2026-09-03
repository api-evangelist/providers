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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/digbi-health-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/digbi-health-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/digbi-health-llms.txt
- group: company
  title: ''
  type: Website
  url: https://digbihealth.com/
- group: company
  title: ''
  type: Blog
  url: https://digbihealth.com/blogs/science-talk
- group: operate
  title: ''
  type: Support
  url: https://digbihealth.com/pages/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://digbihealth.com/pages/privacy-and-accuracy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://digbihealth.com/pages/terms-conditions
- group: start
  title: ''
  type: Login
  url: https://member.digbihealth.com/login
created: '2026-07-17'
description: Digbi Health is a digital therapeutics company delivering a precision-biology virtual clinic for food-related and inflammatory illnesses — obesity, cardiometabolic disease, type 2 diabetes, digestive disorders (IBS, GERD), MSK chronic pain, PCOS, sleep and mental health. Its FoodRx program combines host-genetics and gut-microbiome testing with app-based coaching, precision nutrition, and pre/probiotic therapies, delivered to members through health plans and employers. Digbi Health is backed by Accel. The company operates a consumer-facing storefront and member app rather than a public developer API; this profile captures the public web, agent, and security surfaces observable at digbihealth.com.
image: https://digbihealth.com/cdn/shop/files/playstore_32x32.png
layout: provider
modified: '2026-07-18'
name: Digbi Health
nav: Providers
network: true
overview: 'Digbi Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Digital Therapeutics, Precision Medicine, and Genomics.


  Digbi Health''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/digbi-health/refs/heads/main/screenshots/digbi-health-2026-08-07T164337.png
security:
- kind: domain-security
  name: Digbi Health Domain Security
  slug: digbi-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: digbi-health
tags:
- Company
- Health
- Digital Therapeutics
- Precision Medicine
- Genomics
- Microbiome
- Nutrition
- Chronic Care
- Telehealth
website: https://digbihealth.com/
---
