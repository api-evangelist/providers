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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/dinilu-dk/llms/dinilu-dk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dinilu-dk-llms.txt
- group: auth
  href: https://artifacts.apis.io/dinilu-dk/well-known/dinilu-dk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dinilu-dk-security.txt
- group: agent
  href: https://artifacts.apis.io/dinilu-dk/well-known/dinilu-dk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dinilu-dk-well-known.yml
- group: other
  href: https://artifacts.apis.io/dinilu-dk/hosts/dinilu-dk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dinilu-dk-hosts.yml
- group: auth
  href: https://artifacts.apis.io/dinilu-dk/security/dinilu-dk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dinilu-dk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dinilu.dk/
coverage:
  checked: '2026-11-05'
  detail: No public API documentation or machine‑readable contract was found; the only API reference URL https://dinilu.dk/api returns 404.
  evidence:
  - status: 404
    url: https://dinilu.dk/api
  reason: no-developer-program
  state: none
created: '2026-11-05'
description: Dinilu Reklame- & Trykprodukter er en leverandør af kvalitetsreklameprodukter og tryksager fra Fjernøsten, der tilbyder online tilbud på et bredt udvalg af specialfremstillede artikler, firmagaver, merchandise og engangsprodukter. Med fokus på hurtig prisberegning, levering i hele Europa, og høj kvalitet, hjælper de kunder med at designe og bestille produkter med eget logo eller design, leveret direkte til døren fra fabrik, grossist og rederi i én aftale.
image: https://cdn.dinilu.dk/art/dinilu-1200x1200.png
layout: provider
modified: '2026-11-05'
name: Dinilu Reklame- & Trykprodukter
nav: Providers
network: true
overview: Dinilu Reklame- & Trykprodukter is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Print, Merchandise, E-Commerce, and Denmark.
random_paper: 9
score:
  band: minimal
  composite: 4.8
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
    operational_transparency: 10.5
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dinilu Dk Domain Security
  slug: dinilu-dk-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dinilu-dk
tags:
- Advertising
- Print
- Merchandise
- E-Commerce
- Denmark
website: https://dinilu.dk/
---
