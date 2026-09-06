---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/govguard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://govguard.com
- group: company
  title: ''
  type: About
  url: https://govguard.com/#about
- group: operate
  title: ''
  type: Support
  url: https://govguard.com/contactus
- group: start
  title: ''
  type: Login
  url: https://govguard.com/app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://govguard.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://govguard.com/privacypolicy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/govguard
- group: company
  title: ''
  type: Twitter
  url: https://x.com/gov_guard
- group: company
  title: ''
  type: Crunchbase
  url: https://www.ycombinator.com/companies/govguard
created: '2026-07-17'
description: GovGuard is a Y Combinator-backed (Spring 2026) GovTech company building AI infrastructure for government agencies, starting with Freedom of Information Act (FOIA) request automation. Its AI agents route incoming public-records requests, search across municipal archives (emails, meeting minutes, PDFs, and shared drives), flag personally identifiable information and other exempt material for redaction against the relevant state exemption codes, and draft response letters for clerk review while maintaining a complete audit trail. Agencies retain full ownership and control of all records and metadata, and GovGuard states that it does not train models on client data. The company was founded by Aditya Sabharwal and Gleb Hulting and is based in San Francisco.
image: https://govguard.com/logo.png
layout: provider
modified: '2026-07-19'
name: GovGuard
nav: Providers
network: true
overview: 'GovGuard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, GovTech, FOIA, and Public Records.


  GovGuard''s developer surface includes support and 9 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 25.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/govguard/refs/heads/main/screenshots/govguard-2026-07-25T220131.png
security:
- kind: domain-security
  name: Govguard Domain Security
  slug: govguard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: govguard
tags:
- Company
- Government
- GovTech
- FOIA
- Public Records
- Records Management
- Redaction
- Compliance
- Artificial Intelligence
- AI Agents
website: https://govguard.com
---
