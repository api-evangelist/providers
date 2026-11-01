---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API surface not publicly documented; no machine-readable spec found.
  name: Atomic Tessellator API
  slug: atomic-tessellator-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/atomic-tessellator/hosts/atomic-tessellator-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atomic-tessellator-hosts.yml
- group: other
  href: https://artifacts.apis.io/atomic-tessellator/vendors/atomic-tessellator-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atomic-tessellator-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atomictessellator.com/privacy
- group: other
  title: ''
  type: Leadership
  url: https://atomictessellator.com/team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AtomicTessellator
- group: auth
  href: https://artifacts.apis.io/atomic-tessellator/security/atomic-tessellator-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atomic-tessellator-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atomictessellator.com/
- group: auth
  href: https://artifacts.apis.io/atomic-tessellator/security/atomic-tessellator-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atomic-tessellator-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atomictessellator.com/
coverage:
  checked: '2026-10-29'
  detail: No machine-readable API spec found after probing known hosts.
  evidence:
  - status: 404
    url: https://api.atomictessellator.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: 'Atomic Tessellator is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by crane-venture-partners) and added to the network as a stub for full-pipeline profiling.'
image: https://atomictessellator.com/_nuxt/screenshot800.C7GtA1nS.png
layout: provider
modified: '2026-10-29'
name: Atomic Tessellator
nav: Providers
network: true
overview: Atomic Tessellator is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 12
score:
  band: minimal
  composite: 7.0
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
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: unknown
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
  name: Atomic Tessellator Domain Security
  slug: atomic-tessellator-domain-security
  summary_line: TLSv1.3 · DMARC
slug: atomic-tessellator
tags:
- Company
website: https://atomictessellator.com/
---
