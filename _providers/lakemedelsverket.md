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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.lakemedelsverket.se/en/security/responsible-disclosure
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lakemedelsverket/refs/heads/main/well-known/lakemedelsverket-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lakemedelsverket-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lakemedelsverket/refs/heads/main/well-known/lakemedelsverket-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lakemedelsverket-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lakemedelsverket/refs/heads/main/hosts/lakemedelsverket-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lakemedelsverket-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lakemedelsverket/refs/heads/main/vendors/lakemedelsverket-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lakemedelsverket-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lakemedelsverket/refs/heads/main/security/lakemedelsverket-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lakemedelsverket-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lakemedelsverket/refs/heads/main/security/lakemedelsverket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lakemedelsverket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lakemedelsverket.se/
coverage:
  checked: '2026-10-12'
  detail: The provider's website returns HTML but no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://www.lakemedelsverket.se/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Lakemedelsverket (Swedish Medical Products Agency) is a Swedish governmental authority responsible for promoting public and animal health concerning medicines, medical devices, and cosmetics. It oversees the regulation, approval, and monitoring of pharmaceuticals and related products to ensure safety and efficacy for the Swedish population.
image: https://www.lakemedelsverket.se/globalassets/bilder/bild-logga-1200x630.jpg
layout: provider
modified: '2026-10-12'
name: Lakemedelsverket (Swedish Medical Products Agency)
nav: Providers
network: true
overview: Lakemedelsverket (Swedish Medical Products Agency) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Health, Sweden, Pharmaceuticals, and Regulations.
random_paper: 10
score:
  band: minimal
  composite: 5.8
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
    operational_transparency: 10.5
  provenance:
    mcp: unknown
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
  name: Lakemedelsverket Domain Security
  slug: lakemedelsverket-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Lakemedelsverket Vulnerability Disclosure
  slug: lakemedelsverket-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lakemedelsverket
tags:
- Government
- Health
- Sweden
- Pharmaceuticals
- Regulations
website: https://www.lakemedelsverket.se/
---
