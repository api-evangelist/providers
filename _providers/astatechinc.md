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
- description: API for Astatechinc services as listed in the catalog
  name: Astatechinc API
  slug: astatechinc-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/astatechinc/refs/heads/main/hosts/astatechinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astatechinc-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/astatechinc/refs/heads/main/security/astatechinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astatechinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.astatechinc.com/
- group: operate
  title: ''
  type: Support
  url: https://www.astatechinc.com/Contact_Us.php
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.astatechinc.com/Order-Terms.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.astatechinc.com/Order-Privacy.php
coverage:
  checked: 2026-09-26
  detail: Main site pages render via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.astatechinc.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Astatechinc, operating as AstaTech Inc., is a long‑standing U.S. contract research organization (CRO) based in Bristol, Pennsylvania. Founded in 1996, it provides extensive chemistry catalog products, custom synthesis, bulk manufacturing, and analytical services to pharmaceutical and biotechnology companies worldwide. The company emphasizes high‑quality, cost‑effective solutions and is certified as a Woman‑Owned Small Business.
layout: provider
modified: '2026-09-26'
name: Astatechinc
nav: Providers
network: true
overview: 'Astatechinc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Contract Research Organization, Pharmaceuticals, Custom Synthesis, Bulk Manufacturing, and Analytical Services.


  Astatechinc''s developer surface includes support and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 53.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Astatechinc Domain Security
  slug: astatechinc-domain-security
  summary_line: TLSv1.2
slug: astatechinc
tags:
- Contract Research Organization
- Pharmaceuticals
- Custom Synthesis
- Bulk Manufacturing
- Analytical Services
- Catalog Products
website: https://www.astatechinc.com/
---
