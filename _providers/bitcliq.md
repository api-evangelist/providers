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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: SOAP WSDL service for issue tracking, sourced from Bitcliq GitHub repository fishackathon2016.
  name: Bitcliq Issues Service
  slug: bitcliq-issues-service
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitcliq/refs/heads/main/wsdl/bitcliq-issues.wsdl
  title: ''
  type: WSDL
  url: wsdl/bitcliq-issues.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitcliq/refs/heads/main/hosts/bitcliq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitcliq-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bitcliq
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitcliq/refs/heads/main/security/bitcliq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitcliq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bitcliq.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/bitcliq
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: Bitcliq Technologies is a Portuguese software company that develops innovative digital solutions for the transport, fisheries and agri‑food industries. Their platform enables smarter food chains through real‑time data integration, traceability, and operational management for fleets and packaging. Bitcliq offers products such as Big Eye Smart Fishing and Lota Digital, serving national and international clients with cloud‑based services.
layout: provider
modified: '2026-09-28'
name: Bitcliq
nav: Providers
network: true
overview: Bitcliq publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software, Agrifood, Fisheries, and Transport.
random_paper: 18
score:
  band: minimal
  composite: 4.6
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
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bitcliq Domain Security
  slug: bitcliq-domain-security
  summary_line: TLSv1.2 · DMARC
slug: bitcliq
tags:
- Company
- Software
- Agrifood
- Fisheries
- Transport
website: https://www.bitcliq.com
---
