---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
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
  score: 8.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Glympt technographic enrichment, documented at the MCP setup guide.
  name: Glympt API
  slug: glympt-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/glympt-com/plans/glympt-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/glympt-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/glympt-com/conventions/glympt-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/glympt-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/glympt-com/conventions/glympt-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/glympt-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/glympt-com/authentication/glympt-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/glympt-com-authentication.yml
- group: other
  href: https://artifacts.apis.io/glympt-com/hosts/glympt-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/glympt-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/glympt-com/vendors/glympt-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/glympt-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/glympt-com/security/glympt-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/glympt-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://glympt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://glympt.com/docs/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://glympt.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://glympt.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://glympt.com/sign-up
- group: operate
  title: ''
  type: Support
  url: https://glympt.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://glympt.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://glympt.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/serkandrgn
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are JavaScript-rendered single-page apps, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://glympt.com/docs/mcp
  - status: 200
    url: https://glympt.com/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Glympt provides technographic lead lists for agencies and developers, offering a database of bulk CSV API and MCP extensions to enrich domains with technology fingerprints. Users can search websites by tech stack, upload domains for enrichment, and export results via API. The platform includes pricing plans, a free tier, and documentation for integration.
image: https://glympt.com/logos/logo-500.png
layout: provider
modified: '2026-10-30'
name: glympt-com
nav: Providers
network: true
overview: 'glympt-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Enrichment, Technographics, and MCP.


  glympt-com''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, and 10 more developer resources.'
plans:
- name: Glympt Com Plans Pricing
  plan_count: 4
  slug: glympt-com-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 29.0
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/glympt-com/glympt-com-2026-11-03T132856.png
security:
- kind: authentication
  name: Glympt Com Authentication
  slug: glympt-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Glympt Com Domain Security
  slug: glympt-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: glympt-com
tags:
- Company
- Data Enrichment
- Technographics
- MCP
website: https://glympt.com/
---
