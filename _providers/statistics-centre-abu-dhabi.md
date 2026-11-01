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
- group: agent
  href: https://artifacts.apis.io/statistics-centre-abu-dhabi/llms/statistics-centre-abu-dhabi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/statistics-centre-abu-dhabi-llms.txt
- group: other
  href: https://artifacts.apis.io/statistics-centre-abu-dhabi/hosts/statistics-centre-abu-dhabi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/statistics-centre-abu-dhabi-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scad.gov.ae/privacypolicy
- group: start
  title: ''
  type: Login
  url: https://scad.gov.ae/login
- group: auth
  href: https://artifacts.apis.io/statistics-centre-abu-dhabi/security/statistics-centre-abu-dhabi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/statistics-centre-abu-dhabi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.scad.ae
coverage:
  checked: '2026-10-28'
  detail: No public developer documentation or API specifications were found on the provider's website.
  evidence:
  - status: 200
    url: https://scad.gov.ae/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Statistics Centre - Abu Dhabi (SCAD) is the official statistical authority of the Emirate of Abu Dhabi, providing comprehensive data, analysis, and insights across economic, demographic, social, and environmental domains. It supports government decision‑making, business planning, and public research by publishing regular reports, interactive dashboards, and open data sets. SCAD collaborates with international statistical bodies and adheres to global standards, ensuring data quality, transparency, and accessibility for stakeholders.
image: https://scad.gov.ae/documents/20122/0/scad-sharing.jpg/97de65d6-0cad-ec35-e5c2-f3086d927fa4?version=1.0&t=1731498678574&imagePreview=1
layout: provider
modified: '2026-10-28'
name: Statistics Centre - Abu Dhabi
nav: Providers
network: true
overview: Statistics Centre - Abu Dhabi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Statistics, Government, Data, and AbuDhabi.
random_paper: 3
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Statistics Centre Abu Dhabi Domain Security
  slug: statistics-centre-abu-dhabi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: statistics-centre-abu-dhabi
tags:
- Company
- Statistics
- Government
- Data
- AbuDhabi
website: http://www.scad.ae
---
