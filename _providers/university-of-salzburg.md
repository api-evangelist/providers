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
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/university-of-salzburg/well-known/university-of-salzburg-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/university-of-salzburg-security.txt
- group: agent
  href: https://artifacts.apis.io/university-of-salzburg/well-known/university-of-salzburg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/university-of-salzburg-well-known.yml
- group: other
  href: https://artifacts.apis.io/university-of-salzburg/hosts/university-of-salzburg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/university-of-salzburg-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ZGIS
- group: auth
  href: https://artifacts.apis.io/university-of-salzburg/security/university-of-salzburg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/university-of-salzburg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.plus.ac.at
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.zgis.at
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: The University of Salzburg is a public university in Austria, offering a wide range of academic programs across six faculties, including natural sciences, humanities, law, and business. It conducts extensive research, provides extensive student services, and engages in international collaborations. The university’s website (plus.ac.at) presents information about study programs, research initiatives, campus life, and support services, reflecting its role as a major educational and research institution in the region.
image: https://www.plus.ac.at/wp-content/uploads/2022/12/logo-quadrat.jpg
layout: provider
modified: '2026-10-28'
name: University of Salzburg
nav: Providers
network: true
overview: University of Salzburg is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Research, Austria, and University.
random_paper: 19
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 15.8
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
  name: University Of Salzburg Domain Security
  slug: university-of-salzburg-domain-security
  summary_line: TLSv1.3
slug: university-of-salzburg
tags:
- Company
- Education
- Research
- Austria
- University
website: https://www.plus.ac.at
---
