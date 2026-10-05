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
  href: https://raw.githubusercontent.com/api-evangelist/bodyshopbids/refs/heads/main/hosts/bodyshopbids-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bodyshopbids-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bodyshopbids/refs/heads/main/security/bodyshopbids-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bodyshopbids-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://snapsheet.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/bodyshopbids
  reason: no-developer-program
  state: none
created: '2026-10-02'
description: Bodyshopbids, now operating as SnapSheet, is a Chicago‑based technology company that provides a mobile and web platform enabling consumers to obtain multiple auto body repair estimates by uploading photos of vehicle damage. The service connects drivers with local body shops through a competitive bidding system, streamlining the claims process for insurers and repair shops. SnapSheet offers APIs for claim intake, estimate management, and shop communication, supporting integration with insurance carriers and third‑party services.
image: https://snapsheet.com/favicon.ico
layout: provider
modified: '2026-10-02'
name: Bodyshopbids
nav: Providers
network: true
overview: Bodyshopbids is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Automotive, Claims, B2B, and Platform.
random_paper: 14
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 5
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
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 5.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bodyshopbids Domain Security
  slug: bodyshopbids-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bodyshopbids
tags:
- Insurance
- Automotive
- Claims
- B2B
- Platform
website: https://snapsheet.com
---
