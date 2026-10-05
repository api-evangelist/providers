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
api_count: 1
apis:
- description: REST API for gender probability of first names.
  name: Vornamencheck API
  slug: vornamencheck-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vornamencheck/refs/heads/main/conformance/vornamencheck-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vornamencheck-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vornamencheck/refs/heads/main/hosts/vornamencheck-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vornamencheck-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vornamencheck/refs/heads/main/security/vornamencheck-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vornamencheck-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vornamencheck.de
- group: docs
  title: ''
  type: Documentation
  url: https://vornamencheck.de/en
created: '2026-10-02'
description: Vornamencheck provides a REST API that determines the gender probability of a given first name based on the specified country. The service returns a likelihood for male or female, helping businesses clean and personalize data, suggest appropriate salutations, and automate gender-based workflows. It supports multiple languages and countries, offering a simple HTTP GET endpoint for integration into forms, databases, and applications.
layout: provider
modified: '2026-10-02'
name: Vornamencheck
nav: Providers
network: true
overview: 'Vornamencheck publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Vornamencheck''s developer surface includes documentation and 4 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Vornamencheck Domain Security
  slug: vornamencheck-domain-security
  summary_line: TLSv1.3 · HSTS
slug: vornamencheck
tags:
- Company
website: https://vornamencheck.de
---
