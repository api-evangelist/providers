---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://snapfinger.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.tillster.com/ — a different registrable domain (snapfinger.com -> tillster.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snapfinger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://snapfinger.com
created: '2026-07-17'
description: Snapfinger was an online and mobile food-ordering platform that let diners browse menus and place takeout and delivery orders across a network of restaurant brands. The snapfinger.com domain now 301-redirects to Tillster, the restaurant-commerce company (ordering, kiosk, loyalty, menu, and data solutions for 40,000+ restaurants), so Snapfinger operates today as a defunct brand absorbed into Tillster. No public API, developer portal, OpenAPI specification, or SDK surface is published under the Snapfinger name. It remains in the API Evangelist network as a Norwest Venture Partners portfolio lead pending any future developer surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snapfinger.png
layout: provider
modified: '2026-07-21'
name: Snapfinger
nav: Providers
network: true
overview: Snapfinger is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant Technology, Food Ordering, Online Ordering, and Restaurant.
random_paper: 19
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/snapfinger/refs/heads/main/screenshots/snapfinger-2026-09-02T160003.png
security:
- kind: domain-security
  name: Snapfinger Domain Security
  slug: snapfinger-domain-security
  summary_line: TLSv1.3 · DMARC
slug: snapfinger
tags:
- Company
- Restaurant Technology
- Food Ordering
- Online Ordering
- Restaurant
- Takeout and Delivery
website: https://snapfinger.com
---
