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
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for DayOneLead prospecting and outreach platform
  name: DayOneLead API
  slug: dayonelead-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/dayonelead-com/plans/dayonelead-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dayonelead-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dayonelead-com/conformance/dayonelead-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dayonelead-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dayonelead-com/llms/dayonelead-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dayonelead-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dayonelead-com/well-known/dayonelead-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dayonelead-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dayonelead-com/hosts/dayonelead-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dayonelead-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dayonelead-com/vendors/dayonelead-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dayonelead-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dayonelead.com/terms
- group: auth
  title: ''
  type: Security
  url: https://dayonelead.com/new-york/manhattan/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dayonelead.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dayonelead.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://dayonelead.com/press
- group: start
  title: ''
  type: Login
  url: https://dayonelead.com/login
- group: other
  title: ''
  type: Leadership
  url: https://dayonelead.com/new-york/albany/management
- group: docs
  title: ''
  type: Documentation
  url: https://dayonelead.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Dayonelead
- group: auth
  href: https://artifacts.apis.io/dayonelead-com/security/dayonelead-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dayonelead-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dayonelead.com/
coverage:
  checked: '2026-11-05'
  detail: Documentation pages are rendered via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://dayonelead.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: DayOneLead provides prospecting and outreach software that monitors newly registered businesses across multiple states, researches public contact information, and enables teams to run targeted cold email campaigns at scale. The platform automates lead discovery, data enrichment, and outreach workflows for sales and marketing professionals.
image: https://dayonelead.com/opengraph-image?72a49326bb37561a
layout: provider
modified: '2026-11-05'
name: DayOneLead
nav: Providers
network: true
overview: 'DayOneLead is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Business, Lead Generation, Sales Automation, Marketing, and Software-as-a-Service.


  DayOneLead''s developer surface includes pricing, documentation, and 15 more developer resources.'
plans:
- name: Dayonelead Com Plans Pricing
  plan_count: 2
  slug: dayonelead-com-plans-pricing
random_paper: 18
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 60.7
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dayonelead Com Domain Security
  slug: dayonelead-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dayonelead-com
tags:
- Business
- Lead Generation
- Sales Automation
- Marketing
- Software-as-a-Service
- Company
website: https://dayonelead.com/
---
