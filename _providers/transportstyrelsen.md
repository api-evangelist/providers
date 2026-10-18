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
  href: https://raw.githubusercontent.com/api-evangelist/transportstyrelsen/refs/heads/main/well-known/transportstyrelsen-transportstyrelsen-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/transportstyrelsen-transportstyrelsen-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/transportstyrelsen/refs/heads/main/security/transportstyrelsen-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/transportstyrelsen-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/transportstyrelsen/refs/heads/main/well-known/transportstyrelsen-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/transportstyrelsen-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/transportstyrelsen/refs/heads/main/well-known/transportstyrelsen-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/transportstyrelsen-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/transportstyrelsen/refs/heads/main/hosts/transportstyrelsen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/transportstyrelsen-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://www.transportstyrelsen.se/en/Log-in/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/transportstyrelsen/refs/heads/main/security/transportstyrelsen-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/transportstyrelsen-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/transportstyrelsen/refs/heads/main/security/transportstyrelsen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/transportstyrelsen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://transportstyrelsen.se/
coverage:
  checked: '2026-10-15'
  detail: No public developer program or API documentation was found for Transportstyrelsen.
  evidence:
  - status: 200
    url: https://transportstyrelsen.se/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Transportstyrelsen is the Swedish Transport Agency responsible for overseeing all aspects of transportation in Sweden, including road, rail, air, and maritime sectors. It develops regulations, issues permits, and provides public services such as vehicle registration, driver licensing, and safety oversight. The agency also publishes statistical data, guidelines, and digital services for citizens and industry stakeholders through its website.
image: https://www.transportstyrelsen.se/static/Images/ts-og-default-logo.png
layout: provider
modified: '2026-10-15'
name: Transportstyrelsen
nav: Providers
network: true
overview: Transportstyrelsen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Transport, Government, Sweden, and Regulations.
random_paper: 4
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Transportstyrelsen Domain Security
  slug: transportstyrelsen-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Transportstyrelsen Vulnerability Disclosure
  slug: transportstyrelsen-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: transportstyrelsen
tags:
- Company
- Transport
- Government
- Sweden
- Regulations
website: https://transportstyrelsen.se/
---
