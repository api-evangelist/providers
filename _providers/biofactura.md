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
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/biofactura/refs/heads/main/plans/biofactura-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/biofactura-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biofactura/refs/heads/main/hosts/biofactura-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biofactura-hosts.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.biofactura.com/pricing-tables/
- group: company
  title: ''
  type: Newsroom
  url: https://www.biofactura.com/media/
- group: other
  title: ''
  type: Leadership
  url: https://www.biofactura.com/company/management/
- group: company
  title: ''
  type: Blog
  url: https://www.biofactura.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biofactura/refs/heads/main/security/biofactura-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biofactura-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.biofactura.com/
coverage:
  checked: '2026-09-28'
  detail: BioFactura's website provides no developer program or API documentation pages.
  evidence:
  - status: 200
    url: https://www.biofactura.com/pricing-tables/
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: BioFactura is a biosimilar and biodefense biomanufacturing company developing high‑value biosimilars, biodefense medical countermeasures, and client‑selected novel drugs. It operates through its Capitol Biologics CDMO division and focuses on accelerating biologics development from concept to clinic. The company provides platforms, pipeline products, and services for the biotech industry.
layout: provider
modified: '2026-09-28'
name: BioFactura
nav: Providers
network: true
overview: 'BioFactura is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biosimilars, Biodefense, Biomanufacturing, CDMO, and Biotechnology.


  BioFactura''s developer surface includes pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Biofactura Plans Pricing
  plan_count: 4
  slug: biofactura-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biofactura Domain Security
  slug: biofactura-domain-security
  summary_line: TLSv1.3 · DMARC
slug: biofactura
tags:
- Biosimilars
- Biodefense
- Biomanufacturing
- CDMO
- Biotechnology
website: https://www.biofactura.com/
---
