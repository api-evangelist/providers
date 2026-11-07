---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Messaging Api Agentic Access
  operation_count: 6
  slug: messaging-api-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Managing, sending, and receiving of messages via SMS and other channels.
  name: Messaging API Messages API
  slug: messaging-api-messages-api
artifact_total: 9
collections:
- collection_type: open
  name: Messaging API Messages API
  slug: open-messaging-api-messages-api
- collection_type: open
  name: Messaging API Messages API
  slug: open-messaging-api
common:
- group: commercial
  href: https://artifacts.apis.io/messaging-api/plans/messaging-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/messaging-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/messaging-api/rate-limits/messaging-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/messaging-api-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/messaging-api/finops/messaging-api-finops.yml
  title: ''
  type: FinOps
  url: finops/messaging-api-finops.yml
- group: agent
  href: https://artifacts.apis.io/messaging-api/agentic-access/messaging-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/messaging-api-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/messaging-api/authentication/messaging-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/messaging-api-authentication.yml
created: '2024-12-29'
description: A template and concept entry for messaging APIs. This represents the pattern and structure for messaging API implementations used in storytelling, training, and knowledge bases.
finops:
- has_sources: false
  method: generated
  name: Messaging Api Finops
  primary_unit: request
  service_category: API
  slug: messaging-api-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/messaging-api.png
layout: provider
modified: '2026-05-19'
name: Messaging API
nav: Providers
network: true
overview: 'Messaging API publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Messages API. Tagged areas include API Pattern, Messaging, and Templates.


  The Messaging API catalog on APIs.io includes 1 Spectral governance ruleset.


  Messaging API''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Messaging Api Plans Pricing
  plan_count: 3
  slug: messaging-api-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Messaging Api Rate Limits
  slug: messaging-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Messaging API API Rules
  rule_count: 64
  severity_counts:
    error: 62
    hint: 0
    info: 1
    warn: 1
  slug: messaging-api-rules
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.5
    catalog_earned_first_party: 0.0
    catalog_gap: 77.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 55.6
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 7.9
  previous_composite: 23.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Messaging Api Authentication
  slug: messaging-api-authentication
  summary_line: apiKey · 1 scheme
slug: messaging-api
tags:
- API Pattern
- Messaging
- Templates
---
