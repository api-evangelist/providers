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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Developer portal for Campus Explorer providing access to college search data.
  name: Campus Explorer API
  slug: campus-explorer-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/campusexplorer/refs/heads/main/llms/campusexplorer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/campusexplorer-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/campusexplorer/refs/heads/main/hosts/campusexplorer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/campusexplorer-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/campusexplorer/refs/heads/main/vendors/campusexplorer-vendors.yml
  title: ''
  type: Vendors
  url: vendors/campusexplorer-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.campusexplorer.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/campusexplorer/refs/heads/main/security/campusexplorer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/campusexplorer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.campusexplorer.com
- group: company
  title: ''
  type: Blog
  url: https://www.campusexplorer.com/student-resources/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.campusexplorer.com/company/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.campusexplorer.com/company/legal/privacy/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.campusexplorer.com/search-online-programs/
coverage:
  checked: '2026-10-06'
  detail: Developer portal page renders via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://dev.campusexplorer.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Campusexplorer helps prospective students discover and compare online college programs across the United States. The platform aggregates information on degrees, majors, accreditation, tuition, and student outcomes, providing tools to search by location, field of study, and career goals. It aims to simplify the college selection process by offering detailed program listings, resources, and personalized recommendations for learners seeking flexible, remote education options.
image: https://www.campusexplorer.com/wp-content/uploads/2021/08/CampusExplorer_logo.png.svg
layout: provider
modified: '2026-10-06'
name: Campusexplorer
nav: Providers
network: true
overview: 'Campusexplorer is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, CollegeSearch, E-Learning, HigherEd, and StudentResources.


  Campusexplorer''s developer surface includes engineering blog, getting-started guide, and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Campusexplorer Domain Security
  slug: campusexplorer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: campusexplorer
tags:
- Education
- CollegeSearch
- E-Learning
- HigherEd
- StudentResources
website: https://www.campusexplorer.com
---
