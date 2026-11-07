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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Brandloupe provides data via a private API; no public documentation or OpenAPI spec was found.
  name: Brandloupe API
  slug: brandloupe-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/brandloupe-com/llms/brandloupe-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brandloupe-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/brandloupe-com/well-known/brandloupe-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brandloupe-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/brandloupe-com/hosts/brandloupe-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brandloupe-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/brandloupe-com/vendors/brandloupe-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brandloupe-com-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://brandloupe.com/pricing/
- group: auth
  href: https://artifacts.apis.io/brandloupe-com/security/brandloupe-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brandloupe-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brandloupe.com/
coverage:
  checked: '2026-11-03'
  detail: Docs page returns a 404 rendered page with no machine‑readable spec despite attempts to fetch common spec URLs.
  evidence:
  - status: 404
    url: https://brandloupe.com/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Brandloupe tracks 936,017 live Shopify stores every week, providing data on product launches, best sellers, price changes, apps, ads, and traffic estimates. It offers competitor insights, methodology details, and a searchable database of Shopify store metrics.
image: https://brandloupe.com/og/index.png
layout: provider
modified: '2026-11-02'
name: Brandloupe
nav: Providers
network: true
overview: 'Brandloupe is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Analytics, Shopify, Competitor Intelligence, and Data Platform.


  Brandloupe''s developer surface includes pricing and 6 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
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
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brandloupe Com Domain Security
  slug: brandloupe-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: brandloupe-com
tags:
- E-Commerce
- Analytics
- Shopify
- Competitor Intelligence
- Data Platform
website: https://brandloupe.com/
---
