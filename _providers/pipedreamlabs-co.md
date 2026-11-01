---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/pipedreamlabs-co/hosts/pipedreamlabs-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pipedreamlabs-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/pipedreamlabs-co/vendors/pipedreamlabs-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pipedreamlabs-co-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.pipedreamlabs.co/newsroom
- group: auth
  href: https://artifacts.apis.io/pipedreamlabs-co/security/pipedreamlabs-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pipedreamlabs-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pipedreamlabs.co/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://pipedreamlabs.co/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Pipedream Labs builds autonomous underground delivery systems that transport groceries, restaurant orders, and other consumer goods through a network of underground pipes. By leveraging high‑speed robots and portal stations, they aim to reduce delivery times to seconds, improve access in food deserts, and create a hyperlogistics infrastructure for cities. The company envisions a seamless, low‑cost logistics layer that operates beneath streets, offering fast, reliable pickup and drop‑off for restaurants, grocery stores, and urban residents.
image: http://static1.squarespace.com/static/6568c17d16068b20cfac0d81/t/6578c012bac1ed0a52eac108/1702412307058/robot_bridge_2.jpg?format=1500w
layout: provider
modified: '2026-10-24'
name: Pipedream
nav: Providers
network: true
overview: Pipedream is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Autonomous, Delivery, and UrbanTech.
random_paper: 16
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pipedreamlabs Co Domain Security
  slug: pipedreamlabs-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pipedreamlabs-co
tags:
- Company
- Logistics
- Autonomous
- Delivery
- UrbanTech
website: https://pipedreamlabs.co/
---
