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
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: Access Vishay component data programmatically through the Octopart/Nexar API. Search for Vishay parts by part number or category, retrieve datasheets, specifications, pricing, and distributor inventor
  name: Vishay Parts Data via Octopart/Nexar API
  slug: vishay-parts-data-via-octopart
- description: Access Vishay component inventory, pricing, specifications, and datasheets through the DigiKey REST API. Enables integration of Vishay component data into BOM management and design tools.
  name: Vishay Parts Data via DigiKey API
  slug: vishay-parts-data-via-digikey
- description: The Vishay Parts Library (VPL) is a cross-reference resource that provides Vishay alternatives for industry reference designs, searchable by IC part number and manufacturer.
  name: Vishay Parts Library (VPL)
  slug: vishay-parts-library
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vishay-intertechnology-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vishay-intertechnology-inc-
- group: company
  title: ''
  type: Website
  url: https://www.vishay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.vishay.com/en/how/onlineliterature/online-libraries/
- group: other
  title: ''
  type: ProductCatalog
  url: https://www.vishay.com/en/product-selector/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/vishay-electronic-component-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/vishay-intertechnology-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/vishay-intertechnology-vocabulary.yml
created: '2025'
description: Vishay Intertechnology is one of the world's largest manufacturers of discrete semiconductors (diodes, rectifiers, MOSFETs, optoelectronics, selected ICs) and passive electronic components (resistors, inductors, capacitors). Vishay components are used in automotive, industrial, computing, consumer, telecommunications, military, aerospace, and medical applications. Component data is accessible via distributor APIs (Octopart/Nexar, DigiKey) and Vishay's own Parts Library (VPL) tool.
examples:
- key_count: 11
  name: Vishay Electronic Component Example
  slug: vishay-electronic-component-example
- key_count: 11
  name: Vishay Resistor Component Example
  slug: vishay-resistor-component-example
finops:
- name: Vishay Intertechnology Finops
  service_category: API
  slug: vishay-intertechnology-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vishay-intertechnology.png
json_schemas:
- name: Vishay Electronic Component
  property_count: 11
  slug: vishay-electronic-component
json_structures:
- name: Vishay Electronic Component Structure
  property_count: 0
  slug: vishay-electronic-component-structure
jsonld:
- class_count: 0
  name: Vishay Intertechnology Context
  property_count: 22
  slug: vishay-intertechnology-context
layout: provider
modified: '2026-05-03'
name: Vishay Intertechnology
nav: Providers
network: true
overview: 'Vishay Intertechnology publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Capacitors, Diodes, Electronics, and Industrial.


  The Vishay Intertechnology catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Vishay Intertechnology''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Vishay Intertechnology Plans Pricing
  plan_count: 3
  slug: vishay-intertechnology-plans-pricing
press:
- date: '2026-05-25'
  title: Vishay Intertechnology Q1 Earnings Call Highlights
  url: https://www.marketbeat.com/instant-alerts/vishay-intertechnology-q1-earnings-call-highlights-2026-05-15/
- date: '2026-05-25'
  title: AIXTRON SE's Post
  url: https://www.linkedin.com/posts/aixtron-se_newport-pressrelease-sic-activity-7188436242999508993-lOmB
- date: '2026-05-25'
  title: Vishay to acquire Nexperia's Newport, UK 200mm wafer fab
  url: https://atreg.com/vishay-to-acquire-nexperia-newport-uk-200mm-waferfab/
- date: '2026-05-25'
  title: Vishay Intertechnology, Inc. (VSH) Presents at J.P. Morgan ...
  url: https://seekingalpha.com/article/4907641-vishay-intertechnology-inc-vsh-presents-at-j-p-morgan-54th-annual-global-technology-media-and
- date: '2026-05-25'
  title: of 2020 China AI Innovation Excellence Award
  url: https://www.vishay.com/en/company/press/releases/2020/microBRICKwins2020AIAward/
random_paper: 4
rate_limits:
- limit_count: 5
  name: Vishay Intertechnology Rate Limits
  slug: vishay-intertechnology-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Vishay Intertechnology API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vishay-intertechnology-jsonschema-spectral-rules
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 60.3
    catalog_earned_first_party: 0.0
    catalog_gap: 54.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 17.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vishay-intertechnology/refs/heads/main/screenshots/vishay-intertechnology-2026-06-20T201047.png
security:
- kind: domain-security
  name: Vishay Intertechnology Domain Security
  slug: vishay-intertechnology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vishay-intertechnology
tags:
- Automotive
- Capacitors
- Diodes
- Electronics
- Industrial
- MOSFETs
- Manufacturing
- Medical
- Optoelectronics
- Passive Components
- Resistors
- Semiconductors
- Fortune 1000
website: https://www.vishay.com/
---
