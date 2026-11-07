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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/alleskralle-com/hosts/alleskralle-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alleskralle-com-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alleskralle
- group: auth
  href: https://artifacts.apis.io/alleskralle-com/security/alleskralle-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alleskralle-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alleskralle.com/
coverage:
  checked: '2026-11-01'
  detail: AllesKralle is a job search platform with no public developer program or API.
  evidence:
  - status: 404
    url: https://www.alleskralle.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-11-01'
description: AllesKralle is a German job search platform that aggregates listings from numerous job boards and career sites, presenting all vacancies on a single searchable page. Users can filter by location, industry, and employment type to quickly find suitable positions. The service aims to simplify the job hunting process, offering a fast and easy way to discover thousands of opportunities across Germany.
image: https://cdn.alleskralle.com/images/alleskralle_anzeigenportal.png
layout: provider
modified: '2026-11-01'
name: alleskralle
nav: Providers
network: true
overview: alleskralle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Job, Job Search, Germany, Careers, and Employment.
random_paper: 16
score:
  band: minimal
  composite: 3.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 3.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
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
  name: Alleskralle Com Domain Security
  slug: alleskralle-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alleskralle-com
tags:
- Job
- Job Search
- Germany
- Careers
- Employment
website: https://www.alleskralle.com/
---
