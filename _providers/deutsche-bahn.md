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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bahn/refs/heads/main/security/deutsche-bahn-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/deutsche-bahn-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bahn/refs/heads/main/well-known/deutsche-bahn-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deutsche-bahn-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bahn/refs/heads/main/well-known/deutsche-bahn-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deutsche-bahn-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bahn/refs/heads/main/hosts/deutsche-bahn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deutsche-bahn-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bahn/refs/heads/main/security/deutsche-bahn-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deutsche-bahn-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deutsche-bahn/refs/heads/main/security/deutsche-bahn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deutsche-bahn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bahn.de/
created: '2026-10-12'
description: Deutsche Bahn AG is Germany's national railway company, operating passenger and freight services across Europe. It provides a comprehensive digital platform offering journey planning, ticket booking, real-time traffic information, and various travel-related services via web and mobile applications. The API ecosystem includes endpoints for timetables, fare calculation, reservation management, and service alerts, supporting developers building travel solutions and integrations.
image: https://assets.static-bahn.de/.resources/bahn-common/webresources/img/social-media-default.jpg
layout: provider
modified: '2026-10-12'
name: Deutsche Bahn
nav: Providers
network: true
overview: Deutsche Bahn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Transportation, Railways, Travel, and Germany.
random_paper: 9
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deutsche Bahn Domain Security
  slug: deutsche-bahn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deutsche Bahn Vulnerability Disclosure
  slug: deutsche-bahn-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deutsche-bahn
tags:
- Company
- Transportation
- Railways
- Travel
- Germany
website: https://bahn.de/
---
