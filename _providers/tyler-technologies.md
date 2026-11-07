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
api_count: 1
apis:
- description: Public sector software APIs (none publicly documented)
  name: Tyler Technologies API
  slug: tyler-technologies-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/tyler-technologies/hosts/tyler-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tyler-technologies-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tylertech.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://www.tylertech.com/Register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tylertech.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://investors.tylertech.com/news/default.aspx
- group: docs
  title: ''
  type: Documentation
  url: https://help.tylertech.com/
- group: auth
  href: https://artifacts.apis.io/tyler-technologies/security/tyler-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tyler-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tylertech.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.tylertech.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Tyler Technologies provides software and services for the public sector, offering solutions that manage the entire property tax lifecycle, including computer‑assisted mass appraisal (CAMA), tax billing and collections, assessment administration, and civic services. Their AI‑enabled platforms help automate routine work, improve decision‑making, and enhance service delivery for government agencies.
layout: provider
modified: '2026-10-13'
name: Tyler Technologies
nav: Providers
network: true
overview: 'Tyler Technologies is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software, Public Sector, Government, and TaxSolutions.


  Tyler Technologies'' developer surface includes signup flow, documentation, and 6 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 54.5
    operational_transparency: 0.0
  previous_composite: 14.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tyler-technologies/tyler-technologies-2026-11-03T145335.png
security:
- kind: domain-security
  name: Tyler Technologies Domain Security
  slug: tyler-technologies-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: tyler-technologies
tags:
- Company
- Software
- Public Sector
- Government
- TaxSolutions
website: https://www.tylertech.com
---
