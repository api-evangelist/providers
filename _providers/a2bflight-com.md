---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public documentation for a2bflight is available at the Guides page, but no machine‑readable API specification is published.
  name: a2bflight API
  slug: a2bflight-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/a2bflight-com/llms/a2bflight-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/a2bflight-com-llms.txt
- group: other
  href: https://artifacts.apis.io/a2bflight-com/hosts/a2bflight-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/a2bflight-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/a2bflight-com/vendors/a2bflight-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/a2bflight-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://a2bflight.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://a2bflight.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://a2bflight.com/guides
- group: company
  title: ''
  type: Blog
  url: https://blog.a2bflight.com/admin
- group: auth
  href: https://artifacts.apis.io/a2bflight-com/security/a2bflight-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/a2bflight-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://a2bflight.com/
coverage:
  checked: '2026-10-31'
  detail: The public Guides documentation is readable but provides no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://a2bflight.com/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: a2bflight is a flight search platform that helps individuals and groups find the cheapest flights across cities. It offers a collaborative search experience where each participant can see fares side by side, sorted by price and time. The service provides AI‑assisted assistance, route comparisons, and multi‑currency pricing. Users can explore guides, compare routes, and use an AI assistant for quick answers.
image: https://a2bflight.com/favicon.svg
layout: provider
modified: '2026-10-31'
name: a2bflight
nav: Providers
network: true
overview: 'a2bflight is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Flights, Search, Pricing, and Collaboration.


  a2bflight''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: A2Bflight Com Plans Pricing
  plan_count: 0
  slug: a2bflight-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: A2Bflight Com Rate Limits
  slug: a2bflight-com-rate-limits
scopes:
- name: A2Bflight Com Scopes
  scope_count: 0
  slug: a2bflight-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 13.6
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: A2Bflight Com Authentication
  slug: a2bflight-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: A2Bflight Com Domain Security
  slug: a2bflight-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: a2bflight-com
tags:
- Travel
- Flights
- Search
- Pricing
- Collaboration
website: https://a2bflight.com/
---
