---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
  score: 10.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Cin7 API provides inventory, POS, and ERP integration endpoints as documented on the Swagger page.
  name: Cin7 API
  slug: cin7-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/cin7/plans/cin7-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cin7-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.cin7.com/legal/security/
- group: auth
  href: https://artifacts.apis.io/cin7/security/cin7-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cin7-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cin7/well-known/cin7-academy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cin7-academy-security.txt
- group: agent
  href: https://artifacts.apis.io/cin7/well-known/cin7-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cin7-well-known.yml
- group: other
  href: https://artifacts.apis.io/cin7/hosts/cin7-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cin7-hosts.yml
- group: other
  href: https://artifacts.apis.io/cin7/vendors/cin7-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cin7-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cin7.com/legal/terms-of-use-omni/
- group: operate
  title: ''
  type: Support
  url: https://help.omni.cin7.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cin7.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cin7.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cin7.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.cin7.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://api.cin7.com/api/swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://help.core.cin7.com/hc/en-us/sections/10207278703247-Getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.core.cin7.com/
- group: auth
  href: https://artifacts.apis.io/cin7/security/cin7-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cin7-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cin7/security/cin7-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cin7-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cin7/security/cin7-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cin7-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cin7.com
coverage:
  checked: '2026-10-14'
  detail: Swagger page redirects to a JS‑rendered UI with no raw OpenAPI JSON available.
  evidence:
  - status: 301
    url: https://api.cin7.com/api/swagger
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Cin7 provides cloud‑based inventory management, point‑of‑sale, and enterprise resource planning (ERP) software for small to medium‑sized businesses. The platform integrates with over 700 third‑party applications, offering features such as AI‑driven demand forecasting, multi‑channel sales, B2B portals, and embedded global payments. Cin7 helps retailers, wholesalers, and manufacturers streamline operations, improve visibility across warehouses, and automate financial processes.
layout: provider
modified: '2026-10-14'
name: Cin7
nav: Providers
network: true
overview: 'Cin7 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Inventory, ERP, Retail, and Integration.


  Cin7''s developer surface includes support, pricing, engineering blog, API reference, getting-started guide, documentation, and 14 more developer resources.'
plans:
- name: Cin7 Plans Pricing
  plan_count: 3
  slug: cin7-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 63.4
    operational_transparency: 10.5
  previous_composite: 33.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cin7/cin7-2026-11-03T124143.png
security:
- kind: domain-security
  name: Cin7 Domain Security
  slug: cin7-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cin7 Vulnerability Disclosure
  slug: cin7-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Cin7 Trust Center
  slug: cin7-trust-center
  summary_line: SOC 2
slug: cin7
tags:
- Company
- Inventory
- ERP
- Retail
- Integration
website: https://www.cin7.com
---
