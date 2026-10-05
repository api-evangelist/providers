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
- description: Help library for Ab Initio platform
  name: Ab Initio Help Library
  slug: ab-initio-help-library
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/abinitio/refs/heads/main/hosts/abinitio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/abinitio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/abinitio/refs/heads/main/vendors/abinitio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/abinitio-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abinitio.com/de/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abinitio.com/de/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/abinitio/refs/heads/main/security/abinitio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/abinitio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.abinitio.com
coverage:
  checked: '2026-10-03'
  detail: Docs site returns only a JavaScript shell with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://docs.abinitio.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Ab Initio provides an enterprise data platform that enables large-scale data processing, integration, and analytics across diverse industries. Its software automates data ingestion, transformation, and delivery, supporting batch and real‑time workloads on cloud and on‑premises environments. The platform emphasizes scalability, self‑service, and governance, helping organizations turn massive data streams into actionable insights.
image: https://www.abinitio.com/pub/abinitio-og.jpg
layout: provider
modified: '2026-10-03'
name: Ab Initio
nav: Providers
network: true
overview: Ab Initio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Platform, Enterprise Software, Integration, and Analytics.
random_paper: 11
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Abinitio Domain Security
  slug: abinitio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: abinitio
tags:
- Company
- Data Platform
- Enterprise Software
- Integration
- Analytics
website: https://www.abinitio.com
---
