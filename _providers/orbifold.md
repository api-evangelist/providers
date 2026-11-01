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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: docs
  title: ''
  type: Documentation
  url: https://docs.orbifold.ai/
- group: other
  href: https://artifacts.apis.io/orbifold/hosts/orbifold-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orbifold-hosts.yml
- group: other
  href: https://artifacts.apis.io/orbifold/vendors/orbifold-vendors.yml
  title: ''
  type: Vendors
  url: vendors/orbifold-vendors.yml
- group: auth
  href: https://artifacts.apis.io/orbifold/security/orbifold-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orbifold-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orbifold.ai
- group: company
  title: ''
  type: Blog
  url: https://www.orbifold.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.orbifold.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orbifold.ai/privacy
coverage:
  checked: '2026-10-22'
  detail: Documentation pages return 404 HTML shells without machine-readable specs.
  evidence:
  - status: 404
    url: https://www.orbifold.ai/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Orbifold AI provides a distributed infrastructure for physical AI, offering a unified multimodal data API that ingests, aligns, and manages real‑world data such as text, images, video, and audio. Their platform enables engineers, data scientists, and product designers to build AI‑driven applications faster, with built‑in compliance, observability, and zero data retention. Backed by Bonfire Ventures, Orbifold aims to replace fragmented pipelines and manual labeling, delivering scalable, cost‑effective AI solutions for enterprises.
layout: provider
modified: '2026-10-21'
name: Orbifold
nav: Providers
network: true
overview: 'Orbifold is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Data, Infrastructure, and Multimodal.


  Orbifold''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Orbifold Domain Security
  slug: orbifold-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: orbifold
tags:
- Company
- AI
- Data
- Infrastructure
- Multimodal
website: https://orbifold.ai
---
