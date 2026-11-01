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
  href: https://artifacts.apis.io/electrainfo/hosts/electrainfo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/electrainfo-hosts.yml
- group: other
  href: https://artifacts.apis.io/electrainfo/vendors/electrainfo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/electrainfo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dashboard.electrainfo.com/terms-of-use.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dashboard.electrainfo.com/privacy.php
- group: company
  title: ''
  type: Blog
  url: https://www.greshamtech.com/blog
- group: auth
  href: https://artifacts.apis.io/electrainfo/security/electrainfo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/electrainfo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://electrainfo.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://electrainfo.com/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: Gresham Technologies provides enterprise data management and reconciliation solutions for financial services firms. Its product portfolio includes EDM platforms, Control Cloud and Connect Cloud for automated reconciliation, and data services for regulatory reporting, ESG, and trading data. The company serves banks, asset managers, custodians and other financial institutions that need to automate, validate and scale data operations.
image: https://www.greshamtech.com/hubfs/00%20Struto_FLUID%20Theme/images/Gresham-icon.svg
layout: provider
modified: '2026-10-20'
name: Gresham Technologies
nav: Providers
network: true
overview: 'Gresham Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise Data Management, Reconciliation, Regulatory Reporting, Data Services, and Financial Services.


  Gresham Technologies'' developer surface includes engineering blog and 6 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Electrainfo Domain Security
  slug: electrainfo-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: electrainfo
tags:
- Enterprise Data Management
- Reconciliation
- Regulatory Reporting
- Data Services
- Financial Services
- ESG Data
- Trading Data
website: https://electrainfo.com/
---
