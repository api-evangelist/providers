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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bempower/refs/heads/main/hosts/bempower-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bempower-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bempower/refs/heads/main/security/bempower-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bempower-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bempower.org
coverage:
  checked: '2026-09-27'
  detail: The public website provides only HTML pages with no machine‑readable API specification.
  evidence:
  - status: 404
    url: https://bempower.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Bempower is a nonprofit organization focused on empowering communities in East Africa through education, water, sanitation, health, climate-smart agriculture, and livelihood initiatives. It works to improve access to clean water, education, sustainable agriculture, and health services, while promoting climate resilience and human rights.
layout: provider
modified: '2026-09-27'
name: Bempower
nav: Providers
network: true
overview: Bempower is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Non-Profit, Development, Education, Water, and Climate.
random_paper: 7
score:
  band: minimal
  composite: 2.6
  coverage:
    artifact_dirs: 5
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
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bempower Domain Security
  slug: bempower-domain-security
  summary_line: TLSv1.3
slug: bempower
tags:
- Non-Profit
- Development
- Education
- Water
- Climate
website: https://bempower.org
---
