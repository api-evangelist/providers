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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/measurequick/plans/measurequick-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/measurequick-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/measurequick/llms/measurequick-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/measurequick-llms.txt
- group: other
  href: https://artifacts.apis.io/measurequick/hosts/measurequick-hosts.yml
  title: ''
  type: Hosts
  url: hosts/measurequick-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.measurequick.com/portal/en/kb/articles/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.measurequick.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://measurequick.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://measurequick.com/news/
- group: docs
  title: ''
  type: Documentation
  url: https://measurequick.com/documentation/
- group: operate
  title: ''
  type: ChangeLog
  url: https://measurequick.com/whats-new/
- group: start
  title: ''
  type: GettingStarted
  url: https://measurequick.com/getting-started-with-static-pressure-diagnostics/
- group: auth
  href: https://artifacts.apis.io/measurequick/security/measurequick-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/measurequick-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://measurequick.com/
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are HTML shells requiring JavaScript rendering, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://measurequick.com/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: measureQuick provides a residential HVAC commissioning platform that reads technician probes, scores systems against live conditions, and generates trusted reports. It supports over 80 tools across 17 brands, offering free and paid plans with advanced diagnostics, cloud dashboards, and training resources.
image: https://cms.measurequick.com/assets/95493d58-d6cb-4afe-8566-d9876432a02d?width=1200&quality=80&format=jpg
layout: provider
modified: '2026-10-28'
name: measureQuick
nav: Providers
network: true
overview: 'measureQuick is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HVAC, Diagnostics, Residential, and Software.


  measureQuick''s developer surface includes support, pricing, documentation, changelog, getting-started guide, and 7 more developer resources.'
plans:
- name: Measurequick Plans Pricing
  plan_count: 2
  slug: measurequick-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Measurequick Domain Security
  slug: measurequick-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: measurequick
tags:
- Company
- HVAC
- Diagnostics
- Residential
- Software
website: https://measurequick.com/
---
