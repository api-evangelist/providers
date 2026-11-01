---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: MISMO provides data standards and XML schemas for mortgage industry; documentation is available as PDF but no machine-readable API contract was found.
  name: MISMO API
  slug: mismo-api
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/mortgage-industry-standards-maintenance-organization-mismo/changelog/mortgage-industry-standards-maintenance-organization-mismo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mortgage-industry-standards-maintenance-organization-mismo-changelog.yml
- group: agent
  href: https://artifacts.apis.io/mortgage-industry-standards-maintenance-organization-mismo/well-known/mortgage-industry-standards-maintenance-organization-mismo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mortgage-industry-standards-maintenance-organization-mismo-well-known.yml
- group: other
  href: https://artifacts.apis.io/mortgage-industry-standards-maintenance-organization-mismo/hosts/mortgage-industry-standards-maintenance-organization-mismo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mortgage-industry-standards-maintenance-organization-mismo-hosts.yml
- group: other
  href: https://artifacts.apis.io/mortgage-industry-standards-maintenance-organization-mismo/vendors/mortgage-industry-standards-maintenance-organization-mismo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mortgage-industry-standards-maintenance-organization-mismo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mismo.org/terms
- group: start
  title: ''
  type: SignUp
  url: https://www.mismo.org/register-for-a-summit
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mismo.org/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://www.mismo.org/docs/mismolibraries/active-(documents/getting-started-with-the-mismo-api-toolkit.pdf?sfvrsn=15289242_3
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mismo.org/standards-resources/life-of-loan/release-notes
- group: auth
  href: https://artifacts.apis.io/mortgage-industry-standards-maintenance-organization-mismo/security/mortgage-industry-standards-maintenance-organization-mismo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mortgage-industry-standards-maintenance-organization-mismo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mismo.org
coverage:
  checked: '2026-10-26'
  detail: Documentation is provided as PDF files with no machine‑readable OpenAPI/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://www.mismo.org/docs/mismolibraries/active-(documents/getting-started-with-the-mismo-api-toolkit.pdf?sfvrsn=15289242_3
  reason: pdf-only-docs
  state: unreadable
created: '2026-10-26'
description: Mortgage Industry Standards Maintenance Organization (MISMO) is a nonprofit association that develops and maintains data standards for the mortgage finance industry. It provides a comprehensive reference model, logical data models, XML schemas, and implementation guides that enable consistent data exchange among lenders, servicers, investors, and technology providers. MISMO’s resources support regulatory compliance, improve operational efficiency, and foster innovation across the mortgage ecosystem.
image: https://www.mismo.org/images/mismolibraries/active/mismo-logo-high-res_50percent.png?sfvrsn=97977f5f_1
layout: provider
modified: '2026-10-26'
name: Mortgage Industry Standards Maintenance Organization (MISMO)
nav: Providers
network: true
overview: 'Mortgage Industry Standards Maintenance Organization (MISMO) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mortgage, Standards, Data, and Finance.


  Mortgage Industry Standards Maintenance Organization (MISMO)''s developer surface includes changelog, signup flow, documentation, and 8 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mortgage Industry Standards Maintenance Organization Mismo Domain Security
  slug: mortgage-industry-standards-maintenance-organization-mismo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mortgage-industry-standards-maintenance-organization-mismo
tags:
- Company
- Mortgage
- Standards
- Data
- Finance
website: https://www.mismo.org
---
