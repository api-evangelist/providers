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
- description: The MediaBeacon REST API provides programmatic access to the MediaBeacon Digital Asset Management platform, enabling integration with other products and automated data transfer between services.
  name: MediaBeacon API
  slug: mediabeacon-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mediabeacon-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mediabeacon
- group: company
  title: ''
  type: Website
  url: https://www.esko.com/en/products/mediabeacon
- group: docs
  title: ''
  type: Documentation
  url: https://www.esko.com/en/products/mediabeacon
created: '2025-03-01'
description: MediaBeacon is a Digital Asset Management (DAM) platform from Esko with a highly flexible architecture and open APIs that enable integration into many products. Its APIs support hands-off data transfer between services, reducing human intervention and enabling workflow automation.
finops:
- name: Mediabeacon Finops
  service_category: API
  slug: mediabeacon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mediabeacon.png
layout: provider
modified: '2026-07-25'
name: MediaBeacon
nav: Providers
network: true
overview: 'MediaBeacon publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include DAM, Digital Asset Management, Integration, and Media.


  MediaBeacon''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Mediabeacon Plans Pricing
  plan_count: 3
  slug: mediabeacon-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Mediabeacon Rate Limits
  slug: mediabeacon-rate-limits
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 6
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
  previous_composite: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mediabeacon/refs/heads/main/screenshots/mediabeacon-2026-06-20T185117.png
security:
- kind: domain-security
  name: Mediabeacon Domain Security
  slug: mediabeacon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mediabeacon
tags:
- DAM
- Digital Asset Management
- Integration
- Media
website: https://www.esko.com/en/products/mediabeacon
---
