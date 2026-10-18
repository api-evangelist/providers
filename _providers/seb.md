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
  href: https://raw.githubusercontent.com/api-evangelist/seb/refs/heads/main/hosts/seb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seb-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seb/refs/heads/main/security/seb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://seb.se/
coverage:
  checked: '2026-10-15'
  detail: The SEB website returns HTML but no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://seb.se/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: SEB (Skandinaviska Enskilda Banken) is a leading Nordic financial services group offering banking, investment, and insurance solutions. Based in Sweden, SEB provides personal and corporate banking, loans, mortgages, savings, and digital payment services, serving customers across the region with a focus on innovation and security.
image: https://seb.se/Images/seb-wordmark-logo.png
layout: provider
modified: '2026-10-14'
name: SEB
nav: Providers
network: true
overview: SEB is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Finance, Nordic, and Payments.
random_paper: 6
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Seb Domain Security
  slug: seb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: seb
tags:
- Company
- Banking
- Finance
- Nordic
- Payments
website: https://seb.se/
---
