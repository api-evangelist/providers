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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Arcadian Infracom | Who We Are
  name: Arcadian Infracom API
  slug: arcadian-infracom-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arcadian-infracom/refs/heads/main/hosts/arcadian-infracom-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcadian-infracom-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arcadian-infracom/refs/heads/main/vendors/arcadian-infracom-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcadian-infracom-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arcadian-infracom/refs/heads/main/security/arcadian-infracom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcadian-infracom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arcadianinfra.com/
- group: docs
  title: ''
  type: Documentation
  url: https://arcadianinfra.com/about/
- group: other
  title: ''
  type: Projects
  url: https://arcadianinfra.com/projects/
- group: operate
  title: ''
  type: Contact
  url: https://arcadianinfra.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arcadianinfra.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arcadianinfra.com/terms-and-conditions/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Arcadian Infracom, founded in 2018 and headquartered in St. Louis, Missouri, builds diverse, long‑haul fiber routes to bridge the digital divide. The company develops, constructs, and operates information infrastructure, connecting major data centers and providing low‑cost backhaul to rural and tribal communities across the United States. Its mission is to lay the foundation for next‑generation digital services, supporting hyperscalers, content providers, and underserved regions.
layout: provider
modified: '2026-09-25'
name: Arcadian Infracom
nav: Providers
network: true
overview: 'Arcadian Infracom publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Infrastructure, Fiber, Broadband, Rural Connectivity, and St. Louis.


  Arcadian Infracom''s developer surface includes documentation and 8 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arcadian Infracom Domain Security
  slug: arcadian-infracom-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arcadian-infracom
tags:
- Infrastructure
- Fiber
- Broadband
- Rural Connectivity
- St. Louis
website: https://arcadianinfra.com/
---
