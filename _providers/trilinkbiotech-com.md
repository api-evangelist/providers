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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/trilinkbiotech-com/hosts/trilinkbiotech-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trilinkbiotech-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/trilinkbiotech-com/vendors/trilinkbiotech-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trilinkbiotech-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/trilinkbiotech-com/security/trilinkbiotech-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trilinkbiotech-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://go.trilinkbiotech.com/molecular-assemblies
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://go.trilinkbiotech.com/api/mcp
  - status: 200
    url: https://go.trilinkbiotech.com/molecular-assemblies
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Molecular Assemblies, now part of TriLink BioTechnologies, provides synthetic DNA using Fully Enzymatic Synthesis (FES) technology. It produces long, pure single‑stranded oligonucleotides up to 400 bases for applications in therapeutics, vaccines, immunotherapy, agriculture, and nanotechnology, delivering orders without post‑synthesis purification.
layout: provider
modified: '2026-10-24'
name: Molecular Assemblies
nav: Providers
network: true
overview: Molecular Assemblies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include DNA Synthesis, Synthetic DNA, Therapeutics, Vaccines, and Agriculture.
random_paper: 15
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
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 3.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/trilinkbiotech-com/trilinkbiotech-com-2026-11-03T145056.png
security:
- kind: domain-security
  name: Trilinkbiotech Com Domain Security
  slug: trilinkbiotech-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: trilinkbiotech-com
tags:
- DNA Synthesis
- Synthetic DNA
- Therapeutics
- Vaccines
- Agriculture
- Nanotechnology
website: https://go.trilinkbiotech.com/molecular-assemblies
---
