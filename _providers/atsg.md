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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API documentation is provided via the Help portal.
  name: XTIUM API
  slug: xtium-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atsg/refs/heads/main/well-known/atsg-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/atsg-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atsg/refs/heads/main/well-known/atsg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atsg-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atsg/refs/heads/main/hosts/atsg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atsg-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atsg/refs/heads/main/vendors/atsg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atsg-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.xtium.com/
- group: company
  title: ''
  type: Newsroom
  url: https://xtium.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://help.xtium.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xtium
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atsg/refs/heads/main/security/atsg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atsg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://xtium.com
coverage:
  checked: 2026-09-26
  detail: Help portal renders documentation via JavaScript, no machine‑readable OpenAPI found.
  evidence:
  - status: 200
    url: https://help.xtium.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: XTIUM provides managed IT solutions, AI services, and cloud infrastructure for enterprises. Their offerings include AI readiness assessments, managed detection and response, desktop-as-a-service, and secure networking. The company emphasizes secure, scalable solutions across healthcare, finance, retail, and education sectors, positioning itself as a trusted partner for digital transformation.
image: https://xtium.com/hubfs/XTIUM-featured-logo.jpg
layout: provider
modified: '2026-09-26'
name: XTIUM
nav: Providers
network: true
overview: 'XTIUM publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Managed IT, AI Services, Cloud Infrastructure, Enterprise Solutions, and Security.


  XTIUM''s developer surface includes documentation and 9 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 58.9
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atsg Domain Security
  slug: atsg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atsg
tags:
- Managed IT
- AI Services
- Cloud Infrastructure
- Enterprise Solutions
- Security
website: https://xtium.com
---
