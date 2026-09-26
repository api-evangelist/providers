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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bloomberg-law/refs/heads/main/hosts/bloomberg-law-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bloomberg-law-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bloomberg-law/refs/heads/main/vendors/bloomberg-law-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bloomberg-law-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bloomberg-law/refs/heads/main/security/bloomberg-law-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bloomberg-law-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pro.bloomberglaw.com/
created: '2026-09-23'
description: Bloomberg Law provides a comprehensive legal research platform offering primary and secondary sources, analytics, and workflow tools for law firms, corporations, and government agencies. The service integrates news, court opinions, statutes, regulations, and proprietary Bloomberg content to support legal professionals in research, case preparation, and compliance. It aims to streamline legal workflows with advanced search, AI-driven insights, and collaboration features, positioning itself as a leading solution in the legal technology market.
layout: provider
modified: '2026-09-23'
name: Bloomberg Law
nav: Providers
network: true
overview: Bloomberg Law is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Legal Tech, Research, Analytics, Collaboration, and Artificial Intelligence.
random_paper: 2
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 4.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bloomberg Law Domain Security
  slug: bloomberg-law-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloomberg-law
tags:
- Legal Tech
- Research
- Analytics
- Collaboration
- Artificial Intelligence
website: https://pro.bloomberglaw.com/
---
