---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/squirrel-systems/well-known/squirrel-systems-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/squirrel-systems-well-known.yml
- group: other
  href: https://artifacts.apis.io/squirrel-systems/hosts/squirrel-systems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/squirrel-systems-hosts.yml
- group: other
  href: https://artifacts.apis.io/squirrel-systems/vendors/squirrel-systems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/squirrel-systems-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.squirrelsystems.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://help.squirrelsystems.com/s/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.squirrelsystems.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.squirrelsystems.com/posts/category/news/
- group: company
  title: ''
  type: Blog
  url: https://www.squirrelsystems.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://help.squirrelsystems.com/
- group: auth
  href: https://artifacts.apis.io/squirrel-systems/security/squirrel-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/squirrel-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://squirrelsystems.com/
coverage:
  checked: '2026-10-28'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://help.squirrelsystems.com/s/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Squirrel Systems provides a cloud‑based point‑of‑sale platform for restaurants, multi‑unit restaurant chains, and hospitality venues such as hotels, resorts, and casinos. The solution includes POS, payments, digital ordering, kitchen automation, reporting, analytics, and integrations with inventory, labor, payroll, reservations, gaming, and property‑management systems.
image: https://www.squirrelsystems.com/wp-content/uploads/2026/03/6630transparent-scaled.png
layout: provider
modified: '2026-10-28'
name: Squirrel Systems
nav: Providers
network: true
overview: 'Squirrel Systems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Point-of-Sale, Restaurant, Hospitality, Digital Ordering, and Kitchen Automation.


  Squirrel Systems'' developer surface includes support, engineering blog, documentation, and 8 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 49.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/squirrel-systems/squirrel-systems-2026-11-03T143705.png
security:
- kind: domain-security
  name: Squirrel Systems Domain Security
  slug: squirrel-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: squirrel-systems
tags:
- Point-of-Sale
- Restaurant
- Hospitality
- Digital Ordering
- Kitchen Automation
- Analytics
- Integration
website: https://squirrelsystems.com/
---
