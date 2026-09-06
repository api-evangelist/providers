---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://getturnstyle.com'', ''status'': 301, ''note'': ''declared website redirects to https://business.yelp.com/ — a different registrable domain (getturnstyle.com -> yelp.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
artifact_total: 0
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/yelp/
- group: company
  title: ''
  type: Website
  url: https://getturnstyle.com
created: '2026-07-17'
description: Turnstyle (Turnstyle Analytics) was a WiFi-marketing and customer-analytics platform for brick-and-mortar businesses, capturing guest WiFi logins to build customer profiles, segments, and automated re-marketing campaigns. It was a 500 Global portfolio company and was acquired by Yelp, becoming Yelp WiFi. As of this enrichment pass the product no longer operates independently - its domain getturnstyle.com now permanently redirects through app.yelpwifi.com to business.yelp.com (Yelp for Business). No standalone Turnstyle developer portal, API, documentation, or SDKs are published; there is no independent API surface to enrich.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/turnstyle.png
layout: provider
modified: '2026-07-21'
name: Turnstyle
nav: Providers
network: true
overview: Turnstyle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, WiFi Marketing, Customer Analytics, Location Marketing, and Acquired.
random_paper: 10
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/turnstyle/refs/heads/main/screenshots/turnstyle-2026-09-02T164547.png
slug: turnstyle
tags:
- Company
- WiFi Marketing
- Customer Analytics
- Location Marketing
- Acquired
- Yelp
website: https://getturnstyle.com
---
