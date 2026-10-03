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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API documentation not publicly available
  name: Antidot API
  slug: antidot-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antidot/refs/heads/main/hosts/antidot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/antidot-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/antidot/refs/heads/main/security/antidot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/antidot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://antidot.io
coverage:
  checked: 2026-09-25
  detail: No API documentation or OpenAPI spec found at known hosts.
  evidence:
  - status: 0
    url: https://api.antidot.io/openapi.json
  reason: no-developer-program
  state: none
created: '2026-09-25'
description: Antidot is a creative studio and web development agency led by interdisciplinary designer and developer Pedro Stöhr. With over 20 years of experience in print and digital media, the studio offers services in art direction, typography, web development, and multimedia production, catering to clients seeking innovative and culturally resonant digital solutions.
layout: provider
modified: '2026-09-25'
name: Antidot
nav: Providers
network: true
overview: Antidot publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Creative, Web Development, Design, and Multimedia.
random_paper: 7
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Antidot Domain Security
  slug: antidot-domain-security
  summary_line: TLSv1.3
slug: antidot
tags:
- Company
- Creative
- Web Development
- Design
- Multimedia
website: https://antidot.io
---
