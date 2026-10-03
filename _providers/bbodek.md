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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bbodek/refs/heads/main/well-known/bbodek-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bbodek-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bbodek/refs/heads/main/hosts/bbodek-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bbodek-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bbodek/refs/heads/main/vendors/bbodek-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bbodek-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.bbodek.com/News
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bbodek/refs/heads/main/security/bbodek-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bbodek-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bbodek.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.bbodek.com/About
- group: company
  title: ''
  type: Blog
  url: https://blog.naver.com/bbodek_official
- group: operate
  title: ''
  type: Support
  url: https://www.bbodek.com/FAQ
coverage:
  checked: '2026-09-27'
  detail: The provider's documentation pages (e.g., https://www.bbodek.com/About) contain only HTML without any published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.bbodek.com/About
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Bbodek provides dish‑washing‑free solutions through a large‑scale dishware rental and cleaning service. As Korea’s leading provider, it offers automated cleaning, delivery, and collection of plates and utensils for businesses and institutions. The company emphasizes hygiene, convenience, and cost‑effectiveness, serving over 2,000 client companies with smart‑factory technology and a focus on clean, convenient, and cost‑effective services.
image: https://cdn.imweb.me/upload/S202205266171e99f7fcc2/8a283d9e4746f.png
layout: provider
modified: '2026-09-27'
name: Bbodek
nav: Providers
network: true
overview: 'Bbodek is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Dishware, Rentals, Cleaning, and South Korea.


  Bbodek''s developer surface includes documentation, engineering blog, support, and 6 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 6.9
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
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bbodek Domain Security
  slug: bbodek-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bbodek
tags:
- Company
- Dishware
- Rentals
- Cleaning
- South Korea
- B2B
website: https://www.bbodek.com
---
