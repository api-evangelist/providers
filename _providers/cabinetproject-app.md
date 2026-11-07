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
    mcp_server: documented
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
  score: 24.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/cabinetproject-app/llms/cabinetproject-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cabinetproject-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/cabinetproject-app/well-known/cabinetproject-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cabinetproject-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/cabinetproject-app/hosts/cabinetproject-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cabinetproject-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/cabinetproject-app/vendors/cabinetproject-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cabinetproject-app-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cabinetproject.app/login
- group: start
  title: ''
  type: Login
  url: https://api.cabinetproject.app/login
- group: docs
  title: ''
  type: Documentation
  url: https://dev.cabinetproject.app/
- group: auth
  href: https://artifacts.apis.io/cabinetproject-app/security/cabinetproject-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cabinetproject-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cabinetproject.app/
- group: company
  title: ''
  type: Blog
  url: https://cabinetproject.app/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://cabinetproject.app/#pricing
- group: operate
  title: ''
  type: Support
  url: https://cabinetproject.app/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cabinetproject.app/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cabinetproject.app/privacy/
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite public documentation pages.
  evidence:
  - status: 404
    url: https://api.cabinetproject.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Design Master Solutions LLC provides software for US RTA and semi‑custom cabinet dealers and installer crews. It offers quoting by SKU and multiplier, kitchen layout drawing, order management, delivery verification, install routing, punch‑list tracking, and QuickBooks sync, with a 14‑day free trial and tiered pricing plans.
image: https://cabinetproject.app/assets/logo-horizontal-1200.png
layout: provider
modified: '2026-11-03'
name: Design Master Solutions LLC
nav: Providers
network: true
overview: 'Design Master Solutions LLC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cabinet Software, Quoting, Dealer Tools, and QuickBooks Integration.


  Design Master Solutions LLC''s developer surface includes documentation, engineering blog, pricing, support, and 10 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 39.3
    operational_transparency: 7.9
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cabinetproject App Domain Security
  slug: cabinetproject-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cabinetproject-app
tags:
- Cabinet Software
- Quoting
- Dealer Tools
- QuickBooks Integration
website: https://cabinetproject.app/
---
