---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  - sandbox
  trial: false
  try_now: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/technologyone/plans/technologyone-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/technologyone-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/technologyone/lifecycle/technologyone-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/technologyone-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/technologyone/conformance/technologyone-conformance.yml
  title: ''
  type: Conformance
  url: conformance/technologyone-conformance.yml
- group: other
  href: https://artifacts.apis.io/technologyone/hosts/technologyone-hosts.yml
  title: ''
  type: Hosts
  url: hosts/technologyone-hosts.yml
- group: other
  href: https://artifacts.apis.io/technologyone/vendors/technologyone-vendors.yml
  title: ''
  type: Vendors
  url: vendors/technologyone-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/technologyonecorp
- group: auth
  href: https://artifacts.apis.io/technologyone/security/technologyone-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/technologyone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://technologyonecorp.com/
created: '2026-10-22'
description: TechnologyOne (Technology One; UK entity TECHNOLOGY ONE UK LIMITED) is an enterprise software company that provides ERP delivered as SaaS. Its OnePublicSector product, listed on the UK government G-Cloud Digital Marketplace, is a fully integrated ERP SaaS solution for the public sector that builds in best-practice business processes. It covers financial management, including general ledger, accounts payable and receivable, budgeting and forecasting, and is available on any device. The company surfaced via the australia-apidays-2026 harvest. Its website (technologyonecorp.com) refuses automated clients with a 403 bot challenge.
layout: provider
modified: '2026-10-22'
name: TechnologyOne
nav: Providers
network: true
overview: TechnologyOne is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, ERP, Software-as-a-Service, Enterprise Software, and Public Sector.
plans:
- name: Technologyone Plans Pricing
  plan_count: 2
  slug: technologyone-plans-pricing
random_paper: 14
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/technologyone/technologyone-2026-11-03T144401.png
security:
- kind: domain-security
  name: Technologyone Domain Security
  slug: technologyone-domain-security
  summary_line: TLSv1.3 · DMARC
slug: technologyone
tags:
- Company
- ERP
- Software-as-a-Service
- Enterprise Software
- Public Sector
- Financial Management
- Australia
website: https://technologyonecorp.com/
---
