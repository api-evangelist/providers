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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Real's platform, as documented on the website.
  name: Real API
  slug: real-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/join-real-com/well-known/join-real-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/join-real-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/join-real-com/hosts/join-real-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/join-real-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/join-real-com/vendors/join-real-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/join-real-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/join-real-com/security/join-real-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/join-real-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://joinreal.com/
created: '2026-10-29'
description: Real is a real estate experience company working to simplify complex transactions for agents, home buyers, and sellers. It offers platforms for buying, selling, and renting homes, with divisions for luxury properties, military families, and mortgage services. The company emphasizes technology-driven tools for agents and integrates various real estate services under a unified brand.
image: https://joinreal.com/wp-content/uploads/sites/11/2026/09/join-real-graph.png
layout: provider
modified: '2026-10-29'
name: Real
nav: Providers
network: true
overview: Real is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Banking, Payments, and API.
random_paper: 13
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 9.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Join Real Com Domain Security
  slug: join-real-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: join-real-com
tags:
- Company
- Fintech
- Banking
- Payments
- API
website: https://joinreal.com/
---
