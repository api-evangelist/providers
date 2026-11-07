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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/maihem/hosts/maihem-hosts.yml
  title: ''
  type: Hosts
  url: hosts/maihem-hosts.yml
- group: other
  href: https://artifacts.apis.io/maihem/vendors/maihem-vendors.yml
  title: ''
  type: Vendors
  url: vendors/maihem-vendors.yml
- group: auth
  href: https://artifacts.apis.io/maihem/security/maihem-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/maihem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tekton-dynamics.com/
- group: company
  title: ''
  type: Blog
  url: https://tekton-dynamics.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tekton-dynamics.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tekton-dynamics.com/terms
coverage:
  checked: '2026-10-18'
  detail: No API documentation or machine-readable contracts were found on the provider's hosts.
  evidence:
  - status: 503
    url: https://api.maihem.com/openapi.json
  - status: 503
    url: https://api.maihem.com/graphql
  - status: 0
    url: https://api.tekton-dynamics.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-18'
description: Tekton Dynamics provides an AI control layer for welding robots, enabling manufacturers to automate welding without programming. The platform integrates vision and AI to turn any robot into an autonomous expert welder, offering rapid deployment, free automation plans, and support for high-mix production. Founded to address labor shortages and accelerate advanced manufacturing, Tekton Dynamics serves the industrial robotics market with a focus on AI-driven automation and scalability.
image: https://tekton-dynamics.com/assets/og.png
layout: provider
modified: '2026-10-18'
name: MAIHEM
nav: Providers
network: true
overview: 'MAIHEM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Robotics, Automation, Manufacturing, and Welding.


  MAIHEM''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 9.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/maihem/maihem-2026-11-03T135232.png
security:
- kind: domain-security
  name: Maihem Domain Security
  slug: maihem-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: maihem
tags:
- Artificial Intelligence
- Robotics
- Automation
- Manufacturing
- Welding
website: https://tekton-dynamics.com/
---
