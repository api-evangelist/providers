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
- group: agent
  href: https://artifacts.apis.io/ecoexperten-com/llms/ecoexperten-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ecoexperten-com-llms.txt
- group: other
  href: https://artifacts.apis.io/ecoexperten-com/hosts/ecoexperten-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecoexperten-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ecoexperten-com/vendors/ecoexperten-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ecoexperten-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ecoexperten-com/security/ecoexperten-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecoexperten-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ecoexperten.com/
coverage:
  checked: '2026-11-06'
  detail: The provider's website offers consulting services but provides no public API documentation or machine‑readable contracts.
  evidence:
  - status: 200
    url: https://ecoexperten.com/
  reason: no-developer-program
  state: none
created: '2026-11-06'
description: ecoExperten provides certified energy consulting across Germany, offering services such as energy performance certificates (Energieausweis), iSFP, QNG-Audit, and GEG compliance documentation. They guide clients from the initial inquiry through project completion, ensuring sustainable building practices. Contact via info@ecoexperten.com for personalized advice.
image: https://ecoexperten.com/hero-vor-ort.png
layout: provider
modified: '2026-11-06'
name: ecoExperten
nav: Providers
network: true
overview: ecoExperten is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Consulting, Sustainability, Germany, and Certification.
random_paper: 14
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ecoexperten Com Domain Security
  slug: ecoexperten-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ecoexperten-com
tags:
- Energy
- Consulting
- Sustainability
- Germany
- Certification
- Company
website: https://ecoexperten.com/
---
