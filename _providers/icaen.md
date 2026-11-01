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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/icaen/hosts/icaen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/icaen-hosts.yml
- group: other
  href: https://artifacts.apis.io/icaen/vendors/icaen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/icaen-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://icaen.gencat.cat/ca/plans_programes/
- group: auth
  href: https://artifacts.apis.io/icaen/security/icaen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/icaen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://icaen.gencat.cat/
- group: docs
  title: ''
  type: Documentation
  url: https://icaen.gencat.cat/ca/l_icaen/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://icaen.gencat.cat/ca/l_icaen/
- group: start
  title: ''
  type: GettingStarted
  url: https://icaen.gencat.cat/ca/inici/
coverage:
  checked: '2026-10-28'
  detail: The provider’s site lists pricing but provides no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://icaen.gencat.cat/ca/plans_programes/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: The Institut Català d'Energia (ICAEN) is a public research institute based in Catalonia, Spain, dedicated to advancing energy research, innovation, and policy. It provides data, publications, and programs on renewable energy, energy efficiency, and sustainable development, supporting both regional and international initiatives. Through its campaigns, reports, and collaborations, ICAEN aims to promote a low‑carbon future and facilitate the transition to clean energy technologies across Catalonia and beyond.
image: http://icaen.gencat.cat/web/resources/fwk/comuns/img/avatar.jpg
layout: provider
modified: '2026-10-28'
name: ICAEN (Catalonia)
nav: Providers
network: true
overview: 'ICAEN (Catalonia) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Research, Public Institution, and Catalonia.


  ICAEN (Catalonia)''s developer surface includes pricing, documentation, getting-started guide, and 5 more developer resources.'
plans:
- name: Icaen Plans Pricing
  plan_count: 0
  slug: icaen-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Icaen Rate Limits
  slug: icaen-rate-limits
scopes:
- name: Icaen Scopes
  scope_count: 0
  slug: icaen-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Icaen Authentication
  slug: icaen-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Icaen Domain Security
  slug: icaen-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: icaen
tags:
- Company
- Energy
- Research
- Public Institution
- Catalonia
website: https://icaen.gencat.cat/
---
