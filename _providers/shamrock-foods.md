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
  href: https://artifacts.apis.io/shamrock-foods/hosts/shamrock-foods-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shamrock-foods-hosts.yml
- group: other
  href: https://artifacts.apis.io/shamrock-foods/vendors/shamrock-foods-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shamrock-foods-vendors.yml
- group: auth
  href: https://artifacts.apis.io/shamrock-foods/security/shamrock-foods-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shamrock-foods-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shamrockfoods.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shamrockfoodservice.com/privacy-policy/
coverage:
  checked: '2026-10-28'
  detail: No public developer program or API documentation was found on the company's website.
  evidence:
  - status: 200
    url: https://www.shamrockfoods.com/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Shamrock Foods Company is a family‑owned and operated foodservice distributor founded in 1922. It supplies a broad range of grocery, dairy, frozen, and specialty products to restaurants, schools, and institutions across the United States, emphasizing quality, service, and local community support. The company operates a modern logistics network and maintains a strong commitment to sustainability and customer satisfaction.
image: https://www.shamrockfoods.com/wp-content/uploads/2022/05/Associates-Grid.png
layout: provider
modified: '2026-10-28'
name: Shamrock Foods
nav: Providers
network: true
overview: Shamrock Foods is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Foodservice, Distributor, Dairy, and Logistics.
random_paper: 0
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Shamrock Foods Domain Security
  slug: shamrock-foods-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shamrock-foods
tags:
- Company
- Foodservice
- Distributor
- Dairy
- Logistics
website: https://shamrockfoods.com/
---
