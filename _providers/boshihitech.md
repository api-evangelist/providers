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
  href: https://raw.githubusercontent.com/api-evangelist/boshihitech/refs/heads/main/hosts/boshihitech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boshihitech-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boshihitech/refs/heads/main/security/boshihitech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boshihitech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://boshihitech.com
coverage:
  checked: '2026-10-02'
  detail: No public developer program or API documentation was found for Boshihitech.
  evidence:
  - status: 0
    url: https://api.boshihitech.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-02'
description: Boshihitech (大连博世科技有限公司) is a Chinese technology company specializing in industrial automation, IoT solutions, and smart manufacturing services. Established in 2008, the firm offers a range of products including sensor integration, data analytics platforms, and cloud-based monitoring tools for factories and enterprises. Their website provides detailed information on capabilities, case studies, and partnership opportunities, reflecting a focus on advancing digital transformation in the manufacturing sector.
layout: provider
modified: '2026-10-02'
name: Boshihitech
nav: Providers
network: true
overview: Boshihitech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Automation, IoT, and Manufacturing.
random_paper: 18
score:
  band: minimal
  composite: 3.0
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boshihitech Domain Security
  slug: boshihitech-domain-security
  summary_line: no transport/DNS hardening detected
slug: boshihitech
tags:
- Company
- Technology
- Automation
- IoT
- Manufacturing
website: http://boshihitech.com
---
