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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/jawaharlal-nehru-technological-university-hyderabad/hosts/jawaharlal-nehru-technological-university-hyderabad-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jawaharlal-nehru-technological-university-hyderabad-hosts.yml
- group: auth
  href: https://artifacts.apis.io/jawaharlal-nehru-technological-university-hyderabad/security/jawaharlal-nehru-technological-university-hyderabad-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jawaharlal-nehru-technological-university-hyderabad-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jntuh.ac.in/
- group: docs
  title: ''
  type: Documentation
  url: https://jntuh.ac.in/
- group: operate
  title: ''
  type: Help
  url: https://jntuh.ac.in/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jntuh.ac.in/terms-and-conditions
coverage:
  checked: '2026-10-26'
  detail: The university website returns HTML for typical OpenAPI URLs (e.g., https://jntuh.ac.in/openapi.json) with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://jntuh.ac.in/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Jawaharlal Nehru Technological University Hyderabad (JNTUH) is a public university located in Hyderabad, India, offering a wide range of engineering, technology, and management programs. Established in 1972, it serves thousands of students and conducts extensive research, collaborations, and industry partnerships. The university provides various digital services and portals for students, faculty, and staff, reflecting its commitment to modern education and technology integration.
layout: provider
modified: '2026-10-26'
name: Jawaharlal Nehru Technological University Hyderabad
nav: Providers
network: true
overview: 'Jawaharlal Nehru Technological University Hyderabad is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, University, India, and Engineering.


  Jawaharlal Nehru Technological University Hyderabad''s developer surface includes documentation and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Jawaharlal Nehru Technological University Hyderabad Domain Security
  slug: jawaharlal-nehru-technological-university-hyderabad-domain-security
  summary_line: TLSv1.2
slug: jawaharlal-nehru-technological-university-hyderabad
tags:
- Company
- Education
- University
- India
- Engineering
website: https://jntuh.ac.in/
---
