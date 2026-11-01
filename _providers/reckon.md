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
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://help.reckon.com/category/dfwpu8zpfx-reckon-customer-portal-getting-started
- group: agent
  href: https://artifacts.apis.io/reckon/llms/reckon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/reckon-llms.txt
- group: agent
  href: https://artifacts.apis.io/reckon/well-known/reckon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/reckon-well-known.yml
- group: other
  href: https://artifacts.apis.io/reckon/hosts/reckon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/reckon-hosts.yml
- group: other
  href: https://artifacts.apis.io/reckon/vendors/reckon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/reckon-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reckon.com
- group: start
  title: ''
  type: Login
  url: https://community.reckon.com/entry/signin
- group: auth
  href: https://artifacts.apis.io/reckon/security/reckon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reckon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reckon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.reckon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learning.reckon.com/
- group: operate
  title: ''
  type: Support
  url: https://www.reckon.com/au/support/
- group: company
  title: ''
  type: Blog
  url: https://www.reckon.com/au/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reckon.com/au/blog/pricing-models-small-business/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reckon.com/au/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reckon.com/au/privacy/
coverage:
  checked: '2026-10-27'
  detail: Developer portal at https://developer.reckon.com/ serves only JavaScript‑rendered pages with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://developer.reckon.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Reckon provides accounting, business, and bookkeeping software solutions for small businesses in Australia and New Zealand. Their cloud‑based platforms include Reckon One, Reckon Cloud POS, and Reckon Accounts Hosted, offering features such as payroll, invoicing, bank reconciliation, inventory management, and data migration tools. The company emphasizes easy migration from existing systems, comprehensive support resources, and a focus on helping small enterprises streamline financial operations.
image: https://www.reckon.com/au/wp-content/uploads/2024/09/JOB240908-Website-Thumbnail_01.png
layout: provider
modified: '2026-10-27'
name: Reckon
nav: Providers
network: true
overview: 'Reckon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Software, Small Business, Australia, and New Zealand.


  The Reckon catalog on APIs.io includes 1 Spectral governance ruleset.


  Reckon''s developer surface includes getting-started guide, documentation, support, engineering blog, pricing, and 11 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Reckon API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: reckon-rules
scopes:
- name: Reckon Scopes
  scope_count: 0
  slug: reckon-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 31.5
    catalog_earned_first_party: 0.0
    catalog_gap: 83.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 1.7
    developer_ergonomics: 38.1
    discoverability: 48.2
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Reckon Authentication
  slug: reckon-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Reckon Domain Security
  slug: reckon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reckon
tags:
- Accounting
- Software
- Small Business
- Australia
- New Zealand
website: https://reckon.com/
---
