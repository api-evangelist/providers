---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
api_count: 1
apis:
- description: The Petco Animal Supplies API provides access to platform services and data for enterprise integration and automation.
  name: Petco Animal Supplies API
  slug: petco-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/petco-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/petco-animal-supplies-inc-
- group: company
  title: ''
  type: Website
  url: https://www.petco.com
created: '2026-04-19'
description: Petco Animal Supplies is a major US corporation and Fortune 1000 company. The Petco Animal Supplies API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Petco Finops
  service_category: B2B Integration
  slug: petco-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/petco.png
layout: provider
modified: '2026-04-19'
name: Petco Animal Supplies
nav: Providers
network: true
overview: Petco Animal Supplies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Pet Care, Retail, and Veterinary.
plans:
- name: Petco Plans Pricing
  plan_count: 1
  slug: petco-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Petco Rate Limits
  slug: petco-rate-limits
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Petco Domain Security
  slug: petco-domain-security
  summary_line: TLSv1.3 · DMARC
slug: petco
tags:
- Pet Care
- Retail
- Veterinary
website: https://www.petco.com
---
