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
  href: https://raw.githubusercontent.com/api-evangelist/banco-de-mexico/refs/heads/main/hosts/banco-de-mexico-hosts.yml
  title: ''
  type: Hosts
  url: hosts/banco-de-mexico-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.banxico.org.mx/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banco-de-mexico/refs/heads/main/security/banco-de-mexico-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/banco-de-mexico-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.banxico.org.mx
coverage:
  checked: '2026-10-14'
  detail: No machine‑readable API specification was found on the provider's site or API host.
  evidence:
  - status: 200
    url: https://www.banxico.org.mx
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Banco de México, also known as Banxico, is the central bank of Mexico. It oversees monetary policy, financial stability, and the national payment systems. The institution provides economic indicators, statistical data, and regulatory information through its public portals, supporting transparency and research for businesses, analysts, and the public.
layout: provider
modified: '2026-10-14'
name: Banco de Mexico
nav: Providers
network: true
overview: 'Banco de Mexico is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Central Bank, Mexico, Economic Data, and Payments.


  Banco de Mexico''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 2.8
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
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Banco De Mexico Domain Security
  slug: banco-de-mexico-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: banco-de-mexico
tags:
- Finance
- Central Bank
- Mexico
- Economic Data
- Payments
website: https://www.banxico.org.mx
---
