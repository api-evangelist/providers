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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avisalaw/refs/heads/main/hosts/avisalaw-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avisalaw-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avisalaw/refs/heads/main/security/avisalaw-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avisalaw-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avisalaw.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://avisalaw.com
  - status: 403
    url: https://equityzen.com/company/avisalaw
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Avisalaw is a legal technology company that provides a platform for managing legal services, client relationships, and case workflows. The company aims to streamline law firm operations through cloud-based tools, offering features such as document management, billing, and collaboration. While detailed public information is limited, Avisalaw appears to target small to medium-sized law practices seeking integrated solutions for practice management and client engagement.
layout: provider
modified: '2026-09-27'
name: Avisalaw
nav: Providers
network: true
overview: Avisalaw is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Legal Tech, Software-as-a-Service, LawFirmSoftware, Practice Management, and Company.
random_paper: 20
score:
  band: minimal
  composite: 3.0
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
    operational_transparency: 0.0
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
  name: Avisalaw Domain Security
  slug: avisalaw-domain-security
  summary_line: TLSv1.3
slug: avisalaw
tags:
- Legal Tech
- Software-as-a-Service
- LawFirmSoftware
- Practice Management
- Company
website: https://avisalaw.com
---
