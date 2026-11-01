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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.helyx.co.uk/vulnerability-reporting
- group: auth
  href: https://artifacts.apis.io/helyx-secure-information-systems-ltd/well-known/helyx-secure-information-systems-ltd-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/helyx-secure-information-systems-ltd-security.txt
- group: agent
  href: https://artifacts.apis.io/helyx-secure-information-systems-ltd/well-known/helyx-secure-information-systems-ltd-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/helyx-secure-information-systems-ltd-well-known.yml
- group: other
  href: https://artifacts.apis.io/helyx-secure-information-systems-ltd/hosts/helyx-secure-information-systems-ltd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/helyx-secure-information-systems-ltd-hosts.yml
- group: other
  href: https://artifacts.apis.io/helyx-secure-information-systems-ltd/vendors/helyx-secure-information-systems-ltd-vendors.yml
  title: ''
  type: Vendors
  url: vendors/helyx-secure-information-systems-ltd-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.helyx.co.uk/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/helyx
- group: auth
  href: https://artifacts.apis.io/helyx-secure-information-systems-ltd/security/helyx-secure-information-systems-ltd-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/helyx-secure-information-systems-ltd-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/helyx-secure-information-systems-ltd/security/helyx-secure-information-systems-ltd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/helyx-secure-information-systems-ltd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.helyx.co.uk/
coverage:
  detail: No machine‑readable API specification found on the provider's sites.
  evidence:
  - status: 200
    url: https://api.co.uk/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Helyx secure information systems ltd provides specialist geospatial information management and exploitation solutions, primarily serving defence and government sectors in the UK. The company offers consultancy, technical services, and integrates vendor solutions to enhance decision‑making in demanding environments, while expanding into commercial markets.
layout: provider
modified: '2026-10-26'
name: Helyx secure information systems ltd
nav: Providers
network: true
overview: Helyx secure information systems ltd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geospatial, InformationManagement, Defence, and Consultancy.
random_paper: 15
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Helyx Secure Information Systems Ltd Domain Security
  slug: helyx-secure-information-systems-ltd-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Helyx Secure Information Systems Ltd Vulnerability Disclosure
  slug: helyx-secure-information-systems-ltd-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: helyx-secure-information-systems-ltd
tags:
- Company
- Geospatial
- InformationManagement
- Defence
- Consultancy
website: https://www.helyx.co.uk/
---
