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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/cheapcadtools-com/plans/cheapcadtools-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cheapcadtools-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cheapcadtools-com/llms/cheapcadtools-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cheapcadtools-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cheapcadtools-com/well-known/cheapcadtools-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cheapcadtools-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cheapcadtools-com/hosts/cheapcadtools-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cheapcadtools-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cheapcadtools-com/vendors/cheapcadtools-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cheapcadtools-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cheapcadtools.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cheapcadtools.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://cheapcadtools.com/account/sign-in
- group: auth
  href: https://artifacts.apis.io/cheapcadtools-com/security/cheapcadtools-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cheapcadtools-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cheapcadtools.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://cheapcadtools.com/pricing/
coverage:
  checked: '2026-11-04'
  detail: CheapCADTools provides only a web UI with no public developer documentation or API reference.
  evidence:
  - status: 200
    url: https://cheapcadtools.com/
  reason: no-developer-program
  state: none
created: '2026-11-04'
description: CheapCADTools provides browser‑based parametric CAD tools for designing timing pulleys, roller‑chain sprockets, involute gears, worm gears, bevel gears and planetary gear sets. All generators are live, built to ISO, DIN and ASME standards, and output STL, STEP, DXF or SVG files for 3‑D printing or CNC cutting. The service offers a free tier with limited downloads and paid per‑download pricing, aiming to make precise gear design accessible without installing heavyweight CAD software.
image: https://cheapcadtools.com/assets/img/apps/pulley-page.webp?v=d641d6e09d
layout: provider
modified: '2026-11-04'
name: CheapCADTools
nav: Providers
network: true
overview: 'CheapCADTools is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include CAD, Engineering, Tools, Manufacturing, and Open Source.


  CheapCADTools'' developer surface includes pricing and 10 more developer resources.'
plans:
- name: Cheapcadtools Com Plans Pricing
  plan_count: 4
  slug: cheapcadtools-com-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
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
  name: Cheapcadtools Com Domain Security
  slug: cheapcadtools-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cheapcadtools-com
tags:
- CAD
- Engineering
- Tools
- Manufacturing
- Open Source
website: https://cheapcadtools.com/
---
