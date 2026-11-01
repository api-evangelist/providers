---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: unknown
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
  score: 3.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/corinex/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/corinex/hosts/corinex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/corinex-hosts.yml
- group: other
  href: https://artifacts.apis.io/corinex/vendors/corinex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/corinex-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.corinex.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.corinex.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.corinex.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.corinex.com/team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Corinex
- group: auth
  href: https://artifacts.apis.io/corinex/security/corinex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/corinex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.corinex.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.corinex.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Corinex provides broadband‑over‑power‑lines (BPL) based grid visibility and flexibility solutions. Its offerings target energy companies such as electric utilities, EV manufacturers, and EV charging providers, helping them automate electricity infrastructure and integrate low‑carbon technologies.
image: https://cdn.prod.website-files.com/62337650701b6f122d6b4d65/65974a1b88b276d54f09900f_corinex-broadband-over-power-line-homepage.webp
layout: provider
modified: '2026-10-21'
name: Corinex
nav: Providers
network: true
overview: Corinex is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Broadband over Power Lines, Grid Visibility, Grid Flexibility, Smart Grid, and Energy Utilities.
random_paper: 16
score:
  band: minimal
  composite: 9.9
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
    developer_ergonomics: 6.4
    discoverability: 51.8
    operational_transparency: 15.8
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Corinex Domain Security
  slug: corinex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: corinex
tags:
- Broadband over Power Lines
- Grid Visibility
- Grid Flexibility
- Smart Grid
- Energy Utilities
- Distributed Energy Resources
- Renewable Integration
website: https://www.corinex.com/
---
