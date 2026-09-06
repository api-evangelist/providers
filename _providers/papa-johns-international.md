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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/papa-johns-international-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.papajohns.com
- group: other
  title: ''
  type: Franchise
  url: https://franchise.papajohns.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/papajohns
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/papajohns-admin
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/papa-johns-international/refs/heads/main/plans/papa-johns-international-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/papa-johns-international/refs/heads/main/rate-limits/papa-johns-international-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/papa-johns-international/refs/heads/main/finops/papa-johns-international-finops.yml
created: '2026-04-19'
description: Papa John's International, Inc. is a major US-based quick-service pizza restaurant chain and Fortune 1000 company operating company-owned and franchised locations worldwide. Papa John's runs consumer-facing online ordering, a Papa Rewards loyalty program, and mobile apps, and integrates with third-party delivery aggregators and restaurant-technology platforms. Papa John's does NOT publish a public developer API or developer portal; its technology surface is internal, franchise-facing, and partner-only. Integrations are arranged through enterprise and franchise partner agreements.
features:
- description: Consumer-facing web and mobile ordering for pizza, sides, and beverages across company-owned and franchised locations.
  name: Online Ordering
- description: Loyalty and rewards program tracking points and offers for repeat consumer customers.
  name: Papa Rewards Loyalty
- description: Fulfillment through third-party delivery aggregators in addition to in-house drivers.
  name: Third-Party Delivery
- description: Internal and partner-only integrations across ordering, point-of-sale, loyalty, and delivery systems managed under franchise and partner agreements. No public developer API.
  name: Partner / Franchise Integration
finops:
- name: Papa Johns International Finops
  service_category: Food Service / QSR
  slug: papa-johns-international-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/papa-johns-international.png
integrations:
- description: AI-powered Smart Dispatch & Delivery Management platform unifying in-house and third-party order fulfillment across US restaurants (rollout targeted through 2027).
  name: Deliverect
- description: Third-party delivery aggregator marketplace; Papa John's was an early national pizza chain to integrate with on-demand delivery aggregators.
  name: DoorDash
- description: Third-party delivery aggregator marketplace integration.
  name: Uber Eats
- description: Third-party delivery aggregator marketplace integration.
  name: Grubhub
- description: Internal API management platform used to streamline and accelerate partner API integrations; not a public developer API surface.
  name: Kong
layout: provider
modified: '2026-06-03'
name: Papa John's International
nav: Providers
network: true
overview: Papa John's International is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Food Service, Restaurant, QSR, Pizza, and Online Ordering.
plans:
- name: Papa Johns International Plans Pricing
  plan_count: 1
  slug: papa-johns-international-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Papa Johns International Rate Limits
  slug: papa-johns-international-rate-limits
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 8.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/papa-johns-international/refs/heads/main/screenshots/papa-johns-international-2026-06-20T191345.png
security:
- kind: domain-security
  name: Papa Johns International Domain Security
  slug: papa-johns-international-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: papa-johns-international
tags:
- Food Service
- Restaurant
- QSR
- Pizza
- Online Ordering
- Delivery
website: https://www.papajohns.com
---
