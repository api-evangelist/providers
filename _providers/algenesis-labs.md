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
api_count: 1
apis:
- description: API for Algenesis Labs' biodegradable materials platform, as described on the Technology page.
  name: Algenesis Labs API
  slug: algenesis-labs-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/algenesis-labs/refs/heads/main/hosts/algenesis-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/algenesis-labs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/algenesis-labs/refs/heads/main/vendors/algenesis-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/algenesis-labs-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.algenesislabs.com/press
- group: other
  title: ''
  type: Leadership
  url: https://www.algenesislabs.com/team/ann-king
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algenesis-labs/refs/heads/main/security/algenesis-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/algenesis-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.algenesislabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.algenesislabs.com/technology
- group: company
  title: ''
  type: About
  url: https://www.algenesislabs.com/company
- group: operate
  title: ''
  type: Support
  url: https://www.algenesislabs.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.algenesislabs.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.algenesislabs.com/privacy-policy
coverage:
  checked: '2026-10-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec was discoverable on the API host.
  evidence:
  - status: 0
    url: https://api.algenesislabs.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Algenesis Labs develops Soleic, the world’s first fully biodegradable, high‑performance polyurethane made from plant‑based polymers. Founded in 2016, the materials‑science company creates bio‑based solutions to eliminate microplastics and reduce carbon footprints across industries. Their technology is validated by peer‑reviewed studies and recognized for green chemistry innovation.
image: https://cdn.prod.website-files.com/66189f0e0003de3e87c34df2/666948659f28f43a3fb50055_Soleic-share.jpg
layout: provider
modified: '2026-09-24'
name: Algenesis Labs
nav: Providers
network: true
overview: 'Algenesis Labs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MaterialsScience, BiodegradablePolymers, GreenChemistry, and Sustainability.


  Algenesis Labs'' developer surface includes documentation, support, and 9 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.6
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 60.7
    operational_transparency: 0.0
  previous_composite: 0.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Algenesis Labs Domain Security
  slug: algenesis-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: algenesis-labs
tags:
- Company
- MaterialsScience
- BiodegradablePolymers
- GreenChemistry
- Sustainability
website: https://www.algenesislabs.com/
---
