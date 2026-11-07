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
api_count: 1
apis:
- description: API for Slurp'it network inventory and automation platform.
  name: Slurp'it API
  slug: slurp-it-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/slurpit/plans/slurpit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/slurpit-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/slurpit/llms/slurpit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/slurpit-llms.txt
- group: other
  href: https://artifacts.apis.io/slurpit/hosts/slurpit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/slurpit-hosts.yml
- group: other
  href: https://artifacts.apis.io/slurpit/vendors/slurpit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/slurpit-vendors.yml
- group: auth
  href: https://artifacts.apis.io/slurpit/security/slurpit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/slurpit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://slurpit.io/
- group: company
  title: ''
  type: Blog
  url: https://slurpit.io/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://slurpit.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://slurpit.io/getting-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://slurpit.io/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://slurpit.io/privacy-policy/
coverage:
  checked: '2026-10-19'
  detail: The provider's website offers documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://slurpit.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Slurp'it provides open-source network inventory and automation tools, offering plugins for NetBox and Nautobot, a sandbox environment, and extensive documentation. It helps organizations build a single source of truth for IT infrastructure, supports AI-driven mock data generation, and delivers use cases for network onboarding and security transformation.
image: https://slurpit.io/wp-content/uploads/2025/06/og_logo.jpg
layout: provider
modified: '2026-10-18'
name: Slurp'it
nav: Providers
network: true
overview: 'Slurp''it is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networks, Automation, Open Source, and Documentation.


  Slurp''it''s developer surface includes engineering blog, documentation, getting-started guide, pricing, and 7 more developer resources.'
plans:
- name: Slurpit Plans Pricing
  plan_count: 4
  slug: slurpit-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 20.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/slurpit/slurpit-2026-11-03T143333.png
security:
- kind: domain-security
  name: Slurpit Domain Security
  slug: slurpit-domain-security
  summary_line: TLSv1.3 · DMARC
slug: slurpit
tags:
- Company
- Networks
- Automation
- Open Source
- Documentation
website: https://slurpit.io/
---
