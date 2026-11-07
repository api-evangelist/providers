---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
- description: BriefMe MCP provides meeting timer integration and setup documentation.
  name: BriefMe MCP
  slug: briefme-mcp
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/briefme-us/plans/briefme-us-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/briefme-us-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/briefme-us/authentication/briefme-us-authentication.yml
  title: ''
  type: Authentication
  url: authentication/briefme-us-authentication.yml
- group: design
  href: https://artifacts.apis.io/briefme-us/conformance/briefme-us-conformance.yml
  title: ''
  type: Conformance
  url: conformance/briefme-us-conformance.yml
- group: agent
  href: https://artifacts.apis.io/briefme-us/llms/briefme-us-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/briefme-us-llms.txt
- group: agent
  href: https://artifacts.apis.io/briefme-us/well-known/briefme-us-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/briefme-us-well-known.yml
- group: other
  href: https://artifacts.apis.io/briefme-us/hosts/briefme-us-hosts.yml
  title: ''
  type: Hosts
  url: hosts/briefme-us-hosts.yml
- group: other
  href: https://artifacts.apis.io/briefme-us/vendors/briefme-us-vendors.yml
  title: ''
  type: Vendors
  url: vendors/briefme-us-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://briefme.us/terms
- group: operate
  title: ''
  type: Support
  url: https://briefme.us/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://briefme.us/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://briefme.us/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://briefme.us/press
- group: start
  title: ''
  type: Login
  url: https://briefme.us/login
- group: start
  title: ''
  type: GettingStarted
  url: https://briefme.us/docs/mcp
- group: auth
  href: https://artifacts.apis.io/briefme-us/security/briefme-us-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/briefme-us-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://briefme.us/
coverage:
  detail: Docs are rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://briefme.us/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: BriefMe provides a free, no‑signup meeting timer that lets participants share a live countdown agenda across phones, laptops, and room screens. It helps keep meetings on schedule, preventing topics from running over time. Users can create timed agendas, share a single link, and integrate the timer into Zoom, Google Meet, or Teams calls. The service is SaaS‑based, focused on productivity and meeting efficiency.
image: https://briefme.us/images/og.png
layout: provider
modified: '2026-11-03'
name: BriefMe
nav: Providers
network: true
overview: 'BriefMe is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Timer, Meetings, Productivity, Software-as-a-Service, and Free.


  BriefMe''s developer surface includes authentication, support, pricing, getting-started guide, and 12 more developer resources.'
plans:
- name: Briefme Us Plans Pricing
  plan_count: 3
  slug: briefme-us-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 58.0
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Briefme Us Authentication
  slug: briefme-us-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Briefme Us Domain Security
  slug: briefme-us-domain-security
  summary_line: TLSv1.3 · HSTS
slug: briefme-us
tags:
- Timer
- Meetings
- Productivity
- Software-as-a-Service
- Free
website: https://briefme.us/
---
