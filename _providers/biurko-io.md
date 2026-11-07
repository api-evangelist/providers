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
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/biurko-io/well-known/biurko-io-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/biurko-io-app-security.txt
- group: agent
  href: https://artifacts.apis.io/biurko-io/well-known/biurko-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/biurko-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/biurko-io/hosts/biurko-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biurko-io-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://app.biurko.io/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://biurko.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://biurko.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://biurko.io/en/kb/getting-started/first-steps
- group: auth
  href: https://artifacts.apis.io/biurko-io/security/biurko-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biurko-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biurko.io/
coverage:
  checked: '2026-11-02'
  detail: Provider documentation is HTML pages without any machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract.
  evidence:
  - status: 200
    url: https://biurko.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Biurko provides online accounting services for sole proprietors and companies in Poland, offering invoicing, KSeF integration, VAT registers, JPK_V7 reporting, and advance tax calculations in one platform. It supports JDG and limited liability companies, including ZUS contributions for flat-rate taxpayers, streamlining financial compliance and bookkeeping.
image: https://biurko.io/images/og-default.jpg
layout: provider
modified: '2026-11-02'
name: Biurko
nav: Providers
network: true
overview: 'Biurko is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Software-as-a-Service, Poland, Finance, and Invoicing.


  Biurko''s developer surface includes changelog, engineering blog, getting-started guide, and 6 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - poland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biurko Io Domain Security
  slug: biurko-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biurko-io
tags:
- Accounting
- Software-as-a-Service
- Poland
- Finance
- Invoicing
website: https://biurko.io/
---
