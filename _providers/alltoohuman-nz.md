---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/alltoohuman-nz/hosts/alltoohuman-nz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alltoohuman-nz-hosts.yml
- group: other
  href: https://artifacts.apis.io/alltoohuman-nz/vendors/alltoohuman-nz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alltoohuman-nz-vendors.yml
- group: auth
  href: https://artifacts.apis.io/alltoohuman-nz/security/alltoohuman-nz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alltoohuman-nz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alltoohuman.nz/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.alltoohuman.nz/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alltoohuman.nz/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alltoohuman.nz/terms-of-service
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.alltoohuman.nz/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: All Too Human builds practical AI tools and systems for iwi, community organisations and local businesses across Aotearoa. Their technology serves communities, emphasizing data sovereignty, open-source solutions, and self‑hosted infrastructure. They offer custom AI agents, automation, reporting, and blockchain‑based records, all designed to keep data in the hands of the community.
image: https://www.alltoohuman.nz/opengraph-image?5d239ce30a4c6a71
layout: provider
modified: '2026-11-01'
name: All Too Human
nav: Providers
network: true
overview: 'All Too Human is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Community, New Zealand, Data Sovereignty, and Open Source.


  All Too Human''s developer surface includes getting-started guide and 6 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - new-zealand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 11.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alltoohuman Nz Domain Security
  slug: alltoohuman-nz-domain-security
  summary_line: TLSv1.3 · HSTS
slug: alltoohuman-nz
tags:
- Artificial Intelligence
- Community
- New Zealand
- Data Sovereignty
- Open Source
website: https://www.alltoohuman.nz/
---
