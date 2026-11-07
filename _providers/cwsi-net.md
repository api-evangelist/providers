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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
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
  score: 0.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Airline fare classes, mileage calculators, great circle distance and airport lounges.
  name: cwsi.net API
  slug: cwsi-net-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/cwsi-net/plans/cwsi-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cwsi-net-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cwsi-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cwsi-net/conformance/cwsi-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cwsi-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cwsi-net/llms/cwsi-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cwsi-net-llms.txt
- group: other
  href: https://artifacts.apis.io/cwsi-net/hosts/cwsi-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cwsi-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/cwsi-net/vendors/cwsi-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cwsi-net-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cwsi.net/terms/
- group: operate
  title: ''
  type: Support
  url: https://cwsi.net/help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cwsi.net/privacy/
- group: start
  title: ''
  type: Login
  url: https://cwsi.net/login/
- group: start
  title: ''
  type: GettingStarted
  url: https://cwsi.net/mcp/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.cwsi.net</code
- group: docs
  title: ''
  type: APIReference
  url: https://cwsi.net/developers/
- group: auth
  href: https://artifacts.apis.io/cwsi-net/security/cwsi-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cwsi-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cwsi.net/
created: '2026-11-04'
description: CWSI provides flight tracking, fare class charts, delay information, and lounge access tools for airlines. The platform offers real‑time flight status, airport details, and airline‑specific services, targeting travelers and aviation enthusiasts. It aggregates data from multiple carriers and presents it via a web interface and APIs.
image: https://cwsi.net/images/og-cwsi-2026.jpg
layout: provider
modified: '2026-11-04'
name: CWSI
nav: Providers
network: true
overview: 'CWSI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Aviation, Flight Tracking, Travel, Data API, and Airlines.


  CWSI''s developer surface includes support, getting-started guide, API reference, and 12 more developer resources.'
plans:
- name: Cwsi Net Plans Pricing
  plan_count: 3
  slug: cwsi-net-plans-pricing
random_paper: 18
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.1
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cwsi Net Domain Security
  slug: cwsi-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: cwsi-net-api
  slug: cwsi-net-api
slug: cwsi-net
tags:
- Aviation
- Flight Tracking
- Travel
- Data API
- Airlines
website: https://cwsi.net/
---
