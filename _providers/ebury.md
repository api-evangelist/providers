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
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ebury/refs/heads/main/well-known/ebury-online-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ebury-online-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ebury/refs/heads/main/well-known/ebury-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ebury-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ebury/refs/heads/main/well-known/ebury-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ebury-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ebury/refs/heads/main/llms/ebury-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ebury-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.ebury.com/
- group: operate
  title: ''
  type: Support
  url: https://help.ebury.com/en/
- group: start
  title: ''
  type: Login
  url: https://online.ebury.com/login/
- group: company
  title: ''
  type: Blog
  url: https://ebury.com/resources/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.ebury.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ebury/refs/heads/main/security/ebury-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ebury-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ebury.com/
coverage:
  checked: 2026-09-21
  detail: Developer documentation is only available as JavaScript‑rendered pages without a machine‑readable OpenAPI spec.
  evidence:
  - status: 0
    url: https://api.ebury.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-21'
description: Ebury is a global fintech providing international business accounts, multi‑currency payments, FX hedging, trade finance, and business APIs to over 25,000 businesses in more than 160 countries, supporting 140+ currencies. It helps companies manage cross‑border payments, mitigate foreign‑exchange risk, and scale globally through its digital platform.
image: https://cdn.prod.website-files.com/6911cdf6e0645000756617a4/698614febcc9cdb7dfeedd6d_Ebury%20Open%20Graph.jpg
layout: provider
modified: '2026-09-21'
name: Ebury
nav: Providers
network: true
overview: 'Ebury is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, and Internationalapis: [].


  Ebury''s developer surface includes support, engineering blog, documentation, and 8 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ebury Domain Security
  slug: ebury-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ebury
tags:
- Company
- Fintech
- Payments
- 'Internationalapis: []'
website: https://ebury.com/
---
