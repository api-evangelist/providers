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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazentis/refs/heads/main/llms/amazentis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amazentis-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amazentis/refs/heads/main/hosts/amazentis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amazentis-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amazentis/refs/heads/main/vendors/amazentis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amazentis-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazentis/refs/heads/main/security/amazentis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazentis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amazentis.com
coverage:
  checked: '2026-10-05'
  detail: The website provides information but no machine‑readable API specification was found after probing common spec locations.
  evidence:
  - status: 200
    url: https://www.amazentis.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Amazentis is a Swiss longevity-biotech pioneer focused on developing mitochondrial health solutions. For over 18 years, they have researched aging, discovering Urolithin A and creating Mitopure®, a proprietary, highly pure form of the molecule. Their work includes 25 human clinical trials, 100+ global patents, and extensive scientific publications, aiming to translate rigorous aging research into clinically validated cellular nutrition.
image: https://www.amazentis.com/images/og-image.jpg
layout: provider
modified: '2026-09-24'
name: Amazentis
nav: Providers
network: true
overview: Amazentis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Longevity, Health, and Research.
random_paper: 4
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 0.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amazentis Domain Security
  slug: amazentis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: amazentis
tags:
- Company
- Biotechnology
- Longevity
- Health
- Research
website: https://www.amazentis.com
---
