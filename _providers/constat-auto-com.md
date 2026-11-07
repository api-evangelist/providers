---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
- group: agent
  href: https://artifacts.apis.io/constat-auto-com/llms/constat-auto-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/constat-auto-com-llms.txt
- group: other
  href: https://artifacts.apis.io/constat-auto-com/hosts/constat-auto-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/constat-auto-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/constat-auto-com/vendors/constat-auto-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/constat-auto-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/constat-auto-com/security/constat-auto-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/constat-auto-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://constat-auto.com/
coverage:
  checked: '2026-11-04'
  detail: The provider’s website is a JavaScript‑rendered Next.js application with no static OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://constat-auto.com/
  - status: 404
    url: https://api.constat-auto.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Constat Auto provides a free online service to generate a vehicle accident report (constat amiable) in minutes. Users can fill guided forms, sign, and download a PDF to send to their insurer without registration. The platform emphasizes data privacy, storing inputs only locally in the browser, and clarifies that the service does not guarantee insurer decisions. It is a French-language tool aimed at simplifying the creation of legally recognized accident statements.
layout: provider
modified: '2026-11-04'
name: Constat Auto
nav: Providers
network: true
overview: Constat Auto is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Vehicles, Accident, Reporting, PDF, and French.
random_paper: 6
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Constat Auto Com Domain Security
  slug: constat-auto-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: constat-auto-com
tags:
- Vehicles
- Accident
- Reporting
- PDF
- French
website: https://constat-auto.com/
---
