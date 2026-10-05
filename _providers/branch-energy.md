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
  href: https://raw.githubusercontent.com/api-evangelist/branch-energy/refs/heads/main/hosts/branch-energy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/branch-energy-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/branch-energy/refs/heads/main/vendors/branch-energy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/branch-energy-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/branchenergy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/branch-energy/refs/heads/main/security/branch-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/branch-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://branchenergy.com
- group: docs
  title: ''
  type: Documentation
  url: https://branchenergy.com/about-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.branchenergy.com/
- group: operate
  title: ''
  type: Support
  url: https://branchenergy.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://branchenergy.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://branchenergy.com/terms
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://branchenergy.com
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Branch Energy is a Texas‑based retail electric provider offering commercial, industrial and residential electricity plans. It pairs electricity supply with behind‑the‑meter battery storage that the company owns, operates and insures, lowering costs and providing backup power during outages. The firm also offers fixed‑rate renewable electricity plans and aims to strengthen the Texas grid through distributed storage and demand‑response services.
layout: provider
modified: '2026-10-03'
name: Branch Energy
nav: Providers
network: true
overview: 'Branch Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Electricity, Battery Storage, Texas, and Retail.


  Branch Energy''s developer surface includes documentation, support, and 8 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Branch Energy Domain Security
  slug: branch-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: branch-energy
tags:
- Energy
- Electricity
- Battery Storage
- Texas
- Retail
website: https://branchenergy.com
---
