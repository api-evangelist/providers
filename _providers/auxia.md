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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nasdaqprivatemarket.com/data-intelligence/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/auxia/refs/heads/main/plans/auxia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/auxia-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auxia/refs/heads/main/hosts/auxia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auxia-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auxia/refs/heads/main/vendors/auxia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auxia-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auxia/refs/heads/main/security/auxia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auxia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
created: '2026-09-26'
description: Auxia is an agentic marketing platform that enables enterprises to orchestrate personalized, AI‑driven customer journeys across web, mobile, and lifecycle channels. It integrates first‑party data, automates growth experiments, and continuously optimizes experiences using proprietary machine learning, helping marketers increase conversion, retention, and revenue.
layout: provider
modified: '2026-09-26'
name: Auxia
nav: Providers
network: true
overview: 'Auxia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Marketing, Artificial Intelligence, AI Agents, Customer Journey, and Enterprise.


  Auxia''s developer surface includes pricing and 5 more developer resources.'
plans:
- name: Auxia Plans Pricing
  plan_count: 3
  slug: auxia-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.5
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/auxia/refs/heads/main/screenshots/auxia-2026-10-11T101021.png
security:
- kind: domain-security
  name: Auxia Domain Security
  slug: auxia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: auxia
tags:
- Marketing
- Artificial Intelligence
- AI Agents
- Customer Journey
- Enterprise
website: https://www.nasdaqprivatemarket.com/
---
