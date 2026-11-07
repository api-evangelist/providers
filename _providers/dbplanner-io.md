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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: DB Planner offers database planning services but does not expose a public API.
  name: DB Planner API
  slug: db-planner-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/dbplanner-io/plans/dbplanner-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dbplanner-io-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dbplanner-io/llms/dbplanner-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dbplanner-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/dbplanner-io/well-known/dbplanner-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dbplanner-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/dbplanner-io/hosts/dbplanner-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dbplanner-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/dbplanner-io/vendors/dbplanner-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dbplanner-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dbplanner-io/security/dbplanner-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dbplanner-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dbplanner.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://dbplanner.io/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://dbplanner.io/features
- group: operate
  title: ''
  type: Support
  url: https://dbplanner.io/faq
coverage:
  checked: '2026-11-05'
  detail: No public API documentation or machine‑readable contract was found on the provider's sites.
  evidence:
  - status: 200
    url: https://console.dbplanner.io/
  reason: not-a-software-company
  state: none
created: '2026-11-05'
description: 'dbplanner-io is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://dbplanner.io/og/default.png
layout: provider
modified: '2026-11-05'
name: DB Planner
nav: Providers
network: true
overview: 'DB Planner is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Database Diagram, ER Diagram, DBML, Real-Time Collaboration, and SQL Import.


  DB Planner''s developer surface includes pricing, getting-started guide, support, and 7 more developer resources.'
plans:
- name: Dbplanner Io Plans Pricing
  plan_count: 3
  slug: dbplanner-io-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dbplanner Io Domain Security
  slug: dbplanner-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dbplanner-io
tags:
- Database Diagram
- ER Diagram
- DBML
- Real-Time Collaboration
- SQL Import
- Code Export
- AI Design
website: https://dbplanner.io/
---
