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
    agent_card: flavored
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
  score: 1.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Australasian government reference data API providing free and paid endpoints for tax, rates, and other official data.
  name: ausref
  slug: ausref
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/ausref-dev/llms/ausref-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ausref-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/ausref-dev/a2a/ausref-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ausref-dev-a2a.yml
- group: auth
  href: https://artifacts.apis.io/ausref-dev/well-known/ausref-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ausref-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/ausref-dev/well-known/ausref-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ausref-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/ausref-dev/hosts/ausref-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ausref-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/ausref-dev/vendors/ausref-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ausref-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ausref-dev/security/ausref-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ausref-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ausref.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://ausref.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://ausref.dev/pricing
- group: docs
  title: ''
  type: OpenAPI
  url: https://ausref.dev/openapi.json
- group: agent
  title: ''
  type: LLMS
  url: https://ausref.dev/llms.txt
created: '2026-11-02'
description: Ausref provides Australasian government reference data, offering every value cited to its official source with effective dates and last‑verified timestamps. The service includes free public‑holiday calendars, country catalogs, change logs, and re‑verification windows, all accessible via simple GET endpoints without requiring an API key. Paid endpoints are available via X‑402 challenges, with transparent pricing detailed on the site. This platform aggregates data across multiple regional brands, ensuring comprehensive coverage for Australia and its neighboring regions.
layout: provider
modified: '2026-11-02'
name: ausref
nav: Providers
network: true
overview: 'ausref is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Government, Australia, and Reference.


  ausref''s developer surface includes documentation, pricing, and 10 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 53.6
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ausref Dev Domain Security
  slug: ausref-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: ausref-dev
tags:
- Data
- Government
- Australia
- Reference
website: https://ausref.dev/
---
