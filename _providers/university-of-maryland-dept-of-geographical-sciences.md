---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for geospatial data and services provided by the University of Maryland Department of Geographical Sciences.
  name: Geographical Sciences API
  slug: geographical-sciences-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/university-of-maryland-dept-of-geographical-sciences/authentication/university-of-maryland-dept-of-geographical-sciences-authentication.yml
  title: ''
  type: Authentication
  url: authentication/university-of-maryland-dept-of-geographical-sciences-authentication.yml
- group: auth
  href: https://artifacts.apis.io/university-of-maryland-dept-of-geographical-sciences/well-known/university-of-maryland-dept-of-geographical-sciences-belonging-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/university-of-maryland-dept-of-geographical-sciences-belonging-security.txt
- group: agent
  href: https://artifacts.apis.io/university-of-maryland-dept-of-geographical-sciences/well-known/university-of-maryland-dept-of-geographical-sciences-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/university-of-maryland-dept-of-geographical-sciences-well-known.yml
- group: other
  href: https://artifacts.apis.io/university-of-maryland-dept-of-geographical-sciences/hosts/university-of-maryland-dept-of-geographical-sciences-hosts.yml
  title: ''
  type: Hosts
  url: hosts/university-of-maryland-dept-of-geographical-sciences-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blog.umd.edu/support-and-documentation/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://support.umd.edu/esc
- group: auth
  title: ''
  type: Security
  url: https://it.umd.edu/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.umd.edu/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://it.umd.edu/news
- group: other
  title: ''
  type: Leadership
  url: https://it.umd.edu/about-dit/leadership
- group: company
  title: ''
  type: Blog
  url: https://blog.umd.edu/
- group: start
  title: ''
  type: GettingStarted
  url: https://blog.umd.edu/support-and-documentation/quick-start/
- group: auth
  href: https://artifacts.apis.io/university-of-maryland-dept-of-geographical-sciences/security/university-of-maryland-dept-of-geographical-sciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/university-of-maryland-dept-of-geographical-sciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://geog.umd.edu
coverage:
  checked: '2026-10-29'
  detail: The provider's documentation pages contain no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract files.
  evidence:
  - status: 200
    url: https://blog.umd.edu/support-and-documentation/quick-start/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: The University of Maryland Department of Geographical Sciences focuses on research, education, and outreach in geography, GIS, remote sensing, and spatial analysis. It offers undergraduate and graduate programs, conducts interdisciplinary research on environmental change, land use, and geospatial technologies, and provides resources and collaborations for students, scholars, and partners.
image: https://geog.umd.edu/sites/geog.umd.edu/files/geog_meta.JPG
layout: provider
modified: '2026-10-28'
name: University of Maryland Dept. of Geographical Sciences
nav: Providers
network: true
overview: 'University of Maryland Dept. of Geographical Sciences is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Geography, Research, GIS, and Remote Sensing.


  University of Maryland Dept. of Geographical Sciences'' developer surface includes authentication, support, engineering blog, getting-started guide, and 10 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 18.0
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
    developer_ergonomics: 31.0
    discoverability: 60.7
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: University Of Maryland Dept Of Geographical Sciences Authentication
  slug: university-of-maryland-dept-of-geographical-sciences-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: University Of Maryland Dept Of Geographical Sciences Domain Security
  slug: university-of-maryland-dept-of-geographical-sciences-domain-security
  summary_line: TLSv1.3 · DMARC
slug: university-of-maryland-dept-of-geographical-sciences
tags:
- Education
- Geography
- Research
- GIS
- Remote Sensing
website: https://geog.umd.edu
---
