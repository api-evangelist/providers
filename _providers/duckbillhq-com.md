---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - security
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/duckbillhq-com/plans/duckbillhq-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/duckbillhq-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/duckbillhq-com/llms/duckbillhq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/duckbillhq-com-llms.txt
- group: other
  href: https://artifacts.apis.io/duckbillhq-com/hosts/duckbillhq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/duckbillhq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/duckbillhq-com/vendors/duckbillhq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/duckbillhq-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.duckbillhq.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.duckbillhq.com/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.duckbillhq.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.duckbillhq.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.duckbillhq.com/blog/
- group: auth
  href: https://artifacts.apis.io/duckbillhq-com/security/duckbillhq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/duckbillhq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.duckbillhq.com
coverage:
  checked: '2026-10-29'
  detail: Duckbill provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.duckbillhq.com
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Duckbill (formerly The Duckbill Group) provides a unified AI and cloud data platform that helps enterprises manage and negotiate cloud and compute contracts. Their Skyway platform offers AI model labs, GPU capacity deals, and hyperscaler contract negotiations, enabling finance, procurement, and engineering teams to forecast costs, secure optimal terms, and maintain cost awareness without sacrificing product velocity. Duckbill combines strategic expertise with a data-driven approach to streamline cloud cost management and AI infrastructure procurement for large organizations.
image: https://www.duckbillhq.com/media/2025/10/dbg-home-og.jpg
layout: provider
modified: '2026-10-29'
name: Duckbill
nav: Providers
network: true
overview: 'Duckbill is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud Cost Management, AI Platform, Enterprise Finance, and Procurement.


  Duckbill''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Duckbillhq Com Plans Pricing
  plan_count: 5
  slug: duckbillhq-com-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 46.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 55.4
    operational_transparency: 7.9
  previous_composite: 20.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/duckbillhq-com/duckbillhq-com-2026-11-03T131111.png
security:
- kind: domain-security
  name: Duckbillhq Com Domain Security
  slug: duckbillhq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: duckbillhq-com
tags:
- Company
- Cloud Cost Management
- AI Platform
- Enterprise Finance
- Procurement
website: https://www.duckbillhq.com
---
