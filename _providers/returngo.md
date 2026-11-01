---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/returngo/plans/returngo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/returngo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/returngo/changelog/returngo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/returngo-changelog.yml
- group: agent
  href: https://artifacts.apis.io/returngo/well-known/returngo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/returngo-well-known.yml
- group: other
  href: https://artifacts.apis.io/returngo/hosts/returngo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/returngo-hosts.yml
- group: other
  href: https://artifacts.apis.io/returngo/vendors/returngo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/returngo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://returngo.ai/terms/
- group: operate
  title: ''
  type: Support
  url: https://support.returngo.ai/
- group: company
  title: ''
  type: Newsroom
  url: https://returngo.ai/press/
- group: start
  title: ''
  type: Login
  url: https://app.returngo.ai/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.returngo.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://returngo.ai/release-notes/
- group: auth
  href: https://artifacts.apis.io/returngo/security/returngo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/returngo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://returngo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://returngo.ai/returns-management-api/
- group: docs
  title: ''
  type: APIReference
  url: https://returngo.ai/returns-management-api/
- group: company
  title: ''
  type: Blog
  url: https://returngo.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://returngo.ai/pricing/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite public documentation pages.
  evidence:
  - status: 200
    url: https://returngo.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: ReturnGO provides a sustainable returns and exchanges management platform for eCommerce brands. Their open API enables automated return processing, warranty handling, exchange management, and tracking, helping companies turn post‑purchase interactions into revenue while reducing waste. The service integrates with major eCommerce tools and offers a white‑label solution for branded return portals.
layout: provider
modified: '2026-10-28'
name: ReturnGO
nav: Providers
network: true
overview: 'ReturnGO is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, eCommerce, Returns, API, and Sustainability.


  ReturnGO''s developer surface includes changelog, support, documentation, API reference, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Returngo Plans Pricing
  plan_count: 3
  slug: returngo-plans-pricing
random_paper: 22
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 46.4
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Returngo Domain Security
  slug: returngo-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: returngo
tags:
- Company
- eCommerce
- Returns
- API
- Sustainability
website: https://returngo.ai/
---
