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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The 42Q Manufacturing Execution System API provides programmatic integration with Sanmina's cloud-based MES platform. The API enables enterprise system integration with ERP (SAP, Oracle), PLM, WMS, an
  name: 42Q MES API
  slug: sanmina-42q-mes-api
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sanmina/refs/heads/main/plans/sanmina-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sanmina-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sanmina/refs/heads/main/rate-limits/sanmina-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sanmina-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sanmina/refs/heads/main/finops/sanmina-finops.yml
  title: ''
  type: FinOps
  url: finops/sanmina-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sanmina/refs/heads/main/security/sanmina-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sanmina-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sanmina
- group: company
  title: ''
  type: Website
  url: https://www.sanmina.com
- group: company
  title: ''
  type: Website
  url: https://www.42-q.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.42-q.com/mes-products/
- group: operate
  title: ''
  type: Support
  url: https://support.42-q.com/
- group: other
  title: ''
  type: Case Studies
  url: https://www.sanmina.com/insights/case-studies/
- group: operate
  title: ''
  type: Press Releases
  url: https://www.sanmina.com/category/press-releases/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sanmina/refs/heads/main/vocabulary/sanmina-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sanmina-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sanmina/refs/heads/main/json-ld/sanmina-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sanmina-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://www.sanmina.com/feed/
created: '2026-05-02'
description: Sanmina Corporation is a global contract manufacturer and leading provider of end-to-end design, manufacturing, logistics, and repair solutions for OEMs across defense, industrial, medical, communications, and computing markets. Through its 42Q subsidiary, Sanmina offers a cloud-based Manufacturing Execution System (MES) with APIs for integrating with ERP, PLM, WMS, and other enterprise systems. Sanmina's 42Q MES provides real-time factory visibility, traceability, quality management, and production control across globally distributed manufacturing facilities.
finops:
- has_sources: false
  method: generated
  name: Sanmina Finops
  primary_unit: ''
  service_category: API
  slug: sanmina-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sanmina.png
jsonld:
- class_count: 0
  name: Sanmina Context
  property_count: 11
  slug: sanmina-context
layout: provider
modified: '2026-05-02'
name: Sanmina
nav: Providers
network: true
overview: 'Sanmina is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Manufacturing, Contract Manufacturing, MES, Supply Chain, and Industrial.


  The Sanmina catalog on APIs.io includes 1 JSON-LD context.


  Sanmina''s developer surface includes documentation, support, engineering blog, and 11 more developer resources.'
plans:
- name: Sanmina Plans Pricing
  plan_count: 3
  slug: sanmina-plans-pricing
press:
- date: ''
  title: AMD Partners With Sanmina for AI Solutions Manufacturing
  url: https://www.linkedin.com/posts/dylanljmartin_amd-makes-sanmina-a-top-ai-ally-after-3b-activity-7388598982773628930-unbe
- date: ''
  title: How the Story Around Sanmina Is Evolving Amid AI and ...
  url: https://finance.yahoo.com/news/story-around-sanmina-evolving-amid-011206291.html
- date: ''
  title: Dexterity and Sanmina Deepen Partnership to Scale Mech ...
  url: https://dexterity.ai/blog/dexterity-and-sanmina-deepen-partnership-to-scale-mech-superhumanoids
- date: ''
  title: SANMINA ANNOUNCES ACQUISITION OF DATA ...
  url: https://www.prnewswire.com/news-releases/sanmina-announces-acquisition-of-data-center-infrastructure-manufacturing-business-of-zt-systems-from-amd-302458905.html
- date: ''
  title: Press Releases Archives - Page 2 of 10
  url: https://www.sanmina.com/category/press-releases/page/2/
random_paper: 17
rate_limits:
- limit_count: 5
  name: Sanmina Rate Limits
  slug: sanmina-rate-limits
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 50.5
    catalog_earned_first_party: 0.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 10.7
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 16.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/sanmina/refs/heads/main/screenshots/sanmina-2026-10-11T193820.png
security:
- kind: domain-security
  name: Sanmina Domain Security
  slug: sanmina-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sanmina
tags:
- Manufacturing
- Contract Manufacturing
- MES
- Supply Chain
- Industrial
- Enterprise
- Fortune 500
website: https://www.sanmina.com
---
