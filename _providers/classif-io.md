---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The Fashion Style Classification API detects and categorizes clothing items from images, including shirts, pants, dresses, and accessories, and produces stylistic labels suitable for personal styling,
  name: Classif.io Fashion Style Classification API
  slug: fashion-style-classification-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.classif.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.classif.io/fashion-style-classification-api/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/classif-io-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/classif-io-rules.yml
created: '2025-03-01'
description: Classif.io provides machine-learning-powered classification APIs that identify and label visual content. The flagship offering is a Fashion Style Classification API that detects clothing items, categorizes shirts, pants, dresses, and accessories from images, and supports outfit recommendation, retail product matching, virtual fitting room, social media tagging, and e-commerce styling use cases. APIs are delivered as REST endpoints and authenticated with API keys.
finops:
- name: Classif Io Finops
  service_category: API
  slug: classif-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/classif-io.png
jsonld:
- class_count: 13
  name: Classif Io Context
  property_count: 0
  slug: classif-io-context
layout: provider
modified: '2026-04-23'
name: Classif.io
nav: Providers
network: true
overview: 'Classif.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Apparel, Classification, Computer-Vision, Fashion, and Image Recognition.


  The Classif.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Classif.io''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Classif Io Plans Pricing
  plan_count: 3
  slug: classif-io-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Classif Io Rate Limits
  slug: classif-io-rate-limits
rules:
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Classif.io API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: classif-io-rules
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 45.5
    contract_quality: 10.7
    developer_ergonomics: 4.8
    discoverability: 59.3
    governance: 45.5
    operational_transparency: 7.9
  previous_composite: 19.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
slug: classif-io
tags:
- Apparel
- Classification
- Computer-Vision
- Fashion
- Image Recognition
- Machine-Learning
- Recommendation
website: https://www.classif.io/
---
