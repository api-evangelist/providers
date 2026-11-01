---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/ankiweb/vendors/ankiweb-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ankiweb-vendors.yml
- group: agent
  href: https://artifacts.apis.io/ankiweb/llms/ankiweb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ankiweb-llms.txt
- group: other
  href: https://artifacts.apis.io/ankiweb/a2a/ankiweb-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ankiweb-a2a.yml
- group: agent
  href: https://artifacts.apis.io/ankiweb/well-known/ankiweb-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ankiweb-well-known.yml
- group: other
  href: https://artifacts.apis.io/ankiweb/hosts/ankiweb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ankiweb-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ankiweb.net/releases/betas/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ankiweb.net/manual/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ankiweb.net/
- group: auth
  href: https://artifacts.apis.io/ankiweb/security/ankiweb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ankiweb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ankiweb.net/
coverage:
  checked: '2026-10-28'
  detail: Docs site returns only a JavaScript shell with no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://docs.ankiweb.net/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: 'AnkiWeb (Ankitects) is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-28'
name: AnkiWeb (Ankitects)
nav: Providers
network: true
overview: 'AnkiWeb (Ankitects) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  AnkiWeb (Ankitects)''s developer surface includes changelog, getting-started guide, documentation, and 7 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 26.8
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ankiweb Domain Security
  slug: ankiweb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ankiweb
tags:
- Company
website: https://ankiweb.net/
---
