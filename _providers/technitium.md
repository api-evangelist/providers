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
api_count: 1
apis:
- description: The DNS Server HTTP API allows configuration of the DNS server via HTTP endpoints as documented in the project's APIDOCS.md.
  name: Technitium DNS Server HTTP API
  slug: technitium-dns-server-http-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/technitium/hosts/technitium-hosts.yml
  title: ''
  type: Hosts
  url: hosts/technitium-hosts.yml
- group: auth
  href: https://artifacts.apis.io/technitium/security/technitium-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/technitium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://technitium.com/
- group: docs
  title: ''
  type: Documentation
  url: https://technitium.com/dns/
- group: company
  title: ''
  type: Blog
  url: https://blog.technitium.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TechnitiumSoftware
- group: operate
  title: ''
  type: Support
  url: https://technitium.com/dns/#support
coverage:
  checked: '2026-10-28'
  detail: The provider only offers API documentation in a Markdown file on GitHub without a published OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://github.com/TechnitiumSoftware/DnsServer/blob/master/APIDOCS.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Technitium DNS Server provides an open source authoritative and recursive DNS server solution focused on privacy and security. It offers easy self‑hosting with a web console, supports DNS‑over‑TLS, DNS‑over‑HTTPS, and DNS‑over‑QUIC, and includes features like ad‑blocking, malware filtering, and detailed query logging. The software runs on Windows, Linux, macOS, and Raspberry Pi, and is available as a portable app, installer, Docker image, and source code, enabling users to protect their networks and gain insight into DNS traffic.
layout: provider
modified: '2026-10-28'
name: Technitium DNS Server
nav: Providers
network: true
overview: 'Technitium DNS Server is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DNS, OpenSource, Privacy, and Security.


  Technitium DNS Server''s developer surface includes documentation, engineering blog, support, and 4 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 53.6
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Technitium Domain Security
  slug: technitium-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: technitium
tags:
- Company
- DNS
- OpenSource
- Privacy
- Security
website: https://technitium.com/
---
