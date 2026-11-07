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
api_count: 1
apis:
- description: Public website provides no developer documentation or API specifications.
  name: Amber Therapeutics API
  slug: amber-therapeutics-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/amber-therapeutics/hosts/amber-therapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amber-therapeutics-hosts.yml
- group: other
  href: https://artifacts.apis.io/amber-therapeutics/vendors/amber-therapeutics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amber-therapeutics-vendors.yml
- group: auth
  href: https://artifacts.apis.io/amber-therapeutics/security/amber-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amber-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amber-tx.com/
coverage:
  checked: '2026-10-26'
  detail: No public developer documentation or API specifications were found on the company's website.
  evidence:
  - status: 200
    url: https://ambertherapeutics.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Amber Therapeutics is a biotechnology company focused on developing innovative therapies for metabolic and cardiovascular diseases. Leveraging cutting‑edge gene editing and RNA‑based platforms, Amber aims to create precision medicines that address the underlying causes of disease. The company collaborates with academic institutions and industry partners to advance its pipeline from preclinical research through clinical trials, with a commitment to safety, efficacy, and patient‑centric outcomes. Amber Therapeutics is backed by leading venture investors and operates from its headquarters in Austin, Texas, serving a global research community.
layout: provider
modified: '2026-10-25'
name: Amber Therapeutics
nav: Providers
network: true
overview: Amber Therapeutics is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Gene Editing, RNA Therapeutics, and Metabolic Diseases.
random_paper: 13
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 4.0
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
screenshot: https://apis.io/screenshots/amber-therapeutics/amber-therapeutics-2026-11-03T120806.png
security:
- kind: domain-security
  name: Amber Therapeutics Domain Security
  slug: amber-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amber-therapeutics
tags:
- Company
- Biotechnology
- Gene Editing
- RNA Therapeutics
- Metabolic Diseases
- Cardiovascular
website: https://www.amber-tx.com/
---
