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
  href: https://artifacts.apis.io/west-university-of-timisoara/hosts/west-university-of-timisoara-hosts.yml
  title: ''
  type: Hosts
  url: hosts/west-university-of-timisoara-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.uvt.ro/
- group: auth
  href: https://artifacts.apis.io/west-university-of-timisoara/security/west-university-of-timisoara-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/west-university-of-timisoara-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.uvt.ro/
coverage:
  checked: '2026-10-24'
  detail: The university website redirects and serves only HTML with no machine‑readable API specifications.
  evidence:
  - status: 301
    url: https://uvt.ro/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: West University of Timisoara (UVT) is a public university located in Timișoara, Romania, offering a wide range of undergraduate, graduate, and doctoral programs across faculties such as Engineering, Sciences, Arts, and Social Sciences. Established in 1962, UVT focuses on research, innovation, and community engagement, fostering international collaborations and providing modern facilities for students and staff. The institution actively publishes data, APIs, and digital services to support education, research, and public information.
image: https://uvt.ro/wp-content/uploads/2020/10/UVT-2-2.jpg
layout: provider
modified: '2026-10-23'
name: West University of Timisoara
nav: Providers
network: true
overview: 'West University of Timisoara is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, University, Romania, Research, and Public.


  West University of Timisoara''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: West University Of Timisoara Domain Security
  slug: west-university-of-timisoara-domain-security
  summary_line: TLSv1.3
slug: west-university-of-timisoara
tags:
- Education
- University
- Romania
- Research
- Public
website: http://www.uvt.ro/
---
