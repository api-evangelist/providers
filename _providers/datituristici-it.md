---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read‑only MCP server exposing nine tourism data tools for Italian municipalities.
  name: DatiTuristici MCP
  slug: datituristici-mcp
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/datituristici-it/llms/datituristici-it-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datituristici-it-llms.txt
- group: other
  href: https://artifacts.apis.io/datituristici-it/hosts/datituristici-it-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datituristici-it-hosts.yml
- group: auth
  href: https://artifacts.apis.io/datituristici-it/security/datituristici-it-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datituristici-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datituristici.it/
- group: docs
  title: ''
  type: APIReference
  url: https://datituristici.it/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://datituristici.it/about
- group: operate
  title: ''
  type: Support
  url: https://datituristici.it/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datituristici.it/termini
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datituristici.it/privacy
created: '2026-11-05'
description: DatiTuristici.it provides institutional tourism data for Italian municipalities. It offers searchable information on arrivals, stays, accommodation capacity, and estimated short‑term rental revenues, sourced from ISTAT and re‑processed. Users can query data per municipality via a web interface or programmatically through a read‑only MCP server exposing nine tools such as cerca_comune and leggi_dati_comune. The service is free, requires no registration, and includes downloadable reports in PDF and Excel formats.
image: https://datituristici.it/logo.png
layout: provider
modified: '2026-11-05'
name: DatiTuristici
nav: Providers
network: true
overview: 'DatiTuristici is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  DatiTuristici''s developer surface includes API reference, getting-started guide, support, and 6 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datituristici It Domain Security
  slug: datituristici-it-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datituristici-it
tags:
- Company
website: https://datituristici.it/
---
