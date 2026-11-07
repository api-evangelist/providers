---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public-company analysis workspace API documented at Capital Workbench Documentation.
  name: Capital Workbench API
  slug: capital-workbench-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/capital-workbench-com/plans/capital-workbench-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/capital-workbench-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/capital-workbench-com/llms/capital-workbench-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capital-workbench-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/capital-workbench-com/well-known/capital-workbench-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/capital-workbench-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/capital-workbench-com/hosts/capital-workbench-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capital-workbench-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/capital-workbench-com/vendors/capital-workbench-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capital-workbench-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capital-workbench.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capital-workbench.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://capital-workbench.com/pricing
- group: start
  title: ''
  type: Login
  url: https://capital-workbench.com/login
- group: auth
  href: https://artifacts.apis.io/capital-workbench-com/security/capital-workbench-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capital-workbench-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capital-workbench.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.capital-workbench.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.capital-workbench.com/user/getting-started/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages are rendered via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.capital-workbench.com/user/getting-started/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Capital Workbench provides a public-company analysis workspace that delivers reasoning and analytics built on publicly available filings and market disclosures. The platform offers corporate finance intelligence, enabling users to explore financial data, performance metrics, and analytical tools for public companies.
layout: provider
modified: '2026-11-04'
name: Capital Workbench
nav: Providers
network: true
overview: 'Capital Workbench is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Analytics, Public Companies, Data, and Platform.


  Capital Workbench''s developer surface includes pricing, documentation, getting-started guide, and 10 more developer resources.'
plans:
- name: Capital Workbench Com Plans Pricing
  plan_count: 3
  slug: capital-workbench-com-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Capital Workbench Com Domain Security
  slug: capital-workbench-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: capital-workbench-com
tags:
- Finance
- Analytics
- Public Companies
- Data
- Platform
website: https://capital-workbench.com/
---
