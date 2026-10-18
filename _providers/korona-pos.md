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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for KORONA POS platform, providing access to POS functions and data.
  name: KORONA POS API
  slug: korona-pos-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/korona-pos/refs/heads/main/plans/korona-pos-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/korona-pos-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/korona-pos/refs/heads/main/llms/korona-pos-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/korona-pos-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/korona-pos/refs/heads/main/well-known/korona-pos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/korona-pos-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/korona-pos/refs/heads/main/hosts/korona-pos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/korona-pos-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/korona-pos/refs/heads/main/vendors/korona-pos-vendors.yml
  title: ''
  type: Vendors
  url: vendors/korona-pos-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://koronapos.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://koronapos.com/privacy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://koronapos.com/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://manual.koronapos.com/category/setup-guides
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/korona-pos/refs/heads/main/security/korona-pos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/korona-pos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://koronapos.com
- group: docs
  title: ''
  type: Documentation
  url: https://manual.koronapos.com/
- group: docs
  title: ''
  type: APIReference
  url: https://manual.koronapos.com/category/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://koronapos.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://koronapos.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://manual.koronapos.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://koronapos.com/schedule-a-demo/
- group: start
  title: ''
  type: Login
  url: https://www.koronacloud.com/web/login
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://koronapos.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: KORONA POS provides an all‑in‑one cloud‑based point‑of‑sale platform for retail, hospitality, and specialty stores. It offers inventory management, employee scheduling, CRM, e‑commerce integration, loyalty programs, and robust reporting tools. The solution supports multi‑location businesses, integrates with major payment processors, and includes a developer API for custom extensions and third‑party integrations.
image: https://koronapos.com/wp-content/uploads/2025/07/KORONA-POS-by-COMBASE-A-trusted-point-of-sale-solution-made-to-improve-your-business.-.png
layout: provider
modified: '2026-10-13'
name: KORONA POS
nav: Providers
network: true
overview: 'KORONA POS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Point-of-Sale, Retail, and Hospitality.


  KORONA POS''s developer surface includes getting-started guide, documentation, API reference, pricing, engineering blog, support, signup flow, and 11 more developer resources.'
plans:
- name: Korona Pos Plans Pricing
  plan_count: 8
  slug: korona-pos-plans-pricing
random_paper: 21
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Korona Pos Domain Security
  slug: korona-pos-domain-security
  summary_line: TLSv1.3 · DMARC
slug: korona-pos
tags:
- Company
- Point-of-Sale
- Retail
- Hospitality
website: https://koronapos.com
---
