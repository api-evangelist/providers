---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
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
- description: The Warrior Met Coal API provides access to platform services and data for enterprise integration and automation.
  name: Warrior Met Coal API
  slug: warrior-met-coal-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/warrior-met-coal-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/warrior-met-coal-inc
- group: company
  title: ''
  type: Website
  url: https://www.warriormetcoal.com
created: '2026-04-19'
description: Warrior Met Coal is a major US corporation and Fortune 1000 company. The Warrior Met Coal API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Warrior Met Coal Finops
  service_category: Mining / Metallurgical Coal
  slug: warrior-met-coal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/warrior-met-coal.png
layout: provider
modified: '2026-04-19'
name: Warrior Met Coal
nav: Providers
network: true
overview: Warrior Met Coal publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Coal, Mining, and Steel.
plans:
- name: Warrior Met Coal Plans Pricing
  plan_count: 1
  slug: warrior-met-coal-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Warrior Met Coal Rate Limits
  slug: warrior-met-coal-rate-limits
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 6
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
screenshot: https://raw.githubusercontent.com/api-evangelist/warrior-met-coal/refs/heads/main/screenshots/warrior-met-coal-2026-06-20T201236.png
security:
- kind: domain-security
  name: Warrior Met Coal Domain Security
  slug: warrior-met-coal-domain-security
  summary_line: DNSSEC · DMARC
slug: warrior-met-coal
tags:
- Coal
- Mining
- Steel
website: https://www.warriormetcoal.com
---
