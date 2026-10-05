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
  href: https://raw.githubusercontent.com/api-evangelist/akagera-medicines/refs/heads/main/hosts/akagera-medicines-hosts.yml
  title: ''
  type: Hosts
  url: hosts/akagera-medicines-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/akagera-medicines/refs/heads/main/vendors/akagera-medicines-vendors.yml
  title: ''
  type: Vendors
  url: vendors/akagera-medicines-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forgeglobal
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/akagera-medicines/refs/heads/main/security/akagera-medicines-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/akagera-medicines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.akageramedicines.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.akageramedicines.com/product-pipeline
- group: start
  title: ''
  type: GettingStarted
  url: https://www.akageramedicines.com/mission-statement
- group: operate
  title: ''
  type: Contact
  url: https://www.akageramedicines.com/contact
coverage:
  checked: '2026-10-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found at the API host.
  evidence:
  - status: 0
    url: https://api.akageramedicines.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Akagera Medicines is a Rwandan biotech company focused on developing liposomal nanotherapeutics for tuberculosis and other infectious diseases. It aims to improve vaccine delivery and drug efficacy through innovative lipid-based platforms, partnering with global health organizations and investors to advance its pipeline.
image: http://static1.squarespace.com/static/5e6142ff61a7272e784cd7c3/t/64f794b44b613b70facd7c92/1693947060937/Gold_Stacked+copy.jpg?format=1500w
layout: provider
modified: '2026-09-24'
name: Akagera Medicines
nav: Providers
network: true
overview: 'Akagera Medicines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Rwanda, Tuberculosis, and Nanomedicine.


  Akagera Medicines'' developer surface includes API reference, getting-started guide, and 6 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.9
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
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 5.3
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
  name: Akagera Medicines Domain Security
  slug: akagera-medicines-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: akagera-medicines
tags:
- Company
- Biotechnology
- Rwanda
- Tuberculosis
- Nanomedicine
website: https://www.akageramedicines.com/
---
