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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/fantlab/hosts/fantlab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fantlab-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fantlab.ru/terms
- group: company
  title: ''
  type: Newsroom
  url: https://fantlab.ru/news
- group: company
  title: ''
  type: Blog
  url: https://fantlab.ru/user17299/blog
- group: auth
  href: https://artifacts.apis.io/fantlab/security/fantlab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fantlab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fantlab.ru/
coverage:
  checked: '2026-10-28'
  detail: The FantLab website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://fantlab.ru
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: FantLab is a Russian online community and database dedicated to science fiction and fantasy literature. It aggregates extensive information on books, authors, series, and characters, providing reviews, ratings, and user discussions. The platform offers a searchable catalog, personalized reading lists, and various statistics for enthusiasts and researchers.
image: https://fantlab.ru/img/logo2.png
layout: provider
modified: '2026-10-28'
name: FantLab
nav: Providers
network: true
overview: 'FantLab is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Community, Literature, Science-Fiction, and Fantasy.


  FantLab''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - russia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fantlab Domain Security
  slug: fantlab-domain-security
  summary_line: TLSv1.2 · HSTS
slug: fantlab
tags:
- Company
- Community
- Literature
- Science-Fiction
- Fantasy
website: https://fantlab.ru/
---
