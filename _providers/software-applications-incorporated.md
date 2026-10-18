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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/software-applications-incorporated/refs/heads/main/hosts/software-applications-incorporated-hosts.yml
  title: ''
  type: Hosts
  url: hosts/software-applications-incorporated-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/software-applications-incorporated/refs/heads/main/vendors/software-applications-incorporated-vendors.yml
  title: ''
  type: Vendors
  url: vendors/software-applications-incorporated-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/software-applications-incorporated/refs/heads/main/security/software-applications-incorporated-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/software-applications-incorporated-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://software.inc
coverage:
  checked: '2026-10-12'
  detail: The company website renders only a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://software.inc
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Software Applications Incorporated is an AI‑focused software startup that builds innovative applications such as the Sky natural‑language interface for macOS. Founded by former Apple engineers, it was acquired by OpenAI in 2025, expanding OpenAI’s desktop AI capabilities. The company offers a suite of automation tools for businesses and individuals, integrating deep data and application workflows.
layout: provider
modified: '2026-10-12'
name: Software Applications Incorporated
nav: Providers
network: true
overview: Software Applications Incorporated is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Startups, Automation, and macOS.
random_paper: 0
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
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Software Applications Incorporated Domain Security
  slug: software-applications-incorporated-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: software-applications-incorporated
tags:
- Company
- Artificial Intelligence
- Startups
- Automation
- macOS
website: https://software.inc
---
