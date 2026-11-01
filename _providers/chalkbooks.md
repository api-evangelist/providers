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
  href: https://artifacts.apis.io/chalkbooks/hosts/chalkbooks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chalkbooks-hosts.yml
- group: other
  href: https://artifacts.apis.io/chalkbooks/vendors/chalkbooks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chalkbooks-vendors.yml
- group: auth
  href: https://artifacts.apis.io/chalkbooks/security/chalkbooks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chalkbooks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
created: '2026-10-08'
description: ChalkBooks is a Generative AI-powered CRM and prospect intelligence platform designed to streamline fundraising and donor engagement for independent schools. It automates time‑consuming tasks such as prospect research, donor outreach, and stewardship, enabling development teams to focus on building stronger relationships. Founded in 2021 and based in Palo Alto, CA, ChalkBooks serves top schools like Phillips Exeter Academy.
layout: provider
modified: '2026-10-08'
name: ChalkBooks
nav: Providers
network: true
overview: ChalkBooks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, CRM, Fundraising, Education, and Generative AI.
random_paper: 1
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 2.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chalkbooks Domain Security
  slug: chalkbooks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chalkbooks
tags:
- Artificial Intelligence
- CRM
- Fundraising
- Education
- Generative AI
website: https://www.nasdaqprivatemarket.com/
---
