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
  href: https://raw.githubusercontent.com/api-evangelist/bezahl/refs/heads/main/hosts/bezahl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bezahl-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bezahl/refs/heads/main/vendors/bezahl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bezahl-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.bezahl.de/newsroom/andere-ueber-uns
- group: company
  title: ''
  type: Blog
  url: https://www.bezahl.de/newsroom/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bezahl.de/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bezahl/refs/heads/main/security/bezahl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bezahl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bezahl.de
coverage:
  checked: '2026-09-28'
  detail: No public developer documentation or API specification was found on the website.
  evidence:
  - status: 404
    url: https://www.bezahl.de/developer
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: Bezahl provides digital payment management solutions tailored for the automotive trade. It offers a modern payment experience, digital financing, anti-money laundering prevention, and white‑label platforms for dealerships, aiming to automate financial processes and improve transparency across the automotive sector.
image: https://cdn.prod.website-files.com/655f4a8ae7674cc7cb14f8d2/65d890b9439a219bb15a524b_Open-Graph-Image.jpg
layout: provider
modified: '2026-09-28'
name: Bezahl
nav: Providers
network: true
overview: 'Bezahl is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Automotive, Payments, Digital Platform, and B2B.


  Bezahl''s developer surface includes engineering blog, documentation, and 5 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bezahl Domain Security
  slug: bezahl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bezahl
tags:
- Fintech
- Automotive
- Payments
- Digital Platform
- B2B
website: https://www.bezahl.de
---
