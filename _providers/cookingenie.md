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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cookingenie/refs/heads/main/hosts/cookingenie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cookingenie-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cookingenie/refs/heads/main/vendors/cookingenie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cookingenie-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cookingenie/refs/heads/main/security/cookingenie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cookingenie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cookingenie.com/
coverage:
  checked: '2026-10-11'
  detail: Tried common OpenAPI endpoints on cookingenie.com and subdomains, all returned 404, no machine‑readable spec found.
  evidence:
  - status: 404
    url: https://cookingenie.com/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: CookinGenie is a startup that aims to simplify home cooking by providing AI‑driven recipe recommendations, meal planning tools, and grocery list automation. The platform integrates with smart kitchen appliances and offers a mobile app for personalized cooking experiences. While the company is listed in the API Evangelist harvest backlog, its public web presence is currently minimal, and no dedicated website could be located during profiling.
layout: provider
modified: '2026-10-10'
name: CookinGenie
nav: Providers
network: true
overview: CookinGenie is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cooking, Artificial Intelligence, MealPlanning, and Grocery.
random_paper: 19
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cookingenie Domain Security
  slug: cookingenie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cookingenie
tags:
- Company
- Cooking
- Artificial Intelligence
- MealPlanning
- Grocery
website: https://cookingenie.com/
---
