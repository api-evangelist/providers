---
agent_readiness:
  band: human-only
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
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: The StockTrim developer portal provides API documentation for inventory planning and forecasting operations.
  name: StockTrim API
  slug: stocktrim-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/stocktrim/plans/stocktrim-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stocktrim-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/stocktrim/conventions/stocktrim-conventions.yml
  title: ''
  type: Conventions
  url: conventions/stocktrim-conventions.yml
- group: auth
  href: https://artifacts.apis.io/stocktrim/authentication/stocktrim-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stocktrim-authentication.yml
- group: other
  href: https://artifacts.apis.io/stocktrim/hosts/stocktrim-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stocktrim-hosts.yml
- group: other
  href: https://artifacts.apis.io/stocktrim/vendors/stocktrim-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stocktrim-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://go.stocktrim.com/Account/Login
- group: auth
  href: https://artifacts.apis.io/stocktrim/security/stocktrim-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stocktrim-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stocktrim.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.stocktrim.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.stocktrim.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.stocktrim.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://stocktrim.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.stocktrim.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stocktrim.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stocktrim.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stocktrim.com/privacy-policy
coverage:
  checked: '2026-10-28'
  detail: Docs pages are rendered via JavaScript, preventing machine‑readable extraction.
  evidence:
  - status: 200
    url: https://www.stocktrim.com/getting-started
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: StockTrim provides inventory planning and forecasting software that helps businesses predict future inventory needs, optimize working capital, and reduce errors in spreadsheet-based forecasting. The platform offers features such as demand forecasting, integration with ERP and accounting systems, and industry-specific solutions for manufacturing, wholesale, retail, and e‑commerce. Trusted by small and medium enterprises worldwide, StockTrim aims to improve supply chain efficiency and support data‑driven decision making.
image: https://www.stocktrim.com/hubfs/Warehouse%20worker%20and%20manager%20looking%20at%20laptop%20in%20a%20large%20warehouse-1.jpeg
jsonld:
- class_count: 33
  name: Stocktrim Context
  property_count: 164
  slug: stocktrim-context
layout: provider
modified: '2026-10-27'
name: StockTrim
nav: Providers
network: true
overview: 'StockTrim publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Inventory, Forecasting, Supply-Chain, and SaaS.


  The StockTrim catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  StockTrim''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Stocktrim Plans Pricing
  plan_count: 2
  slug: stocktrim-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: StockTrim API Rules
  rule_count: 8
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 0
  slug: stocktrim-rules
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.8
    catalog_earned_first_party: 8.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 15.9
    contract_quality: 14.7
    developer_ergonomics: 50.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Stocktrim Authentication
  slug: stocktrim-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Stocktrim Domain Security
  slug: stocktrim-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stocktrim
tags:
- Company
- Inventory
- Forecasting
- Supply-Chain
- SaaS
website: https://stocktrim.com/
---
