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
    mcp_server: documented
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
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Provides programmatic access to the MDBG Chinese Dictionary lookup services. Documentation is listed at the About page, but no machine‑readable contract was found.
  name: MDBG API
  slug: mdbg-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/mdbg/hosts/mdbg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mdbg-hosts.yml
- group: auth
  href: https://artifacts.apis.io/mdbg/security/mdbg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mdbg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mdbg.net/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mdbg.net/chinese/dictionary?page=about
coverage:
  checked: '2026-10-28'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other contract was found after probing common spec locations.
  evidence:
  - status: 404
    url: https://www.mdbg.net/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: MDBG Chinese Dictionary provides an online English‑to‑Chinese dictionary with Mandarin Pinyin, handwriting recognition, and example sentences. The site offers search tools, audio pronunciation, and language learning resources for students and professionals seeking to improve their Chinese proficiency. It is intended for human use, and automated scripted access is prohibited.
image: https://www.mdbg.net/logos/mdbg_500x500.png
layout: provider
modified: '2026-10-28'
name: MDBG Chinese Dictionary
nav: Providers
network: true
overview: 'MDBG Chinese Dictionary is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chinese, Dictionary, Language-Learning, and Education.


  MDBG Chinese Dictionary''s developer surface includes documentation and 3 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mdbg Domain Security
  slug: mdbg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mdbg
tags:
- Company
- Chinese
- Dictionary
- Language-Learning
- Education
website: https://www.mdbg.net/
---
