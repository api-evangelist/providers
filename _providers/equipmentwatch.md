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
api_count: 7
apis:
- description: Foundational API providing access to EquipmentWatch's manufacturer and model database, covering the taxonomy used across the broader API suite for construction and heavy equipment.
  name: EquipmentWatch Taxonomy API
  slug: taxonomy
- description: Access to the industry's most comprehensive database of rich machine specifications for construction and heavy equipment.
  name: EquipmentWatch Specs API
  slug: specs
- description: Serial number verification API supporting approximately 30,000 models of construction and heavy equipment.
  name: EquipmentWatch Verification API
  slug: verification
- description: Ownership and operating cost recovery rates derived from the Rental Rate Blue Book, supporting equipment cost benchmarking and rate calculation.
  name: EquipmentWatch Costs API
  slug: costs
- description: Current market values and pricing data for heavy equipment, supporting valuation, appraisal, and resale pricing workflows.
  name: EquipmentWatch Values API
  slug: values
- description: National, regional, and rental-house specific equipment rental rates, supporting rate optimization for rental fleets and customers.
  name: EquipmentWatch Retail Rental API
  slug: retail-rental
- description: Raw equipment sales activity and market-derived utilization benchmarks for the heavy equipment industry.
  name: EquipmentWatch Market Data API
  slug: market-data
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/equipmentwatch-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/equipmentwatch
- group: company
  title: ''
  type: Website
  url: https://www.equipmentwatch.com/
- group: other
  title: ''
  type: APIs
  url: https://www.equipmentwatch.com/api/
- group: company
  title: ''
  type: Blog
  url: https://www.equipmentwatch.com/blog/feed/
created: '2026-03-16'
description: EquipmentWatch (a Fusable brand) provides construction and equipment data APIs that deliver rental rates, ownership costs, market values, and specifications for heavy equipment. Their data is used by contractors, equipment dealers, rental houses, and insurance professionals to make informed decisions about equipment valuation, procurement, and rental.
finops:
- name: Equipmentwatch Finops
  service_category: API
  slug: equipmentwatch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/equipmentwatch.png
layout: provider
modified: '2026-04-28'
name: Equipmentwatch
nav: Providers
network: true
overview: 'Equipmentwatch publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Equipment, Rental Rates, Valuation, and Heavy Equipment.


  Equipmentwatch''s developer surface includes engineering blog and 4 more developer resources.'
plans:
- name: Equipmentwatch Plans Pricing
  plan_count: 3
  slug: equipmentwatch-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Equipmentwatch Rate Limits
  slug: equipmentwatch-rate-limits
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/screenshots/equipmentwatch-2026-06-20T180808.png
security:
- kind: domain-security
  name: Equipmentwatch Domain Security
  slug: equipmentwatch-domain-security
  summary_line: TLSv1.3 · DMARC
slug: equipmentwatch
tags:
- Construction
- Equipment
- Rental Rates
- Valuation
- Heavy Equipment
website: https://www.equipmentwatch.com/
---
