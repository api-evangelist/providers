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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jaxsta/refs/heads/main/hosts/jaxsta-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jaxsta-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jaxsta/refs/heads/main/vendors/jaxsta-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jaxsta-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.jaxsta.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jaxsta/refs/heads/main/security/jaxsta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jaxsta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jaxsta.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jaxsta.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jaxsta.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://support@jaxsta.com
coverage:
  checked: '2026-10-12'
  detail: The OpenAPI endpoint returns HTML from a Framer site, not a machine‑readable spec.
  evidence:
  - status: 200
    url: https://jaxsta.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Jaxsta is a music industry data platform that aggregates official metadata from record labels, distributors, and rights owners. The service provides verified artist, release, and credit information to creators, partners, and industry members. As of 2024, Jaxsta entered hibernation under Vinyl Group, pausing commercial operations while preserving its underlying database and technology for future use. The platform remains a valuable source of authoritative music data for integration via APIs and data services.
layout: provider
modified: '2026-10-12'
name: Jaxsta
nav: Providers
network: true
overview: 'Jaxsta is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Data, and Platform.


  Jaxsta''s developer surface includes documentation, support, and 6 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Jaxsta Domain Security
  slug: jaxsta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jaxsta
tags:
- Company
- Music
- Data
- Platform
website: https://jaxsta.com/
---
