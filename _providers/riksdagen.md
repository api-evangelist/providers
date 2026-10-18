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
  href: https://raw.githubusercontent.com/api-evangelist/riksdagen/refs/heads/main/well-known/riksdagen-riksdagen-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/riksdagen-riksdagen-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/riksdagen/refs/heads/main/security/riksdagen-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/riksdagen-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/riksdagen/refs/heads/main/well-known/riksdagen-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/riksdagen-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/riksdagen/refs/heads/main/well-known/riksdagen-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/riksdagen-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/riksdagen/refs/heads/main/hosts/riksdagen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/riksdagen-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.riksdagen.se/sv/kontakt-och-besok/press/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/riksdagen/refs/heads/main/security/riksdagen-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/riksdagen-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/riksdagen/refs/heads/main/security/riksdagen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/riksdagen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://riksdagen.se/
coverage:
  checked: '2026-10-15'
  detail: Riksdagen provides legislative information and does not expose a software API.
  evidence:
  - status: 301
    url: https://www.riksdagen.se/
  reason: not-a-software-company
  state: none
created: '2026-10-15'
description: Riksdagen (Swedish Parliament) is the national legislature of Sweden, responsible for lawmaking, overseeing the government, and representing the Swedish people. The official website provides information about parliamentary work, members, legislation, debates, and public services. It serves as a portal for citizens to access documents, watch live sessions, and engage with democratic processes.
image: https://media.riksdagen.se/images/321a52d4a13411f1b3fc6e26682a384a
layout: provider
modified: '2026-10-15'
name: Riksdagen
nav: Providers
network: true
overview: Riksdagen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Sweden, Legislature, and Politics.
random_paper: 6
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 6
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
    discoverability: 50.0
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
  name: Riksdagen Domain Security
  slug: riksdagen-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Riksdagen Vulnerability Disclosure
  slug: riksdagen-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: riksdagen
tags:
- Company
- Government
- Sweden
- Legislature
- Politics
website: https://riksdagen.se/
---
