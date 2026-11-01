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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/ancestry/well-known/ancestry-ancestry-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ancestry-ancestry-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.ancestry.com/c/legal/security
- group: auth
  href: https://artifacts.apis.io/ancestry/well-known/ancestry-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ancestry-security.txt
- group: auth
  href: https://artifacts.apis.io/ancestry/well-known/ancestry-data-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ancestry-data-security.txt
- group: auth
  href: https://artifacts.apis.io/ancestry/well-known/ancestry-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ancestry-api-security.txt
- group: agent
  href: https://artifacts.apis.io/ancestry/well-known/ancestry-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ancestry-well-known.yml
- group: other
  href: https://artifacts.apis.io/ancestry/hosts/ancestry-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ancestry-hosts.yml
- group: other
  href: https://artifacts.apis.io/ancestry/vendors/ancestry-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ancestry-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ancestry
- group: auth
  href: https://artifacts.apis.io/ancestry/security/ancestry-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ancestry-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ancestry/security/ancestry-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ancestry-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ancestry.com/
created: '2026-10-28'
description: Ancestry TreeShare download + WebHints provides tools for downloading family tree data from Ancestry.com and offers web hints for navigating the service. The company aggregates publicly available genealogical data, enabling users to export their family histories and integrate them into other applications. It focuses on simplifying data extraction, supporting various file formats, and delivering guidance for accessing Ancestry’s web interface efficiently.
layout: provider
modified: '2026-10-28'
name: Ancestry TreeShare download + WebHints
nav: Providers
network: true
overview: Ancestry TreeShare download + WebHints is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Genealogy, DataExport, WebTools, and FamilyHistory.
random_paper: 9
score:
  band: minimal
  composite: 6.0
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
    discoverability: 44.6
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ancestry Domain Security
  slug: ancestry-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ancestry Vulnerability Disclosure
  slug: ancestry-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ancestry
tags:
- Company
- Genealogy
- DataExport
- WebTools
- FamilyHistory
website: https://ancestry.com/
---
