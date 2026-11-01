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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/layer2solutions/plans/layer2solutions-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/layer2solutions-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/layer2solutions/hosts/layer2solutions-hosts.yml
  title: ''
  type: Hosts
  url: hosts/layer2solutions-hosts.yml
- group: other
  href: https://artifacts.apis.io/layer2solutions/vendors/layer2solutions-vendors.yml
  title: ''
  type: Vendors
  url: vendors/layer2solutions-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.layer2solutions.com/about-us/news
- group: auth
  href: https://artifacts.apis.io/layer2solutions/security/layer2solutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/layer2solutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://layer2solutions.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.layer2solutions.com/data-integration
- group: commercial
  title: ''
  type: Pricing
  url: https://www.layer2solutions.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.layer2solutions.com/support
- group: operate
  title: ''
  type: Contact
  url: https://www.layer2solutions.com/contact-us
- group: other
  title: ''
  type: Sitemap
  url: https://www.layer2solutions.com/sitemap
coverage:
  checked: '2026-10-20'
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine-readable contract discovered on api.layer2solutions.com.
  evidence:
  - status: no-response
    url: https://api.layer2solutions.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Layer 2 provides data integration and file synchronization solutions for Microsoft Cloud services such as Office 365, SharePoint, and Azure. It enables synchronization across 150+ systems and apps, serving over 2,500 companies worldwide with products like Layer2 Cloud Connector and Business Data List Connector.
layout: provider
modified: '2026-10-20'
name: Layer 2
nav: Providers
network: true
overview: 'Layer 2 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Integration, File Synchronization, Microsoft Cloud, and Office 365.


  Layer 2''s developer surface includes documentation, pricing, support, and 8 more developer resources.'
plans:
- name: Layer2Solutions Plans Pricing
  plan_count: 5
  slug: layer2solutions-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Layer2Solutions Domain Security
  slug: layer2solutions-domain-security
  summary_line: TLSv1.3 · DMARC
slug: layer2solutions
tags:
- Company
- Data Integration
- File Synchronization
- Microsoft Cloud
- Office 365
website: https://layer2solutions.com/
---
