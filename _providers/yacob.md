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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://yacob.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yacob-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yacob-llms.txt
created: '2026-07-17'
description: Yacob was a Dubai-based Intelligent Nutrition platform and 500 Global portfolio company that combined cashless school-meal payments with nutrition monitoring. Pupils paid for school meals with a stored-value card while parents topped up accounts online, tracked transactions in real time, set spend and food limits, flagged allergies, and reviewed the nutritional value of their children's meals. The company appears dormant, with yacob.com no longer resolving as of 2026, and no public API surface was ever found.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yacob.png
layout: provider
modified: '2026-07-21'
name: Yacob
nav: Providers
network: true
overview: Yacob is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nutrition, Education, Payments, and Cashless Payments.
random_paper: 1
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yacob/refs/heads/main/screenshots/yacob-2026-09-02T171216.png
security:
- kind: domain-security
  name: Yacob Domain Security
  slug: yacob-domain-security
  summary_line: no transport/DNS hardening detected
slug: yacob
tags:
- Company
- Nutrition
- Education
- Payments
- Cashless Payments
- Schools
- Parenting
- United Arab Emirates
website: https://yacob.com
---
