---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/bestwestern-fr/hosts/bestwestern-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bestwestern-fr-hosts.yml
- group: other
  href: https://artifacts.apis.io/bestwestern-fr/vendors/bestwestern-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bestwestern-fr-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bestwestern-fr/security/bestwestern-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bestwestern-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bestwestern.fr/
coverage:
  checked: '2026-11-02'
  detail: No public API documentation or developer program was found; only a Plesk login page appears.
  evidence:
  - status: 200
    url: https://api.bestwestern.fr/login_up.php
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: Best Western France is a leading hospitality brand offering online hotel reservations across France and worldwide. With over 4,000 hotels, the group provides unique local experiences, loyalty programs, and tailored travel solutions for leisure and business travelers. The website showcases promotions, destination guides, and a rewards program, reflecting a modern, customer‑focused approach to accommodation services.
layout: provider
modified: '2026-11-02'
name: Best Western France
nav: Providers
network: true
overview: Best Western France is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Hospitality, Hotels, Travel, Reservations, and Loyalty.
random_paper: 3
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 6
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
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bestwestern Fr Domain Security
  slug: bestwestern-fr-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bestwestern-fr
tags:
- Hospitality
- Hotels
- Travel
- Reservations
- Loyalty
website: https://bestwestern.fr/
---
