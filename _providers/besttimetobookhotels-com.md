---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Besttimetobookhotels Com Agentic Access
  operation_count: 5
  slug: besttimetobookhotels-com-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: Read-only public API providing hotel booking timing data and last‑minute deals.
  name: Best Time To Book Hotels API
  slug: best-time-to-book-hotels-api
- baseURL: https://www.besttimetobookhotels.com
  baseurl_source: declared
  description: When to book, from observed prices.
  name: Best Time To Book Hotels Booking Timing API
  slug: besttimetobookhotels-com-booking-timing-api
- baseURL: https://www.besttimetobookhotels.com
  baseurl_source: declared
  description: Agent-readable Markdown for public pages.
  name: Best Time To Book Hotels Content API
  slug: besttimetobookhotels-com-content-api
- baseURL: https://www.besttimetobookhotels.com
  baseurl_source: declared
  description: Last-minute deal price history.
  name: Best Time To Book Hotels Deals API
  slug: besttimetobookhotels-com-deals-api
- baseURL: https://www.besttimetobookhotels.com
  baseurl_source: declared
  description: Service health.
  name: Best Time To Book Hotels Operations API
  slug: besttimetobookhotels-com-operations-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/besttimetobookhotels-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/besttimetobookhotels-com/conformance/besttimetobookhotels-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/besttimetobookhotels-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/besttimetobookhotels-com/llms/besttimetobookhotels-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/besttimetobookhotels-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/besttimetobookhotels-com/well-known/besttimetobookhotels-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/besttimetobookhotels-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/besttimetobookhotels-com/hosts/besttimetobookhotels-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/besttimetobookhotels-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/besttimetobookhotels-com/vendors/besttimetobookhotels-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/besttimetobookhotels-com-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.besttimetobookhotels.com/docs/api
- group: auth
  href: https://artifacts.apis.io/besttimetobookhotels-com/security/besttimetobookhotels-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/besttimetobookhotels-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://besttimetobookhotels.com/
created: '2026-11-02'
description: Best Time To Book Hotels provides a platform that aggregates daily median hotel prices across major cities worldwide, helping travelers identify the cheapest dates to book. By comparing historical pricing data, the service offers insights into price trends, seasonal variations, and optimal booking windows, enabling users to save money and plan trips more efficiently. The site supports multiple languages and currencies, and integrates with popular travel partners to deliver up-to-date pricing information and last‑minute deals.
json_schemas:
- name: BookingAdvice
  property_count: 14
  slug: besttimetobookhotels-com-booking-advice
- name: DealHistorySeries
  property_count: 7
  slug: besttimetobookhotels-com-deal-history-series
- name: Health
  property_count: 4
  slug: besttimetobookhotels-com-health
- name: LeadTimeRecord
  property_count: 9
  slug: besttimetobookhotels-com-lead-time-record
- name: LeadTimeSuggestion
  property_count: 4
  slug: besttimetobookhotels-com-lead-time-suggestion
jsonld:
- class_count: 7
  name: Besttimetobookhotels Com Context
  property_count: 35
  slug: besttimetobookhotels-com-context
layout: provider
modified: '2026-11-02'
name: Best Time To Book Hotels
nav: Providers
network: true
overview: 'Best Time To Book Hotels publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Booking Timing API, Content API, Deals API, and 2 more. Tagged areas include Travel, Hotels, Pricing, Data, and Multilingual.


  The Best Time To Book Hotels catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Best Time To Book Hotels'' developer surface includes API reference and 8 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 1
  name: Besttimetobookhotels Com Rate Limits
  slug: besttimetobookhotels-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Best Time To Book Hotels API Rules
  rule_count: 56
  severity_counts:
    error: 52
    hint: 0
    info: 3
    warn: 1
  slug: besttimetobookhotels-com-rules
scopes:
- name: Besttimetobookhotels Com Scopes
  scope_count: 0
  slug: besttimetobookhotels-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 58.5
    catalog_earned_first_party: 8.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 56.9
    developer_ergonomics: 5.4
    discoverability: 62.5
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Besttimetobookhotels Com Authentication
  slug: besttimetobookhotels-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Besttimetobookhotels Com Domain Security
  slug: besttimetobookhotels-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: hotel-booking-timing
  slug: besttimetobookhotels-com-hotel-booking-timing
slug: besttimetobookhotels-com
tags:
- Travel
- Hotels
- Pricing
- Data
- Multilingual
website: https://besttimetobookhotels.com/
---
