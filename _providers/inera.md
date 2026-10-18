---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/inera/refs/heads/main/well-known/inera-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/inera-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/inera/refs/heads/main/hosts/inera-hosts.yml
  title: ''
  type: Hosts
  url: hosts/inera-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/inera/refs/heads/main/security/inera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.inera.se/
- group: company
  title: ''
  type: Blog
  url: https://www.inera.se/aktuellt/
- group: operate
  title: ''
  type: Support
  url: https://www.inera.se/kontakta-oss/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://kundportal.inera.se/api/mcp
  - status: 200
    url: https://www.inera.se/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Inera is a Swedish digitalization company that works on behalf of municipalities and regions to develop and maintain digital services for the welfare sector. It provides platforms such as 1177 Vårdguiden, NLL (National Patient Overview), and various digital portals for citizens, healthcare professionals, and public administrations. Inera focuses on secure, interoperable, and user‑centric solutions that enable access to health information, appointment booking, and other public services through modern web and mobile applications.
layout: provider
modified: '2026-10-12'
name: Inera
nav: Providers
network: true
overview: 'Inera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Health, Sweden, PublicSector, and Healthcare.


  Inera''s developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 5.5
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
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Inera Domain Security
  slug: inera-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: inera
tags:
- Company
- Digital Health
- Sweden
- PublicSector
- Healthcare
website: https://www.inera.se/
---
