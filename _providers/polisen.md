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
  href: https://raw.githubusercontent.com/api-evangelist/polisen/refs/heads/main/security/polisen-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/polisen-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/polisen/refs/heads/main/well-known/polisen-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/polisen-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/polisen/refs/heads/main/well-known/polisen-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/polisen-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/polisen/refs/heads/main/hosts/polisen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/polisen-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://polisen.se/en/laws-and-regulations/travel-to-and-stay-in-sweden/terms-of-stay-in-sweden/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/polisen/refs/heads/main/security/polisen-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/polisen-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/polisen/refs/heads/main/security/polisen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/polisen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://polisen.se/
- group: docs
  title: ''
  type: Documentation
  url: https://polisen.se/om-polisen/om-webbplatsen/oppna-data/api-over-polisens-handelser/
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was discovered on any owned host.
  evidence:
  - status: 0
    url: https://api.polisen.se/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Polisen is Sweden’s national police authority, responsible for law enforcement, public safety, and crime prevention across the country. The agency provides public information, services, and resources through its website, including crime statistics, reporting tools, and guidance for citizens. While primarily a governmental organization, its digital platforms expose various APIs for data access, service integration, and public engagement, making it a relevant entity for API profiling and integration efforts.
image: https://polisen.se/contentassets/8c8311b0de514a09b6ae2f84e5afab9d/polisen_twitter_image.png
layout: provider
modified: '2026-10-15'
name: Polisen
nav: Providers
network: true
overview: 'Polisen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Law Enforcement, Public Safety, and Sweden.


  Polisen''s developer surface includes documentation and 8 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Polisen Domain Security
  slug: polisen-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Polisen Vulnerability Disclosure
  slug: polisen-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: polisen
tags:
- Company
- Government
- Law Enforcement
- Public Safety
- Sweden
website: https://polisen.se/
---
