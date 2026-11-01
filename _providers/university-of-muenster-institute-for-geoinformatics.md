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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.uni-muenster.de/CERT/en/incidents/
- group: auth
  href: https://artifacts.apis.io/university-of-muenster-institute-for-geoinformatics/well-known/university-of-muenster-institute-for-geoinformatics-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/university-of-muenster-institute-for-geoinformatics-security.txt
- group: agent
  href: https://artifacts.apis.io/university-of-muenster-institute-for-geoinformatics/well-known/university-of-muenster-institute-for-geoinformatics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/university-of-muenster-institute-for-geoinformatics-well-known.yml
- group: other
  href: https://artifacts.apis.io/university-of-muenster-institute-for-geoinformatics/hosts/university-of-muenster-institute-for-geoinformatics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/university-of-muenster-institute-for-geoinformatics-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uni-muenster.de/
- group: company
  title: ''
  type: Newsroom
  url: https://www.uni-muenster.de/news/view.php?cmdid=15359
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ifgi
- group: auth
  href: https://artifacts.apis.io/university-of-muenster-institute-for-geoinformatics/security/university-of-muenster-institute-for-geoinformatics-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-muenster-institute-for-geoinformatics-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/university-of-muenster-institute-for-geoinformatics/security/university-of-muenster-institute-for-geoinformatics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/university-of-muenster-institute-for-geoinformatics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uni-muenster.de/Geoinformatics/
created: '2026-10-23'
description: The Institute for Geoinformatics (IFGI) at the University of Münster, Germany, conducts research, education, and technology transfer in geographic information science, spatial data analysis, and geospatial technologies. It offers academic programs, collaborates on EU-funded projects, and provides resources such as datasets, tools, and expertise to advance geoinformatics research and applications worldwide.
layout: provider
modified: '2026-10-23'
name: University of Muenster - Institute for Geoinformatics
nav: Providers
network: true
overview: University of Muenster - Institute for Geoinformatics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geoinformatics, Research, GIS, and University.
random_paper: 13
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: University Of Muenster Institute For Geoinformatics Domain Security
  slug: university-of-muenster-institute-for-geoinformatics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: University Of Muenster Institute For Geoinformatics Vulnerability Disclosure
  slug: university-of-muenster-institute-for-geoinformatics-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-muenster-institute-for-geoinformatics
tags:
- Company
- Geoinformatics
- Research
- GIS
- University
- Germany
website: https://www.uni-muenster.de/Geoinformatics/
---
