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
    agent_skills: unknown
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
  score: 3.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/atlass-os-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/atlass-os-com/plans/atlass-os-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/atlass-os-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/atlass-os-com/llms/atlass-os-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atlass-os-com-llms.txt
- group: other
  href: https://artifacts.apis.io/atlass-os-com/hosts/atlass-os-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlass-os-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/atlass-os-com/vendors/atlass-os-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlass-os-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Atlass-OS
- group: auth
  href: https://artifacts.apis.io/atlass-os-com/security/atlass-os-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlass-os-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlass-os.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.atlass-os.com/login
- group: company
  title: ''
  type: Blog
  url: https://atlass-os.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://atlass-os.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atlass-os.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://atlass-os.com/founding
coverage:
  checked: '2026-11-02'
  detail: No API documentation or machine-readable contract found after probing common spec URLs and documentation paths.
  evidence:
  - status: 404
    url: https://atlass-os.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: 'ATLASS OS — the business operating system for trades and field-service companies, on one ledger, one timeline and one API: CRM with every call, text and email on one timeline, estimates and invoices, jobs and Boards, full double-entry books, Canadian payroll, a business phone system with transcribed call recordings, and field apps for your crew — one system, one ledger. Built in Alberta.'
image: https://atlass-os.com/_cdn/static/atlass-network-sphere-cropped.png
layout: provider
modified: '2026-11-01'
name: ATLASS OS
nav: Providers
network: true
overview: 'ATLASS OS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Trade, Field Service Management, CRM, and Payroll.


  ATLASS OS''s developer surface includes engineering blog, pricing, getting-started guide, and 10 more developer resources.'
plans:
- name: Atlass Os Com Plans Pricing
  plan_count: 5
  slug: atlass-os-com-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 18.3
    discoverability: 39.3
    operational_transparency: 2.6
  previous_composite: 20.7
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atlass Os Com Domain Security
  slug: atlass-os-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atlass-os-com
tags:
- Trade
- Field Service Management
- CRM
- Payroll
website: https://atlass-os.com/
---
