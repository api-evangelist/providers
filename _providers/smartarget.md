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
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/smartarget/security/smartarget-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smartarget-domain-security.yml
- group: other
  href: https://artifacts.apis.io/smartarget/hosts/smartarget-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smartarget-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://smartarget.online/blog/
- group: company
  href: https://artifacts.apis.io/smartarget/security/smartarget-domain-security.yml
  title: ''
  type: Website
  url: security/smartarget-domain-security.yml
created: '2026-10-26'
description: Smartarget provides a platform for financial application developers to integrate banking services, offering APIs for payments, account information, and transaction processing. The company focuses on enabling fintech solutions with robust security, compliance, and developer-friendly tools, targeting businesses building modern financial products.
image: https://smartarget.online/images/apps.webp
layout: provider
modified: '2026-10-26'
name: Smartarget
nav: Providers
network: true
overview: 'Smartarget is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Banking APIs, and Developer Platform.


  Smartarget''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 3.2
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
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Smartarget Domain Security
  slug: smartarget-domain-security
  summary_line: TLSv1.2 · DMARC
slug: smartarget
tags:
- Company
- Fintech
- Payments
- Banking APIs
- Developer Platform
---
