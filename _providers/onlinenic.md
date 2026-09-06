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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: OnlineNIC offers a RESTful API with JSON format response for our partners to directly manage their products and orders. We intends to help our partners automate the purchase process and enpower them t
  name: OnlineNIC
  slug: onlinenic
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onlinenic-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onlinenic-inc-
created: '2025-02-09'
description: OnlineNIC offers a RESTful API with JSON format response for our partners to directly manage their products and orders. We intends to help our partners automate the purchase process and enpower them to provide enduser a better user experience.
finops:
- name: Onlinenic Finops
  service_category: API
  slug: onlinenic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onlinenic.png
layout: provider
modified: '2026-04-28'
name: OnlineNIC
nav: Providers
network: true
overview: OnlineNIC publishes 1 API on the [APIs.io](https://apis.io/) network.
plans:
- name: Onlinenic Plans Pricing
  plan_count: 3
  slug: onlinenic-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Onlinenic Rate Limits
  slug: onlinenic-rate-limits
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 11.1
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onlinenic/refs/heads/main/screenshots/onlinenic-2026-06-20T190720.png
security:
- kind: domain-security
  name: Onlinenic Domain Security
  slug: onlinenic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: onlinenic
---
