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
  href: https://raw.githubusercontent.com/api-evangelist/bgl-group/refs/heads/main/hosts/bgl-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bgl-group-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bgl-group/refs/heads/main/security/bgl-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bgl-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bglgroup.com/
coverage:
  checked: '2026-09-28'
  detail: The BGL Group website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://bglgroup.com
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: BGL Group provides business intelligence, consulting, and technology services, delivering data-driven solutions for over 20 years. Their offerings include staff augmentation, project management, infrastructure deployment, and application development, serving a diverse client base across various industries.
layout: provider
modified: '2026-09-28'
name: BGL Group
nav: Providers
network: true
overview: BGL Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Intelligence, Consulting, Technology Services, and Data Analytics.
random_paper: 9
score:
  band: minimal
  composite: 3.0
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
  name: Bgl Group Domain Security
  slug: bgl-group-domain-security
  summary_line: TLSv1.3
slug: bgl-group
tags:
- Company
- Business Intelligence
- Consulting
- Technology Services
- Data Analytics
website: https://bglgroup.com/
---
