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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bnovatetechnologies/refs/heads/main/llms/bnovatetechnologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bnovatetechnologies-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bnovatetechnologies/refs/heads/main/hosts/bnovatetechnologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bnovatetechnologies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bnovatetechnologies/refs/heads/main/vendors/bnovatetechnologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bnovatetechnologies-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bnovate.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.bnovate.com/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bnovatetechnologies/refs/heads/main/security/bnovatetechnologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bnovatetechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bnovate.com
coverage:
  checked: '2026-09-29'
  detail: OpenAPI spec not found at standard endpoints on api.bnovate.com (all returned 404).
  evidence:
  - status: 404
    url: https://api.bnovate.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: bNovate Technologies is a Swiss technology company specializing in real-time microbiological water monitoring. It provides automated flow cytometry solutions for continuous, rapid detection of microbial contamination in drinking water, wastewater, pharmaceutical, food & beverage, and industrial water systems, helping customers improve safety, compliance, and operational efficiency.
image: https://static.wixstatic.com/media/05f6a1_b2d5f9aa01f04b3ca8ebd5e42d185e90~mv2.jpg/v1/fill/w_1063,h_709,al_c/05f6a1_b2d5f9aa01f04b3ca8ebd5e42d185e90~mv2.jpg
layout: provider
modified: '2026-09-29'
name: Bnovatetechnologies
nav: Providers
network: true
overview: Bnovatetechnologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Water, Monitoring, Microbiology, and Automation.
random_paper: 11
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 7
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
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bnovatetechnologies Domain Security
  slug: bnovatetechnologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bnovatetechnologies
tags:
- Company
- Water
- Monitoring
- Microbiology
- Automation
website: https://www.bnovate.com
---
