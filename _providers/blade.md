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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blade/refs/heads/main/hosts/blade-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blade-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blade/refs/heads/main/vendors/blade-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blade-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://stratacritical.com/news
- group: other
  title: ''
  type: Leadership
  url: https://stratacritical.com/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blade/refs/heads/main/security/blade-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blade-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stratacritical.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://forgeglobal.com/blade_stock/
  reason: no-developer-program
  state: none
created: '2026-09-29'
description: Strata Critical Medical is a time‑critical logistics and medical services provider to the U.S. healthcare industry. It operates one of the nation’s largest air transport and surgical services networks for transplant hospitals and organ procurement organizations, offering an integrated “one‑call” solution for donor organ recovery, cardiac and perfusion services, and end‑to‑end transplant solutions on a national scale.
image: https://cdn.prod.website-files.com/688d0aef3e779c81e23e0bc2/6a7cc705093aff478393ae45_Open%20Graph%20Strata.jpg
layout: provider
modified: '2026-09-29'
name: Strata Critical Medical
nav: Providers
network: true
overview: Strata Critical Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Logistics, Transplant, Medical Services, and Air Transport.
random_paper: 20
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 5
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
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blade Domain Security
  slug: blade-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blade
tags:
- Healthcare
- Logistics
- Transplant
- Medical Services
- Air Transport
- Company
website: https://stratacritical.com/
---
