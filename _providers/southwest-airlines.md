---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: The Southwest Airlines internal flight booking API powers the southwest.com website for searching and booking flights. It provides flight availability, pricing, schedules, and air booking shopping cap
  name: Southwest Airlines Flight API
  slug: southwest-flight-api
- description: The Rapid Rewards loyalty program API enables management of points balances, redemption, and tier status for Southwest Airlines frequent fliers.
  name: Southwest Airlines Rapid Rewards API
  slug: southwest-rapid-rewards-api
- description: The Southwest Airlines in-flight network provides a JSON API available at getconnected.southwestwifi.com/current.json while onboard the aircraft. It delivers real-time flight information including spe
  name: Southwest Airlines In-Flight Network API
  slug: southwest-inflight-api
artifact_total: 15
common:
- group: commercial
  href: https://artifacts.apis.io/southwest-airlines/plans/southwest-airlines-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/southwest-airlines-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/southwest-airlines/rate-limits/southwest-airlines-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/southwest-airlines-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/southwest-airlines/finops/southwest-airlines-finops.yml
  title: ''
  type: FinOps
  url: finops/southwest-airlines-finops.yml
- group: auth
  href: https://artifacts.apis.io/southwest-airlines/security/southwest-airlines-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/southwest-airlines-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/southwest-airlines/security/southwest-airlines-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/southwest-airlines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.southwest.com
- group: company
  title: ''
  type: Investor Relations
  url: https://ir.southwest.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SouthwestAir
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/southwest-airlines
- group: other
  title: ''
  type: X
  url: https://twitter.com/SouthwestAir
- group: other
  title: ''
  type: Open Source
  url: https://github.com/SouthwestAir/.github
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/southwest-airlines/refs/heads/main/json-ld/southwest-airlines-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/southwest-airlines/refs/heads/main/vocabulary/southwest-airlines-vocabulary.yml
created: '2026-03-21'
description: Southwest Airlines is one of the world's most profitable airlines and the largest domestic air carrier in the United States by number of passengers. The company provides scheduled air transportation in the United States and near-international markets, known for its low fares, no baggage fees policy, and customer service. Southwest Airlines is a Fortune 500 company headquartered in Dallas, Texas.
examples:
- key_count: 10
  name: Southwest Airlines Flight Example
  slug: southwest-airlines-flight-example
- key_count: 7
  name: Southwest Airlines Reservation Example
  slug: southwest-airlines-reservation-example
finops:
- has_sources: true
  method: generated
  name: Southwest Airlines Finops
  primary_unit: ''
  service_category: Travel & Distribution
  slug: southwest-airlines-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/southwest-airlines.png
json_schemas:
- name: Southwest Airlines Flight
  property_count: 12
  slug: southwest-airlines-flight
- name: Southwest Airlines Reservation
  property_count: 7
  slug: southwest-airlines-reservation
json_structures:
- name: Southwest Airlines Flight Structure
  property_count: 0
  slug: southwest-airlines-flight-structure
jsonld:
- class_count: 8
  name: Southwest Airlines Context
  property_count: 16
  slug: southwest-airlines-context
layout: provider
modified: '2026-05-02'
name: Southwest Airlines
nav: Providers
network: true
overview: 'Southwest Airlines is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Airlines, Aviation, and Travel.


  The Southwest Airlines catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Southwest Airlines Plans Pricing
  plan_count: 1
  slug: southwest-airlines-plans-pricing
press:
- date: ''
  title: Southwest Airlines has banned robots from flights, a policy ...
  url: https://www.facebook.com/KING5News/posts/southwest-airlines-has-banned-robots-from-flights-a-policy-change-that-came-afte/1452439983594853/
- date: ''
  title: Southwest Airlines Co. News and Press Releases
  url: https://www.prnewswire.com/news/southwest-airlines-co./
- date: ''
  title: Southwest Airlines recently changed their baggage policy ...
  url: https://www.facebook.com/Fox32Chicago/posts/southwest-airlines-recently-changed-their-baggage-policy-after-a-passenger-at-da/1449339787239217/
- date: ''
  title: Southwest Airlines Transforms Customer Experience with ...
  url: https://aws.amazon.com/video/watch/6d31bc3cfa4/
- date: ''
  title: Southwest uses AI to modernize management software
  url: https://www.pwc.com/us/en/library/case-studies/southwest-ai-software-update.html
random_paper: 18
rate_limits:
- limit_count: 1
  name: Southwest Airlines Rate Limits
  slug: southwest-airlines-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Southwest Airlines — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: southwest-airlines-jsonschema-spectral-rules
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 61.8
    catalog_earned_first_party: 0.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 23.5
    contract_quality: 26.7
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 20.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/southwest-airlines/southwest-airlines-2026-06-20T194230.png
security:
- kind: domain-security
  name: Southwest Airlines Domain Security
  slug: southwest-airlines-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Southwest Airlines Vulnerability Disclosure
  slug: southwest-airlines-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: southwest-airlines
tags:
- Fortune 500
- Airlines
- Aviation
- Travel
website: https://www.southwest.com
---
