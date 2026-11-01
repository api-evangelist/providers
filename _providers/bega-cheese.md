---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/bega-cheese/hosts/bega-cheese-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bega-cheese-hosts.yml
- group: auth
  href: https://artifacts.apis.io/bega-cheese/security/bega-cheese-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bega-cheese-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.begacheese.com.au/
created: '2026-10-21'
description: 'Bega Cheese Limited (ASX: BGA) is an Australian food company headquartered at 23-45 Ridge St, North Bega, New South Wales, with roots in the Bega Co-operative Creamery Company formed by local dairy farmers in 1899. It receives, processes, manufactures and distributes dairy and other food products through Branded and Bulk segments, with brands including Bega, Vegemite, Bega Peanut Butter, Dairy Farmers, Big M, Dare Iced Coffee and Zooper Dooper. No public developer API or developer portal was found during profiling.'
layout: provider
modified: '2026-10-21'
name: Bega Cheese
nav: Providers
network: true
overview: Bega Cheese is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Dairy, Consumer Goods, and Manufacturing.
plans:
- name: Bega Cheese Plans Pricing
  plan_count: 0
  slug: bega-cheese-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Bega Cheese Rate Limits
  slug: bega-cheese-rate-limits
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 3.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bega Cheese Domain Security
  slug: bega-cheese-domain-security
  summary_line: DMARC
slug: bega-cheese
tags:
- Company
- Food
- Dairy
- Consumer Goods
- Manufacturing
- Australia
- ASX Listed
website: https://www.begacheese.com.au/
---
